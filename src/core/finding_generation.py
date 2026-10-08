"""Render complete findings from evidence; the model selects references only."""

from dataclasses import dataclass, replace
import json
import re
from typing import Callable, Mapping, Sequence

from .cve import extract_cve_ids
from .finding_evidence import (
    ABSENT,
    EvidenceError,
    ExploitationAssessment,
    assess_exploitation,
    build_finding_detail_context,
    collect_finding_details,
    detail_statement_roles,
    recommendation_action,
    validate_finding_evidence,
)
from .reporting import ReportingSource
from .recommendations import directive_units


@dataclass(frozen=True)
class SourceExcerpt:
    key: str
    text: str
    roles: tuple[str, ...]


@dataclass(frozen=True)
class SourceLink:
    key: str
    url: str
    required: bool


@dataclass(frozen=True)
class FindingRecord:
    key: str
    cves: tuple[str, ...]
    status: str
    heading: str
    state_prose: str
    fields: tuple[tuple[str, str], ...]
    excerpts: tuple[SourceExcerpt, ...]
    links: tuple[SourceLink, ...] = ()


def _one_line(text: str) -> str:
    return " ".join(text.split())


def _unique(values):
    return tuple(dict.fromkeys(_one_line(value) for value in values if value.strip()))


def _state_prose(assessment: ExploitationAssessment, subject: str) -> str:
    if assessment.conflicting:
        return (
            f"Reporting contains conflicting exploitation evidence for {subject}. "
            "Some supplied reporting states that exploitation has not been observed; "
            "the combined exploitation status is unknown."
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


def _severity(texts: Sequence[str]) -> str:
    """Recognize explicit scoped ratings, never article-wide severity keywords."""
    values = set()

    def qualified(text, start):
        prefix = re.split(r"[;,.!?]", text[:start])[-1]
        return bool(
            re.search(
                r"\b(?:not|never|no|neither|nor|may|might|could|potentially|possibly|unlikely|non)\b",
                prefix,
                re.I,
            )
        )

    for text in texts:
        for match in re.finditer(
            r"\b(?:(?P<label>critical|high|medium|low)(?:-severity)? (?:vulnerability|flaw|bug)"
            r"|(?:severity(?: rating)?[: ]+|rated )(?P<rated>critical|high|medium|low))\b",
            text,
            re.I,
        ):
            if qualified(text, match.start()):
                continue
            values.add((match["label"] or match["rated"]).lower())
        for match in re.finditer(
            r"\bCVSS(?: v(?:ersion)?\s*[34](?:\.\d)?)?"
            r"(?:\s+(?:base )?(?:score|rating)(?: of| is)?\s*:?|\s*:)\s*"
            r"(10(?:\.0)?|[0-9](?:\.\d)?)(?![\d/]|\.\d)",
            text,
            re.I,
        ):
            if qualified(text, match.start()):
                continue
            score = float(match[1])
            # FIRST CVSS qualitative bands. A zero rating has no enum equivalent.
            values.add(
                "critical"
                if score >= 9
                else (
                    "high"
                    if score >= 7
                    else "medium" if score >= 4 else "low" if score > 0 else "unknown"
                )
            )
    return next(iter(values)) if len(values) == 1 else "unknown"


EXCERPT_ROLES = {
    "impact": r"\b(?:allows?|could|can|leads? to|access|expose|steal|disclos\w*|denial|execute|execution|privilege\w*)\b",
    "systems": r"\b(?:versions?|releases?|platforms?|servers?|gateways?|appliances?|products?|Windows|Linux|macOS|Android|iOS|plugins?|software|interfaces?)\b",
    "vectors": r"\b(?:SSRF|request forgery|injection|cross.site|deserialization|phishing|authentication|remote code|malicious|crafted|attack vector|by exploiting|zero.day)\b",
    "actors": r"\b(?:actors?|attackers?|campaigns?|operators?|attribut\w*|ransomware|malware|espionage|APT\w*|gained access|began exploiting)\b",
}


def _excerpt_roles(text: str) -> tuple[str, ...]:
    # Presentation eligibility only. Whole-finding evidence validation decides
    # which complete source sentences may enter this inventory at all.
    return tuple(
        role for role, cue in EXCERPT_ROLES.items() if re.search(cue, text, re.I)
    )


def _anchored_spans(spans, cves):
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
            if not wanted or (mentioned <= wanted if mentioned else section_owned):
                yield span


def _substantive_prose(text, *, statement=False):
    return bool(
        len(text.split()) >= 5
        and (statement or re.search(r"[.!?]", text))
        and not re.search(
            r"^(?:by\s|(?:image|photo|picture|screenshot|illustration)(?:\s|:)"
            r"|(?:the |a )?(?:logo|image|photo|picture|screenshot) (?:of|for|shows)\b)",
            text,
            re.I,
        )
    )


def _advisory_urls(sources, cves):
    urls = []
    for source in sources:
        spans = collect_finding_details([source], cves).spans
        blocks = {_one_line(span.source_block) for span in _anchored_spans(spans, cves)}
        for link in source.link_contexts:
            label, context = _one_line(link.label), _one_line(link.context)
            if (
                link.url in source.links
                and context in blocks
                and label in context
                and re.fullmatch(
                    r"(?:(?:vendor|security|official|product)\s+)*(?:advisory|bulletin|security notice)(?:\s+for\s+CVE-\d{4}-\d{4,})?",
                    label,
                    re.I,
                )
            ):
                if _one_line(source.content).count(context) != 1:
                    raise EvidenceError(
                        "Repeated advisory paragraphs have ambiguous link ownership",
                        code="ambiguous_advisory_link_scope",
                        field="Vendor Links",
                    )
                urls.append(link.url)
    return tuple(dict.fromkeys(urls))


def _finding(
    record: FindingRecord, excerpts: Sequence[str] = (), *, impact=(), links=None
) -> str:
    # All text is source-derived or a fixed assessment rendering, never model prose.
    description = " ".join(excerpts) or record.state_prose
    lines = [
        f"### {record.heading}",
        f"- **Description**: {description}",
        f"- **Status**: {record.state_prose}",
    ]
    if impact:
        lines.append(f"- **Impact**: {' '.join(impact)}")
    lines.extend(
        f"- **{name}**: {('; '.join(links) or ABSENT) if name == 'Vendor Links' and links is not None else value}"
        for name, value in record.fields
    )
    return "\n".join(lines) + "\n\n"


def _check_finding(record, catalog, excerpts=()):
    validate_finding_evidence(
        "## Active Exploitation Details\n\n" + _finding(record, excerpts), catalog
    )


def _finding_scopes(
    catalog, required_cves, relevance: Callable[[str], bool] | None = None
):
    """Join only scopes needed to own otherwise-lost complete detail blocks."""
    contexts = build_finding_detail_context(catalog)
    signatures = {}
    no_cves = []
    metadata = {
        key: set(source.metadata_cves) & set(required_cves)
        for key, source in catalog.items()
    }
    for item in contexts:
        scope = tuple(item["cves"])
        if not scope:
            if not metadata[item["source_key"]]:
                no_cves.append(((), (item["source_key"],)))
            continue
        owned = signatures.setdefault(scope, set())
        for span in item.get("spans", []):
            if span["role"] != "body":
                continue
            for field in span["fields"]:
                value = (
                    span.get("source_block", span["text"])
                    if field == "Recommended Actions"
                    else span["text"]
                )
                owned.add((item["source_key"], field, _one_line(value)))
    # Metadata supplies identity coverage, never an implicit body assertion or
    # a synthetic CVE heading. Unattributed body facts still fail the same gate.
    for identities in metadata.values():
        for cve in sorted(identities):
            signatures.setdefault((cve,), set())
    cves = list(dict.fromkeys(cve for scope in signatures for cve in scope))
    groups = [{cve} for cve in cves]
    covered = set().union(
        *(values for scope, values in signatures.items() if len(scope) == 1)
    )
    for scope, values in sorted(signatures.items(), key=lambda item: len(item[0])):
        if len(scope) < 2 or not values - covered:
            continue
        members = set(scope)
        overlapping = [group for group in groups if group & members]
        groups = [group for group in groups if not group & members]
        groups.append(set().union(members, *overlapping))
        covered.update(values)
    result = []
    for group in groups:
        scope = tuple(sorted(group))
        keys = tuple(
            key
            for key, source in catalog.items()
            if group & (set(extract_cve_ids(source.content)) | metadata[key])
        )
        result.append((scope, keys))
    candidates = result + list(dict.fromkeys(no_cves))
    if relevance is None:
        return candidates
    is_relevant: Callable[[str], bool] = relevance

    def eligible(scope, keys):
        if set(scope) & set(required_cves):
            return True
        texts = [
            span["text"]
            for item in contexts
            if item["source_key"] in keys and set(item["cves"]) <= set(scope)
            for span in item.get("spans", [])
            if span["role"] == "body"
        ]
        # Membership is distinct from confirmation. Explicit negative/unknown
        # exploitation discussion remains relevant. The original report also
        # covers explicitly rated high-impact risks without observed activity.
        return any(is_relevant(text) for text in texts) or (
            _severity(texts) in {"high", "critical"}
            and any(set(_excerpt_roles(text)) & {"impact", "vectors"} for text in texts)
        )

    # Select complete groups, never trim supporting or contrary source keys.
    return [(scope, keys) for scope, keys in candidates if eligible(scope, keys)]


def compile_finding_records(
    catalog: Mapping[str, ReportingSource],
    required_cves: Sequence[str] = (),
    *,
    relevance: Callable[[str], bool] | None = None,
) -> tuple[FindingRecord, ...]:
    """Compile selected groups without converting ambiguity into absence.

    Joint detail ownership determines grouping; incidental co-mentions cannot
    create duplicate findings. The complete selected group is validated again.

    Explicit compiler callers can inspect candidate scopes; production supplies
    the established relevance predicate and unchanged required-CVE coverage.
    """
    scopes = _finding_scopes(catalog, required_cves, relevance)
    represented = {cve for cves, _ in scopes for cve in cves}
    if set(required_cves) - represented:
        raise EvidenceError(
            "Required CVEs have no retained source-content scope",
            code="missing_generation_source_scope",
            field="Reporting",
        )
    if not scopes:
        raise EvidenceError(
            "No source findings to generate", code="empty_generation_evidence"
        )
    records = []
    for cves, keys in scopes:
        sources = [catalog[key] for key in keys]
        assessment = assess_exploitation(sources, cves)
        details = collect_finding_details(sources, cves)
        narrative_spans = tuple(_anchored_spans(details.spans, cves))
        versions = _unique(details.version_lines)
        exceptions = _unique(
            [
                span.text
                for span in details.spans
                if span.role == "body" and "Exceptions" in span.fields
            ]
            + list(details.excluded_version_lines)
        )
        recommendations = _unique(
            span.source_block or span.text
            for span in details.spans
            if span.role == "body" and "Recommended Actions" in span.fields
        )
        # References are local to this immutable catalog, not persistent IDs.
        # Short IDs keep the complete plan inside the existing output budget.
        key = f"f{len(records) + 1}"
        subject = ", ".join(cves) or "this source finding"
        heading = ", ".join(cves) or f"Security reporting {len(records) + 1}"
        fields = [
            (
                "Severity",
                _severity([span.text for span in narrative_spans]),
            ),
            ("Exploitation Status", assessment.status),
            ("Action", recommendation_action(recommendations)),
        ]
        if dict(fields)["Severity"] == "unknown":
            fields.append(
                (
                    "Severity Context",
                    "No single unqualified severity rating is supported for this finding scope.",
                )
            )
        if recommendations and dict(fields)["Action"] == "none":
            fields.append(
                (
                    "Action Context",
                    "Follow the complete source guidance and qualifications in Recommended Actions; no unconditional action badge is asserted.",
                )
            )
        if cves:
            fields.append(("CVE IDs", ", ".join(cves)))
            if not any(
                set(cves) & set(extract_cve_ids(source.content)) for source in sources
            ):
                fields.append(
                    (
                        "Attribution Context",
                        "This identifier is supplied by article metadata. The retained body does not explicitly attribute finding details to it.",
                    )
                )
        fields.extend(
            [
                ("Reporting", ", ".join(keys)),
                ("Affected Versions", "; ".join(versions) or ABSENT),
                ("Exceptions", "; ".join(exceptions) or ABSENT),
                ("Recommended Actions", "; ".join(recommendations) or ABSENT),
                ("Vendor Links", ABSENT),
            ]
        )
        record = FindingRecord(
            key,
            cves,
            assessment.status,
            heading,
            _state_prose(assessment, subject),
            tuple(fields),
            (),
        )
        _check_finding(record, catalog)
        excerpts = []
        for text in _unique(
            span.source_block or span.text
            for span in narrative_spans
            if _substantive_prose(span.source_block or span.text)
            and (
                not span.fields
                or (
                    set(span.fields) == {"Recommended Actions"}
                    and any(
                        _substantive_prose(unit, statement=True)
                        and not detail_statement_roles(unit)
                        for unit in directive_units(span.text)
                    )
                )
            )
        ):
            try:
                _check_finding(record, catalog, [text])
            except EvidenceError as error:
                if error.code not in {
                    "unsupported_finding_exploitation_claim",
                    "unsupported_current_exploitation_claim",
                }:
                    raise
                # The assessment retains the contrary evidence. An affirmative
                # quote cannot become a new assertion under an unknown badge.
                continue
            excerpt_key = f"{key}e{len(excerpts) + 1}"
            excerpts.append(SourceExcerpt(excerpt_key, text, _excerpt_roles(text)))
        links = tuple(
            SourceLink(f"{key}l{index + 1}", url, True)
            for index, url in enumerate(_advisory_urls(sources, cves))
        )
        records.append(replace(record, excerpts=tuple(excerpts), links=links))
    return tuple(records)


def generation_plan_context(records: Sequence[FindingRecord]) -> list[dict]:
    return [
        {
            "id": record.key,
            "cves": record.cves,
            "state": record.status,
            "finding": _finding(record),
            "excerpts": [
                {"id": item.key, "text": item.text, "roles": item.roles}
                for item in record.excerpts
            ],
            "links": [
                {"id": item.key, "url": item.url, "required": item.required}
                for item in record.links
            ],
        }
        for record in records
    ]


def _invalid_plan():
    return EvidenceError(
        "Generation plan must contain complete finding identities and owned excerpt references only",
        code="invalid_generation_plan",
    )


def render_finding_plan(
    raw: str,
    records: Sequence[FindingRecord],
    catalog: Mapping[str, ReportingSource],
) -> str:
    """Resolve a closed model plan; never recover by editing its factual prose."""

    def unique_object(pairs):
        if len(pairs) != len(dict(pairs)):
            raise _invalid_plan()
        return dict(pairs)

    try:
        plan = json.loads(raw, object_pairs_hook=unique_object)
    except (ValueError, TypeError) as error:
        raise _invalid_plan() from error
    if not isinstance(plan, dict) or set(plan) != {"findings"}:
        raise _invalid_plan()
    entries = plan["findings"]
    if not isinstance(entries, list) or len(entries) != len(records):
        raise _invalid_plan()
    available = {record.key: record for record in records}
    selected = []
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {
            "id",
            "excerpts",
            "vendor_links",
            *EXCERPT_ROLES,
        }:
            raise _invalid_plan()
        key = entry["id"]
        if not isinstance(key, str) or key not in available:
            raise _invalid_plan()
        record = available.pop(key)
        references = entry["excerpts"]
        if (
            not isinstance(references, list)
            or len(references) > 3
            or not all(isinstance(value, str) for value in references)
            or len(set(references)) != len(references)
        ):
            raise _invalid_plan()
        excerpts = {item.key: item.text for item in record.excerpts}
        if any(value not in excerpts for value in references) or (
            excerpts and not references
        ):
            raise _invalid_plan()
        choices = {"excerpts": [excerpts[value] for value in references]}
        for role in EXCERPT_ROLES:
            eligible = {
                item.key: item.text for item in record.excerpts if role in item.roles
            }
            references = entry[role]
            if (
                not isinstance(references, list)
                or len(references) > 3
                or not all(isinstance(value, str) for value in references)
                or len(set(references)) != len(references)
                or any(value not in eligible for value in references)
                or (eligible and not references)
            ):
                raise _invalid_plan()
            choices[role] = [eligible[value] for value in references]
        link_refs = entry["vendor_links"]
        links = {item.key: item.url for item in record.links}
        if (
            not isinstance(link_refs, list)
            or not all(isinstance(value, str) for value in link_refs)
            or len(set(link_refs)) != len(link_refs)
            or any(value not in links for value in link_refs)
            or any(item.required and item.key not in link_refs for item in record.links)
        ):
            raise _invalid_plan()
        choices["links"] = [links[value] for value in link_refs]
        selected.append((record, choices))
    findings = "".join(
        _finding(
            record,
            choices["excerpts"],
            impact=choices["impact"],
            links=choices["links"],
        )
        for record, choices in selected
    )
    summary = "\n\n".join(record.state_prose for record, _ in selected)

    def rollup(role):
        rows = []
        for record, choices in selected:
            values = list(choices[role])
            if role == "systems":
                fields = dict(record.fields)
                values.extend(
                    f"{name}: {fields[name]}"
                    for name in ("Affected Versions", "Exceptions")
                    if fields[name] != ABSENT
                )
            if values:
                rows.append(f"- **{record.heading}**: {' '.join(_unique(values))}")
        return (
            "\n".join(rows)
            or "No additional source-grounded detail is available for these finding scopes."
        )

    report = (
        "# Exploitation Report\n\n## Executive Summary\n\n"
        + summary
        + "\n\n## Active Exploitation Details\n\n"
        + findings
        + "## Affected Systems and Products\n\n"
        + rollup("systems")
        + "\n\n## Attack Vectors and Techniques\n\n"
        + rollup("vectors")
        + "\n\n## Threat Actor Activities\n\n"
        + rollup("actors")
        + "\n"
    )
    validate_finding_evidence(report, catalog)
    return report
