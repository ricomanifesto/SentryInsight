"""A run-local snapshot of the sources a report run read and analyzed.

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


def build_run_snapshot(state: Mapping[str, Any] | None) -> dict[str, Any]:
    """Sources the run read, which of them it analyzed, and how it ended."""
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
    kept = {a["link"] for a in articles}
    filtered = state.get("filtered_articles")
    analyzed = (
        None
        if filtered is None
        else [a.get("link") for a in filtered if a.get("link") in kept]
    )
    failure = state.get("failure") or {}
    return {
        "schema": SCHEMA,
        "status": state.get("status"),
        "failure_codes": list(failure.get("codes") or []),
        "articles": articles,
        "analyzed_links": analyzed,
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
