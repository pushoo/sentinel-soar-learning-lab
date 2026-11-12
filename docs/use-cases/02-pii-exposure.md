# Use case 2 — PII exposure across laptops and cloud, with severity ranges

> Learning lab. The generator describes *where* fake PII was "found"; it contains no PII.

**Story:** a PII scan finds personal data on laptops, file shares, SharePoint, OneDrive and Azure Blob storage and
exports the findings as a CSV. Each **data location** becomes one incident and one case, and its **severity comes
from a risk-score range**.

## Risk score

**Risk score = RecordCount × PII type weight × exposure weight**, summed across a data location's findings.

| PII type | Weight |
|---|---|
| Email, Phone | 1 |
| Address | 2 |
| DOB | 3 |
| DriversLicence | 5 |
| Passport, HealthCard | 8 |
| SIN, CreditCard | 10 |

| Exposure | Weight |
|---|---|
| Private (one user's device or account) | 1 |
| Internal (shared inside the company) | 2 |
| SharedLink (anyone with the link) | 5 |
| Public (open to the internet) | 10 |

## Severity ranges

| Risk score | Severity | Response target |
|---|---|---|
| 1–99 | Informational | 14 days |
| 100–999 | Low | 5 days |
| 1,000–9,999 | Medium | 48 hours |
| 10,000+ | High | 4 hours |

**Override:** SIN, CreditCard, Passport or HealthCard on a SharedLink or Public location is always **High**
(Critical in TheHive). Without it, one passport scan on a public link would score only 40.

## Expected result from the sample data

| Data location | Calculation | Score | Severity |
|---|---|---|---|
| stfinancearchive (public blob) | 2,000 × 10 × 10 | 200,000 | High (and override) |
| LAPTOP-HR-014 (laptop) | 120 × 10 × 1 + 120 × 3 × 1 | 1,560 | Medium |
| OD-mkt.lead (shared link) | 300 × 1 × 5 | 1,500 | Medium |
| SP-HR-Onboarding (SharePoint) | 40 × 3 × 2 + 40 × 2 × 2 | 400 | Low |
| OD-travel.coord (shared link) | 1 × 8 × 5 | 40 | High (override) |
| FILESRV01 (file share) | 20 × 1 × 2 | 40 | Informational |

The weights and ranges are a teaching starting point, not a standard. Tune them with your privacy team.

| Piece | File |
|---|---|
| Generator (prints the expected result) | [`data/generators/make_pii_findings.py`](../../data/generators/make_pii_findings.py) |
| DCR transform | [`sentinel/dcr/pii-transform.kql`](../../sentinel/dcr/pii-transform.kql) |
| Ingest workflow | [`logic-apps/ingest-pii/workflow.json`](../../logic-apps/ingest-pii/workflow.json) |
| Detection with dynamic severity | [`sentinel/analytics/pii-exposure-by-location.kql`](../../sentinel/analytics/pii-exposure-by-location.kql) |
| Routing playbook | `la-pb-pii-route` — [step 4](../04-playbooks.md) |
| Case template | [step 5.5](../05-shuffle-thehive.md#55-pii-case-template-use-case-2) |
