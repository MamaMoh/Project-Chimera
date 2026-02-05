# Roadmap
Purpose: Phase plan aligned to the SRS implementation roadmap.

## Phase 1: Core Swarm
- Establish Planner, Worker, and Judge service skeletons.
- Define Task and Result schemas.
- Implement queue contracts (Redis).

## Phase 2: MCP Integration
- Stand up MCP servers for social, memory, and commerce.
- Implement MCP client in agent runtime.
- Validate MCP-only external actions.

## Phase 3: Agentic Commerce
- Integrate Coinbase AgentKit for wallets and transfers.
- Implement CFO Judge budget checks.
- Add monitoring and audit trails.
