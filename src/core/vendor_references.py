"""Host-owned vendor URL selections; published reports retain ordinary URLs.

Fresh analysis requires the host protocol marker. Stored/public report URLs
continue through their existing artifact and evidence validation paths.
"""

import hashlib
import json
import re
from typing import Any, Mapping

from .finding_evidence import ABSENT, EvidenceError
from .report_findings import report_findings
from .reporting import ReportingSource

PROTOCOL_KEY = "vendor_reference_protocol"
PROTOCOL_VERSION = 1
REFERENCE = re.compile(r"vendor-[0-9a-f]{32}")
VENDOR_FIELD = re.compile(
    r"^(?P<prefix>-[ \t]+\*\*Vendor Links\*\*:[ \t]*)(?P<value>[^\r\n]*)$",
    re.MULTILINE,
)


def build_vendor_reference_context(
    catalog: Mapping[str, ReportingSource],
) -> list[dict[str, str]]:
    references = []
    for key, source in sorted(catalog.items()):
        content_hash = hashlib.sha256(source.content.encode()).hexdigest()
        for url in dict.fromkeys(source.links):
            identity = json.dumps([key, content_hash, url], ensure_ascii=True)
            references.append(
                {
                    "id": "vendor-"
                    + hashlib.sha256(identity.encode()).hexdigest()[:32],
                    "source_key": key,
                    "url": url,
                }
            )
    return references


def resolve_vendor_references(
    report: str, catalog: Mapping[str, ReportingSource]
) -> str:
    references = build_vendor_reference_context(catalog)
    available = {item["id"]: item for item in references}
    if len(available) != len(references):
        raise EvidenceError(
            "Vendor reference collision",
            code="vendor_reference_collision",
            field="Vendor Links",
        )
    table = report_findings(report)
    replacements = []
    for row in table.rows:

        def reject(code: str) -> EvidenceError:
            error = EvidenceError(code, code=code, field="Vendor Links")
            error.finding_index = row.index
            error.cves = row.cves
            error.source_keys = tuple(key for key in row.cited_keys if key in catalog)
            error.finding_sha256 = row.sha256
            return error

        matches = list(VENDOR_FIELD.finditer(row.body))
        if len(matches) != 1 or len(row.pairs) != len(row.fields()):
            raise reject("invalid_vendor_reference_field")
        field = matches[0]
        # Continuations must not hide a second selection outside the field.
        tail = row.body[field.end() :]
        next_field = re.search(r"^-\s+\*\*", tail, re.MULTILINE)
        if tail[: next_field.start() if next_field else len(tail)].strip():
            raise reject("invalid_vendor_reference_field")
        value = field["value"].strip()
        if value == ABSENT:
            continue
        refs = [part.strip() for part in value.split(";")]
        if any(not REFERENCE.fullmatch(ref) for ref in refs):
            raise reject("invalid_vendor_reference")
        if len(refs) != len(set(refs)):
            raise reject("duplicate_vendor_reference")
        if any(
            ref not in available or available[ref]["source_key"] not in row.cited_keys
            for ref in refs
        ):
            raise reject("unsupported_vendor_reference")
        urls = [available[ref]["url"] for ref in refs]
        if len(urls) != len(set(urls)):
            raise reject("duplicate_vendor_reference")
        replacements.append(
            (
                row.body_start + field.start("value"),
                row.body_start + field.end("value"),
                "; ".join(urls),
            )
        )
    if not table.rows:
        raise EvidenceError(
            "Missing findings", code="missing_finding_section", field="Vendor Links"
        )
    scrubbed = table.render((start, end, ABSENT) for start, end, _ in replacements)
    if REFERENCE.search(scrubbed):
        raise EvidenceError(
            "Misplaced vendor reference",
            code="misplaced_vendor_reference",
            field="Vendor Links",
        )
    return table.render(replacements)


def resolve_analysis_vendor_references(
    result: Mapping[str, Any], report: str, catalog: Mapping[str, ReportingSource]
) -> str:
    if (
        type(result.get(PROTOCOL_KEY)) is not int
        or result.get(PROTOCOL_KEY) != PROTOCOL_VERSION
    ):
        raise EvidenceError(
            "Invalid vendor reference protocol",
            code="invalid_vendor_reference_protocol",
            field="Vendor Links",
        )
    return resolve_vendor_references(report, catalog)
