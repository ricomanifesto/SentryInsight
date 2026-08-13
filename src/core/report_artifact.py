"""Versioned, source-owned report artifact contract."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import TypeVar

CVE_ID_PATTERN = re.compile(r"^CVE-\d{4}-\d{4,}$", re.IGNORECASE)
PARTIAL_CVE_PATTERN = re.compile(r"\bCVE-\d{4}-\d{0,3}(?!\d)", re.IGNORECASE)
HEADING_PATTERN = re.compile(r"^###\s+(.+?)\s*$", re.MULTILINE)
FIELD_PATTERN = re.compile(
    r"^-\s+\*\*(Severity|Exploitation Status|Action|CVE IDs?)\*\*:\s*(.*?)\s*$",
    re.MULTILINE,
)


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
class Finding:
    title: str
    slug: str
    severity: Severity
    exploitation_status: ExploitationStatus
    action: Action
    cve_ids: tuple[str, ...]


@dataclass(frozen=True)
class ReportArtifact:
    schema_version: int
    report_date: date
    generated_at: datetime
    body: str
    source: str
    findings: tuple[Finding, ...]


def slugify(value: str) -> str:
    """Return a stable, human-readable HTML fragment identifier."""
    slug = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
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


def _active_exploitation_section(body: str) -> str:
    match = re.search(
        r"^##\s+Active Exploitation Details\s*$\n(?P<section>.*?)(?=^##\s+|\Z)",
        body,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise ReportArtifactError("Missing Active Exploitation Details section")
    return match.group("section")


def _parse_findings(body: str) -> tuple[Finding, ...]:
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
    if schema_version != 1:
        raise ReportArtifactError(f"Unsupported schema_version: {schema_version}")

    try:
        report_date = date.fromisoformat(_required_metadata(metadata, "report_date"))
    except ValueError as exc:
        raise ReportArtifactError("report_date must use YYYY-MM-DD") from exc
    generated_at = _parse_timestamp(_required_metadata(metadata, "generated_at"))
    findings = _parse_findings(body)
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
    )
