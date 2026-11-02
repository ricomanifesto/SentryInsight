"""Resolve model-selected version references to source-owned constraints.

This is an internal generation protocol. Published reports still contain the
schema-4 evidence state and must pass source-bound grounding validation.
"""

from dataclasses import asdict, dataclass
import hashlib
import json
import re
from typing import Any, Mapping, Sequence

from .cve import CVE_ID_PATTERN, extract_cve_ids
from .finding_evidence import (
    ABSENT,
    FIELD,
    DetailSpan,
    EvidenceError,
    VERSION_FINITE_PREDICATE,
    VERSION_STATE,
    _partition_detail_spans,
    _plain,
    _version_clauses,
    _version_constraints,
    _version_entries,
    _version_list_cue,
    _version_source_text,
    build_finding_detail_context,
    collect_affected_version_constraints,
)
from .reporting import (
    ACTIVE_SECTION_PATTERN,
    FINDING_PATTERN,
    ReportingSource,
    deserialize_reporting_catalog,
)
from .report_validation import prepare_generated_report
from .version_state import STATE_FIELD, UNRESOLVED, VersionEvidenceStatus

PROTOCOL_VERSION = 2
PROTOCOL_KEY = "version_reference_protocol"
VERSION_FIELD = re.compile(
    r"^(?P<prefix>-[ \t]+\*\*Affected Versions\*\*:[ \t]*)(?P<value>[^\r\n]*)$",
    re.MULTILINE,
)
REFERENCE = re.compile(r"(?:unresolved-version|version)-[0-9a-f]{32}")
VERSION_SHAPE = re.compile(
    r"\b(?:v\d+|\d+(?:\.(?:\d+|x|\*))+(?:[a-z][\w.-]*)?|\d+[ru]\d[\w.-]*|"
    r"(?:CU|SP)\s*\d+|RTM|(?:versions?|releases?|builds?)\s+[^.!?]*\d|"
    r"(?:all|any|earlier|older|prior|previous)\s+[^.!?]*\b(?:versions?|releases?|builds?))(?=$|\W)",
    re.I,
)
BARE_MAJOR_RELEASE = re.compile(r"(?:[a-z][\w+/-]*\s+){1,8}\d+(?:\s*\(.*\))?", re.I)
CVSS_SCORE = re.compile(
    r"\bCVSS(?:\s+v?\d+(?:\.\d+)?)?(?:\s+(?:base\s+)?(?:score|rating))?"
    r"\s*(?:of\s+|:\s*)?\d+(?:\.\d+)?\b",
    re.I,
)
SCALED_QUANTITY = re.compile(
    r"(?<![\w.])\d+(?:\.\d+)?\s+(?:thousand|million|billion|trillion)\b", re.I
)
VERSION_LABEL = re.compile(r"\b(?:versions?|releases?|builds?)\b", re.I)
TARGET_ASSERTION = re.compile(r"\b(?:targets?|targeted|targeting)\b", re.I)
FIXED_RELEASE = re.compile(
    r"(?:(?:the (?:flaw|issue|vulnerability) )?(?:was|is|has been) )?"
    r"(?:fixed|patched|addressed|resolved) in (.+)",
    re.I,
)


def _reject(code: str, message: str) -> EvidenceError:
    # Messages never contain a candidate value, source text, title or URL.
    return EvidenceError(message, code=code, field="Affected Versions")


@dataclass(frozen=True)
class VersionConstraint:
    id: str
    source_key: str
    content_sha256: str
    text: str


@dataclass(frozen=True)
class UnresolvedVersionReference:
    id: str
    source_key: str
    content_sha256: str
    span_sha256: str
    reason: str = "unclassified_numeric_prose"


@dataclass(frozen=True)
class VersionScope:
    cves: tuple[str, ...]
    source_keys: tuple[str, ...]
    constraints: tuple[VersionConstraint, ...]
    blocked: bool
    unresolved_references: tuple[UnresolvedVersionReference, ...] = ()
    failure_reasons: tuple[str, ...] = ()

    @property
    def absence_allowed(self) -> bool:
        return (
            not self.blocked and not self.constraints and not self.unresolved_references
        )

    @property
    def unresolved_allowed(self) -> bool:
        return (
            not self.blocked
            and not self.cves
            and not self.constraints
            and bool(self.unresolved_references)
        )

    @property
    def state(self) -> str:
        if self.blocked:
            return "blocked"
        if self.unresolved_allowed:
            return VersionEvidenceStatus.UNRESOLVED.value
        if self.constraints:
            return VersionEvidenceStatus.SUPPORTED.value
        return VersionEvidenceStatus.NOT_STATED.value

    def context(self) -> dict[str, Any]:
        return {
            "cves": list(self.cves),
            "source_keys": list(self.source_keys),
            "constraints": [asdict(item) for item in self.constraints],
            "absence_allowed": self.absence_allowed,
            "blocked": self.blocked,
            "state": self.state,
            "unresolved_allowed": self.unresolved_allowed,
            "unresolved_references": [
                asdict(item) for item in self.unresolved_references
            ],
            "failure_reasons": list(self.failure_reasons),
        }


def _is_event_count_narrative(text: str) -> bool:
    """Recognize one positive narrative form, never infer prose from a stray verb.

    An attributed event followed by a counted-device observation has explicit
    clause ownership. Every other unclassified form stays blocked. This does
    not classify the event's numbered entity or claim affected-version absence.
    Original text still owns all constraints, qualifications and parse errors.
    """
    return bool(
        re.fullmatch(
            r"(?:when|after|before|while|once|since)\s+"
            r"(?:[a-z][a-z'-]*\s+){1,6}"
            r"(?:reported|disclosed|described|disrupted|investigated|sued|analyzed|"
            r"examined|observed|identified|detected|tracked|documented|published)\s+"
            r"[^,;:|—–\n]+,\s*"
            r"(?:the\s+)?"
            r"(?:(?:(?:more|less|fewer) than|at least|at most|about|approximately)\s+)?"
            r"\d+(?:\.\d+)?\s+(?:(?:thousand|million|billion|trillion)\s+)?"
            r"(?:devices|systems|hosts|machines|servers|endpoints)\s+"
            r"(?:involved\s+)?(?:were|are)\s+(?:not\s+)?[a-z][a-z-]*[.!?]?",
            text.strip(),
            re.I,
        )
    )


def _version_span_reason(span: DetailSpan, constraints: Sequence[str]) -> str | None:
    if span.role != "body":
        return None
    text = _version_source_text(span.text)
    text = CVSS_SCORE.sub("", text)
    # Scaled quantities are not target software versions. Only suppress their
    # shape, never their original clause: affected assertions and collected
    # constraints still use text. Entity names and dates remain unresolved.
    version_shape = bool(
        VERSION_SHAPE.search(text)
        or BARE_MAJOR_RELEASE.fullmatch(text.strip().rstrip("."))
    )
    shape_text = SCALED_QUANTITY.sub("", text)
    if version_shape and shape_text != text:
        # Keep dated releases and any unclassified neighboring number. Only
        # original version shapes enter this refinement; ordinary integer
        # quantities must retain their existing clause-classification path.
        version_shape = bool(
            VERSION_SHAPE.search(shape_text)
            or VERSION_LABEL.search(shape_text)
            or re.search(r"\d", shape_text)
        )
    # Integer-only assertions still need clause classification. For example,
    # "Gateway 7 is vulnerable" cannot establish absence merely because the
    # sentence is neither a dotted version nor a bare release row.
    if not version_shape and not re.search(r"\b\d+\b", text):
        return None
    # A typed recommendation or fixed-release statement supplies no affected
    # range. Other version-bearing prose remains unresolved, never absence.
    fixed = FIXED_RELEASE.fullmatch(text.strip().rstrip("."))
    try:
        if fixed and _version_entries(fixed[1]):
            return None
        cue = _version_list_cue(text)
        remainder = re.sub(
            r"^\s*(?:(?:are|is|include|includes)\b)?\s*[:=-]?\s*",
            "",
            text[cue.end :] if cue else text,
            flags=re.I,
        ).rstrip(". ")
        clauses = _version_clauses(remainder)
        if (
            not cue
            and clauses
            and all(
                clause.kind in {"recommendation", "information"}
                for _, clause in clauses
            )
        ):
            return None
        if (
            not version_shape
            and not TARGET_ASSERTION.search(text)
            and not any(
                clause.kind in {"affected", "unaffected", "audience", "exception"}
                for _, clause in clauses
            )
        ):
            return None
        included, excluded = _version_constraints(remainder)
        # Every version-bearing span must contribute to a complete collected
        # constraint. A known list elsewhere cannot hide unresolved prose.
        unresolved = not (included or excluded) or any(
            not any(_plain(part) in _plain(whole) for whole in constraints)
            for part in [*included, *excluded]
        )
        if not unresolved:
            return None
        if (
            not cue
            and not span.fields
            and not VERSION_LABEL.search(text)
            and not TARGET_ASSERTION.search(text)
            and clauses
            and all(
                clause.kind == "list" and _is_event_count_narrative(clause.text)
                for _, clause in clauses
            )
            and not excluded
        ):
            # This makes no assertion about the number's entity type. It only
            # permits an explicit unresolved state under the scope-level gates.
            return "unclassified_numeric_prose"
        return "unresolved_version_assertion"
    except EvidenceError:
        return "version_clause_error"


def _unresolved_version_span(span: DetailSpan, constraints: Sequence[str]) -> bool:
    return _version_span_reason(span, constraints) is not None


def _unaccounted_version_evidence(span: DetailSpan) -> bool:
    """Recognize pending evidence without assigning it to a product or CVE."""
    if span.role == "boundary":
        return False
    cue = _version_list_cue(span.text)
    if cue and cue.kind == "explicit" or "Affected Versions" in span.fields:
        # A required list without entries/digits is still unresolved evidence.
        return True
    if span.role != "body":
        return False
    # This probe does not alter the source used by the existing role parser.
    # Identifier digits alone are not software releases.
    probe = CVE_ID_PATTERN.sub("", span.text).strip().rstrip(".")
    bare_release = BARE_MAJOR_RELEASE.fullmatch(probe) and not (
        re.search(VERSION_FINITE_PREDICATE, probe, re.I)
    )
    assertion = re.search(r"\b\d+\b", probe) and (
        re.search(rf"\b(?:{VERSION_STATE})\b", probe, re.I)
        or TARGET_ASSERTION.search(probe)
    )
    if not (VERSION_SHAPE.search(probe) or bare_release or assertion):
        return False
    return _version_span_reason(span, []) is not None


def _scope(
    catalog: Mapping[str, ReportingSource],
    cves: tuple[str, ...],
    keys: Sequence[str],
) -> VersionScope:
    constraints: dict[str, VersionConstraint] = {}
    excluded: set[str] = set()
    failures: set[str] = set()
    unresolved: dict[str, UnresolvedVersionReference] = {}
    known_version_list = False
    pending_context = False
    pending_version = False
    for key in keys:
        source = catalog[key]
        try:
            partition = _partition_detail_spans(source, cves)
            spans = partition.scoped
            pending_context |= any(span.text for span in partition.unaccounted)
            try:
                pending_version |= any(
                    _unaccounted_version_evidence(span)
                    for span in partition.unaccounted
                )
            except EvidenceError:
                pending_version = True
            included, exclusions, known_list = collect_affected_version_constraints(
                spans
            )
        except EvidenceError:
            failures.add("version_collection_error")
            continue
        excluded.update(_plain(value) for value in exclusions)
        known_version_list |= known_list
        if known_list and not included and not exclusions:
            failures.add("empty_version_list")
        content_hash = hashlib.sha256(source.content.encode()).hexdigest()
        for span in spans:
            reason = _version_span_reason(span, [*included, *exclusions])
            if reason == "unclassified_numeric_prose":
                span_hash = hashlib.sha256(span.text.encode()).hexdigest()
                identity = json.dumps(
                    [key, content_hash, cves, span_hash, reason], ensure_ascii=True
                )
                ref = (
                    "unresolved-version-"
                    + hashlib.sha256(identity.encode()).hexdigest()[:32]
                )
                unresolved[ref] = UnresolvedVersionReference(
                    ref, key, content_hash, span_hash
                )
            elif reason:
                failures.add(reason)
        for value in included:
            text = " ".join(value.split())
            identity = json.dumps([key, content_hash, cves, text], ensure_ascii=True)
            ref = "version-" + hashlib.sha256(identity.encode()).hexdigest()[:32]
            item = VersionConstraint(ref, key, content_hash, text)
            if ref in constraints and constraints[ref] != item:
                raise _reject(
                    "version_reference_collision", "Version reference collision"
                )
            constraints[ref] = item
    if pending_version or pending_context and (constraints or excluded):
        failures.add("unowned_version_evidence")
    if excluded & {_plain(item.text) for item in constraints.values()}:
        failures.add("contradictory_version_constraints")
    if unresolved and (cves or constraints or excluded or known_version_list):
        failures.add("unresolved_scope_not_eligible")
    return VersionScope(
        cves,
        tuple(keys),
        tuple(constraints.values()),
        bool(failures),
        tuple(unresolved.values()),
        tuple(sorted(failures)),
    )


def _scopes(
    catalog: Mapping[str, ReportingSource],
    detail_context: Sequence[Mapping[str, Any]] | None = None,
) -> list[VersionScope]:
    # A precomputed presentation context is not proof of catalog completeness.
    # Derive all groups and peer source sets from the retained bodies, even when
    # a caller supplies an empty, partial or stale cache. Keep the optional
    # parameter for compatibility with existing generation callers.
    context = build_finding_detail_context(catalog)
    groups: dict[tuple[tuple[str, ...], str], list[str]] = {}
    for item in context:
        cves = tuple(sorted(item["cves"]))
        key = item["source_key"]
        group = (cves, "" if cves else key)
        if key not in groups.setdefault(group, []):
            groups[group].append(key)
    return [_scope(catalog, cves, keys) for (cves, _), keys in groups.items()]


def build_version_reference_context(
    catalog: Mapping[str, ReportingSource],
    detail_context: Sequence[Mapping[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    return [scope.context() for scope in _scopes(catalog, detail_context)]


def _finding_scope(
    catalog: Mapping[str, ReportingSource],
    cves: tuple[str, ...],
    keys: Sequence[str],
    scopes: Mapping[tuple[str, ...], VersionScope] | None = None,
) -> VersionScope:
    if (
        not keys
        or len(set(keys)) != len(keys)
        or any(key not in catalog for key in keys)
    ):
        raise _reject(
            "invalid_version_reference_source", "Invalid version reference source"
        )
    if scopes is None:
        scopes = {scope.cves: scope for scope in _scopes(catalog) if scope.cves}
    scope = scopes.get(tuple(cves)) if cves else _scope(catalog, (), keys)
    if (cves and scope and any(key not in scope.source_keys for key in keys)) or (
        not cves and any(extract_cve_ids(catalog[key].content) for key in keys)
    ):
        raise _reject(
            "invalid_version_reference_source",
            "Cited source does not match the version evidence scope",
        )
    if scope is None or scope.blocked:
        raise _reject(
            "unresolved_version_evidence", "Version evidence scope is unresolved"
        )
    return scope


def validate_resolved_version_status(
    fields: Mapping[str, str],
    catalog: Mapping[str, ReportingSource],
    *,
    cves: Sequence[str],
) -> None:
    """Recompute source eligibility; a canonical status is not trusted metadata."""
    keys = tuple(key.strip() for key in fields.get("Reporting", "").split(","))
    scope = _finding_scope(catalog, tuple(sorted(cves)), keys)
    state = fields.get(STATE_FIELD)
    value = fields.get("Affected Versions")
    if state != scope.state or (
        state == VersionEvidenceStatus.UNRESOLVED
        and value != UNRESOLVED
        or state == VersionEvidenceStatus.NOT_STATED
        and value != ABSENT
        or state == VersionEvidenceStatus.SUPPORTED
        and value in {ABSENT, UNRESOLVED}
    ):
        raise _reject(
            "invalid_version_evidence_state",
            "Version evidence state does not match the source scope",
        )


def resolve_version_references(
    report: str, catalog: Mapping[str, ReportingSource]
) -> str:
    """Resolve only an exact reference protocol; never repair free-text claims."""
    section = ACTIVE_SECTION_PATTERN.search(report)
    if not section:
        raise _reject("missing_finding_section", "Missing finding section")
    scopes = {scope.cves: scope for scope in _scopes(catalog) if scope.cves}
    replacements = []
    for index, finding in enumerate(FINDING_PATTERN.finditer(section["section"]), 1):
        fields = dict(FIELD.findall(finding["body"]))
        cves = tuple(
            sorted(
                extract_cve_ids(fields.get("CVE IDs", "") + " " + finding["heading"])
            )
        )
        keys = tuple(key.strip() for key in fields.get("Reporting", "").split(","))
        try:
            pairs = FIELD.findall(finding["body"])
            matches = list(VERSION_FIELD.finditer(finding["body"]))
            if len(pairs) != len(fields) or len(matches) != 1:
                raise _reject(
                    "invalid_version_reference_field",
                    "Expected one version reference field",
                )
            if STATE_FIELD in fields:
                raise _reject(
                    "invalid_version_reference_field",
                    "Version evidence status is host-owned",
                )
            scope = _finding_scope(catalog, cves, keys, scopes)
            field = matches[0]
            tail = finding["body"][field.end() :]
            next_field = FIELD.search(tail)
            if tail[: next_field.start() if next_field else len(tail)].strip():
                raise _reject(
                    "wrapped_version_reference",
                    "Version references must occupy one line",
                )
            value = field["value"].strip()
            if value == ABSENT:
                if not scope.absence_allowed:
                    raise _reject(
                        "unsupported_version_absence",
                        "Version evidence does not permit absence",
                    )
                rendered = ABSENT
            else:
                refs = [part.strip() for part in value.split(";")]
                if not refs or any(not REFERENCE.fullmatch(ref) for ref in refs):
                    raise _reject(
                        "invalid_version_reference",
                        "Affected versions require supplied references",
                    )
                if len(set(refs)) != len(refs):
                    raise _reject(
                        "duplicate_version_reference", "Duplicate version reference"
                    )
                available = {
                    item.id: item
                    for item in (
                        scope.unresolved_references
                        if scope.unresolved_allowed
                        else scope.constraints
                    )
                }
                if any(
                    ref not in available or available[ref].source_key not in keys
                    for ref in refs
                ):
                    raise _reject(
                        "unsupported_version_reference",
                        "Version reference does not match cited source and CVE scope",
                    )
                if scope.unresolved_allowed:
                    if set(refs) != set(available):
                        raise _reject(
                            "missing_version_references",
                            "Unresolved references omit required source evidence",
                        )
                    rendered = UNRESOLVED
                else:
                    constraints = {item.id: item for item in scope.constraints}
                    selected = [constraints[ref] for ref in refs]
                    if {_plain(item.text) for item in selected} != {
                        _plain(item.text) for item in scope.constraints
                    }:
                        raise _reject(
                            "missing_version_references",
                            "Version references omit required source constraints",
                        )
                    rendered = "; ".join(dict.fromkeys(item.text for item in selected))
            rendered += f"\n- **{STATE_FIELD}**: {scope.state}"
            start = (
                section.start("section") + finding.start("body") + field.start("value")
            )
            end = section.start("section") + finding.start("body") + field.end("value")
            replacements.append((start, end, rendered))
        except EvidenceError as exc:
            exc.finding_index = index
            exc.cves = cves
            exc.source_keys = tuple(key for key in keys if key in catalog)
            exc.finding_sha256 = hashlib.sha256(finding.group().encode()).hexdigest()
            raise
    if not replacements:
        raise _reject("missing_finding_section", "No finding version references")
    for start, end, value in reversed(replacements):
        report = report[:start] + value + report[end:]
    if REFERENCE.search(report):
        raise _reject(
            "misplaced_version_reference", "Version reference outside its field"
        )
    return report


def resolve_analysis_version_references(result: Mapping[str, Any]) -> str:
    """Shared production/evaluation adapter; protocol is host-owned metadata."""
    report = prepare_generated_report(result["exploitation_report"])
    if (
        type(result.get(PROTOCOL_KEY)) is not int
        or result[PROTOCOL_KEY] != PROTOCOL_VERSION
    ):
        raise _reject(
            "invalid_version_reference_protocol", "Missing version reference protocol"
        )
    catalog = deserialize_reporting_catalog(result.get("reporting_sources", []))
    return resolve_version_references(report, catalog)
