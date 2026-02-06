# API Documentation

**Purpose:** Describe the intended API surface for the Orchestrator and, when implemented, the Dashboard. No runtime is implemented; this document aligns with the research and specs.

---

## Relationship to Research and Specs

- **`research/architecture_strategy.md`** §2.3–2.4 defines the runtime flow: `main.py` → Orchestrator → Planner → Worker → Judge. The “API” for the system is currently the programmatic interface to the Orchestrator (e.g. `run_once(goal_description)` returning a `Decision`).
- **`specs/technical.md`** (when fully written) will define detailed API contracts, request/response shapes, and error codes.
- **`research/architecture_strategy.md`** §8 describes CI/CD and deployment; any future HTTP/gRPC API would be part of the containerised runtime.

---

## Intended Surfaces (To Be Implemented)

1. **Orchestrator** – Programmatic: `OrchestratorService.run_once(goal_description) -> Decision`. Optional: REST or gRPC wrapper for remote invocation.
2. **Dashboard** – REST or similar for HITL queue, approval actions, and fleet metrics (see `dashboard/README.md`).

---

## Implementation Status

- **Current:** No HTTP/gRPC API is implemented. Orchestrator is a stub (see `orchestrator/README.md`).
- **References:** `research/architecture_strategy.md` §2.3–2.4, §8; `specs/technical.md`; `orchestrator/README.md`, `dashboard/README.md`.
