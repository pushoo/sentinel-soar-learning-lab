# Step 6: Dry run, recording checklist and cleanup

> Learning lab.

## Dry run (do it once off camera)

- [ ] Generate fresh CSVs and POST them → both Logic App runs return `202` with the expected row counts
- [ ] `SignInDemo_CL | count` = 58 and `PIIFindings_CL | count` = 8
- [ ] Use case 1: one incident (Medium → High after the playbook) with Account and IP entities
- [ ] Use case 2: six incidents, severities match the list `make_pii_findings.py` printed
- [ ] Playbooks ran: tags, comments, Teams/email message
- [ ] Shuffle created one TheHive case per incident within 1-2 minutes, with observables
- [ ] Sentinel incidents show "Case #N opened" and status Active
- [ ] Closing a TheHive case closes the Sentinel incident with the right classification
- [ ] Re-running Workflow 1 does not create duplicate cases
- [ ] You timed the full loop, so you know what to cut on camera

Reset for a new take: close the lab incidents, then regenerate the CSVs so the timestamps are fresh.

## Recording checklist

- [ ] Lab tenant only; blur subscription ID, tenant ID, client IDs, secrets, API keys and email addresses
- [ ] 1920×1080, browser zoom 110-125%, dark mode, terminal font 16pt+
- [ ] Say "learning lab, synthetic data" in the first minute and show it on screen
- [ ] Add a clock overlay when you cut waits (rule schedule, ingestion delay)
- [ ] Upload your own captions so Sentinel, SOAR, Entra, Shuffle and TheHive are spelled correctly
- [ ] Put the GitHub repo link in the description and pinned comment

## Cleanup

```bash
az group delete --name rg-soc-lab --yes --no-wait        # workspace, Logic Apps, DCRs, storage
az ad app delete --id "$APP_ID"                          # the Shuffle app registration
```

- Remove the lab victim user if you no longer need it.
- Stop or delete the Docker host. On a VM: `docker compose down -v` in each stack, then delete the VM.
- Rotate any key that appeared on screen (AbuseIPDB, TheHive API key, client secret).
