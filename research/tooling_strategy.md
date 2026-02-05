# Tooling Strategy
Purpose: Define developer MCP tooling and runtime agent skills.

## Developer MCP Tooling (for engineering)
- git-mcp: version control operations
- filesystem-mcp: file navigation and edits
- terminal-mcp: controlled command execution

## Runtime MCP Servers (for agents)
- mcp-server-social: publish and interact on platforms
- mcp-server-weaviate: semantic memory retrieval
- mcp-server-coinbase: AgentKit wallet operations

## Skills vs Tools
- **Skills** are internal capability packages (e.g., `skill_transcribe_audio`)
- **MCP Servers** are external bridges and must be the only path to external APIs

## Governance
- All runtime tool calls must be logged via MCP Sense.
- Credentials are stored in environment variables, never in code.
