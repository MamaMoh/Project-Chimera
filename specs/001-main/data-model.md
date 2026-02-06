# Data Model: Core Swarm Orchestration (001-main)

**Branch**: 001-main | **Date**: 2026-02-04

## Entities

### Task

- **Purpose**: Unit of work produced by Planner from a goal.
- **Fields**: task_id (uuid), task_type, priority, context (goal_description, persona_constraints, required_resources, budget_limit_usd), acceptance_criteria, created_at, status.
- **Validation**: priority in {low, medium, high}; task_type non-empty; context and acceptance_criteria present.
- **State**: status in {pending, in_progress, review, complete}.

### Result

- **Purpose**: Output of Worker for a single Task.
- **Fields**: task_id, status (success | failure | retry), confidence_score (0.0–1.0), output (type + payload), artifacts, traces, created_at.
- **Validation**: confidence_score in [0.0, 1.0]; result linked to task_id.

### Decision

- **Purpose**: Judge outcome for a Result.
- **Fields**: task_id, decision (approve | reject | escalate), rationale, state_version, created_at.
- **Validation**: decision in {approve, reject, escalate}; state_version non-empty.

### Policy (governance)

- **Purpose**: Constraints applied during review (from agents/AGENTS.md and SOUL).
- **Representation**: Referenced by Judge; not a separate stored entity in 001-main.

## Relationships

- One Task → one Result (per execution).
- One Result → one Decision.
- Orchestrator holds current state_version for OCC.

## State Transitions

- Task: pending → in_progress (Worker picks up) → review (Result submitted) → complete (Decision approve) or re-queued (reject).
- Result status and Decision decision drive next step (commit vs escalate vs retry).
