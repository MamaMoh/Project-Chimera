"""FR-CORE-002: Skills input/output contracts are enforced."""


def test_skill_post_social_contract() -> None:
    payload = {}
    required_inputs = {"platform", "text_content"}
    assert required_inputs.issubset(payload.keys())
