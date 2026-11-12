# Step 3 — Detections (analytics rules)

> Learning lab.

Create both as **Scheduled query rules** (Defender portal → Microsoft Sentinel → Configuration → Analytics → Create).

## Rule 1: Brute force followed by successful sign-in (Lab)

Query: [`sentinel/analytics/brute-force-then-success.kql`](../sentinel/analytics/brute-force-then-success.kql)

| Setting | Value |
|---|---|
| Severity | **Medium** (the playbook raises it, which looks good on camera) |
| Tactic | Credential Access (T1110) |
| Entities | Account → FullName = `UserPrincipalName`; IP → Address = `IPAddress` |
| Custom details | `FailedCount` |
| Alert title | `Brute force then success for {{UserPrincipalName}} from {{IPAddress}}` |
| Schedule | Every 5 minutes, look back 1 hour |
| Suppression | **On, 1 hour** (otherwise the same rows re-alert every run) |
| Incident settings | Create incidents; group alerts matching Account and IP |

## Rule 2: PII exposure by data location (Lab)

Query: [`sentinel/analytics/pii-exposure-by-location.kql`](../sentinel/analytics/pii-exposure-by-location.kql)
Background: [use case 2](use-cases/02-pii-exposure.md)

| Setting | Value |
|---|---|
| Event grouping | **Trigger an alert for each event** (one row = one data location) |
| Alert details override | Severity from column **`Severity`**; title `PII exposure on {{DataStore}} ({{StoreType}})` |
| Entities | Account → FullName = `Owner`; Host → HostName = `DataStore`; File → Name = `SampleFile` |
| Custom details | `RiskScore`, `TotalRecords`, `PIITypes`, `Exposures`, `Files` |
| Schedule | Every 5 minutes, look back 1 hour |
| Suppression | On, 1 hour |
| Incident settings | Create incidents; alert grouping **off** |

Use **Test with current data** in the wizard to show the results on camera. Scheduled rules have no "run now",
so send the CSV about five minutes before you cut to the incident queue.

## Expected results

| Use case | Incidents |
|---|---|
| 1 | 1 incident, Medium (High after the playbook) |
| 2 | 6 incidents: 2 High, 2 Medium, 1 Low, 1 Informational (run `make_pii_findings.py` to print the expected list) |
