"""Conservative report-local coverage, independent of source grounding."""

from dataclasses import dataclass, field
import re

from markdown_it import MarkdownIt

from .heading_identity import normalize_heading_identity
from .reporting import normalize_reporting_url, ReportingGroundingError
from .source_markup import source_literal, source_literal_value

_PARSER = MarkdownIt("commonmark")
THREAT_ACTIVITY_MARKER_PATTERN = re.compile(
    r"\b(?:campaigns?|threat actors?)\b", re.IGNORECASE
)
_ITEM = re.compile(r" {0,3}- \*\*([^*\n]+)\*\*: (.+)")
_SOURCE = re.compile(r"\[Source\]\((?:<[^<>\n]+>|[^()\n]+)\): “")
_ACTIVE = "Active Exploitation Details"
_ACTORS = "Threat Actor Activities"
_ROLLUPS = {"Affected Systems and Products", "Attack Vectors and Techniques", _ACTORS}
_LITERAL_FIELDS = {
    "Description",
    "Impact",
    "Status",
    "Affected Versions",
    "Exceptions",
    "Recommended Actions",
    "Release Details",
    "Action Context",
    "Attribution Context",
}
_QUOTED_FIELDS = {"Source Evidence", "Source Constraints", "Severity Context"}


@dataclass
class _Finding:
    fields: dict[str, tuple[str, int]] = field(default_factory=dict)
    atoms: set[str] = field(default_factory=set)
    required: set[str] = field(default_factory=set)
    covered: set[str] = field(default_factory=set)


def _literal(value: str) -> str | None:
    if not value.startswith("`"):
        children = _PARSER.parseInline(value)[0].children or []
        # Literal plain text needs no decoding. Any interpreted markup,
        # escaped punctuation or entity substitution remains unproven.
        return (
            value
            if [(t.type, t.content) for t in children] == [("text", value)]
            else None
        )
    decoded = source_literal_value(value)
    return decoded if source_literal(decoded) == value else None


def _links(value: str) -> set[str] | None:
    """Only explicit inline links and comma separators establish report identity."""
    children = _PARSER.parseInline(value)[0].children or []
    urls: set[str] = set()
    inside = False
    for token in children:
        if token.type == "link_open" and not inside:
            url = token.attrGet("href") or ""
            if (
                not isinstance(url, str)
                or not url.startswith(("https://", "http://"))
                or url in urls
            ):
                return None
            try:
                normalize_reporting_url(url)
            except ReportingGroundingError:
                return None
            urls.add(url)
            inside = True
        elif token.type == "link_close" and inside:
            inside = False
        elif token.type in {"text", "code_inline"} and inside:
            continue
        elif token.type == "text" and not inside and token.content.strip() in {"", ","}:
            continue
        else:
            return None
    return urls if urls and not inside else None


def _quoted_atoms(value: str, urls: set[str]) -> list[tuple[str, int, int]] | None:
    """Read complete canonical source literals, with their exact wire spans."""
    result = []
    position = 0
    while position < len(value):
        link = _SOURCE.match(value, position)
        if not link or not (owned := _links(link.group()[:-3])) or not owned <= urls:
            return None
        start = link.end()
        if delimiter := re.match(r"`+", value[start:]):
            # Canonical encoding uses a delimiter longer than any interior run.
            closing = re.search(
                rf"(?<!`){re.escape(delimiter.group())}(?!`)",
                value[start + len(delimiter.group()) :],
            )
            if not closing:
                return None
            end = start + len(delimiter.group()) + closing.end()
        else:
            end = value.find("”", start)
        if end < start or value[end : end + 1] != "”":
            return None
        text = _literal(value[start:end])
        if text is None or not text:
            return None
        result.append((text, start, end))
        position = end + 1
        if position < len(value):
            if value[position : position + 1] != " ":
                return None
            position += 1
    return result


def _partition(value: str, atoms: set[str]) -> tuple[str, ...] | None:
    """Count complete partitions up to two; iterative DP never enumerates paths."""
    counts = [0] * (len(value) + 1)
    previous: dict[int, tuple[int, str]] = {}
    counts[0] = 1
    for position in range(len(value)):
        if not counts[position]:
            continue
        for atom in atoms:
            if not atom or not value.startswith(atom, position):
                continue
            end = position + len(atom)
            if end < len(value):
                if value[end : end + 1] != " " or end + 1 == len(value):
                    continue
                end += 1
            previous[end] = (position, atom)
            counts[end] = min(2, counts[end] + counts[position])
    if counts[-1] != 1:
        return None
    result = []
    position = len(value)
    while position:
        position, atom = previous[position]
        result.append(atom)
    return tuple(reversed(result))


def _markers_inside(value: str, spans: list[tuple[int, int]]) -> bool:
    return all(
        any(start <= match.start() and match.end() <= end for start, end in spans)
        for match in THREAT_ACTIVITY_MARKER_PATTERN.finditer(value)
    )


def has_complete_activity_coverage(markdown: str) -> bool:
    """Prove only coverage of stated report material; ambiguity yields no proof.

    The caller retains the legacy heuristic when this returns false. No external
    certificate, source catalog, cached decision or caller exemption is accepted.
    """
    lines = markdown.splitlines()
    tokens = _PARSER.parse(markdown)
    findings: dict[str, _Finding] = {}
    identities: set[str] = set()
    sections: set[str] = set()
    headings: set[int] = set()
    activity_lines: set[int] = set()
    accounted: set[int] = set()
    rollups: list[tuple[str, str, str, int]] = []
    section = ""
    owner: _Finding | None = None
    for index, token in enumerate(tokens):
        if token.type == "heading_open":
            if token.level != 0 or not token.map or token.map[1] != token.map[0] + 1:
                return False
            inline = tokens[index + 1]
            title = inline.content
            if lines[token.map[0]] != "#" * int(token.tag[1:]) + " " + title:
                return False
            if any(child.type != "text" for child in inline.children or []):
                return False
            headings.add(token.map[0])
            if token.tag == "h2":
                identity = normalize_heading_identity(title)
                if identity in sections:
                    return False
                sections.add(identity)
                section, owner = title, None
            elif token.tag == "h3":
                identity = normalize_heading_identity(title)
                if section != _ACTIVE or identity in identities:
                    return False
                identities.add(identity)
                owner = findings[title] = _Finding()
            elif token.tag != "h1":
                return False
        if section == _ACTORS and token.map:
            activity_lines.update(range(*token.map))
        if token.type != "list_item_open":
            continue
        expected = [
            "list_item_open",
            "paragraph_open",
            "inline",
            "paragraph_close",
            "list_item_close",
        ]
        if token.level != 1 or [t.type for t in tokens[index : index + 5]] != expected:
            return False
        inline = tokens[index + 2]
        if not inline.map or inline.map[1] != inline.map[0] + 1:
            return False
        line = inline.map[0]
        item = _ITEM.fullmatch(lines[line])
        if not item:
            if THREAT_ACTIVITY_MARKER_PATTERN.search(lines[line]):
                return False
            continue
        label, value = item.groups()
        if section == _ACTIVE:
            if owner is None or label in owner.fields:
                return False
            owner.fields[label] = (value, line)
        elif section in _ROLLUPS:
            rollups.append((section, label, value, line))

    if (
        not findings
        or not {
            normalize_heading_identity(_ACTIVE),
            normalize_heading_identity(_ACTORS),
        }
        <= sections
    ):
        return False
    for finding in findings.values():
        reporting = finding.fields.get("Reporting")
        if not reporting or not (urls := _links(reporting[0])):
            return False
        cves = finding.fields.get("CVE IDs")
        if cves and not re.fullmatch(
            r"CVE-\d{4}-\d{4,}(?:, CVE-\d{4}-\d{4,})*", cves[0]
        ):
            return False
        if "Source Evidence" not in finding.fields:
            return False
        for name in _QUOTED_FIELDS:
            if name not in finding.fields:
                continue
            value, line = finding.fields[name]
            if (
                name != "Source Evidence"
                and not value.startswith("[Source]")
                and not THREAT_ACTIVITY_MARKER_PATTERN.search(lines[line])
            ):
                continue
            atoms = _quoted_atoms(value, urls)
            if atoms is None:
                return False
            finding.atoms.update(text for text, _, _ in atoms)
            if THREAT_ACTIVITY_MARKER_PATTERN.search(lines[line]):
                if THREAT_ACTIVITY_MARKER_PATTERN.search(
                    lines[line][: -len(value)]
                ) or not _markers_inside(
                    value, [(start, end) for _, start, end in atoms]
                ):
                    return False
                accounted.add(line)
            finding.required.update(
                text
                for text, _, _ in atoms
                if THREAT_ACTIVITY_MARKER_PATTERN.search(text)
            )
        for name, (value, line) in finding.fields.items():
            if name in _QUOTED_FIELDS or not THREAT_ACTIVITY_MARKER_PATTERN.search(
                lines[line]
            ):
                continue
            if name not in _LITERAL_FIELDS or THREAT_ACTIVITY_MARKER_PATTERN.search(
                lines[line][: -len(value)]
            ):
                return False
            literal = _literal(value)
            parts = _partition(literal, finding.atoms) if literal is not None else None
            if parts is None:
                return False
            finding.required.update(
                part for part in parts if THREAT_ACTIVITY_MARKER_PATTERN.search(part)
            )
            accounted.add(line)
    for kind, label, value, line in rollups:
        if kind != _ACTORS and not THREAT_ACTIVITY_MARKER_PATTERN.search(lines[line]):
            continue
        finding = findings.get(label)
        if finding is None or THREAT_ACTIVITY_MARKER_PATTERN.search(
            lines[line][: -len(value)]
        ):
            return False
        literal = _literal(value)
        parts = _partition(literal, finding.atoms) if literal is not None else None
        if parts is None:
            return False
        if kind == _ACTORS:
            finding.covered.update(parts)
        else:
            finding.required.update(
                part for part in parts if THREAT_ACTIVITY_MARKER_PATTERN.search(part)
            )
            accounted.add(line)
    # Account for all counted marker occurrences, including unsupported prose,
    # comments, URL/label text and metadata. Headings/actor section are excluded
    # by the legacy rule; Source Attribution was removed by the caller.
    recognized = accounted | headings | activity_lines
    if any(
        THREAT_ACTIVITY_MARKER_PATTERN.search(line) and index not in recognized
        for index, line in enumerate(lines)
    ):
        return False
    return all(f.required <= f.covered for f in findings.values())
