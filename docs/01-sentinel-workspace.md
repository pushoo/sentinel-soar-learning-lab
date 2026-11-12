# Step 1 — Sentinel workspace, custom tables and DCRs

> Learning lab. Lab subscription only.

## 1.1 Workspace and Sentinel

```bash
az monitor log-analytics workspace create -g rg-soc-lab -n law-soc-lab -l canadacentral
```

Then in the portal: **Microsoft Sentinel → Create → law-soc-lab → Add**. The free-trial banner should appear.

Connect the workspace to the **Microsoft Defender portal** and do the Sentinel work there. Sentinel's Azure-portal
experience is being retired, so recordings made in the Defender portal stay current longer.

## 1.2 Custom tables (one per use case)

Portal: **Log Analytics workspace → Tables → Create → New custom log (DCR-based)**.

| Use case | Table name (portal adds `_CL`) | New DCR | Sample file | Transform |
|---|---|---|---|---|
| 1 | `SignInDemo` | `dcr-signin-demo` | `data/schema/signins.sample.json` | `sentinel/dcr/signins-transform.kql` |
| 2 | `PIIFindings` | `dcr-pii-findings` | `data/schema/pii_findings.sample.json` | `sentinel/dcr/pii-transform.kql` |

Create a data collection endpoint (DCE) if the wizard asks for one.

> On camera: the transform is "filter and reshape before you pay to store it".

## 1.3 Collect the ingestion details

You need the **immutable ID** and the **logs ingestion endpoint** for each DCR.

```bash
az monitor data-collection rule show -g rg-soc-lab -n dcr-signin-demo \
  --query "{immutableId: immutableId, endpoint: endpoints.logsIngestion}" -o table
# If your DCR uses a DCE, take the endpoint from the DCE instead:
az monitor data-collection endpoint show -g rg-soc-lab -n <dce-name> --query "logsIngestion.endpoint" -o tsv
```

Ingestion URL format:

```
{endpoint}/dataCollectionRules/{immutableId}/streams/Custom-SignInDemo_CL?api-version=2023-01-01
{endpoint}/dataCollectionRules/{immutableId}/streams/Custom-PIIFindings_CL?api-version=2023-01-01
```

## Done when

- [ ] Sentinel is enabled on `law-soc-lab`
- [ ] `SignInDemo_CL` and `PIIFindings_CL` exist
- [ ] You have both ingestion URLs written down (keep them out of git)
