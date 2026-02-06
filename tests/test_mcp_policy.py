"""FR-4.0: External actions must go through MCP tools."""

from pathlib import Path

import pytest


class TestMCPPolicyDocument:
    """Policy document exists and states MCP-only for external actions."""

    def test_policy_file_exists(self, repo_root: Path) -> None:
        policy_path = repo_root / "agents" / "AGENTS.md"
        assert policy_path.is_file(), f"Missing {policy_path.relative_to(repo_root)}"
        # FR-4.0: Policy must explicitly state MCP tools only (fail until doc updated)
        text = policy_path.read_text(encoding="utf-8")
        assert "MCP tools only" in text, (
            "AGENTS.md must state 'MCP tools only' for external actions (see research)."
        )

    def test_policy_mentions_mcp_and_only(self, repo_root: Path) -> None:
        """FR-4.0: Policy must state external actions go via MCP tools only (see research)."""
        policy_path = repo_root / "agents" / "AGENTS.md"
        text = policy_path.read_text(encoding="utf-8")
        assert "MCP tools only" in text, (
            "Policy must state 'MCP tools only' for external actions (research/architecture_strategy.md)."
        )

    def test_policy_states_mcp_tools_only_for_external_actions(
        self, repo_root: Path
    ) -> None:
        """FR-4.0: Document must state that external actions go via MCP tools only."""
        policy_path = repo_root / "agents" / "AGENTS.md"
        text = policy_path.read_text(encoding="utf-8")
        assert "MCP tools only" in text, (
            "Policy must explicitly state 'MCP tools only' for external actions "
            "(see specs/functional.md FR-4.0 and research/architecture_strategy.md)."
        )
