"""Condition ownership across punctuation, coordination and source scopes.

Existing if/unless assertions and already supported directive conditions keep
their meanings with or without an attaching comma. Bind their spans before
coordination. Nominal conjunctions inside a condition stay inside it; an explicit
independent relation keeps its own condition, polarity, tense and identity.
Joint identities and source-owned empty scopes remain exact. Unsupported
assertion adjuncts do not gain positive grammar: fail before model transport.
"""

import json

import pytest

from src.core.assertions import parse_assertions
from src.core.finding_evidence import assess_exploitation, recommendation_action
from src.core.recommendations import parse_recommendation
from src.core.report_artifact import parse_report_artifact
from test_finding_generation import catalog_for, render
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article

CVE = "CVE-2026-1234"
OTHER = "CVE-2026-5678"


@pytest.mark.parametrize("separator", [" ", ", "])
@pytest.mark.parametrize(
    "condition", ["if reports are accurate", "unless reports are inaccurate"]
)
@pytest.mark.parametrize(
    "predicate",
    ["is actively exploited", "was exploited", "is not exploited", "may be exploited"],
)
@pytest.mark.parametrize(
    "subject,cves", [(CVE, (CVE,)), (f"{CVE} and {OTHER}", (CVE, OTHER)), ("", ())]
)
def test_assertion_condition_owns_one_complete_relation(
    separator, condition, predicate, subject, cves
):
    text = f"{subject} {predicate}{separator}{condition}.".strip()
    result = assess_exploitation([article(text)], cves)
    assert result.status == "unknown" and not result.unsupported
    assert len(result.relations) == 1
    relation = result.relations[0]
    assert relation.cves == cves
    assert relation.conditions == (condition,)
    assert relation.source_text == text
    assert relation.polarity == ("negative" if "not" in predicate else "affirmative")
    assert relation.tense == (
        "past"
        if predicate.startswith("was")
        else "current" if predicate.startswith("is") else "unspecified"
    )
    records, report = render(catalog_for(text))
    assert len(records) == 1 and records[0].cves == cves
    assert records[0].status == "unknown" and text in report


@pytest.mark.parametrize("separator", [" ", ", "])
@pytest.mark.parametrize(
    "prefix",
    [
        f"Attackers gained access by exploiting a vulnerability ({CVE})",
        f"{CVE}, which attackers began exploiting as a zero-day in June",
    ],
)
def test_intrusion_uses_the_same_condition_boundary(prefix, separator):
    text = f"{prefix}{separator}if reports are accurate."
    result = assess_exploitation([article(text)], (CVE,))
    assert not result.unsupported and result.status == "unknown"
    assert len(result.relations) == 1
    assert result.relations[0].conditions == ("if reports are accurate",)
    assert result.relations[0].tense == "past"


@pytest.mark.parametrize("connector", [" and ", ", and ", ", but ", "; "])
@pytest.mark.parametrize("reverse", [False, True])
def test_independent_assertion_keeps_its_identity_and_tense(
    monkeypatch, tmp_path, connector, reverse
):
    qualified = f"{CVE} is actively exploited, if reports and observations are accurate"
    independent = f"{OTHER} was exploited yesterday"
    source = (
        connector.join(
            (independent, qualified) if reverse else (qualified, independent)
        )
        + "."
    )
    relations = [r for r in parse_assertions(source) if r.kind == "assertion"]
    assert len(relations) == 2 and not any(r.unsupported for r in relations)
    by_cve = {r.cves: r for r in relations}
    assert by_cve[(CVE,)].conditions == ("if reports and observations are accurate",)
    assert by_cve[(CVE,)].status == "unknown"
    assert by_cve[(OTHER,)].conditions == () and by_cve[(OTHER,)].status == "observed"
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(source)]
    )
    assert result["status"] == "completed", result
    saved = (tmp_path / "index.md").read_text()
    assert source in saved
    findings = parse_report_artifact(saved).findings
    assert {f.cve_ids: f.exploitation_status.value for f in findings} == {
        (CVE,): "unknown",
        (OTHER,): "observed",
    }
    assert (
        json.loads((tmp_path / "current-findings.json").read_text())["finding_count"]
        == 2
    )


@pytest.mark.parametrize("separator", [" ", ", "])
@pytest.mark.parametrize(
    "condition",
    [
        "if needed",
        "unless unavailable",
        "until verification completes",
        "when needed",
        "only after verification",
        "provided that verification completes",
        "depending on verification",
    ],
)
@pytest.mark.parametrize("negative", [False, True])
def test_directive_conditions_attach_before_punctuation(separator, condition, negative):
    text = f"Users should {'not ' if negative else ''}install the patch{separator}{condition}."
    directive = parse_recommendation(text)
    assert directive is not None and not directive.ambiguous
    assert len(directive.clauses) == 1
    clause = directive.clauses[0]
    assert clause.verb == "install" and clause.object_members == ("patch",)
    assert clause.conditions == (condition,)
    assert clause.polarity == ("negative" if negative else "affirmative")
    assert directive.source_text == text
    assert recommendation_action([text]) == "none"


@pytest.mark.parametrize("connector", [" and ", ", and ", ", but ", "; "])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize(
    "qualified",
    [
        "monitor logs, if reports and observations warrant it",
        "monitor logs, if reports and observations are accurate",
        "not monitor logs, unless needed",
        "restart the service, if needed",
        "do so, if needed",
    ],
)
def test_directive_qualifiers_do_not_leak_to_independent_actions(
    monkeypatch, tmp_path, connector, reverse, qualified
):
    # A reference can only bind to its preceding directive; the reverse case
    # explicitly names a preceding independent monitoring target.
    if qualified.startswith("do so"):
        qualified = "monitor logs and " + qualified
    # Repeating the finite advice modal explicitly establishes independence.
    # Bare "not monitor ... and install" correctly inherits negation in the
    # existing grammar and is not an independent affirmative instruction.
    bodies = (
        ("Users should " + qualified, "Users should install the patch")
        if reverse
        else ("Users should install the patch", "Users should " + qualified)
    )
    guidance = connector.join(bodies) + "."
    directive = parse_recommendation(guidance)
    unsupported = qualified == "monitor logs, if reports and observations warrant it"
    assert directive is not None and directive.ambiguous is unsupported
    assert directive.source_text == guidance
    patch = next(c for c in directive.clauses if c.verb == "install")
    assert not patch.conditions and patch.polarity == "affirmative"
    if not unsupported:
        assert recommendation_action([guidance]) == "patch"
    source = f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}"
    prior = {
        "index.md": b"Previous report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
        ".sentryinsight-articles-fingerprint": b"previous-inputs\n",
    }
    if unsupported:
        for name, data in prior.items():
            (tmp_path / name).write_bytes(data)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(source)],
        expect_model_call=not unsupported,
    )
    if unsupported:
        assert result["status"] == "failed", result
        assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
        assert all(
            (tmp_path / name).read_bytes() == data for name, data in prior.items()
        )
        return
    assert result["status"] == "completed", result
    (finding,) = parse_report_artifact((tmp_path / "index.md").read_text()).findings
    assert finding.action.value == "patch" and finding.recommended_actions == guidance


@pytest.mark.parametrize("separator", [" ", ", "])
@pytest.mark.parametrize(
    "tail",
    [
        "only when a user opens a file",
        "when a user opens a file",
        "provided that a user opens a file",
        "depending on user interaction",
        "subject to verification",
        "conditionally",
    ],
)
def test_unclassified_assertion_adjunct_is_terminal_before_transport(
    monkeypatch, tmp_path, separator, tail
):
    source = f"{CVE} is exploited{separator}{tail}."
    prior = {
        "index.md": b"Previous report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
        ".sentryinsight-articles-fingerprint": b"previous-inputs\n",
    }
    for name, data in prior.items():
        (tmp_path / name).write_bytes(data)
    assessment = assess_exploitation([article(source)], (CVE,))
    assert assessment.unsupported and assessment.status == "unknown"
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(source)],
        expect_model_call=False,
    )
    assert result["status"] == "failed", result
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all((tmp_path / name).read_bytes() == data for name, data in prior.items())


@pytest.mark.parametrize(
    "tail",
    [
        f"and {OTHER} will be exploited",
        f"but {OTHER} is thought by analysts to be exploited",
    ],
)
def test_supported_condition_does_not_hide_unsupported_residual_predicates(
    monkeypatch, tmp_path, tail
):
    source = f"{CVE} is exploited, if reports are accurate, {tail}."
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(source)],
        expect_model_call=False,
    )
    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"


@pytest.mark.parametrize("prefix", ["in attacks ", "in attacks, "])
def test_context_adjunct_cannot_hide_an_unclassified_condition(
    monkeypatch, tmp_path, prefix
):
    source = f"{CVE} is exploited {prefix}only when a user opens a file."
    assessment = assess_exploitation([article(source)], (CVE,))
    assert assessment.unsupported and assessment.status == "unknown"
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(source)],
        expect_model_call=False,
    )
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"


@pytest.mark.parametrize(
    "residual",
    ["consider installing an update", "assess whether to upgrade the system"],
)
def test_condition_cannot_swallow_an_unclassified_advice_clause(
    monkeypatch, tmp_path, residual
):
    guidance = f"Users should monitor logs, if needed and {residual}."
    parsed = parse_recommendation(guidance)
    assert parsed is not None and parsed.ambiguous
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}")
        ],
        expect_model_call=False,
    )
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"


def test_existing_modified_directive_is_an_independent_clause():
    guidance = "Users should monitor logs, if needed and promptly install the patch."
    parsed = parse_recommendation(guidance)
    assert parsed is not None and not parsed.ambiguous
    assert len(parsed.clauses) == 2
    assert parsed.clauses[0].conditions == ("if needed",)
    assert parsed.clauses[1].conditions == ()
    assert recommendation_action([guidance]) == "patch"
