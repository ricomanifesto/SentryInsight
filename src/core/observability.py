"""Optional Logfire tracing for report generation runs.

Span attributes carry identifiers, counts, outcomes and bounded failure codes.
Article text and titles, prompts, model output, validation messages and
credentials are never recorded. Recorded exceptions keep only their type, because
messages and tracebacks can carry header values or source content.
"""

from collections.abc import Awaitable, Callable, Mapping
import functools
from typing import Any, TypeVar

import logfire
from logfire.types import ExceptionCallbackHelper
from opentelemetry.trace import Status, StatusCode

from .model_config import resolve_model, validate_model

SERVICE_NAME = "sentryinsight"

StateT = TypeVar("StateT", bound=Mapping[str, Any])


def record_exception_type(helper: ExceptionCallbackHelper) -> None:
    """Replace a recorded exception with its type alone."""
    exception_type = type(helper.exception).__qualname__
    helper.no_record_exception()
    helper.span.set_attribute("error.type", exception_type)
    if helper.span.status.status_code is StatusCode.ERROR:
        helper.span.set_status(Status(StatusCode.ERROR, exception_type))


def logfire_options() -> dict[str, Any]:
    """Return the configuration shared by the entrypoint and its tests."""
    return {
        "service_name": SERVICE_NAME,
        "send_to_logfire": "if-token-present",
        "console": False,
        # Span messages use templates, never f-strings.
        "inspect_arguments": False,
        "advanced": logfire.AdvancedOptions(exception_callback=record_exception_type),
    }


def configure_observability() -> None:
    """Configure export from the executable entrypoint.

    Nothing leaves the process unless ``LOGFIRE_TOKEN`` is set. HTTP clients are
    not auto-instrumented: their spans record raw transport exception text in the
    span status, after any exception callback runs.
    """
    logfire.configure(**logfire_options())


def model_attributes(config: Mapping[str, Any]) -> dict[str, str]:
    """Return the configured model identifier when it is well formed."""
    model = resolve_model(dict(config))
    try:
        validate_model(model)
    except ValueError:
        return {"model.id_valid": "false"}
    return {"model.id": model}


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
