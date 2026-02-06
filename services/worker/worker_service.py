from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List

from services.planner.planner_service import Task


@dataclass(frozen=True)
class Result:
    task_id: str
    status: str
    confidence_score: float
    output: Dict[str, Any]
    artifacts: List[str]
    traces: str
    created_at: str


class WorkerService:
    def execute_task(self, task: Task) -> Result:
        output_type, payload = self._build_output(task)
        return Result(
            task_id=task.task_id,
            status="success",
            confidence_score=0.85,
            output={"type": output_type, "payload": payload},
            artifacts=[],
            traces="Executed task with default worker logic.",
            created_at=datetime.now(timezone.utc).isoformat(),
        )

    def _build_output(self, task: Task) -> tuple[str, Dict[str, Any]]:
        if task.task_type == "generate_content":
            return "text", {"text": "Generated placeholder content."}
        if task.task_type == "reply_comment":
            return "text", {"text": "Generated reply placeholder."}
        if task.task_type == "execute_transaction":
            return "transaction", {
                "action": "get_balance",
                "amount": 0,
                "asset": "USDC",
            }
        return "text", {"text": "Unsupported task type."}
