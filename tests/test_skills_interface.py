"""FR-3.0/FR-4.0: Skills input/output contracts enforced."""

import json
from pathlib import Path

import pytest

from skills.skill_analyze_trends.analyze_trends import analyze_trends


class TestSkillsSchema:
    """All skill schemas define required inputs (discovered from repo)."""

    def test_every_skill_schema_has_required_fields(
        self, schema_paths: list[Path]
    ) -> None:
        """Each skill schema must define required inputs and output contract (research §6–7)."""
        assert schema_paths, "No skill schemas found under skills/"
        for schema_path in schema_paths:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            required = set(schema.get("required", []))
            assert required, (
                f"No required fields defined in {schema_path.name}"
            )
            assert "output_schema" in schema or "output" in schema, (
                f"{schema_path.parent.name}: define output_schema for response contract."
            )

    def test_skill_download_video_in_schemas(
        self, schema_paths: list[Path]
    ) -> None:
        """Architecture §6 requires all listed skills; fail until all are present with schemas."""
        names = [p.parent.name for p in schema_paths]
        required_skills = {
            "skill_download_video",
            "skill_download_youtube",
            "skill_post_social",
            "skill_transcribe_audio",
            "skill_analyze_trends",
        }
        missing = required_skills - set(names)
        assert not missing, f"Missing skill schema(s): {sorted(missing)}"
        # All skills must define output contract per research (tests fail until added)
        assert len(names) >= 6, (
            "Architecture expects at least 6 skills with schemas (research/architecture_strategy.md §6)."
        )

    def test_every_skill_schema_defines_output_contract(
        self, schema_paths: list[Path]
    ) -> None:
        """Each skill schema must define output shape (see research/architecture_strategy.md)."""
        for schema_path in schema_paths:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            assert "output_schema" in schema or "output" in schema, (
                f"{schema_path.parent.name}: schema must define output_schema or output "
                "for response contract (see skill READMEs and research docs)."
            )


class TestSkillInputContracts:
    """Input contract checks for skills with runtime callables."""

    def test_post_social_required_inputs(self) -> None:
        """Contract: platform and text_content required (skill_post_social README)."""
        required = {"platform", "text_content"}
        payload = {"platform": "twitter", "text_content": "Hello"}
        missing = required - set(payload.keys())
        assert not missing, f"Missing required: {sorted(missing)}"
        # Fail until post_social() is implemented and returns contract-shaped output
        raise NotImplementedError(
            "post_social() not implemented. Implement to satisfy skill_post_social README contract."
        )

    @pytest.mark.parametrize("platform", ["youtube", "tiktok", "twitter"])
    def test_analyze_trends_accepts_platform(self, platform: str) -> None:
        result = analyze_trends(platform)
        assert "request_id" in result
        assert result["error"] is None


class TestSkillOutputContract:
    """Output contract: at least one skill returns request_id and result shape."""

    def test_analyze_trends_output_contract(self) -> None:
        result = analyze_trends("youtube")
        assert "request_id" in result
        assert "trends" in result
        assert "pagination" in result
        assert "analysis" in result
        assert "error" in result
        if result["error"] is None:
            assert isinstance(result["trends"], list)
            assert "page" in result["pagination"]
            assert "total" in result["pagination"]
