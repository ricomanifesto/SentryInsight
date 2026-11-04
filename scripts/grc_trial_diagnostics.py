"""Closed, value-free diagnostic records shared by the sender and private worker."""

import asyncio

VERSION = 1
STAGES = frozenset({"trial", "calibration", "analysis", "plan", "control", "worker"})
PHASES = frozenset(
    {
        "context",
        "source_guard",
        "calibration_source",
        "calibration_worker",
        "calibration_payload",
        "calibration_host",
        "claim_create",
        "claim_persistence",
        "claim_close",
        "request_send",
        "response_status",
        "response_read",
        "response_validation",
        "response_close",
        "derive_worker",
        "derived_body_validation",
        "plan_binding",
        "replay_worker",
        "host_validation",
        "final_source_guard",
        "report_fence",
        "worker_launch",
        "worker_io",
        "worker_wait",
        "worker_protocol",
        "worker_cleanup",
        "worker_scratch_create",
        "worker_scratch_cleanup",
        "worker_context",
        "worker_input",
        "worker_import",
        "worker_workflow",
        "worker_request_capture",
        "worker_analysis_parser",
        "worker_recognition_gate",
        "worker_derived_capture",
        "worker_host_validation",
        "worker_complete",
        "complete",
        "sender_open",
        "sender_execution",
        "sender_close",
        "control_close",
    }
)
CODES = frozenset(
    {
        "in_progress",
        "ok",
        "unknown_failure",
        "timeout",
        "cancelled",
        "check_refused",
        "persistence_unknown",
        "claim_unavailable",
        "http_rejected",
        "response_refused",
        "response_read_refused",
        "derived_body_refused",
        "host_refused",
        "source_refused",
        "report_fence_refused",
        "worker_launch_failed",
        "worker_exit_failed",
        "invalid_worker_envelope",
        "worker_output_refused",
        "calibration_refused",
    }
)
WORKER_PHASES = frozenset(
    {
        "worker_context",
        "worker_input",
        "worker_import",
        "worker_workflow",
        "worker_request_capture",
        "worker_analysis_parser",
        "worker_recognition_gate",
        "worker_derived_capture",
        "worker_host_validation",
    }
)
WORKER_CODES = frozenset({"unknown_failure", "timeout", "cancelled", "check_refused"})


def record(stage, phase, code):
    if type(stage) is not str or type(phase) is not str or type(code) is not str:
        raise ValueError("Diagnostic record refused")
    if stage not in STAGES or phase not in PHASES or code not in CODES:
        raise ValueError("Diagnostic record refused")
    return {"stage": stage, "phase": phase, "code": code}


def validate(value):
    if type(value) is not dict or set(value) != {"stage", "phase", "code"}:
        raise ValueError("Diagnostic record refused")
    return record(value["stage"], value["phase"], value["code"])


class Error(RuntimeError):
    def __init__(self, diagnostic, secondary=()):
        super().__init__("Closed trial stopped")
        self.diagnostic = validate(diagnostic)
        values = [validate(value) for value in secondary]
        self.secondary = values[:3]
        self.observed = values[-1] if values else self.diagnostic
        self.claim_recorded = False

    def add_secondary(self, value):
        value = validate(value)
        self.observed = value
        if len(self.secondary) < 3:
            self.secondary.append(value)


def code_for(error):
    if isinstance(error, asyncio.CancelledError):
        return "cancelled"
    if isinstance(error, TimeoutError):
        return "timeout"
    return "unknown_failure"


def details(last, failure=None):
    return {
        "version": VERSION,
        "last": validate(failure.observed if failure is not None else last),
        "failure": validate(failure.diagnostic) if failure is not None else None,
        "secondary": (
            [validate(row) for row in failure.secondary] if failure is not None else []
        ),
    }
