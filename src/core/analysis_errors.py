"""Bounded classification of analysis failures for telemetry.

Classes come from a fixed vocabulary and detail values are integers, so neither
can carry provider messages, prompts or model output.
"""

from .openrouter_client import OpenRouterError

ANALYSIS_ERROR_CLASSES = frozenset(
    {
        "model_provider_unavailable",
        "model_rate_limited",
        "model_auth_rejected",
        "model_request_failed",
        "input_budget_exceeded",
        "analysis_exception",
    }
)
PROVIDER_UNAVAILABLE_CODES = frozenset({502, 503, 504, 529})
RATE_LIMITED_CODES = frozenset({429})
AUTH_REJECTED_CODES = frozenset({401, 403})


def classify_analysis_error(error: BaseException) -> tuple[str, dict[str, int]]:
    """Return an error class and integer-only detail; never message text."""
    if not isinstance(error, OpenRouterError):
        return "analysis_exception", {}
    detail = {
        name: value
        for name, value in (
            ("http_status", error.http_status),
            ("provider_code", error.provider_code),
            ("attempts", error.attempts),
        )
        if type(value) is int
    }
    # HTTP 200 responses can still carry a provider error code.
    code = detail.get("provider_code", detail.get("http_status"))
    if code in PROVIDER_UNAVAILABLE_CODES:
        return "model_provider_unavailable", detail
    if code in RATE_LIMITED_CODES:
        return "model_rate_limited", detail
    if code in AUTH_REJECTED_CODES:
        return "model_auth_rejected", detail
    return "model_request_failed", detail
