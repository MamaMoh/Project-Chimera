# Contracts: 001-main (Core Swarm Orchestration)

**Branch**: 001-main

## In-process contracts (no HTTP API in this feature)

- **Task**: Planner → Worker. See repo root `schemas/task.schema.json` and `specs/technical.md` (Planner → Worker Request).
- **Result**: Worker → Judge. See `schemas/result.schema.json` and `specs/technical.md` (Worker → Judge Response).
- **Decision**: Judge → Orchestrator. See `specs/technical.md` (Judge → Orchestrator Decision).

## Implementation

- Task/Result/Decision are implemented as dataclasses in `services/planner/planner_service.py`, `services/worker/worker_service.py`, `services/judge/judge_service.py`, and consumed by `orchestrator/orchestrator_service.py`.
