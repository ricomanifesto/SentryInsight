"""Canonical article presentation shared by generation and source preflight."""

from typing import Any, Dict, Sequence

from .cve import extract_cve_ids
from .reporting import ReportingGroundingError, ReportingSource, reporting_key
from ..services.article_content import normalize_feed_content

UNKNOWN_SOURCE_SENTINELS = {"unknown source"}


def clean_article_source(value: Any) -> str:
    if value is None:
        return ""
    source = " ".join(str(value).split())
    if source.casefold() in UNKNOWN_SOURCE_SENTINELS:
        return ""
    return source


def format_article_summary(article: Dict[str, Any]) -> str:
    def clean_text(value: Any, default: str = "") -> str:
        if value is None:
            return default
        return str(value).strip()

    title = clean_text(article.get("title"), "Untitled article") or "Untitled article"
    source = clean_article_source(article.get("source"))
    link = clean_text(article.get("link"))
    content = (
        normalize_feed_content(article.get("content") or article.get("summary"))
        or "No content available"
    )

    metadata = []
    if source:
        metadata.append(f"Source: {source}")
    if link:
        metadata.append(f"URL: {link}")
        try:
            metadata.append(f"Reporting key: {reporting_key(link)}")
        except ReportingGroundingError:
            pass
    if article_cves := collect_structured_cves(article):
        metadata.append(f"CVEs: {', '.join(article_cves)}")

    heading = f"**{title}**"
    if metadata:
        heading = f"{heading} ({'; '.join(metadata)})"

    links = "\n".join(str(link) for link in article.get("source_links", []))
    return f"{heading}\nContent coverage: {article.get('content_kind', 'feed')}\n\n{content}\nSource links: {links or 'Not stated in supplied sources.'}\n\n"


def collect_structured_cves(article: Dict[str, Any]) -> list[str]:
    """Collect CVE IDs from structured article metadata."""
    cves: list[str] = []
    cves.extend(str(cve).strip() for cve in article.get("cves", []) if str(cve).strip())
    cves.extend(extract_cve_ids("\n".join(cves)))

    seen: set[str] = set()
    unique_cves: list[str] = []
    for cve in cves:
        normalized_cve = cve.upper()
        if normalized_cve in seen:
            continue
        seen.add(normalized_cve)
        unique_cves.append(normalized_cve)

    return unique_cves


def canonical_source_article(
    source: ReportingSource, cves: Sequence[str]
) -> dict[str, Any]:
    """Use the complete normalized source fields for both preflight and generation."""
    return {
        "title": source.title,
        "source": source.publisher,
        "link": source.url,
        "content": source.content,
        "content_kind": source.content_kind,
        "source_links": list(source.links),
        "cves": list(cves),
    }
