#!/usr/bin/env python3
"""Learning lab: synthetic sign-in events for use case 1 (brute force, then success).

All data is fake. Timestamps are relative to "now" (UTC) so the analytics rule's
1-hour lookback always sees them. Re-run right before each test or recording take.

Usage:
    python3 make_signins.py --domain yourlab.onmicrosoft.com --victim lab.victim
"""
import argparse
import csv
import random
from datetime import datetime, timedelta, timezone

HEADER = ["TimeGenerated", "UserPrincipalName", "IPAddress", "Location",
          "ResultType", "ResultDescription", "AppDisplayName", "UserAgent"]


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--domain", default="yourlab.onmicrosoft.com", help="lab tenant domain")
    p.add_argument("--victim", default="lab.victim", help="victim user alias (lab test user)")
    p.add_argument("--attacker-ip", default="185.220.101.45",
                   help="attacker IP (default is in a known Tor exit range, so reputation lookups flag it)")
    p.add_argument("--failures", type=int, default=37, help="number of failed sign-ins")
    p.add_argument("--noise", type=int, default=20, help="number of normal sign-ins from other users")
    p.add_argument("--out", default="signins.csv")
    p.add_argument("--seed", type=int, default=None, help="random seed for repeatable noise")
    a = p.parse_args()

    rng = random.Random(a.seed)
    now = datetime.now(timezone.utc)
    victim = f"{a.victim}@{a.domain}"
    start = now - timedelta(minutes=6)
    rows = []

    for i in range(a.failures):
        rows.append([start + timedelta(seconds=i * 3), victim, a.attacker_ip, "DE", 50126,
                     "Invalid username or password", "Azure Portal", "python-requests/2.31"])
    rows.append([start + timedelta(seconds=a.failures * 3 + 5), victim, a.attacker_ip, "DE", 0,
                 "Success", "Azure Portal", "python-requests/2.31"])

    users = ["priya.n", "sam.k", "alex.r", "maria.g"]
    for _ in range(a.noise):
        rows.append([now - timedelta(minutes=rng.randint(1, 30)), f"{rng.choice(users)}@{a.domain}",
                     f"203.0.113.{rng.randint(2, 250)}",  # TEST-NET-3: reserved for documentation
                     "CA", 0, "Success", "Microsoft Teams", "Mozilla/5.0"])

    rows.sort(key=lambda r: r[0])
    with open(a.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        for r in rows:
            w.writerow([r[0].strftime("%Y-%m-%dT%H:%M:%SZ")] + r[1:])

    print(f"Wrote {len(rows)} rows to {a.out} ({a.failures} failures + 1 success for {victim}, {a.noise} noise)")


if __name__ == "__main__":
    main()
