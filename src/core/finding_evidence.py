"""Conservative, source-bound exploitation and finding detail publication checks.

Relevance is not confirmation. Ambiguous subject attribution fails closed; a
model may not discard negative evidence by selecting only a positive excerpt.
This is a bounded recognition grammar, not a general English parser.
Unrecognized constructions remain unknown and can block publication; genuine
source confirmations are not guaranteed to be recognized in every phrasing.
"""

from dataclasses import dataclass
import re
from typing import Any, Literal, Mapping, Sequence

from markdown_it import MarkdownIt
from markdown_it.token import Token

from .cve import extract_cve_ids
from .reporting import (
    ACTIVE_SECTION_PATTERN,
    FINDING_PATTERN,
    ReportingGroundingError,
    ReportingSource,
    normalize_reporting_url,
)

ABSENT = "Not stated in supplied sources."
DETAIL_FIELDS = (
    "Affected Versions",
    "Exceptions",
    "Recommended Actions",
    "Vendor Links",
)
FIELD = re.compile(r"^-\s+\*\*([^*]+)\*\*:\s*(.*?)\s*$", re.MULTILINE)
NEGATIVE = re.compile(
    r"\b(?:exploit\w* (?:has |have |is |was |were )?not (?:yet |been )*(?:observed|detected|confirmed)|no (?:known exploitation|evidence|signs?|reports?|exploitation)|(?:not|never) (?:yet |been |being |actively |publicly |known to be |observed to be )*(?:exploit\w*|weaponiz\w*)|(?:has|have) not been (?:actively )?(?:exploit\w*|weaponiz\w*)|without (?:evidence|reports?) of exploitation)\b",
    re.I,
)
UNCERTAIN_ADVERBS = ("potentially", "likely", "possibly", "probably", "unlikely")
UNCERTAIN = re.compile(
    rf"\b(?:{'|'.join(UNCERTAIN_ADVERBS)}|may|might|could|potential|possible|risk|proof.of.concept|assessment|unknown|unclear|unconfirmed|unverified|investigat\w*|whether)\b",
    re.I,
)
CONFIRMED = re.compile(
    r"\b(?:actively exploited|active exploitation(?: attempts)?|(?:is|are|was|were|been|being) exploited (?:in|by)|(?:attackers?|actors?|operators?) (?:are |were )?exploit(?:ing|ed)?|exploitation (?:was |is )?(?:confirmed|observed|detected)|weaponized in (?:the wild|attacks))\b",
    re.I,
)
EXPLOIT = re.compile(r"\b(?:exploit\w*|weaponiz\w*)\b", re.I)
EPISTEMIC = re.compile(r"\b(?:unknown|unclear|unconfirmed|unverified|whether)\b", re.I)
MODAL = re.compile(r"\b(?:may|might|could)\b", re.I)
CORRELATIVE_START = re.compile(r"\bnot (?:only|just|merely|simply)\b", re.I)
CLAUSE_BOUNDARY = re.compile(
    r"([;,]\s*(?:and|but|while|whereas)\b|[;,]|\b(?:and|but|while|whereas)\b)",
    re.I,
)
PREDICATE_MODIFIERS = frozenset(UNCERTAIN_ADVERBS) | {
    "also",
    "currently",
    "now",
    "still",
    "not",
    "never",
    "actively",
    "newly",
    "recently",
    "widely",
    "publicly",
    "successfully",
}
FINITE_PREDICATE_HEADS = frozenset(
    {
        "is",
        "are",
        "was",
        "were",
        "has",
        "have",
        "had",
        "may",
        "might",
        "could",
        "can",
        "will",
        "would",
    }
)
PARTICIPIAL_PREDICATE_HEADS = frozenset(
    {
        "exploited",
        "weaponized",
        "affected",
        "vulnerable",
        "exploitable",
    }
)
PREDICATE_HEADS = (
    FINITE_PREDICATE_HEADS | PARTICIPIAL_PREDICATE_HEADS | {"be", "been", "being"}
)
ADJUNCT_INTRODUCERS = frozenset(
    {
        "after",
        "before",
        "when",
        "because",
        "since",
        "until",
        "once",
        "although",
        "though",
        "unless",
        "if",
        "where",
        "during",
        "upon",
        "in",
        "by",
        "on",
        "at",
        "through",
        "via",
        "against",
        "for",
        "to",
        "from",
        "with",
        "without",
        "as",
        "within",
        "across",
        "under",
        "over",
        "throughout",
        "around",
        "despite",
    }
)
PREDICATE_ADVERBS = frozenset(
    {
        "worldwide",
        "abroad",
        "overseas",
        "here",
        "there",
        "today",
        "yesterday",
        "tomorrow",
        "tonight",
        "earlier",
        "later",
        "again",
        "already",
        "often",
        "sometimes",
        "always",
        "ever",
        "soon",
        "twice",
        "ago",
        "overnight",
    }
)
TIME_UNIT = r"(?:second|minute|hour|day|week|fortnight|month|quarter|year|weekend|night|morning|afternoon|evening)s?"
WEEKDAY = r"(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday)(?: (?:morning|afternoon|evening|night))?"
QUANTITY = r"(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|several|many|multiple|numerous|a|an|(?:hundreds|thousands|millions|dozens) of)"
NOMINAL_ADJUNCT = re.compile(
    rf"(?:(?:the )?(?:last|next|previous|following|this|that|every|each|all) (?:{QUANTITY} )?(?:{TIME_UNIT}|{WEEKDAY})"
    rf"|{QUANTITY} {TIME_UNIT}"
    rf"|{WEEKDAY}"
    rf"|(?:(?:more|less|fewer) than |at (?:least|most) |up to )?{QUANTITY} (?:times|occasions))(?= |$)"
)


class EvidenceError(ValueError):
    pass


@dataclass(frozen=True)
class ExploitationAssessment:
    status: str
    negative: tuple[str, ...] = ()
    positive: tuple[str, ...] = ()
    conflicting: bool = False


@dataclass(frozen=True)
class ExploitationStatement:
    """A source span with its own subject attribution and evidence state."""

    text: str
    cves: tuple[str, ...]
    attribution: Literal["explicit", "coordinated", "unscoped"]
    relation: Literal["root", "additive", "adversative", "correlative", "boundary"]
    status: str


def _sentences(text: str) -> list[str]:
    return [
        part.strip() for part in re.split(r"(?<=[.!?])\s+|\n+", text) if part.strip()
    ]


def _value(source: Any, field: str, default=""):
    return (
        source.get(field, default)
        if isinstance(source, dict)
        else getattr(source, field, default)
    )


def _scoped_sentences(source: Any, cves: Sequence[str]) -> list[tuple[str, bool]]:
    content = str(_value(source, "content"))
    source_cves = set(extract_cve_ids(content))
    wanted = set(cves)
    result = []
    for sentence in _sentences(content):
        if sentence.startswith("#"):
            continue
        mentioned = set(extract_cve_ids(sentence))
        # A sentence about two vulnerabilities is ambiguous, even if one matches.
        if mentioned and (not mentioned <= wanted or not mentioned & wanted):
            continue
        direct = bool(mentioned and mentioned <= wanted)
        if direct or (not mentioned and wanted and source_cves == wanted):
            result.append((sentence, direct))
    return result


def _clause_status(clause: str) -> str:
    if not EXPLOIT.search(clause):
        return "unknown"
    if NEGATIVE.search(clause):
        return "not_observed"
    if UNCERTAIN.search(clause):
        if EPISTEMIC.search(clause):
            return "unknown"
        return "potential"
    return "active" if CONFIRMED.search(clause) else "unknown"


def _predicate_head(clause: str) -> str:
    # Only known modifiers may precede an inherited predicate. In particular,
    # an arbitrary -ly suffix is not enough: it can also occur in noun subjects.
    words = clause.casefold().rstrip(".!?").split()
    for index, word in enumerate(words):
        if word not in PREDICATE_MODIFIERS:
            if word in PARTICIPIAL_PREDICATE_HEADS:
                # An adjective/participle can instead introduce a noun subject:
                # "newly affected issue" is not the prior CVE's predicate.
                # Parse the continuation as adverbs followed by an optional
                # adjunct. A new noun phrase ends attribution regardless of
                # which lexical verb follows it. An adjunct's own finite verb
                # does not establish a new subject for the main predicate.
                tail = words[index + 1 :]
                while tail:
                    token = tail[0]
                    if token in ADJUNCT_INTRODUCERS:
                        break
                    nominal = NOMINAL_ADJUNCT.match(" ".join(tail))
                    if nominal:
                        tail = tail[len(nominal.group().split()) :]
                        continue
                    if (
                        token in PREDICATE_MODIFIERS | PREDICATE_ADVERBS
                        or re.fullmatch(r"[a-z]+ly", token)
                    ):
                        tail = tail[1:]
                        continue
                    return ""
            return word
    return ""


def _statements(sentence: str) -> list[ExploitationStatement]:
    """Track subjects and stance through recognized coordinated predicates.

    This deliberately does not resolve pronouns, new noun subjects, or subjects
    across sentences/semicolons. Relative ``which`` stays in its original span.
    A shared modal or negation qualifies a bare coordinated predicate; a new
    finite auxiliary starts its own assertion. Epistemic scope ("unknown
    whether ... and ...") also applies when the CVE is repeated. Adversative
    ``but`` may retain the subject but starts a new assertion scope. Paired
    ``not only ... but [also]`` is correlative addition and keeps its opener's
    scope; consuming the pair lets a later adversative start a new assertion.
    """
    parts = CLAUSE_BOUNDARY.split(sentence)
    statements: list[ExploitationStatement] = []
    subjects: tuple[str, ...] = ()
    epistemic = modal = negative = False
    correlative_scopes: list[tuple[bool, bool, bool]] = []
    for index in range(0, len(parts), 2):
        clause = parts[index].strip()
        if not clause:
            continue
        boundary = " ".join(parts[index - 1].lower().split()) if index else ""
        relation: Literal["root", "additive", "adversative", "correlative", "boundary"]
        correlative_scope = None
        if boundary in {"but", ", but"} and correlative_scopes:
            relation = "correlative"
            correlative_scope = correlative_scopes.pop()
        elif boundary in {"but", ", but"}:
            relation = "adversative"
        elif boundary in {"and", ", and"}:
            relation = "additive"
        else:
            relation = "boundary" if index else "root"
            correlative_scopes.clear()
        additive = relation in {"additive", "correlative"}
        coordinate = relation in {"additive", "correlative", "adversative"}
        head = _predicate_head(clause)
        predicate = coordinate and head in PREDICATE_HEADS
        finite = head in FINITE_PREDICATE_HEADS
        mentioned = tuple(extract_cve_ids(clause))
        attribution: Literal["explicit", "coordinated", "unscoped"]
        if mentioned:
            subjects = mentioned
            attribution = "explicit"
        elif predicate and len(subjects) == 1:
            attribution = "coordinated"
        else:
            subjects = ()
            attribution = "unscoped"

        shared_predicate = additive and predicate and not finite
        if correlative_scope is not None:
            inherited_epistemic, inherited_modal, inherited_negative = correlative_scope
        else:
            inherited_epistemic = epistemic and additive
            inherited_modal = modal and shared_predicate
            inherited_negative = negative and shared_predicate
        epistemic = bool(EPISTEMIC.search(clause)) or inherited_epistemic
        modal = bool(MODAL.search(clause)) or inherited_modal
        negative = bool(NEGATIVE.search(clause)) or inherited_negative
        status = _clause_status(clause)
        if EXPLOIT.search(clause):
            if epistemic:
                status = "unknown"
            elif negative:
                status = "not_observed"
            elif modal:
                status = "potential"
        for opener in CORRELATIVE_START.finditer(clause):
            # Only qualifiers governing the pair transfer to its second part.
            # A qualifier inside the first constituent belongs to that part.
            prefix = clause[: opener.start()]
            correlative_scopes.append(
                (
                    inherited_epistemic or bool(EPISTEMIC.search(prefix)),
                    inherited_modal or bool(UNCERTAIN.search(prefix)),
                    inherited_negative or bool(NEGATIVE.search(prefix)),
                )
            )
        statements.append(
            ExploitationStatement(clause, subjects, attribution, relation, status)
        )
    return statements


def assess_exploitation(
    sources: Sequence[Any], cves: Sequence[str]
) -> ExploitationAssessment:
    unique_cves = tuple(dict.fromkeys(cves))
    if len(unique_cves) > 1:
        assessments = [assess_exploitation(sources, [cve]) for cve in unique_cves]
        statuses = {item.status for item in assessments}
        return ExploitationAssessment(
            assessments[0].status if len(statuses) == 1 else "unknown",
            tuple(text for item in assessments for text in item.negative),
            tuple(text for item in assessments for text in item.positive),
            any(item.conflicting for item in assessments)
            or ("active" in statuses and "not_observed" in statuses),
        )
    positive, negative, potential = [], [], []
    for source in sources:
        for sentence, direct in _scoped_sentences(source, cves):
            for statement in _statements(sentence):
                attributed = bool(set(cves) & set(statement.cves))
                if direct and not attributed:
                    continue
                if statement.status == "not_observed":
                    negative.append(sentence)
                elif statement.status == "potential":
                    potential.append(sentence)
                elif attributed and statement.status == "active":
                    positive.append(sentence)
    conflict = bool(positive and negative)
    status = (
        "unknown"
        if conflict
        else (
            "not_observed"
            if negative
            else "active" if positive else "potential" if potential else "unknown"
        )
    )
    return ExploitationAssessment(status, tuple(negative), tuple(positive), conflict)


def _plain(text: str) -> str:
    return " ".join(text.split()).casefold()


def _version_entries(text: str) -> list[str]:
    """Keep range tails, stop at clear clauses, and reject ambiguous tails."""
    text = re.sub(
        r"\b(?:users|customers|operators|administrators) of ([^,;]+?) "
        r"(?:are|were|remain) (?:(?:also|still) )?(?:affected|impacted|vulnerable)\b",
        r"\1",
        text,
        flags=re.I,
    )
    parts = re.split(r"([,;]|\s+(?:and|or)\s+)", text.strip().rstrip("."), flags=re.I)
    entries: list[str] = []
    pending = ""
    for index in range(0, len(parts), 2):
        entry = parts[index].strip()
        if not entry:
            continue
        if pending:
            if parts[index - 1].strip().casefold() not in {"and", "or"}:
                raise EvidenceError("ambiguous affected-version continuation")
            entry = pending + parts[index - 1] + entry
            pending = ""
        qualifier = re.match(
            r"(?:(?:all|any|the|other)\s+)*(?:(?:versions?|releases?|builds?)\s+)?"
            r"(?:earlier|later|older|newer|higher|lower|above|below|before|after|prior|previous|subsequent|up|down|greater|less|lesser|onwards?|beyond)\b",
            entry,
            re.I,
        )
        recommendation = re.match(
            r"(?P<subject>(?:customers|users|admins|administrators|operators|owners|vendors|maintainers|organizations|you)\b.*?)"
            r"\b(?:should|must|needs? to|are advised to|is advised to)\s+(?:\w+ly\s+)*"
            r"(?:install|apply|patch|upgrade|update|consult|review|contact)\b",
            entry,
            re.I,
        )
        information = re.match(
            r"(?:(?:further|more) )?(?:details|information)\b.*?\b(?:is|are) "
            r"(?:available|provided|published)\b",
            entry,
            re.I,
        )
        if entries and qualifier:
            entries[-1] += parts[index - 1] + entry
        elif (
            entries
            and not re.search(
                r"\b(?:affected|impacted|vulnerable)\b",
                entry,
                re.I,
            )
            and (
                information
                or (
                    recommendation
                    and not re.search(
                        r"\d|\bRTM\b", recommendation.group("subject"), re.I
                    )
                )
            )
        ):
            break
        elif not re.search(r"\d|\bRTM\b", entry, re.I):
            pending = entry
        else:
            entries.append(entry)
    if pending:
        if entries:
            raise EvidenceError("ambiguous affected-version continuation")
        entries.append(pending)
    return entries


def _supported_version_text(entry: str, source: str) -> bool:
    """Match full source tokens, including unknown version suffix syntax."""
    source = _plain(source)
    for match in re.finditer(rf"(?<!\w){re.escape(_plain(entry))}", source):
        tail = re.match(r"[^\s,;()\[\]{}\"']*", source[match.end() :])
        if tail and not tail.group().strip(".!?:"):
            return True
    return False


def _rendered_text(tokens: Sequence[Token]) -> str:
    parts = []
    for token in tokens:
        if token.type in {"softbreak", "hardbreak"}:
            parts.append(" ")
        elif token.children:
            parts.append(_rendered_text(token.children))
        elif token.type in {"text", "code_inline"}:
            parts.append(token.content)
    return "".join(parts)


def _rendered_statements(text: str) -> list[ExploitationStatement]:
    # Check reader-visible Markdown text so emphasis/entities cannot split a
    # claim into a form that the evidence guard fails to recognize.
    blocks = []
    for token in MarkdownIt("commonmark").parse(text):
        if token.type == "inline":
            blocks.append(_rendered_text(token.children or []))
        elif token.type in {"fence", "code_block"}:
            blocks.append(" ".join(token.content.split()))
    text = "\n".join(blocks)
    return [
        statement
        for sentence in _sentences(text)
        for statement in _statements(sentence)
    ]


def _positive_claim(text: str) -> bool:
    return any(statement.status == "active" for statement in _rendered_statements(text))


def validate_finding_evidence(
    report: str, catalog: Mapping[str, ReportingSource]
) -> None:
    section = ACTIVE_SECTION_PATTERN.search(report)
    if not section:
        raise EvidenceError("Missing finding evidence section")
    nonconfirmed = []
    for finding in FINDING_PATTERN.finditer(section.group("section")):
        title = finding.group("heading").removeprefix("###").strip()
        body = finding.group("body")
        pairs = FIELD.findall(body)
        fields = dict(pairs)
        if len(pairs) != len(fields):
            raise EvidenceError(f"{title}: duplicate finding field")
        keys = [key.strip() for key in fields.get("Reporting", "").split(",")]
        if not keys or any(key not in catalog for key in keys):
            raise EvidenceError(f"{title}: missing retained source evidence")
        sources = [catalog[key] for key in keys]
        if any(not source.content.strip() for source in sources):
            raise EvidenceError(f"{title}: missing retained source content")
        cves = extract_cve_ids(fields.get("CVE IDs", "") + " " + title)
        # Assess every supplied source naming this CVE, even when the model
        # omits that source from its chosen citations.
        relevant = list(sources)
        relevant.extend(
            source
            for source in catalog.values()
            if source not in relevant
            and set(cves) & set(extract_cve_ids(source.content))
        )
        assessment = assess_exploitation(relevant, cves)
        status = fields.get("Exploitation Status", "")
        allowed = {assessment.status}
        if assessment.status == "active":
            allowed.add("observed")
        if status not in allowed:
            raise EvidenceError(
                f"{title}: unsupported exploitation status {status!r}; source evidence is {assessment.status}"
            )
        # Check narrative separately; changing only the badge cannot pass.
        narrative = FIELD.sub(
            lambda match: (
                ""
                if match.group(1) in {"Reporting", "CVE IDs", "Exploitation Status"}
                else match.group(2)
            ),
            body,
        )
        if status not in {"active", "observed"}:
            nonconfirmed.append((title, cves))
            if _positive_claim(title + "\n\n" + narrative):
                raise EvidenceError(f"{title}: unsupported exploitation claim in prose")
        if assessment.negative and not NEGATIVE.search(narrative):
            raise EvidenceError(f"{title}: prose omits negative exploitation evidence")
        if assessment.conflicting and not re.search(
            r"\bconflict\w*\b", narrative, re.I
        ):
            raise EvidenceError(
                f"{title}: prose must disclose conflicting exploitation evidence"
            )
        if (
            fields.get("Action") in {"patch", "mitigate"}
            and fields.get("Recommended Actions") == ABSENT
        ):
            raise EvidenceError(
                f"{title}: action badge omits a supported recommendation"
            )
        scoped = "\n".join(
            sentence
            for source in sources
            for sentence, _ in _scoped_sentences(source, cves)
        )
        # Without a CVE, exact source details remain usable, but exploitation is
        # unknown until an unambiguous subject identity is available.
        if not cves:
            scoped = "\n".join(source.content for source in sources)
        # Version lists are easy to lose even when one supported version remains.
        version_lines = []
        in_versions = False
        for line in scoped.splitlines():
            cue = re.search(
                r"\b(?:affected versions?|versions? (?:are )?(?:impacted|affected))\b",
                line,
                re.I,
            )
            if cue:
                in_versions = True
                remainder = re.sub(
                    r"^\s*(?:(?:are|is|include|includes)\b)?\s*[:=-]?\s*",
                    "",
                    line[cue.end() :],
                    flags=re.I,
                ).rstrip(". ")
                version_lines.extend(
                    entry
                    for entry in _version_entries(remainder)
                    if re.search(r"\d|\bRTM\b", entry) and not extract_cve_ids(entry)
                )
                continue
            if in_versions:
                if re.search(r"\d|\bRTM\b", line) and not extract_cve_ids(line):
                    version_lines.extend(_version_entries(line))
                else:
                    in_versions = False
        reported_versions = {
            _plain(entry)
            for entry in _version_entries(fields.get("Affected Versions", ""))
        }
        if any(_plain(line) not in reported_versions for line in version_lines):
            raise EvidenceError(
                f"{title}: Affected Versions omits supplied version list entries"
            )
        if version_lines and reported_versions - {
            _plain(line) for line in version_lines
        }:
            raise EvidenceError(f"{title}: unsupported affected-version entry")
        for name in DETAIL_FIELDS:
            value = fields.get(name, "")
            if not value:
                raise EvidenceError(
                    f"{title}: missing {name}; use {ABSENT!r} when absent"
                )
            cues = {
                "Affected Versions": r"\b(?:affected versions?|versions? (?:are )?(?:impacted|affected)|cumulative update)\b",
                "Exceptions": r"\b(?:need(?:s)? no action|not (?:required|affected)|unaffected|does not allow|no customer action)\b",
                "Recommended Actions": r"\b(?:install (?:the )?(?:updates?|patch)|apply (?:the )?(?:fix|patch|update)|advised to|recommended to)\b",
            }
            if value == ABSENT:
                if name in cues and re.search(cues[name], scoped, re.I):
                    raise EvidenceError(
                        f"{title}: {name} omits supplied source details"
                    )
                continue
            entries = [entry.strip() for entry in value.split(";")]
            if name == "Vendor Links":
                links = {link for source in sources for link in source.links}
                try:
                    normalized = [normalize_reporting_url(entry) for entry in entries]
                except ReportingGroundingError as exc:
                    raise EvidenceError(f"{title}: unsupported vendor link") from exc
                if any(entry not in links for entry in normalized):
                    raise EvidenceError(f"{title}: unsupported vendor link")
            elif name == "Affected Versions" and any(
                not _supported_version_text(entry, scoped) for entry in entries
            ):
                raise EvidenceError(
                    f"{title}: {name} must preserve exact source-supported details"
                )
            elif any(_plain(entry) not in _plain(scoped) for entry in entries):
                raise EvidenceError(
                    f"{title}: {name} must preserve exact source-supported details"
                )
    # Free-standing aggregate claims cannot safely inherit the heading's state.
    # Require explicit CVEs for confirmed claims outside finding bodies whenever
    # the report contains mixed evidence states.
    outside = report[: section.start()] + report[section.end() :]
    for statement in _rendered_statements(outside):
        if statement.status != "active":
            continue
        mentioned = set(statement.cves)
        if nonconfirmed and (
            not mentioned or any(mentioned & set(cves) for _, cves in nonconfirmed)
        ):
            raise EvidenceError(
                "Unsupported exploitation claim in summary or cross-finding prose"
            )
