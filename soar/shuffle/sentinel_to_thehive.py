# Shuffle step: new Microsoft Sentinel incidents become TheHive cases (CISSP Coffee Shot lab)
import json, uuid, requests
D = chr(36)  # dollar sign, so Shuffle does not treat OData options as variables
TENANT = "<tenant-id>"
CLIENT = "<client-id>"
SECRET = "$client_secret"
SUB = "<subscription-id>"
HIVE = "http://<vm-private-ip>:9000"
HIVE_KEY = "$thehive_api_key"
API = "2024-03-01"
base = ("https://management.azure.com/subscriptions/" + SUB + "/resourceGroups/rg-soc-lab"
        "/providers/Microsoft.OperationalInsights/workspaces/law-soc-lab/providers/Microsoft.SecurityInsights")

tok = requests.post("https://login.microsoftonline.com/" + TENANT + "/oauth2/v2.0/token", data={
    "grant_type": "client_credentials", "client_id": CLIENT, "client_secret": SECRET,
    "scope": "https://management.azure.com/.default"}, timeout=30).json()["access_token"]
az = {"Authorization": "Bearer " + tok}
hv = {"Authorization": "Bearer " + HIVE_KEY}
sev = {"Informational": 1, "Low": 1, "Medium": 2, "High": 3}

# 1. Sentinel incidents still New (anything we handled is set to Active, so no duplicates)
r = requests.get(base + "/incidents", headers=az, timeout=30, params={
    "api-version": API, D + "filter": "properties/status eq 'New'",
    D + "orderby": "properties/createdTimeUtc desc", D + "top": "5"})
r.raise_for_status()
done = []
for inc in r.json().get("value", []):
    p = inc["properties"]
    n = p["incidentNumber"]
    # 2. Create the TheHive case
    body = {"title": p["title"],
            "description": p.get("description", "") + "\n\nSentinel incident #" + str(n) + ": " + p.get("incidentUrl", ""),
            "severity": sev.get(p["severity"], 2),
            "tags": ["sentinel", "sentinel-" + str(n)]}
    if p["title"].startswith("PII exposure"):
        body["caseTemplate"] = "PII Exposure"
        if "override" in p.get("description", ""):
            body["severity"] = 4   # Critical: high-risk PII on a shared or public location
    case = requests.post(HIVE + "/api/v1/case", headers=hv, timeout=30, json=body).json()
    # 3. Entities become observables
    ents = requests.post(base + "/incidents/" + inc["name"] + "/entities", headers=az,
                         params={"api-version": API}, timeout=30)
    for e in (ents.json().get("entities", []) if ents.ok else []):
        k, q = e.get("kind"), e.get("properties", {})
        obs = None
        if k == "Ip" and q.get("address"):
            obs = {"dataType": "ip", "data": q["address"]}
        elif k == "Account" and q.get("accountName"):
            obs = {"dataType": "mail", "data": q["accountName"] + "@" + q["upnSuffix"]} if q.get("upnSuffix") \
                else {"dataType": "other", "data": q["accountName"]}
        elif k == "Host" and q.get("hostName"):
            obs = {"dataType": "hostname", "data": q["hostName"]}
        if obs:
            requests.post(HIVE + "/api/v1/case/" + case["_id"] + "/observable", headers=hv, json=obs, timeout=30)
    # 4. Comment on the Sentinel incident and set it to Active
    msg = "TheHive case #" + str(case["number"]) + " opened by Shuffle (learning lab)."
    requests.put(base + "/incidents/" + inc["name"] + "/comments/" + str(uuid.uuid4()), headers=az,
                 params={"api-version": API}, json={"properties": {"message": msg}}, timeout=30)
    cur = requests.get(base + "/incidents/" + inc["name"], headers=az, params={"api-version": API}, timeout=30).json()
    cp = cur["properties"]
    requests.put(base + "/incidents/" + inc["name"], headers=az, params={"api-version": API}, timeout=30, json={
        "etag": cur["etag"], "properties": {"title": cp["title"], "severity": cp["severity"], "status": "Active",
                                            "labels": [l for l in cp.get("labels", []) if l.get("labelType") == "User"]}})
    done.append({"sentinel": n, "thehive_case": case["number"], "title": p["title"]})

print(json.dumps({"processed": len(done), "cases": done}))
