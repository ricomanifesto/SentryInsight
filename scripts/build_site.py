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

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from markdown_it import MarkdownIt
from markdown_it.token import Token

from src.core.report_artifact import (
    Finding,
    ReportArtifact,
    parse_report_artifact,
    slugify,
)

PUBLIC_ROOT = "https://ricomanifesto.github.io/SentryInsight/"
CVE_TEXT_PATTERN = re.compile(r"\bCVE-\d{4}-\d{4,}\b", re.IGNORECASE)


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


def _generated_label(value) -> str:
    utc_value = value.astimezone(timezone.utc)
    return f"{utc_value.strftime('%B')} {utc_value.day}, {utc_value.year} at {utc_value.strftime('%H:%M')} UTC"


def _strip_raw_html(tokens: list[Token]) -> None:
    for token in tokens:
        if token.type in {"html_inline", "html_block"}:
            token.content = ""
        if token.children:
            _strip_raw_html(token.children)


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


def _heading_entries(tokens: list[Token]) -> list[tuple[int, str, str]]:
    entries: list[tuple[int, str, str]] = []
    for index, token in enumerate(tokens):
        if token.type != "heading_open" or token.tag not in {"h2", "h3"}:
            continue
        inline = tokens[index + 1]
        title = inline.content.strip()
        entries.append((int(token.tag[1]), title, slugify(title)))
    return entries


def _render_markdown(
    artifact: ReportArtifact,
) -> tuple[str, list[tuple[int, str, str]]]:
    markdown = MarkdownIt("commonmark", {"html": True})
    tokens = markdown.parse(artifact.body)
    _strip_raw_html(tokens)
    _link_cves(tokens)

    findings = {finding.slug: finding for finding in artifact.findings}
    for index, token in enumerate(tokens):
        if token.type != "heading_open" or token.tag not in {"h1", "h2", "h3"}:
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

    rendered = markdown.renderer.render(tokens, markdown.options, {})
    lowered = rendered.casefold()
    forbidden = ("<script", "<iframe", "<object", "<embed", "onerror=", "onclick=")
    if any(value in lowered for value in forbidden) or re.search(
        r"href\s*=\s*['\"]\s*javascript:", rendered, re.IGNORECASE
    ):
        raise SiteBuildError("Rendered report contains active content")
    return rendered, _heading_entries(tokens)


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
    return value


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
) -> str:
    report_html, headings = _render_markdown(artifact)
    metadata = {
        "schema_version": artifact.schema_version,
        "report_date": artifact.report_date.isoformat(),
        "generated_at": _timestamp(artifact.generated_at),
        "findings": [_finding_json(finding) for finding in artifact.findings],
    }
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
            "REPORT_DATE_LABEL": _date_label(artifact.report_date),
            "GENERATED_AT_ISO": _timestamp(artifact.generated_at),
            "GENERATED_AT_LABEL": _generated_label(artifact.generated_at),
            "DESKTOP_TOC": toc,
            "MOBILE_TOC": toc,
            "REPORT_HTML": report_html,
            "REPORT_JSON": html.escape(
                json.dumps(metadata, separators=(",", ":")), quote=False
            ).replace("</", "<\\/"),
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
    return {
        "report_date": artifact.report_date.isoformat(),
        "generated_at": _timestamp(artifact.generated_at),
        "html_path": f"{artifact.report_date.isoformat()}.html",
        "markdown_path": f"{artifact.report_date.isoformat()}.md",
        "finding_count": len(artifact.findings),
        "cve_count": len(
            {cve for finding in artifact.findings for cve in finding.cve_ids}
        ),
    }


def _archive_items(entries: list[ArchiveEntry]) -> str:
    if not entries:
        return '<li class="archive-empty">No archived reports yet.</li>'
    items = []
    for entry in entries:
        report_date = str(entry["report_date"])
        findings = entry["finding_count"]
        cves = entry["cve_count"]
        items.append(
            "<li><article>"
            f'<h2><a href="{html.escape(str(entry["html_path"]))}">Report for {html.escape(report_date)}</a></h2>'
            f"<p>{findings} findings · {cves} complete CVE IDs</p>"
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
    dompurify = (template_path / "vendor" / "dompurify.min.js").read_text()
    dompurify_license = (template_path / "vendor" / "DOMPURIFY-LICENSE.txt").read_text()
    asset_version = hashlib.sha256((css + script + dompurify).encode()).hexdigest()[:12]
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
    )
    (output_path / "index.html").write_text(latest_html)

    entries = [_archive_entry(archived) for archived in archived_artifacts]
    manifest = {"schema_version": 1, "reports": entries}
    (reports_path / "index.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=False) + "\n"
    )
    count = len(entries)
    count_label = f"{count} report{'s' if count != 1 else ''} available"
    archive_html = _template(
        template_path / "archive.html",
        {
            "ASSET_VERSION": asset_version,
            "REPORT_COUNT": count_label,
            "ARCHIVE_ITEMS": _archive_items(entries),
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
