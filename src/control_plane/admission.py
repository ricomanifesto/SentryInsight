"""Admission requests for the report control plane.

The control plane admits a strict JSON body whose article records carry a
closed set of fields. This module builds that body from the product's
enriched article dicts without changing their text, refuses locally what the
control plane would refuse, and submits it. Identical bytes are one operation,
so a retry after a transient failure is safe.
"""

from __future__ import annotations

import dataclasses
import hashlib
import json
import re
from datetime import datetime
from typing import Any, Iterable, Mapping

import httpx

SCHEMA = "report-control-plane/admission/1"
STRING_FIELDS = (
    "title",
    "link",
    "source",
    "content",
    "summary",
    "content_kind",
    "published_at",
)
LIST_FIELDS = ("source_links", "cves")

MAX_LINK_CHARS = 2048
MAX_TITLE_CHARS = 512
MAX_SOURCE_CHARS = 256
MAX_LIST_ITEMS = 64
MAX_LIST_ITEM_CHARS = 2048


@dataclasses.dataclass(frozen=True)
class Limits:
    articles: int
    content_bytes: int
    record_bytes: int
    body_bytes: int


# An admission's bounds, and a projection's larger ones for the producer's full
# article text (the Worker's LIMITS and PROJECTION_LIMITS).
ADMISSION_LIMITS = Limits(100, 64 * 1024, 64 * 1024, 1024 * 1024)
PROJECTION_LIMITS = Limits(100, 256 * 1024, 320 * 1024, 8 * 1024 * 1024)

TOKEN = re.compile(r"[a-z0-9][a-z0-9._-]{0,63}")
SOURCE_REVISION = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:@+/-]{0,199}")
LINK = re.compile(r"https?://[\x21-\x7e]+")
PUBLISHED_AT = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?Z")


class AdmissionError(Exception):
    """The admission did not produce a verified operation."""


class AdmissionRefused(AdmissionError):
    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason


class AdmissionConflict(AdmissionError):
    """The source revision label already names different bytes."""

    def __init__(self, operation_id: str):
        super().__init__("source_revision_conflict")
        self.operation_id = operation_id


class AdmissionTransient(AdmissionError):
    """Retry later with the same bytes."""


@dataclasses.dataclass(frozen=True)
class Admitted:
    operation_id: str
    fingerprint: str
    created: bool
    status: Mapping[str, Any]


def _units(text: str) -> int:
    """Length in UTF-16 code units, as the control plane measures strings."""
    return len(text.encode("utf-16-le")) // 2


def _encodable(text: str) -> bool:
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def valid_published_at(value: str) -> bool:
    """An RFC 3339 UTC timestamp that names a real instant."""
    if not PUBLISHED_AT.fullmatch(value):
        return False
    try:
        datetime.strptime(value[:19], "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        return False
    return int(value[17:19]) < 60


def checked_record(article: Mapping[str, Any], limits: Limits) -> dict[str, Any]:
    record: dict[str, Any] = {}
    for key in STRING_FIELDS:
        value = article.get(key)
        if value is None and key != "content":
            continue
        if not isinstance(value, str) or not _encodable(value):
            raise AdmissionRefused("article_invalid")
        record[key] = value
    for key in LIST_FIELDS:
        value = article.get(key)
        if value is None:
            continue
        if (
            not isinstance(value, list)
            or len(value) > MAX_LIST_ITEMS
            or not all(
                isinstance(item, str)
                and _encodable(item)
                and _units(item) <= MAX_LIST_ITEM_CHARS
                for item in value
            )
        ):
            raise AdmissionRefused("article_invalid")
        record[key] = value
    if "published_at" in record and not valid_published_at(record["published_at"]):
        raise AdmissionRefused("article_invalid")
    title, link = record.get("title"), record.get("link")
    if title is None or not title.strip() or _units(title) > MAX_TITLE_CHARS:
        raise AdmissionRefused("article_invalid")
    if link is None or len(link) > MAX_LINK_CHARS or not LINK.fullmatch(link):
        raise AdmissionRefused("article_invalid")
    if len(record["content"].encode("utf-8")) > limits.content_bytes:
        raise AdmissionRefused("article_invalid")
    if _units(record.get("source", "")) > MAX_SOURCE_CHARS:
        raise AdmissionRefused("article_invalid")
    # The control plane bounds each record by its ASCII-escaped encoding.
    escaped = json.dumps(
        record, sort_keys=True, ensure_ascii=True, separators=(",", ":")
    )
    if len(escaped) > limits.record_bytes:
        raise AdmissionRefused("article_too_large")
    return record


def admission_body(
    articles: Iterable[Mapping[str, Any]],
    *,
    pipeline: str,
    policy_id: str,
    source_revision: str,
    limits: Limits = ADMISSION_LIMITS,
) -> bytes:
    """The exact request bytes; the same articles always give the same bytes."""
    if not TOKEN.fullmatch(pipeline):
        raise AdmissionRefused("pipeline_invalid")
    if not TOKEN.fullmatch(policy_id):
        raise AdmissionRefused("policy_invalid")
    if not SOURCE_REVISION.fullmatch(source_revision):
        raise AdmissionRefused("source_revision_invalid")
    if source_revision.startswith("schedule:"):
        raise AdmissionRefused("source_revision_reserved")
    records = []
    links = set()
    for article in articles:
        record = checked_record(article, limits)
        if record["link"] in links:
            raise AdmissionRefused("article_duplicate_key")
        links.add(record["link"])
        records.append(record)
    if not records or len(records) > limits.articles:
        raise AdmissionRefused("articles_invalid")
    body = json.dumps(
        {
            "schema": SCHEMA,
            "pipeline": pipeline,
            "policy_id": policy_id,
            "source_revision": source_revision,
            "articles": records,
        },
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    if len(body) > limits.body_bytes:
        raise AdmissionRefused("request_too_large")
    return body


def expected_identity(body: bytes, pipeline: str, policy_id: str) -> tuple[str, str]:
    """The snapshot fingerprint and operation id the control plane derives."""
    fingerprint = hashlib.sha256(body).hexdigest()
    operation_id = hashlib.sha256(
        f"report-control-plane/1\n{pipeline}\n{policy_id}\n{fingerprint}".encode()
    ).hexdigest()
    return fingerprint, operation_id


def _error(response: httpx.Response) -> dict[str, Any]:
    try:
        value = response.json()
    except ValueError:
        return {}
    return value if isinstance(value, dict) else {}


def submit(
    client: httpx.Client,
    base_url: str,
    token: str,
    body: bytes,
    *,
    pipeline: str,
    policy_id: str,
) -> Admitted:
    """Admit ``body`` and verify the control plane named the expected operation."""
    fingerprint, operation_id = expected_identity(body, pipeline, policy_id)
    try:
        response = client.post(
            f"{base_url.rstrip('/')}/v1/operations",
            content=body,
            headers={
                "authorization": f"Bearer {token}",
                "content-type": "application/json",
            },
        )
    except httpx.HTTPError as error:
        raise AdmissionTransient("transport") from error
    if response.status_code in (200, 201):
        status = _error(response)
        operation = status.get("operation")
        if (
            not isinstance(operation, dict)
            or operation.get("operation_id") != operation_id
        ):
            raise AdmissionError("operation_identity_mismatch")
        return Admitted(operation_id, fingerprint, response.status_code == 201, status)
    detail = _error(response)
    if (
        response.status_code == 409
        and detail.get("error") == "source_revision_conflict"
    ):
        raise AdmissionConflict(str(detail.get("operation_id", "")))
    if 400 <= response.status_code < 500 and response.status_code not in (408, 429):
        raise AdmissionRefused(str(detail.get("error", f"http_{response.status_code}")))
    raise AdmissionTransient(f"http_{response.status_code}")
