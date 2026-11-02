"""Host coverage is distinct from asserted findings and cannot be forged by prose."""

import json
from pathlib import Path
import re

import pytest

from src.core.source_coverage import (
    COVERAGE_HEADING,
    coverage_markdown,
    make_source_coverage,
    split_source_coverage,
    validate_source_coverage,
)
from src.core.source_review import SourceReviewError, digest, prepare_source_review
from src.core.report_artifact import ReportArtifactError, parse_report_artifact
from src.core.reporting import resolve_reporting_keys
from test_source_review import AMBIGUOUS
from test_unresolved_versions import raw_report
from test_version_references import ABSENT, source, with_version_state


def fixture(held_title=None):
    held = source(AMBIGUOUS, "held")
    if held_title is not None:
        held["title"] = held_title
    plan = prepare_source_review(
        [
            source("A service advisory.", "one"),
            source("A separate advisory.", "two"),
            held,
        ]
    )
    cited = plan.eligible_keys[:1]
    coverage = make_source_coverage(plan.packet, cited)
    body = resolve_reporting_keys(
        with_version_state(raw_report(cited, ABSENT), "not_stated"),
        plan.eligible_catalog,
    )
    header = (
        "---\nschema_version: 5\nreport_date: 2026-11-02\n"
        "generated_at: 2026-11-02T12:00:00Z\n"
        "digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-11-02/\n"
        f"source_coverage: {json.dumps(coverage, sort_keys=True, separators=(',', ':'))}\n---\n"
    )
    return plan, coverage, body, header


def reseal(value):
    value["coverage_id"] = digest(
        {k: v for k, v in value.items() if k != "coverage_id"}
    )
    return value


def test_source_count_equations_do_not_invent_finding_counts():
    _, coverage, _, _ = fixture()
    assert coverage["counts"] == {
        "input_sources": 3,
        "eligible_sources": 2,
        "cited_sources": 1,
        "review_required_sources": 1,
        "rejected_sources": 0,
        "unrepresented_eligible_sources": 1,
    }
    assert coverage["coverage_id"] != coverage["plan"]["plan_id"]
    assert "finding_count" not in coverage["counts"]
    assert validate_source_coverage(coverage) == coverage


def test_held_source_cannot_be_counted_as_cited_even_with_a_new_digest():
    plan, coverage, _, _ = fixture()
    held = next(
        row["key"] for row in plan.packet["sources"] if row["state"] != "eligible"
    )
    coverage["cited_source_keys"] = [held]
    with pytest.raises(SourceReviewError):
        validate_source_coverage(reseal(coverage))


@pytest.mark.parametrize(
    "field", ["input_sources", "cited_sources", "review_required_sources"]
)
def test_inconsistent_counts_fail_even_with_a_matching_digest(field):
    _, coverage, _, _ = fixture()
    coverage["counts"][field] += 1
    with pytest.raises(SourceReviewError):
        validate_source_coverage(reseal(coverage))


def test_coverage_is_exactly_host_rendered_not_a_strip_anything_exception():
    _, coverage, body, _ = fixture()
    combined = body.rstrip() + "\n\n" + coverage_markdown(coverage)
    assert split_source_coverage(combined, coverage).strip() == body.strip()
    with pytest.raises(SourceReviewError):
        split_source_coverage(combined.replace("awaiting review", "verified"), coverage)
    with pytest.raises(SourceReviewError):
        split_source_coverage(combined + "\nUnvalidated text", coverage)
    with pytest.raises(SourceReviewError):
        split_source_coverage(COVERAGE_HEADING + "\n\n" + combined, coverage)


def test_schema_five_owns_coverage_and_counts_only_real_findings():
    _, coverage, body, header = fixture()
    artifact = parse_report_artifact(
        header + body.rstrip() + "\n\n" + coverage_markdown(coverage)
    )
    assert artifact.schema_version == 5
    assert len(artifact.findings) == 1
    assert artifact.source_coverage == coverage
    assert artifact.findings[0].reporting[0].url.endswith("/one") or artifact.findings[
        0
    ].reporting[0].url.endswith("/two")


def test_schema_five_requires_actual_reporting_keys_to_match_coverage():
    plan, coverage, body, header = fixture()
    other_key = next(
        key for key in plan.eligible_keys if key not in coverage["cited_source_keys"]
    )
    other_url = plan.catalog[other_key].url
    actual_url = plan.catalog[coverage["cited_source_keys"][0]].url
    body = body.replace(actual_url, other_url)
    with pytest.raises(ReportArtifactError):
        parse_report_artifact(
            header + body.rstrip() + "\n\n" + coverage_markdown(coverage)
        )


@pytest.mark.parametrize("version", [1, 2, 3, 4])
def test_legacy_schema_cannot_carry_new_coverage_under_an_old_version(version):
    _, coverage, body, header = fixture()
    with pytest.raises(ReportArtifactError):
        parse_report_artifact(
            header.replace("schema_version: 5", f"schema_version: {version}")
            + body.rstrip()
            + "\n\n"
            + coverage_markdown(coverage)
        )


def test_legacy_schema_cannot_impersonate_coverage_by_omitting_its_metadata():
    _, coverage, body, header = fixture()
    header = re.sub(r"^source_coverage:.*\n", "", header, flags=re.M).replace(
        "schema_version: 5", "schema_version: 4"
    )
    with pytest.raises(ReportArtifactError):
        parse_report_artifact(
            header + body.rstrip() + "\n\n" + coverage_markdown(coverage)
        )


def test_source_titles_are_escaped_in_the_host_markdown():
    article = source(AMBIGUOUS, "held")
    article["title"] = "<script>alert(1)</script> [claim](javascript:alert(1))"
    plan = prepare_source_review([article, source("An advisory.", "good")])
    text = coverage_markdown(make_source_coverage(plan.packet, plan.eligible_keys))
    assert "<script>" not in text
    assert "](javascript:" not in text
    assert AMBIGUOUS not in text


@pytest.mark.parametrize(
    "held_title", [None, "<img src=x onerror=alert(1)> & </script>"]
)
def test_schema_five_site_shows_coverage_without_counting_review_rows(
    tmp_path, held_title
):
    from scripts.build_site import build_site

    _, coverage, body, header = fixture(held_title)
    path = tmp_path / "index.md"
    path.write_text(header + body.rstrip() + "\n\n" + coverage_markdown(coverage))
    build_site(
        report_path=path,
        output_path=tmp_path,
        template_path=Path(__file__).resolve().parents[1] / "site",
    )
    rendered = (tmp_path / "index.html").read_text()
    assert 'id="source-coverage-notice"' in rendered
    assert "Partial source coverage" in rendered
    assert '<th scope="col">Disposition</th>' in rendered
    assert "<img src=x" not in rendered
    metadata = json.loads(
        re.search(
            r'<script id="report-metadata" type="application/json">(.*?)</script>',
            rendered,
            re.S,
        )[1]
    )
    assert metadata["source_coverage"] == coverage
    assert metadata["finding_count"] == len(metadata["findings"]) == 1
    manifest = json.loads((tmp_path / "current-findings.json").read_text())
    assert manifest["schema_version"] == 1
    assert manifest["finding_count"] == 1
