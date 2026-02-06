"""Planner – creates tasks from goals. No logic implemented; see research/architecture_strategy.md."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Task:
    task_id: str
    task_type: str
    priority: str
    context: dict
    acceptance_criteria: list
    created_at: str
    status: str


class PlannerService:
    """Creates Task with goal, priority, acceptance_criteria. Not implemented."""

    def create_task(
        self,
        task_type: str,
        goal_description: str,
        required_resources: list[str],
        priority: str = "medium",
        persona_constraints: list[str] | None = None,
        budget_limit_usd: float | None = None,
        acceptance_criteria: list[str] | None = None,
    ) -> Task:
        raise NotImplementedError(
            "Planner logic not implemented. See research/architecture_strategy.md §2.3."
        )
