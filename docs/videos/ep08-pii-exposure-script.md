# Episode 08: PII exposure, with severity ranges

> CISSP Coffee Shot, Sentinel + SOAR learning lab. Learning lab, synthetic data only. About 4.1 minutes.
> Use case: [PII exposure](../use-cases/02-pii-exposure.md).

## Before you record

- Table `PIIFindings_CL` on `dce-soc-lab`, Logic App `la-ingest-pii`, playbook `la-pb-pii-route`.
- Query: [`sentinel/analytics/pii-exposure-by-location.kql`](../../sentinel/analytics/pii-exposure-by-location.kql). Rules through the Sentinel API: [`scripts/create-pii-rules.sh`](../../scripts/create-pii-rules.sh) (the Analytics and Automation pages now open in the Defender portal).
- Playbook: [`logic-apps/pb-pii-route/workflow.json`](../../logic-apps/pb-pii-route/workflow.json). TheHive case template "PII Exposure" with three tasks.
- Synthetic data only: the findings say where fake PII was found and contain no PII. A person decides whether a breach is reportable.

## Narration

| Time | Line |
|---|---|
| 0:00 | So far, our lab catches attackers. Today, a privacy problem: personal data sitting in the wrong place. |
| 0:07 | A PII scan finds data on laptops, file shares, SharePoint, OneDrive and blob storage. |
| 0:14 | This is a learning lab, with synthetic data only. |
| 0:17 | Here's the plan. Findings go into a new table. A rule scores each location, and the score sets the severity. A playbook routes it, and TheHive opens a case from a template. |
| 0:29 | The score is simple: records, times a weight for the type of PII, times a weight for how exposed it is. |
| 0:36 | A credit card number weighs ten, a phone number one. Public weighs ten, private one. |
| 0:42 | Then ranges: under 100 is informational, up to 1,000 is low, up to 10,000 is medium, and above that is high. |
| 0:51 | One override: card numbers, SINs, passports or health cards on a shared or public link are always high. |
| 1:00 | First, the table. In the workspace, create a custom log called PIIFindings. |
| 1:06 | It needs a data collection rule, so we create a new one, and pick the endpoint from Episode 3. |
| 1:12 | Upload a sample file. Azure reads the columns, and their types, from it. |
| 1:16 | Review and create. The table and its rule are ready. |
| 1:20 | The rule's JSON shows its immutable ID and the stream name. The ingest app needs both. |
| 1:27 | Next, the ingest Logic App: la-ingest-pii, on the consumption plan, in our resource group. |
| 1:34 | In code view, paste the workflow from the repo. It takes a CSV, turns each line into a row, and posts the rows to the ingestion API. |
| 1:43 | It signs in with its own managed identity, so turn the identity on. |
| 1:48 | Then, on the data collection rule, give that identity one role: Monitoring Metrics Publisher. |
| 1:53 | Now run it with the CSV from the generator. Eight findings across six locations. Status 202, and the run succeeded. |
| 2:02 | Next, routing. Sentinel's automation pages now open in the Defender portal, so we build the playbook as a Logic App. |
| 2:11 | la-pb-pii-route: a Sentinel incident trigger, then a switch on severity. |
| 2:18 | High gets the pii-high tag and a 4-hour target. Medium gets 48 hours. Everything else waits for review. |
| 2:27 | Azure wants unique action names in every branch, so each branch gets its own suffix. |
| 2:33 | Its identity gets Microsoft Sentinel Responder on the resource group, so it can tag and comment. |
| 2:40 | Now the detection rule, and the automation rule that runs the playbook. Their pages moved too, so we use the Sentinel API from Cloud Shell. |
| 2:50 | One script: the scoring query, every 5 minutes, one alert per location, with the severity read from the query. |
| 2:57 | Both rules are in. The detection rule runs every 5 minutes, and the automation rule runs the playbook. |
| 3:04 | Last, TheHive. Case templates need the org-admin profile, so as admin, we give the analyst org-admin. |
| 3:12 | Then, as the analyst, create the template: PII Exposure. |
| 3:17 | A title prefix, medium by default, a pii tag, and three tasks: confirm the data, let the privacy officer decide if it's reportable, and contain it. |
| 3:30 | Within minutes, six cases arrive, each one built from the template. |
| 3:34 | The public blob and the shared passport scan are critical. The override worked. |
| 3:39 | In Sentinel: two high, two medium, one low and one informational. Exactly what the generator predicted. |
| 3:45 | And every incident carries the playbook's tag. |
| 3:49 | Recap: a table, an ingest app, a scoring rule, a routing playbook, and a case template. |
| 3:55 | Everything is in the repo. Next episode: a full dry run, then cleanup. |
