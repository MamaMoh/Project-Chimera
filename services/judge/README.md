# Judge Service

**Purpose:** Review **Results** from the Worker and produce a **Decision** (approve / escalate / reject) for HITL or commit. No logic is implemented; behaviour is defined in the research and spec documents.

---

## Role in the Architecture

The Judge is the decision sub-agent in the **Orchestrator cycle** (see **`research/architecture_strategy.md`** §2.3 and §3):

- **Worker** produces a `Result` (e.g. confidence score, output, traces).
- **Judge** evaluates the result against policy (e.g. confidence thresholds, sensitive topics) and returns a `Decision`: **approve**, **escalate** (to HITL), or **reject**.
- The Orchestrator (and/or HITL layer) uses the Decision to either publish, queue for human review, or retry.

Human-in-the-Loop (HITL) is described in §3 of the architecture strategy: content is submitted to an Approval Queue, and a human approves or rejects before publishing to social APIs.

---

## Responsibilities (To Be Implemented)

1. **Review logic** – Map `Result.confidence_score` and optional policy rules (e.g. sensitive-topic filters) to one of: approve, escalate, reject. Example thresholds (from `agents/AGENTS.md`): auto-approve when confidence ≥ 0.90 and no sensitive triggers; escalate when confidence in [0.70, 0.90) or sensitive topic; reject when confidence < 0.70.
2. **Decision shape** – Return a `Decision` with: `task_id`, `decision`, `rationale`, `state_version`, `created_at`.
3. **Optimistic concurrency** – FR-6.1 requires the Judge to implement optimistic concurrency control before committing state; the `state_version` from the Orchestrator is part of this contract.

---

## Data Contracts

- **Input:** A `Result` from the Worker and the current `state_version` from the Orchestrator.
- **Output:** A **Decision** with: `task_id`, `decision` (approve | escalate | reject), `rationale`, `state_version`, `created_at`.

---

## Implementation Status

- **Current:** Stub only. `JudgeService.review_result()` raises `NotImplementedError`.
- **Tests:** `tests/test_services_flow.py` asserts that the Orchestrator returns a Decision with the required attributes; those tests fail until the full flow (including Judge) is implemented.

---

## References

- `research/architecture_strategy.md` – §2.3 (Runtime Flow), §3 (HITL Safety).
- `specs/functional.md` – FR-6.0, FR-6.1 (Judge, OCC).
- `agents/AGENTS.md` – HITL thresholds and policy.
