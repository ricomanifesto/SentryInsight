"""Static article-owned text extraction; no rendered-page or whole-page fallback."""

from dataclasses import dataclass, field
from html.parser import HTMLParser
from typing import Any
from urllib.parse import urljoin, urlsplit


@dataclass
class _Node:
    tag: str
    attrs: dict[str, str]
    children: list[Any] = field(default_factory=list)


class _Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = _Node("root", {})
        self.stack = [self.root]
        self.nodes = []

    def handle_starttag(self, tag, attrs):
        node = _Node(tag, {key: value or "" for key, value in attrs})
        self.stack[-1].children.append(node)
        self.nodes.append(node)
        if tag not in {
            "area",
            "base",
            "br",
            "col",
            "embed",
            "hr",
            "img",
            "input",
            "link",
            "meta",
            "param",
            "source",
            "track",
            "wbr",
        }:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


@dataclass(frozen=True)
class ArticleContent:
    text: str
    links: tuple[str, ...] = ()


def _extract(node: _Node, url: str) -> ArticleContent:
    chunks: list[str] = []
    links: list[str] = []

    def visit(item):
        if isinstance(item, str):
            chunks.append(item)
            return
        if (
            item.tag
            in {
                "script",
                "style",
                "nav",
                "aside",
                "footer",
                "form",
                "noscript",
                "template",
            }
            or "hidden" in item.attrs
        ):
            return
        classes = item.attrs.get("class", "").casefold().split()
        if any(
            word
            in {"related", "related-posts", "social", "newsletter", "advertisement"}
            for word in classes
        ):
            return
        block = item.tag in {
            "p",
            "li",
            "div",
            "section",
            "article",
            "blockquote",
            "br",
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "h6",
            "tr",
        }
        if block:
            chunks.append("\n\n")
        if item.tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            chunks.append("#" * int(item.tag[1]) + " ")
        if item.tag == "a":
            target = urljoin(url, item.attrs.get("href", ""))
            parsed = urlsplit(target)
            if (
                parsed.scheme in {"http", "https"}
                and parsed.hostname
                and not parsed.username
                and not parsed.password
            ):
                links.append(target)
        for child in item.children:
            visit(child)
        if block:
            chunks.append("\n\n")

    visit(node)
    text = "\n\n".join(
        " ".join(part.split()) for part in "".join(chunks).split("\n\n") if part.strip()
    )
    return ArticleContent(text, tuple(dict.fromkeys(links)))


def extract_article_content(html: str, url: str) -> ArticleContent:
    document = _Document()
    document.feed(html)
    explicit = [
        node
        for node in document.nodes
        if node.attrs.get("id", "").casefold() == "articlebody"
        or "articlebody" in node.attrs.get("itemprop", "").casefold().split()
        or set(node.attrs.get("class", "").casefold().split())
        & {"articlebody", "article-body", "article-content"}
    ]
    candidates = explicit or [node for node in document.nodes if node.tag == "article"]
    return _extract(candidates[0], url) if candidates else ArticleContent("")


def normalize_feed_content(value: Any) -> str:
    if isinstance(value, list):
        return "\n\n".join(
            normalize_feed_content(
                item.get("value", "") if isinstance(item, dict) else item
            )
            for item in value
        )
    text = str(value or "")
    if "<" not in text:
        return text.strip()
    document = _Document()
    document.feed(text)
    return _extract(document.root, "").text
