# Agent Protocols
Purpose: Define input/output formats, shared conventions, and handoffs.

## Artifact Naming
- Task artifacts: `task-{uuid}.json`
- Result artifacts: `result-{uuid}.json`
- Review notes: `review-{uuid}.md`

## Required Result Fields
- status: success | failure | retry
- confidence_score: float (0.0 - 1.0)
- output: primary payload (text, media, or transaction request)
- traces: short reasoning summary
- created_at: ISO-8601 timestamp

## MCP Usage Rules
- Tools are the only execution pathway for external actions.
- Resources are read-only; do not mutate via resource paths.
- Prompts must be referenced by name and version.

## Handoff Protocol
- Planner -> Worker: task + acceptance criteria + required resources.
- Worker -> Judge: result + confidence score + artifacts.
- Judge -> Planner: approval or rejection with rationale.

## Error Handling
- Retries are allowed up to 2 times with updated prompts.
- After 2 failures, escalate to HITL or flag as blocked.
