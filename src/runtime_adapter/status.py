"""Read-only status of one job from durable product state and the run document.

Every value is a fixed token, a count, a digest, a bounded integer or a
timestamp. Reserved submissions are budget charges, not a billing count; an
open or ambiguous intent is reported as uncertain provider acceptance; a
prepared artifact never reads as published.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .checkpoint import ledger_view
from .send_gate import DEFAULT_BUDGET

_LABELS = (
    ("run_id", "run id"),
    ("run_state", "Runtime state"),
    ("attempt", "leases granted"),
    ("leases_remaining", "leases remaining"),
    ("lease_version", "lease version"),
    ("runtime_error_code", "Runtime error code"),
    ("product_stage", "product stage"),
    ("product_reason", "product reason"),
    ("retry_eligible", "Runtime retry pending"),
    ("reserved", "reserved provider submissions (not a billing count)"),
    ("budget_remaining", "provider budget remaining"),
    ("known_outcomes", "known provider outcomes"),
    ("failed_before_forward", "refused before forwarding"),
    ("uncertain_provider_acceptance", "uncertain provider acceptance"),
    ("provider_intent", "provider intent"),
    ("replays", "captured outcome replays"),
    ("not_before", "provider not-before"),
    ("artifact_sha256", "prepared artifact (not published)"),
    ("publication", "publication"),
    ("note", "note"),
)


def _iso(value: float | None) -> str | None:
    if value is None:
        return None
    moment = datetime.fromtimestamp(value, timezone.utc)
    return moment.isoformat(timespec="seconds").replace("+00:00", "Z")


def job_status(
    record: dict[str, Any] | None,
    run: dict[str, Any] | None,
    *,
    now: float | None = None,
    budget: int = DEFAULT_BUDGET,
) -> dict[str, Any]:
    view = ledger_view(record) if record else None
    disposition = (record or {}).get("disposition") or {}
    publication = (record or {}).get("publication") or {}
    artifact = (record or {}).get("artifact") or {}
    run = run or {}
    uncertain = (
        len(view.open_reservations) + len(view.ambiguous_reservations) if view else None
    )
    attempt, max_attempts = run.get("attempt"), run.get("max_attempts")
    not_before = view.not_before if view else None
    note = None
    if (
        run.get("state") == "failed"
        and disposition.get("reason") == "provider_retry_after_deferred"
        and attempt == max_attempts
    ):
        note = "lease_budget_exhausted_before_provider_not_before"
    elif run.get("state") == "running" and uncertain:
        note = "no_progress_without_claim_traffic"
    return {
        "run_id": run.get("run_id"),
        "run_state": run.get("state"),
        "attempt": attempt,
        "leases_remaining": (
            max_attempts - attempt
            if type(attempt) is int and type(max_attempts) is int
            else None
        ),
        "lease_version": run.get("lease_version"),
        "runtime_error_code": run.get("error_code"),
        "product_stage": (record or {}).get("stage"),
        "product_reason": disposition.get("reason"),
        "retry_eligible": run.get("state") == "retry_wait",
        "reserved": view.reserved if view else None,
        "budget_remaining": budget - view.reserved if view else None,
        "known_outcomes": view.resolved if view else None,
        "failed_before_forward": len(view.failed_before_forward) if view else None,
        "uncertain_provider_acceptance": uncertain,
        "provider_intent": "unresolved" if uncertain else "none_open",
        "replays": view.replays if view else None,
        "not_before": _iso(not_before),
        "not_before_remaining_seconds": (
            max(0, int(not_before - now))
            if not_before is not None and now is not None
            else None
        ),
        "artifact_sha256": artifact.get("sha256"),
        "publication": publication.get("state", "not_published"),
        "note": note,
    }


def render_status(status: dict[str, Any]) -> str:
    rows = ["| field | value |", "|---|---|"]
    for key, label in _LABELS:
        value = status.get(key)
        rows.append(f"| {label} | {'-' if value is None else value} |")
    return "\n".join(rows) + "\n"
