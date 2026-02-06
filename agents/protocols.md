# Agent Protocols

**Purpose:** This document defines how agents exchange information: artifact naming, required fields for results, MCP usage rules, handoff protocol, and error handling. Following these protocols ensures that the Planner, Worker, and Judge can interoperate and that all external actions go through MCP correctly.

**Context:** The runtime flow is Planner → Worker → Judge (see `research/architecture_strategy.md` §2.3). Each handoff uses structured data (Task, Result, Decision). Artifacts may be persisted for audit or retry; naming and field consistency matter for traceability.

---

## Artifact Naming

When tasks, results, or review notes are stored as files or queue messages, use these conventions so they can be discovered and linked:

| Type | Pattern | Example |
|------|---------|---------|
| Task | `task-{uuid}.json` | `task-a1b2c3d4-....json` |
| Result | `result-{uuid}.json` | `result-e5f6g7h8-....json` |
| Review notes | `review-{uuid}.md` | `review-i9j0k1l2-....md` |

The `task_id` in the Task should match the UUID used in the filename where applicable. Result and Decision objects reference the same `task_id` for traceability.

---

## Required Result Fields

Every **Result** produced by the Worker must include at least these fields so the Judge can evaluate and route correctly:

| Field | Type | Description |
|-------|------|-------------|
| **status** | string | One of: `success`, `failure`, `retry`. |
| **confidence_score** | float | Between 0.0 and 1.0. Used by the Judge for approve / escalate / reject (see `AGENTS.md` HITL thresholds). |
| **output** | object | Primary payload: e.g. `{ "type": "text", "payload": { "text": "..." } }` or media/transaction request. |
| **traces** | string | Short reasoning or execution summary for audit and debugging. |
| **created_at** | string | ISO-8601 timestamp (e.g. `2025-02-06T12:00:00Z`). |

Optional but recommended: `task_id`, `artifacts` (list of paths or IDs). Schema: see `schemas/result.schema.json` if present.

---

## MCP Usage Rules

All external actions go through the Model Context Protocol. These rules apply to the Worker and any skill that performs I/O:

1. **Tools are the only execution pathway for external actions.** No direct HTTP calls to social APIs, payment APIs, or third-party services. Use MCP tools (e.g. `post_content`, `search_memory`, `get_balance`) as defined in `mcp_servers/README.md`. This aligns with FR-4.0 and `AGENTS.md`.
2. **Resources are read-only.** MCP resources (e.g. `social://mentions/recent`) are for reading context; do not assume that mutating a resource path will change state. Use tools for actions.
3. **Prompts and versions.** When prompts or templates are referenced (e.g. for content generation or replies), reference them by name and version so behaviour is reproducible and auditable.

---

## Handoff Protocol

Who passes what to whom in one Orchestrator cycle:

| From | To | Payload | Notes |
|------|-----|---------|--------|
| **Planner** | **Worker** | Task + acceptance criteria + required resources | Task includes `context`, `acceptance_criteria`; Worker uses them to execute and to populate Result. |
| **Worker** | **Judge** | Result + confidence score + artifacts | Judge does not re-execute; it only evaluates the Result. |
| **Judge** | **Orchestrator** (and optionally **Planner**) | Decision (approve / escalate / reject) + rationale | On reject, Orchestrator may trigger a new plan or retry; on escalate, item goes to HITL queue. |

The Orchestrator owns the cycle and passes the goal to the Planner and the Result (with state version) to the Judge. It does not bypass any step.

---

## Error Handling

- **Retries:** Transient failures (e.g. rate limit, timeout) may be retried up to 2 times with the same or updated context. After 2 failures, do not retry indefinitely.
- **Escalation:** After 2 failures, either escalate to HITL with a clear summary (e.g. “Worker failed twice: timeout contacting MCP”) or mark the task as blocked and surface to the operator.
- **No silent failure:** The Worker must return a Result (with `status: failure` and a meaningful `traces` or error payload) rather than raising unhandled exceptions that break the flow. The Judge can then reject or escalate with rationale.

---

## References

- `research/architecture_strategy.md` – §2.3 (Runtime flow), §5 (Agent communication).
- `agents/AGENTS.md` – MCP-only policy, HITL thresholds.
- `agents/roles.md` – Who produces Task, Result, Decision.
- `schemas/task.schema.json`, `schemas/result.schema.json` – Formal shapes when present.
