"""Input-owned reporting identities and model-output grounding."""

from __future__ import annotations

import hashlib
import ipaddress
import re
from dataclasses import asdict, dataclass
from typing import Any, Iterable, Mapping
from urllib.parse import quote, urlsplit

from ..services.article_content import normalize_feed_content
from .report_findings import (  # noqa: F401 - the finding grammar's public names
    ACTIVE_SECTION_PATTERN,
    FINDING_PATTERN,
    REPORTING_FIELD_PATTERN,
    FindingRow,
    report_findings,
)

import idna

REPORTING_KEY_PATTERN = re.compile(r"^source-[0-9a-f]{12}$")


class ReportingGroundingError(ValueError):
    """Raised when reporting evidence cannot be grounded in supplied inputs."""


@dataclass(frozen=True)
class ReportingSource:
    key: str
    publisher: str
    title: str
    url: str
    content: str = ""
    content_kind: str = "feed"
    links: tuple[str, ...] = ()


def normalize_reporting_url(value: Any) -> str:
    """Return the stable safe URL identity used across both public products."""
    raw = str(value or "").strip()
    try:
        parsed = urlsplit(raw)
    except ValueError as exc:
        raise ReportingGroundingError(
            "Reporting links must use an absolute http or https URL"
        ) from exc
    if (
        parsed.scheme.casefold() not in {"http", "https"}
        or not parsed.hostname
        or parsed.username
        or parsed.password
    ):
        raise ReportingGroundingError(
            "Reporting links must use an absolute http or https URL without credentials"
        )
    scheme = parsed.scheme.casefold()
    host = parsed.hostname.lower()
    try:
        port = parsed.port
    except ValueError as exc:
        raise ReportingGroundingError("Reporting URL contains an invalid port") from exc
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        try:
            host = idna.encode(host, uts46=True, transitional=False).decode("ascii")
        except idna.IDNAError as exc:
            raise ReportingGroundingError(
                "Reporting URL contains an invalid host"
            ) from exc
    else:
        if isinstance(address, ipaddress.IPv6Address):
            host = f"[{address.compressed}]"

    if port and not (
        (scheme == "http" and port == 80) or (scheme == "https" and port == 443)
    ):
        host = f"{host}:{port}"

    path = _remove_dot_segments((parsed.path or "/").replace("\\", "/"))
    encoded_path = quote(path, safe="/%:@-._~!$&'()*+,;=")
    encoded_query = quote(parsed.query, safe="!$&'()*+,-./:;=?@_%~")
    raw_without_fragment = raw.split("#", maxsplit=1)[0]
    query = f"?{encoded_query}" if "?" in raw_without_fragment else ""
    return f"{scheme}://{host}{encoded_path}{query}"


def _remove_dot_segments(path: str) -> str:
    """Apply the URL path dot-segment behavior used by WHATWG URL parsers."""
    segments = path.split("/")
    output: list[str] = []
    trailing_directory = path.endswith(("/.", "/.."))
    for segment in segments:
        normalized_segment = segment.casefold()
        if normalized_segment in {".", "%2e"}:
            continue
        if normalized_segment in {"..", ".%2e", "%2e.", "%2e%2e"}:
            if output and output[-1]:
                output.pop()
            continue
        output.append(segment)
    normalized = "/".join(output)
    if trailing_directory and not normalized.endswith("/"):
        normalized += "/"
    return normalized or "/"


def _identity(value: Any) -> str:
    return hashlib.sha256(normalize_reporting_url(value).encode()).hexdigest()[:12]


def reporting_key(value: Any) -> str:
    return f"source-{_identity(value)}"


def reporting_fragment(value: Any) -> str:
    return f"reporting-{_identity(value)}"


def _clean_text(value: Any, field: str) -> str:
    cleaned = " ".join(str(value or "").split())
    if not cleaned:
        raise ReportingGroundingError(f"Reporting source is missing {field}")
    return cleaned


def build_reporting_catalog(
    articles: Iterable[Mapping[str, Any]],
) -> dict[str, ReportingSource]:
    """Build a deterministic allowlist from the exact model input articles."""
    catalog: dict[str, ReportingSource] = {}
    for article in articles:
        url = normalize_reporting_url(article.get("link"))
        source = ReportingSource(
            key=reporting_key(url),
            publisher=_clean_text(article.get("source"), "publisher"),
            title=_clean_text(article.get("title"), "title"),
            url=url,
            content=normalize_feed_content(
                article.get("content") or article.get("summary")
            ),
            content_kind=str(article.get("content_kind", "feed")),
            links=tuple(
                normalize_reporting_url(link)
                for link in article.get("source_links", [])
            ),
        )
        existing = catalog.get(source.key)
        if existing and existing != source:
            raise ReportingGroundingError(f"Reporting key collision for {source.key}")
        catalog[source.key] = source
    return catalog


def serialize_reporting_catalog(
    catalog: Mapping[str, ReportingSource],
) -> list[dict[str, Any]]:
    return [asdict(source) for source in catalog.values()]


def deserialize_reporting_catalog(
    records: Iterable[Mapping[str, Any]],
) -> dict[str, ReportingSource]:
    catalog: dict[str, ReportingSource] = {}
    for record in records:
        url = normalize_reporting_url(record.get("url"))
        source = ReportingSource(
            key=_clean_text(record.get("key"), "key"),
            publisher=_clean_text(record.get("publisher"), "publisher"),
            title=_clean_text(record.get("title"), "title"),
            url=url,
            content=str(record.get("content", "")),
            content_kind=str(record.get("content_kind", "feed")),
            links=tuple(
                normalize_reporting_url(link) for link in record.get("links", [])
            ),
        )
        if source.key != reporting_key(url):
            raise ReportingGroundingError(
                f"Reporting source key does not match its URL: {source.key}"
            )
        if source.key in catalog:
            raise ReportingGroundingError(
                f"Duplicate reporting source key: {source.key}"
            )
        catalog[source.key] = source
    if not catalog:
        raise ReportingGroundingError("No reporting sources were supplied")
    return catalog


def _markdown_label(source: ReportingSource) -> str:
    label = f"{source.publisher} — {source.title}"
    return label.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def _resolve_finding(row: FindingRow, catalog: Mapping[str, ReportingSource]) -> str:
    body = row.body
    fields = row.reporting_fields
    title = row.title
    if len(fields) != 1:
        raise ReportingGroundingError(f"{title}: expected exactly one Reporting field")
    value = fields[0].group("value").strip()
    keys = [candidate.strip() for candidate in value.split(",")]
    if not keys or any(not REPORTING_KEY_PATTERN.fullmatch(key) for key in keys):
        raise ReportingGroundingError(
            f"{title}: Reporting must contain only supplied source keys"
        )
    if len(keys) != len(set(keys)):
        raise ReportingGroundingError(f"{title}: Reporting contains duplicate keys")
    unknown = [key for key in keys if key not in catalog]
    if unknown:
        raise ReportingGroundingError(
            f"{title}: Reporting contains unknown source keys: {', '.join(unknown)}"
        )
    links = ", ".join(
        f"[{_markdown_label(catalog[key])}]({catalog[key].url})" for key in keys
    )
    field = fields[0]
    resolved_body = (
        body[: field.start()] + field.group("prefix") + links + body[field.end() :]
    )
    return row.heading + resolved_body


def resolve_reporting_keys(report: str, catalog: Mapping[str, ReportingSource]) -> str:
    """Resolve model-selected keys; URLs and labels always come from inputs."""
    table = report_findings(report)
    if not table.has_section:
        raise ReportingGroundingError("Missing Active Exploitation Details section")
    if not table.rows:
        raise ReportingGroundingError(
            "No findings are available for reporting evidence"
        )
    # A list, not a generator: a callback's exception propagates unchanged.
    return table.render(
        [(row.start, row.end, _resolve_finding(row, catalog)) for row in table.rows]
    )
