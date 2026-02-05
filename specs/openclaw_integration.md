# OpenClaw Integration
Purpose: Define integration contracts, endpoints, and failure handling.

## Scope
This spec governs how agents interact with OpenClaw capabilities through MCP.

## Integration Contract
- Access method: MCP tools and resources only.
- Authentication: managed by the MCP server, not by agents.
- Rate limits: enforced at MCP server boundary.

## Failure Handling
- Transient errors: retry up to 2 times with backoff.
- Persistent errors: escalate to HITL and log incident.
