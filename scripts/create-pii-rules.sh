# Ep08: the PII detection rule and its automation rule, through the Sentinel API
# (the Analytics and Automation pages now open in the Defender portal)
SUB=$(az account show --query id -o tsv); TEN=$(az account show --query tenantId -o tsv)
WS="/subscriptions/$SUB/resourceGroups/rg-soc-lab/providers/Microsoft.OperationalInsights/workspaces/law-soc-lab/providers/Microsoft.SecurityInsights"
RULE="$WS/alertRules/pii-exposure-by-location"
cat > rule.json <<'JSON'
{
  "kind": "Scheduled",
  "properties": {
    "displayName": "PII exposure by data location (Lab)",
    "description": "One incident per data location. Severity comes from the risk-score range (CISSP Coffee Shot learning lab, synthetic data).",
    "severity": "Medium",
    "enabled": true,
    "query": "let typeWeight = datatable(PIIType:string, W:int)[\n    \"Email\",1, \"Phone\",1, \"Address\",2, \"DOB\",3, \"DriversLicence\",5,\n    \"Passport\",8, \"HealthCard\",8, \"SIN\",10, \"CreditCard\",10];\nlet exposureWeight = datatable(Exposure:string, E:int)[\n    \"Private\",1, \"Internal\",2, \"SharedLink\",5, \"Public\",10];\nlet highRiskTypes = dynamic([\"SIN\",\"CreditCard\",\"Passport\",\"HealthCard\"]);\nPIIFindings_CL\n| where TimeGenerated > ago(1h)\n| lookup kind=leftouter typeWeight on PIIType\n| lookup kind=leftouter exposureWeight on Exposure\n| extend RowScore = RecordCount * coalesce(W, 1) * coalesce(E, 1),\n         ForceHigh = PIIType in (highRiskTypes) and Exposure in (\"Public\", \"SharedLink\")\n| summarize RiskScore = sum(RowScore), TotalRecords = sum(RecordCount),\n            Files = dcount(FilePath), PIITypes = make_set(PIIType),\n            Exposures = make_set(Exposure), ForceHigh = max(toint(ForceHigh)),\n            SampleFile = take_any(FilePath)\n    by DataStore, StoreType, Owner\n| extend Severity = case(ForceHigh == 1 or RiskScore >= 10000, \"High\",\n                         RiskScore >= 1000, \"Medium\",\n                         RiskScore >= 100, \"Low\",\n                         \"Informational\")\n| extend Reason = strcat(\"Risk score \", tostring(RiskScore), \" (records x PII weight x exposure weight)\",\n                         iff(ForceHigh == 1, \". High-risk PII on a shared or public location: override to High.\", \".\"))",
    "queryFrequency": "PT5M",
    "queryPeriod": "PT1H",
    "triggerOperator": "GreaterThan",
    "triggerThreshold": 0,
    "suppressionDuration": "PT1H",
    "suppressionEnabled": true,
    "tactics": [
      "Exfiltration"
    ],
    "eventGroupingSettings": {
      "aggregationKind": "AlertPerResult"
    },
    "alertDetailsOverride": {
      "alertDisplayNameFormat": "PII exposure on {{DataStore}} ({{StoreType}})",
      "alertDescriptionFormat": "{{Reason}}",
      "alertSeverityColumnName": "Severity"
    },
    "customDetails": {
      "RiskScore": "RiskScore",
      "TotalRecords": "TotalRecords",
      "PIITypes": "PIITypes",
      "Exposures": "Exposures",
      "Files": "Files"
    },
    "entityMappings": [
      {
        "entityType": "Account",
        "fieldMappings": [
          {
            "identifier": "FullName",
            "columnName": "Owner"
          }
        ]
      },
      {
        "entityType": "Host",
        "fieldMappings": [
          {
            "identifier": "HostName",
            "columnName": "DataStore"
          }
        ]
      },
      {
        "entityType": "File",
        "fieldMappings": [
          {
            "identifier": "Name",
            "columnName": "SampleFile"
          }
        ]
      }
    ],
    "incidentConfiguration": {
      "createIncident": true,
      "groupingConfiguration": {
        "enabled": false,
        "reopenClosedIncident": false,
        "lookbackDuration": "PT5H",
        "matchingMethod": "AllEntities"
      }
    }
  }
}
JSON
az rest --method put --url "https://management.azure.com$RULE?api-version=2024-03-01" --body @rule.json --query "{name:properties.displayName, enabled:properties.enabled, every:properties.queryFrequency}" -o table
cat > auto.json <<JSON
{"properties": {"displayName": "Route PII incidents", "order": 2,
  "triggeringLogic": {"isEnabled": true, "triggersOn": "Incidents", "triggersWhen": "Created",
    "conditions": [{"conditionType": "Property", "conditionProperties": {"propertyName": "IncidentRelatedAnalyticRuleIds", "operator": "Contains", "propertyValues": ["$RULE"]}}]},
  "actions": [{"order": 1, "actionType": "RunPlaybook", "actionConfiguration": {"tenantId": "$TEN",
    "logicAppResourceId": "/subscriptions/$SUB/resourceGroups/rg-soc-lab/providers/Microsoft.Logic/workflows/la-pb-pii-route"}}]}}
JSON
az rest --method put --url "https://management.azure.com$WS/automationRules/route-pii-incidents?api-version=2024-03-01" --body @auto.json --query "{name:properties.displayName, runs:properties.actions[0].actionType}" -o table
