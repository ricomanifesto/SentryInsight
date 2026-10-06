"""Static article-owned text extraction; no rendered-page or whole-page fallback."""

from dataclasses import dataclass, field
import html5lib
import re
from typing import Any
from urllib.parse import urljoin, urlsplit


@dataclass
class _Node:
    tag: str
    attrs: dict[str, str]
    children: list[Any] = field(default_factory=list)


class _Document:
    def __init__(self, html: str, *, fragment: bool = False):
        parse = html5lib.parseFragment if fragment else html5lib.parse
        tree = parse(html, treebuilder="etree", namespaceHTMLElements=False)
        self.nodes = []
        self.root = self._from_element(tree)

    def _from_element(self, element):
        node = _Node(element.tag.rsplit("}", 1)[-1], dict(element.attrib))
        self.nodes.append(node)
        if element.text:
            node.children.append(element.text)
        for child in element:
            if isinstance(child.tag, str):
                node.children.append(self._from_element(child))
            if child.tail:
                node.children.append(child.tail)
        return node


@dataclass(frozen=True)
class ArticleContent:
    text: str
    links: tuple[str, ...] = ()


def _extract(node: _Node, url: str) -> ArticleContent:
    chunks: list[str] = []
    links: list[str] = []

    def visit(item, list_depth=0):
        if isinstance(item, str):
            chunks.append(re.sub(r"\s+", " ", item))
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
        if item.tag == "br":
            # List-item breaks cannot detach nested actions from their owner.
            # Outside lists, repeated breaks can separate prose paragraphs.
            chunks.append("\v" if list_depth else "\n")
            return
        block = item.tag in {
            "p",
            "li",
            "div",
            "section",
            "article",
            "blockquote",
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "h6",
            "tr",
        }
        separator = " " if list_depth else "\n\n"
        if block:
            chunks.append(separator)
        if not list_depth and item.tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
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
        child_depth = list_depth + (item.tag == "li")
        seen_item = False
        for child in item.children:
            if (
                child_depth
                and item.tag in {"ul", "ol"}
                and isinstance(child, _Node)
                and child.tag == "li"
            ):
                if seen_item:
                    while chunks and not chunks[-1].strip():
                        chunks.pop()
                    if chunks:
                        chunks[-1] = chunks[-1].rstrip()
                    chunks.append("; ")
                seen_item = True
            visit(child, child_depth)
        if block:
            chunks.append(separator)

    visit(node)
    text = "\n\n".join(
        "\n".join(" ".join(line.split()) for line in part.splitlines() if line.strip())
        for part in re.split(r"\n[ \t]*\n", "".join(chunks))
        if part.strip()
    )
    return ArticleContent(text, tuple(dict.fromkeys(links)))


def extract_article_content(html: str, url: str) -> ArticleContent:
    document = _Document(html)
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
    document = _Document(text, fragment=True)
    return _extract(document.root, "").text
