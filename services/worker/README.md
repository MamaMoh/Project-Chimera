# Worker Service

**Purpose:** Execute **Tasks** (e.g. by invoking skills) and return **Results**. No logic is implemented; behaviour is defined in the research and spec documents.

---

## Role in the Architecture

The Worker is the execution sub-agent in the **Orchestrator cycle** (see **`research/architecture_strategy.md`** §2.3 and §6):

- **Planner** produces a `Task`.
- **Worker** runs the task (e.g. calls `skill_download_video`, `skill_analyze_trends`, etc.) and produces a `Result` with `confidence_score`, `output`, `artifacts`, `traces`.
- **Judge** reviews the `Result` and returns a `Decision`.

The architecture diagram in §6 shows the Worker invoking skills (e.g. `skill_download_video`, `skill_download_youtube`, `skill_transcribe_audio`, `skill_post_social`). All external actions must go through **MCP tools only** (FR-4.0); skills are the abstraction that the Worker uses.

---

## Responsibilities (To Be Implemented)

1. **Task execution** – Map `Task.task_type` and `Task.context` to the appropriate skill(s) or MCP tools, execute them, and aggregate outputs.
2. **Result shape** – Return a `Result` with at least: `task_id`, `status`, `confidence_score`, `output`, `artifacts`, `traces`, `created_at`.
3. **Error handling** – On failure, return a Result that the Judge can interpret (e.g. low confidence, error payload) so that the flow can escalate or reject.

---

## Data Contracts

- **Input:** A `Task` from the Planner.
- **Output:** A **Result** with at least: `task_id`, `status`, `confidence_score`, `output` (e.g. `{ "type": "...", "payload": { ... } }`), `artifacts`, `traces`, `created_at`. See `schemas/result.schema.json` if present.

---

## Implementation Status

- **Current:** Stub only. `WorkerService.execute_task()` raises `NotImplementedError`.
- **Tests:** Orchestrator flow tests require a working Worker once the Orchestrator is implemented. Skill-level contracts are tested in `tests/test_trend_fetcher.py` and `tests/test_skills_interface.py` (they fail until skills are implemented).

---

## References

- `research/architecture_strategy.md` – §2.3 (Runtime Flow), §6 (Skill Layer Interaction).
- `specs/functional.md` – FR-3.0/FR-4.0 (content generation, MCP-only actions), FR-6.0.
- `skills/README.md` – List of skills and their contracts.
