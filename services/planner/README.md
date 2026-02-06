# Planner Service

**Purpose:** Decompose high-level goals into executable **Tasks**. No logic is implemented; behaviour is defined in the research and spec documents.

---

## Role in the Architecture

The Planner is one of the three sub-agents in the **Orchestrator cycle** (see **`research/architecture_strategy.md`** §2.3):

1. **Planner** – Creates a `Task` from a goal, priority, and optional acceptance criteria.
2. **Worker** – Executes the task (e.g. via skills) and returns a `Result`.
3. **Judge** – Reviews the result and returns a `Decision` (approve / escalate / reject).

The Planner does **not** execute tasks or call external APIs; it only produces a structured Task for the Worker.

---

## Responsibilities (To Be Implemented)

1. **Task creation** – Given `task_type`, `goal_description`, `required_resources`, `priority`, and optional `persona_constraints`, `budget_limit_usd`, `acceptance_criteria`, return a `Task` with a unique `task_id`, `context`, and `status` (e.g. `"pending"`).
2. **Validation** – Enforce allowed values (e.g. `priority` in `low` | `medium` | `high`) and required fields.
3. **Traceability** – Task should include `created_at` (e.g. ISO-8601) for auditing.

---

## Data Contracts

- **Input:** `task_type`, `goal_description`, `required_resources`, `priority`, and optional fields (see `specs/technical.md` and `schemas/task.schema.json` if present).
- **Output:** A **Task** with at least: `task_id`, `task_type`, `priority`, `context`, `acceptance_criteria`, `created_at`, `status`.

---

## Implementation Status

- **Current:** Stub only. `PlannerService.create_task()` raises `NotImplementedError`.
- **Tests:** Orchestrator flow tests in `tests/test_services_flow.py` indirectly require a working Planner once the Orchestrator is implemented.

---

## References

- `research/architecture_strategy.md` – §2.3 (Runtime Flow), §7 (Infrastructure).
- `specs/functional.md` – FR-6.0 (Planner, Worker, Judge as decoupled services).
- `orchestrator/README.md` – How the Planner is invoked by the Orchestrator.
