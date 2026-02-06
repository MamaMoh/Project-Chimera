from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List
from uuid import uuid4


@dataclass(frozen=True)
class Task:
    task_id: str
    task_type: str
    priority: str
    context: dict
    acceptance_criteria: List[str]
    created_at: str
    status: str


class PlannerService:
    def create_task(
        self,
        task_type: str,
        goal_description: str,
        required_resources: List[str],
        priority: str = "medium",
        persona_constraints: List[str] | None = None,
        budget_limit_usd: float | None = None,
        acceptance_criteria: List[str] | None = None,
    ) -> Task:
        if priority not in {"low", "medium", "high"}:
            raise ValueError("priority must be low, medium, or high")

        context = {
            "goal_description": goal_description,
            "persona_constraints": persona_constraints or [],
            "required_resources": required_resources,
            "budget_limit_usd": budget_limit_usd,
        }
        return Task(
            task_id=str(uuid4()),
            task_type=task_type,
            priority=priority,
            context=context,
            acceptance_criteria=acceptance_criteria or [],
            created_at=datetime.now(timezone.utc).isoformat(),
            status="pending",
        )
