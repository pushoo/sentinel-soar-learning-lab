# Video series: shot lists

> Learning series on the *CISSP Coffee Shot* channel. Say "learning lab, synthetic data" in every episode.

## Episode 0: Prerequisites: build a free SOC lab (7-9 min)

Full script: [videos/ep00-prerequisites-script.md](videos/ep00-prerequisites-script.md)

## Episode 1: Set up your lab, step by step (about 5 min)

Script and cue card: [videos/ep01-setup-your-lab-script.md](videos/ep01-setup-your-lab-script.md)

## Episode 2: Turn on Microsoft Sentinel (about 4 min)

Script: [videos/ep02-sentinel-workspace-script.md](videos/ep02-sentinel-workspace-script.md)

## Later episodes (split into short parts when recorded)

### Brute force, end to end

| Time | Scene | On screen | Key line |
|---|---|---|---|
| 0:00-0:30 | Hook | Sentinel incident Closed by Shuffle, next to the TheHive case | "Real incident, open-source SOAR. Here's the whole build." |
| 0:30-1:30 | Architecture | README diagram | "Sentinel detects, Logic Apps ingest and enrich, Shuffle and TheHive orchestrate." |
| 1:30-3:00 | Data | Generator, custom table wizard, DCR transform | "Transform before you pay to store it." |
| 3:00-4:30 | Ingest | Logic App code view, `curl` POST, run history, `take 10` | "The old connector is retired. Here's the supported way." |
| 4:30-6:00 | Detect | KQL, entity mapping, test results | "Brute force, then a success, from the same IP." |
| 6:00-7:30 | Automate | Incident, playbook run, severity jump, Teams post | "The playbook raised it to High on its own." |
| 7:30-10:00 | Orchestrate | Shuffle workflow, de-duplication, TheHive case, analyst closes it | "Shuffle moves it, TheHive holds it." |
| 10:00-10:45 | Mirror | Sentinel incident Closed, TruePositive, comment trail | "Closed in one place, closed everywhere." |
| 10:45-11:30 | Rules + CTA | "Give every field one owner", repo link | "Everything is on GitHub." |

### PII exposure with severity ranges

| Time | Scene | On screen | Key line |
|---|---|---|---|
| 0:00-0:30 | Hook | Six TheHive cases, four severities, from one CSV | "Same pipeline, different question: how bad is this exposure?" |
| 0:30-2:00 | The scoring model | Weight tables and ranges | "Records × sensitivity × exposure." |
| 2:00-3:30 | Data + ingest | `make_pii_findings.py` printing the expected result, POST | "We know the answer before Sentinel does. Now let's check it." |
| 3:30-5:30 | Detection | KQL `datatable` + `case()`, alert details override | "Severity comes from the query, not a fixed setting." |
| 5:30-7:00 | Routing | `la-pb-pii-route` Switch by severity | "High tells privacy now. Low waits for review." |
| 7:00-9:30 | Cases | TheHive "PII Exposure" template, due dates, privacy-officer task | "Automation routes it; a human decides if it's reportable." |
| 9:30-10:30 | Wrap | Expected vs actual table | "Tune the weights with your privacy team." |

## Shorts

- The 30-second attack timeline from Episode 1
- "Records × sensitivity × exposure" explained in 45 seconds
- "Why one passport scan on a public link is High"
