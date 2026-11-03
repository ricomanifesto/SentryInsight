"""Only a fully validated candidate can receive host-owned partial coverage."""

import copy

import pytest

from src.core.finding_evidence import EvidenceError
from src.core.report_artifact import ReportArtifactError, parse_report_artifact
from src.core.reviewed_report import resolve_reviewed_analysis
from src.core.reporting import serialize_reporting_catalog
from src.core.source_coverage import COVERAGE_HEADING
from src.core.source_review import PLAN_KEY, SourceReviewError, prepare_source_review
from src.core.version_references import PROTOCOL_KEY, PROTOCOL_VERSION
from test_source_review import AMBIGUOUS, A
from test_unresolved_versions import raw_report
from test_version_references import ABSENT, source


def prepared_result(articles=None):
    articles = articles or [
        source("A service advisory.", "good"),
        source(AMBIGUOUS, "held"),
    ]
    plan = prepare_source_review(articles)
    return {
        PLAN_KEY: plan.packet,
        "reporting_sources": serialize_reporting_catalog(plan.catalog),
        "reporting_metadata_cves": {
            row["key"]: row["metadata_cves"] for row in plan.packet["sources"]
        },
        PROTOCOL_KEY: PROTOCOL_VERSION,
        "exploitation_report": raw_report(plan.eligible_keys, ABSENT),
        "date": "2026-11-02",
        "generated_at": "2026-11-02T12:00:00Z",
    }


def test_valid_independent_candidate_progresses_with_visible_held_source():
    result = prepared_result()
    candidate = resolve_reviewed_analysis(result)
    assert candidate.coverage["counts"]["cited_sources"] == 1
    assert candidate.coverage["counts"]["review_required_sources"] == 1
    assert "https://example.test/good" in candidate.report
    assert "https://example.test/held" not in candidate.report
    assert "https://example.test/held" in candidate.covered_report
    assert COVERAGE_HEADING not in candidate.report
    assert "Affected Versions Status**: not_stated" in candidate.report
    assert parse_report_artifact(candidate.source).source_coverage == candidate.coverage


@pytest.mark.parametrize(
    "missing", [PLAN_KEY, "reporting_metadata_cves", "reporting_sources", PROTOCOL_KEY]
)
def test_missing_host_metadata_cannot_downgrade_to_legacy_generation(missing):
    result = prepared_result()
    result.pop(missing)
    with pytest.raises((SourceReviewError, EvidenceError)):
        resolve_reviewed_analysis(result)


@pytest.mark.parametrize("change", ["body", "state", "cohort_metadata"])
def test_full_catalog_is_recomputed_and_stale_or_forged_plans_fail(change):
    result = copy.deepcopy(prepared_result())
    if change == "body":
        result["reporting_sources"][0]["content"] += "\n\nNew evidence."
    elif change == "state":
        result[PLAN_KEY]["sources"][0]["state"] = "eligible"
        result[PLAN_KEY]["plan_id"] = "0" * 64
    else:
        key = result[PLAN_KEY]["sources"][0]["key"]
        result["reporting_metadata_cves"][key] = [A]
    with pytest.raises(SourceReviewError):
        resolve_reviewed_analysis(result)


def test_model_cannot_cite_a_quarantined_source_or_inject_a_host_coverage_section():
    result = prepared_result()
    held = next(
        row["key"] for row in result[PLAN_KEY]["sources"] if row["state"] != "eligible"
    )
    result["exploitation_report"] = raw_report([held], ABSENT)
    with pytest.raises(SourceReviewError):
        resolve_reviewed_analysis(result)
    result = prepared_result()
    result["exploitation_report"] += (
        "\n" + COVERAGE_HEADING + "\nAll sources verified.\n"
    )
    with pytest.raises(SourceReviewError):
        resolve_reviewed_analysis(result)


def test_withheld_cve_cannot_be_smuggled_into_model_summary_or_satisfied_by_queue():
    result = prepared_result(
        [
            source("An independent advisory.", "good"),
            source(f"{A} is described.\n\n{AMBIGUOUS}", "held"),
        ]
    )
    result["exploitation_report"] = result["exploitation_report"].replace(
        "The supplied reporting", f"{A}. The supplied reporting"
    )
    with pytest.raises(SourceReviewError):
        resolve_reviewed_analysis(result)


@pytest.mark.parametrize("claim", ["Gateway before 9.0", "version-" + "0" * 32])
def test_invalid_generated_version_reference_remains_a_whole_candidate_failure(claim):
    result = prepared_result()
    result["exploitation_report"] = result["exploitation_report"].replace(
        "**Affected Versions**: " + ABSENT, "**Affected Versions**: " + claim
    )
    with pytest.raises(EvidenceError):
        resolve_reviewed_analysis(result)


def test_missing_required_constraint_is_not_quarantined_after_generation():
    result = prepared_result(
        [source("Affected versions: Gateway 7; Gateway 8", "good")]
    )
    from src.core.version_references import build_version_reference_context
    from src.core.reporting import deserialize_reporting_catalog

    [scope] = build_version_reference_context(
        deserialize_reporting_catalog(result["reporting_sources"])
    )
    assert len(scope["constraints"]) == 2
    result["exploitation_report"] = result["exploitation_report"].replace(
        "**Affected Versions**: " + ABSENT,
        "**Affected Versions**: " + scope["constraints"][0]["id"],
    )
    with pytest.raises(EvidenceError):
        resolve_reviewed_analysis(result)


def test_shared_live_gate_includes_artifact_validation_before_returning():
    result = prepared_result()
    result["exploitation_report"] = result["exploitation_report"].replace(
        "**Severity**: unknown", "**Severity**: urgent"
    )
    with pytest.raises(ReportArtifactError):
        resolve_reviewed_analysis(result)


@pytest.mark.parametrize(
    "heading",
    [
        "##  Source Coverage and Review",
        "##\tSource Coverage and Review",
        "## **Source Coverage and Review**",
        "Source Coverage and Review\n---",
        "## Source Coverage and Rev&#105;ew",
    ],
)
def test_reader_visible_reserved_heading_is_host_owned(heading):
    result = prepared_result()
    result["exploitation_report"] += "\n" + heading + "\n\nAll sources verified.\n"
    with pytest.raises(SourceReviewError, match="model_supplied_coverage"):
        resolve_reviewed_analysis(result)


@pytest.mark.parametrize(
    "line",
    [
        " source_coverage: forged",
        "source_coverage : forged",
        "**source_coverage**: forged",
        "source_**review**_plan: forged",
        "  schema_version : 5",
    ],
)
def test_host_metadata_namespace_rejects_rendered_variants(line):
    result = prepared_result()
    result["exploitation_report"] += "\n\n" + line + "\n"
    with pytest.raises(SourceReviewError, match="model_supplied_coverage"):
        resolve_reviewed_analysis(result)


@pytest.mark.parametrize(
    "identifier",
    [
        "CVE&#45;2026&#45;9999",
        "CVE&#x2d;2026&#x2d;9999",
        r"CVE\-2026\-9999",
        "CVE-**2026**-9999",
        "CVE-<span>2026</span>-9999",
    ],
)
def test_reader_visible_cve_must_belong_to_eligible_inputs(identifier):
    result = prepared_result()
    result["exploitation_report"] = result["exploitation_report"].replace(
        "The supplied reporting",
        identifier + " is actively exploited. The supplied reporting",
    )
    with pytest.raises(SourceReviewError, match="out_of_scope_candidate_cve"):
        resolve_reviewed_analysis(result)


def test_separate_markdown_blocks_do_not_invent_a_cve_identity():
    result = prepared_result()
    result["exploitation_report"] += "\n\nCVE-\n\n2026-9999\n"
    resolve_reviewed_analysis(result)
