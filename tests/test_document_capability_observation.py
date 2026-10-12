"""Capability prerequisites cannot contradict reporter-qualified observation."""

import json

import pytest

from src.core.assertions import parse_assertions
from src.core.finding_evidence import assess_exploitation
from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline
from test_source_document_contract import source

CVE = "CVE-2026-1234"
OTHER = "CVE-2026-5678"
CONDITION = "if SRv6, which is supported only on some Nexus 9000 models, is turned on"


def body(capability):
    return (
        "<p>All two vulnerabilities require a feature to be active:</p>"
        f"<ul><li>{CVE}: Gateway flaw.</li><li>{OTHER}: Gateway flaw.</li></ul>"
        f"<p>{capability}</p><p>All two vulnerabilities were discovered during internal security testing, "
        "and Example said it was unaware of public announcements or malicious exploitation "
        "at the time of publishing the advisories.</p>"
    )


@pytest.mark.parametrize("negative", [False, True])
def test_complete_capability_condition_is_context_not_an_observation(negative):
    text = f"{CVE} is {'not ' if negative else ''}exploitable {CONDITION}."
    (clause,) = parse_assertions(text)
    assert clause.kind == "context" and clause.modal == "capability"
    assert not clause.unsupported and clause.assertion_status is None
    assert clause.text == text and clause.conditions == (CONDITION,)
    assert clause.polarity == ("negative" if negative else "affirmative")
    result = assess_exploitation(
        [source(f"<article>{body(text)}</article>")], [CVE, OTHER]
    )
    assert result.status == "not_observed" and not result.unsupported


def test_complete_capability_and_reporter_absence_render_together(
    monkeypatch, tmp_path
):
    text = f"{CVE} is exploitable {CONDITION}."

    def plan(**kwargs):
        from test_analyze_guards import reference_plan_from_prompt

        records = json.loads(
            kwargs["user_prompt"]
            .split("BEGIN FINDING RECORDS\n", 1)[1]
            .split("\nEND FINDING RECORDS", 1)[0]
        )
        result = json.loads(reference_plan_from_prompt(**kwargs))
        for finding, record in zip(result["findings"], records):
            finding["excerpts"] = [
                e["id"] for e in record["excerpts"] if text in e["text"]
            ] or finding["excerpts"]
        return json.dumps(result)

    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(body(text))],
        select_plan=plan,
    )
    assert result["status"] == "completed", result.get("analysis_results", {}).get(
        "error"
    )
    report = (tmp_path / "index.md").read_text()
    assert text in report and "at the time of publishing the advisories" in report
    constraints = next(
        line
        for line in report.splitlines()
        if line.startswith("- **Source Constraints**:")
    )
    assert text in constraints
    assert "**Exploitation Status**: not_observed" in report
    artifact = json.loads((tmp_path / "current-findings.json").read_text())
    assert sorted(artifact["cve_ids"]) == [CVE, OTHER]
    assert artifact["finding_count"] == 1
    from src.core.finding_evidence import EvidenceError, validate_finding_evidence
    from src.core.reporting import build_reporting_catalog
    from src.core.finding_generation import compile_finding_records, _finding

    catalog = build_reporting_catalog([article(body(text))])
    (record,) = compile_finding_records(catalog, [CVE, OTHER])
    report = "## Active Exploitation Details\n\n" + _finding(record)
    validate_finding_evidence(report, catalog)
    for damaged in (
        constraints.replace(", is turned on", ""),
        constraints.replace("is turned on", "is not turned on"),
    ):
        with pytest.raises(EvidenceError) as caught:
            validate_finding_evidence(report.replace(constraints, damaged), catalog)
        assert caught.value.code == "source_constraints_not_grounded"


@pytest.mark.parametrize(
    "tail",
    [
        " and unspecified assumptions apply",
        ", and unclassified predicates warrant certainty",
        " with an unknown requirement",
    ],
)
def test_capability_cannot_swallow_required_residual(monkeypatch, tmp_path, tail):
    text = f"{CVE} is exploitable {CONDITION}{tail}."
    assert any(c.unsupported for c in parse_assertions(text))
    previous = {
        name: b"Prior validated artifact"
        for name in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    }
    for name, value in previous.items():
        (tmp_path / name).write_bytes(value)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(body(text))],
        expect_model_call=False,
    )
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == value for name, value in previous.items()
    )


@pytest.mark.parametrize(
    "predicate,state",
    [
        ("is actively exploited", "active"),
        ("was exploited yesterday", "observed"),
        ("exploitation has not been observed", "not_observed"),
    ],
)
def test_independent_event_retains_its_owner_after_capability(predicate, state):
    text = f"{CVE} is exploitable {CONDITION}, but {OTHER} {predicate}."
    clauses = parse_assertions(text)
    assert not any(c.unsupported for c in clauses)
    capability = next(c for c in clauses if c.cves == (CVE,))
    event = next(c for c in clauses if c.cves == (OTHER,))
    assert capability.kind == "context" and capability.conditions == (CONDITION,)
    assert event.assertion_status == state and not event.conditions
