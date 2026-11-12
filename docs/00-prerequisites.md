# Step 0 — Prerequisites (and how to do it for free)

> Learning lab. Use a lab tenant or a dedicated test subscription, never production.
> Video: [Episode 0 script](videos/ep00-prerequisites-script.md)

## What you need

| Need | Why | Free option |
|---|---|---|
| Azure subscription (Owner) | Sentinel, Logic Apps, DCR | New **Azure free account** (credit for the first 30 days), or any existing subscription. Sentinel's **31-day free trial** covers ingestion up to 10 GB/day on a new workspace. |
| Entra ID tenant you control | App registration for Shuffle, one test "victim" user | Use the tenant that comes with the Azure account, or a separate lab tenant |
| A Docker host, about 8–12 GB free RAM | Shuffle + TheHive | **Oracle Cloud Always Free** ARM VM (2 OCPU / 12 GB at the time of writing), or your own machine with Colima/Docker |
| Python 3.10+ | CSV generators | Already on macOS/Linux, or python.org |
| Azure CLI | Role assignments and checks from the terminal | `brew install azure-cli` or Microsoft's installer |
| Git + a GitHub account | Clone this repo | Free |
| OBS Studio (optional) | Recording | Free |
| AbuseIPDB API key (optional) | Real IP reputation lookups | Free tier; or use the `BadIPs` watchlist instead |
| Teams channel or email (optional) | Playbook notifications | Anything you already have |

Check your machine:

```bash
bash scripts/check-prereqs.sh
```

## Choosing where Shuffle + TheHive run

Shuffle (OpenSearch inside) and TheHive (its own database and index) are the heavy part. Rough sizing
for this lab with memory caps applied: **Shuffle ~3–4 GB, TheHive ~3–4 GB**.

| Your machine | Recommendation |
|---|---|
| 16 GB RAM or more | Run both locally with Docker Desktop or Colima |
| 8 GB RAM (for example an M1 MacBook Air) | Run both on a free cloud VM; keep the laptop for the browser and OBS. Or run **Shuffle only** locally and treat the Sentinel incident as the case |
| No spare machine | Oracle Cloud Always Free ARM VM |

### Option A — Oracle Cloud Always Free ARM VM

1. Create an Oracle Cloud account (a card is needed for identity verification; stay inside the Always Free limits).
2. Create an instance: shape `VM.Standard.A1.Flex`, Ubuntu 24.04, up to the Always Free limit (check the current limit on
   Oracle's *Always Free Resources* page — it was reduced to 2 OCPU / 12 GB in June 2026).
3. If you get "out of capacity", try another availability domain or a smaller shape, and retry later.
4. In the VCN security list, allow ports 22, 3443 (Shuffle) and 9000 (TheHive) **from your own IP only**.
5. SSH in and run `soar/install-docker-ubuntu.sh`, then the Shuffle and TheHive scripts in `soar/`.

> TheHive publishes official `linux/arm64` images. Check Shuffle's current ARM support on its GitHub before
> choosing an ARM VM.

### Option B — your Mac with Colima (free, open source)

Colima runs Docker in a lightweight VM and lets you cap its memory.

```bash
brew install colima docker docker-compose
colima start --cpu 4 --memory 6 --disk 40 --vm-type vz
docker info | grep -E "Total Memory|Architecture"
```

With 8 GB RAM, give Colima 5–6 GB, run **one** of Shuffle or TheHive at a time, and close other heavy apps while recording.

### Option C — Docker Desktop

Free for personal and education use under Docker's licence terms. Set **Settings → Resources → Memory** to cap it.

## Azure: one-time setup

```bash
az login
az account set --subscription "<your lab subscription>"

# Everything for the lab lives in one resource group, so cleanup is one command.
az group create --name rg-soc-lab --location canadacentral
```

Then set a **budget alert** (Portal → Cost Management → Budgets → Add, for example $5 with an email alert at 50%).

## Lab identities

1. **Victim test user** — create `lab.victim@<yourtenant>.onmicrosoft.com` in Entra ID. Use its UPN in the generators.
2. **Shuffle app registration** — created in [step 5](05-shuffle-thehive.md).

## Done when

- [ ] `scripts/check-prereqs.sh` shows Python, Git and Azure CLI installed
- [ ] `rg-soc-lab` exists and a budget alert is set
- [ ] A Docker host is chosen and `docker run --rm hello-world` works on it
- [ ] A lab victim user exists
