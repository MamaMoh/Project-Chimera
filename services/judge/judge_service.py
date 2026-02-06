"""Judge – reviews Result and returns Decision. No logic implemented; see research/architecture_strategy.md."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Decision:
    task_id: str
    decision: str
    rationale: str
    state_version: str
    created_at: str


class JudgeService:
    """Reviews result → approve / escalate / reject. Not implemented."""

    def review_result(self, result: Any, state_version: str) -> Decision:
        raise NotImplementedError(
            "Judge logic not implemented. See research/architecture_strategy.md §2.3 and §3."
        )
