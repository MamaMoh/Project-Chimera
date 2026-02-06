# Agent Roles

**Purpose:** This document defines the responsibilities of each agent type in the Chimera system. Roles are implemented as the Orchestrator and the Planner, Worker, and Judge services (see `research/architecture_strategy.md` §2.3). Understanding these roles is essential for implementing and testing the flow.

**Context:** The architecture uses a **Hierarchical Swarm** pattern: a Chief Agent (Orchestrator) coordinates specialised sub-agents. Each role has a single responsibility and clear inputs/outputs to avoid overlap and ambiguity.

---

## Orchestrator (Chief Agent)

**What it is:** The central coordinator. It receives high-level goals (e.g. “Generate a welcome post”) and runs one cycle: Plan → Execute → Judge.

**Responsibilities:**

- Invoke the Planner to create a **Task** from the goal.
- Invoke the Worker to execute the task and produce a **Result**.
- Invoke the Judge to review the result and produce a **Decision** (approve / escalate / reject).
- Maintain orchestrator state (e.g. state version) for traceability and optimistic concurrency (FR-6.1).

**What it does not do:** It does not execute tasks itself, call external APIs, or make policy decisions; it delegates to Planner, Worker, and Judge. Implementation: `orchestrator/orchestrator_service.py` (currently a stub). See `orchestrator/README.md`.

---

## Planner

**What it is:** The agent that decomposes goals into executable tasks.

**Responsibilities:**

- **Goal decomposition:** Turn a high-level goal (and optional priority, persona constraints, budget) into a single **Task** with a unique ID, context, and acceptance criteria.
- **Task shape:** Ensure every task has at least: `task_id`, `task_type`, `priority`, `context`, `acceptance_criteria`, `created_at`, `status`.
- **Re-planning:** When context shifts or tasks fail, the Planner may be invoked again to produce a new or revised task (orchestrator responsibility to decide when).

**What it does not do:** It does not execute tasks or call MCP tools; it only produces a Task for the Worker. Implementation: `services/planner/planner_service.py` (stub). See `services/planner/README.md`.

---

## Worker

**What it is:** The agent that executes one atomic task per run.

**Responsibilities:**

- **Execution:** Take a **Task** from the Planner and run it (e.g. by invoking the appropriate skill or MCP tool).
- **MCP only:** Use MCP tools only for any external action; no direct external API calls (FR-4.0). Skills (e.g. `skill_analyze_trends`, `skill_post_social`) are the abstraction the Worker uses to call MCP.
- **Result:** Return a structured **Result** with at least: `task_id`, `status`, `confidence_score`, `output`, `artifacts`, `traces`, `created_at`.

**What it does not do:** It does not decide whether the result is good enough to publish; that is the Judge’s role. Implementation: `services/worker/worker_service.py` (stub). See `services/worker/README.md` and `research/architecture_strategy.md` §6 (Skill Layer).

---

## Judge

**What it is:** The agent that validates outputs and decides approve / escalate / reject.

**Responsibilities:**

- **Validation:** Check the Worker’s **Result** against acceptance criteria and policy (e.g. confidence threshold, sensitive-topic filters).
- **Decision:** Produce a **Decision** with: `task_id`, `decision` (approve | escalate | reject), `rationale`, `state_version`, `created_at`.
- **Optimistic concurrency:** Before committing state, perform checks required by FR-6.1 (e.g. using `state_version` from the Orchestrator).
- **HITL routing:** When confidence is in [0.70, 0.90) or a sensitive topic is detected, route to the human-in-the-loop queue (see `AGENTS.md` and `hitl/README.md`).

**What it does not do:** It does not execute tasks or call external APIs; it only reviews the Result and returns a Decision. Implementation: `services/judge/judge_service.py` (stub). See `services/judge/README.md`.

---

## Reviewer (Human)

**What it is:** The human operator in the HITL layer.

**Responsibilities:**

- **Review escalated items:** Approve, reject, or request edits for content or actions that the Judge sent to the approval queue.
- **Feedback:** Provide clear feedback when rejecting so the system can revise or retry (see `research/architecture_strategy.md` §3 sequence diagram).
- **Timeouts:** Items may auto-expire after a configured timeout (e.g. 24 hours for content) if no action is taken.

**What it does not do:** The human does not run the Planner, Worker, or Judge; they only act on items that have been escalated.

---

## Summary Table

| Role | Input | Output | Implemented in |
|------|--------|--------|-----------------|
| Orchestrator | Goal (string) | Decision | `orchestrator/` |
| Planner | Goal, priority, options | Task | `services/planner/` |
| Worker | Task | Result | `services/worker/` |
| Judge | Result, state_version | Decision | `services/judge/` |
| Reviewer (Human) | Escalated item | Approve / Reject / Feedback | HITL queue / dashboard |

---

## References

- `research/architecture_strategy.md` – §2.2 (Conceptual structure), §2.3 (Runtime flow).
- `specs/functional.md` – FR-6.0, FR-6.1.
- `agents/AGENTS.md` – Policy and HITL thresholds.
- `agents/protocols.md` – Handoff protocol and artifact formats.
