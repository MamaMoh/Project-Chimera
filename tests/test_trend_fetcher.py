"""FR-2.2: Trend data structure and analyze_trends response contract."""

import uuid

import pytest

from skills.skill_analyze_trends.analyze_trends import analyze_trends


class TestTrendFetcherContract:
    """Response contract: request_id, trends array, pagination, metrics, analysis."""

    def test_calls_analyze_trends_and_returns_dict(self) -> None:
        result = analyze_trends("youtube")
        assert isinstance(result, dict)

    def test_response_has_request_id(self) -> None:
        result = analyze_trends("youtube")
        assert "request_id" in result
        assert isinstance(result["request_id"], str)
        uuid.UUID(result["request_id"])

    def test_response_has_trends_array(self) -> None:
        result = analyze_trends("youtube", {"limit": 3})
        assert "trends" in result
        assert isinstance(result["trends"], list)
        assert len(result["trends"]) >= 1

    def test_response_has_pagination(self) -> None:
        result = analyze_trends("youtube")
        assert "pagination" in result
        pag = result["pagination"]
        assert "page" in pag and "limit" in pag and "total" in pag
        assert isinstance(pag["total"], int)

    def test_each_trend_has_required_fields_and_types(self) -> None:
        result = analyze_trends("twitter")
        expected_fields = {
            "trend_id": str,
            "topic": str,
            "confidence_score": float,
            "source": str,
            "created_at": str,
        }
        for trend in result["trends"]:
            for field_name, field_type in expected_fields.items():
                assert field_name in trend, f"Missing field: {field_name}"
                assert isinstance(
                    trend[field_name], field_type
                ), f"Invalid type for {field_name}"

    def test_each_trend_has_metrics(self) -> None:
        result = analyze_trends("tiktok")
        for trend in result["trends"]:
            assert "metrics" in trend
            m = trend["metrics"]
            for key in ("views", "likes", "shares", "velocity"):
                assert key in m, f"Missing metrics.{key}"
                assert isinstance(m[key], (int, float))

    def test_each_trend_has_virality_score(self) -> None:
        result = analyze_trends("youtube")
        for trend in result["trends"]:
            assert "virality_score" in trend
            assert isinstance(trend["virality_score"], (int, float))

    def test_response_has_analysis_block(self) -> None:
        result = analyze_trends("youtube")
        assert "analysis" in result
        analysis = result["analysis"]
        assert analysis is not None
        assert "confidence" in analysis
        assert "content_gaps" in analysis
        assert "recommendations" in analysis
        assert isinstance(analysis["content_gaps"], list)
        assert isinstance(analysis["recommendations"], list)

    @pytest.mark.parametrize("platform", ["youtube", "tiktok", "twitter"])
    def test_multiple_platforms_return_contract(self, platform: str) -> None:
        result = analyze_trends(platform)
        assert "request_id" in result and "trends" in result
        assert result["error"] is None


class TestTrendFetcherErrors:
    """Error handling: invalid platform, error shape."""

    def test_invalid_platform_returns_error_block(self) -> None:
        result = analyze_trends("invalid_platform")
        assert "error" in result
        assert result["error"] is not None
        assert result["error"]["code"] == "INVALID_PLATFORM"
        assert "message" in result["error"]

    def test_error_response_has_request_id_and_empty_trends(self) -> None:
        result = analyze_trends("unknown")
        assert "request_id" in result
        assert result["trends"] == []
        assert result["pagination"]["total"] == 0
