# Episode 5: The detection rule: query in, incident out

> CISSP Coffee Shot, Sentinel + SOAR learning lab. Learning lab, synthetic data only. About 3 minutes.

Turns the brute-force query into a scheduled analytics rule that raises an incident on its own, with the user and the IP mapped as entities.

## Before you record

- Episodes 2 to 4 done: `SignInDemo_CL` exists and the Logic App `la-ingest-signins` accepts the CSV.
- Send fresh data first (Run with payload). The rule looks back one hour.
- Query: [`sentinel/analytics/brute-force-then-success.kql`](../../sentinel/analytics/brute-force-then-success.kql). Settings: [docs/03-detections.md](../03-detections.md).

## Rule settings shown

| Setting | Value |
|---|---|
| Name | Brute force followed by successful sign-in (Lab) |
| Severity | Medium |
| MITRE | Credential Access, T1110 Brute force |
| Entities | Account (FullName → UserPrincipalName), IP (Address → IPAddress) |
| Custom details | FailedCount |
| Schedule | Every 5 minutes, look back 1 hour |
| Alert | One alert for each result; stop running for 1 hour after an alert |
| Incidents | Create incidents from alerts: Enabled |

## Narration

| Time | Section | Line |
|---|---|---|
| 0:00 | Intro | Last time, our sign-ins landed in Sentinel. Today, Sentinel watches them for us. |
| 0:05 | Intro | We turn our brute force query into a scheduled detection rule that raises an incident on its own. |
| 0:11 | Intro | This is a learning lab, with synthetic data only. |
| 0:14 | Intro | Here's the plan. Fresh sign-ins go in, a rule checks them every five minutes, and an incident comes out, with the user and the IP already attached. |
| 0:24 | Fresh data | First, fresh data. The rule only looks back one hour, so we send the CSV in again. |
| 0:30 | Fresh data | Run with payload, paste the sample, and run it. Status 202, rows sent. |
| 0:36 | Rule basics | In Defender, open Microsoft Sentinel, then Analytics. No rules yet. |
| 0:41 | Rule basics | Create, then Scheduled query rule. |
| 0:43 | Rule basics | Give it a clear name: Brute force followed by successful sign-in. Add a short description of what it catches. |
| 0:49 | Rule basics | Severity: Medium. Tactic: Credential Access, technique T1110, brute force. |
| 0:56 | Rule logic | Next, the rule logic. Paste the query from the repo. |
| 1:00 | Rule logic | It counts failed sign-ins per user and address over the last hour. |
| 1:05 | Rule logic | If one address fails twenty times or more, and then a sign-in from that same address succeeds, that's our alert. |
| 1:12 | Rule logic | View query results. One row: Alex, thirty-seven failures, from Germany. The logic works. |
| 1:19 | Entities | Now, entity mapping. This tells Sentinel what our columns mean. |
| 1:24 | Entities | An Account, from UserPrincipalName. |
| 1:26 | Entities | And an IP address, from IPAddress. |
| 1:30 | Entities | A custom detail carries FailedCount into the alert, so the analyst sees the number right away. |
| 1:36 | Schedule and save | Scheduling: run every five minutes, and look back one hour. |
| 1:40 | Schedule and save | One alert for each result. Then stop for an hour after an alert, so one attack doesn't flood the queue. |
| 1:46 | Schedule and save | Incident settings: create incidents from these alerts. That's the switch that puts it in front of an analyst. |
| 1:53 | Schedule and save | Review and create. Validation passed. Save. |
| 1:56 | Schedule and save | The rule is live, and enabled. |
| 1:59 | The incident | Now we wait for the first run. Here, it fired within a minute of saving. |
| 2:03 | The incident | There it is. Incident one, severity Medium, status New. |
| 2:07 | The incident | Open it. Under assets: the user, alex. |
| 2:11 | The incident | Under evidence: the attacker's IP address. |
| 2:14 | The incident | And the alert carries our query results: thirty-seven failures, the first and last fail, from Germany. |
| 2:21 | The incident | Nobody ran a query. The rule caught the attack on its own. |
| 2:25 | Wrap | Recap: a query, mapped entities, a five-minute schedule, and an incident on its own. |
| 2:32 | Wrap | One tip: if no incident shows up, check that your data is less than an hour old, and wait for the next run. |
| 2:39 | Wrap | Everything is in the repo. Next episode, an automation rule and a playbook, so this incident starts a response by itself. |

## Result

Incident 1, Medium, New: user `alex@lab.example`, IP `185.220.101.45`, 37 failures from Germany (DE). The rule fired within a minute of saving.

## If no incident shows up

- Check the data is less than an hour old (`SignInDemo_CL | summarize max(TimeGenerated)`).
- Wait for the next 5-minute run, and check the rule is Enabled.
