"""Static article-owned text extraction; no rendered-page or whole-page fallback."""

from dataclasses import dataclass, field
import hashlib
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
class ArticleLink:
    url: str
    label: str
    context: str


@dataclass(frozen=True)
class ArticleBlock:
    """An exact range in extracted text, with structure owned by the HTML DOM."""

    start: int
    end: int
    text: str
    text_sha256: str
    kind: str
    level: int = 0
    table: int | None = None
    cells: tuple[str, ...] = ()
    header: bool = False
    list_id: int | None = None
    children: tuple["ArticleBlock", ...] = ()


@dataclass(frozen=True)
class ArticleContent:
    text: str
    links: tuple[str, ...] = ()
    link_contexts: tuple[ArticleLink, ...] = ()
    blocks: tuple[ArticleBlock, ...] = ()


def _excluded(node: _Node) -> bool:
    return (
        node.tag
        in {"script", "style", "nav", "aside", "footer", "form", "noscript", "template"}
        or "hidden" in node.attrs
        or bool(
            set(node.attrs.get("class", "").casefold().split())
            & {"related", "related-posts", "social", "newsletter", "advertisement"}
        )
    )


def article_blocks(records, text: str) -> tuple[ArticleBlock, ...]:
    """Reject stale or inconsistent provenance at both catalog boundaries."""
    digest = hashlib.sha256(text.encode()).hexdigest()
    blocks = []
    end = 0
    for value in records:
        if isinstance(value, ArticleBlock):
            block = value
        else:
            fields: dict[str, Any] = {
                **value,
                "cells": tuple(value.get("cells", ())),
                "children": article_blocks(value.get("children", ()), text),
            }
            block = ArticleBlock(**fields)
        if (
            block.text_sha256 != digest
            or not 0 <= end <= block.start < block.end <= len(text)
            or text[block.start : block.end] != block.text
            or block.kind
            not in {
                "paragraph",
                "list_item",
                "quotation",
                "heading",
                "table_row",
                "caption",
                "context",
            }
            or (block.kind == "heading") != (block.level in range(1, 7))
            or (block.kind == "table_row") != (block.table is not None)
            or (block.kind != "table_row" and (block.cells or block.header))
        ):
            raise ValueError("Article structure does not match retained source text")
        if block.cells:
            # DOM cell boundaries can occur without whitespace in the original
            # extraction. They may only partition the existing row, never add
            # names, release values or column labels.
            if re.sub(r"\s", "", "".join(block.cells)) != re.sub(r"\s", "", block.text):
                raise ValueError("Article table cells do not match their source row")
        if block.children:
            children = article_blocks(block.children, text)
            if block.kind != "list_item" or any(
                child.kind != "list_item"
                or not block.start <= child.start < child.end <= block.end
                for child in children
            ):
                raise ValueError(
                    "Article list children do not belong to their source item"
                )
        blocks.append(block)
        end = block.end
    return tuple(blocks)


def _dom_blocks(node: _Node, text: str, url: str) -> tuple[ArticleBlock, ...]:
    """Capture atomic DOM blocks without reformatting the retained text."""
    cursor = 0
    table_index = -1
    list_index = -1
    result = []
    digest = hashlib.sha256(text.encode()).hexdigest()

    def heading_level(item):
        if item.tag in {f"h{n}" for n in range(1, 7)}:
            return int(item.tag[1])
        if item.attrs.get("role") == "heading" and item.attrs.get("aria-level") in {
            str(n) for n in range(1, 7)
        }:
            return int(item.attrs["aria-level"])
        return 0

    def contains_heading(item):
        return any(
            isinstance(child, _Node)
            and (heading_level(child) or contains_heading(child))
            for child in item.children
        )

    def nested_items(item, start, stop):
        """Direct nested list members retain exact ranges inside their parent."""
        members = []
        position = start
        for child in item.children:
            if not isinstance(child, _Node) or child.tag not in {"ul", "ol"}:
                continue
            for member in child.children:
                if not isinstance(member, _Node) or member.tag != "li":
                    continue
                value = _extract(member, url, collect_links=False).text
                offset = text.find(value, position, stop) if value else -1
                if offset < 0:
                    raise ValueError("Nested list range does not match retained source")
                end = offset + len(value)
                members.append(
                    ArticleBlock(
                        offset,
                        end,
                        value,
                        digest,
                        "list_item",
                        children=nested_items(member, offset, end),
                    )
                )
                position = end
        return tuple(members)

    def visit(item, table=None, list_id=None):
        nonlocal cursor, table_index, list_index
        if isinstance(item, str) or _excluded(item):
            return
        if item.tag == "table":
            table_index += 1
            table = table_index
        if item.tag in {"ul", "ol"}:
            list_index += 1
            list_id = list_index
        kind = {
            "p": "paragraph",
            "li": "list_item",
            "blockquote": "quotation",
            "tr": "table_row",
            "figcaption": "caption",
            **{f"h{n}": "heading" for n in range(1, 7)},
        }.get(item.tag)
        if heading_level(item):
            kind = "heading"
        if kind == "list_item" and contains_heading(item):
            # A story container is not one indivisible factual sentence.
            # Preserve the pre-heading furniture as context while retaining
            # actual heading/body child ranges without changing extracted text.
            first = len(result)
            for child in item.children:
                visit(child, table, list_id)
            if len(result) > first:
                initial = result[first]
                value = _extract(item, url, collect_links=False).text
                start = text.rfind(value, 0, initial.end + len(value)) if value else -1
                if start >= 0 and text[start : initial.start].strip():
                    prefix = text[start : initial.start].strip()
                    prefix_start = (
                        start
                        + len(text[start : initial.start])
                        - len(text[start : initial.start].lstrip())
                    )
                    result.insert(
                        first,
                        ArticleBlock(
                            prefix_start,
                            prefix_start + len(prefix),
                            prefix,
                            digest,
                            "context",
                            list_id=list_id,
                        ),
                    )
            return
        if kind:
            value = _extract(item, url, collect_links=False).text
            start = text.find(value, cursor) if value else -1
            if start >= 0:
                cells = tuple(
                    _extract(child, url, collect_links=False).text
                    for child in item.children
                    if isinstance(child, _Node) and child.tag in {"td", "th"}
                )
                result.append(
                    ArticleBlock(
                        start,
                        start + len(value),
                        value,
                        digest,
                        kind,
                        heading_level(item) if kind == "heading" else 0,
                        table if kind == "table_row" else None,
                        cells if kind == "table_row" else (),
                        kind == "table_row"
                        and bool(cells)
                        and all(
                            child.tag == "th" and child.attrs.get("scope") != "row"
                            for child in item.children
                            if isinstance(child, _Node) and child.tag in {"td", "th"}
                        ),
                        list_id,
                        (
                            nested_items(item, start, start + len(value))
                            if kind == "list_item"
                            else ()
                        ),
                    )
                )
                cursor = start + len(value)
                return
        for child in item.children:
            visit(child, table, list_id)

    visit(node)
    return article_blocks(result, text)


def _extract(node: _Node, url: str, *, collect_links: bool = True) -> ArticleContent:
    chunks: list[str] = []
    links: list[str] = []
    link_contexts: list[ArticleLink] = []

    def visit(item, list_depth=0, context=None):
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
        if item.tag in {"p", "li", "tr"} and not list_depth:
            context = item
        if item.tag == "a" and collect_links:
            target = urljoin(url, item.attrs.get("href", ""))
            parsed = urlsplit(target)
            if (
                parsed.scheme in {"http", "https"}
                and parsed.hostname
                and not parsed.username
                and not parsed.password
            ):
                links.append(target)
                if context is not None:
                    link_contexts.append(
                        ArticleLink(
                            target,
                            _extract(item, url, collect_links=False).text,
                            _extract(context, url, collect_links=False).text,
                        )
                    )
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
            visit(child, child_depth, context)
        if block:
            chunks.append(separator)

    visit(node)
    text = "\n\n".join(
        "\n".join(" ".join(line.split()) for line in part.splitlines() if line.strip())
        for part in re.split(r"\n[ \t]*\n", "".join(chunks))
        if part.strip()
    )
    return ArticleContent(
        text, tuple(dict.fromkeys(links)), tuple(dict.fromkeys(link_contexts))
    )


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
    if not candidates:
        return ArticleContent("")
    result = _extract(candidates[0], url)
    return ArticleContent(
        result.text,
        result.links,
        result.link_contexts,
        _dom_blocks(candidates[0], result.text, url),
    )


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
