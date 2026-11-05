#!/usr/bin/env python3
"""Build deterministic static SentryInsight report and archive pages."""

from __future__ import annotations

# ruff: noqa: E402

import argparse
import hashlib
import html
import json
import re
import shutil
import sys
import tempfile
from dataclasses import asdict
from datetime import timezone
from pathlib import Path
from typing import TypedDict
from urllib.parse import urlsplit

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from markdown_it import MarkdownIt
from markdown_it.token import Token

from src.core.public_site import emitted_origin
from src.core.report_artifact import (
    Finding,
    ReportArtifact,
    parse_report_artifact,
    slugify,
)
from src.core.version_state import VersionEvidenceStatus
from src.core.source_coverage import (
    coverage_html,
    coverage_notice_html,
    split_source_coverage,
)

PUBLIC_ROOT = emitted_origin("SentryInsight")
CVE_TEXT_PATTERN = re.compile(r"\bCVE-\d{4}-\d{4,}\b", re.IGNORECASE)
# A trailing "— CVE-…" or "(CVE-…)" in a finding title repeats the linked CVE
# chips beside it, and the title sits inside a button where it cannot link.
TITLE_CVE_SUFFIX_PATTERN = re.compile(
    r"\s*(?:[—–-]\s*|\(\s*)"
    r"(CVE-\d{4}-\d{4,}(?:\s*(?:,|/|&|and)\s*CVE-\d{4}-\d{4,})*)"
    r"\s*\)?\s*$",
    re.IGNORECASE,
)
STRUCTURED_FINDING_FIELD_PATTERN = re.compile(
    r"^\*\*(Severity|Exploitation Status|Action|CVE IDs?|Reporting|Vendor Links|Affected Versions Status)\*\*:",
    re.IGNORECASE,
)
BADGE_LABELS = {
    "severity": {
        "critical": "Critical",
        "high": "High",
        "medium": "Medium",
        "low": "Low",
        "unknown": "Severity unknown",
    },
    "exploitation_status": {
        "active": "Exploited in the wild",
        "observed": "Exploitation observed",
        "potential": "Exploitable, no attacks seen",
        "not_observed": "No exploitation seen",
        "unknown": "Exploitation unknown",
    },
    "action": {
        "patch": "Patch",
        "mitigate": "Mitigate",
        "investigate": "Investigate",
        "monitor": "Monitor",
        "none": "No action listed",
    },
}
# Plain-language meanings, matching the generation and evidence rules.
BADGE_DESCRIPTIONS = {
    "severity": {
        "critical": "The source rates it critical or gives a CVSS score of 9.0 or higher.",
        "high": "The source rates it high or gives a CVSS score from 7.0 to 8.9.",
        "medium": "The source rates it medium or gives a CVSS score from 4.0 to 6.9.",
        "low": "The source rates it low or gives a CVSS score below 4.0.",
        "unknown": "No source states a severity or CVSS score.",
    },
    "exploitation_status": {
        "active": "A source directly confirms attackers are exploiting this CVE.",
        "observed": "A source reports exploitation telemetry, but of limited scope.",
        "potential": "A proof of concept or likely risk exists, but no source confirms attacks.",
        "not_observed": "A source explicitly says exploitation has not been seen.",
        "unknown": "The sources do not establish whether it is being exploited.",
    },
    "action": {
        "patch": "A fix is available: apply it.",
        "mitigate": "A source gives a workaround to apply.",
        "investigate": "Check your environment for signs of compromise.",
        "monitor": "Watch for updates; no other action is supported yet.",
        "none": "The sources support no specific action.",
    },
}
LEGEND_HEADINGS = {
    "severity": "Severity",
    "exploitation_status": "Exploitation",
    "action": "Action",
}


class ArchiveEntry(TypedDict):
    report_date: str
    generated_at: str
    html_path: str
    markdown_path: str
    finding_count: int
    cve_count: int


class ArchiveConflictError(RuntimeError):
    """Raised when a dated immutable archive already contains other content."""


class SiteBuildError(RuntimeError):
    """Raised when safe static output cannot be produced."""


def _timestamp(value) -> str:
    return (
        value.astimezone(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z")
    )


def _date_label(value) -> str:
    return f"{value.strftime('%A, %B')} {value.day}, {value.year}"


def _edition_label(value) -> str:
    return f"{value.strftime('%B')} {value.day}, {value.year}"


def _generated_label(value) -> str:
    utc_value = value.astimezone(timezone.utc)
    return f"{utc_value.strftime('%B')} {utc_value.day}, {utc_value.year} at {utc_value.strftime('%H:%M')} UTC"


def _strip_raw_html(tokens: list[Token]) -> None:
    for token in tokens:
        if token.type in {"html_inline", "html_block"}:
            token.content = ""
        if token.children:
            _strip_raw_html(token.children)


def _literal_single_asterisks(tokens: list[Token]) -> None:
    """Keep single ``*`` as text: reports quote password hashes and wildcards.

    Generated prose only uses ``**bold**`` labels. A lone asterisk such as
    ``"*"`` or ``*sshole`` otherwise pairs with a later one and italicizes,
    and drops, the text between them.
    """
    for token in tokens:
        if not token.children:
            continue
        for index, child in enumerate(token.children):
            if child.type in {"em_open", "em_close"} and child.markup == "*":
                text = Token("text", "", 0)
                text.content = "*"
                token.children[index] = text


def _display_title(finding: Finding) -> str:
    """Drop a trailing CVE suffix that only repeats the finding's CVE chips."""
    match = TITLE_CVE_SUFFIX_PATTERN.search(finding.title)
    if not match or not finding.cve_ids:
        return finding.title
    suffix_cves = {cve.upper() for cve in CVE_TEXT_PATTERN.findall(match.group(1))}
    if not suffix_cves <= set(finding.cve_ids):
        return finding.title
    return finding.title[: match.start()].rstrip() or finding.title


def _vendor_link_labels(urls) -> list[str]:
    """Label each vendor link by its host, numbering repeated hosts."""
    labels = []
    seen: dict[str, int] = {}
    for url in urls:
        host = urlsplit(url).hostname or "Vendor advisory"
        host = host.removeprefix("www.")
        seen[host] = seen.get(host, 0) + 1
        labels.append(host if seen[host] == 1 else f"{host} ({seen[host]})")
    return labels


def _link_cves(tokens: list[Token]) -> None:
    for token in tokens:
        if not token.children:
            continue
        linked_children: list[Token] = []
        link_depth = 0
        for child in token.children:
            if child.type == "link_open":
                link_depth += 1
                linked_children.append(child)
                continue
            if child.type == "link_close":
                link_depth = max(0, link_depth - 1)
                linked_children.append(child)
                continue
            if child.type != "text" or link_depth:
                linked_children.append(child)
                continue

            cursor = 0
            for match in CVE_TEXT_PATTERN.finditer(child.content):
                if match.start() > cursor:
                    before = Token("text", "", 0)
                    before.content = child.content[cursor : match.start()]
                    linked_children.append(before)
                cve = match.group(0).upper()
                link_open = Token("link_open", "a", 1)
                link_open.attrSet("href", f"https://nvd.nist.gov/vuln/detail/{cve}")
                link_open.attrSet("class", "cve-link")
                link_open.attrSet("target", "_blank")
                link_open.attrSet("rel", "noopener noreferrer")
                link_text = Token("text", "", 0)
                link_text.content = cve
                link_close = Token("link_close", "a", -1)
                linked_children.extend((link_open, link_text, link_close))
                cursor = match.end()
            if cursor:
                if cursor < len(child.content):
                    after = Token("text", "", 0)
                    after.content = child.content[cursor:]
                    linked_children.append(after)
            else:
                linked_children.append(child)
        token.children = linked_children


def _strip_structured_finding_fields(tokens: list[Token]) -> list[Token]:
    """Remove artifact-only fields after they have been parsed into metadata."""
    rendered_tokens: list[Token] = []
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if token.type != "list_item_open":
            rendered_tokens.append(token)
            index += 1
            continue

        depth = 1
        end = index + 1
        while end < len(tokens) and depth:
            if tokens[end].type == "list_item_open":
                depth += 1
            elif tokens[end].type == "list_item_close":
                depth -= 1
            end += 1
        item_tokens = tokens[index:end]
        inline_text = " ".join(
            item.content for item in item_tokens if item.type == "inline"
        ).strip()
        if not STRUCTURED_FINDING_FIELD_PATTERN.match(inline_text):
            rendered_tokens.extend(item_tokens)
        index = end
    return rendered_tokens


def _controlled_html(content: str, *, block: bool = False) -> Token:
    token = Token("html_block" if block else "html_inline", "", 0)
    token.content = content
    return token


def _badge(dimension: str, value: str) -> str:
    label = BADGE_LABELS[dimension][value]
    description = BADGE_DESCRIPTIONS[dimension][value]
    class_name = dimension.replace("_", "-")
    return (
        f'<span class="badge badge-{class_name}" data-value="{html.escape(value)}" '
        f'title="{html.escape(description)}">'
        f"{html.escape(label)}</span>"
    )


def _badge_legend_html() -> str:
    """A visible key: badge tooltips are unavailable on touch devices."""
    groups = []
    for dimension, heading in LEGEND_HEADINGS.items():
        class_name = dimension.replace("_", "-")
        rows = "".join(
            f'<dt><span class="badge-key badge badge-{class_name}" data-value="{html.escape(value)}">'
            f"{html.escape(label)}</span></dt>"
            f"<dd>{html.escape(BADGE_DESCRIPTIONS[dimension][value])}</dd>"
            for value, label in BADGE_LABELS[dimension].items()
        )
        groups.append(
            f'<div class="badge-legend-group"><p class="badge-legend-heading">{html.escape(heading)}</p>'
            f"<dl>{rows}</dl></div>"
        )
    return (
        '<details class="badge-legend"><summary>What the labels mean</summary>'
        '<div class="badge-legend-body">' + "".join(groups) + "</div></details>\n"
    )


def _finding_heading_html(finding: Finding, claimed_cves: set[str]) -> str:
    badges = "".join(
        (
            _badge("severity", finding.severity.value),
            _badge("exploitation_status", finding.exploitation_status.value),
            _badge("action", finding.action.value),
        )
    )
    cves = "".join(
        f'<a class="cve-chip" href="https://nvd.nist.gov/vuln/detail/{html.escape(cve)}" '
        f'target="_blank" rel="noopener noreferrer">{html.escape(cve)}</a>'
        for cve in finding.cve_ids
    )
    cve_group = f'<span class="cve-list">{cves}</span>' if cves else ""
    handoff_cves = [cve for cve in finding.cve_ids if cve not in claimed_cves]
    claimed_cves.update(handoff_cves)
    cve_handoff_targets = "".join(
        f'<span id="{html.escape(cve.lower())}" class="cve-handoff-target" '
        'aria-hidden="true"></span>'
        for cve in handoff_cves
    )
    title = html.escape(_display_title(finding))
    heading_id = html.escape(finding.slug)
    return (
        f"{cve_handoff_targets}"
        f'<button type="button" class="finding-disclosure" aria-expanded="true" '
        f'aria-controls="{heading_id}-details">'
        '<span class="disclosure-icon" aria-hidden="true">−</span>'
        f'<span class="finding-title">{title}</span>'
        "</button>"
        '<span class="finding-supporting">'
        f'<span class="badge-list" aria-label="Finding classification">{badges}</span>'
        f"{cve_group}"
        f'<a class="heading-anchor" href="#{heading_id}" '
        f'aria-label="Copy link to {title}">#</a>'
        "</span>"
    )


def _finding_reporting_html(finding: Finding, digest_issue_url: str | None) -> str:
    version_notice = (
        '<p class="vendor-guidance"><strong>Affected versions unresolved.</strong> '
        "Review the linked reporting before inferring an affected version range.</p>"
        if finding.affected_versions_status == VersionEvidenceStatus.UNRESOLVED
        else ""
    )
    vendor = ""
    if finding.vendor_links:
        links = ", ".join(
            f'<a href="{html.escape(url)}" target="_blank" rel="noopener noreferrer">'
            f"{html.escape(label)}</a>"
            for url, label in zip(
                finding.vendor_links, _vendor_link_labels(finding.vendor_links)
            )
        )
        vendor = (
            f'<p class="vendor-guidance"><strong>Vendor guidance:</strong> {links}</p>'
        )
    elif finding.affected_versions is not None:
        vendor = '<p class="vendor-guidance"><strong>Vendor guidance:</strong> Not stated in supplied sources.</p>'
    if not finding.reporting or not digest_issue_url:
        return version_notice + vendor
    items = []
    for reference in finding.reporting:
        label = f"{reference.publisher} — {reference.title}"
        digest_url = f"{digest_issue_url}#{reference.digest_fragment}"
        items.append(
            "<li>"
            f'<a class="reporting-source" href="{html.escape(reference.url)}" '
            f'target="_blank" rel="noopener noreferrer">{html.escape(label)}</a>'
            '<span aria-hidden="true"> · </span>'
            f'<a class="reporting-context" href="{html.escape(digest_url)}">'
            "Digest context</a>"
            "</li>"
        )
    return (
        f'<aside class="finding-reporting" aria-label="Reporting for {html.escape(finding.title)}">'
        "<strong>Reporting</strong><ul>"
        + "".join(items)
        + "</ul>"
        + version_notice
        + vendor
        + "</aside>\n"
    )


def _enhance_finding_tokens(
    tokens: list[Token], findings: dict[str, Finding], digest_issue_url: str | None
) -> list[Token]:
    """Build disclosure controls and classification into the initial HTML."""
    enhanced: list[Token] = []
    finding_body_open = False
    claimed_cves: set[str] = set()
    legend_emitted = False
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if (
            finding_body_open
            and token.type == "heading_open"
            and token.tag in {"h2", "h3"}
        ):
            enhanced.append(_controlled_html("</div>\n", block=True))
            finding_body_open = False

        if token.type == "heading_open" and token.tag == "h3":
            inline = tokens[index + 1]
            finding = findings.get(slugify(inline.content.strip()))
            if finding is not None:
                if not legend_emitted:
                    enhanced.append(_controlled_html(_badge_legend_html(), block=True))
                    legend_emitted = True
                token.attrSet("class", "finding-heading")
                token.attrSet("data-expanded", "true")
                enhanced.extend(
                    (
                        token,
                        _controlled_html(_finding_heading_html(finding, claimed_cves)),
                        tokens[index + 2],
                        _controlled_html(
                            f'<div id="{html.escape(finding.slug)}-details" '
                            'class="finding-body">\n',
                            block=True,
                        ),
                        _controlled_html(
                            _finding_reporting_html(finding, digest_issue_url),
                            block=True,
                        ),
                    )
                )
                finding_body_open = True
                index += 3
                continue

        enhanced.append(token)
        index += 1

    if finding_body_open:
        enhanced.append(_controlled_html("</div>\n", block=True))
    return enhanced


def _heading_entries(tokens: list[Token]) -> list[tuple[int, str, str]]:
    entries: list[tuple[int, str, str]] = []
    for index, token in enumerate(tokens):
        if token.type != "heading_open" or token.tag not in {"h2", "h3"}:
            continue
        inline = tokens[index + 1]
        title = inline.content.strip()
        entries.append((int(token.tag[1]), title, slugify(title)))
    return entries


def _without_source_title(tokens: list[Token]) -> list[Token]:
    for index, token in enumerate(tokens):
        if token.type != "heading_open" or token.tag != "h1":
            continue
        if (
            index + 2 < len(tokens)
            and tokens[index + 1].type == "inline"
            and tokens[index + 2].type == "heading_close"
        ):
            return tokens[:index] + tokens[index + 3 :]
    return tokens


def _render_markdown(
    artifact: ReportArtifact,
) -> tuple[str, list[tuple[int, str, str]]]:
    markdown = MarkdownIt("commonmark", {"html": True})
    body = (
        split_source_coverage(artifact.body, artifact.source_coverage)
        if artifact.source_coverage is not None
        else artifact.body
    )
    tokens = markdown.parse(body)
    _strip_raw_html(tokens)
    tokens = _strip_structured_finding_fields(tokens)
    _literal_single_asterisks(tokens)
    _link_cves(tokens)
    tokens = _without_source_title(tokens)

    findings = {finding.slug: finding for finding in artifact.findings}
    heading_entries = [
        (
            level,
            _display_title(findings[slug]) if slug in findings else title,
            slug,
        )
        for level, title, slug in _heading_entries(tokens)
    ]
    for index, token in enumerate(tokens):
        if token.type != "heading_open" or token.tag not in {"h2", "h3"}:
            continue
        title = tokens[index + 1].content.strip()
        heading_slug = slugify(title)
        token.attrSet("id", heading_slug)
        finding = findings.get(heading_slug)
        if finding is not None:
            token.attrSet("data-severity", finding.severity.value)
            token.attrSet("data-exploitation-status", finding.exploitation_status.value)
            token.attrSet("data-action", finding.action.value)
            if finding.cve_ids:
                token.attrSet("data-cves", ",".join(finding.cve_ids))

    tokens = _enhance_finding_tokens(tokens, findings, artifact.digest_issue_url)

    rendered = markdown.renderer.render(tokens, markdown.options, {})
    lowered = rendered.casefold()
    forbidden = ("<script", "<iframe", "<object", "<embed", "onerror=", "onclick=")
    if any(value in lowered for value in forbidden) or re.search(
        r"href\s*=\s*['\"]\s*javascript:", rendered, re.IGNORECASE
    ):
        raise SiteBuildError("Rendered report contains active content")
    if artifact.source_coverage is not None:
        rendered += coverage_html(artifact.source_coverage)
        heading_entries.append(
            (2, "Source Coverage and Review", "source-coverage-and-review")
        )
    return rendered, heading_entries


def _toc(entries: list[tuple[int, str, str]]) -> str:
    links = []
    for level, title, heading_slug in entries:
        class_name = "section-link" if level == 2 else "finding-link"
        links.append(
            f'<a class="{class_name}" href="#{html.escape(heading_slug)}">'
            f"{html.escape(title)}</a>"
        )
    return "".join(links)


def _finding_json(finding: Finding) -> dict[str, object]:
    value = asdict(finding)
    value["severity"] = finding.severity.value
    value["exploitation_status"] = finding.exploitation_status.value
    value["action"] = finding.action.value
    value["cve_ids"] = list(finding.cve_ids)
    if finding.affected_versions_status is None:
        value.pop("affected_versions_status")
    else:
        value["affected_versions_status"] = finding.affected_versions_status.value
    return value


def _report_shape(artifact: ReportArtifact) -> tuple[int, int, str]:
    finding_count = len(artifact.findings)
    complete_cve_count = len(
        {cve for finding in artifact.findings for cve in finding.cve_ids}
    )
    finding_label = "finding" if finding_count == 1 else "findings"
    cve_label = "CVE" if complete_cve_count == 1 else "CVEs"
    return (
        finding_count,
        complete_cve_count,
        f"{finding_count} {finding_label} · {complete_cve_count} {cve_label}",
    )


def _current_findings_manifest(artifact: ReportArtifact) -> dict[str, object]:
    finding_count, complete_cve_count, _label = _report_shape(artifact)
    cve_ids = list(
        dict.fromkeys(cve for finding in artifact.findings for cve in finding.cve_ids)
    )
    return {
        "schema_version": 1,
        "report_date": artifact.report_date.isoformat(),
        "generated_at": _timestamp(artifact.generated_at),
        "report_url": PUBLIC_ROOT,
        "finding_count": finding_count,
        "complete_cve_count": complete_cve_count,
        "cve_ids": cve_ids,
    }


def _template(path: Path, values: dict[str, str]) -> str:
    rendered = path.read_text()
    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    unresolved = re.findall(r"{{[A-Z0-9_]+}}", rendered)
    if unresolved:
        raise SiteBuildError(f"Unresolved template values: {', '.join(unresolved)}")
    return rendered


def _render_report_page(
    artifact: ReportArtifact,
    *,
    template_path: Path,
    asset_version: str,
    root_prefix: str,
    markdown_path: str,
    canonical_url: str,
    relative_age: bool,
) -> str:
    report_html, headings = _render_markdown(artifact)
    finding_count, complete_cve_count, report_shape = _report_shape(artifact)
    metadata: dict[str, object] = {
        "schema_version": artifact.schema_version,
        "report_date": artifact.report_date.isoformat(),
        "generated_at": _timestamp(artifact.generated_at),
        "finding_count": finding_count,
        "complete_cve_count": complete_cve_count,
        "digest_issue_url": artifact.digest_issue_url,
        "findings": [_finding_json(finding) for finding in artifact.findings],
    }
    if artifact.schema_version >= 4:
        metadata["unresolved_version_count"] = artifact.unresolved_version_count
    if artifact.source_coverage is not None:
        metadata["source_coverage"] = artifact.source_coverage
        report_html = coverage_notice_html(artifact.source_coverage) + report_html
    if artifact.unresolved_version_count:
        count = artifact.unresolved_version_count
        subject = "1 finding has" if count == 1 else f"{count} findings have"
        report_html = (
            f'<p class="vendor-guidance" role="note"><strong>{subject} unresolved affected-version evidence.</strong> '
            "Review each finding’s linked reporting before inferring version ranges.</p>"
            + report_html
        )
    toc = _toc(headings)
    page_title = f"SentryInsight report for {_date_label(artifact.report_date)}"
    identity = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "SentryInsight",
        "url": canonical_url,
        "description": "Current exploitation intelligence for rapid defensive triage.",
        "datePublished": artifact.report_date.isoformat(),
        "dateModified": _timestamp(artifact.generated_at),
        "author": {
            "@type": "Person",
            "name": "Michael Rico",
            "url": "https://ricomanifesto.com/",
        },
        "sameAs": "https://github.com/ricomanifesto/SentryInsight",
    }
    return _template(
        template_path / "report.html",
        {
            "PAGE_TITLE": page_title,
            "CANONICAL_URL": canonical_url,
            "ROOT_PREFIX": root_prefix,
            "MARKDOWN_PATH": markdown_path,
            "ASSET_VERSION": asset_version,
            "REPORT_DATE_ISO": artifact.report_date.isoformat(),
            "REPORT_EDITION_LABEL": _edition_label(artifact.report_date),
            "GENERATED_AT_ISO": _timestamp(artifact.generated_at),
            "GENERATED_AT_LABEL": _generated_label(artifact.generated_at),
            "REPORT_AGE_SUFFIX": (
                '<span id="report-age"></span>'
                if relative_age
                else '<span class="report-frozen"> · Archived snapshot</span>'
            ),
            "REPORT_SHAPE": report_shape,
            "DIGEST_ISSUE_URL": artifact.digest_issue_url
            or emitted_origin("SentryDigest"),
            "THEME_BOOTSTRAP": (template_path / "theme-bootstrap.js")
            .read_text()
            .strip(),
            "DESKTOP_TOC": toc,
            "MOBILE_TOC": toc,
            "REPORT_HTML": report_html,
            "REPORT_JSON": (
                json.dumps(metadata, separators=(",", ":"))
                .replace("&", "\\u0026")
                .replace("<", "\\u003c")
                .replace(">", "\\u003e")
                if artifact.source_coverage is not None
                else html.escape(
                    json.dumps(metadata, separators=(",", ":")), quote=False
                ).replace("</", "<\\/")
            ),
            "REPORT_IDENTITY_JSON": json.dumps(identity, separators=(",", ":")).replace(
                "</", "<\\/"
            ),
        },
    )


def _write_immutable(path: Path, content: str) -> None:
    if path.exists():
        if path.read_text() != content:
            raise ArchiveConflictError(
                f"Refusing to overwrite dated archive {path.stem} with different content"
            )
        return
    path.write_text(content)


def archive_previous_report(
    *, current_source: str, next_report: ReportArtifact, reports_path: Path
) -> None:
    """Archive the prior current report only when the report date advances."""
    current_report = parse_report_artifact(current_source)
    if next_report.report_date < current_report.report_date:
        raise ArchiveConflictError(
            "Refusing to publish a report older than the current report: "
            f"{next_report.report_date.isoformat()} < {current_report.report_date.isoformat()}"
        )
    if next_report.report_date == current_report.report_date:
        return

    reports_path.mkdir(parents=True, exist_ok=True)
    archived_path = reports_path / f"{current_report.report_date.isoformat()}.md"
    _write_immutable(archived_path, current_source)


def _archive_entry(artifact: ReportArtifact) -> ArchiveEntry:
    finding_count, complete_cve_count, _report_shape_label = _report_shape(artifact)
    return {
        "report_date": artifact.report_date.isoformat(),
        "generated_at": _timestamp(artifact.generated_at),
        "html_path": f"{artifact.report_date.isoformat()}.html",
        "markdown_path": f"{artifact.report_date.isoformat()}.md",
        "finding_count": finding_count,
        "cve_count": complete_cve_count,
    }


def _archive_items(entries: list[ArchiveEntry]) -> str:
    if not entries:
        return '<li class="archive-empty">No archived reports yet.</li>'
    items = []
    for entry in entries:
        report_date = str(entry["report_date"])
        findings = entry["finding_count"]
        cves = entry["cve_count"]
        finding_label = "finding" if findings == 1 else "findings"
        cve_label = "CVE" if cves == 1 else "CVEs"
        items.append(
            "<li><article>"
            f'<h2><a href="{html.escape(str(entry["html_path"]))}">Report for {html.escape(report_date)}</a></h2>'
            f"<p>{findings} {finding_label} · {cves} {cve_label}</p>"
            f'<p><a href="{html.escape(str(entry["markdown_path"]))}">Source Markdown</a></p>'
            "</article></li>"
        )
    return "".join(items)


def build_site(*, report_path: Path, output_path: Path, template_path: Path) -> None:
    """Build the latest report plus generated, dated archive projections."""
    artifact = parse_report_artifact(report_path.read_text())
    output_path.mkdir(parents=True, exist_ok=True)
    reports_path = output_path / "reports"
    reports_path.mkdir(parents=True, exist_ok=True)
    assets_path = output_path / "assets"
    assets_path.mkdir(parents=True, exist_ok=True)
    vendor_path = assets_path / "vendor"
    vendor_path.mkdir(parents=True, exist_ok=True)

    css = (template_path / "site.css").read_text()
    script = (template_path / "report.js").read_text()
    theme_bootstrap = (template_path / "theme-bootstrap.js").read_text()
    dompurify = (template_path / "vendor" / "dompurify.min.js").read_text()
    dompurify_license = (template_path / "vendor" / "DOMPURIFY-LICENSE.txt").read_text()
    asset_version = hashlib.sha256(
        (css + script + theme_bootstrap + dompurify).encode()
    ).hexdigest()[:12]
    (assets_path / "site.css").write_text(css)
    (assets_path / "report.js").write_text(script)
    (vendor_path / "dompurify.min.js").write_text(dompurify)
    (vendor_path / "DOMPURIFY-LICENSE.txt").write_text(dompurify_license)

    archived_artifacts: list[ReportArtifact] = []
    for archived_path in sorted(reports_path.glob("????-??-??.md"), reverse=True):
        archived_artifacts.append(parse_report_artifact(archived_path.read_text()))

    for archived in archived_artifacts:
        dated_html = _render_report_page(
            archived,
            template_path=template_path,
            asset_version=asset_version,
            root_prefix="../",
            markdown_path=f"{archived.report_date.isoformat()}.md",
            canonical_url=f"{PUBLIC_ROOT}reports/{archived.report_date.isoformat()}.html",
            relative_age=False,
        )
        (reports_path / f"{archived.report_date.isoformat()}.html").write_text(
            dated_html
        )

    latest_html = _render_report_page(
        artifact,
        template_path=template_path,
        asset_version=asset_version,
        root_prefix="",
        markdown_path="index.md",
        canonical_url=PUBLIC_ROOT,
        relative_age=True,
    )
    (output_path / "index.html").write_text(latest_html)
    (output_path / "current-findings.json").write_text(
        json.dumps(_current_findings_manifest(artifact), indent=2, sort_keys=False)
        + "\n"
    )

    entries = [_archive_entry(archived) for archived in archived_artifacts]
    manifest = {"schema_version": 1, "reports": entries}
    (reports_path / "index.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=False) + "\n"
    )
    count = len(entries)
    count_label = f"{count} report{'s' if count != 1 else ''} available"
    if entries:
        oldest = min(archived.report_date for archived in archived_artifacts)
        archive_context = (
            "Reports accumulate through daily rollovers. Retained history begins "
            f"{_date_label(oldest)}."
        )
    else:
        archive_context = (
            "Reports accumulate through daily rollovers. Retained history begins "
            f"with the {_date_label(artifact.report_date)} report at the first date change."
        )
    archive_html = _template(
        template_path / "archive.html",
        {
            "ASSET_VERSION": asset_version,
            "REPORT_COUNT": count_label,
            "ARCHIVE_CONTEXT": archive_context,
            "ARCHIVE_ITEMS": _archive_items(entries),
            "THEME_BOOTSTRAP": theme_bootstrap.strip(),
            "ARCHIVE_IDENTITY_JSON": json.dumps(
                {
                    "@context": "https://schema.org",
                    "@type": "CollectionPage",
                    "name": "SentryInsight Report Archive",
                    "url": f"{PUBLIC_ROOT}reports/",
                    "description": "Dated SentryInsight exploitation intelligence reports.",
                    "author": {
                        "@type": "Person",
                        "name": "Michael Rico",
                        "url": "https://ricomanifesto.com/",
                    },
                },
                separators=(",", ":"),
            ).replace("</", "<\\/"),
        },
    )
    (reports_path / "index.html").write_text(archive_html)
    sitemap_urls = [
        PUBLIC_ROOT,
        f"{PUBLIC_ROOT}reports/",
        *(f"{PUBLIC_ROOT}reports/{entry['html_path']}" for entry in entries),
    ]
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(
            f"  <url><loc>{html.escape(url)}</loc></url>\n" for url in sitemap_urls
        )
        + "</urlset>\n"
    )
    (output_path / "sitemap.xml").write_text(sitemap)


def _generated_paths(root: Path) -> set[Path]:
    paths = {
        Path("index.html"),
        Path("current-findings.json"),
        Path("sitemap.xml"),
        Path("assets/site.css"),
        Path("assets/report.js"),
        Path("assets/vendor/dompurify.min.js"),
        Path("assets/vendor/DOMPURIFY-LICENSE.txt"),
        Path("reports/index.html"),
        Path("reports/index.json"),
    }
    reports_path = root / "reports"
    if reports_path.exists():
        paths.update(
            path.relative_to(root)
            for pattern in ("????-??-??.md", "????-??-??.html")
            for path in reports_path.glob(pattern)
        )
    return paths


def check_site(
    *, report_path: Path, output_path: Path, template_path: Path
) -> list[str]:
    """Return generated paths that are missing, stale, or unexpected."""
    with tempfile.TemporaryDirectory() as temp_dir:
        expected_root = Path(temp_dir) / "site"
        expected_reports = expected_root / "reports"
        expected_reports.mkdir(parents=True)
        current_reports = output_path / "reports"
        if current_reports.exists():
            for archived_path in current_reports.glob("????-??-??.md"):
                shutil.copy2(archived_path, expected_reports / archived_path.name)

        build_site(
            report_path=report_path,
            output_path=expected_root,
            template_path=template_path,
        )

        expected_paths = _generated_paths(expected_root)
        actual_paths = _generated_paths(output_path)
        differences: list[str] = []
        for relative_path in sorted(expected_paths | actual_paths):
            expected_path = expected_root / relative_path
            actual_path = output_path / relative_path
            if not expected_path.exists() or not actual_path.exists():
                differences.append(relative_path.as_posix())
                continue
            if expected_path.read_bytes() != actual_path.read_bytes():
                differences.append(relative_path.as_posix())
        return differences


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, default=Path("index.md"))
    parser.add_argument("--output", type=Path, default=Path("."))
    parser.add_argument("--templates", type=Path, default=Path("site"))
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        differences = check_site(
            report_path=args.report,
            output_path=args.output,
            template_path=args.templates,
        )
        if differences:
            print("Generated site is stale:")
            for difference in differences:
                print(f"- {difference}")
            return 1
        print("Generated site is current")
        return 0
    build_site(
        report_path=args.report,
        output_path=args.output,
        template_path=args.templates,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
