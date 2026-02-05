# MCP Servers
Purpose: External capability providers exposed via MCP tools/resources.

## Runtime Inventory (Planned)

### mcp-server-social
- Tools: `post_content`, `reply_comment`, `fetch_mentions`
- Resources: `social://mentions/recent`, `social://timeline/latest`

### mcp-server-weaviate
- Tools: `search_memory`, `upsert_memory`
- Resources: `memory://semantic/{agent_id}`

### mcp-server-coinbase
- Tools: `get_balance`, `transfer_asset`, `deploy_token`
- Resources: `wallet://{agent_id}/balance`
