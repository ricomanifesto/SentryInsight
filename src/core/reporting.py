"""Input-owned reporting identities and model-output grounding."""

from __future__ import annotations

import hashlib
import json
from html import escape
import ipaddress
import re
from dataclasses import asdict, dataclass
from typing import Any, Iterable, Mapping
from urllib.parse import quote, urlsplit

from ..services.article_content import (
    ArticleBlock,
    ArticleContentError,
    ArticleLink,
    article_content,
    retained_content,
)
from .cve import extract_cve_ids
from .source_markup import source_literal

import idna

REPORTING_KEY_PATTERN = re.compile(r"^source-[0-9a-f]{12}$")
REPORTING_FIELD_PATTERN = re.compile(
    r"^(?P<prefix>-[ \t]+\*\*Reporting\*\*:[ \t]*)(?P<value>.*?)[ \t]*$",
    re.MULTILINE,
)
ACTIVE_SECTION_PATTERN = re.compile(
    r"(?P<prefix>^##\s+Active Exploitation Details\s*$\n)"
    r"(?P<section>.*?)(?=^##\s+|\Z)",
    re.MULTILINE | re.DOTALL,
)
FINDING_PATTERN = re.compile(
    r"(?P<heading>^###\s+.+?\s*$\n)(?P<body>.*?)(?=^###\s+|\Z)",
    re.MULTILINE | re.DOTALL,
)


class ReportingGroundingError(ValueError):
    """Raised when reporting evidence cannot be grounded in supplied inputs."""


class ReportingContentError(ReportingGroundingError):
    """Malformed retained evidence requires terminal rejection, never omission."""


def reporting_content(article):
    try:
        return article_content(article)
    except ArticleContentError as exc:
        raise ReportingContentError("Invalid retained source content") from exc


def validate_retained_content(text, blocks=()):
    try:
        return retained_content(text, blocks)
    except ArticleContentError as exc:
        raise ReportingContentError("Invalid retained source structure") from exc


def _source_records(records):
    if not isinstance(records, Iterable) or isinstance(records, (str, bytes, Mapping)):
        raise ReportingContentError("Invalid retained source collection")
    return records


def _content_kind(value):
    # Provenance is open text, not an encoding declaration. Do not coerce a
    # malformed value or make unknown publisher/provider names a new enum.
    if not isinstance(value, str):
        raise ReportingContentError("Invalid retained source provenance type")
    return value


@dataclass(frozen=True)
class ReportingSource:
    key: str
    publisher: str
    title: str
    url: str
    content: str = ""
    content_kind: str = "feed"
    links: tuple[str, ...] = ()
    link_contexts: tuple[ArticleLink, ...] = ()
    metadata_cves: tuple[str, ...] = ()
    blocks: tuple[ArticleBlock, ...] = ()


@dataclass(frozen=True)
class PreparedReportingInput:
    """Canonical generation input, including valid but uncitable metadata.

    Catalog, prompt and cache consume this record. Encoding declarations and
    unused feed metadata are ingress concerns, not a second evidence identity.
    """

    title: str
    publisher: str
    url: str
    content: str
    content_kind: str
    blocks: tuple[ArticleBlock, ...]
    links: tuple[str, ...]
    link_contexts: tuple[ArticleLink, ...]
    cves: tuple[str, ...]
    affected_systems: tuple[str, ...]
    attack_vectors: tuple[str, ...]


def _input_text(value: Any) -> str:
    return "" if value is None else str(value).strip()


def prepare_reporting_input(
    article: Mapping[str, Any] | PreparedReportingInput,
) -> PreparedReportingInput:
    """Normalize evidence once, without inventing missing citation identity."""
    if isinstance(article, PreparedReportingInput):
        validate_retained_content(article.content, article.blocks)
        _content_kind(article.content_kind)
        _source_links(article.links)
        _link_contexts(article.link_contexts)
        return article
    content = reporting_content(article)
    try:
        links = _source_links(article.get("source_links", []))
        contexts = _link_contexts(article.get("source_link_contexts", []))
    except ReportingGroundingError as exc:
        # Malformed evidence is distinct from an absent/uncitable story URL.
        raise ReportingContentError("Invalid retained source links") from exc
    return PreparedReportingInput(
        title=_input_text(article.get("title")),
        publisher=_input_text(article.get("source")),
        url=_input_text(article.get("link")),
        content=content.text,
        content_kind=_content_kind(article.get("content_kind", "feed")),
        blocks=content.blocks,
        links=links,
        link_contexts=contexts,
        cves=tuple(str(value).strip() for value in article.get("cves", [])),
        affected_systems=tuple(article.get("affected_systems", [])),
        attack_vectors=tuple(article.get("attack_vectors", [])),
    )


def clean_article_source(value: Any) -> str:
    source = " ".join(_input_text(value).split())
    return "" if source.casefold() == "unknown source" else source


def collect_structured_cves(
    article: Mapping[str, Any] | PreparedReportingInput,
) -> list[str]:
    cves = [value for value in prepare_reporting_input(article).cves if value]
    cves.extend(extract_cve_ids("\n".join(cves)))
    return list(dict.fromkeys(value.upper() for value in cves))


def format_article_summary(
    article: Mapping[str, Any] | PreparedReportingInput,
) -> str:
    source = prepare_reporting_input(article)
    title = source.title or "Untitled article"
    publisher = clean_article_source(source.publisher)
    content = source.content or "No content available"
    metadata = []
    if publisher:
        metadata.append(f"Source: {publisher}")
    if source.url:
        metadata.append(f"URL: {source.url}")
        try:
            metadata.append(f"Reporting key: {reporting_key(source.url)}")
        except ReportingGroundingError:
            pass
    if cves := collect_structured_cves(source):
        metadata.append(f"CVEs: {', '.join(cves)}")
    heading = f"**{title}**"
    if metadata:
        heading += f" ({'; '.join(metadata)})"
    links = "\n".join(source.links)
    return f"{heading}\nContent coverage: {source.content_kind}\n\n{content}\nSource links: {links or 'Not stated in supplied sources.'}\n\n"


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


URL_COLLECTION_PREFIX = "urls-v1:"


def serialize_url_collection(urls: Iterable[str]) -> str:
    """Frame whole URL identities without changing semicolon/query semantics."""
    if not isinstance(urls, Iterable) or isinstance(urls, (str, bytes, Mapping)):
        raise ReportingGroundingError("Invalid URL collection")
    values = list(urls)
    if any(not isinstance(value, str) or not value for value in values):
        raise ReportingGroundingError("Invalid URL collection member")
    normalized = [normalize_reporting_url(value) for value in values]
    return URL_COLLECTION_PREFIX + json.dumps(normalized, separators=(",", ":"))


def parse_url_collection(value: str) -> tuple[str, ...]:
    """Read one complete versioned field or the unchanged legacy format.

    Legacy semicolon fields retain their old identity/error behavior. Only new
    versioned fields can represent a semicolon inside a URL; no stored artifact
    is migrated or reinterpreted. Order and duplicates are preserved.
    """
    if not isinstance(value, str):
        raise ReportingGroundingError("Invalid URL collection field")
    if value.startswith(URL_COLLECTION_PREFIX):
        try:
            values = json.loads(value[len(URL_COLLECTION_PREFIX) :])
            if not isinstance(values, list):
                raise ReportingGroundingError("Invalid URL collection")
            if serialize_url_collection(values) != value:
                raise ReportingGroundingError("Noncanonical URL collection")
        except (ValueError, TypeError) as exc:
            raise ReportingGroundingError("Invalid canonical URL collection") from exc
        return tuple(values)
    return tuple(normalize_reporting_url(entry.strip()) for entry in value.split(";"))


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
    articles: Iterable[Mapping[str, Any] | PreparedReportingInput],
) -> dict[str, ReportingSource]:
    """Build a deterministic allowlist from the exact model input articles."""
    catalog: dict[str, ReportingSource] = {}
    for article in _source_records(articles):
        prepared = prepare_reporting_input(article)
        url = normalize_reporting_url(prepared.url)
        source = ReportingSource(
            key=reporting_key(url),
            publisher=_clean_text(prepared.publisher, "publisher"),
            title=_clean_text(prepared.title, "title"),
            url=url,
            content=prepared.content,
            blocks=prepared.blocks,
            content_kind=prepared.content_kind,
            links=prepared.links,
            link_contexts=prepared.link_contexts,
            metadata_cves=tuple(
                extract_cve_ids(
                    " ".join(
                        [
                            prepared.title,
                            url,
                            *prepared.cves,
                        ]
                    )
                )
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
    records = []
    for source in catalog.values():
        validate_retained_content(source.content, source.blocks)
        _content_kind(source.content_kind)
        _source_links(source.links)
        _link_contexts(source.link_contexts)
        record = asdict(source)
        if not source.blocks:
            record.pop("blocks")
        records.append(record)
    return records


def _source_links(records) -> tuple[str, ...]:
    if not isinstance(records, (list, tuple)) or any(
        not isinstance(link, str) for link in records
    ):
        raise ReportingContentError("Invalid retained source links")
    return tuple(normalize_reporting_url(link) for link in records)


def _link_contexts(records) -> tuple[ArticleLink, ...]:
    if not isinstance(records, (list, tuple)):
        raise ReportingContentError("Invalid retained link context")
    values = [
        asdict(record) if isinstance(record, ArticleLink) else record
        for record in records
    ]
    if any(
        not isinstance(record, dict)
        or "url" not in record
        or any(
            not isinstance(record.get(field, ""), str)
            for field in ("url", "label", "context")
        )
        for record in values
    ):
        raise ReportingContentError("Invalid retained link context")
    return tuple(
        ArticleLink(
            normalize_reporting_url(record["url"]),
            record.get("label", ""),
            record.get("context", ""),
        )
        for record in values
    )


def deserialize_reporting_catalog(
    records: Iterable[Mapping[str, Any]],
) -> dict[str, ReportingSource]:
    catalog: dict[str, ReportingSource] = {}
    for record in _source_records(records):
        if not isinstance(record, Mapping):
            raise ReportingContentError("Invalid retained source record")
        url = normalize_reporting_url(record.get("url"))
        content = validate_retained_content(
            record.get("content", ""), record.get("blocks", ())
        )
        source = ReportingSource(
            key=_clean_text(record.get("key"), "key"),
            publisher=_clean_text(record.get("publisher"), "publisher"),
            title=_clean_text(record.get("title"), "title"),
            url=url,
            content=content.text,
            blocks=content.blocks,
            content_kind=_content_kind(record.get("content_kind", "feed")),
            links=_source_links(record.get("links", [])),
            link_contexts=_link_contexts(record.get("link_contexts", [])),
            metadata_cves=tuple(
                extract_cve_ids(
                    " ".join(str(value) for value in record.get("metadata_cves", []))
                )
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


def reporting_markdown_link(label: str, url: str) -> str:
    """Serialize intended evidence links without reinterpreting owned data.

    Angle destinations contain parentheses; entity escaping survives the
    parser's one destination decode without changing URL identity.
    """
    destination = escape(normalize_reporting_url(url), quote=False)
    return f"[{source_literal(label)}](<{destination}>)"


def _resolve_finding(
    block: re.Match[str], catalog: Mapping[str, ReportingSource]
) -> str:
    body = block.group("body")
    fields = list(REPORTING_FIELD_PATTERN.finditer(body))
    title = block.group("heading").removeprefix("###").strip()
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
        reporting_markdown_link(
            f"{catalog[key].publisher} — {catalog[key].title}", catalog[key].url
        )
        for key in keys
    )
    field = fields[0]
    resolved_body = (
        body[: field.start()] + field.group("prefix") + links + body[field.end() :]
    )
    return block.group("heading") + resolved_body


def resolve_reporting_keys(report: str, catalog: Mapping[str, ReportingSource]) -> str:
    """Resolve model-selected keys; URLs and labels always come from inputs."""
    section_match = ACTIVE_SECTION_PATTERN.search(report)
    if not section_match:
        raise ReportingGroundingError("Missing Active Exploitation Details section")
    section = section_match.group("section")
    findings = list(FINDING_PATTERN.finditer(section))
    if not findings:
        raise ReportingGroundingError(
            "No findings are available for reporting evidence"
        )
    resolved_section = FINDING_PATTERN.sub(
        lambda match: _resolve_finding(match, catalog), section
    )
    return (
        report[: section_match.start("section")]
        + resolved_section
        + report[section_match.end("section") :]
    )
