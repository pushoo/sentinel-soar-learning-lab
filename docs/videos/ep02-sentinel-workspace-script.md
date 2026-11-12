# Episode 02: Turn on Microsoft Sentinel (free trial)

> Learning lab, synthetic data only. Target length about 4 minutes. Builds on [Episode 01](ep01-setup-your-lab-script.md).
> Names used on screen: resource group `rg-soc-lab`, workspace `law-soc-lab`, region Canada Central.

## Recording plan (one Chrome window, Claude drives, you record)

| Take | What happens on screen | Lines |
|---|---|---|
| A | Azure portal home, search "Microsoft Sentinel", open it, Create | s09-s12 |
| B | Create a new workspace: resource group `rg-soc-lab` (made in Ep01), name `law-soc-lab`, Canada Central, Review + create, Create, deployment finishes | s13-s19 |
| C | Back in Sentinel: pick `law-soc-lab`, Add, free trial message | s20-s24 |
| D | Defender portal (security.microsoft.com): Microsoft Sentinel in the menu, System > Settings > Microsoft Sentinel shows the primary workspace | s25-s30 |
| E | Azure portal: `law-soc-lab` > Tables | s31-s33 |

Graphics only (no recording): hook, "three things" pipeline, cost card, recap, outro.

## Narration

**Hook**
- s01 By the end of this episode, Microsoft Sentinel is running in your own lab.
- s02 It's free for thirty-one days, and it takes about ten minutes.
- s03 This is a learning lab, with synthetic data only.

**What we build**
- s04 We build three things today.
- s05 A resource group, to hold everything in the lab.
- s06 A Log Analytics workspace, which is where every log is stored.
- s07 And Sentinel, switched on for that workspace.
- s08 Sentinel doesn't store anything itself. It sits on top of the workspace.

**Create the workspace**
- s09 Sign in to the Azure portal with your lab subscription.
- s10 Use a lab subscription only, never your company's production one.
- s11 In the search bar, type Microsoft Sentinel, and open it.
- s12 Select Create.
- s13 We don't have a workspace yet, so select Create a new workspace.
- s14 Under Resource group, pick rg-soc-lab, the one we made last episode.
- s15 Name the workspace law-soc-lab. LAW stands for Log Analytics workspace.
- s16 Pick a region close to you. I'm using Canada Central.
- s17 Select Review and create, then Create.
- s18 The deployment takes about a minute.
- s19 When it says your deployment is complete, we're ready.

**Turn on Sentinel**
- s20 Back in Sentinel, select the new workspace, and select Add.
- s21 And there it is. The free trial is now active.
- s22 The first ten gigabytes a day are free for thirty-one days.
- s23 Our lab sends a few kilobytes, so we stay far below that.
- s24 Set a reminder for day thirty. We clean everything up in the last episode.

**The Defender portal**
- s25 One more thing has changed recently.
- s26 Sentinel now lives in the Microsoft Defender portal.
- s27 New workspaces are connected to it automatically when you have Owner rights.
- s28 Open security dot microsoft dot com, and Sentinel is right here in the menu.
- s29 Under System, Settings, Microsoft Sentinel, our workspace shows as the primary workspace.
- s30 We'll do the Sentinel work here from now on, so this series stays current.

**Look at the workspace**
- s31 Before we finish, one look at the workspace itself.
- s32 Under Tables, you'll see the built-in ones.
- s33 Next episode, we add our own: SignInDemo underscore C L.

**Wrap**
- s34 Quick recap.
- s35 A resource group, a workspace, and Sentinel on top, all on the free trial.
- s36 Note down your resource group and workspace names. You'll need them next time.
- s37 Every name and command is in the repo, linked below.
- s38 In episode three, we create the custom table, and a transform that cleans the data before you pay to store it.

## On-screen evidence

- Free trial terms: Microsoft Learn, "Plan costs and understand pricing and billing for Microsoft Sentinel" (10 GB/day free for 31 days).
- Defender portal: Microsoft Learn, "Onboard Microsoft Sentinel" (new customers with Owner or User Access Administrator are onboarded automatically).
