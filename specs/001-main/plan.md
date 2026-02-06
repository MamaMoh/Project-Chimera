# Implementation Plan: Core Swarm Orchestration

**Branch**: `001-main` | **Date**: 2026-02-04 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-main/spec.md`

## Summary

Implement the Planner–Worker–Judge orchestration loop so a goal produces a validated decision. The system already has service modules (planner, worker, judge, orchestrator); this plan formalizes contracts, data model, and quickstart for the 001-main feature scope.

## Technical Context

**Language/Version**: Python 3.12+  
**Primary Dependencies**: Standard library (dataclasses, uuid, datetime); existing services in `services/` and `orchestrator/`  
**Storage**: In-memory for this feature; queues/stores out of scope for 001-main  
**Testing**: pytest; contract tests in `tests/`  
**Target Platform**: Cross-platform (Windows/Linux/macOS)  
**Project Type**: Single codebase (services + orchestrator)  
**Performance Goals**: Single-run latency under 10s for one orchestration cycle  
**Constraints**: MCP-only external actions; no direct API calls from agent logic  
**Scale/Scope**: Single-threaded loop for 001-main; scaling deferred

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Constitution file is template-only; no project-specific MUST/SHOULD gates defined.
- Assumed alignment: spec-driven, testable requirements, no implementation details in spec. **PASS**.

## Project Structure

### Documentation (this feature)

```text
specs/001-main/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/            # Phase 1 output (Task, Result, Decision)
└── tasks.md             # Phase 2 output (/speckit.tasks - not created by plan)
```

### Source Code (repository root)

```text
services/
├── planner/             # Task creation from goals
├── worker/              # Task execution → Result
└── judge/               # Result review → Decision

orchestrator/            # Coordinates Planner → Worker → Judge
main.py                  # Entry point: run_once(goal)
tests/                   # Contract and flow tests
```

**Structure Decision**: Existing layout is retained. This feature adds/aligns contracts and docs under `specs/001-main/`.

## Complexity Tracking

No constitution violations. Table left empty.
