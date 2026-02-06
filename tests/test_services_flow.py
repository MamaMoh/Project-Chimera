"""FR-6.0/FR-6.1: Planner-Worker-Judge flow produces a decision."""

from orchestrator.orchestrator_service import OrchestratorService


def test_orchestrator_flow_returns_decision() -> None:
    orchestrator = OrchestratorService()
    decision = orchestrator.run_once("Draft a welcome post.")
    assert decision.decision in {"approve", "escalate", "reject"}
