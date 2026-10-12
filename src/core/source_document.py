"""Immutable source spans: structure and references precede semantic consumers.

All text remains retained. DOM ranges are checked against their exact source;
plain/feed sources only supply the structural boundaries they actually contain.
This module assigns no exploitation status, action or release interpretation.
"""

from dataclasses import dataclass, replace
from functools import lru_cache
import re
from typing import Any

from markdown_it import MarkdownIt

from ..services.article_content import ArticleBlock, article_blocks
from .cve import extract_cve_ids
from .reporting import validate_retained_content

ADVISORY_DECLARATION = re.compile(
    r"^(?P<vendor>[A-Z][A-Za-z-]*(?: [A-Z][A-Za-z-]*){0,3}) released security advisories for "
    r"(?P<count>\d+|one|two|three|four|five|six|seven|eight|nine|ten) "
    r"(?P<severity>critical|high|medium|low)(?:-severity)? vulnerabilities in its "
)


@dataclass(frozen=True)
class SourceSpan:
    start: int
    end: int
    text: str
    kind: str = "paragraph"
    role: str = "body"
    level: int = 0
    identities: tuple[str, ...] = ()
    section: tuple[str, ...] = ()
    reference: tuple[str, ...] = ()
    reference_kind: str = ""
    table: int | None = None
    cells: tuple[str, ...] = ()
    headers: tuple[str, ...] = ()
    headings: tuple[str, ...] = ()
    list_id: int | None = None
    reference_valid: bool = True
    product: str = ""
    constraint_text: str = ""
    reference_text: str = ""
    children: tuple[ArticleBlock, ...] = ()
    list_role: str = ""
    list_intro: str = ""
    list_members: tuple[str, ...] = ()
    list_items: tuple["SourceSpan", ...] = ()


@dataclass(frozen=True)
class SourceDocument:
    text: str
    spans: tuple[SourceSpan, ...]


@dataclass(frozen=True)
class ReportingEnvelope:
    source_text: str
    body: str
    subject: str
    finite: str
    adjunct: str = ""


def reporting_envelope(text: str) -> ReportingEnvelope | None:
    """A delimited quotation and a complete finite attribution own each other.

    Unknown reporting operators, prefixes and trailing clauses are not stripped.
    This operation assigns no assertion state or directive action.
    """
    subject = r"(?:the company|the vendor|it|(?:the )?[A-Z][A-Za-z0-9.'/-]*(?: (?:[A-Z][A-Za-z0-9.'/-]*|of|for|the|and|\([A-Z]+\))){0,16})"
    match = re.fullmatch(
        rf'["“](?P<body>[^"”]+)["”],? (?P<subject>{subject}) (?P<finite>said|says|added|warned)'
        r"(?P<adjunct> in its message to customers| on (?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday))?[.!?]*",
        text,
    )
    if match is None:
        match = re.fullmatch(
            rf'["“](?P<body>[^"”]+)["”],? (?P<finite>said|says|added|warned) (?P<subject>{subject})(?P<adjunct>)[.!?]*',
            text,
        )
        if match is None:
            return None
    return ReportingEnvelope(
        text,
        match["body"].rstrip(","),
        match["subject"],
        match["finite"],
        (match["adjunct"] or "").strip(),
    )


def _table_references(spans):
    """Resolve explicit product/row and marked-row references within a section.

    Aliases are exact contiguous token spans of table products. A sentence
    identifying another product starts a separate owned range; it never lends
    that product's conditions to its predecessor.
    """
    products = {}
    marked = set()
    result = []
    for span in spans:
        if span.kind == "heading":
            products, marked = {}, set()
        if span.role == "table_row" and span.identities:
            cells = dict(zip(span.headers, span.cells))
            product = cells.get("Product", "")
            if product:
                products.setdefault(product, set()).update(span.identities)
                if any("*" in cell and extract_cve_ids(cell) for cell in span.cells):
                    marked.update(span.identities)
            result.append(span)
            continue
        if span.role != "body" or not products:
            result.append(span)
            continue
        note = re.match(
            r"The advisory marks (\d+) of the (\d+) with an asterisk\b", span.text
        )
        if note:
            all_ids = set().union(*products.values())
            result.append(
                replace(
                    span,
                    reference=tuple(sorted(marked)),
                    reference_kind="table_note",
                    reference_valid=len(marked) == int(note[1])
                    and len(all_ids) == int(note[2]),
                    constraint_text=span.text,
                )
            )
            continue
        aliases = {}
        for product, identities in products.items():
            words = product.split()
            for alias in {
                " ".join(words[start:stop])
                for start in range(len(words))
                for stop in range(start + 1, len(words) + 1)
            }:
                aliases.setdefault(alias, set()).update(identities)
        pattern = re.compile(
            r"(?:The |the )?(?P<product>"
            + "|".join(re.escape(a) for a in sorted(aliases, key=len, reverse=True))
            + r")(?=(?:'s|’s) own advisory\b| flaw\b)"
        )
        references = list(pattern.finditer(span.text))
        if not references:
            result.append(span)
            continue
        for index, reference in enumerate(references):
            start = reference.start()
            stop = (
                references[index + 1].start()
                if index + 1 < len(references)
                else len(span.text)
            )
            text = span.text[start:stop].strip()
            identities = tuple(sorted(aliases[reference["product"]]))
            product = next(
                (p for p, ids in products.items() if set(identities) == ids),
                reference["product"],
            )
            result.append(
                replace(
                    span,
                    start=span.start + start,
                    end=span.start + start + len(text),
                    text=text,
                    reference=identities,
                    reference_kind="table_product",
                    reference_valid=len(identities) == 1,
                    product=product,
                    constraint_text=text,
                )
            )
        if references[0].start():
            prefix = span.text[: references[0].start()].strip()
            result.insert(
                len(result) - len(references),
                replace(
                    span, end=span.start + len(prefix), text=prefix, role="context"
                ),
            )
    return tuple(result)


def _text_blocks(text: str):
    """Markdown maps preserve physical version rows inside logical paragraphs."""
    lines = text.splitlines(keepends=True)
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))
    depth = 0
    end = 0
    for token in MarkdownIt("commonmark").parse(text):
        if token.type == "list_item_close":
            depth -= 1
        owns = (
            token.type in {"paragraph_open", "heading_open", "fence", "code_block"}
            and not depth
        )
        if token.type == "list_item_open":
            owns = not depth
            depth += 1
        if not owns or not token.map:
            continue
        start, stop = (offsets[index] for index in token.map)
        if start < end:
            continue
        raw = text[start:stop]
        leading = len(raw) - len(raw.lstrip())
        start += leading
        stop = start + len(raw.strip())
        heading = token.type == "heading_open"
        yield SourceSpan(
            start,
            stop,
            text[start:stop],
            "heading" if heading else "list_item" if depth else "paragraph",
            "heading" if heading else "body",
            int(token.tag[1]) if heading else 0,
        )
        end = stop


def _spans(text: str, blocks: tuple[ArticleBlock, ...]):
    if not blocks:
        yield from _text_blocks(text)
        return
    cursor = 0
    for block in article_blocks(blocks, text):
        if text[cursor : block.start].strip():
            for gap in _text_blocks(text[cursor : block.start]):
                yield replace(gap, start=gap.start + cursor, end=gap.end + cursor)
        yield SourceSpan(
            block.start,
            block.end,
            block.text,
            block.kind,
            (
                "heading"
                if block.kind == "heading"
                else "context" if block.kind in {"caption", "context"} else "body"
            ),
            block.level,
            table=block.table,
            cells=block.cells,
            headers=block.cells if block.header else (),
            list_id=block.list_id,
            children=block.children,
        )
        cursor = block.end
    for gap in _text_blocks(text[cursor:]):
        yield replace(gap, start=gap.start + cursor, end=gap.end + cursor)


def _list_relations(spans, text):
    """Actual adjacent DOM lists bind a finite introduction and its members.

    These are source boundaries only. Version and recommendation consumers
    must still parse every identity, target and qualifier under their owner.
    """
    result = []
    index = 0
    while index < len(spans):
        span = spans[index]
        role = ""
        if span.role == "body":
            if re.search(
                r"\b(?:advised|urged) (?:customers|users|IT administrators) (?:not )?to upgrade .+ to:$",
                span.text,
            ):
                role = "destination"
            elif re.fullmatch(
                r"The (?:issue|vulnerability) impacts the following versions [-:]",
                span.text,
            ):
                role = "affected"
            elif re.fullmatch(
                r"The (?:shortcoming|issue|vulnerability) has been addressed in the versions below [-:]",
                span.text,
            ):
                role = "fixed"
            elif re.fullmatch(
                r"[A-Z][A-Za-z0-9-]*(?: [A-Z][A-Za-z0-9-]*)* shared the following detailed guidance on the required actions by [A-Z][A-Za-z0-9-]* version:",
                span.text,
            ):
                role = "audience"
        members = []
        next_index = index + 1
        while role and next_index < len(spans):
            candidate = spans[next_index]
            if (
                candidate.kind != "list_item"
                or candidate.list_id is None
                or members
                and candidate.list_id != members[0].list_id
            ):
                break
            members.append(candidate)
            next_index += 1
        if members:
            if role in {"destination", "affected", "fixed"}:
                result.append(
                    replace(
                        span,
                        end=members[-1].end,
                        text=text[span.start : members[-1].end],
                        list_role=role,
                        list_intro=span.text,
                        list_members=tuple(m.text for m in members),
                        list_items=tuple(members),
                    )
                )
            else:
                result.append(span)
                result.extend(
                    replace(m, list_role=role, list_intro=span.text) for m in members
                )
            index = next_index
        else:
            result.append(span)
            index += 1
    return tuple(result)


@lru_cache(maxsize=128)
def _document(text: str, blocks: tuple[ArticleBlock, ...]) -> SourceDocument:
    result = []
    sections: list[tuple[int, tuple[str, ...], str, str]] = []
    tables = {}
    antecedent: tuple[str, ...] = ()
    spans = _list_relations(tuple(_spans(text, blocks)), text)
    group: tuple[str, ...] = ()
    group_valid = True
    topic: tuple[str, ...] = ()
    declared_groups: set[tuple[str, ...]] = set()
    for index, span in enumerate(spans):
        identities = tuple(
            extract_cve_ids(" ".join(span.cells) if span.cells else span.text)
        )
        role = span.role
        if span.kind == "heading":
            while sections and sections[-1][0] >= span.level:
                sections.pop()
            title = re.sub(r"^#+\s*", "", span.text).strip(" :").casefold()
            inherited = sections[-1][1] if sections else ()
            role = (
                "navigation"
                if title in {"related articles", "related stories", "related posts"}
                else "heading"
            )
            sections.append(
                (
                    span.level,
                    identities or inherited,
                    role,
                    re.sub(r"^#+\s*", "", span.text),
                )
            )
            antecedent = identities or inherited
            group = ()
            group_valid = True
            topic = ()
        section = sections[-1][1] if sections else ()
        if any(item[2] == "navigation" for item in sections):
            role = "navigation"
        headers = span.headers
        if span.table is not None:
            if headers:
                tables[span.table] = headers
                role = "table_header"
            else:
                headers = tables.get(span.table, ())
                # A missing header remains unknown structure. Never fabricate
                # affected/fixed roles from a row's numeric values.
                role = "table_row"
        reference = ()
        reference_kind = ""
        reference_valid = True
        reference_text = ""
        # A declared cardinality plus actual adjacent list/table supplies a
        # closed group. Co-mentions elsewhere in an article never do.
        declared = re.search(
            r"\b(?:[Aa]ll|lists) (?P<count>\d+|one|two|three|four|five|six|seven|eight|nine|ten) (?:known )?(?:vulnerabilities|flaws)\b",
            span.text,
        )
        if declared and role == "body":
            numbers = dict(
                zip(
                    (
                        "one",
                        "two",
                        "three",
                        "four",
                        "five",
                        "six",
                        "seven",
                        "eight",
                        "nine",
                        "ten",
                    ),
                    range(1, 11),
                )
            )
            count = numbers.get(
                declared["count"],
                int(declared["count"]) if declared["count"].isdigit() else 0,
            )
            following = spans[index + 1 :]
            members = []
            container = None
            for candidate in following:
                if candidate.kind == "heading":
                    break
                if candidate.kind in {"list_item", "table_row"}:
                    identity = (
                        candidate.kind,
                        (
                            candidate.table
                            if candidate.kind == "table_row"
                            else candidate.list_id
                        ),
                    )
                    if container is None:
                        container = identity
                    if identity != container:
                        break
                    members.extend(
                        extract_cve_ids(
                            " ".join(candidate.cells)
                            if candidate.cells
                            else candidate.text
                        )
                    )
                elif container is not None:
                    break
                elif not re.search(
                    r"\b(?:table|flaws|versions)\b", candidate.text, re.I
                ):
                    break
            if members:
                declared_group = tuple(dict.fromkeys(members))
                declared_valid = len(declared_group) == count
                reference, reference_kind, reference_valid = (
                    declared_group,
                    "declared_group",
                    declared_valid,
                )
                if declared_valid:
                    declared_groups.add(tuple(sorted(declared_group)))
                if container and container[0] != "table_row":
                    group, group_valid = declared_group, declared_valid
            elif group:
                reference, reference_kind, reference_valid = (
                    group,
                    "group",
                    group_valid and len(group) == count,
                )
            elif antecedent:
                reference, reference_kind, reference_valid = (
                    antecedent,
                    "group",
                    len(antecedent) == count,
                )
        listed = re.search(
            r"\bthe (?P<count>\d+|one|two|three|four|five|six|seven|eight|nine|ten) (?:flaws|vulnerabilities) listed (?P<direction>above|below)\b",
            span.text,
        )
        if listed and role == "body":
            counts = dict(
                zip(
                    (
                        "one",
                        "two",
                        "three",
                        "four",
                        "five",
                        "six",
                        "seven",
                        "eight",
                        "nine",
                        "ten",
                    ),
                    range(1, 11),
                )
            )
            count = (
                int(listed["count"])
                if listed["count"].isdigit()
                else counts[listed["count"]]
            )
            matching = [ids for ids in declared_groups if len(ids) == count]
            reference = tuple(sorted(set().union(*(matching or declared_groups))))
            reference_kind = "listed_group"
            reference_text = listed.group()
            reference_valid = len(matching) == 1 and listed["direction"] == "above"
        if role == "table_row":
            reference = identities or tuple(extract_cve_ids(" ".join(headers)))
            reference_kind = "table_row" if reference else ""
        if (
            role == "body"
            and not identities
            and re.search(
                r"\b(?:The|This|the|this) (?:issue|flaw|vulnerability)\b", span.text
            )
        ):
            reference, reference_kind, reference_valid = (
                antecedent,
                "singular",
                len(antecedent) == 1,
            )
        if identities and role in {"body", "table_row"}:
            antecedent = identities
        if role == "body" and identities:
            # A local identity declaration owns its subsequent detail topic.
            # Table rows and incidental multi-identity comparisons cannot seed
            # a last-row/article-wide topic. Assertions still require explicit
            # subjects or typed reference edges, independently of this topic.
            identity = re.escape(next(iter(identities)))
            declaration = re.match(
                rf'^["“]?(?:(?:Tracked as |The (?:first|second|third) pattern is exploitation of ){identity}\b|{identity} is an? (?:[A-Za-z][\w-]* ){{0,4}}(?:flaw|vulnerability)\b)',
                span.text,
                re.I,
            )
            if len(identities) == 1 and declaration:
                topic = identities
                if sections:
                    level, _, section_role, title = sections[-1]
                    sections[-1] = (level, identities, section_role, title)
            elif topic and not set(identities) <= set(topic):
                topic = ()
        # A declared local group owns its following context until an explicit
        # new identity/section. The reference itself remains separately typed.
        if group and identities and not set(identities) <= set(group):
            group = ()
        result.append(
            replace(
                span,
                role=role,
                identities=identities,
                section=section or group or topic,
                reference=reference,
                reference_kind=reference_kind,
                reference_valid=reference_valid,
                reference_text=reference_text,
                headers=headers,
                headings=tuple(item[3] for item in sections),
            )
        )
    return SourceDocument(text, _forward_declared_contexts(_table_references(result)))


def _forward_declared_contexts(spans):
    """Resolve an advisory set declaration to its unique complete local list.

    Cardinality is meaningful only with an explicit declaration and actual
    list provenance. Boundaries/foreign identities end the forward search;
    ambiguity cannot become article-wide severity or event ownership.
    """
    result = []
    numbers = dict(
        zip(
            (
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
                "ten",
            ),
            range(1, 11),
        )
    )
    for index, span in enumerate(spans):
        declaration = (
            ADVISORY_DECLARATION.match(span.text) if span.role == "body" else None
        )
        if declaration:
            count = (
                int(declaration["count"])
                if declaration["count"].isdigit()
                else numbers[declaration["count"]]
            )
            groups = set()
            for candidate in spans[index + 1 :]:
                if candidate.kind == "heading" or candidate.role not in {
                    "body",
                    "table_row",
                    "table_header",
                }:
                    break
                if (
                    candidate.reference_kind == "declared_group"
                    and candidate.reference_valid
                ):
                    groups.add(tuple(sorted(candidate.reference)))
                owned = {cve for group in groups for cve in group}
                if candidate.identities and not set(candidate.identities) <= owned:
                    break
            matching = {group for group in groups if len(group) == count}
            if matching:
                span = replace(
                    span,
                    reference=tuple(
                        sorted({cve for group in matching for cve in group})
                    ),
                    reference_kind="forward_declared_group",
                    reference_valid=len(matching) == 1,
                )
        result.append(span)
    return tuple(result)


def source_document(source: Any) -> SourceDocument:
    content = source.get("content", "") if isinstance(source, dict) else source.content
    blocks = (
        source.get("blocks", ())
        if isinstance(source, dict)
        else getattr(source, "blocks", ())
    )
    retained = validate_retained_content(content, blocks)
    return _document(retained.text, retained.blocks)
