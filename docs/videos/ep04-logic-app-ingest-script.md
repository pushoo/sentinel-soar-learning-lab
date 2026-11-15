# Episode 04: The Logic App that sends the CSV in

> Learning lab, synthetic data only. Target length about 3.5 minutes. Builds on [Episode 03](ep03-custom-table-script.md).
> Names used on screen: Logic App `la-ingest-signins`, DCR `dcr-signin-demo`, DCE `dce-soc-lab`, table `SignInDemo_CL`.
> Guide: [Step 2: Logic App 1: ingest the CSV](../02-ingest-logic-app.md).

## Before you record

- Workflow: `logic-apps/ingest-signins/workflow.json`. Put your logs ingestion address and DCR immutable ID into `ingestionUrl` before you paste it (keep that filled-in copy out of Git).
- Sample data: `python3 data/generators/make_signins.py` writes 58 sign-ins, including 37 failed attempts on one user from one IP in Germany.
- Blur in the edit: subscription ID, DCR immutable ID, and the trigger URL (it carries a signature).

## Recording plan (one Chrome window, Claude drives, you record)

| Take | What happens on screen | Lines |
|---|---|---|
| A | Logic apps > Create > Consumption, Multi-tenant. `rg-soc-lab`, `la-ingest-signins`, Canada Central. Review + create, Create, Go to resource | s06-s10 |
| B | Identity > System assigned > On > Save > Yes. The object ID appears | s12-s13 |
| C | `dcr-signin-demo` > Access control (IAM) > Add role assignment > Monitoring Metrics Publisher > Managed identity > Logic app > `la-ingest-signins` > Review + assign | s15-s18 |
| D | Logic app code view: paste the workflow, Save. Then the designer: the six steps | s19-s26 |
| E | Run > Run with payload: paste the CSV, Run. Output 202 and `rowsSent: 58`. Open the run: every step green, the ingestion call returns 204 | s27-s31 |
| F | Defender > Advanced hunting: `SignInDemo_CL | where TimeGenerated > ago(30m) | take 10`, then the failed sign-ins query | s32-s35 |

Graphics only: hook, "Data Collector API is out" card, the plan diagram, managed identity card, least privilege card, recap, outro.
B-roll: someone hammering a keyboard (password guessing), an alarm clock (the first-ingestion wait).

## Queries shown

```kql
SignInDemo_CL
| where TimeGenerated > ago(30m)
| take 10
```

```kql
SignInDemo_CL
| where TimeGenerated > ago(30m)
| where ResultType != 0
| summarize FailedAttempts = count() by UserPrincipalName, IPAddress, Location
| where FailedAttempts >= 5
```

## Narration

Final narration, as it is in the published video.

**Hook**
- s01 Our table is ready. Today we fill it.
- s02 We build a Logic App that takes a CSV file and sends every row into Sentinel.
- s03 This is a learning lab, with synthetic data only.
- s04 The old Data Collector API lost its support in September 2026, so we use the supported way: the Logs Ingestion API.
- s05 Here's the plan. The CSV goes to the Logic App, the Logic App sends the rows to our endpoint, and the data collection rule writes them into our table.

**Create the Logic App**
- s06 In the portal, open Logic apps, and select Create.
- s07 Pick Consumption, multi-tenant. You pay per run, and a few lab runs cost next to nothing.
- s08 Our lab resource group, the name la-ingest-signins, and Canada Central, the same region as the workspace.
- s09 Review and create, then Create.
- s10 Deployment complete. Go to the resource.

**Managed identity**
- s11 Now, how does the Logic App prove who it is? No passwords, no keys. We give it a managed identity.
- s12 Open Identity, switch System assigned to On, and save.
- s13 Azure registers it in Entra ID and gives it an object ID. Think of it as a staff badge for the app.

**One permission, one resource**
- s14 A badge alone opens nothing. So we give it one permission, on one resource.
- s15 Open the data collection rule, Access control, and Add role assignment.
- s16 Search for Monitoring Metrics Publisher. That's the role allowed to send data through this rule.
- s17 Members: Managed identity, then pick our Logic App.
- s18 Review and assign. Least privilege: it can write through this one rule, and nothing else.

**The workflow**
- s19 Now the workflow itself. Open Logic app code view.
- s20 Paste the workflow from the repo, under logic-apps, ingest-signins, and save.
- s21 The designer shows the steps.
- s22 A request trigger receives the CSV.
- s23 Lines splits it into rows and skips the header. Non empty lines drops the blank ones.
- s24 Rows maps each line to our eight columns.
- s25 Then one HTTP call sends them all to the Logs Ingestion API, signed in with the managed identity.
- s26 And the response tells us how many rows went in.

**Test it**
- s27 Time to test. Run with payload, and paste the sample CSV: fifty-eight sign-ins.
- s28 Hidden in there: someone trying Alex's password over and over, from one address in Germany.
- s29 Run it. Status 202, and fifty-eight rows sent.
- s30 Open the run. Every step is green.
- s31 And the ingestion call came back 204: accepted.

**Proof in Defender**
- s32 Now the proof. In Defender, open Advanced hunting.
- s33 SignInDemo_CL, the last thirty minutes, take ten. Our rows are there.
- s34 One more query: failed sign-ins, counted by user and address, five or more.
- s35 One row. Alex, thirty-seven failures, one IP, in Germany. That's a brute force attack, and now we can see it.

**Wrap**
- s36 One tip: the first data into a new table can take up to fifteen minutes. If you see nothing, wait, and run it again.
- s37 Recap: a Logic App with its own identity, one role on the rule, and a CSV that lands in Sentinel.
- s38 Everything is in the repo. Next episode, we turn that query into a detection rule that raises an incident on its own.

## On-screen evidence

- Data Collector API: Azure Updates, "Azure Monitor Data Collection API Retirement" (retirement on 14 September 2026; move to the Logs Ingestion API).
- Role: Microsoft Learn, "Logs Ingestion API in Azure Monitor" (the sender needs Monitoring Metrics Publisher on the DCR).
