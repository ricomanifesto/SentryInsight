"""Source-owned vendor link IDs: offered in the prompt, resolved by the host.

Each offered ID names one exact (Reporting key, source content, normalized
URL) triple from an eligible source's ``links``, so the same URL in two
sources gets two IDs, an ID always identifies its owner, and an ID minted for
different source content never resolves against a changed source. The model copies IDs instead of URLs; the
host replaces an ID with its URL only when the owning source is cited by that
same finding. Everything else stays exactly as written for the existing
vendor-link validators, so raw URLs and absence keep today's strict behavior.
A field that selects the same ID twice, or reaches the same URL twice through
an ID, is malformed: the reference path never repeats a selection.

The host never guesses, substitutes or drops a link, and never writes absence.
"""

import hashlib
import re
from typing import Mapping

from .finding_evidence import EvidenceError
from .report_findings import FIELD, FindingRow, report_findings
from .reporting import (
    ReportingGroundingError,
    ReportingSource,
    normalize_reporting_url,
)
from .source_review import SourceReviewError

LINK_ID_PATTERN = re.compile(r"link-[0-9a-f]{16}")
# An ID-shaped token that is not part of a URL, path, query or longer word.
STRAY_LINK_ID_PATTERN = re.compile(r"(?<![\w/.~%=?&#:@+-])link-[0-9a-f]{16}(?![\w-])")
_DOMAIN = b"sentryinsight/vendor-link-id/v2\n"
FIELD_NAME = "Vendor Links"


def link_id(source_key: str, content: str, url: str) -> str:
    """Domain-separated digest of owner key, source-content digest and URL."""
    content_sha256 = hashlib.sha256(content.encode()).hexdigest()
    preimage = "\n".join((source_key, content_sha256, url)).encode()
    return "link-" + hashlib.sha256(_DOMAIN + preimage).hexdigest()[:16]


def _offerable(url: str) -> bool:
    """Only URLs that survive the semicolon field grammar unchanged.

    A link containing the separator stays on the legacy raw-URL path, where it
    fails closed; the host never encodes a separator into a different URL.
    """
    if type(url) is not str or ";" in url or url != url.strip() or not url:
        return False
    try:
        return normalize_reporting_url(url) == url
    except ReportingGroundingError:
        return False


def vendor_link_targets(
    catalog: Mapping[str, ReportingSource],
) -> dict[str, tuple[str, str]]:
    """Map each offered ID to its (owning key, URL); a collision fails closed."""
    targets: dict[str, tuple[str, str]] = {}
    for key, source in catalog.items():
        for url in source.links:
            if not _offerable(url):
                continue
            identity = link_id(key, source.content, url)
            existing = targets.setdefault(identity, (key, url))
            if existing != (key, url):
                raise SourceReviewError("invalid_review_input_catalog")
    return targets


def build_vendor_link_context(
    catalog: Mapping[str, ReportingSource],
) -> dict[str, list[list[str]]]:
    """Compact prompt contract: Reporting key -> [[ID, URL], ...]."""
    context: dict[str, list[list[str]]] = {}
    for identity, (key, url) in vendor_link_targets(catalog).items():
        context.setdefault(key, []).append([identity, url])
    return context


def _reject(code: str, row: FindingRow | None, catalog) -> EvidenceError:
    error = EvidenceError(
        "Unsupported vendor link",
        code=code,
        field=FIELD_NAME,
        expected=True,
        observed=False,
    )
    if row is not None:
        error.finding_index = row.index
        error.cves = row.cves
        error.source_keys = tuple(key for key in row.cited_keys if key in catalog)
        error.finding_sha256 = row.sha256
    return error


def _normalizes(entry: str) -> bool:
    try:
        normalize_reporting_url(entry)
    except ReportingGroundingError:
        return False
    return True


def _resolve_value(
    value: str,
    row: FindingRow,
    targets: Mapping[str, tuple[str, str]],
    catalog: Mapping[str, ReportingSource],
) -> str:
    parts = value.split(";")
    entries = [part.strip() for part in parts]
    ids = [entry for entry in entries if LINK_ID_PATTERN.fullmatch(entry)]
    if not ids:
        return value
    if not all(
        LINK_ID_PATTERN.fullmatch(entry) or _normalizes(entry) for entry in entries
    ):
        # Malformed syntax wins, exactly as the validators order it today.
        # Leave the field untouched; the validators and the stray-ID check
        # reject it as invalid_vendor_link.
        return value
    if len(set(ids)) != len(ids):
        raise _reject("invalid_vendor_link", row, catalog)
    cited = set(row.cited_keys)
    resolved = []
    for part, entry in zip(parts, entries, strict=True):
        if not LINK_ID_PATTERN.fullmatch(entry):
            resolved.append(part)
            continue
        target = targets.get(entry)
        if target is None or target[0] not in cited or target[0] not in catalog:
            raise _reject("unsupported_vendor_link", row, catalog)
        start = part.index(entry)
        resolved.append(part[:start] + target[1] + part[start + len(entry) :])
    urls = [normalize_reporting_url(part.strip()) for part in resolved]
    if len(set(urls)) != len(urls):
        # Two IDs, or an ID and a raw entry, select the same resolved URL.
        raise _reject("invalid_vendor_link", row, catalog)
    return ";".join(resolved)


def resolve_vendor_link_ids(report: str, catalog: Mapping[str, ReportingSource]) -> str:
    """Replace each finding's owned IDs with their URLs; reject the rest.

    Run on canonical text whose Reporting fields are already exact eligible
    keys, before grouping, so a merge can never lend another finding's
    citation to an ID. No unresolved ID survives into the returned text.
    """
    targets = vendor_link_targets(catalog)
    table = report_findings(report)
    replacements = []
    for row in table.rows:
        edits = []
        for match in FIELD.finditer(row.body):
            if match[1] != FIELD_NAME:
                continue
            value = _resolve_value(match[2], row, targets, catalog)
            if value != match[2]:
                edits.append((match.start(2), match.end(2), value))
        if edits:
            body = row.body
            for start, end, value in reversed(edits):
                body = body[:start] + value + body[end:]
            replacements.append((row.start, row.end, row.heading + body))
    resolved = table.render(replacements)
    stray = STRAY_LINK_ID_PATTERN.search(resolved)
    if stray:
        owner = next(
            (
                row
                for row in report_findings(resolved).rows
                if row.start <= stray.start() < row.end
            ),
            None,
        )
        raise _reject("invalid_vendor_link", owner, catalog)
    return resolved
