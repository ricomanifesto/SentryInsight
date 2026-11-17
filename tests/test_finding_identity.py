"""Fresh generation cannot silently union contradictory finding identities."""

import asyncio

import pytest

from src.core.finding_evidence import EvidenceError
from src.core.report_artifact import parse_report_artifact
from src.core.reviewed_report import resolve_reviewed_analysis
from src.core.validation_diagnostics import validation_diagnostic
from test_reviewed_report import prepared_result
from test_version_references import source

A = "CVE-2026-1234"
B = "CVE-2026-5678"


def candidate(title, explicit):
    result = prepared_result([source(f"{A} and {B} are described.")])
    result["exploitation_report"] = (
        result["exploitation_report"]
        .replace("### Synthetic campaign", f"### Gateway flaw ({title})")
        .replace("- **Reporting**:", f"- **CVE IDs**: {explicit}\n- **Reporting**:")
    )
    return result


@pytest.mark.parametrize("advisory", [False, True])
@pytest.mark.parametrize("heading", [A, "CVE&#45;2026&#45;1234", "CVE-**2026**-1234"])
def test_mismatch_blocks_before_version_resolution(advisory, heading, monkeypatch):
    def forbidden(*args, **kwargs):
        pytest.fail("Contradictory identity must fail before resolving versions")

    monkeypatch.setattr(
        "src.core.reviewed_report.resolve_analysis_version_references", forbidden
    )
    with pytest.raises(EvidenceError) as caught:
        resolve_reviewed_analysis(candidate(heading, B), advisory=advisory)
    assert caught.value.code == "finding_cve_identity_mismatch"
    diagnostic = validation_diagnostic("reporting_identity", caught.value)
    assert diagnostic["codes"] == ["finding_cve_identity_mismatch"]
    assert diagnostic["field"] == "CVE IDs"
    assert diagnostic["finding_index"] == 1


@pytest.mark.parametrize("advisory", [False, True])
@pytest.mark.parametrize("heading", [A, f"{A} and {B}"])
def test_valid_combined_scope_can_name_one_or_all_members(advisory, heading):
    report = resolve_reviewed_analysis(
        candidate(heading, f"{A}, {B}"), advisory=advisory
    )
    assert set(parse_report_artifact(report.source).findings[0].cve_ids) == {A, B}


def test_historical_artifact_parser_keeps_legacy_identity_compatibility():
    valid = resolve_reviewed_analysis(candidate(A, A))
    historical = valid.source.replace(f"**CVE IDs**: {A}", f"**CVE IDs**: {B}")
    assert parse_report_artifact(historical).findings


@pytest.mark.parametrize("advisory", [False, True])
def test_link_destination_cannot_add_a_hidden_heading_identity(advisory):
    result = candidate(A, A)
    result["exploitation_report"] = result["exploitation_report"].replace(
        f"Gateway flaw ({A})", f"[Gateway flaw ({A})](https://example.test/{B})"
    )
    with pytest.raises(EvidenceError, match="identity disagree"):
        resolve_reviewed_analysis(result, advisory=advisory)


@pytest.mark.parametrize("advisory", [False, True])
@pytest.mark.parametrize("mutation", ["missing", "duplicate"])
def test_heading_identity_requires_one_explicit_field(advisory, mutation):
    result = candidate(A, A)
    field = f"- **CVE IDs**: {A}\n"
    result["exploitation_report"] = result["exploitation_report"].replace(
        field, "" if mutation == "missing" else field + field
    )
    with pytest.raises(EvidenceError, match="identity disagree"):
        resolve_reviewed_analysis(result, advisory=advisory)


@pytest.mark.parametrize("advisory", [False, True])
def test_identity_failure_preserves_the_last_report_and_fingerprint(advisory, tmp_path):
    from src.core.source_review import (
        PLAN_KEY,
        digest,
        prepare_source_review,
        review_articles,
    )
    from test_workflow_guards import import_workflow_with_stubs

    articles = [source(f"{A} and {B} are described.")]
    plan = prepare_source_review(articles, advisory=advisory)
    result = candidate(A, B)
    result[PLAN_KEY] = plan.packet
    output = tmp_path / "index.md"
    output.write_text("LAST VALID REPORT")
    fingerprint = tmp_path / ".sentryinsight-articles-fingerprint"
    fingerprint.write_text("LAST VALID FINGERPRINT")
    workflow = import_workflow_with_stubs()
    state = {
        "analysis_results": result,
        "filtered_articles": review_articles(plan, eligible_only=False),
        PLAN_KEY: plan.packet,
        "articles_fingerprint": digest(
            {"generation_schema": 5, "plan_id": plan.packet["plan_id"]}
        ),
        "config": {
            "output_path": str(output),
            "analysis": {"grounding": "advisory" if advisory else "strict"},
        },
        "status": "started",
    }
    failed = asyncio.run(workflow.generate_report(state))
    assert failed["status"] == "failed"
    assert failed["failure"]["codes"] == ["finding_cve_identity_mismatch"]
    assert failed["failure"]["field"] == "CVE IDs"
    assert failed["failure"]["stage"] == "reporting_identity"
    assert failed["failure_diagnostic"]["stage"] == "reporting_identity"
    assert output.read_text() == "LAST VALID REPORT"
    assert fingerprint.read_text() == "LAST VALID FINGERPRINT"
    assert not (tmp_path / "reports").exists()
