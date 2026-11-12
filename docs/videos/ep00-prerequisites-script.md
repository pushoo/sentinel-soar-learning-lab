# Episode 0: Prerequisites: build a free SOC lab (script)

**Format:** learning video, screen recording with voice-over · **Target length:** 7-9 minutes
**Channel:** CISSP Coffee Shot · **Series:** Sentinel + Logic Apps + Open-Source SOAR learning lab

> Say early and on screen: *"This is a learning lab. Synthetic data, a lab tenant, nothing production."*

## Scene list

| Time | Scene | On screen | Voice-over (key lines) |
|---|---|---|---|
| 0:00-0:25 | Hook | Final result from Ep1: Sentinel incident closed by Shuffle, TheHive case beside it | "By the end of this series, one CSV file becomes a closed case across four tools. Today we set up everything you need, for free." |
| 0:25-0:50 | Learning-lab disclaimer | Text card: *Learning lab · Synthetic data · Lab tenant only* | "This is a learning project. Every record is fake, and we never touch production." |
| 0:50-2:00 | What we're building | Architecture diagram from the README (Mermaid render) | "Sentinel detects, Logic Apps ingest and enrich, Shuffle orchestrates, TheHive holds the case." |
| 2:00-3:00 | The shopping list | Table from `docs/00-prerequisites.md` | "An Azure subscription, an Entra tenant you control, a Docker host, Python and Git. Everything has a free option." |
| 3:00-4:00 | How it stays free | Sentinel free trial page, Azure free account page, Oracle Always Free page | "Sentinel gives a new workspace a 31-day trial. The CSVs are kilobytes. Shuffle and TheHive are self-hosted." |
| 4:00-5:00 | Pick your Docker host | Decision table (16 GB / 8 GB / no machine) | "My laptop has 8 GB, so the SOAR tools go on a free cloud VM and the laptop just records." |
| 5:00-6:15 | Clone and check | Terminal: `git clone`, `bash scripts/check-prereqs.sh`, run both generators, open the CSVs | "Fresh timestamps every run. That matters later, because the detection only looks back one hour." |
| 6:15-7:15 | Azure one-time setup | `az group create`, then Cost Management → Budgets → $5 alert | "One resource group means one-command cleanup. And a budget alert, because free should stay free." |
| 7:15-7:50 | Lab identities | Entra: create the lab victim user | "This account will be attacked in Episode 1. It's a lab user, nothing else." |
| 7:50-8:30 | Recap + next | Checklist with all four ticks, then Ep1 thumbnail | "Next episode, the brute-force attack goes from CSV to closed case." |

## Recording checklist

- [ ] Lab tenant only; blur subscription ID, tenant ID and email addresses
- [ ] Browser zoom 110-125%, dark mode, 1920×1080
- [ ] Terminal font 16pt or larger
- [ ] Upload your own captions (Sentinel, SOAR, Entra, TheHive, Shuffle spelled correctly)
- [ ] Pin the GitHub repo link in the description and first comment

## Description template

> Learning lab, part 0: everything you need to build a free SOC lab with Microsoft Sentinel, Azure Logic Apps,
> Shuffle and TheHive. Synthetic data, lab tenant only.
> Code, diagrams and guides: <GitHub repo link>
> Chapters: 0:00 Intro · 0:50 Architecture · 2:00 What you need · 3:00 Keeping it free · 4:00 Docker host ·
> 5:00 Clone and check · 6:15 Azure setup · 7:15 Lab identities · 7:50 Next
