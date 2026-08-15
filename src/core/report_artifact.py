"""Versioned, source-owned report artifact contract."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import TypeVar

from markdown_it import MarkdownIt

from .heading_identity import normalize_heading_identity
from .reporting import (
    ReportingGroundingError,
    normalize_reporting_url,
    reporting_fragment,
)

CVE_ID_PATTERN = re.compile(r"^CVE-\d{4}-\d{4,}$", re.IGNORECASE)
PARTIAL_CVE_PATTERN = re.compile(r"\bCVE-\d{4}-\d{0,3}(?!\d)", re.IGNORECASE)
HEADING_PATTERN = re.compile(r"^###\s+(.+?)\s*$", re.MULTILINE)
FIELD_PATTERN = re.compile(
    r"^-[ \t]+\*\*(Severity|Exploitation Status|Action|CVE IDs?|Reporting)\*\*:[ \t]*(.*?)[ \t]*$",
    re.MULTILINE,
)
DIGEST_ARCHIVE_ROOT = "https://ricomanifesto.github.io/SentryDigest/archive/"


class ReportArtifactError(ValueError):
    """Raised when a report does not satisfy the published artifact contract."""


class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    UNKNOWN = "unknown"


class ExploitationStatus(str, Enum):
    ACTIVE = "active"
    OBSERVED = "observed"
    POTENTIAL = "potential"
    NOT_OBSERVED = "not_observed"
    UNKNOWN = "unknown"


class Action(str, Enum):
    PATCH = "patch"
    MITIGATE = "mitigate"
    INVESTIGATE = "investigate"
    MONITOR = "monitor"
    NONE = "none"


EnumType = TypeVar("EnumType", bound=Enum)


@dataclass(frozen=True)
class ReportingReference:
    publisher: str
    title: str
    url: str
    digest_fragment: str


@dataclass(frozen=True)
class Finding:
    title: str
    slug: str
    severity: Severity
    exploitation_status: ExploitationStatus
    action: Action
    cve_ids: tuple[str, ...]
    reporting: tuple[ReportingReference, ...] = ()


@dataclass(frozen=True)
class ReportArtifact:
    schema_version: int
    report_date: date
    generated_at: datetime
    body: str
    source: str
    findings: tuple[Finding, ...]
    digest_issue_url: str | None = None


def slugify(value: str) -> str:
    """Return a stable, human-readable HTML fragment identifier."""
    slug = normalize_heading_identity(value)
    if not slug:
        raise ReportArtifactError("Heading cannot produce an empty slug")
    return slug


def _parse_front_matter(source: str) -> tuple[dict[str, str], str]:
    lines = source.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ReportArtifactError("Report must start with metadata front matter")

    try:
        closing_index = next(
            index
            for index, line in enumerate(lines[1:], start=1)
            if line.strip() == "---"
        )
    except StopIteration as exc:
        raise ReportArtifactError("Report metadata front matter is not closed") from exc

    metadata: dict[str, str] = {}
    for line in lines[1:closing_index]:
        if not line.strip():
            continue
        if ":" not in line:
            raise ReportArtifactError(f"Invalid report metadata line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key or not value:
            raise ReportArtifactError(f"Invalid report metadata line: {line}")
        if key in metadata:
            raise ReportArtifactError(f"Duplicate report metadata field: {key}")
        metadata[key] = value

    body = "\n".join(lines[closing_index + 1 :]).lstrip()
    return metadata, body


def _required_metadata(metadata: dict[str, str], key: str) -> str:
    value = metadata.get(key, "").strip()
    if not value:
        raise ReportArtifactError(f"Missing required report metadata: {key}")
    return value


def _parse_timestamp(value: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ReportArtifactError("generated_at must be an ISO 8601 timestamp") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ReportArtifactError("generated_at must include a timezone")
    return parsed


def _parse_enum(enum_type: type[EnumType], field: str, value: str) -> EnumType:
    try:
        return enum_type(value.casefold())
    except ValueError as exc:
        allowed = ", ".join(item.value for item in enum_type)
        raise ReportArtifactError(
            f"{field} must be one of: {allowed}; received {value!r}"
        ) from exc


def _parse_cves(value: str) -> tuple[str, ...]:
    candidates = [candidate.strip().upper() for candidate in value.split(",")]
    if not candidates or any(not candidate for candidate in candidates):
        raise ReportArtifactError("CVE IDs must contain complete identifiers")
    invalid = [
        candidate for candidate in candidates if not CVE_ID_PATTERN.fullmatch(candidate)
    ]
    if invalid:
        raise ReportArtifactError(
            "CVE IDs must use complete CVE-YYYY-NNNN identifiers: " + ", ".join(invalid)
        )
    return tuple(dict.fromkeys(candidates))


def _parse_reporting(value: str) -> tuple[ReportingReference, ...]:
    inline = MarkdownIt("commonmark").parseInline(value)
    children = inline[0].children if inline else None
    if not children:
        raise ReportArtifactError("Reporting must contain at least one source link")

    references: list[ReportingReference] = []
    index = 0
    while index < len(children):
        if children[index].type != "link_open":
            raise ReportArtifactError(
                "Reporting must be a comma-separated list of Markdown source links"
            )
        href = children[index].attrGet("href") or ""
        index += 1
        label_parts: list[str] = []
        while index < len(children) and children[index].type != "link_close":
            if children[index].type != "text":
                raise ReportArtifactError("Reporting link labels must be plain text")
            label_parts.append(children[index].content)
            index += 1
        if index >= len(children):
            raise ReportArtifactError("Reporting contains an unclosed source link")
        index += 1
        label = "".join(label_parts).strip()
        if " — " not in label:
            raise ReportArtifactError(
                "Reporting link labels must use 'Publisher — Title'"
            )
        publisher, title = (part.strip() for part in label.split(" — ", 1))
        if not publisher or not title:
            raise ReportArtifactError(
                "Reporting link labels must name a publisher and title"
            )
        try:
            url = normalize_reporting_url(href)
        except ReportingGroundingError as exc:
            raise ReportArtifactError(str(exc)) from exc
        references.append(
            ReportingReference(
                publisher=publisher,
                title=title,
                url=url,
                digest_fragment=reporting_fragment(url),
            )
        )
        if index < len(children):
            separator = children[index]
            if separator.type != "text" or not re.fullmatch(r",\s*", separator.content):
                raise ReportArtifactError("Reporting links must be separated by commas")
            index += 1

    urls = [reference.url for reference in references]
    if len(urls) != len(set(urls)):
        raise ReportArtifactError("Reporting contains duplicate source links")
    return tuple(references)


def _active_exploitation_section(body: str) -> str:
    match = re.search(
        r"^##\s+Active Exploitation Details\s*$\n(?P<section>.*?)(?=^##\s+|\Z)",
        body,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise ReportArtifactError("Missing Active Exploitation Details section")
    return match.group("section")


def _parse_findings(body: str, *, require_reporting: bool) -> tuple[Finding, ...]:
    section = _active_exploitation_section(body)
    matches = list(HEADING_PATTERN.finditer(section))
    if not matches:
        raise ReportArtifactError("Active Exploitation Details must include findings")

    findings: list[Finding] = []
    seen_slugs: set[str] = set()
    for index, match in enumerate(matches):
        title = match.group(1).strip()
        block_end = (
            matches[index + 1].start() if index + 1 < len(matches) else len(section)
        )
        block = section[match.end() : block_end]
        fields: dict[str, str] = {}
        for field_match in FIELD_PATTERN.finditer(block):
            field = field_match.group(1)
            canonical_field = "CVE IDs" if field in {"CVE ID", "CVE IDs"} else field
            if canonical_field in fields:
                raise ReportArtifactError(f"{title}: duplicate {canonical_field} field")
            fields[canonical_field] = field_match.group(2).strip()

        for required in ("Severity", "Exploitation Status", "Action"):
            if required not in fields:
                raise ReportArtifactError(f"{title}: missing required {required} field")
        if require_reporting and "Reporting" not in fields:
            raise ReportArtifactError(f"{title}: missing required Reporting field")

        slug = slugify(title)
        if slug in seen_slugs:
            raise ReportArtifactError(f"Duplicate finding slug: {slug}")
        seen_slugs.add(slug)

        findings.append(
            Finding(
                title=title,
                slug=slug,
                severity=_parse_enum(Severity, "Severity", fields["Severity"]),
                exploitation_status=_parse_enum(
                    ExploitationStatus,
                    "Exploitation Status",
                    fields["Exploitation Status"],
                ),
                action=_parse_enum(Action, "Action", fields["Action"]),
                cve_ids=_parse_cves(fields["CVE IDs"]) if "CVE IDs" in fields else (),
                reporting=(
                    _parse_reporting(fields["Reporting"])
                    if "Reporting" in fields
                    else ()
                ),
            )
        )

    return tuple(findings)


def parse_report_artifact(source: str) -> ReportArtifact:
    """Parse and validate a versioned Markdown report artifact."""
    metadata, body = _parse_front_matter(source)

    try:
        schema_version = int(_required_metadata(metadata, "schema_version"))
    except ValueError as exc:
        raise ReportArtifactError("schema_version must be an integer") from exc
    if schema_version not in {1, 2}:
        raise ReportArtifactError(f"Unsupported schema_version: {schema_version}")

    try:
        report_date = date.fromisoformat(_required_metadata(metadata, "report_date"))
    except ValueError as exc:
        raise ReportArtifactError("report_date must use YYYY-MM-DD") from exc
    generated_at = _parse_timestamp(_required_metadata(metadata, "generated_at"))
    digest_issue_url: str | None = None
    if schema_version == 2:
        digest_issue_url = _required_metadata(metadata, "digest_issue_url")
        expected_digest_url = f"{DIGEST_ARCHIVE_ROOT}{report_date.isoformat()}/"
        if digest_issue_url != expected_digest_url:
            raise ReportArtifactError(
                "digest_issue_url must identify the report date SentryDigest archive: "
                f"{expected_digest_url}"
            )
    findings = _parse_findings(body, require_reporting=schema_version == 2)
    if partial_cve := PARTIAL_CVE_PATTERN.search(body):
        raise ReportArtifactError(
            f"Report contains a partial CVE identifier: {partial_cve.group(0)}"
        )

    return ReportArtifact(
        schema_version=schema_version,
        report_date=report_date,
        generated_at=generated_at,
        body=body,
        source=source,
        findings=findings,
        digest_issue_url=digest_issue_url,
    )
