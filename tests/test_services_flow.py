"""FR-6.0/FR-6.1: Planner–Worker–Judge flow produces a decision."""

import pytest

from orchestrator.orchestrator_service import OrchestratorService


class TestOrchestratorFlow:
    """Full Decision shape and valid decision values."""

    @pytest.fixture
    def orchestrator(self) -> OrchestratorService:
        return OrchestratorService()

    def test_returns_decision_in_allowed_set(
        self, orchestrator: OrchestratorService
    ) -> None:
        decision = orchestrator.run_once("Draft a welcome post.")
        assert decision.decision in {"approve", "escalate", "reject"}

    def test_decision_has_required_attributes(
        self, orchestrator: OrchestratorService
    ) -> None:
        decision = orchestrator.run_once("Generate a short tweet.")
        assert hasattr(decision, "task_id")
        assert hasattr(decision, "rationale")
        assert hasattr(decision, "state_version")
        assert hasattr(decision, "created_at")
        assert isinstance(decision.task_id, str)
        assert isinstance(decision.rationale, str)
        assert isinstance(decision.state_version, str)
        assert isinstance(decision.created_at, str)

    @pytest.mark.parametrize(
        "goal_description",
        [
            "Draft a welcome post.",
            "Generate a short tweet.",
            "Create a thread about AI.",
        ],
    )
    def test_flow_returns_decision_for_goals(
        self, orchestrator: OrchestratorService, goal_description: str
    ) -> None:
        decision = orchestrator.run_once(goal_description)
        assert decision.decision in {"approve", "escalate", "reject"}
        assert decision.task_id
        assert decision.rationale
