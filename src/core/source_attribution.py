"""Source attribution helpers for generated reports."""

from typing import Any, Dict

UNKNOWN_SOURCE_SENTINELS = {"unknown source"}
MARKDOWN_TEXT_ESCAPE_CHARACTERS = frozenset(r"\*_[]<>`&~")


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


def escape_markdown_text(value: str) -> str:
    return "".join(
        f"\\{character}" if character in MARKDOWN_TEXT_ESCAPE_CHARACTERS else character
        for character in value
    )


def collect_source_attribution_entries(articles: list[Dict[str, Any]]) -> list[str]:
    entries: list[str] = []
    seen_entries: set[str] = set()
    for article in articles:
        title = clean_article_text(article.get("title"), "Untitled article")
        title = title or "Untitled article"
        source = clean_article_source(article.get("source"))
        link = clean_article_link(article.get("link"))
        title_text = escape_markdown_text(title)
        source_text = escape_markdown_text(source)

        if link and source:
            entry = f"- **{title_text}**: {source_text} - {link}"
        elif link:
            entry = f"- **{title_text}**: {link}"
        elif source:
            entry = f"- **{title_text}**: {source_text}"
        else:
            continue

        if entry not in seen_entries:
            entries.append(entry)
            seen_entries.add(entry)

    return entries
