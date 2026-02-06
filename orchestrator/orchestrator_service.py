from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

from services.judge.judge_service import Decision, JudgeService
from services.planner.planner_service import PlannerService
from services.worker.worker_service import WorkerService


@dataclass(frozen=True)
class OrchestratorState:
    state_version: str
    updated_at: str


class OrchestratorService:
    def __init__(self) -> None:
        self._planner = PlannerService()
        self._worker = WorkerService()
        self._judge = JudgeService()
        self._state = OrchestratorState(
            state_version=str(uuid4()),
            updated_at=datetime.now(timezone.utc).isoformat(),
        )

    def run_once(self, goal_description: str) -> Decision:
        task = self._planner.create_task(
            task_type="generate_content",
            goal_description=goal_description,
            required_resources=[],
            priority="medium",
        )
        result = self._worker.execute_task(task)
        decision = self._judge.review_result(result, self._state.state_version)
        self._state = OrchestratorState(
            state_version=str(uuid4()),
            updated_at=datetime.now(timezone.utc).isoformat(),
        )
        return decision
