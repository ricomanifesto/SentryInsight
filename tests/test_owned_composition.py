"""Finite/event and directive/scope composition preserve independent owners."""

from dataclasses import replace
import json
from pathlib import Path

import pytest

from src.core.assertion_bindings import bind_subject
from src.core.assertion_predicates import bind_predicate
from src.core.finding_evidence import (
    EvidenceError,
    _scoped_detail_spans,
    _source_recommendation_block,
    _source_recommendation_blocks,
    collect_finding_details,
    validate_finding_evidence,
)
from src.core.finding_generation import compile_finding_records, render_finding_plan
from src.core.reporting import build_reporting_catalog
from src.core.recommendations import parse_recommendation, _frame_actions
from test_owned_relation_contract import article
from test_finding_generation import plan_for, render

CASES = json.loads(
    (Path(__file__).parent / "fixtures/owned_composition.json").read_text()
)["cases"]
CVE, OTHER = "CVE-2026-1234", "CVE-2026-5678"


def catalog(case):
    return build_reporting_catalog(
        [
            article(
                text,
                link=f"https://example.test/owned-composition/{i}",
                **case["metadata"],
            )
            for i, text in enumerate(case["sources"])
        ]
    )


def ordered(records):
    return sorted(records, key=lambda r: (r["cves"], r["status"], r["action"]))


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_complete_compositions_match_the_frozen_publication_contract(case):
    sources = catalog(case)
    if not case["expected"]["compile"]:
        with pytest.raises(EvidenceError):
            render(sources)
        return
    records, report = render(sources)
    actual = [
        {"cves": list(r.cves), "status": r.status, "action": dict(r.fields)["Action"]}
        for r in records
    ]
    assert ordered(actual) == ordered(case["expected"]["records"])
    for token in case["literal_tokens"]:
        assert case["text"][slice(*token["span"])] == token["text"]


def scoped_span():
    source = next(
        iter(
            catalog(
                {
                    "sources": [
                        f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\nUsers should patch immediately."
                    ],
                    "metadata": {},
                }
            ).values()
        )
    )
    return next(
        s
        for s in _scoped_detail_spans(source, [CVE])
        if s.text == "Users should patch immediately."
    )


@pytest.mark.parametrize(
    "field,value",
    [
        ("source_key", "foreign"),
        ("source_url", "https://foreign.test/"),
        ("document_sha256", "f" * 64),
        ("block_index", 99),
    ],
)
def test_scope_cannot_borrow_another_source_document_or_block(field, value):
    span = scoped_span()
    scope = replace(
        span.remediation_scope, origin=replace(span.source_origin, **{field: value})
    )
    with pytest.raises(EvidenceError):
        _source_recommendation_block(replace(span, remediation_scope=scope))


def test_scope_cannot_add_cves_or_distribute_a_joint_owner():
    span = scoped_span()
    with pytest.raises(EvidenceError):
        _source_recommendation_block(
            replace(
                span,
                remediation_scope=replace(span.remediation_scope, cves=(CVE, OTHER)),
            )
        )
    joint = replace(
        span,
        owned_cves=(CVE, OTHER),
        remediation_scope=replace(span.remediation_scope, cves=(CVE, OTHER)),
    )
    with pytest.raises(EvidenceError):
        _source_recommendation_blocks([joint], [CVE])


def test_explicit_target_does_not_consume_unrelated_scope_metadata():
    span = scoped_span()
    explicit = replace(
        span,
        text=f"Users should patch {CVE} immediately.",
        source_block=f"Users should patch {CVE} immediately.",
    )
    expected = _source_recommendation_block(replace(explicit, remediation_scope=None))
    unrelated = replace(
        explicit.remediation_scope,
        cves=(OTHER,),
        origin=replace(explicit.source_origin, block_index=99),
    )
    actual = _source_recommendation_block(
        replace(explicit, remediation_scope=unrelated)
    )
    assert actual == expected
    assert not any(
        clause.argument_relation == "scope"
        for directive in actual.directives
        for clause in directive.clauses
    )


def test_empty_scope_cannot_mean_every_source():
    sources = tuple(
        catalog(
            {
                "sources": [
                    "Attackers are exploiting the gateway.",
                    "Attackers are exploiting the server.",
                ],
                "metadata": {},
            }
        ).values()
    )
    with pytest.raises(EvidenceError):
        collect_finding_details(sources, [])


def test_metadata_and_missing_scope_do_not_certify_a_patch_target():
    sources = catalog(
        {
            "sources": ["Users should patch immediately."],
            "metadata": {"cves": [CVE], "title": CVE + " advisory"},
        }
    )
    spans = _scoped_detail_spans(next(iter(sources.values())), [CVE])
    assert not any(s.remediation_scope for s in spans)
    parsed = parse_recommendation("Users should patch immediately.")
    assert parsed and parsed.ambiguous
    assert all(c.argument_relation != "scope" for c in parsed.clauses)


def test_complete_owned_guidance_cannot_be_omitted_from_publication():
    sources = catalog(
        {
            "sources": [
                f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\nUsers should patch immediately."
            ],
            "metadata": {},
        }
    )
    _, report = render(sources)
    assert "Users should patch immediately." in report
    with pytest.raises(EvidenceError):
        validate_finding_evidence(
            report.replace(
                "Users should patch immediately.", "Not stated in supplied sources."
            ),
            sources,
        )


@pytest.mark.parametrize(
    "argument", ["inexplicable objects", "it", "immediately immediately"]
)
def test_explicit_or_unresolved_argument_never_falls_back_to_scope(argument):
    parsed = parse_recommendation(
        f"Users should patch {argument}.",
        remediation_scope=scoped_span().remediation_scope,
    )
    assert parsed and all(c.argument_relation != "scope" for c in parsed.clauses)


def test_finite_and_observation_spans_cannot_be_reassigned():
    text = f"Attackers do not exploit {CVE}."
    subject = bind_subject(text)
    frame = bind_predicate(text[subject.end :], voice=subject.kind, subject=subject)
    assert frame.supported and frame.operator_binding.supported
    assert not replace(frame.operator_binding, spans=((1, 2),)).supported
    text = f"{CVE} has not been observed not to be exploited."
    subject = bind_subject(text)
    frame = bind_predicate(text[subject.end :], voice=subject.kind, subject=subject)
    assert frame.supported and frame.observation.supported
    assert (
        len(frame.observation.observation_scope.operators)
        == len(frame.observation.event_scope.operators)
        == 1
    )
    assert not replace(frame.observation, predicate_span=frame.event_span).supported


@pytest.mark.parametrize(
    "case",
    [
        c
        for c in CASES
        if c["family"]
        in {
            "do",
            "do-position",
            "observation",
            "observation-position",
            "observation-negation",
        }
    ],
    ids=lambda c: c["id"],
)
def test_composed_tokens_keep_their_frozen_literal_owner(case):
    # Conditions are tested through complete publication above; these literal
    # offsets address the predicate operand before its trailing condition.
    text = case["text"].partition(" if reports are accurate")[0]
    subject = bind_subject(text)
    frame = bind_predicate(text[subject.end :], voice=subject.kind, subject=subject)
    assert frame.supported
    owned = {}

    def add(spans, owner):
        for start, end in spans:
            owned[(start + subject.end, end + subject.end)] = owner

    add([frame.event_span], "event")
    add(
        [(t.start, t.end) for t in (*frame.scope.terms, *frame.scope.operators)],
        "event",
    )
    if frame.observation:
        observation = frame.observation
        assert observation.supported
        add(
            [observation.predicate_span, *observation.finite_binding.spans],
            "observation",
        )
        add(
            [
                (t.start, t.end)
                for t in (
                    *observation.observation_scope.terms,
                    *observation.observation_scope.operators,
                )
            ],
            "observation",
        )
        add(observation.complement_spans, "event")
    else:
        assert frame.operator_binding.supported
        add(frame.operator_binding.spans, "event")
    for token in case["literal_tokens"]:
        assert owned[tuple(token["span"])] == token["proposed_owner"]


@pytest.mark.parametrize("modifiers", [(), ("immediately", "immediately")])
def test_urgency_cannot_be_dropped_or_duplicated_in_a_scoped_target(modifiers):
    parsed = parse_recommendation(
        "Users should patch immediately.",
        remediation_scope=scoped_span().remediation_scope,
    )
    clause = parsed.clauses[0]
    frame = clause.directive_frame
    assert frame.scope_supported
    tampered = replace(frame, argument=replace(frame.argument, modifiers=modifiers))
    assert not tampered.scope_supported
    assert _frame_actions(replace(clause, directive_frame=tampered)) is None


@pytest.mark.parametrize(
    "mutation", ["foreign_finding", "foreign_excerpt", "duplicate"]
)
def test_new_compositions_do_not_weaken_the_model_plan(mutation):
    sources = catalog(
        {
            "sources": [
                f"Attackers do exploit {CVE}.",
                f"{OTHER} has been observed to be exploited.",
            ],
            "metadata": {},
        }
    )
    records = compile_finding_records(sources)
    plan = plan_for(records)
    if mutation == "foreign_finding":
        plan["findings"][0]["id"] = "foreign"
    elif mutation == "foreign_excerpt":
        plan["findings"][0]["excerpts"] = [records[1].excerpts[0].key]
    else:
        plan["findings"].append(plan["findings"][0])
    with pytest.raises(EvidenceError):
        render_finding_plan(json.dumps(plan), records, sources)
