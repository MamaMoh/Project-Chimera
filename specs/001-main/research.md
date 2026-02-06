# Research: Core Swarm Orchestration (001-main)

**Branch**: 001-main | **Date**: 2026-02-04

## Decisions

| Topic | Decision | Rationale |
|-------|----------|-----------|
| Orchestration pattern | Planner → Worker → Judge (FastRender-style) | Aligns with SRS and existing service layout; clear separation of plan, execution, review. |
| Task/Result/Decision shape | Structured dataclasses with ids, timestamps, confidence | Enables testing and traceability; matches specs/technical.md contracts. |
| External actions | MCP-only | Governance and audit; no direct API calls from agent logic. |
| Confidence thresholds | High ≥0.9 auto-approve; 0.7–0.9 escalate; &lt;0.7 reject | Matches NFR-1.1 and agents/AGENTS.md. |

## Alternatives Considered

- **Single monolithic agent**: Rejected; spec requires distinct Planner/Worker/Judge roles.
- **Direct API calls from Worker**: Rejected; FR-005 and constitution imply MCP-only.

## References

- Feature spec: `specs/001-main/spec.md`
- Platform technical spec: `specs/technical.md`
- Agent governance: `agents/AGENTS.md`
