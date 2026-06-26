"""Source attribution helpers for generated reports."""

from typing import Any, Dict

UNKNOWN_SOURCE_SENTINELS = {"unknown source"}


def clean_article_text(value: Any, default: str = "") -> str:
    if value is None:
        return default
    return " ".join(str(value).split())


def clean_article_source(value: Any) -> str:
    source = clean_article_text(value)
    if source.casefold() in UNKNOWN_SOURCE_SENTINELS:
        return ""
    return source


def clean_article_link(value: Any) -> str:
    if value is None:
        return ""
    return "".join(str(value).split())


def collect_source_attribution_entries(articles: list[Dict[str, Any]]) -> list[str]:
    entries: list[str] = []
    for article in articles:
        title = clean_article_text(article.get("title"), "Untitled article")
        title = title or "Untitled article"
        source = clean_article_source(article.get("source"))
        link = clean_article_link(article.get("link"))

        if link and source:
            entries.append(f"- **{title}**: {source} - {link}")
        elif link:
            entries.append(f"- **{title}**: {link}")
        elif source:
            entries.append(f"- **{title}**: {source}")

    return entries
