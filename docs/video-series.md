# Video series: shot lists

> Learning series on the *CISSP Coffee Shot* channel. Say "learning lab, synthetic data" in every episode.

## Episode 0: Prerequisites: build a free SOC lab (7-9 min)

Full script: [videos/ep00-prerequisites-script.md](videos/ep00-prerequisites-script.md)

## Episode 1: Set up your lab, step by step (about 5 min)

Script and cue card: [videos/ep01-setup-your-lab-script.md](videos/ep01-setup-your-lab-script.md)

## Episode 2: Turn on Microsoft Sentinel (about 4 min)

Script: [videos/ep02-sentinel-workspace-script.md](videos/ep02-sentinel-workspace-script.md)

## Episode 3: The custom table and its transform (about 4 min)

Script: [videos/ep03-custom-table-script.md](videos/ep03-custom-table-script.md)

## Episode 4: The Logic App that sends the CSV in (about 3.5 min)

Script and recording plan: [videos/ep04-logic-app-ingest-script.md](videos/ep04-logic-app-ingest-script.md)

## Episode 5: The detection rule: query in, incident out (about 3 min)

Script and recording plan: [videos/ep05-detection-rule-script.md](videos/ep05-detection-rule-script.md)

## Bonus: Microsoft Sentinel 101, by example (about 3 min)

Collect, detect, investigate, respond, explained with one brute-force story.

Watch the **Sentinel 101** playlist: [https://www.youtube.com/playlist?list=PLYyAEoIo5XUE](https://www.youtube.com/playlist?list=PLYyAEoIo5XUE)

1. [Ep01 What is Microsoft Sentinel? SIEM explained](https://youtu.be/bky22YoXBSE)
2. [Ep02 Log Analytics workspace and Sentinel pricing](https://youtu.be/Zn8vIYr_MZI)
3. [Ep03 Connect data: Content hub and data connectors](https://youtu.be/1DaMubbs-4Q)
4. [Ep04 KQL for beginners: catch a brute-force attack](https://youtu.be/GHgq_vHCI54)
5. [Ep05 Build your first detection rule](https://youtu.be/yIxAG7yS1I4)
6. [Ep06 Investigate an incident step by step](https://youtu.be/28lvzVzgyEM)
7. [Ep07 Automation rules vs playbooks vs workbooks](https://youtu.be/HNaWbUkwQTg)
8. [Ep08 Build your first playbook (SOAR)](https://youtu.be/SYzhfloBA58)
9. [Ep09 Build a workbook dashboard with KQL](https://youtu.be/qkf5jS9THj4)
10. [Ep10 What's next for Sentinel, plus lab cleanup](https://youtu.be/slo-I0ywUzY)
11. [Full course: Microsoft Sentinel SIEM and SOAR, free SOC lab (32 min)](https://youtu.be/JT4phZDic5Q)

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
