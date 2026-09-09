"""Exclude explicitly tagged promotions without rewriting source records."""

from collections.abc import Iterable, Mapping
import html
from html.parser import HTMLParser
import re
from typing import Any

from markdown_it import MarkdownIt

VIRTUAL_EVENT_PATTERN = re.compile(r"\[\s*virtual\s+event\s*\]", re.IGNORECASE)
MARKDOWN_PARSER = MarkdownIt("commonmark", {"html": True})
TEXT_BREAK_TAGS = {
    "article",
    "br",
    "div",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "li",
    "p",
    "section",
    "td",
    "th",
    "tr",
}


class _RenderedTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in TEXT_BREAK_TAGS:
            self.parts.append("\n")
        if tag == "img":
            self.parts.append(dict(attrs).get("alt") or "")

    def handle_endtag(self, tag: str) -> None:
        if tag in TEXT_BREAK_TAGS:
            self.parts.append("\n")


def contains_virtual_event_tag(text: str) -> bool:
    """Match the bracketed marker in source or rendered Markdown/HTML text."""
    decoded = html.unescape(text)
    # A second pass handles escaped Markdown preserved inside raw HTML blocks.
    for _ in range(2):
        if VIRTUAL_EVENT_PATTERN.search(decoded):
            return True
        parser = _RenderedTextParser()
        parser.feed(MARKDOWN_PARSER.render(decoded))
        parser.close()
        decoded = "".join(parser.parts)
    return bool(VIRTUAL_EVENT_PATTERN.search(decoded))


def _content_texts(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, Mapping):
        # feedparser content entries carry text in value, not type/base metadata.
        yield from _content_texts(value.get("value"))
    elif isinstance(value, (list, tuple)):
        for item in value:
            yield from _content_texts(item)


def is_virtual_event_promotion(article: Mapping[str, Any]) -> bool:
    return any(
        contains_virtual_event_tag(text)
        for field in (
            "title",
            "summary",
            "description",
            "content",
            "source",
            "dc_source",
        )
        for text in _content_texts(article.get(field))
    )


def exclude_virtual_event_promotions(
    articles: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Retain eligible records verbatim, including their identity and CVE metadata."""
    return [article for article in articles if not is_virtual_event_promotion(article)]
