"""A reversible presentation boundary for source data that resembles markup."""

import re

from markdown_it import MarkdownIt


def source_literal(text: str) -> str:
    """Keep markup-like single-line source data literal in CommonMark.

    Call only on owned data, never on renderer-owned links, labels or syntax.
    Source records themselves remain unchanged. CommonMark removes exactly the
    added padding and preserves entities/backticks inside this code span.
    """
    if not re.search(r"[<>]|&(?:#\d+|#[xX][0-9a-fA-F]+|[A-Za-z][A-Za-z0-9]+);", text):
        return text
    if "\n" in text or "\r" in text:
        raise ValueError("Source literals require single-line presentation data")
    delimiter = "`" * (
        1 + max((len(run) for run in re.findall(r"`+", text)), default=0)
    )
    return f"{delimiter} {text} {delimiter}"


def source_literal_value(value: str) -> str:
    """Decode only an entire canonical literal, never arbitrary Markdown/HTML."""
    if not value.startswith("`"):
        return value
    children = MarkdownIt("commonmark").parseInline(value)[0].children or []
    if len(children) == 1 and children[0].type == "code_inline":
        text = children[0].content
        if source_literal(text) == value:
            return text
    return value
