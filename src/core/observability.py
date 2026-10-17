"""Optional Logfire tracing for report generation runs.

Span attributes carry identifiers, counts, outcomes and bounded failure codes.
Article text and titles, prompts, model output, validation messages and
credentials are never recorded. Recorded exceptions keep only their type, because
messages and tracebacks can carry header values or source content.
"""

from collections.abc import Awaitable, Callable, Mapping
import functools
import os
import re
from typing import Any, TypeVar

import logfire
from logfire.types import ExceptionCallbackHelper
from opentelemetry.trace import Status, StatusCode

from .analysis_errors import ANALYSIS_ERROR_CLASSES
from .model_config import resolve_model, validate_model

SERVICE_NAME = "sentryinsight"
MODEL_DETAIL_FIELDS = ("http_status", "provider_code", "attempts")
_DIGITS = re.compile(r"[0-9]{1,20}")
_EVENT_NAME = re.compile(r"[a-z_]{1,64}")

StateT = TypeVar("StateT", bound=Mapping[str, Any])


def record_exception_type(helper: ExceptionCallbackHelper) -> None:
    """Replace a recorded exception with its type alone."""
    exception_type = type(helper.exception).__qualname__
    helper.no_record_exception()
    helper.span.set_attribute("error.type", exception_type)
    if helper.span.status.status_code is StatusCode.ERROR:
        helper.span.set_status(Status(StatusCode.ERROR, exception_type))


def logfire_options() -> dict[str, Any]:
    """Return the configuration shared by the entrypoint and its tests.

    Export requires ``LOGFIRE_TOKEN``. ``send_to_logfire="if-token-present"``
    would also use a token saved under ``.logfire`` by the Logfire CLI.
    """
    token = os.environ.get("LOGFIRE_TOKEN", "").strip() or None
    return {
        "service_name": SERVICE_NAME,
        "send_to_logfire": token is not None,
        "token": token,
        "console": False,
        # Span messages use templates, never f-strings.
        "inspect_arguments": False,
        "advanced": logfire.AdvancedOptions(exception_callback=record_exception_type),
    }


def configure_observability() -> None:
    """Configure export from the executable entrypoint.

    Nothing leaves the process unless ``LOGFIRE_TOKEN`` is set. Without it,
    Logfire stays unconfigured and spans are no-ops: configuring would still add
    an exporter for any ``OTEL_EXPORTER_OTLP_*ENDPOINT`` set by the host. HTTP
    clients are not auto-instrumented: their spans record raw transport exception
    text in the span status, after any exception callback runs.
    """
    options = logfire_options()
    if not options["send_to_logfire"]:
        return
    logfire.configure(**options)


def model_attributes(config: Mapping[str, Any]) -> dict[str, str]:
    """Return the configured model identifier when it is well formed."""
    model = resolve_model(dict(config))
    try:
        validate_model(model)
    except ValueError:
        return {"model.id_valid": "false"}
    return {"model.id": model}


def ci_attributes(environ: Mapping[str, str] = os.environ) -> dict[str, Any]:
    """Return the GitHub Actions run identity when the values are well formed."""
    attributes: dict[str, Any] = {}
    for name, variable in (
        ("ci.run_id", "GITHUB_RUN_ID"),
        ("ci.run_attempt", "GITHUB_RUN_ATTEMPT"),
    ):
        value = environ.get(variable, "")
        if _DIGITS.fullmatch(value):
            attributes[name] = int(value)
    event = environ.get("GITHUB_EVENT_NAME", "")
    if _EVENT_NAME.fullmatch(event):
        attributes["ci.event"] = event
    return attributes


def state_attributes(state: Mapping[str, Any]) -> dict[str, Any]:
    """Summarize workflow state as bounded span attributes."""
    attributes: dict[str, Any] = {
        "workflow.status": str(state.get("status", "")),
        "articles.count": len(state.get("articles") or []),
        "filtered_articles.count": len(state.get("filtered_articles") or []),
    }
    analysis = state.get("analysis_results") or {}
    if analysis:
        if analysis.get("error"):
            attributes["analysis.outcome"] = "error"
        elif analysis.get("skipped"):
            attributes["analysis.outcome"] = "skipped"
        else:
            attributes["analysis.outcome"] = "analyzed"
        if "analyzed_article_count" in analysis:
            attributes["analysis.article_count"] = int(
                analysis["analyzed_article_count"]
            )
        if "cves_identified" in analysis:
            attributes["analysis.cve_count"] = len(analysis["cves_identified"] or [])
        error_class = analysis.get("error_class")
        if isinstance(error_class, str) and error_class in ANALYSIS_ERROR_CLASSES:
            attributes["analysis.error_class"] = error_class
        detail = analysis.get("error_detail")
        if not isinstance(detail, Mapping):
            detail = {}
        for field in MODEL_DETAIL_FIELDS:
            # Integers only: booleans and strings are never recorded.
            if type(detail.get(field)) is int:
                attributes[f"model.{field}"] = detail[field]
    failure = state.get("failure")
    if failure:
        attributes["failure.stage"] = failure["stage"]
        attributes["failure.codes"] = list(failure["codes"])
        if failure.get("field"):
            attributes["failure.field"] = failure["field"]
    return attributes


def traced_stage(
    name: str, stage: Callable[[StateT], Awaitable[StateT]]
) -> Callable[[StateT], Awaitable[StateT]]:
    """Wrap one graph stage in a span that records the resulting state."""

    @functools.wraps(stage)
    async def run(state: StateT) -> StateT:
        with logfire.span(
            "sentryinsight {stage}", stage=name, _span_name=f"sentryinsight.{name}"
        ) as span:
            result = await stage(state)
            span.set_attributes(state_attributes(result))
            return result

    return run
