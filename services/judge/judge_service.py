from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from services.worker.worker_service import Result


@dataclass(frozen=True)
class Decision:
    task_id: str
    decision: str
    rationale: str
    state_version: str
    created_at: str


class JudgeService:
    def review_result(self, result: Result, state_version: str) -> Decision:
        decision, rationale = self._decide(result)
        return Decision(
            task_id=result.task_id,
            decision=decision,
            rationale=rationale,
            state_version=state_version,
            created_at=datetime.now(timezone.utc).isoformat(),
        )

    def _decide(self, result: Result) -> tuple[str, str]:
        if result.confidence_score >= 0.9:
            return "approve", "High confidence score."
        if result.confidence_score >= 0.7:
            return "escalate", "Medium confidence score; HITL required."
        return "reject", "Low confidence score."
