"""Static article-owned text extraction; no rendered-page or whole-page fallback."""

from dataclasses import dataclass, field
import html5lib
import re
from typing import Any
from urllib.parse import urljoin, urlsplit

from .source_tables import normalize_around_tables, render_source_table, source_tables


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


def _excluded(item: _Node) -> bool:
    return (
        item.tag
        in {"script", "style", "nav", "aside", "footer", "form", "noscript", "template"}
        or "hidden" in item.attrs
        or bool(
            set(item.attrs.get("class", "").casefold().split())
            & {"related", "related-posts", "social", "newsletter", "advertisement"}
        )
    )


def _normalize_extracted_whitespace(text: str) -> str:
    return "\n\n".join(
        "\n".join(" ".join(line.split()) for line in part.splitlines() if line.strip())
        for part in re.split(r"\n[ \t]*\n", text)
        if part.strip()
    )


def _extract(node: _Node, url: str) -> ArticleContent:
    chunks: list[str] = []
    links: list[str] = []

    def visit(item, list_depth=0):
        if isinstance(item, str):
            chunks.append(re.sub(r"\s+", " ", item))
            return
        if _excluded(item):
            return
        if item.tag == "br":
            # List-item breaks cannot detach nested actions from their owner.
            # Outside lists, repeated breaks can separate prose paragraphs.
            chunks.append("\v" if list_depth else "\n")
            return
        if item.tag == "table":
            rows = []
            opaque = False

            def collect_rows(parent):
                nonlocal opaque
                if _excluded(parent):
                    return
                if parent.tag == "tr":
                    cells = [
                        child
                        for child in parent.children
                        if isinstance(child, _Node) and child.tag in {"td", "th"}
                    ]
                    if not rows and (
                        not cells or any(cell.tag != "th" for cell in cells)
                    ):
                        opaque = True
                    values = []
                    for cell in cells:
                        if any(
                            cell.attrs.get(name, "1") != "1"
                            for name in ("rowspan", "colspan")
                        ):
                            opaque = True

                        def nested_table(node):
                            return any(
                                isinstance(child, _Node)
                                and (child.tag == "table" or nested_table(child))
                                for child in node.children
                            )

                        opaque |= nested_table(cell)
                        extracted = _extract(cell, url)
                        values.append(extracted.text)
                        links.extend(extracted.links)
                    rows.append(values)
                    return
                for child in parent.children:
                    if not isinstance(child, _Node):
                        continue
                    if child.tag == "caption":
                        extracted = _extract(child, url)
                        chunks.extend(["\n\n", extracted.text, "\n\n"])
                        links.extend(extracted.links)
                    elif child.tag != "table":
                        collect_rows(child)

            collect_rows(item)
            if not rows:
                return
            opaque |= not rows or any(len(row) != len(rows[0]) for row in rows)
            chunks.extend(["\n\n", render_source_table(rows, opaque=opaque), "\n\n"])
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
    text = normalize_around_tables("".join(chunks), _normalize_extracted_whitespace)
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
    tables = source_tables(text)
    if tables:
        # Normalize surrounding input independently; a carrier never exempts
        # neighboring raw HTML from extraction or consumes its qualifications.
        return normalize_around_tables(text, normalize_feed_content)
    if not re.search(r"</?[A-Za-z][A-Za-z0-9:-]*(?:\s|/?>)", text):
        return text.strip()
    document = _Document(text, fragment=True)
    return _extract(document.root, "").text
