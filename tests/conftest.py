"""Shared pytest fixtures and configuration."""

from pathlib import Path

import pytest


@pytest.fixture
def repo_root() -> Path:
    """Project root (parent of tests/)."""
    return Path(__file__).resolve().parents[1]


@pytest.fixture
def schema_paths(repo_root: Path) -> list[Path]:
    """All skill schema.json paths under skills/."""
    skills_dir = repo_root / "skills"
    if not skills_dir.is_dir():
        return []
    return sorted(
        p for p in skills_dir.glob("*/schema.json") if p.is_file()
    )
