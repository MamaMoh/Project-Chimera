# Orchestrator (Chief Agent)

**Purpose:** Central coordination for the Planner → Worker → Judge cycle. No logic is implemented; this document and the research docs define expected behaviour.

---

## Role in the Architecture

The Orchestrator is the **Chief Agent** in the Hierarchical Swarm pattern described in **`research/architecture_strategy.md`** (§2.2–2.4). It:

- Accepts high-level goals (e.g. “Generate a welcome post”).
- Runs one cycle: **Plan** → **Execute** → **Judge**.
- Returns a **Decision** (approve / escalate / reject) for HITL or commit.

The runtime flow is:

```
main.py → Orchestrator → Planner Service → Worker Service → Judge Service → Orchestrator
```

See the Mermaid diagrams in `research/architecture_strategy.md` §2.3 (Runtime Flow) and §8 (Deployment & CI/CD).

---

## Responsibilities (To Be Implemented)

1. **Coordination** – Call Planner to create a `Task`, Worker to execute it and produce a `Result`, Judge to review the result and produce a `Decision`.
2. **State** – Maintain orchestrator state (e.g. state version, updated_at) for traceability and optimistic concurrency (FR-6.1).
3. **Integration** – All external actions must go through MCP tools (FR-4.0); no direct API calls from the orchestrator.

---

## Data Contracts

- **Input:** Goal description (string) passed to `run_once(goal_description)`.
- **Output:** A `Decision` with at least: `task_id`, `decision` (approve | escalate | reject), `rationale`, `state_version`, `created_at`.
- Task, Result, and Decision shapes are specified in `specs/technical.md` and the service READMEs under `services/`.

---

## Implementation Status

- **Current:** Stub only. `OrchestratorService.run_once()` raises `NotImplementedError`.
- **Tests:** `tests/test_services_flow.py` defines the expected Decision shape and flow; they **fail** until the orchestrator (and Planner, Worker, Judge) are implemented.

---

## References

- `research/architecture_strategy.md` – §2 (Agent Architecture), §2.3–2.4 (Runtime Flow).
- `specs/functional.md` – FR-6.0, FR-6.1 (Planner–Worker–Judge, Judge OCC).
- `services/planner/README.md`, `services/worker/README.md`, `services/judge/README.md` – Sub-service contracts.
