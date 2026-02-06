# Dashboard

**Purpose:** Describe the future HITL review UI and fleet monitoring interface for Project Chimera. No implementation is present; the role is defined here and in the research documents.

---

## Role in the Architecture

- **`research/architecture_strategy.md`** §3 describes the Human-in-the-Loop flow: content is submitted to an Approval Queue, and a human operator is notified to approve or reject. The **dashboard** is the intended interface for that review and for monitoring agent state.
- **`hitl/README.md`** describes approval gates, risk levels, and timeouts; the dashboard would expose these (e.g. pending queue, approval/reject actions, audit log).

---

## Intended Capabilities (To Be Implemented)

1. **HITL review** – View pending content and decisions; approve or reject with optional feedback.
2. **Fleet monitoring** – View orchestrator state, recent tasks, Judge decisions, and alerts.
3. **Governance** – Access to policy and disclosure settings (see `policies/`).

---

## Implementation Status

- **Current:** Specification only. No UI or backend is implemented in this directory.
- **References:** `research/architecture_strategy.md` §3, `hitl/README.md`, `agents/AGENTS.md`.
