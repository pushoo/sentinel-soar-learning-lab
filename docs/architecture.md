# Architecture

> Learning lab. Synthetic data, lab tenant only.

## 1. Data and control flow

```mermaid
flowchart LR
  subgraph SRC["Synthetic data"]
    CSV1["signins.csv"]
    CSV2["pii_findings.csv"]
  end

  subgraph AZ["Microsoft Azure"]
    LA1["Logic App 1: ingest CSV"]
    DCR["Data collection rule + KQL transform"]
    LAW[("Log Analytics workspace: custom tables")]
    RULE["Sentinel analytics rules"]
    INC["Sentinel incident"]
    AR["Automation rule"]
    LA2["Logic App 2: playbook"]
  end

  subgraph OSS["Open-source SOAR in Docker"]
    SH["Shuffle: orchestration"]
    TH["TheHive: case management"]
  end

  CSV1 -->|HTTP POST| LA1
  CSV2 -->|HTTP POST| LA1
  LA1 -->|Logs Ingestion API| DCR --> LAW --> RULE --> INC --> AR --> LA2
  LA2 -->|severity, tags, comment| INC
  LA2 --> NOTIFY["Teams or email"]
  SH -->|poll every minute| INC
  SH -->|create case| TH
  TH -->|case closed| SH
  SH -->|close incident| INC
```

## 2. One incident, step by step (use case 1)

```mermaid
sequenceDiagram
  autonumber
  participant You as You (lab)
  participant LA1 as Logic App 1
  participant LAW as Sentinel / Log Analytics
  participant LA2 as Logic App 2 (playbook)
  participant SH as Shuffle
  participant TH as TheHive
  participant Analyst

  You->>LA1: POST signins.csv
  LA1->>LAW: Logs Ingestion API (JSON rows)
  Note over LAW: Analytics rule runs every 5 min
  LAW->>LAW: Brute force then success → incident (Medium)
  LAW->>LA2: Automation rule runs playbook
  LA2->>LAW: Severity High, tags, comment
  SH->>LAW: Poll for New incidents
  SH->>SH: De-duplicate
  SH->>TH: Create case + observables
  SH->>LAW: Comment "Case opened", status Active
  Analyst->>TH: Review and close as true positive
  TH->>SH: Case closed
  SH->>LAW: Close incident (TruePositive)
```

## 3. Where each piece runs (free option)

```mermaid
flowchart TB
  subgraph MAC["Your laptop"]
    BR["Browser: Azure / Defender portal"]
    OBS["OBS: recording"]
    PY["Python: CSV generators"]
  end
  subgraph AZURE["Azure (free trial / credit)"]
    S["Sentinel + Log Analytics"]
    L["Logic Apps"]
  end
  subgraph VM["Oracle Cloud Always Free ARM VM (or your own machine)"]
    D1["Shuffle"]
    D2["TheHive"]
  end
  PY -->|POST CSV| L
  BR --> S
  BR --> D1
  BR --> D2
  D1 -->|outbound HTTPS to Azure APIs| S
```

Shuffle only makes **outbound** calls to Azure (it polls), so it works from a home network or a cloud VM
without opening inbound ports to the internet. Lock the Shuffle and TheHive web UIs to your own IP.

## Who owns what

| Component | Role | Owns |
|---|---|---|
| Logic App 1 | Data connector | Getting the CSV into a table |
| DCR | Data collection rule | Schema and ingestion-time transform |
| Analytics rules | Detection | Deciding what is an incident, and its severity |
| Logic App 2 | Playbook | Fast Azure-side enrichment and notification |
| Shuffle | Orchestration | Moving the incident between tools, de-duplication, closing |
| TheHive | Case management | The analyst's tasks, evidence and decision |

Rule of thumb: **give every field one owner.** Sentinel owns detection fields, TheHive owns the case
decision, and Shuffle is the only thing that writes between them.
