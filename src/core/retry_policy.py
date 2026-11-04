"""Request observations determine advice, never permission for a new episode."""

import math

MAX_ATTEMPTS = 3
MAX_RETRY_DELAY = 30.0
REQUEST_STATES = frozenset(
    {
        "not_sent",
        "reserved",
        "retryable_rejection",
        "response_received",
        "permanent_rejection",
        "uncertain",
        "deferred_rejection",
    }
)
DISPOSITIONS = REQUEST_STATES.difference({"reserved"})


def retry_decision(state: str, *, attempts: int, limit: int, delay: float = 0) -> dict:
    coherent = (
        type(state) is str
        and state in REQUEST_STATES
        and type(attempts) is int
        and type(limit) is int
        and 1 <= limit <= MAX_ATTEMPTS
        and 0 <= attempts <= limit
        and type(delay) in (int, float)
        and 0 <= delay
        and math.isfinite(delay)
    )
    decision: dict[str, str | int | float | None] = {
        "action": "reconcile",
        "reason": "request_outcome_unknown",
        "remaining_attempts": limit - attempts if coherent else 0,
        "delay_seconds": None,
    }
    if not coherent:
        return decision
    terminal = {
        "response_received": ("stop", "response_received"),
        "permanent_rejection": ("repair_required", "permanent_rejection"),
        "deferred_rejection": ("review_required", "retry_after_exceeds_budget"),
    }
    if state in terminal:
        decision["action"], decision["reason"] = terminal[state]
    elif state in {"not_sent", "retryable_rejection"}:
        if attempts == limit:
            decision.update(action="stop", reason="attempt_budget_exhausted")
        elif delay > MAX_RETRY_DELAY:
            decision.update(
                action="review_required", reason="retry_after_exceeds_budget"
            )
        else:
            decision.update(
                action="retry_after",
                reason="transient_rejection",
                delay_seconds=delay,
            )
    return decision
