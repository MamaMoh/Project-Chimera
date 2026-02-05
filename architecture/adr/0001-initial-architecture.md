# ADR 0001: Initial Architecture

## Status
Accepted

## Context
Project Chimera requires a scalable, autonomous influencer system with strong governance. The SRS mandates MCP for external connectivity, a Planner-Worker-Judge swarm for internal task execution, and a single orchestrator model with HITL safety.

## Decision
- Use a Hub-and-Spoke topology with a Central Orchestrator as the MCP Host.
- Implement the FastRender swarm pattern with Planner, Worker, and Judge services.
- Enforce all external actions via MCP tools; no direct API calls from agents.
- Use SOUL.md for immutable persona definitions and AGENTS.md for global governance.
- Apply HITL gating using confidence thresholds and sensitive-topic policies.

## Consequences
- Enables horizontal scaling of Workers without shared state coupling.
- Centralizes policy changes and ensures global behavioral consistency.
- Requires MCP server maintenance for each external integration.
- Adds operational overhead for governance and review workflows, but improves safety.
