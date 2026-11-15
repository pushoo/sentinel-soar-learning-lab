# Episode 03: The custom table and its transform

> Learning lab, synthetic data only. Target length about 4 minutes. Builds on [Episode 02](ep02-sentinel-workspace-script.md).
> Names used on screen: workspace `law-soc-lab`, table `SignInDemo_CL`, DCR `dcr-signin-demo`, DCE `dce-soc-lab`.

## Before you record

- Chrome zoom 150% (Cmd and +), so the portal text is captured large and stays sharp.
- Sample file: `data/schema/signins.sample.json` (3 rows: one mixed-case user name, one empty row, so the transform has something to fix). Transform: `sentinel/dcr/signins-transform.kql`.

## Recording plan (one Chrome window, Claude drives, you record)

| Take | What happens on screen | Lines |
|---|---|---|
| A | Azure portal: Monitor > Data collection endpoints > Create: `dce-soc-lab`, `rg-soc-lab`, Canada Central | s05-s08 |
| B | `law-soc-lab` > Tables > Create > New custom log (DCR-based). Basics: table `SignInDemo`, Analytics plan, new DCR `dcr-signin-demo`, endpoint `dce-soc-lab` | s09-s13 |
| C | Schema and transformation: upload the sample file, open the transformation editor, paste the transform, Run, results | s14-s21 |
| D | Review + create, Create, the new table in the Tables list (takes about 2 minutes) | s22-s25 |
| E | The DCR overview: immutable ID, then the DCE overview: logs ingestion address (blur both) | s26-s28 |

Graphics only: hook, "why a transform" card, the transform as code, recap, outro.

## Narration

Final narration, as it is in the published video.

**Hook**
- s01 Sentinel is on. Now it needs data, and that data needs a home.
- s02 Today we create a custom table, and a transform that cleans the data before you pay to store it.
- s03 This is a learning lab, with synthetic data only.
- s04 Our sign-in events don't fit a built-in table, so we make our own: SignInDemo underscore C L.

**The endpoint**
- s05 First, a data collection endpoint. It's the address our Logic App will send data to.
- s06 In Azure Monitor, open Data collection endpoints, and select Create.
- s07 Name it dce-soc-lab, in our lab resource group, and the same region as the workspace.
- s08 Review and create, then Create. And there it is.

**Create the table**
- s09 Now open the law-soc-lab workspace, then Tables, then Create, New custom log.
- s10 Name the table SignInDemo. Azure adds underscore C L for you.
- s11 Keep the Analytics plan. Our detection rules need it.
- s12 Create a new data collection rule: dcr-signin-demo. It decides what gets in, and in what shape.
- s13 And pick the endpoint we just made.

**Schema and transform**
- s14 Next, upload a sample file. It's in the repo, under data, schema.
- s15 Azure reads the columns from it. Notice two problems: one user name has capital letters, and the last row is empty.
- s16 Now the transformation editor. This is the part that saves you money.
- s17 The transform runs at ingestion, before anything is stored.
- s18 It drops rows with no user or no IP address.
- s19 It turns the time and the result code into the right types.
- s20 And it makes every user name lower case, so one person is always one user.
- s21 Run it. Three rows go in, two come out, and both names match.

**Create**
- s22 Apply, review, and create.
- s23 Azure builds the table in the background. It takes a minute or two.
- s24 And there it is: SignInDemo underscore C L, a custom table on the Analytics plan.
- s25 It's empty for now. That's expected.

**Ingestion details**
- s26 Open the data collection rule. The first value we need is the immutable ID.
- s27 The second is on the endpoint: the logs ingestion address.
- s28 Keep both out of Git. Our Logic App needs them next time.

**Wrap**
- s29 Quick recap. A custom table, a rule that shapes the data, and an endpoint to send it to.
- s30 Next episode, the Logic App that takes a C S V and sends it into Sentinel.
