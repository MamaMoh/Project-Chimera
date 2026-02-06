from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4
from typing import Optional

from services.judge.judge_service import Decision, JudgeService
from services.planner.planner_service import PlannerService
from services.worker.worker_service import WorkerService


@dataclass(frozen=True)
class OrchestratorState:
    state_version: str
    updated_at: str


class OrchestratorService:
    """
    OrchestratorService coordinates the Planner, Worker, and Judge services.
    
    Features:
    - Tracks state version with timestamp for traceability
    - Supports test/failure injection for TDD
    - Fully mockable sub-services for pytest
    """
    def __init__(
        self,
        planner: Optional[PlannerService] = None,
        worker: Optional[WorkerService] = None,
        judge: Optional[JudgeService] = None,
        fail_worker: bool = False
    ) -> None:
        self._planner = planner or PlannerService()
        self._worker = worker or WorkerService()
        self._judge = judge or JudgeService()
        self._fail_worker = fail_worker
        self._state = OrchestratorState(
            state_version=str(uuid4()),
            updated_at=datetime.now(timezone.utc).isoformat()
        )

    def run_once(self, goal_description: str) -> Decision:
        """Run one cycle of planning → execution → judging."""
        # 1. Planning
        task = self._planner.create_task(
            task_type="generate_content",
            goal_description=goal_description,
            required_resources=[],
            priority="medium"
        )

        # 2. Execution
        if self._fail_worker:
            # Injected failure for TDD / contract testing
            result = {
                "error": {
                    "code": "WORKER_FAILURE",
                    "message": "Injected failure for testing"
                }
            }
        else:
            result = self._worker.execute_task(task)

        # 3. Judging / decision-making
        decision = self._judge.review_result(result, self._state.state_version)

        # 4. Update orchestrator state
        self._state = OrchestratorState(
            state_version=str(uuid4()),
            updated_at=datetime.now(timezone.utc).isoformat()
        )

        return decision

    @property
    def state(self) -> OrchestratorState:
        """Return current orchestrator state for inspection."""
        return self._state
