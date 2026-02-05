"""FR-4.0: External actions must go through MCP tools."""

from pathlib import Path


def test_mcp_only_policy_present() -> None:
    policy_path = Path(__file__).resolve().parents[1] / "agents" / "AGENTS.md"
    policy_text = policy_path.read_text(encoding="utf-8")
    assert "MCP" in policy_text and "only" in policy_text
