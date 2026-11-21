# Episode 07b: Sentinel to TheHive, and back

> CISSP Coffee Shot, Sentinel + SOAR learning lab. Learning lab, synthetic data only. About 2.6 minutes.
> Guide: [Step 5: Shuffle + TheHive](../05-shuffle-thehive.md).

## Before you record

- Episode 07a done: TheHive on port 9000, Shuffle on port 3001, a TheHive service account with an API key.
- Python steps: [`soar/shuffle/sentinel_to_thehive.py`](../../soar/shuffle/sentinel_to_thehive.py) and [`soar/shuffle/thehive_closed_to_sentinel.py`](../../soar/shuffle/thehive_closed_to_sentinel.py). Keep the secrets in workflow variables, not in the code.
- App registration `shuffle-sentinel-lab` with Microsoft Sentinel Responder on `law-soc-lab`. The client secret is shown once: blur it.
- Blur in the edit: tenant ID, client ID, client secret, TheHive API key, VM public IP.

## Narration

| Time | Line |
|---|---|
| 0:00 | Last time we built TheHive and Shuffle. Today, Sentinel incidents become TheHive cases on their own. |
| 0:07 | And when an analyst closes the case, Sentinel closes the incident too. |
| 0:12 | This is a learning lab, with synthetic data only. |
| 0:15 | Here's the plan. Shuffle asks Sentinel for new incidents every minute, opens a case in TheHive, and mirrors the close back. |
| 0:24 | Shuffle needs its own identity in Azure. In Entra ID, register an app: shuffle-sentinel-lab. |
| 0:30 | Give it one role, Microsoft Sentinel Responder, on our workspace only. |
| 0:35 | It can read and update incidents, and nothing else. |
| 0:39 | Shuffle has a Sentinel app, but it wants an interactive Microsoft sign-in. For a service, we call the Sentinel API directly, with the app's own credentials. |
| 0:48 | So in Shuffle, create a workflow: Sentinel to TheHive. |
| 0:52 | Secrets go in workflow variables, never in the code. |
| 0:56 | One holds the API key from TheHive's service account. |
| 0:59 | The other holds a new client secret from the app registration. Azure shows it once, so copy it straight across. |
| 1:08 | Now one Python step does the work. |
| 1:10 | It gets a token, and lists Sentinel incidents that are still New. |
| 1:15 | For each one, it opens a case in TheHive, and adds the IP addresses and accounts as observables. |
| 1:20 | Then it comments on the incident, and sets it to Active. Active means handled, so no duplicates. |
| 1:27 | Run it. Two incidents, two cases. |
| 1:29 | A schedule runs it every 60 seconds. |
| 1:32 | In Sentinel: zero New, two Active. |
| 1:35 | And on the incident, Shuffle's comment: TheHive case 1 opened. |
| 1:40 | Now the way back. A second step looks for TheHive cases that an analyst closed. |
| 1:46 | It closes the matching Sentinel incident with the same verdict, and marks the case, so it only happens once. |
| 1:54 | Let's try it. As the analyst, open case 1. The IP and the account came straight from Sentinel. |
| 2:00 | Close it as a true positive, with impact, and a short summary. |
| 2:04 | Within a minute, Shuffle's next run picks it up. Mirrored: case 1, incident 2, true positive. |
| 2:10 | And in Sentinel, incident 2 is closed. True positive, suspicious activity, with the analyst's summary. |
| 2:17 | Closed in one place, closed everywhere. |
| 2:20 | Recap: an app with one role, two secrets in variables, and two steps on a schedule. |
| 2:26 | The code is in the repo. Next episode, a new use case: PII exposure, with severity ranges. |
