# Agent Roles
Purpose: Define planner, implementer, reviewer, and tester responsibilities.

## Planner
- Owns goal decomposition and task DAG creation.
- Defines acceptance criteria for each task.
- Re-plans when context shifts or tasks fail.

## Worker
- Executes one atomic task per run.
- Uses MCP tools only; no direct external API calls.
- Returns a structured result artifact for review.

## Judge
- Validates outputs against acceptance criteria and policies.
- Performs optimistic concurrency checks before commit.
- Routes to HITL when confidence or safety triggers require it.

## Reviewer (Human)
- Approves, rejects, or edits escalated outputs.
- Provides feedback signals for future retries.

## Orchestrator
- Manages fleet state, budgets, and resource allocation.
- Owns global configuration and campaign activation.
