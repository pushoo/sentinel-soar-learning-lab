# Episode 06: The playbook (automation rule + Logic App)

> Learning lab, synthetic data only. About 3.5 minutes. Builds on [Episode 05](ep05-detection-rule-script.md).
> Names on screen: watchlist `BadIPs`, playbook `la-pb-ip-enrich`, automation rule `Enrich brute-force incidents (Lab)`, resource group `rg-soc-lab`.
> Guide: [Step 4: Playbooks](../04-playbooks.md).

## Before you record

- Watchlist file: `sentinel/watchlists/BadIPs.csv` (search key `IP`).
- Workflow: `playbooks/la-pb-ip-enrich/workflow.json`. Replace `<your-subscription-id>` in `$connections` with your own before you paste it (keep that copy out of Git).
- Fresh data: run `la-ingest-signins` with a new CSV from `data/generators/make_signins.py`, so the detection rule (1-hour lookback) fires again.
- Blur in the edit: subscription ID, object IDs, tenant ID (it also shows in Chrome's link preview).

## Permissions this episode needs

1. The playbook's managed identity: **Microsoft Sentinel Responder** on `rg-soc-lab` (read and update incidents).
2. Sentinel itself: permission to run playbooks in `rg-soc-lab` (Automation, Create automation rule, Manage playbook permissions).
   If granting fails, add the **Microsoft Sentinel Automation Contributor** role on `rg-soc-lab` for the **Azure Security Insights** app in Access control (IAM).

## Narration


### Open

- **s01** Last time, Sentinel raised an incident on its own. Today, that incident starts its own response.
- **s02** We build a playbook that checks the incident's IP address against a list of known bad addresses, and an automation rule that runs it the moment the incident is created.
- **s03** This is a learning lab, with synthetic data only.
- **s04** Here's the plan. A watchlist of bad IPs, a playbook that reads it, and a rule that starts the playbook. The incident comes out enriched, with nobody touching it.

### 1 · Watchlist

- **s05** First, the list. In Sentinel, open Watchlist, and select New.
- **s06** Name it BadIPs, with the alias BadIPs.
- **s07** Upload the CSV from the repo, and pick IP as the search key.
- **s08** Review, and create. Two lab addresses, ready for lookups.

### 2 · Playbook

- **s09** Now the playbook. Open Automation, Create, then Logic App playbook, with the incident trigger.
- **s10** Our lab resource group, the name la-pb-ip-enrich, in Canada Central.
- **s11** It connects to Sentinel with its own managed identity. No passwords, no keys.
- **s12** Review, and create. Then open it in the Azure portal.

### 2 · Playbook (workflow)

- **s13** Open code view, and paste the workflow from the repo, under playbooks.
- **s14** The designer shows the steps. The incident trigger starts it.
- **s15** It reads the BadIPs watchlist, then the IP addresses on the incident, and keeps the ones on both.
- **s16** If there's a match, it raises the severity to High, adds two tags, and writes a comment that says why. If not, it leaves a short note.
- **s17** Publish. Saved.

### 3 · Permission

- **s18** The playbook needs one permission. On the resource group, open Access control, and Add role assignment.
- **s19** Microsoft Sentinel Responder. It can update incidents, and nothing more.
- **s20** Members: Managed identity, then our playbook. Review and assign.

### 4 · Automation rule

- **s21** Now the trigger. Back in Defender, open Automation, Create, Automation rule.
- **s22** A standard rule, a clear name, and the trigger: when an incident is created.
- **s23** Condition: the analytics rule is our brute force rule.
- **s24** Action: run a playbook. Sentinel also needs permission to run playbooks in our resource group, so tick it here, and grant.
- **s25** Pick la-pb-ip-enrich. The warning badge can lag behind that permission. Create.
- **s26** The rule is active.

### 5 · Test

- **s27** Time to test. Fresh sign-ins go in, the same way as last episode. Status 202.
- **s28** The detection rule runs every five minutes, so we wait.
- **s29** There it is. Incident two, and it arrived at High, not Medium.
- **s30** Open it. Tagged auto-enriched, and malicious IP.
- **s31** And the comment: the attacker's IP is on the BadIPs watchlist, so the severity went from Medium to High.
- **s32** Nobody touched it. The playbook did the triage on its own.

### Close

- **s33** Recap: a watchlist, a playbook with its own identity, one role, and a rule that runs it.
- **s34** One tip: if granting playbook permissions fails, give the Azure Security Insights app the Microsoft Sentinel Automation Contributor role on the resource group.
- **s35** Everything is in the repo. Next episode, Shuffle and TheHive, so every incident becomes a case automatically.

## Result

Incident 2 arrives already at **High**, tagged `malicious-ip` and `auto-enriched`, with a comment from the playbook: the attacker IP is on the BadIPs watchlist, severity raised from Medium to High.
