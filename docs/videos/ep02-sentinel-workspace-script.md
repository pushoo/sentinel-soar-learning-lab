# Episode 02: Turn on Microsoft Sentinel (free trial)

> Learning lab, synthetic data only. Target length about 4 minutes. Builds on [Episode 01](ep01-setup-your-lab-script.md).
> Names used on screen: resource group `rg-soc-lab`, workspace `law-soc-lab`, region Canada Central.

## Recording plan (one Chrome window, Claude drives, you record)

| Take | What happens on screen | Lines |
|---|---|---|
| A | Azure portal: search "Microsoft Sentinel", open it, Create | s08-s12 |
| B | Create a new workspace: resource group `rg-soc-lab` (made in Ep01), name `law-soc-lab`, Canada Central, Review + create, Create, deployment finishes | s13-s19 |
| C | Back in Sentinel: pick `law-soc-lab`, Add, free trial message | s20-s25 |
| D | Azure portal: `law-soc-lab` > Tables | s26-s27 |
| E | Defender portal (security.microsoft.com/?tid=<your tenant ID>): first-run "preparing" screen | s28-s32 |

Graphics only (no recording): hook, "two things" stack, tenant ID tip, recap, outro.

## Narration

Final narration, as it is in the published video.

**Hook**
- s01 By the end of this episode, Microsoft Sentinel is running in your own lab.
- s02 It's free for thirty-one days, and it takes about ten minutes.
- s03 This is a learning lab, with synthetic data only.

**What we build**
- s04 We build two things today.
- s05 A Log Analytics workspace, which is where every log is stored.
- s06 And Sentinel, switched on for that workspace.
- s07 Sentinel doesn't store anything itself. It sits on top of the workspace.

**Find Sentinel**
- s08 In the Azure portal, search for Microsoft Sentinel, and open it.
- s09 There's nothing here yet, so select Create.
- s10 Two notes on this page. Sentinel has a thirty-one day free trial.
- s11 And new workspaces move to the Microsoft Defender portal automatically.
- s12 We don't have a workspace yet, so select Create a new workspace.

**Create the workspace**
- s13 Pick the resource group from the last episode, rg-soc-lab.
- s14 Name the workspace law-soc-lab. LAW stands for Log Analytics workspace.
- s15 Pick a region close to you. I'm using Canada Central.
- s16 Select Review and create, and wait for validation to pass.
- s17 The pricing tier is pay as you go, per gigabyte. The trial covers us.
- s18 Select Create. The deployment takes about a minute.
- s19 Your deployment is complete.

**Turn on Sentinel**
- s20 Back in Sentinel, the new workspace is in the list. Select it, and select Add.
- s21 This step takes a minute or two.
- s22 And there it is. The Microsoft Sentinel free trial is activated.
- s23 For thirty-one days, the first ten gigabytes a day are free, for both Sentinel and Log Analytics.
- s24 Our lab sends a few kilobytes, so we stay far below that.
- s25 Set a reminder for day thirty. We clean everything up in the last episode.

**Look at the workspace**
- s26 Now look at the workspace itself. Under Tables, there are already over a hundred and sixty built-in tables.
- s27 Next episode, we add our own: SignInDemo underscore C L.

**The Defender portal**
- s28 Last stop: the Microsoft Defender portal, at security dot microsoft dot com.
- s29 Tip: with a personal account, add your tenant ID to that address, or the sign-in lands in the wrong directory.
- s30 The first time you open it, Defender prepares your tenant.
- s31 That takes a few minutes, and your data fills in over the next few hours.
- s32 Once it's ready, Sentinel shows up right in the Defender menu. We'll pick it up there next time.

**Wrap**
- s33 Quick recap.
- s34 A workspace in our lab resource group, Sentinel on top, and the free trial running.
- s35 Every name is in the repo, linked below.
- s36 Next episode, we create the custom table, and a transform that cleans the data before you pay to store it.

## On-screen evidence

- Free trial terms: Microsoft Learn, "Plan costs and understand pricing and billing for Microsoft Sentinel" (10 GB/day free for 31 days).
- Defender portal: Microsoft Learn, "Onboard Microsoft Sentinel" (new customers with Owner or User Access Administrator are onboarded automatically).
