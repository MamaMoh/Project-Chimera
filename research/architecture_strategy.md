# Project Chimera – Architecture Strategy (Paraphrased & Diagrammed)

**Version:** 1.0.0  
**Date:** February 4, 2025  
**Status:** Draft for Team Review

---

## 1. Overview

Project Chimera is an autonomous AI influencer system that researches trends, generates content, and engages audiences with minimal human oversight.

**Key principles:**

- **Spec-Driven Development (SDD)** – All code is anchored in formal specifications.
- **Agentic Orchestration** – Planner, Worker, Judge agents have clearly defined roles.
- **Robust Infrastructure** – Scalable, traceable, and fault-tolerant.

---

## 2. Agent Architecture Approach

### 2.1 Evaluated Patterns (Textual)

| Pattern                | Score  | Notes                                                                 |
| ---------------------- | ------ | --------------------------------------------------------------------- |
| **Hierarchical Swarm** | 9/10   | Central Chief Agent manages sub-agents. Clear authority, scalable, fault-isolated. Single point of failure risk. |
| **Sequential Chain**  | 4/10   | Linear processing pipeline. Simple, predictable, but brittle.         |
| **Mesh Network**       | 7/10   | Peer-to-peer agent collaboration. Resilient but coordination-heavy. |
| **Actor Model**       | 8/10   | Asynchronous message-passing. High concurrency, complex debugging.   |

**Decision:** Core **Hierarchical Swarm** with **Mesh fallback**.

### 2.2 Conceptual Agent Structure

```mermaid
graph LR
    H[Human Operator] --> HA[Approval Queue]
    CA[Chief Agent] --> TF[Trend Fetcher]
    CA --> CG[Content Generator]
    CA --> EM[Engagement Manager]
    CA --> QA[Quality Assessor]

    CG --> SK1[skill_download_video]
    CG --> SK2[skill_download_youtube]
    CG --> SK3[skill_transcribe_audio]
    EM --> SK4[skill_post_social]
    QA --> SK3

    TF --> TR[Trend APIs]
    EM --> SM[Social Media APIs]
    CA --> OC[OpenClaw Network]
    HA --> CA
```

### 2.3 Runtime Flow (Orchestrator Cycle)

```mermaid
flowchart LR
    main[main.py] --> Orch[Orchestrator]
    Orch --> Planner[Planner Service]
    Planner --> Worker[Worker Service]
    Worker --> Judge[Judge Service]
    Judge --> Orch
```

- **Planner:** Creates tasks with goal, priority, and acceptance criteria.
- **Worker:** Executes tasks using skills and returns results.
- **Judge:** Reviews results → approves, escalates, or rejects.

---

## 3. Human-in-the-Loop (HITL) Safety

```mermaid
sequenceDiagram
    participant Agent as Chimera Agent
    participant Queue as Approval Queue
    participant Human as Human Operator
    participant Social as Social Media APIs

    Agent->>Queue: Submit Content for Review
    Queue->>Human: Notify for Approval

    alt Approved
        Human->>Queue: Approve
        Queue->>Social: Publish Content
        Social-->>Agent: Confirmation
    else Rejected
        Human->>Queue: Reject with Feedback
        Queue->>Agent: Feedback for Revision
    end

    alt Timeout
        Queue->>Agent: Auto-expire pending items
    end
```

---

## 4. Database Strategy

**Hybrid Architecture:** PostgreSQL + Redis + Elasticsearch

```mermaid
erDiagram
    USER ||--o{ CONTENT : creates
    USER ||--o{ ENGAGEMENT : performs
    CONTENT ||--o{ ENGAGEMENT : receives
    CONTENT }|--|| TREND : sourced_from
    CONTENT }|--|| SKILL : generated_by

    USER {
        uuid id PK
        string username
        jsonb preferences
        timestamp created_at
    }
    CONTENT {
        uuid id PK
        uuid user_id FK
        uuid trend_id FK
        string content_type
        jsonb metadata
        string status
        timestamp created_at
        timestamp published_at
    }
    ENGAGEMENT {
        uuid id PK
        uuid user_id FK
        uuid content_id FK
        string engagement_type
        jsonb details
        timestamp created_at
    }
    TREND {
        uuid id PK
        string platform
        string topic
        float score
        jsonb raw_data
        timestamp fetched_at
    }
    SKILL {
        string name PK
        string version
        jsonb input_schema
        jsonb output_schema
        boolean enabled
    }
```

---

## 5. Agent Communication Protocols

```mermaid
graph LR
    Chimera[Chimera Agent] --> Registry[OpenClaw Registry]
    Chimera --> PubSub[Pub/Sub Module]
    Chimera --> Heartbeat[Heartbeat Generator]
    Chimera --> Capability[Capability Advertiser]
    OtherAgent[Other Agents] --> Registry
    OtherAgent --> Chimera
```

---

## 6. Skill Layer Interaction

```mermaid
graph TD
    Worker --> SK1[skill_download_video]
    Worker --> SK2[skill_download_youtube]
    Worker --> SK3[skill_transcribe_audio]
    Worker --> SK4[skill_post_social]

    SK1 --> Result[Task Result]
    SK2 --> Result
    SK3 --> Result
    SK4 --> Result
```

---

## 7. Infrastructure Overview

| Component        | Technology                          | Purpose                    |
| ---------------- | ----------------------------------- | -------------------------- |
| **Runtime**      | Python 3.11+                        | Agent logic                |
| **Dependencies** | uv                                  | Dependency management      |
| **Containers**   | Docker                              | Reproducible environment   |
| **Data**         | PostgreSQL + Redis + Elasticsearch | Storage & caching          |
| **CI/CD**        | GitHub Actions                      | Automation & testing       |
| **Telemetry**    | MCP Sense                           | Logging & auditing         |

**Directory structure (narrative):**

- `main.py` – Entrypoint
- `orchestrator/` – Chief Agent
- `services/` – Sub-agents (Planner, Worker, Judge)
- `skills/` – Invokable agent abilities
- `specs/` – Spec-driven documentation
- `agents/` – Governance & personas
- `schemas/` – Shared JSON schemas
- `policies/` – Sensitive content & disclosure rules
- `tests/` – Unit tests

---

## 8. Deployment & CI/CD Flow

```mermaid
flowchart TB
    subgraph Dev["Developer"]
        Code[Code / Specs]
        Push[Push / PR]
    end

    subgraph CI["GitHub Actions"]
        Checkout[Checkout]
        Setup[Setup Python]
        Deps[Install deps - make setup]
        SpecCheck[Spec check - make spec-check]
        Lint[Lint / Security / Test policy checks]
        Test[make test]
    end

    subgraph Build["Build & Run"]
        Docker[Docker build]
        Container[Chimera Container]
    end

    subgraph Runtime["Runtime Dependencies"]
        PG[(PostgreSQL)]
        Redis[(Redis)]
        MCP[MCP Sense - Telemetry]
    end

    Code --> Push
    Push --> Checkout
    Checkout --> Setup
    Setup --> Deps
    Deps --> SpecCheck
    SpecCheck --> Lint
    Lint --> Test
    Test --> Docker
    Docker --> Container
    Container --> PG
    Container --> Redis
    Container --> MCP
```

- **CI:** On push/PR to `main`, run checkout → Python setup → `make setup` → `make spec-check` → quality policy checks → `make test`.
- **Build:** Docker image builds from passing CI.
- **Runtime:** Container connects to PostgreSQL, Redis, and MCP Sense for persistence, cache, and telemetry.

---

## 9. Next Steps

1. Stakeholder approval of architecture.
2. Define detailed API contracts (`specs/technical.md`).
3. Build Chief Agent skeleton using hierarchical swarm pattern.
4. Set up Docker + PostgreSQL dev environment.
5. Connect MCP Sense telemetry for logging and auditing.

---

## 10. References

- **a16z:** The Trillion Dollar AI Code Stack
- **OpenClaw:** Agent social networking framework
- **MoltBook:** Social media for bots
- **Project Chimera SRS**

---

_Document Version: 1.0.0_  
_Last Updated: February 4, 2025_  
_Next Review: February 6, 2025_
