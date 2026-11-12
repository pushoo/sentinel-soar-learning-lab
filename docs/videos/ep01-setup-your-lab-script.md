# Episode 01: Set up your lab, step by step (macOS)

> Learning lab, synthetic data only. Target length about 5 minutes.
> Hands-on version of [Step 0: Prerequisites](../00-prerequisites.md). Recorded on an 8 GB Apple silicon Mac.

## Cue card (type these in Terminal, in this order)

Pause about two seconds after each command finishes so the edit has room to breathe.

| Take | Command | What viewers see |
|---|---|---|
| T1 | `git clone https://github.com/pushoo/sentinel-soar-learning-lab.git` | Repo downloads |
| T1 | `cd sentinel-soar-learning-lab` | |
| T2 | `bash scripts/check-prereqs.sh` | Azure CLI and Docker missing |
| T3 | `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` | Enter your Mac password, press Return to continue |
| T3 | `echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile` | Adds brew to your path for next time |
| T3 | `eval "$(/opt/homebrew/bin/brew shellenv)"` | Adds brew to this window |
| T4 | `brew install azure-cli colima docker docker-compose` | Long wait (cut in the edit) |
| T5 | `colima start --cpu 2 --memory 5 --disk 40 --vm-type vz` | Docker VM starts |
| T5 | `docker run --rm hello-world` | "Hello from Docker!" |
| T6 | `az login` | Browser opens, pick your lab account |
| T6 | `az account show --query "{subscription:name, state:state}" -o table` | Subscription is Enabled |
| T7 | `az group create --name rg-soc-lab --location canadacentral -o table` | Succeeded |
| T8 | `bash scripts/check-prereqs.sh` | Everything ok |

Then in the browser (Claude drives): Cost Management > Budgets > Add, $5 a month, alert at 50%.

If `docker run` says it can't find `docker-credential-desktop` (left over from Docker Desktop), run
`sed -i '' 's/"credsStore"/"credStore"/' ~/.docker/config.json` and try again.

## Narration

**Hook**
- s01 In the last episode we planned the lab. Now we build the foundation.
- s02 Ten minutes, a few commands, and nothing to pay.
- s03 This is a learning lab, with synthetic data only.

**Get the repo**
- s04 Open Terminal, and clone the learning lab repo.
- s05 Every script and document in this series lives here.
- s06 Now run the prerequisite checker. It only reads, it never changes anything.
- s07 Python and Git are already on the Mac.
- s08 We're missing two things: the Azure CLI, and a Docker engine.

**Homebrew**
- s09 We'll install both with Homebrew, the free package manager for macOS.
- s10 Paste the install command from brew dot s h.
- s11 It asks for your Mac password. That's normal, it needs to create its folder.
- s12 When it finishes, these two lines put brew on your path.

**Tools**
- s13 Now one command installs everything else.
- s14 The Azure CLI, Colima, and the Docker command line tools.
- s15 Colima runs Docker inside a small, free virtual machine.
- s16 It's much lighter than Docker Desktop, which matters on an eight gigabyte laptop.
- s17 Start it with two CPUs and five gigabytes of memory.
- s18 That cap keeps the rest of the Mac usable while we record.
- s19 Hello from Docker. The engine works.

**Azure**
- s20 Next, sign in to Azure from the terminal.
- s21 A browser window opens. Pick the account that has your lab subscription.
- s22 Use a lab subscription only, never your company's production one.
- s23 Check which subscription you're in. It should say Enabled.
- s24 Now create one resource group for the whole lab.
- s25 Everything we build goes in here, so cleanup at the end is one command.

**Budget**
- s26 One safety net before we build anything.
- s27 In the portal, open Cost Management, then Budgets.
- s28 Add a budget of five dollars a month, with an email alert at fifty percent.
- s29 If anything ever runs that shouldn't, you'll hear about it early.

**Check again**
- s30 Run the checker one more time.
- s31 Python, Git, the Azure CLI, and a running Docker engine. All green.

**Wrap**
- s32 That's the foundation done.
- s33 Commands are in the repo, linked below, if you want to copy them.
- s34 Next episode, we turn on Microsoft Sentinel and start the free trial.
