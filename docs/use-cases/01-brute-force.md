# Use case 1: Brute force, then success

> Learning lab. Synthetic sign-ins only.

**Story:** someone tries 37 passwords against one account from an IP in a known Tor exit range, then gets in.
Sentinel detects it, a playbook confirms the IP is bad and raises the severity, Shuffle opens a TheHive case,
an analyst closes it as a true positive, and the close is mirrored back to Sentinel.

| Piece | File |
|---|---|
| Generator | [`data/generators/make_signins.py`](../../data/generators/make_signins.py) |
| Table schema sample | [`data/schema/signins.sample.json`](../../data/schema/signins.sample.json) |
| DCR transform | [`sentinel/dcr/signins-transform.kql`](../../sentinel/dcr/signins-transform.kql) |
| Ingest workflow | [`logic-apps/ingest-signins/workflow.json`](../../logic-apps/ingest-signins/workflow.json) |
| Detection | [`sentinel/analytics/brute-force-then-success.kql`](../../sentinel/analytics/brute-force-then-success.kql) |
| Playbook | `la-pb-ip-enrich`: [step 4](../04-playbooks.md) |
| SOAR | [step 5](../05-shuffle-thehive.md) |

## What viewers learn

- ResultType 50126 (bad password) vs 0 (success): real Entra ID codes in a fake dataset
- A KQL `join` that only fires when the success comes **after** the failures
- Why the rule's severity is Medium and the playbook raises it
- Why automation rules trigger on "created" only (mirroring loops)
- Fetch → de-duplicate → case → close → mirror, built by hand in an open-source SOAR
