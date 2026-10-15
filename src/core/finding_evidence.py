"""Conservative, source-bound exploitation and finding detail publication checks.

Relevance is not confirmation. Ambiguous subject attribution fails closed; a
model may not discard negative evidence by selecting only a positive excerpt.
This is a bounded recognition grammar, not a general English parser.
Unrecognized constructions remain unknown and can block publication; genuine
source confirmations are not guaranteed to be recognized in every phrasing.
"""

from dataclasses import dataclass, replace
from functools import lru_cache
from itertools import groupby
import hashlib
import re
from typing import Any, Literal, Mapping, Sequence

from markdown_it import MarkdownIt
from markdown_it.token import Token

from .cve import CVE_ID_PATTERN, extract_cve_ids
from .assertions import FINITE_PREDICATE_HEADS, parse_assertions, source_qualification
from .relations import OwnedClause
from .severity import rating_relation, project_ratings
from .source_document import SourceSpan, source_document
from .source_markup import source_literal, source_literal_value, source_text_collection
from .recommendations import (
    RecommendationBlock,
    RecommendationContext,
    RecommendationDirective,
    directive_units,
    has_owned_advice_cue,
    parse_recommendation,
    recommendation_context,
    project_recommendation_action,
)
from .reporting import (
    ACTIVE_SECTION_PATTERN,
    FINDING_PATTERN,
    ReportingGroundingError,
    ReportingSource,
    parse_url_collection,
    reporting_markdown_link,
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
    # Context is occurrence-bound, ending at this fragment. A caller inspecting
    # an earlier independent clause cannot inherit a later directive's target.
    if context and not _plain(context).endswith(_plain(text)):
        context = ""
    version_cue = _version_list_cue(text)
    recommendation_text = (
        list(_recommendation_source_statements(context))[-1] if context else text
    )
    return tuple(
        name
        for name, cue in DETAIL_CUES.items()
        if (
            bool(version_cue and version_cue.kind == "explicit")
            or _cumulative_version_list(text, context)
            if name == "Affected Versions"
            else re.search(cue, text, re.I)
            or name == "Exceptions"
            and any(
                isinstance(item, RecommendationContext) and item.owner == "exception"
                for item in _recommendation_directives(recommendation_text)
            )
            or (
                name == "Recommended Actions"
                and any(
                    isinstance(item, RecommendationDirective)
                    and (
                        _plain(text).rstrip(".!?…")
                        in _plain(item.source_text).rstrip(".!?…")
                        or _plain(item.source_text).rstrip(".!?…")
                        in _plain(text).rstrip(".!?…")
                    )
                    for item in _recommendation_directives(recommendation_text)
                )
            )
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


def exploitation_state_text(assessment: ExploitationAssessment, subject: str) -> str:
    if not subject:
        # A source-owned finding has no CVE noun phrase. Use the existing
        # nominal productions; source identity is carried by its heading and
        # Reporting reference, not guessed by the assertion parser.
        if assessment.conflicting:
            return (
                "Reporting contains conflicting evidence. "
                + (
                    "Some supplied reporting states that exploitation has not been observed; "
                    if assessment.negative
                    else ""
                )
                + "the combined exploitation status is unknown."
            )
        return {
            "active": "Supplied reporting confirms active exploitation.",
            "observed": "Exploitation was observed in prior reporting. Current exploitation activity is not established by the supplied evidence.",
            "not_observed": "Supplied reporting states exploitation has not been observed.",
            "potential": "Supplied reporting describes potential exploitation.",
            "unknown": "Exploitation status is unknown from the supplied evidence.",
        }[assessment.status]
    if assessment.conflicting:
        return (
            f"Reporting contains conflicting exploitation evidence for {subject}. "
            + (
                "Some supplied reporting states that exploitation has not been observed; "
                if assessment.negative
                else ""
            )
            + "the combined exploitation status is unknown."
        )
    prose = {
        "active": f"Supplied reporting confirms active exploitation of {subject}.",
        "observed": f"{subject} exploitation was observed in prior reporting. Current exploitation activity is not established by the supplied evidence.",
        "not_observed": f"Supplied reporting states exploitation has not been observed for {subject}.",
        "potential": f"Supplied reporting describes potential exploitation of {subject}.",
        "unknown": f"Exploitation status for {subject} is unknown from the supplied evidence.",
    }[assessment.status]
    if assessment.negative and assessment.status != "not_observed":
        prose += " Some supplied reporting states exploitation has not been observed."
    return prose


def _sentences(text: str) -> list[str]:
    # An initialism's internal/full stop belongs to its token, not a new
    # subject. This is structural punctuation protection, not an abbreviation
    # vocabulary or permission to drop an unknown prefix.
    protected = {match.end() for match in re.finditer(r"\b(?:[A-Za-z]\.){2,}", text)}
    start = 0
    result = []
    for boundary in re.finditer(r"(?<=[.!?])\s+|\n+", text):
        if boundary.start() in protected:
            continue
        if text[start : boundary.start()].strip():
            result.append(text[start : boundary.start()].strip())
        start = boundary.end()
    if text[start:].strip():
        result.append(text[start:].strip())
    return result


def _value(source: Any, field: str, default=""):
    return (
        source.get(field, default)
        if isinstance(source, dict)
        else getattr(source, field, default)
    )


def source_assertions(source: Any) -> tuple[OwnedClause, ...]:
    """Interpret before selecting scope; a joint claim is never two singletons."""
    return _document_assertions(source_document(source))


@lru_cache(maxsize=128)
def _document_assertions(document) -> tuple[OwnedClause, ...]:
    """One immutable document interpretation is shared by all finding scopes."""
    source_cves = set(extract_cve_ids(document.text))
    result = []
    for span in document.spans:
        if span.role != "body":
            continue
        for sentence in _sentences(span.text):
            parsed_text = sentence
            if span.reference and span.reference_kind == "singular":
                parsed_text = re.sub(
                    r"\b(?:The|This|the|this) (?:issue|flaw|vulnerability)\b",
                    " and ".join(span.reference),
                    sentence,
                )
            elif span.reference and span.reference_kind == "group":
                parsed_text = re.sub(
                    r"^All (?:\d+|one|two|three|four|five|six|seven|eight|nine|ten) vulnerabilities\b",
                    " and ".join(span.reference),
                    sentence,
                    count=1,
                )
            if span.reference and span.reference_kind == "table_product":
                parsed_text = re.sub(
                    r"^(?:The |the )?[A-Z][\w-]*(?: [A-Z][\w-]*)* flaw\b",
                    " and ".join(span.reference),
                    sentence,
                    count=1,
                )
            for clause in parse_assertions(parsed_text):
                if clause.kind != "assertion" and not clause.unsupported:
                    continue
                if (
                    clause.context_role == "composed:source_qualification"
                    and not clause.cves
                ):
                    clause = replace(clause, cves=span.reference or span.section)
                if span.reference_kind == "forward_declared_group":
                    clause = replace(
                        clause,
                        cves=span.reference,
                        attribution=span.reference_kind,
                        unsupported=clause.unsupported or not span.reference_valid,
                    )
                if (
                    span.reference_kind == "declared_group"
                    and clause.context_role == "composed:exhaustive_list"
                ):
                    result.extend(
                        replace(
                            clause,
                            cves=(identity,),
                            source_text=sentence,
                            attribution="table_row",
                            unsupported=clause.unsupported or not span.reference_valid,
                        )
                        for identity in span.reference
                    )
                    continue
                if span.reference and parsed_text != sentence:
                    clause = replace(
                        clause,
                        cves=span.reference,
                        text=sentence,
                        attribution=span.reference_kind,
                        unsupported=clause.unsupported or not span.reference_valid,
                    )
                # Preserve the limited unscoped negative/possible legacy rule;
                # explicit local references above own positive events too.
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


def source_evidence_text(
    sources: Sequence[ReportingSource], cves: Sequence[str]
) -> str:
    """Complete attributed context for owned assertions, not an aggregate claim.

    Keep whole source sentences even when their other clauses have different
    owners or conflicting states. The same typed relations used by assessment
    determine membership; presentation cannot select away contrary evidence.
    """
    entries = []
    owned = _scope_assertions(sources, cves)
    for source in sources:
        sentences = dict.fromkeys(
            " ".join(clause.source_text.split())
            for owner, clause in owned
            if owner is source
        )
        for sentence in sentences:
            entries.append(
                f"{reporting_markdown_link('Source', source.url)}: “{source_literal(sentence)}”"
            )
    return " ".join(entries)


def _has_cve_identity(source: Any) -> bool:
    return bool(
        extract_cve_ids(str(_value(source, "content")))
        or _value(source, "metadata_cves", ())
    )


def _scope_assertions(sources: Sequence[Any], cves: Sequence[str]):
    """An empty identity is owned by one source, never the entire catalog."""
    if not cves and len(sources) > 1:
        raise EvidenceError(
            "A finding without CVEs requires one source owner",
            code="ambiguous_source_scope",
            field="Reporting",
        )
    wanted = set(cves)
    return tuple(
        (source, clause)
        for source in sources
        for clause in source_assertions(source)
        if (
            bool(wanted & set(clause.cves))
            if wanted
            else not clause.cves and not _has_cve_identity(source)
        )
    )


@dataclass(frozen=True)
class DetailSpan:
    """Keep source structure separate from factual body evidence."""

    text: str
    role: Literal["heading", "body", "boundary"]
    fields: tuple[str, ...] = ()
    source_block: str = ""
    version_context: str = ""
    table_cells: tuple[tuple[str, str], ...] = ()
    constraint_text: str = ""
    product: str = ""
    source_url: str = ""
    owned_cves: tuple[str, ...] = ()
    reference_target: tuple[str, tuple[str, ...]] | None = None
    document_list: SourceSpan | None = None


def anchored_detail_spans(spans, cves):
    """Narrow optional presentation to explicit paragraph/section ownership.

    The evidence collector intentionally retains broader article context for
    negative statements and complete detail fields. That does not make every
    page sentence a useful description of its only mentioned CVE.
    """
    wanted = set(cves)
    section_owned = False
    for span in spans:
        if span.role == "boundary":
            section_owned = False
        elif span.role == "heading":
            mentioned = set(extract_cve_ids(span.text))
            if mentioned:
                section_owned = mentioned <= wanted
        else:
            mentioned = set(extract_cve_ids(span.source_block))
            if not wanted or (
                mentioned <= wanted
                if mentioned
                else bool(span.owned_cves and set(span.owned_cves) <= wanted)
                or section_owned
            ):
                yield span


def assess_severity(spans, cves):
    """Use the same document/paragraph ownership for every rating consumer."""
    relations = []
    for span in anchored_detail_spans(spans, cves):
        for statement in _sentences(span.text):
            relation = rating_relation(
                statement,
                source_url=span.source_url,
                cves=span.owned_cves or tuple(cves),
                source_block=span.source_block or span.text,
            )
            if relation is not None and relation not in relations:
                relations.append(relation)
    return project_ratings(relations)


def severity_context_text(assessment) -> str:
    """One canonical presentation of complete owned rating statements."""
    prefix = (
        "No single unqualified severity rating is supported for this finding scope."
        if assessment.value == "unknown"
        else ""
    )
    return source_text_collection(assessment.context, prefix=prefix)


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


def _scoped_detail_spans(source: Any, cves: Sequence[str]) -> list[DetailSpan]:
    """Detail roles consume the same retained document spans as assertions."""
    document = source_document(source)
    source_cves = set(extract_cve_ids(document.text))
    wanted = set(cves)
    if not wanted and source_cves:
        return [DetailSpan("", "boundary")]
    has_cve_sections = any(
        span.kind == "heading"
        and (span.identities or span.section)
        or span.headings
        and span.section
        for span in document.spans
    )
    result = [DetailSpan("", "boundary")]
    for index, block in enumerate(document.spans):
        if block.role == "table_row":
            owner = set(block.identities or block.reference or block.section)
            if owner and owner <= wanted or not wanted and not source_cves:
                release_table = any(
                    re.search(r"\b(?:versions?|releases?|fixed|fixes)\b", header, re.I)
                    for header in block.headers
                )
                if not release_table:
                    # Layout and other non-release tables remain retained
                    # context; their cells cannot acquire version roles.
                    continue
                if not block.headers or len(block.headers) != len(block.cells):
                    raise EvidenceError(
                        "Required release table lacks column provenance",
                        code="unsupported_evidence_relation",
                        field="Affected Versions",
                    )
                result.append(
                    DetailSpan(
                        block.text,
                        "body",
                        (),
                        block.text,
                        table_cells=tuple(zip(block.headers, block.cells)),
                    )
                )
            continue
        if block.role not in {"body", "heading"}:
            result.append(DetailSpan("", "boundary"))
            continue
        owner = set(block.reference or block.section)
        if not block.reference_valid and (
            not wanted
            or owner & wanted
            or block.reference_kind == "listed_group"
            and not owner
            and source_cves & wanted
        ):
            raise EvidenceError(
                "Required source reference is ambiguous",
                code="unsupported_evidence_relation",
                field="Reporting",
            )
        owned = not wanted or bool(
            owner
            and owner <= wanted
            or block.reference_kind in {"table_note", "listed_group"}
            and owner & wanted
            or not owner
            and not has_cve_sections
            and source_cves
            and source_cves <= wanted
        )
        if block.kind == "heading":
            result.append(
                DetailSpan(re.sub(r"^#+\s*", "", block.text), "heading")
                if owned
                else DetailSpan("", "boundary")
            )
            continue
        if owned and not block.reference_valid:
            raise EvidenceError(
                "Required source reference is ambiguous",
                code="unsupported_evidence_relation",
                field="Reporting",
            )
        qualification = source_qualification(block.text) if owned else None
        if qualification and qualification.unsupported:
            raise EvidenceError(
                "Required source qualification is unsupported",
                code="unsupported_evidence_relation",
                field="Source Constraints",
            )
        if owned and block.constraint_text:
            result.append(
                DetailSpan(
                    block.text,
                    "body",
                    (),
                    block.text,
                    constraint_text=block.constraint_text,
                    product=block.product,
                    source_url=_value(source, "url"),
                )
            )
        elif owned and (
            qualification
            or any(
                clause.kind == "context"
                and clause.modal == "capability"
                and not clause.unsupported
                for sentence in _sentences(block.text)
                for clause in parse_assertions(sentence)
            )
        ):
            # A prerequisite is required context, not contrary observation.
            # Preserve its complete source paragraph independently of optional
            # model-selected excerpts, using the existing constraint gate.
            result.append(
                DetailSpan(
                    block.text,
                    "body",
                    (),
                    block.text,
                    constraint_text=block.text,
                    source_url=_value(source, "url"),
                    owned_cves=tuple(sorted(owner)),
                )
            )
        if owned and block.list_role:
            detail = DetailSpan(
                block.text,
                "body",
                (
                    ("Recommended Actions",)
                    if block.list_role in {"destination", "audience"}
                    else ()
                ),
                block.text,
                source_url=_value(source, "url"),
                document_list=block,
            )
            if block.list_role == "audience" and any(
                isinstance(item, RecommendationContext) and item.owner == "exception"
                for item in _source_recommendation_block(detail).directives
            ):
                detail = replace(detail, fields=(*detail.fields, "Exceptions"))
            result.append(detail)
            continue
        if re.fullmatch(r"The table shows affected and fixed versions\.", block.text):
            following = document.spans[index + 1 : index + 2]
            if not following or following[0].role != "table_header":
                raise EvidenceError(
                    "Required release table lacks column provenance",
                    code="unsupported_evidence_relation",
                    field="Affected Versions",
                )
            continue
        preceding = []
        for line in block.text.splitlines():
            body_line = re.sub(r"^\s*(?:[-+*]|\d+[.)])\s+", "", line)
            for sentence in _sentences(body_line):
                preceding.append(sentence)
                version_context = "\n".join(preceding)
                mentioned = set(extract_cve_ids(sentence))
                selected = mentioned <= wanted if mentioned and wanted else owned
                # Ownership precedes version/advice interpretation. An unrelated
                # product's required grammar cannot contaminate a selected CVE.
                if not selected:
                    result.append(DetailSpan("", "boundary"))
                    continue
                fields = detail_statement_roles(sentence, version_context) or next(
                    (
                        roles
                        for title in reversed(block.headings)
                        if (roles := _heading_detail_roles(title))
                    ),
                    (),
                )
                if re.search(
                    DETAIL_CUES["Recommended Actions"],
                    " ".join(block.text.split()),
                    re.I,
                ):
                    fields = tuple(dict.fromkeys((*fields, "Recommended Actions")))
                if block.reference_kind == "listed_group" and any(
                    isinstance(item, RecommendationDirective)
                    for item in _recommendation_directives(
                        block.text, (block.reference_text, block.reference)
                    )
                ):
                    fields = tuple(dict.fromkeys((*fields, "Recommended Actions")))
                if (
                    "Recommended Actions" in fields
                    and wanted
                    and not set(extract_cve_ids(block.text)) <= wanted
                ):
                    raise EvidenceError(
                        "ambiguous recommendation block CVE scope",
                        code="ambiguous_recommendation_scope",
                        field="Recommended Actions",
                    )
                narrative_owner = (
                    mentioned
                    or set(block.reference)
                    or (
                        owner
                        if any(extract_cve_ids(title) for title in block.headings)
                        else set()
                    )
                )
                result.append(
                    DetailSpan(
                        sentence,
                        "body",
                        fields,
                        block.text,
                        version_context,
                        source_url=_value(source, "url"),
                        owned_cves=tuple(sorted(narrative_owner)),
                        reference_target=(
                            (block.reference_text, block.reference)
                            if block.reference_kind == "listed_group"
                            else None
                        ),
                    )
                )
    return result


def build_finding_detail_context(
    catalog: Mapping[str, ReportingSource],
    *,
    owned_spans: (
        dict[tuple[str, tuple[str, ...]], tuple[DetailSpan, ...]] | None
    ) = None,
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
        for block in dict.fromkeys(span.text for span in source_document(source).spans):
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
            scope_key = (cves, source.key if not cves else None)
            if scope_key not in assessments:
                assessments[scope_key] = assess_exploitation(
                    list(catalog.values()) if cves else [source], cves
                )
            assessment = assessments[scope_key]
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
                if owned_spans is not None:
                    owned_spans[source.key, cves] = tuple(spans)
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
                "Source Evidence",
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
    relations = tuple(clause for _, clause in _scope_assertions(sources, cves))
    # Keep every intersecting relation, including unsupported and contrary
    # joint evidence. Projection only consumes complete owned scopes.
    scopes: dict[frozenset[str], set[str]] = {}
    for clause in relations:
        scope = frozenset(clause.cves)
        if scope <= wanted:
            scopes.setdefault(scope, set()).add(clause.status)
    positive = [r for r in relations if r.status in {"active", "observed"}]
    negative = [r for r in relations if r.status == "not_observed"]
    conflict = any(
        not wanted or set(p.cves) & set(n.cves) for p in positive for n in negative
    )
    conflict |= any(
        p.status in constraint.assertion_projection.excludes
        and (not wanted or bool(set(p.cves) & set(constraint.cves)))
        for p in positive
        for constraint in relations
    )
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
        if not conflict and relations and covered == wanted and len(projected) == 1
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
    if re.fullmatch(
        r"(?:a |the )?supported version of (?:[A-Z][A-Za-z0-9-]* ?){1,4}(?: client or (?:[A-Z][A-Za-z0-9-]* )?[Ss]erver)?",
        value,
    ):
        return ("release",)
    if re.fullmatch(r"(?:the )?recommended (?:[A-Z][A-Za-z0-9-]* )?versions", value):
        return ("release",)
    if re.fullmatch(r"Other [A-Z][A-Za-z0-9-]* versions", value):
        return ("version_scope",)
    if re.fullmatch(r"(?:a |the )?fixed version|[A-Z][A-Za-z0-9-]* releases", value):
        return ("release",)
    if re.fullmatch(
        r"(?:the )?(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{4} security update(?: or later)?",
        value,
    ):
        included, excluded = _version_constraints(value)
        if included and not excluded:
            return ("release",)
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


def _owned_recommendation(unit: str, reference_target=None, audience_reference=""):
    if context := recommendation_context(unit):
        return context
    parsed = parse_recommendation(
        unit,
        version_identity=_version_argument_identity,
        reference_target=reference_target,
        audience_reference=audience_reference,
    )
    if parsed is not None:
        return parsed
    if (
        has_owned_advice_cue(unit)
        or re.search(DETAIL_CUES["Recommended Actions"], unit, re.I)
        or any(
            parse_recommendation(fragment, version_identity=_version_argument_identity)
            is not None
            for fragment in _sentences(unit)
        )
    ):
        return RecommendationDirective(
            unit,
            "unclassified",
            (OwnedClause(text=unit, kind="directive", unsupported=True),),
            (),
            True,
        )
    return RecommendationContext(unit, "narrative")


def _complete_recommendation_fragment(text: str) -> bool:
    """Only an existing owner can certify a source-statement boundary.

    A nominal prefix, incomplete audience/modal or incomplete argument stays
    with its continuation. Punctuation alone cannot turn that continuation into
    an independent imperative. Version identities and roles retain their own
    row boundaries before physical recommendation wraps are joined.
    """
    if recommendation_context(text):
        return True
    parsed = parse_recommendation(text, version_identity=_version_argument_identity)
    if parsed is not None:
        # Qualified advice may legally omit a target. A physical wrap alone
        # cannot certify that omission when the target can follow on the next
        # line; explicit terminal punctuation can close the implicit relation.
        return not parsed.ambiguous and (
            text.endswith((".", "!", "?"))
            or all(clause.object_role != "implicit" for clause in parsed.clauses)
        )
    if re.search(DETAIL_CUES["Recommended Actions"], text, re.I):
        return False
    cue = _version_list_cue(text)
    if cue and cue.kind == "explicit":
        return True
    if re.search(CUMULATIVE_UPDATE_CUE, text, re.I):
        clauses = _version_clauses(text)
        if all(clause.kind not in {"list", "recommendation"} for _, clause in clauses):
            return True
        if _version_argument_identity(text):
            return True
    return any(
        clause.kind == "assertion" or clause.attribution == "explicit"
        for clause in parse_assertions(text)
    )


def _recommendation_source_statements(block: str):
    """Preserve typed rows and whole unclassified prefixes in source order."""
    pending = ""
    for fragment in _sentences(block):
        pending = f"{pending} {fragment}".strip()
        if _complete_recommendation_fragment(pending):
            yield pending
            pending = ""
    if pending:
        yield pending


def _recommendation_directives(
    block: str, reference_target=None, audience_reference=""
):
    """Keep version clauses and wrapped release arguments under their owner."""
    for sentence in _recommendation_source_statements(block):
        cue = _version_list_cue(sentence)
        cue_match = re.search(VERSION_LIST_CUE, sentence, re.I)
        if cue and cue.kind == "explicit" and cue_match:
            remainder = _version_remainder(sentence, cue)
            if remainder:
                # The existing list owner validates following identities;
                # the directive owns only the preceding list introduction.
                _version_constraints(remainder)
                if cue_match.start():
                    yield _owned_recommendation(sentence[: cue.end], reference_target)
                yield RecommendationContext(remainder, "version")
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
                yield RecommendationContext(clause.text, "version")
                continue
            for unit in directive_units(clause.text):
                yield _owned_recommendation(unit, reference_target, audience_reference)


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
    statements = list(_recommendation_source_statements(context)) if context else [text]
    prior = _plain(statements[-1]).removesuffix(current)
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
                if (
                    not attribution
                    and separator.group().strip().lower() == "and"
                    and re.search(
                        r"\bbetween\s+\d[\w.-]*(?: (?:\d[\w.-]*|[A-Z][A-Z0-9-]*))*\s*$",
                        text[start:index],
                    )
                    and re.match(r"\s*\d", text[index + separator.end() :])
                ):
                    index += separator.end()
                    continue
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
        exclusion = re.fullmatch(r"but not including \d[\w.-]*", entry, re.I)
        endpoint = r"\d[\w.-]*(?: (?:\d[\w.-]*|[A-Z][A-Z0-9-]*))*"
        inclusive = (
            entries
            and re.search(rf"\bbetween\s+{endpoint}\s+and\s+{endpoint}$", entries[-1])
            and re.fullmatch(r"inclusive", entry, re.I)
        )
        qualifier = VERSION_RANGE_QUALIFIER.match(entry) or exclusion or inclusive
        if entries and (qualifier or VERSION_AUDIENCE_QUALIFIER.fullmatch(entry)):
            entries[-1] += parts[index - 1] + (
                parts[index] if exclusion or inclusive else entry
            )
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
    # Reader-visible paragraphs keep the same explicit/local reference owners
    # as source paragraphs. No second pronoun or temporal interpreter is used.
    return list(source_assertions({"content": "\n\n".join(blocks)}))


def _positive_claim(text: str) -> bool:
    return any(
        statement.status in {"active", "observed"}
        for statement in _rendered_statements(text)
    )


def _validate_scope_claims(statements, assessment, cves, *, field="prose"):
    """Qualified denials require complete owned wording, even at unknown."""
    qualified_context = any(
        r.assertion_projection.qualified_denial for r in assessment.relations
    )
    checked = [
        statement
        for statement in statements
        if statement.assertion_projection.qualified_denial
        or qualified_context
        and statement.status in {"active", "observed"}
    ]
    if not checked:
        return
    owned = {_plain(r.source_text) for r in assessment.relations}
    canonical = {
        _plain(r.source_text)
        for r in _rendered_statements(
            exploitation_state_text(assessment, ", ".join(cves))
        )
    }
    if any(
        _plain(statement.source_text) not in owned | canonical for statement in checked
    ):
        raise EvidenceError(
            "Unsupported or incomplete qualified exploitation claim in prose",
            code="unsupported_finding_exploitation_claim",
            field=field,
            expected=False,
            observed=True,
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
    release_details: tuple[str, ...] = ()
    source_constraints: tuple[str, ...] = ()
    constraint_evidence: tuple[tuple[str, str], ...] = ()
    recommendation_blocks: tuple[RecommendationBlock, ...] = ()


def source_constraint_text(details: FindingDetails) -> str:
    return (
        " ".join(
            f"{reporting_markdown_link('Source', url)}: “{source_literal(text)}”"
            for url, text in dict.fromkeys(details.constraint_evidence)
        )
        or ABSENT
    )


def _document_release_identity(value: str) -> tuple[str, ...] | None:
    """A DOM release-list role supplies identity context, never an action.

    Called only for a typed list row/audience. Ordinary narrative and directive
    fragments cannot enter the version list owner merely by containing digits.
    """
    if generic := _version_argument_identity(value):
        return generic
    if re.search(r"\d", value) and all(
        clause.kind == "list" for _, clause in _version_clauses(value)
    ):
        included, excluded = _version_constraints(value)
        if included and not excluded:
            return ("release",)
    return None


def _source_recommendation_block(
    span: DetailSpan, audience_reference=""
) -> RecommendationBlock:
    """Compile a document-owned list once into the existing directive owner."""
    if not (block := span.document_list):
        return RecommendationBlock(
            span.source_block or span.text,
            tuple(
                _recommendation_directives(
                    span.source_block or span.text,
                    span.reference_target,
                    audience_reference,
                )
            ),
        )
    parsed = None
    if block.list_role == "destination":
        identities = {
            value: _document_release_identity(value) for value in block.list_members
        }
        parsed = parse_recommendation(
            block.list_intro,
            version_identity=lambda value: identities.get(value)
            or _version_argument_identity(value),
            release_destinations=block.list_members,
        )
    elif block.list_role == "audience":
        prefix, separator, body = block.text.partition(":")
        if separator and _document_release_identity(prefix):
            if body.strip() == "No action is required.":
                return RecommendationBlock(
                    block.text, (RecommendationContext(block.text, "exception"),)
                )
            parsed = parse_recommendation(
                body.strip(),
                version_identity=_version_argument_identity,
                release_audience=prefix,
            )
    if parsed is None:
        parsed = RecommendationDirective(
            block.text,
            "unclassified",
            (OwnedClause(text=block.text, kind="directive", unsupported=True),),
            (),
            True,
        )
    return RecommendationBlock(block.text, (replace(parsed, source_text=block.text),))


def _source_recommendation_blocks(spans):
    """A pronoun can use only the immediately preceding unique advice audience."""
    result = []
    audience = ""
    for _, grouped in groupby(spans, lambda span: span.source_block or span.text):
        group = list(grouped)
        selected = next(
            (
                span
                for span in group
                if span.role == "body" and "Recommended Actions" in span.fields
            ),
            None,
        )
        if selected is None:
            audience = ""
            continue
        block = _source_recommendation_block(selected, audience)
        result.append(block)
        subjects = {
            clause.subject
            for directive in block.directives
            if isinstance(directive, RecommendationDirective)
            and not directive.ambiguous
            for clause in directive.clauses
            if clause.subject
        }
        audience = next(iter(subjects)) if len(subjects) == 1 else ""
    return tuple(dict.fromkeys(result))


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
    release_details = []
    source_constraints = []
    constraint_evidence = []
    list_state: Literal["none", "pending", "active"] = "none"
    known_version_list = False
    range_target: list[str] | None = None
    for span in detail_spans:
        if block := span.document_list:
            list_state = "none"
            range_target = None
            if block.list_role in {"destination", "audience"}:
                continue
            known_version_list |= block.list_role == "affected"
            for member in block.list_items:
                condition = ""
                values = [member.text]
                if member.children:
                    prefix = member.text[
                        : member.children[0].start - member.start
                    ].strip(" :-")
                    if not re.fullmatch(
                        r"When configured as a (?:[A-Z][A-Za-z0-9-]* )(?:IdP|SP)(?: or (?:[A-Z][A-Za-z0-9-]* )(?:IdP|SP))?",
                        prefix,
                    ):
                        raise EvidenceError(
                            "Unsupported qualified release list",
                            code="unsupported_evidence_relation",
                            field="Affected Versions",
                        )
                    condition = prefix
                    values = [child.text for child in member.children]
                    source_constraints.append(member.text)
                    constraint_evidence.append((span.source_url, member.text))
                for value in values:
                    if not _document_release_identity(value):
                        raise EvidenceError(
                            "Unsupported release list identity",
                            code="unsupported_evidence_relation",
                            field="Affected Versions",
                        )
                    included, excluded = _version_constraints(value)
                    label = (
                        "Affected Versions"
                        if block.list_role == "affected"
                        else "Fixed Versions"
                    )
                    release_details.append(
                        (f"Condition: {condition} | " if condition else "")
                        + label
                        + ": "
                        + value
                    )
                    if block.list_role == "affected":
                        version_lines.extend(included)
                        excluded_version_lines.extend(excluded)
            continue
        if span.constraint_text:
            source_constraints.append(span.constraint_text)
            constraint_evidence.append((span.source_url, span.constraint_text))
            # The document owner supplies the product/row reference. The
            # existing version owner still parses the complete range, including
            # exclusions, without treating a fixed release as affected.
            wider = re.fullmatch(
                r"[^.!?]+(?:'s|’s) own advisory gives a wider range than the joint advisory\. It says versions (?P<range>.+), are affected\.",
                span.constraint_text,
            )
            if wider:
                included, excluded = _version_constraints(
                    f"{span.product} {wider['range']}"
                )
                version_lines.extend(included)
                excluded_version_lines.extend(excluded)
                known_version_list = True
            list_state = "none"
            range_target = None
            continue
        if span.table_cells:
            list_state = "none"
            range_target = None
            product = next(
                (
                    value
                    for header, value in span.table_cells
                    if header.casefold() == "product"
                ),
                "",
            )
            row_labels = []
            for header, value in span.table_cells:
                label = header.casefold()
                if label in {"affected versions", "affected versions in the advisory"}:
                    included, excluded = _version_constraints(
                        " ".join(filter(None, (product, value)))
                    )
                    version_lines.extend(included)
                    excluded_version_lines.extend(excluded)
                    known_version_list = True
                row_labels.append(f"{header}: {value}")
            release_details.append(" | ".join(row_labels))
            continue
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
        tuple(release_details),
        tuple(source_constraints),
        tuple(constraint_evidence),
        _source_recommendation_blocks(detail_spans),
    )


def _validate_finding(
    finding: re.Match[str],
    catalog: Mapping[str, ReportingSource],
    nonconfirmed: list[tuple[str, list[str], str]],
) -> None:
    title = finding.group("heading").removeprefix("###").strip()
    body = finding.group("body")
    pairs = FIELD.findall(body)
    fields = {
        name: (
            source_literal_value(value)
            if name
            in {
                "Affected Versions",
                "Exceptions",
                "Recommended Actions",
                "Release Details",
            }
            else value
        )
        for name, value in pairs
    }
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
    # Conflicts and independent clauses in shared sentences need their whole
    # attributed context. Exact source/context equality is checked before this
    # field is separated from the report's own narrative claims. Legacy simple
    # findings remain readable; newly compiled records always carry this field.
    context_required = assessment.conflicting or any(
        clause.assertion_projection.qualified_denial
        or set(extract_cve_ids(clause.source_text)) - set(cves)
        for clause in assessment.relations
    )
    if "Source Evidence" in fields:
        expected_context = source_evidence_text(relevant, cves)
        if not expected_context or fields.get("Source Evidence") != expected_context:
            raise EvidenceError(
                "Finding must retain complete attributed source evidence",
                code="incomplete_source_evidence",
                field="Source Evidence",
                expected=True,
                observed=False,
            )
    details = collect_finding_details(relevant, cves)
    if "Severity Context" in fields and fields[
        "Severity Context"
    ] != severity_context_text(assess_severity(details.spans, cves)):
        raise EvidenceError(
            "Severity context must retain canonical complete source statements",
            code="severity_context_not_grounded",
            field="Severity Context",
        )
    if fields.get("Source Constraints", ABSENT) != source_constraint_text(details):
        raise EvidenceError(
            "Finding must retain complete attributed source constraints",
            code="source_constraints_not_grounded",
            field="Source Constraints",
        )
    # Guidance has source-owned paragraph/list/quotation boundaries. Validate
    # the complete serialized field first, then use those same owned relations;
    # do not reinterpret semicolon-joined display text as an invented sentence.
    guidance_relations = ()
    guidance_owned = False
    if fields.get("Recommended Actions", ABSENT) != ABSENT:
        try:
            _validate_recommendation_statements(
                fields["Recommended Actions"], details.spans
            )
        except EvidenceError:
            # Unowned output remains narrative here and reaches the existing
            # complete-detail rejection below; preserve diagnostic precedence.
            pass
        else:
            guidance_owned = True
            guidance_relations = tuple(
                clause
                for clause in assessment.relations
                if any(
                    _plain(clause.source_text or clause.text)
                    in _plain(block.source_text)
                    for block in details.recommendation_blocks
                )
            )
    # Check narrative separately; changing only the badge cannot pass.
    narrative = FIELD.sub(
        lambda match: (
            ""
            if match.group(1)
            in {
                "Reporting",
                "CVE IDs",
                "Exploitation Status",
                "Source Evidence",
                "Source Constraints",
            }
            or guidance_owned
            and match.group(1) == "Recommended Actions"
            else "\n\n" + match.group(2) + "\n\n"
        ),
        body,
    )
    if not cves and extract_cve_ids(narrative):
        raise EvidenceError(
            "Source-only narrative cannot introduce a CVE-owned claim",
            code="ambiguous_source_scope",
            field="prose",
        )
    statements = _rendered_statements(title + "\n\n" + narrative)
    if any(statement.unsupported for statement in statements):
        raise EvidenceError(
            "Unsupported rendered exploitation claim relation",
            code="unsupported_evidence_relation",
            field="prose",
        )
    _validate_scope_claims(statements, assessment, cves)
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
        for statement in (*_rendered_statements(narrative), *guidance_relations)
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
    if context_required and "Source Evidence" not in fields:
        raise EvidenceError(
            "Finding must retain complete attributed source evidence",
            code="incomplete_source_evidence",
            field="Source Evidence",
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
    detail_spans = details.spans
    scoped = details.scoped
    field_evidence = details.field_evidence
    version_lines = details.version_lines
    excluded_version_lines = details.excluded_version_lines
    known_version_list = details.known_version_list
    if fields.get("Release Details", ABSENT) != (
        "; ".join(dict.fromkeys(details.release_details)) or ABSENT
    ):
        raise EvidenceError(
            "Release details must retain complete source-owned column labels and values",
            code="release_details_not_grounded",
            field="Release Details",
        )
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
                normalized = parse_url_collection(value)
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
                owned_list_exception = any(
                    span.document_list is not None
                    and name in span.fields
                    and _plain(entry) == _plain(span.text)
                    for span in detail_spans
                )
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
                    or owned_list_exception
                )
                if (
                    roles
                    and name not in roles
                    and not parsed_exclusion
                    and not owned_list_exception
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
    for block in details.recommendation_blocks:
        for parsed in block.directives:
            if isinstance(parsed, RecommendationDirective) and any(
                clause.unsupported for clause in parsed.clauses
            ):
                raise EvidenceError(
                    "Selected finding requires an unsupported directive relation",
                    code="unsupported_evidence_relation",
                    field="Recommended Actions",
                )
    if not cves and any(_has_cve_identity(source) for source in sources):
        raise EvidenceError(
            "A CVE-owned source cannot replace a source-only finding owner",
            code="ambiguous_source_scope",
            field="Reporting",
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
    findings = list(FINDING_PATTERN.finditer(section.group("section")))
    for index, finding in enumerate(findings, start=1):
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
    # An explicit heading reference binds a rollup to the same complete finding
    # gate. The heading is a structural owner, not a prefix of the source
    # sentence; flattening it into prose breaks owned group/reporter clauses.
    source_findings: dict[str, list[re.Match[str]]] = {}
    for finding in findings:
        title = finding.group("heading").removeprefix("###").strip()
        source_findings.setdefault(title, []).append(finding)

    def validate_owned_row(match: re.Match[str]) -> str:
        owners = source_findings.get(match[1], [])
        if not owners:
            return match[0]
        if len(owners) != 1:
            raise EvidenceError(
                "Ambiguous source finding reference", code="ambiguous_source_scope"
            )
        owner_fields = dict(FIELD.findall(owners[0].group("body")))
        owner_cves = set(
            extract_cve_ids(match[1] + " " + owner_fields.get("CVE IDs", ""))
        )
        if not set(extract_cve_ids(match[2])) <= owner_cves:
            raise EvidenceError(
                "A rollup cannot introduce another finding's CVE scope",
                code="ambiguous_source_scope",
                field="summary",
            )
        augmented = FINDING_PATTERN.search(
            owners[0].group().rstrip() + "\n- **Summary Context**: " + match[2] + "\n"
        )
        assert augmented is not None
        _validate_finding(augmented, catalog, [])
        return ""

    outside = re.sub(
        r"^- \*\*([^\n]+)\*\*: ([^\n]+)$", validate_owned_row, outside, flags=re.M
    )
    for statement in _rendered_statements(outside):
        if statement.unsupported:
            raise EvidenceError(
                "Unsupported exploitation claim relation in summary or cross-finding prose",
                code="unsupported_evidence_relation",
                field="summary",
            )
        if statement.cves:
            assessment = assess_exploitation(list(catalog.values()), statement.cves)
            _validate_scope_claims(
                [statement], assessment, statement.cves, field="summary"
            )
        elif statement.assertion_projection.qualified_denial:
            raise EvidenceError(
                "A qualified exploitation claim requires an explicit source owner",
                code="unsupported_summary_exploitation_claim",
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
