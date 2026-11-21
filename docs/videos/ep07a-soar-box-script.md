# Episode 07a: The SOAR box (one VM, TheHive and Shuffle)

> CISSP Coffee Shot, Sentinel + SOAR learning lab. Learning lab, synthetic data only. About 3.3 minutes.
> Guide: [Step 5: Shuffle + TheHive](../05-shuffle-thehive.md).

## Before you record

- One Azure VM `vm-soar-lab` in `rg-soc-lab`, locked to your own IP, auto-shutdown at 23:00.
- Install scripts: [`soar/install-thehive.sh`](../../soar/install-thehive.sh) and [`soar/install-shuffle.sh`](../../soar/install-shuffle.sh), run through Run command.
- Blur in the edit: email, subscription and tenant IDs, the VM public IP, your own IP, the TheHive API key.

## Narration

| Time | Line |
|---|---|
| 0:00 | So far, every incident lives and dies inside Sentinel. Today we build the place where incidents become cases. |
| 0:07 | TheHive, for case management, and Shuffle, an open-source SOAR, both on one small Azure VM. |
| 0:14 | This is a learning lab, with synthetic data only. |
| 0:17 | Here's the plan. One VM, locked to our own IP address. Docker on it, then TheHive and Shuffle. |
| 0:24 | In the Azure portal, create a virtual machine, in our lab resource group. |
| 0:28 | Ubuntu Server 24.04. On the free trial, many sizes are blocked in Canada Central, so we pick North Central US. |
| 0:36 | Size: B4as v2. Four virtual CPUs and sixteen gigabytes, for about fifteen cents an hour. |
| 0:44 | Sign in with an SSH key, and no public inbound ports. We open only what we need, later. |
| 0:51 | Review and create. A few minutes later, the VM is running. |
| 0:56 | Now the firewall. In Network settings, create an inbound port rule. |
| 1:01 | Source: my IP address. Ports 22, 3001, 3443 and 9000, TCP only. |
| 1:09 | So SSH, Shuffle and TheHive answer only to us. Everyone else gets nothing. |
| 1:16 | Next, auto-shutdown at 11 PM, so a forgotten VM can't eat the trial credit. |
| 1:22 | Time to install. No SSH client needed: Run command runs a script inside the VM. |
| 1:28 | It clones the lab repo, and runs our Docker install script. |
| 1:33 | Docker Engine and Compose are in. |
| 1:36 | Next, TheHive. The script finishes, but the output is empty. |
| 1:40 | So we run it again with tracing on. Exit code 141. |
| 1:44 | That's a broken pipe. Under pipefail, the line that makes a random secret, tr piped into head, stops the whole script. |
| 1:53 | The fix: make the secret with openssl instead. The repo is fixed too. |
| 1:59 | Run it again. Cassandra, Elasticsearch and TheHive 5 are up, on port 9000. |
| 2:06 | Then Shuffle: its frontend, backend, the Orborus worker, and OpenSearch. |
| 2:11 | Shuffle answers on ports 3001 and 3443. |
| 2:16 | Open TheHive on port 9000. Log in with the default admin, and change that password right away. |
| 2:23 | It runs on a 15-day trial. For the long run, request the free Community license from StrangeBee. |
| 2:30 | Create an organisation: SOC-Lab. |
| 2:32 | Inside it, an analyst account for people. |
| 2:35 | And a service account for Shuffle. It has no password, only an API key. |
| 2:40 | Create the key, and keep it hidden for now. |
| 2:44 | Now Shuffle, on port 3001. The first visit asks for an admin account. |
| 2:49 | We pick Shuffle Core, to build our own workflows. |
| 2:52 | And the app for TheHive is ready to use. |
| 2:56 | Recap: one VM, locked to our IP, shutting down every night, with TheHive and Shuffle running on Docker. |
| 3:05 | Everything is in the repo, including the fix. Next episode, we connect Sentinel to TheHive, and back. |
