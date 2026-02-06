# MCP Servers

**Purpose:** Describe the Model Context Protocol (MCP) servers used at **runtime** to provide external capabilities (social, memory, commerce). All external actions in Chimera must go through **MCP tools only** (FR-4.0; see `specs/functional.md` and `agents/AGENTS.md`).

---

## Relationship to Research Documents

- **`research/architecture_strategy.md`** §5 describes agent communication protocols and OpenClaw integration; §7 lists MCP Sense for telemetry.
- **`research/tooling_strategy.md`** describes **developer** MCP servers (filesystem, git, shell) used during build and review, not production runtime.
- This directory documents **runtime** MCP servers that the Worker and skills will call (e.g. social post, memory search, wallet).

---

## Runtime Inventory (Planned)

| Server | Purpose | Tools (examples) | Resources (examples) |
|--------|---------|------------------|------------------------|
| **mcp-server-social** | Post content, reply, fetch mentions | `post_content`, `reply_comment`, `fetch_mentions` | `social://mentions/recent`, `social://timeline/latest` |
| **mcp-server-weaviate** | Semantic memory | `search_memory`, `upsert_memory` | `memory://semantic/{agent_id}` |
| **mcp-server-coinbase** | Wallet and on-chain actions (AgentKit) | `get_balance`, `transfer_asset`, `deploy_token` | `wallet://{agent_id}/balance` |

No runtime logic is implemented in this repo for these servers; they are specified here and in the specs. Implementation will connect to real MCP endpoints and respect `agents/AGENTS.md` and `policies/`.

---

## Policy

- All social and external actions **must** be executed via MCP tools only (FR-4.0).
- Credentials and secrets are read from environment only; never logged or echoed (`agents/AGENTS.md`).

---

## References

- `research/architecture_strategy.md` – §5 (Agent Communication), §7 (Infrastructure).
- `research/tooling_strategy.md` – Developer MCP (filesystem, git, shell).
- `specs/functional.md` – FR-4.0, FR-5.x (AgentKit).
