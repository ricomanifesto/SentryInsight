"""Closed product failure reasons and their fixed Runtime mapping.

The reason token is authoritative; the Runtime ``error_code`` is chosen from
the closed taxonomy. Coarse mappings are terminal and documented, and no reason
maps to ``unknown`` or ``worker_error``, which Runtime would retry.
``error_summary`` is the token plus bounded integers from a fixed key list, so
it can never carry messages, prompts, headers or exception names.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class ReasonMapping:
    runtime_code: str | None
    retry: bool = False


REASONS: dict[str, ReasonMapping] = {
    "snapshot_invalid": ReasonMapping("invalid_input"),
    "empty_source_set": ReasonMapping("invalid_input"),
    "effective_config_invalid": ReasonMapping("invalid_input"),
    "input_budget_exceeded": ReasonMapping("invalid_input"),
    "unsupported_manifest_version": ReasonMapping("unsupported_workflow"),
    "unsupported_workflow_version": ReasonMapping("unsupported_workflow"),
    "model_auth_rejected": ReasonMapping("invalid_input"),
    "provider_transient_response": ReasonMapping("dependency_unavailable", True),
    "provider_connect_failed": ReasonMapping("dependency_unavailable", True),
    "provider_retry_after_deferred": ReasonMapping("dependency_unavailable", True),
    "provider_budget_exhausted": ReasonMapping("side_effect_conflict"),
    "provider_intent_unresolved": ReasonMapping("side_effect_conflict"),
    "model_response_rejected": ReasonMapping("invalid_input"),
    "report_grounding_rejected": ReasonMapping("invalid_result"),
    "report_validation_rejected": ReasonMapping("invalid_result"),
    "report_artifact_invalid": ReasonMapping("invalid_result"),
    "report_policy_rejected": ReasonMapping("invalid_result"),
    "site_build_failed": ReasonMapping("invalid_result"),
    "archive_conflict": ReasonMapping("side_effect_conflict"),
    "staging_failed": ReasonMapping("invalid_result"),
    "checkpoint_store_failed": ReasonMapping("invalid_result"),
    "checkpoint_state_stale": ReasonMapping("invalid_result"),
    "worker_unclassified": ReasonMapping("invalid_result"),
    # The worker cannot report these to Runtime; it exits instead.
    "lease_lost": ReasonMapping(None),
    "runtime_unreachable": ReasonMapping(None),
    "runtime_auth_rejected": ReasonMapping(None),
    "runtime_draining": ReasonMapping(None),
    # Product-local publication outcomes in this slice.
    "publication_conflict": ReasonMapping(None),
    "publication_unresolved": ReasonMapping(None),
}
SUMMARY_KEYS = ("reserved", "attempts", "http_status", "provider_code")
AUTH_CODES = frozenset({401, 403})
PRE_SEND_FAULTS = frozenset({"connect_error", "connect_timeout", "pool_timeout"})
_RESERVED = re.compile(r"(?:^| )reserved=(\d+)(?: |$)")


def runtime_code(reason: str, *, fault: str | None = None) -> str | None:
    code = REASONS[reason].runtime_code
    if reason == "provider_connect_failed" and fault == "connect_timeout":
        return "dependency_timeout"
    return code


def is_retryable(reason: str) -> bool:
    return REASONS[reason].retry


def error_summary(reason: str, **values: Any) -> str:
    """Return the reason token followed by bounded ``key=int`` pairs."""
    if reason not in REASONS:
        raise ValueError("reason outside the closed set")
    unknown = set(values) - set(SUMMARY_KEYS)
    if unknown:
        raise ValueError("summary key outside the fixed list")
    parts = [reason]
    for key in SUMMARY_KEYS:
        value = values.get(key)
        if type(value) is int and 0 <= value < 10**6:
            parts.append(f"{key}={value}")
    return " ".join(parts)[:512]


def reported_reserved(summary: Any) -> int | None:
    if not isinstance(summary, str):
        return None
    match = _RESERVED.search(summary)
    return int(match.group(1)) if match else None


def provider_failure_reason(
    disposition: Mapping[str, Any],
    *,
    reserved: int,
    budget: int = 3,
    not_before: int | None = None,
    now: float | None = None,
    last_fault: str | None = None,
) -> str:
    """Map the verified legacy retry disposition to a closed reason.

    Auth is never retryable under the legacy rule because 401 and 403 are
    outside its retryable set, so either code means ``model_auth_rejected``.
    """
    if disposition.get("http_status") in AUTH_CODES or (
        disposition.get("provider_code") in AUTH_CODES
    ):
        return "model_auth_rejected"
    if disposition.get("retryable") is not True:
        return "model_response_rejected"
    if reserved >= budget:
        return "provider_budget_exhausted"
    if not_before is not None and (now is None or now < not_before):
        return "provider_retry_after_deferred"
    if last_fault in PRE_SEND_FAULTS:
        return "provider_connect_failed"
    return "provider_transient_response"
