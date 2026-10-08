"""Conservative, source-bound exploitation and finding detail publication checks.

Relevance is not confirmation. Ambiguous subject attribution fails closed; a
model may not discard negative evidence by selecting only a positive excerpt.
This is a bounded recognition grammar, not a general English parser.
Unrecognized constructions remain unknown and can block publication; genuine
source confirmations are not guaranteed to be recognized in every phrasing.
"""

from dataclasses import dataclass, replace
import hashlib
import re
from typing import Any, Literal, Mapping, Sequence

from markdown_it import MarkdownIt
from markdown_it.token import Token

from .cve import CVE_ID_PATTERN, extract_cve_ids
from .assertions import FINITE_PREDICATE_HEADS, parse_assertions
from .relations import OwnedClause
from .recommendations import (
    RecommendationBlock,
    directive_units,
    parse_recommendation,
    project_recommendation_action,
)
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
VERSION_LIST_CUE = r"\b(?:affected (?:versions?|releases?)|versions? (?:are )?(?:impacted|affected)|supported releases?)\b"
CUMULATIVE_UPDATE_CUE = r"\bcumulative updates?\b"
DETAIL_CUES = {
    "Affected Versions": VERSION_LIST_CUE,
    "Exceptions": r"\b(?:need(?:s)? no action|not (?:required|affected|impacted|vulnerable)|no longer (?:affected|impacted|vulnerable)|unaffected|exempt|does not allow|no customer action)\b",
    "Recommended Actions": r"\b(?:install (?:the )?(?:updates?|patch)|apply (?:the )?(?:fix|patch|update)|advised to|recommended to|(?:should|must) (?:install|apply|patch|upgrade|update)|restart (?:the )?service)\b",
}


def detail_statement_roles(text: str, context: str = "") -> tuple[str, ...]:
    version_cue = _version_list_cue(text)
    return tuple(
        name
        for name, cue in DETAIL_CUES.items()
        if (
            bool(version_cue and version_cue.kind == "explicit")
            or _cumulative_version_list(text, context)
            if name == "Affected Versions"
            else re.search(cue, text, re.I)
            or (name == "Recommended Actions" and any(_recommendation_directives(text)))
        )
    )


def _heading_detail_roles(text: str) -> tuple[str, ...]:
    label = re.sub(r"^\d+[.)]\s*", "", text).strip(" :").casefold()
    return tuple(name for name in DETAIL_CUES if name.casefold() == label)


class EvidenceError(ValueError):
    def __init__(
        self,
        message: str,
        *,
        code: str = "finding_evidence_rejected",
        field: str | None = None,
        expected: str | int | bool | None = None,
        observed: str | int | bool | None = None,
    ):
        super().__init__(message)
        self.code = code
        self.field = field
        self.expected = expected
        self.observed = observed
        self.finding_index: int | None = None
        self.cves: tuple[str, ...] = ()
        self.source_keys: tuple[str, ...] = ()
        self.finding_sha256: str | None = None


@dataclass(frozen=True)
class ExploitationAssessment:
    status: str
    negative: tuple[str, ...] = ()
    positive: tuple[str, ...] = ()
    conflicting: bool = False
    unsupported: tuple[str, ...] = ()
    relations: tuple[OwnedClause, ...] = ()


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


def source_assertions(source: Any) -> tuple[OwnedClause, ...]:
    """Interpret before selecting scope; a joint claim is never two singletons."""
    content = str(_value(source, "content"))
    source_cves = set(extract_cve_ids(content))
    result = []
    for sentence in _sentences(content):
        if sentence.startswith("#"):
            continue
        for clause in parse_assertions(sentence):
            if clause.kind != "assertion":
                continue
            # Preserve the existing limited source-context rule. A body naming
            # one CVE may supply unscoped absence/possibility, never positive
            # confirmation or metadata-to-body attribution.
            if (
                not clause.cves
                and not extract_cve_ids(sentence)
                and len(source_cves) == 1
                and clause.status in {"not_observed", "potential"}
            ):
                clause = replace(
                    clause, cves=tuple(source_cves), attribution="source_context"
                )
            result.append(replace(clause, source_text=sentence))
    return tuple(result)


@dataclass(frozen=True)
class DetailSpan:
    """Keep source structure separate from factual body evidence."""

    text: str
    role: Literal["heading", "body", "boundary"]
    fields: tuple[str, ...] = ()
    source_block: str = ""
    version_context: str = ""


def _recommendation_text(text: str) -> str:
    text = _plain(text)
    # A terminal sentence period is optional in the report field. Question
    # marks, exclamations and ellipses remain part of the source statement.
    return text[:-1] if text.endswith(".") and not text.endswith("..") else text


def _validate_recommendation_statements(
    value: str, spans: Sequence[DetailSpan]
) -> None:
    """Match complete source statements before interpreting field delimiters.

    Original source paragraphs/list items own their internal punctuation and
    audience qualifiers; sentence splitting cannot trim those boundaries.
    Source statements own their internal semicolons. Longest matching statements
    are consumed first, so a delimiter inside a statement is never mistaken for
    the delimiter between two report entries.
    """
    required = {
        _recommendation_text(span.source_block or span.text)
        for span in spans
        if span.role == "body" and "Recommended Actions" in span.fields
    }
    candidates = sorted(required, key=len, reverse=True)
    normalized_value = _plain(value)
    remaining = normalized_value
    while remaining:
        for statement in candidates:
            if not remaining.startswith(statement):
                continue
            delimiter = re.match(r"\.?(?:\s*;\s*|$)", remaining[len(statement) :])
            if delimiter:
                remaining = remaining[len(statement) + delimiter.end() :]
                break
        else:
            raise EvidenceError(
                "Recommended Actions must preserve complete source-supported statements with their semantic role",
                code="recommendation_not_grounded",
                field="Recommended Actions",
                expected=True,
                observed=False,
            )
    # A longer copied statement can also contain a complete shorter statement
    # from another source; do not require duplicated clauses in that case.
    if any(
        not re.search(
            rf"(?:^|;\s*){re.escape(statement)}\.?(?=\s*;|$)", normalized_value
        )
        for statement in required
    ):
        raise EvidenceError(
            "Recommended Actions omits a complete source recommendation or prohibition",
            code="missing_source_recommendation",
            field="Recommended Actions",
            expected=True,
            observed=False,
        )


def _logical_source_blocks(content: str) -> list[str]:
    """Map physical lines to original paragraphs or outer list items."""
    lines = content.splitlines()
    blocks = list(lines)
    item_depth = 0
    for token in MarkdownIt("commonmark").parse(content):
        owns_block = False
        if token.type == "list_item_open":
            owns_block = item_depth == 0
            item_depth += 1
        elif token.type == "list_item_close":
            item_depth -= 1
        elif token.type in {"paragraph_open", "fence", "code_block"}:
            owns_block = item_depth == 0
        if owns_block and token.map:
            start, end = token.map
            block = "\n".join(lines[start:end]).strip()
            for index in range(start, end):
                blocks[index] = block
    return blocks


def _scoped_detail_spans(source: Any, cves: Sequence[str]) -> list[DetailSpan]:
    """Retain detail ownership under CVE headings without asserting exploitation."""
    content = str(_value(source, "content"))
    source_cves = set(extract_cve_ids(content))
    wanted = set(cves)
    has_cve_sections = any(
        extract_cve_ids(match[2])
        for line in content.splitlines()
        if (match := re.match(r"^(#{1,6})\s+(.+)", line.strip()))
    )
    sections: list[tuple[int, set[str], tuple[str, ...]]] = []
    # Boundaries prevent version-list context crossing sources or excluded spans.
    result = [DetailSpan("", "boundary")]
    source_blocks = _logical_source_blocks(content)
    previous_block = None
    preceding: list[str] = []
    for line_index, line in enumerate(content.splitlines()):
        source_block = source_blocks[line_index]
        if source_block != previous_block:
            preceding = []
            previous_block = source_block
        heading = re.match(r"^(#{1,6})\s+(.+)", line.strip())
        if heading:
            level = len(heading[1])
            while sections and sections[-1][0] >= level:
                sections.pop()
            mentioned = set(extract_cve_ids(heading[2]))
            inherited = sections[-1][1] if sections else set()
            inherited_fields = sections[-1][2] if sections and not mentioned else ()
            fields = _heading_detail_roles(heading[2]) or inherited_fields
            sections.append((level, mentioned or inherited, fields))
        owner = sections[-1][1] if sections else set()
        owned = not wanted or bool(
            owner
            and owner <= wanted
            or not owner
            and not has_cve_sections
            and source_cves
            and source_cves <= wanted
        )
        if heading:
            result.append(
                DetailSpan(heading[2], "heading")
                if owned
                else DetailSpan("", "boundary")
            )
            continue
        body_line = re.sub(r"^\s*(?:[-+*]|\d+[.)])\s+", "", line)
        for sentence in _sentences(body_line):
            # Position matters: later advice cannot change an earlier row's
            # role, even when the same release name occurs more than once.
            preceding.append(sentence)
            version_context = " ".join(preceding)
            mentioned = set(extract_cve_ids(sentence))
            selected = mentioned <= wanted if mentioned and wanted else owned
            body_fields = detail_statement_roles(sentence, version_context) or (
                sections[-1][2] if sections else ()
            )
            # Recommendation cues can themselves cross a physical line break.
            if re.search(
                DETAIL_CUES["Recommended Actions"], " ".join(source_block.split()), re.I
            ):
                body_fields = tuple(
                    dict.fromkeys((*body_fields, "Recommended Actions"))
                )
            if (
                selected
                and "Recommended Actions" in body_fields
                and wanted
                and not set(extract_cve_ids(source_block)) <= wanted
            ):
                raise EvidenceError(
                    "ambiguous recommendation block CVE scope",
                    code="ambiguous_recommendation_scope",
                    field="Recommended Actions",
                )
            result.append(
                DetailSpan(
                    sentence,
                    "body",
                    body_fields,
                    source_block,
                    version_context,
                )
                if selected
                else DetailSpan("", "boundary")
            )
    return result


def build_finding_detail_context(
    catalog: Mapping[str, ReportingSource],
) -> list[dict[str, Any]]:
    """Show generation the same per-CVE detail scope used by publication.

    These are eligible source spans, not assertions that every mentioned
    release is affected. Keep headings and boundaries distinct from body text.
    Full articles remain in the prompt for narrative and negative evidence.
    """
    context = []
    assessments = {}
    scopes = {}
    for source in catalog.values():
        scopes.update(dict.fromkeys((cve,) for cve in extract_cve_ids(source.content)))
        # Actual source ownership supplies joint scopes, not a powerset of all
        # article CVEs. Paragraph/list blocks also own complete recommendations
        # whose qualifications can span several sentences.
        for block in dict.fromkeys(_logical_source_blocks(source.content)):
            for text in [block, *_sentences(block)]:
                joint = tuple(sorted(extract_cve_ids(text)))
                if len(joint) > 1:
                    scopes[joint] = None
    for source in catalog.values():
        source_cves = set(extract_cve_ids(source.content))
        relevant_scopes = [scope for scope in scopes if source_cves & set(scope)]
        # A joint finding also includes other sources naming any member, even
        # if those sources do not themselves introduce the combined scope.
        for cves in relevant_scopes if source_cves else [()]:
            if cves not in assessments:
                assessments[cves] = assess_exploitation(list(catalog.values()), cves)
            assessment = assessments[cves]
            item: dict[str, Any] = {
                "source_key": source.key,
                "cves": list(cves),
                "exploitation": {
                    "status": assessment.status,
                    "conflicting": assessment.conflicting,
                },
            }
            try:
                spans = _scoped_detail_spans(source, cves)
            except EvidenceError:
                # An unrelated CVE must not block all analysis. If a finding
                # uses this scope, the unchanged publication check rejects it.
                item["scope_error"] = "ambiguous_detail_scope"
            else:
                rendered = []
                recommendation_blocks = set()
                for span in spans:
                    # Consecutive excluded sentences have the same boundary
                    # effect. Do not multiply them by every CVE in a recap.
                    if (
                        span.role == "boundary"
                        and rendered
                        and rendered[-1]["role"] == "boundary"
                    ):
                        continue
                    entry: dict[str, Any] = {
                        "text": span.text,
                        "role": span.role,
                        "fields": span.fields,
                    }
                    if (
                        "Recommended Actions" in span.fields
                        and span.source_block not in recommendation_blocks
                    ):
                        entry["source_block"] = span.source_block
                        recommendation_blocks.add(span.source_block)
                    rendered.append(entry)
                item["spans"] = rendered
            context.append(item)
    return context


def _safe_diagnostic_value(value: str | int | bool | None) -> str | int | bool | None:
    """Only categorical states, booleans and bounded counts may reach logs."""
    if value is None or isinstance(value, bool):
        return value
    if isinstance(value, int):
        return value if 0 <= value <= 1_000_000 else "invalid"
    return (
        value
        if value
        in {
            "active",
            "observed",
            "potential",
            "not_observed",
            "unknown",
            "missing",
            "invalid",
        }
        else "invalid"
    )


def grounding_failure_diagnostic(
    report: str,
    catalog: Mapping[str, ReportingSource],
    error: EvidenceError | ReportingGroundingError,
) -> dict[str, Any]:
    """Bounded metadata for logs; never include source, candidate, URL or error text."""
    evidence_error = error if isinstance(error, EvidenceError) else None
    cves = evidence_error.cves if evidence_error else ()
    logged_cves = [cve for cve in cves if len(cve) <= 64][:32]
    selected = evidence_error.source_keys if evidence_error else ()
    relevant = [catalog[key] for key in dict.fromkeys(selected) if key in catalog]
    relevant.extend(
        source
        for key, source in catalog.items()
        if key not in selected
        and (not cves or set(cves) & set(extract_cve_ids(source.content)))
    )
    return {
        "schema_version": 1,
        "stage": "finding_evidence" if evidence_error else "reporting_identity",
        "code": (
            evidence_error.code if evidence_error else "reporting_identity_rejected"
        ),
        "field": (
            evidence_error.field
            if evidence_error
            and evidence_error.field
            in {
                *DETAIL_FIELDS,
                "Exploitation Status",
                "Reporting",
                "Action",
                "prose",
                "summary",
            }
            else None
        ),
        "expected": (
            _safe_diagnostic_value(evidence_error.expected) if evidence_error else None
        ),
        "observed": (
            _safe_diagnostic_value(evidence_error.observed) if evidence_error else None
        ),
        "finding_index": evidence_error.finding_index if evidence_error else None,
        "finding_sha256": evidence_error.finding_sha256 if evidence_error else None,
        "cves": logged_cves,
        "cves_truncated": len(cves) - len(logged_cves),
        "report_sha256": hashlib.sha256(report.encode()).hexdigest(),
        "sources": [
            {
                "key": source.key,
                "content_kind": (
                    source.content_kind
                    if source.content_kind in {"feed", "article"}
                    else "unknown"
                ),
                "content_chars": len(source.content),
                "content_sha256": hashlib.sha256(source.content.encode()).hexdigest(),
            }
            for source in relevant[:32]
        ],
        "sources_truncated": max(0, len(relevant) - 32),
    }


def assess_exploitation(
    sources: Sequence[Any], cves: Sequence[str]
) -> ExploitationAssessment:
    wanted = set(cves)
    relations = tuple(
        clause
        for source in sources
        for clause in source_assertions(source)
        if wanted & set(clause.cves)
    )
    # Keep every intersecting relation, including unsupported and contrary
    # joint evidence. Projection only consumes complete owned scopes.
    scopes: dict[frozenset[str], set[str]] = {}
    for clause in relations:
        scope = frozenset(clause.cves)
        if scope <= wanted:
            scopes.setdefault(scope, set()).add(clause.status)
    positive = [r for r in relations if r.status in {"active", "observed"}]
    negative = [r for r in relations if r.status == "not_observed"]
    conflict = any(set(p.cves) & set(n.cves) for p in positive for n in negative)
    projected = set()
    covered = set()
    for scope, states in scopes.items():
        covered.update(scope)
        projected.add(
            "not_observed"
            if "not_observed" in states
            else (
                "active"
                if "active" in states
                else (
                    "observed"
                    if "observed" in states
                    else "potential" if "potential" in states else "unknown"
                )
            )
        )
    status = (
        next(iter(projected))
        if not conflict and wanted and covered == wanted and len(projected) == 1
        else "unknown"
    )
    return ExploitationAssessment(
        status,
        tuple(dict.fromkeys(r.source_text for r in negative)),
        tuple(dict.fromkeys(r.source_text for r in positive)),
        conflict,
        tuple(dict.fromkeys(r.source_text for r in relations if r.unsupported)),
        relations,
    )


def _plain(text: str) -> str:
    return " ".join(text.split()).casefold()


@dataclass(frozen=True)
class VersionClause:
    kind: Literal[
        "affected",
        "unaffected",
        "audience",
        "exception",
        "recommendation",
        "information",
        "list",
    ]
    text: str


VERSION_AUDIENCE = r"customers|users|admins|administrators|operators|owners|vendors|maintainers|organizations|you"
VERSION_FINITE_PREDICATE = (
    r"\b(?:"
    + "|".join(
        sorted(
            FINITE_PREDICATE_HEADS
            | {"must", "should", "remain", "remains", "need", "needs"}
        )
    )
    + r")\b"
)
VERSION_AUDIENCE_QUALIFIER = re.compile(
    rf"(?!.*{VERSION_FINITE_PREDICATE})(?:{VERSION_AUDIENCE}) (?:only|with .+)", re.I
)
VERSION_AFFECTED_CLAUSE = re.compile(
    rf"\b(?:{VERSION_AUDIENCE}) of (?P<versions>.+?) "
    r"(?:are|were|remain) (?P<qualifiers>(?:(?:also|still|not|no longer) )*)"
    r"(?P<state>affected|impacted|vulnerable|unaffected)\b",
    re.I,
)
VERSION_RECOMMENDATION_CLAUSE = re.compile(
    rf"\b(?:{VERSION_AUDIENCE})\b.*?\b"
    r"(?:should|must|needs? to|(?:are|is) (?:advised|recommended|urged|encouraged) to) "
    r"(?:\w+ly )*(?P<verb>install|apply|patch|upgrade|update|consult|review|contact)\b.*",
    re.I,
)
VERSION_INFORMATION_CLAUSE = re.compile(
    r"\b(?:(?:further|more) )?(?:details|information)\b.*?\b(?:is|are) "
    r"(?:available|provided|published)\b.*",
    re.I,
)
VERSION_AUDIENCE_ASSERTION = re.compile(
    rf"\b(?P<audience>(?:{VERSION_AUDIENCE}) (?:only|with .+?)) "
    r"(?:are|were|remain) (?P<qualifiers>(?:(?:also|still|not|no longer) )*)"
    r"(?P<state>affected|impacted|vulnerable|unaffected)\b",
    re.I,
)
VERSION_STATE = r"affected|impacted|vulnerable|unaffected"
VERSION_DESCRIPTIVE_STATE = re.compile(
    rf"\b(?:on|for|to|in|within|across) (?:(?:all|any|the|these|those|their) )?"
    rf"(?:{VERSION_STATE}) (?:systems?|servers?|devices?|installations?|deployments?|"
    r"versions?|releases?|products?|applications?|software|platforms?|hosts?)\b(?=[.!?…]*\s*$)",
    re.I,
)


def recommendation_action(blocks: Sequence[str]) -> str:
    """Project badges from parsed source directives, retaining whole guidance."""
    parsed = [
        RecommendationBlock(
            block,
            tuple(_recommendation_directives(block)),
        )
        for block in blocks
    ]
    return project_recommendation_action(parsed)


def _version_argument_identity(text: str) -> tuple[str, ...] | None:
    """Delegate release identities/qualifiers to the existing version owner.

    This never supplies audience, modal or polarity. A typed argument may be
    used only after the directive parser establishes that separate relation.
    """
    value = text.strip(" .!?…:")
    if re.fullmatch(VERSION_LIST_CUE, value, re.I):
        return ("release",)
    cue = _version_list_cue(value)
    cue_match = re.search(VERSION_LIST_CUE, value, re.I)
    if cue and cue_match:
        if cue_match.start() == 0:
            included, excluded = _version_constraints(_version_remainder(value, cue))
            if (included or excluded) and all(
                re.search(r"\d|\bRTM\b", item) for item in (*included, *excluded)
            ):
                return ("version_scope",)
        # A later list cue belongs to a modifier of another object, not to
        # the entire argument. Let the directive structure split that owner.
        return None
    if VERSION_DESCRIPTIVE_STATE.fullmatch(value):
        return ("version_scope",)
    if re.search(CUMULATIVE_UPDATE_CUE, value, re.I):
        description = VERSION_DESCRIPTIVE_STATE.search(value)
        if description:
            value = value[: description.start()].strip()
        normalized = _version_source_text(value)
        if _cumulative_version_list(normalized):
            included, excluded = _version_constraints(normalized)
            if (
                included
                and not excluded
                and all(re.search(r"\d|\bRTM\b", item) for item in included)
            ):
                return tuple(
                    "release_scope" if description else "release" for _ in included
                )
    return None


def _recommendation_directives(block: str):
    """Keep version clauses and wrapped release arguments under their owner."""
    sentences = _sentences(block)
    index = 0
    while index < len(sentences):
        sentence = sentences[index]
        index += 1
        if (
            index < len(sentences)
            and re.search(r"\b(?:install|apply|upgrade|update)$", sentence, re.I)
            and _version_argument_identity(sentences[index])
        ):
            sentence += " " + sentences[index]
            index += 1
        cue = _version_list_cue(sentence)
        cue_match = re.search(VERSION_LIST_CUE, sentence, re.I)
        if cue and cue.kind == "explicit" and cue_match:
            remainder = _version_remainder(sentence, cue)
            if remainder:
                # The existing list owner validates following identities;
                # the directive owns only the preceding list introduction.
                _version_constraints(remainder)
                if cue_match.start():
                    yield parse_recommendation(
                        sentence[: cue.end], version_identity=_version_argument_identity
                    )
                yield None
                continue
        typed = (
            _version_clauses(sentence)
            if re.search(CUMULATIVE_UPDATE_CUE, sentence, re.I)
            else [("", VersionClause("list", sentence))]
        )
        for _, clause in typed:
            if clause.kind in {
                "affected",
                "unaffected",
                "audience",
                "exception",
                "information",
            }:
                yield None
                continue
            for unit in directive_units(clause.text):
                yield parse_recommendation(
                    unit, version_identity=_version_argument_identity
                )


@dataclass(frozen=True)
class VersionListCue:
    end: int
    kind: Literal["explicit", "pending"]


def _version_list_cue(text: str) -> VersionListCue | None:
    """Separate an actual list cue from a terminal advice description."""
    description = VERSION_DESCRIPTIVE_STATE.search(text)
    advice = VERSION_RECOMMENDATION_CLAUSE.fullmatch(text)
    information = VERSION_INFORMATION_CLAUSE.fullmatch(text)
    pending = None
    for cue in re.finditer(VERSION_LIST_CUE, text, re.I):
        if (
            description
            and (advice or information)
            and description.start() <= cue.start() < description.end()
        ):
            pending = VersionListCue(cue.end(), "pending")
            continue
        return VersionListCue(cue.end(), "explicit")
    return pending


def _version_remainder(text: str, cue: VersionListCue) -> str:
    return re.sub(
        r"^\s*(?:(?:are|is|include|includes)\b)?\s*[:=-]?\s*",
        "",
        text[cue.end :],
        flags=re.I,
    ).rstrip(". ")


def _version_assertion_is_negative(match: re.Match[str]) -> bool:
    negated = bool(re.search(r"\b(?:not|no longer)\b", match["qualifiers"], re.I))
    if negated and match["state"].casefold() == "unaffected":
        raise EvidenceError(
            "ambiguous affected-version polarity",
            code="ambiguous_affected_version_polarity",
            field="Affected Versions",
        )
    return negated or match["state"].casefold() == "unaffected"


def _version_clause(text: str) -> VersionClause:
    """Classify complete clauses before interpreting their version constraints."""
    affected = VERSION_AFFECTED_CLAUSE.fullmatch(text)
    if affected:
        return VersionClause(
            "unaffected" if _version_assertion_is_negative(affected) else "affected",
            affected["versions"],
        )
    audience = VERSION_AUDIENCE_ASSERTION.fullmatch(text)
    if audience:
        if not VERSION_AUDIENCE_QUALIFIER.fullmatch(audience["audience"]):
            raise EvidenceError(
                "ambiguous affected-version audience",
                code="ambiguous_affected_version_audience",
                field="Affected Versions",
            )
        return VersionClause(
            "exception" if _version_assertion_is_negative(audience) else "audience",
            text,
        )
    recommendation = VERSION_RECOMMENDATION_CLAUSE.fullmatch(text)
    if not recommendation:
        directive = parse_recommendation(
            text, version_identity=_version_argument_identity
        )
        # A parsed prohibition/qualified directive is still guidance, not an
        # affected-release assertion. Modality comes from the shared relation;
        # the existing version-state ambiguity checks below remain mandatory.
        recommendation = bool(directive and not directive.ambiguous)
    information = VERSION_INFORMATION_CLAUSE.fullmatch(text)
    # Only complete typed assertions above can establish a version state.
    # Advice may end with supported prepositional descriptions, but any other
    # state token is unclassified evidence, regardless of the preceding verb.
    # This deliberately rejects unknown grammar instead of treating it as
    # advice or an implicit release name.
    unclassified = (
        VERSION_DESCRIPTIVE_STATE.sub("", text)
        if recommendation or information
        else text
    )
    if re.search(rf"\b(?:{VERSION_STATE})\b", unclassified, re.I):
        raise EvidenceError(
            "ambiguous affected-version clause",
            code="ambiguous_affected_version_clause",
            field="Affected Versions",
        )
    if recommendation or information:
        # Known independent clauses were separated by _version_clauses. A
        # remaining structural boundary is ambiguous; never let the broad
        # advice/information tail swallow it based on a finite-verb vocabulary.
        if re.search(r"[;|—–]|\s/\s|\s-\s", text):
            raise EvidenceError(
                "ambiguous affected-version clause",
                code="ambiguous_affected_version_clause",
                field="Affected Versions",
            )
        return VersionClause(
            "recommendation" if recommendation else "information", text
        )
    if re.search(
        rf"\b(?:{VERSION_AUDIENCE}) (?:only\b|with\b).*{VERSION_FINITE_PREDICATE}",
        text,
        re.I,
    ):
        raise EvidenceError(
            "ambiguous affected-version audience predicate",
            code="ambiguous_affected_version_audience_predicate",
            field="Affected Versions",
        )
    # Recognizable clauses left inside a numeric fragment are not list entries.
    # Reuse the same grammar so an unknown separator cannot bypass role checks.
    if re.match(rf"(?:{VERSION_AUDIENCE}) of\b", text, re.I) or any(
        pattern.search(text)
        for pattern in (
            VERSION_AFFECTED_CLAUSE,
            VERSION_AUDIENCE_ASSERTION,
            VERSION_RECOMMENDATION_CLAUSE,
            VERSION_INFORMATION_CLAUSE,
        )
    ):
        raise EvidenceError(
            "ambiguous affected-version clause",
            code="ambiguous_affected_version_clause",
            field="Affected Versions",
        )
    return VersionClause("list", text)


def _cumulative_version_list(text: str, context: str = "") -> bool:
    """An update named by advice is not an implicit affected-release list.

    Use the same role decision for required fields and version collection.
    Context ends at this source occurrence. Advice can govern an update name
    on a following line, but cannot reach backward into preceding release rows.
    Complete version clauses keep later advice separate from list constraints.
    """
    if not re.search(CUMULATIVE_UPDATE_CUE, text, re.I):
        return False
    clauses = _version_clauses(text)
    # Explicit assertions own their role regardless of surrounding advice.
    # Context is needed only for implicit release names and wrapped targets.
    if any(
        clause.kind in {"affected", "unaffected", "audience", "exception"}
        for _, clause in clauses
    ):
        return True
    current = _plain(text)
    prior = _sentences(_plain(context or text))[-1].removesuffix(current)
    if prior and not _version_list_cue(prior):
        directive = parse_recommendation(
            prior + current, version_identity=_version_argument_identity
        )
        if directive and not directive.ambiguous:
            return False
    update = re.search(CUMULATIVE_UPDATE_CUE, current, re.I)
    advice = re.search(DETAIL_CUES["Recommended Actions"], current, re.I)
    if re.search(DETAIL_CUES["Recommended Actions"], prior, re.I) or (
        update and advice and advice.start() < update.start()
    ):
        return False
    if not re.search(r"\d|\bRTM\b", text, re.I):
        # A heading can introduce following rows; generic advice/information
        # does not establish a release list just by naming cumulative updates.
        return any(clause.kind == "list" for _, clause in clauses)
    included, excluded = _version_constraints(text)
    return bool(included or excluded)


VERSION_RANGE_QUALIFIER = re.compile(
    r"(?:(?:all|any|the|other)\s+)*(?:(?:versions?|releases?|builds?)\s+)?"
    r"(?:earlier|later|older|newer|higher|lower|above|below|before|after|prior|previous|subsequent|up|down|greater|less|lesser|onwards?|beyond|through|to)\b",
    re.I,
)


def _version_list_parts(text: str, *, attribution: bool = False) -> list[str]:
    """Retain grouped qualifiers while separating top-level release entries."""
    pairs = {"(": ")", "[": "]", "{": "}"}
    closing: list[str] = []
    parts: list[str] = []
    separator_pattern = (
        r"\s*[,;:|—–]|\s+-(?=\s)|\s+(?:and|or|for)(?=\s)"
        if attribution
        else r"[,;]|\s+(?:and|or)\s+"
    )
    start = index = 0
    while index < len(text):
        char = text[index]
        if char in pairs:
            closing.append(pairs[char])
        elif char in pairs.values():
            if not closing or closing.pop() != char:
                raise EvidenceError(
                    "ambiguous affected-version grouping",
                    code="ambiguous_affected_version_grouping",
                    field="Affected Versions",
                )
        if not closing:
            separator = re.match(separator_pattern, text[index:], re.I)
            if separator:
                end = index + separator.end()
                parts.extend((text[start:index], text[index:end]))
                start = index = end
                continue
        index += 1
    if closing:
        raise EvidenceError(
            "ambiguous affected-version grouping",
            code="ambiguous_affected_version_grouping",
            field="Affected Versions",
        )
    parts.append(text[start:])
    return parts


def _version_list_entries(text: str) -> list[str]:
    """Split constraints without detaching range tails or product names."""
    parts = _version_list_parts(text)
    entries: list[str] = []
    pending = ""
    for index in range(0, len(parts), 2):
        entry = parts[index].strip()
        if not entry:
            continue
        if pending:
            if parts[index - 1].strip().casefold() not in {"and", "or"}:
                raise EvidenceError(
                    "ambiguous affected-version continuation",
                    code="ambiguous_affected_version_continuation",
                    field="Affected Versions",
                )
            entry = pending + parts[index - 1] + entry
            pending = ""
        qualifier = VERSION_RANGE_QUALIFIER.match(entry)
        if entries and (qualifier or VERSION_AUDIENCE_QUALIFIER.fullmatch(entry)):
            entries[-1] += parts[index - 1] + entry
        elif not re.search(r"\d|\bRTM\b", entry, re.I):
            pending = entry
        else:
            entries.append(entry)
    if pending:
        raise EvidenceError(
            "ambiguous affected-version continuation",
            code="ambiguous_affected_version_continuation",
            field="Affected Versions",
        )
    return entries


def _version_clauses(text: str) -> list[tuple[str, VersionClause]]:
    """Share complete clause classification between list detection and collection."""
    if text == ABSENT:
        return []
    parts = re.split(
        r"((?:[,;—–]|\s+-\s+)\s*(?:(?:and|or|but)\s+)?|\s+(?:and|or|but)\s+)"
        rf"(?=(?:{VERSION_AUDIENCE}|(?:(?:further|more) )?(?:details|information))\b)",
        text.strip().rstrip("."),
        flags=re.I,
    )
    clauses = [("", parts[0])]
    for index in range(1, len(parts), 2):
        separator, candidate = parts[index : index + 2]
        if any(
            pattern.fullmatch(candidate.strip())
            for pattern in (
                VERSION_AFFECTED_CLAUSE,
                VERSION_AUDIENCE_ASSERTION,
                VERSION_RECOMMENDATION_CLAUSE,
                VERSION_INFORMATION_CLAUSE,
            )
        ):
            clauses.append((separator, candidate))
        else:
            # An audience restriction is part of the complete constraint.
            prefix, previous = clauses[-1]
            clauses[-1] = (prefix, previous + separator + candidate)
    return [
        (separator, _version_clause(value.strip()))
        for separator, value in clauses
        if value.strip()
    ]


def _version_constraints(
    text: str, *, require_affected: bool = False
) -> tuple[list[str], list[str]]:
    """Retain separate affected and explicitly excluded constraint sets."""
    entries: list[str] = []
    exclusions: list[str] = []
    for separator, clause in _version_clauses(text):
        if require_affected and clause.kind not in {"affected", "audience", "list"}:
            raise EvidenceError(
                "Affected Versions contains a non-affected clause",
                code="non_affected_version_clause",
                field="Affected Versions",
            )
        if clause.kind in {"affected", "list"}:
            entries.extend(_version_list_entries(clause.text))
        elif clause.kind == "audience":
            if not entries:
                raise EvidenceError(
                    "ambiguous affected-version audience",
                    code="ambiguous_affected_version_audience",
                    field="Affected Versions",
                )
            entries[-1] += separator + clause.text
        elif clause.kind == "unaffected":
            exclusions.extend(_version_list_entries(clause.text))
        elif clause.kind == "exception":
            exclusions.append(clause.text)
    return entries, exclusions


def _version_entries(text: str) -> list[str]:
    """Validate the report field without dropping any non-affected clauses."""
    return _version_constraints(text, require_affected=True)[0]


def _version_group_members(text: str) -> str:
    """Remove attribution members without inventing or duplicating connectors."""
    parts = _version_list_parts(text, attribution=True)
    retained: list[str] = []
    for index in range(0, len(parts), 2):
        member = parts[index]
        if not member.strip() or re.fullmatch(
            rf"(?:for\s+)?(?:{CVE_ID_PATTERN.pattern})", member.strip(), re.I
        ):
            continue
        if CVE_ID_PATTERN.search(member):
            raise EvidenceError(
                "ambiguous CVE attribution in version constraint",
                code="ambiguous_version_cve_attribution",
                field="Affected Versions",
            )
        if retained:
            retained.append(parts[index - 1])
        retained.append(member)
    return "".join(retained).strip()


def _version_attribution_groups(text: str) -> str:
    """Normalize nested qualifier groups while preserving their boundaries."""
    if not CVE_ID_PATTERN.search(text):
        return text
    pairs = {"(": ")", "[": "]", "{": "}"}
    pieces: list[str] = []
    start = index = 0
    while index < len(text):
        if text[index] not in pairs:
            index += 1
            continue
        closing = [pairs[text[index]]]
        end = index + 1
        while closing and end < len(text):
            char = text[end]
            if char in pairs:
                closing.append(pairs[char])
            elif char in pairs.values():
                if closing.pop() != char:
                    raise EvidenceError(
                        "ambiguous affected-version grouping",
                        code="ambiguous_affected_version_grouping",
                        field="Affected Versions",
                    )
            end += 1
        if closing:
            raise EvidenceError(
                "ambiguous affected-version grouping",
                code="ambiguous_affected_version_grouping",
                field="Affected Versions",
            )
        original = text[index + 1 : end - 1]
        content = _version_attribution_groups(original)
        if CVE_ID_PATTERN.search(original):
            content = _version_group_members(content)
        pieces.append(text[start:index])
        if content.strip():
            pieces.append(text[index] + content + text[end - 1])
        start = index = end
    pieces.append(text[start:])
    return "".join(pieces)


def _version_source_text(text: str) -> str:
    """Remove attribution tags only after detail spans have established CVE scope."""
    if not CVE_ID_PATTERN.search(text):
        return text
    text = _version_attribution_groups(text)
    text = re.sub(
        rf"(?:\s*[,;:|—–-]\s*|\s+(?:for|and|or)\s+)?(?:{CVE_ID_PATTERN.pattern})",
        " ",
        text,
        flags=re.I,
    )
    text = text.strip(" \t.,;:|—–-")
    text = re.sub(r"\bfor\s*$", "", text, flags=re.I)
    return " ".join(text.split())


def _supported_version_text(entry: str, source: str) -> bool:
    """Match full source tokens, including unknown version suffix syntax."""
    source = _plain(source)
    for match in re.finditer(
        rf"(?<![^\s,;()\[\]{{}}\"']){re.escape(_plain(entry))}", source
    ):
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


def _rendered_statements(text: str) -> list[OwnedClause]:
    # Check reader-visible Markdown text so emphasis/entities cannot split a
    # claim into a form that the evidence guard fails to recognize.
    blocks = []
    heading = False
    for token in MarkdownIt("commonmark").parse(text):
        if token.type == "heading_open":
            heading = True
        elif token.type == "heading_close":
            heading = False
        if token.type == "inline":
            if heading and token.content in {
                "Exploitation Report",
                "Active Exploitation Details",
            }:
                continue
            blocks.append(_rendered_text(token.children or []))
        elif token.type in {"fence", "code_block"}:
            blocks.append(" ".join(token.content.split()))
    text = "\n".join(blocks)
    return [
        statement
        for sentence in _sentences(text)
        for statement in parse_assertions(sentence)
    ]


def _positive_claim(text: str) -> bool:
    return any(
        statement.status in {"active", "observed"}
        for statement in _rendered_statements(text)
    )


@dataclass(frozen=True)
class FindingDetails:
    """One source interpretation shared by generation and publication."""

    spans: tuple[DetailSpan, ...]
    scoped: str
    field_evidence: Mapping[str, str]
    version_lines: tuple[str, ...]
    excluded_version_lines: tuple[str, ...]
    known_version_list: bool


def collect_finding_details(
    sources: Sequence[ReportingSource], cves: Sequence[str]
) -> FindingDetails:
    """Collect complete source constraints; ambiguous source grammar still raises."""
    detail_spans = [
        span for source in sources for span in _scoped_detail_spans(source, cves)
    ]
    # Headings guide parsing, but only body text can ground a detail value.
    scoped = "\n".join(span.text for span in detail_spans if span.role == "body")
    field_evidence = {
        name: "\n".join(
            span.text
            for span in detail_spans
            if span.role == "body" and name in span.fields
        )
        for name in DETAIL_CUES
    }
    # Version lists are easy to lose even when one supported version remains.
    version_lines = []
    excluded_version_lines = []
    list_state: Literal["none", "pending", "active"] = "none"
    known_version_list = False
    range_target: list[str] | None = None
    for span in detail_spans:
        line = _version_source_text(span.text) if span.role == "body" else span.text
        if not line and span.role == "body" and extract_cve_ids(span.text):
            continue
        if span.role != "body":
            list_state = "none"
            range_target = None
        cue = _version_list_cue(line)
        if cue and cue.kind == "pending":
            list_state = "pending"
            range_target = None
            continue
        if list_state == "pending":
            release_row = bool(re.search(r"\d|\bRTM\b", line, re.I)) and all(
                clause.kind == "list" for _, clause in _version_clauses(line)
            )
            list_state = "active" if release_row else "none"
            known_version_list = known_version_list or release_row
        cumulative_list = not cue and _cumulative_version_list(
            line, span.version_context
        )
        if (
            not cue
            and re.search(CUMULATIVE_UPDATE_CUE, line, re.I)
            and not cumulative_list
            and not (
                list_state == "active"
                and all(clause.kind == "list" for _, clause in _version_clauses(line))
            )
        ):
            list_state = "none"
            range_target = None
            continue
        if cue or cumulative_list:
            known_version_list = True
            list_state = "active"
            if span.role == "heading":
                continue
            remainder = _version_remainder(line, cue) if cue else line.rstrip(". ")
            included, excluded = _version_constraints(remainder)
            excluded_version_lines.extend(excluded)
            version_lines.extend(
                entry for entry in included if re.search(r"\d|\bRTM\b", entry)
            )
            range_target = (
                excluded_version_lines
                if excluded and not included
                else version_lines if included and not excluded else None
            )
            continue
        if list_state == "active":
            continuation = re.sub(r"^(?:and|or)\s+", "", line, flags=re.I)
            if VERSION_RANGE_QUALIFIER.match(continuation):
                if not range_target:
                    raise EvidenceError(
                        "ambiguous affected-version range continuation",
                        code="ambiguous_affected_version_range_continuation",
                        field="Affected Versions",
                    )
                range_target[-1] = (
                    range_target[-1].rstrip(". ") + " " + line.rstrip(". ")
                )
                continue
            if re.search(r"\d|\bRTM\b", line):
                included, excluded = _version_constraints(line)
                # Advice/information can contain a product version before
                # its wrapped target. End the list at that typed clause.
                list_state = "active" if included or excluded else "none"
                version_lines.extend(included)
                excluded_version_lines.extend(excluded)
                range_target = (
                    excluded_version_lines
                    if excluded and not included
                    else version_lines if included and not excluded else None
                )
            else:
                list_state = "none"
                range_target = None
    return FindingDetails(
        tuple(detail_spans),
        scoped,
        field_evidence,
        tuple(version_lines),
        tuple(excluded_version_lines),
        known_version_list,
    )


def _validate_finding(
    finding: re.Match[str],
    catalog: Mapping[str, ReportingSource],
    nonconfirmed: list[tuple[str, list[str], str]],
) -> None:
    title = finding.group("heading").removeprefix("###").strip()
    body = finding.group("body")
    pairs = FIELD.findall(body)
    fields = dict(pairs)
    if len(pairs) != len(fields):
        raise EvidenceError(
            f"{title}: duplicate finding field",
            code="duplicate_finding_field",
            expected=len(fields),
            observed=len(pairs),
        )
    keys = [key.strip() for key in fields.get("Reporting", "").split(",")]
    if not keys or any(key not in catalog for key in keys):
        raise EvidenceError(
            f"{title}: missing retained source evidence",
            code="missing_retained_source_evidence",
            field="Reporting",
            expected=True,
            observed=False,
        )
    sources = [catalog[key] for key in keys]
    if any(not source.content.strip() for source in sources):
        raise EvidenceError(
            f"{title}: missing retained source content",
            code="missing_retained_source_content",
            field="Reporting",
            expected=True,
            observed=False,
        )
    cves = extract_cve_ids(fields.get("CVE IDs", "") + " " + title)
    # Assess every supplied source naming this CVE, even when the model
    # omits that source from its chosen citations.
    relevant = list(sources)
    relevant.extend(
        source
        for source in catalog.values()
        if source not in relevant and set(cves) & set(extract_cve_ids(source.content))
    )
    assessment = assess_exploitation(relevant, cves)
    status = fields.get("Exploitation Status", "")
    allowed = {assessment.status}
    if assessment.status == "active":
        allowed.add("observed")
    if status not in allowed:
        raise EvidenceError(
            f"{title}: unsupported exploitation status {status!r}; source evidence is {assessment.status}",
            code="unsupported_exploitation_status",
            field="Exploitation Status",
            expected=assessment.status,
            observed=status or "missing",
        )
    if assessment.unsupported:
        raise EvidenceError(
            "Selected finding requires an unsupported assertion relation",
            code="unsupported_evidence_relation",
            field="Exploitation Status",
        )
    # Check narrative separately; changing only the badge cannot pass.
    narrative = FIELD.sub(
        lambda match: (
            ""
            if match.group(1) in {"Reporting", "CVE IDs", "Exploitation Status"}
            else "\n\n" + match.group(2) + "\n\n"
        ),
        body,
    )
    if any(
        statement.unsupported
        for statement in _rendered_statements(title + "\n\n" + narrative)
    ):
        raise EvidenceError(
            "Unsupported rendered exploitation claim relation",
            code="unsupported_evidence_relation",
            field="prose",
        )
    if assessment.status != "active":
        nonconfirmed.append((title, cves, assessment.status))
    if assessment.status == "observed" and any(
        statement.status == "active"
        for statement in _rendered_statements(title + "\n\n" + narrative)
    ):
        raise EvidenceError(
            f"{title}: historical observation does not establish current exploitation",
            code="unsupported_current_exploitation_claim",
            field="prose",
            expected="observed",
            observed="active",
        )
    if status not in {"active", "observed"}:
        if _positive_claim(title + "\n\n" + narrative):
            raise EvidenceError(
                f"{title}: unsupported exploitation claim in prose",
                code="unsupported_finding_exploitation_claim",
                field="prose",
                expected=False,
                observed=True,
            )
    if assessment.negative and not any(
        statement.status == "not_observed"
        for statement in _rendered_statements(narrative)
    ):
        raise EvidenceError(
            f"{title}: prose omits negative exploitation evidence",
            code="missing_negative_exploitation_evidence",
            field="prose",
            expected=True,
            observed=False,
        )
    if assessment.conflicting and not re.search(r"\bconflict\w*\b", narrative, re.I):
        raise EvidenceError(
            f"{title}: prose must disclose conflicting exploitation evidence",
            code="missing_conflicting_exploitation_evidence",
            field="prose",
            expected=True,
            observed=False,
        )
    if (
        fields.get("Action") in {"patch", "mitigate"}
        and fields.get("Recommended Actions") == ABSENT
    ):
        raise EvidenceError(
            f"{title}: action badge omits a supported recommendation",
            code="action_without_recommendation",
            field="Action",
            expected=True,
            observed=False,
        )
    details = collect_finding_details(relevant, cves)
    detail_spans = details.spans
    scoped = details.scoped
    field_evidence = details.field_evidence
    version_lines = details.version_lines
    excluded_version_lines = details.excluded_version_lines
    known_version_list = details.known_version_list
    reported_versions = {
        _plain(entry)
        for entry in _version_entries(fields.get("Affected Versions", ""))
        if fields.get("Affected Versions") != ABSENT
    }
    if any(_plain(line) not in reported_versions for line in version_lines):
        raise EvidenceError(
            f"{title}: Affected Versions omits supplied version list entries",
            code="missing_affected_version_entries",
            field="Affected Versions",
            expected=len({_plain(line) for line in version_lines}),
            observed=len(reported_versions),
        )
    if (
        known_version_list
        or re.search(CUMULATIVE_UPDATE_CUE, fields.get("Affected Versions", ""), re.I)
    ) and reported_versions - {_plain(line) for line in version_lines}:
        raise EvidenceError(
            f"{title}: unsupported affected-version entry",
            code="unsupported_affected_version_entry",
            field="Affected Versions",
            expected=len({_plain(line) for line in version_lines}),
            observed=len(reported_versions),
        )
    if any(
        not _supported_version_text(exclusion, fields.get("Exceptions", ""))
        for exclusion in excluded_version_lines
    ):
        raise EvidenceError(
            f"{title}: Exceptions omits supplied source exclusions",
            code="missing_source_exclusions",
            field="Exceptions",
            expected=True,
            observed=False,
        )
    for name in DETAIL_FIELDS:
        value = fields.get(name, "")
        if not value:
            raise EvidenceError(
                f"{title}: missing {name}; use {ABSENT!r} when absent",
                code="missing_detail_field",
                field=name,
                expected=True,
                observed=False,
            )
        if value == ABSENT:
            if (
                name == "Affected Versions"
                and known_version_list
                and excluded_version_lines
                and not version_lines
            ):
                continue
            if name in DETAIL_CUES and (
                field_evidence[name]
                or name == "Affected Versions"
                and known_version_list
            ):
                raise EvidenceError(
                    f"{title}: {name} omits supplied source details",
                    code="missing_source_details",
                    field=name,
                    expected=True,
                    observed=False,
                )
            continue
        entries = [entry.strip() for entry in value.split(";")]
        if name == "Vendor Links":
            links = {link for source in sources for link in source.links}
            try:
                normalized = [normalize_reporting_url(entry) for entry in entries]
            except ReportingGroundingError as exc:
                raise EvidenceError(
                    f"{title}: unsupported vendor link",
                    code="invalid_vendor_link",
                    field=name,
                    expected=True,
                    observed=False,
                ) from exc
            if any(entry not in links for entry in normalized):
                raise EvidenceError(
                    f"{title}: unsupported vendor link",
                    code="unsupported_vendor_link",
                    field=name,
                    expected=True,
                    observed=False,
                )
        elif name == "Recommended Actions":
            _validate_recommendation_statements(value, detail_spans)
        elif name == "Exceptions":
            for entry in entries:
                roles = detail_statement_roles(entry)
                parsed_exclusion = any(
                    _plain(entry) == _plain(item) for item in excluded_version_lines
                )
                # A phrase with no role cue can inherit one unambiguous
                # source role. Mixed-role sentences require a role-bearing
                # phrase so truncation cannot turn advice into an exception.
                grounded = (
                    any(
                        span.role == "body"
                        and name in span.fields
                        and (name in roles or span.fields == (name,))
                        and _plain(entry) in _plain(span.text)
                        for span in detail_spans
                    )
                    or parsed_exclusion
                )
                if (
                    roles and name not in roles and not parsed_exclusion
                ) or not grounded:
                    raise EvidenceError(
                        f"{title}: {name} must preserve exact source-supported details with the matching semantic role",
                        code="exception_not_grounded",
                        field=name,
                        expected=True,
                        observed=False,
                    )
        elif name == "Affected Versions":
            # Parsed lists already establish exact complete constraints above.
            # Compare that canonical representation, not raw attribution tags.
            # Without a list, grounding must enforce source token boundaries.
            if not known_version_list and any(
                not _supported_version_text(entry, scoped) for entry in entries
            ):
                raise EvidenceError(
                    f"{title}: {name} must preserve exact source-supported details",
                    code="affected_version_not_grounded",
                    field=name,
                    expected=True,
                    observed=False,
                )
        elif any(_plain(entry) not in _plain(scoped) for entry in entries):
            raise EvidenceError(
                f"{title}: {name} must preserve exact source-supported details",
                code="detail_not_grounded",
                field=name,
                expected=True,
                observed=False,
            )

    # Preserve the existing complete-detail/version gate before interpreting
    # directives. Unsupported semantics cannot mask a missing source qualifier,
    # and remain a publication blocker after exact-source grounding succeeds.
    for span in detail_spans:
        if span.role != "body" or "Recommended Actions" not in span.fields:
            continue
        for parsed in _recommendation_directives(span.source_block or span.text):
            if parsed and any(clause.unsupported for clause in parsed.clauses):
                raise EvidenceError(
                    "Selected finding requires an unsupported directive relation",
                    code="unsupported_evidence_relation",
                    field="Recommended Actions",
                )


def validate_finding_evidence(
    report: str, catalog: Mapping[str, ReportingSource]
) -> None:
    section = ACTIVE_SECTION_PATTERN.search(report)
    if not section:
        raise EvidenceError(
            "Missing finding evidence section",
            code="missing_finding_section",
            expected=True,
            observed=False,
        )
    nonconfirmed = []
    for index, finding in enumerate(
        FINDING_PATTERN.finditer(section.group("section")), start=1
    ):
        try:
            _validate_finding(finding, catalog, nonconfirmed)
        except EvidenceError as exc:
            fields = dict(FIELD.findall(finding.group("body")))
            exc.finding_index = index
            exc.cves = tuple(
                extract_cve_ids(
                    fields.get("CVE IDs", "") + " " + finding.group("heading")
                )
            )
            exc.source_keys = tuple(
                key.strip()
                for key in fields.get("Reporting", "").split(",")
                if key.strip() in catalog
            )
            exc.finding_sha256 = hashlib.sha256(finding.group().encode()).hexdigest()
            raise
    # Free-standing aggregate claims cannot safely inherit the heading's state.
    # Require explicit CVEs for confirmed claims outside finding bodies whenever
    # the report contains mixed evidence states.
    outside = report[: section.start()] + report[section.end() :]
    for statement in _rendered_statements(outside):
        if statement.unsupported:
            raise EvidenceError(
                "Unsupported exploitation claim relation in summary or cross-finding prose",
                code="unsupported_evidence_relation",
                field="summary",
            )
        if statement.status not in {"active", "observed"}:
            continue
        mentioned = set(statement.cves)
        constrained = [
            cves
            for _, cves, status in nonconfirmed
            if statement.status == "active" or status != "observed"
        ]
        if constrained and (
            not mentioned or any(mentioned & set(cves) for cves in constrained)
        ):
            raise EvidenceError(
                "Unsupported exploitation claim in summary or cross-finding prose",
                code="unsupported_summary_exploitation_claim",
                field="summary",
                expected=False,
                observed=True,
            )
