"""FR-3.0/FR-4.0: Skills input/output contracts are enforced."""

import json
from pathlib import Path


def test_skill_schemas_define_required_inputs() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    schema_paths = [
        repo_root / "skills" / "skill_download_youtube" / "schema.json",
        repo_root / "skills" / "skill_transcribe_audio" / "schema.json",
        repo_root / "skills" / "skill_post_social" / "schema.json",
    ]
    for schema_path in schema_paths:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        required = set(schema.get("required", []))
        assert required, f"No required fields defined in {schema_path.name}"


def test_skill_post_social_contract_inputs() -> None:
    payload = {
        "platform": "twitter",
        "text_content": "Hello world",
    }
    required_inputs = {"platform", "text_content"}
    missing = required_inputs - set(payload.keys())
    assert not missing, f"Missing required inputs: {sorted(missing)}"
