"""FR-2.2: Trend data structure matches contract."""


def test_trend_payload_shape_and_types() -> None:
    trend_payload = {}
    expected_fields = {
        "trend_id": str,
        "topic": str,
        "confidence_score": float,
        "source": str,
        "created_at": str,
    }
    for field_name, field_type in expected_fields.items():
        assert field_name in trend_payload, f"Missing field: {field_name}"
        assert isinstance(
            trend_payload[field_name], field_type
        ), f"Invalid type for {field_name}"
