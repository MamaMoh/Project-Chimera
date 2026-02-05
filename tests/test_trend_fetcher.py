"""FR-CORE-001: Trend data structure matches contract."""


def test_trend_payload_shape() -> None:
    trend_payload = {}
    required_keys = {"trend_id", "topic", "confidence_score", "source", "created_at"}
    assert required_keys.issubset(trend_payload.keys())
