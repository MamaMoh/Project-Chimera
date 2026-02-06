# Orchestrator
Purpose: Central control plane for fleet state and operations.

## Responsibilities
- Maintain global state and campaign goals.
- Coordinate Planner-Worker-Judge lifecycle.
- Enforce budget limits and governance policies.
- Aggregate telemetry and surface alerts.

## Interfaces
- Accepts high-level goals from operators.
- Publishes tasks to Planner queues.
- Receives Judge decisions for commit or escalation.

## Data Contracts
- Uses Task, Result, and Decision schemas defined in `specs/technical.md`.

## Operational Notes
- All external actions route through MCP servers.
- HITL review is triggered by Judge decisions.
