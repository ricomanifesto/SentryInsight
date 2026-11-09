"""A run-local snapshot of the sources a report run read, and what it did with each.

The report workflow writes it after a run when ``SENTRYINSIGHT_PROJECTION_SNAPSHOT``
names a path, so a later step can project the run into the report history.
The file holds article text and stays in the runner's temporary directory; it
is never committed or uploaded as a workflow artifact. Writing it never
changes the run: any failure is logged and ignored.
"""

from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, Mapping

from src.core.reporting import ReportingGroundingError, reporting_key
from src.core.source_review import PLAN_KEY

from .admission import PROJECTION_LIMITS, AdmissionRefused, checked_record

ENV_PATH = "SENTRYINSIGHT_PROJECTION_SNAPSHOT"
SCHEMA = "sentryinsight-run-snapshot/1"
KEPT = (
    "title",
    "link",
    "source",
    "content",
    "summary",
    "content_kind",
    "source_links",
    "cves",
)

# A source-review plan row's state, as the source's outcome in this run.
ROW_OUTCOMES = {
    "eligible": "executed",
    "review_required": "review_required",
    "source_rejected": "source_rejected",
}

logger = logging.getLogger(__name__)


def published_at(value: Any) -> str | None:
    """The feed's publication time in UTC RFC 3339, or None when unknown.

    A time without a zone is not a known instant, so it stays unknown.
    """
    if not isinstance(value, str) or not value.strip():
        return None
    parsed: datetime | None
    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError, IndexError):
        try:
            parsed = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
        except ValueError:
            return None
    if parsed is None or parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def source_record(article: Mapping[str, Any]) -> dict[str, Any]:
    record = {key: article[key] for key in KEPT if article.get(key) is not None}
    if not isinstance(record.get("content"), str):
        record["content"] = ""
    when = published_at(article.get("published"))
    if when is not None:
        record["published_at"] = when
    return record


def _key(link: Any) -> str | None:
    try:
        return reporting_key(link)
    except ReportingGroundingError:
        return None


def source_outcomes(
    state: Mapping[str, Any], articles: list[dict[str, Any]]
) -> dict[str, str] | None:
    """What the run did with each source, or None when that is not established.

    The model receives exactly the source-review plan's eligible rows, and
    report generation refuses to proceed unless the stored plan, the plan the
    analysis used and a plan rebuilt from the filtered articles are equal. So
    a generated report is the evidence: only then is an eligible row
    ``executed`` and every other source excluded with its reason. A plan
    alone is not evidence, because analysis can stop after building it and
    before any model call; every other ending reports None.
    """
    if state.get("report_generated") is not True:
        return None
    plan = state.get(PLAN_KEY)
    results = state.get("analysis_results")
    if not isinstance(plan, Mapping) or not isinstance(results, Mapping):
        return None
    if results.get("skipped") or results.get("error") or results.get(PLAN_KEY) != plan:
        return None
    rows = plan.get("sources")
    if not isinstance(rows, list):
        return None
    by_key: dict[str, str] = {}
    for row in rows:
        outcome = (
            ROW_OUTCOMES.get(row.get("state")) if isinstance(row, Mapping) else None
        )
        if outcome is None or not isinstance(row.get("key"), str):
            return None
        by_key[row["key"]] = outcome
    filtered = {_key(a.get("link")) for a in state.get("filtered_articles") or []}
    if filtered != set(by_key):
        return None
    # Rows match sources by the product's own URL identity, never raw links.
    # A source the plan does not hold was removed by the filter or triage.
    return {a["link"]: by_key.get(_key(a["link"]), "filtered") for a in articles}


def build_run_snapshot(state: Mapping[str, Any] | None) -> dict[str, Any]:
    """Sources the run read, what it did with each, and how it ended."""
    state = state or {}
    articles: list[dict[str, Any]] = []
    seen: set[str] = set()
    dropped = 0
    for article in state.get("articles") or []:
        record = source_record(article)
        try:
            checked_record(record, PROJECTION_LIMITS)
        except AdmissionRefused:
            dropped += 1
            continue
        if record["link"] in seen:
            dropped += 1
            continue
        seen.add(record["link"])
        articles.append(record)
    if len(articles) > PROJECTION_LIMITS.articles:
        dropped += len(articles) - PROJECTION_LIMITS.articles
        articles = articles[: PROJECTION_LIMITS.articles]
    failure = state.get("failure") or {}
    return {
        "schema": SCHEMA,
        "status": state.get("status"),
        "failure_codes": list(failure.get("codes") or []),
        "articles": articles,
        "source_outcomes": source_outcomes(state, articles),
        "dropped_articles": dropped,
    }


def write_run_snapshot(
    state: Mapping[str, Any] | None, path: str | None = None
) -> bool:
    """Write the snapshot when configured; never raises."""
    target = path or os.environ.get(ENV_PATH)
    if not target:
        return False
    try:
        Path(target).write_text(json.dumps(build_run_snapshot(state)), encoding="utf-8")
    except Exception as error:  # noqa: BLE001 - must never affect the run
        logger.warning("Run snapshot not written: %s", type(error).__name__)
        return False
    return True
