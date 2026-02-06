# Memory Layer

**Purpose:** Define how the system stores and retrieves semantic, episodic, and transactional data for agents. This document aligns with the architecture and tooling strategy; no runtime memory implementation is required in this directory yet.

---

## Role in the Architecture

- **`research/architecture_strategy.md`** §4 describes the database strategy: PostgreSQL (primary), Redis (caching), Elasticsearch (search/analytics). Agent memory and context can use a mix of structured stores and caches.
- **`research/tooling_strategy.md`** does not define production memory servers; runtime MCP servers (e.g. Weaviate for semantic search) are listed in **`mcp_servers/README.md`** as planned (e.g. `mcp-server-weaviate` with `search_memory`, `upsert_memory`).

---

## Intended Contracts (To Be Implemented)

1. **Semantic memory** – Vector search over personas, memories, and context snippets (e.g. via Weaviate MCP).
2. **Short-term / episodic** – Task context, recent interactions (e.g. Redis or in-process with TTL).
3. **Transactional** – User, content, engagement, trend data in PostgreSQL (see architecture §4 ERD).

PII must not be stored in long-term memory without explicit approval (`agents/AGENTS.md`).

---

## Implementation Status

- **Current:** Specification only. No memory read/write logic is implemented in this directory.
- **References:** `research/architecture_strategy.md` §4, `mcp_servers/README.md`, `agents/AGENTS.md` (data handling).
