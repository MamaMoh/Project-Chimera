"""Worker – executes tasks via skills. No logic implemented; see research/architecture_strategy.md."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Result:
    task_id: str
    status: str
    confidence_score: float
    output: dict[str, Any]
    artifacts: list[str]
    traces: str
    created_at: str


class WorkerService:
    """Executes Task and returns Result. Not implemented."""

    def execute_task(self, task: Any) -> Result:
        raise NotImplementedError(
            "Worker logic not implemented. See research/architecture_strategy.md §2.3 and §6."
        )
