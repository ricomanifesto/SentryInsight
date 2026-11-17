"""A canonical, source-hashed carrier for complete HTML table cells.

The carrier is presentation data, never instructions. Encoding keeps each cell
on one physical line; decoding happens once, before cell-local evidence parsing.
Unsupported layouts retain their content but cannot establish row ownership.
"""

from dataclasses import dataclass
import html
import re
from typing import Callable, Sequence

TABLE_START = "```retained-table-v1"
TABLE_END = "```"
_LINE_BREAKS = "\r\n\v\f\x1c\x1d\x1e\x85\u2028\u2029"


def encode_cell(value: str) -> str:
    value = value.replace("&", "&amp;")
    return "".join(
        f"&#{ord(char)};" if char in "<>|`" + _LINE_BREAKS else char for char in value
    )


def _row(cells: Sequence[str]) -> str:
    return "| " + " | ".join(encode_cell(cell) for cell in cells) + " |"


def render_source_table(rows: Sequence[Sequence[str]], *, opaque: bool) -> str:
    if not rows:
        return TABLE_START + " opaque\n" + TABLE_END
    lines = [TABLE_START + (" opaque" if opaque else ""), _row(rows[0])]
    lines.append("| " + " | ".join("---" for _ in rows[0]) + " |")
    lines.extend(_row(row) for row in rows[1:])
    return "\n".join([*lines, TABLE_END])


@dataclass(frozen=True)
class SourceTable:
    start: int
    end: int
    rows: tuple[tuple[str, ...], ...]
    opaque: bool


def source_tables(content: str) -> tuple[SourceTable, ...]:
    """Retain malformed/truncated carriers too, without granting them scope."""
    lines = content.splitlines()
    tables = []
    index = 0
    while index < len(lines):
        opening = lines[index]
        if not opening.lstrip().startswith(TABLE_START):
            index += 1
            continue
        start = index
        index += 1
        while index < len(lines) and lines[index] != TABLE_END:
            index += 1
        closed = index < len(lines)
        end = index + 1 if closed else index
        body = lines[start + 1 : index]
        rows: list[tuple[str, ...]] = (
            [] if opening in {TABLE_START, TABLE_START + " opaque"} else [(opening,)]
        )
        valid = closed and opening == TABLE_START
        for row_index, line in enumerate(body):
            if row_index == 1 and re.fullmatch(r"\| (?:--- \| ?)+", line):
                continue
            if not line.startswith("| ") or not line.endswith(" |"):
                valid = False
                rows.append((line,))
                continue
            encoded = line[2:-2].split(" | ")
            cells = tuple(html.unescape(cell) for cell in encoded)
            valid &= _row(cells) == line
            rows.append(cells)
        valid &= bool(
            len(body) >= 3
            and len(rows) >= 2
            and len(rows[0]) >= 2
            and body[1] == "| " + " | ".join("---" for _ in rows[0]) + " |"
            and all(len(row) == len(rows[0]) for row in rows)
        )
        tables.append(SourceTable(start, end, tuple(rows), not valid))
        index = end
    return tuple(tables)


def normalize_around_tables(content: str, normalize: Callable[[str], str]) -> str:
    """Normalize prose independently without modifying encoded cell columns."""
    tables = source_tables(content)
    if not tables:
        return normalize(content)
    lines = content.splitlines()
    parts = []
    start = 0
    for table in tables:
        before = "\n".join(lines[start : table.start])
        if before.strip():
            parts.append(normalize(before))
        parts.append("\n".join(lines[table.start : table.end]))
        start = table.end
    after = "\n".join(lines[start:])
    if after.strip():
        parts.append(normalize(after))
    return "\n\n".join(parts).strip()
