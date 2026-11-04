"""Allowlisted diagnostics and recovery advice, separate from report evidence."""

import json
import math
import os
from pathlib import Path
import re
import stat
import tempfile

from .retry_policy import REQUEST_STATES, retry_decision
from .validation_diagnostics import UNKNOWN_CODE, sanitize_diagnostic

ENV_PATH = "SENTRYINSIGHT_FAILURE_RECEIPT"
MAX_BYTES = 8192
STATUSES = frozenset(
    {
        "started",
        "failed",
        "completed",
        "completed_with_review",
        "completed_unchanged",
        "completed_with_warnings",
        "review_required",
        "uncertain",
    }
)
_IDENTITY_FIELDS = {
    "run_id": ("GITHUB_RUN_ID", r"[0-9]{1,20}"),
    "run_attempt": ("GITHUB_RUN_ATTEMPT", r"[0-9]{1,5}"),
    "source_revision": ("GITHUB_SHA", r"[a-f0-9]{40}"),
    "admission_key": (
        "SENTRYINSIGHT_ADMISSION_KEY",
        r"(?:run:[0-9]+|digest:[a-f0-9]{40})",
    ),
}
_RECEIPT_FIELDS = frozenset(
    {
        "schema_version",
        *_IDENTITY_FIELDS,
        "plan_id",
        "status",
        "report_generated",
        "request",
        "diagnostic",
        "retry",
    }
)


class FailureReceiptError(RuntimeError):
    def __init__(self):
        super().__init__("Failure receipt invalid or unavailable")


def _mapping(value):
    return value if type(value) is dict else {}


def _label(value, pattern):
    if type(value) is str and re.fullmatch(pattern, value):
        return value
    return None


def _integer(value, low, high):
    if type(value) is int and low <= value <= high:
        return value
    return None


def sanitize_request(value: object) -> dict:
    raw = _mapping(value)
    usage = raw.get("usage")
    if type(usage) is dict:
        usage = {
            key: number
            for key in ("prompt_tokens", "completion_tokens", "total_tokens", "cost")
            if type(number := usage.get(key)) in (int, float)
            and 0 <= number <= 2**63
            and math.isfinite(number)
        }
    else:
        usage = None
    state = raw.get("state")
    if type(state) is not str or state not in REQUEST_STATES:
        state = "uncertain"
    return {
        "state": state,
        "attempts": _integer(raw.get("attempts"), 0, 3),
        "limit": _integer(raw.get("limit"), 1, 3),
        "request_sha256": _label(raw.get("request_sha256"), r"[a-f0-9]{64}"),
        "http_status": _integer(raw.get("http_status"), 100, 599),
        "provider_code": _integer(raw.get("provider_code"), 100, 599),
        "usage": usage,
    }


def decision_for(status, diagnostic, request, report_generated):
    advice = retry_decision(
        request["state"], attempts=request["attempts"], limit=request["limit"]
    )

    def advise(action, reason):
        return {**advice, "action": action, "reason": reason, "delay_seconds": None}

    if status in {"started", "uncertain"}:
        return advise("reconcile", "run_not_terminal")
    if request["state"] in {"reserved", "uncertain", "permanent_rejection"}:
        return advice
    if status == "review_required":
        return advise("review_required", "source_review_required")
    if diagnostic is not None:
        stage = diagnostic["stage"]
        reasons = set(diagnostic["codes"])
        unknown = {
            UNKNOWN_CODE,
            "request_budget_unresolved",
            "analysis_exception",
            "model_request_failed",
        }
        if stage == "unknown_validation_stage" or reasons.intersection(unknown):
            return advise("reconcile", "unclassified_failure")
        if stage == "site_publication":
            return advise("recover_publication", "publication_failed")
        if stage != "analysis" or reasons.intersection(
            {
                "input_budget_exceeded",
                "model_output_limit_exceeded",
                "model_auth_rejected",
            }
        ):
            return advise("repair_required", "validation_or_configuration_failed")
    if status.startswith("completed") or report_generated:
        return advise("stop", "run_completed")
    return advice


def make_receipt(
    state: dict | None, *, request=None, started=False, environ=None
) -> dict:
    state = _mapping(state)
    env = os.environ if environ is None else environ
    status = "started" if started else state.get("status", "uncertain")
    if type(status) is not str or status not in STATUSES:
        status = "uncertain"
    if request is None:
        request = (
            {"state": "not_sent", "attempts": 0, "limit": 3}
            if started
            else _mapping(state.get("analysis_results")).get("request_metadata")
        )
    request = sanitize_request(request)
    failure = state.get("failure_diagnostic", state.get("failure"))
    diagnostic = None
    if failure is not None or status == "failed":
        diagnostic = sanitize_diagnostic(failure)
    generated = state.get("report_generated") is True and status in {
        "completed",
        "completed_with_review",
    }
    identity = {
        field: _label(env.get(env_name), pattern)
        for field, (env_name, pattern) in _IDENTITY_FIELDS.items()
    }
    return {
        "schema_version": 1,
        **identity,
        "plan_id": _label(
            _mapping(state.get("source_review_plan")).get("plan_id"), r"[a-f0-9]{64}"
        ),
        "status": status,
        "report_generated": generated,
        "request": request,
        "diagnostic": diagnostic,
        "retry": decision_for(status, diagnostic, request, generated),
    }


def _encode(value):
    return (json.dumps(value, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")


def validate_receipt(value) -> dict:
    if type(value) is not dict or set(value) != _RECEIPT_FIELDS:
        raise FailureReceiptError()
    state = {
        "status": value["status"],
        "report_generated": value["report_generated"],
        "source_review_plan": {"plan_id": value["plan_id"]},
    }
    if value["diagnostic"] is not None:
        state["failure_diagnostic"] = value["diagnostic"]
    env = {env_name: value[field] for field, (env_name, _) in _IDENTITY_FIELDS.items()}
    canonical = make_receipt(state, request=value["request"], environ=env)
    # Encoding distinguishes booleans from integers and refuses nonfinite data.
    if _encode(value) != _encode(canonical):
        raise FailureReceiptError()
    return value


def read_receipt(path: Path) -> dict:
    try:
        descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
        with os.fdopen(descriptor, "rb") as stream:
            info = os.fstat(stream.fileno())
            safe = (
                stat.S_ISREG(info.st_mode)
                and stat.S_IMODE(info.st_mode) == 0o600
                and info.st_size <= MAX_BYTES
            )
            if not safe:
                raise FailureReceiptError()
            data = stream.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            raise FailureReceiptError()
        return validate_receipt(json.loads(data))
    except (OSError, ValueError, TypeError, KeyError):
        raise FailureReceiptError() from None


def write_receipt(path: Path, value: dict) -> None:
    data = _encode(validate_receipt(value))
    if len(data) > MAX_BYTES or path.is_symlink():
        raise FailureReceiptError()
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=".failure-receipt-", dir=path.parent
    )
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def record_request(path: Path, request: dict) -> None:
    receipt = read_receipt(path)
    receipt["request"] = sanitize_request(request)
    receipt["retry"] = decision_for(
        receipt["status"],
        receipt["diagnostic"],
        receipt["request"],
        receipt["report_generated"],
    )
    write_receipt(path, receipt)


def finish_receipt(path: Path, state: dict | None) -> None:
    request = read_receipt(path)["request"]
    if request["attempts"] in (None, 0):
        analysis = _mapping(_mapping(state).get("analysis_results"))
        request = analysis.get("request_metadata", request)
    write_receipt(path, make_receipt(state, request=request))
