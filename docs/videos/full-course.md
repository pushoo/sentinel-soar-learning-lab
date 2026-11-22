# Full course: all parts in one video

> CISSP Coffee Shot, Sentinel + SOAR learning lab. Learning lab, synthetic data only. About 32 minutes.
> ▶ **Watch:** [https://youtu.be/JT4phZDic5Q](https://youtu.be/JT4phZDic5Q) · 📺 Playlist: [Microsoft Sentinel for Beginners (Sentinel 101)](https://www.youtube.com/playlist?list=PLYyAEoIo5XUE) · [CISSP Coffee Shot channel](https://www.youtube.com/@CISSP-COFFEE-SHOT)

It opens with why a home lab and hands-on learning help, then plays every episode, from the prerequisites to the PII use case, back to back, and closes with how to learn by doing. Each episode ends with its own "Next" card, which leads into the next chapter. The Bonus (Microsoft Sentinel 101) plays after Episode 03, right before the Logic App, so the brute-force story runs in order.

## Chapters

| Time | Chapter | Script |
|---|---|---|
| 0:00 | Why hands-on learning and a home lab | [README: why a home lab](../../README.md#why-a-home-lab-and-why-hands-on) |
| 0:30 | Ep00 Prerequisites: build a free SOC lab | [script](ep00-prerequisites-script.md) |
| 3:17 | Ep01 Set up your lab | [script](ep01-setup-your-lab-script.md) |
| 5:40 | Ep02 Turn on Microsoft Sentinel | [script](ep02-sentinel-workspace-script.md) |
| 8:14 | Ep03 The custom table and its transform | [script](ep03-custom-table-script.md) |
| 10:26 | Bonus: Microsoft Sentinel 101 | [video series](../video-series.md) |
| 12:11 | Ep04 The Logic App that sends the CSV in | [script](ep04-logic-app-ingest-script.md) |
| 15:32 | Ep05 The detection rule | [script](ep05-detection-rule-script.md) |
| 18:19 | Ep06 Automation rule and playbook | [script](ep06-playbook-script.md) |
| 21:39 | Ep07a The SOAR box: TheHive and Shuffle | [script](ep07a-soar-box-script.md) |
| 24:52 | Ep07b Sentinel to TheHive, and back | [script](ep07b-sentinel-to-thehive-script.md) |
| 27:24 | Ep08 PII exposure with severity ranges | [script](ep08-pii-exposure-script.md) |
| 31:19 | Why this playbook works: learn by doing | [README: why a home lab](../../README.md#why-a-home-lab-and-why-hands-on) |

## What you build

1. A Sentinel workspace on the free trial
2. A custom table with a KQL transform
3. A Logic App that ingests a CSV through the Logs Ingestion API
4. A detection rule that raises an incident on its own
5. A playbook that enriches the incident and raises its severity
6. TheHive and Shuffle on one small Azure VM
7. Sentinel incidents that become TheHive cases, with closures synced back to Sentinel
8. A second use case: PII exposure with severity ranges

How each piece links, from the CSV to TheHive: [csv-to-thehive.md](../csv-to-thehive.md)

Next: the full brute-force dry run, end to end, then cleanup ([step 6](../06-dry-run-and-cleanup.md)).
