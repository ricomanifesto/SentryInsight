"""A reversible presentation boundary for source data that resembles markup."""

import re

from markdown_it import MarkdownIt

_COMMONMARK = MarkdownIt("commonmark")


def _plain_text(text: str) -> bool:
    # Standalone text tokens are insufficient: unmatched delimiters/references
    # may activate when composed with another quote or a citation. Reuse the
    # parser's own raw-text boundary instead of maintaining a syntax blacklist.
    if _COMMONMARK.inline.terminator_re.search(text):
        return False
    tokens = _COMMONMARK.parse(text)
    return (
        [token.type for token in tokens]
        == ["paragraph_open", "inline", "paragraph_close"]
        and tokens[1].content == text
        and [(child.type, child.content) for child in tokens[1].children or []]
        == [("text", text)]
    )


def source_literal(text: str) -> str:
    """Keep markup-like single-line source data literal in CommonMark.

    Call only on literal text/label data, never on complete renderer-owned syntax.
    Source records themselves remain unchanged. CommonMark removes exactly the
    added padding and preserves entities/backticks inside this code span.
    """
    if "\n" in text or "\r" in text:
        raise ValueError("Source literals require single-line presentation data")
    if not text.strip() or _plain_text(text):
        return text
    delimiter = "`" * (
        1 + max((len(run) for run in re.findall(r"`+", text)), default=0)
    )
    return f"{delimiter} {text} {delimiter}"


def source_literal_value(value: str) -> str:
    """Decode only an entire canonical literal, never arbitrary Markdown/HTML."""
    if not value.startswith("`"):
        return value
    children = _COMMONMARK.parseInline(value)[0].children or []
    if len(children) == 1 and children[0].type == "code_inline":
        text = children[0].content
        if source_literal(text) == value:
            return text
    return value
