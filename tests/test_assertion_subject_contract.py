"""Finite subject binding keeps predicate, target and qualifier owners separate.

Only the existing actor heads, a leading `the`, and threat actor(s) are accepted.
Unknown noun modifiers or bridges cannot disappear at a predicate boundary.
"""

import pytest

from src.core.assertions import parse_assertions
from src.core.finding_evidence import (
    EvidenceError,
    assess_exploitation,
    validate_finding_evidence,
)
from src.core.report_artifact import parse_report_artifact
from test_finding_generation import catalog_for, render
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article

CVE = "CVE-2026-1234"
OTHER = "CVE-2026-5678"
SUBJECTS = [
    "Attacker",
    "Attackers",
    "Actor",
    "Actors",
    "Operator",
    "Operators",
    "Threat actor",
    "Threat actors",
    "The attacker",
    "The attackers",
    "The actor",
    "The actors",
    "The operator",
    "The operators",
    "The threat actor",
    "The threat actors",
]


def publish(monkeypatch, tmp_path, text, identities, expected):
    # Keep the existing report-breadth gate active with an independent actor
    # finding. It intentionally rejects a one-item actor rollup when broader
    # activity markers are repeated across the report's mandatory sections.
    control_ids = {"CVE-2026-9998", "CVE-2026-9999"}
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(text, cves=identities)]
        + [
            article(
                f"Attackers are actively exploiting {control}.",
                link=f"https://example.test/{control}",
            )
            for control in sorted(control_ids)
        ],
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert text in report
    findings = parse_report_artifact(report).findings
    controls = [f for f in findings if control_ids.intersection(f.cve_ids)]
    assert len(controls) == 2 and all(len(f.cve_ids) == 1 for f in controls)
    assert {c for f in controls for c in f.cve_ids} == control_ids
    assert all(f.exploitation_status.value == "active" for f in controls)
    findings = [f for f in findings if not control_ids.intersection(f.cve_ids)]
    assert {c for f in findings for c in f.cve_ids} == set(identities)
    assert {f.exploitation_status.value for f in findings} == set(expected)
    return findings


def rejected(monkeypatch, tmp_path, text):
    previous = {
        "index.md": b"Previous report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
        ".sentryinsight-articles-fingerprint": b"previous inputs\n",
    }
    for name, data in previous.items():
        (tmp_path / name).write_bytes(data)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(text, cves=[CVE] if CVE in text else [])],
        expect_model_call=False,
    )
    assert result["status"] == "failed", result
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == data for name, data in previous.items()
    )


@pytest.mark.parametrize("subject", SUBJECTS)
@pytest.mark.parametrize(
    "form,status",
    [
        ("current", "active"),
        ("past", "observed"),
        ("negative", "not_observed"),
        ("possible", "potential"),
        ("conditional", "unknown"),
    ],
)
def test_bound_subject_does_not_supply_predicate_semantics(
    monkeypatch, tmp_path, subject, form, status
):
    copula = "are" if subject.endswith("s") else "is"
    predicate = {
        "current": f"{copula} actively exploiting {CVE} in the wild",
        "past": f"exploited {CVE} yesterday",
        "negative": f"{copula} not exploiting {CVE} now",
        "possible": f"may be exploiting {CVE}",
        "conditional": f"{copula} actively exploiting {CVE}, if reports are accurate",
    }[form]
    text = f"{subject} {predicate}."
    (clause,) = parse_assertions(text)
    assert clause.subject == subject and clause.cves == (CVE,)
    assert not clause.unsupported and clause.status == status
    assert clause.polarity == ("negative" if form == "negative" else "affirmative")
    assert clause.conditions == (
        ("if reports are accurate",) if form == "conditional" else ()
    )
    assessment = assess_exploitation([article(text)], [CVE])
    assert assessment.status == status and not assessment.unsupported
    findings = publish(monkeypatch, tmp_path, text, [CVE], [status])
    assert len(findings) == 1


@pytest.mark.parametrize("subject", SUBJECTS)
@pytest.mark.parametrize("past", [False, True])
def test_source_only_scope_retains_subject_and_whole_evidence(
    monkeypatch, tmp_path, subject, past
):
    predicate = "exploited" if past else "are actively exploiting"
    text = f"{subject} {predicate} the gateway."
    (clause,) = parse_assertions(text)
    assert clause.subject == subject and clause.cves == ()
    assert not clause.unsupported
    findings = publish(
        monkeypatch, tmp_path, text, [], ["observed" if past else "active"]
    )
    assert len(findings) == 1 and findings[0].cve_ids == ()


@pytest.mark.parametrize(
    "subject", ["Attackers", "The attackers", "Threat actors", "The threat actors"]
)
def test_reporter_composition_reuses_subject_binding(monkeypatch, tmp_path, subject):
    text = f"The vendor has not found evidence that {subject.lower()} have begun exploiting {CVE}."
    (clause,) = parse_assertions(text)
    assert clause.subject == subject.lower() and not clause.unsupported
    assert clause.reporter and clause.reporter.polarity == "negative"
    assert clause.tense == "past" and clause.status == "not_observed"
    publish(monkeypatch, tmp_path, text, [CVE], ["not_observed"])


@pytest.mark.parametrize("connector", [" and ", ", but ", "; ", " whereas "])
@pytest.mark.parametrize("reverse", [False, True])
def test_later_subject_and_conditions_do_not_cross_independent_clauses(
    monkeypatch, tmp_path, connector, reverse
):
    parts = [
        f"Threat actors are actively exploiting {CVE}",
        f"The attackers are not exploiting {OTHER}, if reports are accurate",
    ]
    if reverse:
        parts.reverse()
    text = connector.join(parts) + "."
    relations = parse_assertions(text)
    assert len(relations) == 2 and not any(r.unsupported for r in relations)
    current = next(r for r in relations if r.cves == (CVE,))
    qualified = next(r for r in relations if r.cves == (OTHER,))
    assert current.subject == "Threat actors" and current.status == "active"
    assert current.conditions == () and current.polarity == "affirmative"
    assert qualified.subject == "The attackers" and qualified.status == "unknown"
    assert qualified.conditions == ("if reports are accurate",)
    assert qualified.polarity == "negative"
    findings = publish(monkeypatch, tmp_path, text, [CVE, OTHER], ["active", "unknown"])
    assert len(findings) == 2


def test_passive_joint_owner_and_actor_clause_keep_distinct_scope(
    monkeypatch, tmp_path
):
    text = f"{CVE} and {OTHER} were exploited yesterday, but The attackers are not exploiting {CVE} now."
    relations = parse_assertions(text)
    assert [r.cves for r in relations] == [(CVE, OTHER), (CVE,)]
    assert [r.status for r in relations] == ["observed", "not_observed"]
    assert not any(r.unsupported for r in relations)
    findings = publish(monkeypatch, tmp_path, text, [CVE, OTHER], ["unknown"])
    assert len(findings) == 1 and set(findings[0].cve_ids) == {CVE, OTHER}


@pytest.mark.parametrize(
    "subject",
    [
        "A threat actor",
        "These attackers",
        "Cyber threat actors",
        "Unknown actors",
        "The alleged attackers",
        "Threat attackers",
        "Threat operators",
        "Threat threat actors",
        "The the attackers",
        "The attackers' associates",
        "The attackers who researchers identified",
        "Attackers apparently",
        "The attackers deny that they",
        "The attackers are unsure whether they",
    ],
)
def test_unknown_subject_or_bridge_cannot_disappear(monkeypatch, tmp_path, subject):
    text = f"{subject} are actively exploiting {CVE}."
    assert any(r.unsupported for r in parse_assertions(text))
    rejected(monkeypatch, tmp_path, text)


@pytest.mark.parametrize(
    "tail",
    [
        f"can exploit {CVE}",
        f"will exploit {CVE}",
        f"have been exploiting {CVE}",
        f"are actively exploiting {CVE} and {OTHER}",
        f"are actively exploiting {CVE} and consider exploiting {OTHER}",
        f"are actively exploiting {CVE}, only when exposed",
        "exploited the gateway yesterday",
        "are not exploiting the gateway now",
    ],
)
def test_subject_binding_cannot_license_unsupported_predicates_or_arguments(
    monkeypatch, tmp_path, tail
):
    text = f"The threat actors {tail}."
    assert any(r.unsupported for r in parse_assertions(text))
    rejected(monkeypatch, tmp_path, text)


@pytest.mark.parametrize("source_only", [False, True])
def test_subject_identity_cannot_replace_source_ownership_or_hide_conflict(source_only):
    target = "the gateway" if source_only else CVE
    texts = [
        f"Threat actors exploited {target}{'' if source_only else ' yesterday'}.",
        f"The attackers are not exploiting {target}{'' if source_only else ' now'}.",
    ]
    catalog = catalog_for(*texts)
    records, report = render(catalog)
    assert all(text in report for text in texts)
    assert [r.status for r in records] == (
        ["observed", "not_observed"] if source_only else ["unknown"]
    )
    damaged = (
        report.replace(
            "**Exploitation Status**: observed", "**Exploitation Status**: active"
        )
        if source_only
        else report.replace(
            "**Exploitation Status**: unknown", "**Exploitation Status**: active"
        )
    )
    assert damaged != report
    with pytest.raises(EvidenceError):
        validate_finding_evidence(damaged, catalog)


def test_subject_support_does_not_bypass_existing_report_breadth_gate(
    monkeypatch, tmp_path
):
    previous = {
        "index.md": b"Previous report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
        ".sentryinsight-articles-fingerprint": b"previous inputs\n",
    }
    for name, data in previous.items():
        (tmp_path / name).write_bytes(data)
    text = f"Threat actors are actively exploiting {CVE} in the wild."
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(text)]
    )
    assert result["status"] == "failed", result
    assert any(
        "Threat Actor Activities has only one item" in value
        for value in result["report_validation_errors"]
    )
    assert all(
        (tmp_path / name).read_bytes() == data for name, data in previous.items()
    )
