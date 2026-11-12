#!/usr/bin/env python3
"""Learning lab: synthetic PII-scan findings for use case 2 (PII exposure + severity ranges).

All data is fake: these rows describe *where* fake PII was "found", they contain no PII.
Built so every severity appears at least once (see docs/use-cases/02-pii-exposure.md).

Usage:
    python3 make_pii_findings.py --domain yourlab.onmicrosoft.com
"""
import argparse
import csv
from datetime import datetime, timezone

HEADER = ["TimeGenerated", "DataStore", "StoreType", "Exposure", "Owner",
          "FilePath", "PIIType", "RecordCount", "Encrypted"]

# DataStore, StoreType, Exposure, Owner alias, FilePath, PIIType, RecordCount, Encrypted
FINDINGS = [
    ("LAPTOP-HR-014", "Endpoint", "Private", "hr.admin", "C:/Users/hr.admin/Downloads/payroll_2026.csv", "SIN", 120, "false"),
    ("LAPTOP-HR-014", "Endpoint", "Private", "hr.admin", "C:/Users/hr.admin/Downloads/payroll_2026.csv", "DOB", 120, "false"),
    ("stfinancearchive", "AzureBlob", "Public", "fin.ops", "exports/customers_export.csv", "CreditCard", 2000, "false"),
    ("SP-HR-Onboarding", "SharePoint", "Internal", "hr.lead", "/sites/HR/Onboarding/forms.docx", "DOB", 40, "true"),
    ("SP-HR-Onboarding", "SharePoint", "Internal", "hr.lead", "/sites/HR/Onboarding/forms.docx", "Address", 40, "true"),
    ("OD-mkt.lead", "OneDrive", "SharedLink", "mkt.lead", "/campaign/leads_q4.xlsx", "Email", 300, "false"),
    ("FILESRV01", "FileShare", "Internal", "it.support", "/it/tickets/callbacks.txt", "Phone", 20, "false"),
    ("OD-travel.coord", "OneDrive", "SharedLink", "travel.coord", "/visa/passport_scan.pdf", "Passport", 1, "false"),
]

# Same weights and ranges as sentinel/analytics/pii-exposure-by-location.kql
TYPE_WEIGHT = {"Email": 1, "Phone": 1, "Address": 2, "DOB": 3, "DriversLicence": 5,
               "Passport": 8, "HealthCard": 8, "SIN": 10, "CreditCard": 10}
EXPOSURE_WEIGHT = {"Private": 1, "Internal": 2, "SharedLink": 5, "Public": 10}
HIGH_RISK = {"SIN", "CreditCard", "Passport", "HealthCard"}


def severity(score: int, force_high: bool) -> str:
    if force_high or score >= 10000:
        return "High"
    if score >= 1000:
        return "Medium"
    if score >= 100:
        return "Low"
    return "Informational"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--domain", default="yourlab.onmicrosoft.com", help="lab tenant domain")
    p.add_argument("--out", default="pii_findings.csv")
    a = p.parse_args()

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(a.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        for store, stype, exp, owner, path, ptype, count, enc in FINDINGS:
            w.writerow([now, store, stype, exp, f"{owner}@{a.domain}", path, ptype, count, enc])

    # Print the expected result so you can check Sentinel against it.
    per_store: dict[str, list] = {}
    for store, _, exp, _, _, ptype, count, _ in FINDINGS:
        s = per_store.setdefault(store, [0, False])
        s[0] += count * TYPE_WEIGHT[ptype] * EXPOSURE_WEIGHT[exp]
        s[1] = s[1] or (ptype in HIGH_RISK and exp in ("Public", "SharedLink"))
    print(f"Wrote {len(FINDINGS)} findings to {a.out}. Expected incidents:")
    for store, (score, force) in sorted(per_store.items(), key=lambda kv: -kv[1][0]):
        print(f"  {store:<18} score {score:>7,}  ->  {severity(score, force)}{' (override)' if force else ''}")


if __name__ == "__main__":
    main()
