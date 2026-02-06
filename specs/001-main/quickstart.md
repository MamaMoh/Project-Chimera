# Quickstart: Core Swarm Orchestration (001-main)

**Branch**: 001-main

## Run one orchestration cycle

From repo root:

```bash
# Install dependencies (if needed)
make setup

# Run entry point with a single goal
python main.py
```

Expected: Console prints a decision (e.g. `Decision: approve (High confidence score.)` or `escalate` / `reject`) and rationale.

## Run tests

```bash
make test
# Or in Docker
make test-docker
```

## Verify spec and plan

- Spec: `specs/001-main/spec.md`
- Plan: `specs/001-main/plan.md`
- Data model: `specs/001-main/data-model.md`
- Contracts: `specs/001-main/contracts/README.md`

## Next steps (Phase 2)

Run `/speckit.tasks` to generate `tasks.md` and then implement or adjust tasks as needed.
