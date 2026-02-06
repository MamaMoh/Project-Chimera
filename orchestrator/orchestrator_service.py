"""Orchestrator – Chief Agent coordination. No logic implemented; see research/architecture_strategy.md."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OrchestratorState:
    state_version: str
    updated_at: str


@dataclass(frozen=True)
class Decision:
    task_id: str
    decision: str
    rationale: str
    state_version: str
    created_at: str


class OrchestratorService:
    """
    Coordinates Planner → Worker → Judge cycle.
    Contract and behaviour are defined in research/architecture_strategy.md and specs.
    """

    def __init__(self) -> None:
        pass

    def run_once(self, goal_description: str) -> Decision:
        """Run one cycle. Not implemented – implement to satisfy tests and specs."""
        raise NotImplementedError(
            "Orchestrator logic not implemented. "
            "See research/architecture_strategy.md §2.3–2.4 and specs/functional.md FR-6.0/FR-6.1."
        )
