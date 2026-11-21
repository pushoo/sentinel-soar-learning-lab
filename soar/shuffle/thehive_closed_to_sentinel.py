# Shuffle step: TheHive case closed -> close the matching Sentinel incident (CISSP Coffee Shot lab)
import json, uuid, requests
TENANT = "<tenant-id>"
CLIENT = "<client-id>"
SECRET = "$client_secret"
SUB = "<subscription-id>"
HIVE = "http://<vm-private-ip>:9000"
HIVE_KEY = "$thehive_api_key"
API = "2024-03-01"
base = ("https://management.azure.com/subscriptions/" + SUB + "/resourceGroups/rg-soc-lab"
        "/providers/Microsoft.OperationalInsights/workspaces/law-soc-lab/providers/Microsoft.SecurityInsights")
hv = {"Authorization": "Bearer " + HIVE_KEY}
# TheHive closing status -> Sentinel classification and reason
cls = {"TruePositive": ("TruePositive", "SuspiciousActivity"),
       "FalsePositive": ("FalsePositive", "IncorrectAlertLogic")}

# 1. TheHive cases from Sentinel that are closed but not mirrored yet
cases = requests.post(HIVE + "/api/v1/query", headers=hv, timeout=30, json={"query": [
    {"_name": "listCase"}, {"_name": "page", "from": 0, "to": 200}]}).json()
todo = [c for c in cases if c.get("stage") == "Closed" and "sentinel" in c.get("tags", [])
        and "sentinel-closed" not in c.get("tags", [])]
done = []
if todo:
    tok = requests.post("https://login.microsoftonline.com/" + TENANT + "/oauth2/v2.0/token", data={
        "grant_type": "client_credentials", "client_id": CLIENT, "client_secret": SECRET,
        "scope": "https://management.azure.com/.default"}, timeout=30).json()["access_token"]
    az = {"Authorization": "Bearer " + tok}
    incs = requests.get(base + "/incidents", headers=az, params={"api-version": API}, timeout=30).json().get("value", [])
for c in todo:
    num = [t for t in c["tags"] if t.startswith("sentinel-") and t[9:].isdigit()]
    inc = [i for i in incs if num and str(i["properties"]["incidentNumber"]) == num[0][9:]]
    if not inc:
        continue
    name = inc[0]["name"]
    classification, reason = cls.get(c.get("status"), ("Undetermined", None))
    note = "Closed from TheHive case #" + str(c["number"]) + " (" + str(c.get("status")) + "): " + (c.get("summary") or "no summary")
    # 2. Fresh GET for the etag, then close the Sentinel incident
    cur = requests.get(base + "/incidents/" + name, headers=az, params={"api-version": API}, timeout=30).json()
    props = {"title": cur["properties"]["title"], "severity": cur["properties"]["severity"], "status": "Closed",
             "classification": classification, "classificationComment": note,
             "labels": [l for l in cur["properties"].get("labels", []) if l.get("labelType") == "User"]}
    if reason:
        props["classificationReason"] = reason
    r = requests.put(base + "/incidents/" + name, headers=az, params={"api-version": API}, timeout=30,
                     json={"etag": cur["etag"], "properties": props})
    requests.put(base + "/incidents/" + name + "/comments/" + str(uuid.uuid4()), headers=az,
                 params={"api-version": API}, json={"properties": {"message": note}}, timeout=30)
    # 3. Mark the TheHive case as mirrored so it is not processed again
    if r.ok:
        requests.patch(HIVE + "/api/v1/case/" + c["_id"], headers=hv, timeout=30,
                       json={"tags": c["tags"] + ["sentinel-closed"]})
    done.append({"thehive_case": c["number"], "sentinel": int(num[0][9:]), "closed": r.ok, "as": classification})

print(json.dumps({"mirrored": len(done), "cases": done}))
