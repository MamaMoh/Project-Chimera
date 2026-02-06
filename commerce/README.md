# Agentic Commerce

**Purpose:** Define how Chimera integrates with **Coinbase AgentKit** for wallet and on-chain actions. No implementation is present; behaviour is specified in the specs and research.

---

## Role in the Architecture

- **`specs/functional.md`** FR-5.0: Each agent shall be assigned a unique non-custodial wallet via AgentKit. FR-5.1: Support on-chain actions (transfer, deploy token, balance). FR-5.2: A CFO Judge shall enforce budget limits and flag anomalies.
- **`research/architecture_strategy.md`** §7 lists the stack; commerce is delivered via MCP (e.g. `mcp-server-coinbase` in **`mcp_servers/README.md`**).

---

## Intended Capabilities (To Be Implemented)

1. **Wallet** – Non-custodial wallet per agent; balance and asset queries via MCP.
2. **Actions** – Transfer, deploy token, and other on-chain actions through AgentKit/MCP only.
3. **Governance** – CFO Judge (or equivalent) enforces budget limits and flags anomalies before committing.

---

## Implementation Status

- **Current:** Specification only. No wallet or on-chain logic is implemented in this directory.
- **References:** `specs/functional.md` FR-5.x, `mcp_servers/README.md`, `research/architecture_strategy.md`.
