"""Advisory grounding: accuracy checks log a bounded reason instead of blocking.

Strict remains the default for direct callers, evaluations and verification.
Site-safety and structural checks still block in advisory mode.
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

from src.core.finding_evidence import EvidenceError
from src.core.report_artifact import parse_report_artifact
from src.core.report_validation import ReportValidationIssue, blocking_issues
from src.core.reviewed_report import (
    ReviewedReportValidationError,
    resolve_reviewed_analysis,
)
from src.core.source_review import PLAN_KEY, SourceReviewError
from test_reviewed_report import prepared_result
from test_version_references import ABSENT, source

ROOT = Path(__file__).resolve().parents[1]
CVE = "CVE-2026-1234"
BOGUS = "version-" + "0" * 32
UNRESOLVED = "Unresolved from supplied sources."


def with_versions(result, value):
    result["exploitation_report"] = result["exploitation_report"].replace(
        "**Affected Versions**: " + ABSENT, "**Affected Versions**: " + value
    )
    return result


def cve_result():
    result = prepared_result(
        [source(f"{CVE} affects Gateway 7 and Gateway 8.", "good")]
    )
    result["exploitation_report"] = result["exploitation_report"].replace(
        "### Synthetic campaign\n",
        f"### Gateway ({CVE})\n- **CVE IDs**: {CVE}\n",
    )
    return result


def test_strict_remains_the_default():
    with pytest.raises(EvidenceError):
        resolve_reviewed_analysis(with_versions(prepared_result(), BOGUS))


def test_unresolvable_versions_publish_as_unresolved_with_a_reason():
    candidate = resolve_reviewed_analysis(
        with_versions(prepared_result(), BOGUS), advisory=True
    )
    assert f"**Affected Versions**: {UNRESOLVED}" in candidate.report
    assert "**Affected Versions Status**: unresolved" in candidate.report
    assert BOGUS not in candidate.report
    [reason] = [a for a in candidate.advisories if a["stage"] == "version_references"]
    assert reason["codes"] == ["unsupported_version_reference"]
    assert reason["finding_index"] == 1
    parse_report_artifact(candidate.source)


def test_cve_finding_may_carry_an_unresolved_version_state():
    candidate = resolve_reviewed_analysis(
        with_versions(cve_result(), BOGUS), advisory=True
    )
    artifact = parse_report_artifact(candidate.source)
    [finding] = artifact.findings
    assert finding.cve_ids == (CVE,)
    assert finding.affected_versions == UNRESOLVED


def test_ungrounded_exploitation_claim_is_logged_not_blocking():
    result = cve_result()
    result["exploitation_report"] = result["exploitation_report"].replace(
        "- **Exploitation Status**: unknown", "- **Exploitation Status**: active"
    )
    with pytest.raises(EvidenceError):
        resolve_reviewed_analysis(result)
    candidate = resolve_reviewed_analysis(result, advisory=True)
    assert "**Exploitation Status**: active" in candidate.report
    stages = [a["stage"] for a in candidate.advisories]
    assert "finding_evidence" in stages
    assert all("Gateway" not in json.dumps(a) for a in candidate.advisories)


def test_active_content_still_blocks_in_advisory_mode():
    result = prepared_result()
    result["exploitation_report"] = result["exploitation_report"].replace(
        "A campaign described", "<script>alert(1)</script> A campaign described"
    )
    with pytest.raises(ReviewedReportValidationError):
        resolve_reviewed_analysis(result, advisory=True)


def test_quarantined_source_citation_still_blocks_in_advisory_mode():
    result = prepared_result()
    report = result["exploitation_report"]
    start = report.index("- **Reporting**: ") + len("- **Reporting**: ")
    end = report.index("\n", start)
    [held] = [
        row["key"]
        for row in result[PLAN_KEY]["sources"]
        if row["state"] == "review_required"
    ]
    result["exploitation_report"] = report[:start] + held + report[end:]
    with pytest.raises(SourceReviewError):
        resolve_reviewed_analysis(result, advisory=True)


def test_invented_vendor_link_is_dropped_in_advisory_mode_and_blocks_in_strict():
    bad_url = "https://evil.example/patch.exe"
    strict_result = cve_result()
    strict_result["exploitation_report"] = strict_result["exploitation_report"].replace(
        "- **Vendor Links**: " + ABSENT,
        f"- **Vendor Links**: {bad_url}",
    )
    with pytest.raises(EvidenceError) as raised:
        resolve_reviewed_analysis(strict_result)
    assert raised.value.code == "unsupported_vendor_link"

    result = with_versions(cve_result(), BOGUS)  # an earlier advisory reason
    result["exploitation_report"] = result["exploitation_report"].replace(
        "- **Vendor Links**: " + ABSENT,
        f"- **Vendor Links**: {bad_url}",
    )
    candidate = resolve_reviewed_analysis(result, advisory=True)
    assert bad_url not in candidate.report
    assert bad_url not in candidate.source
    assert f"- **Vendor Links**: {ABSENT}" in candidate.report
    artifact = parse_report_artifact(candidate.source)
    assert len(artifact.findings) == 1
    assert artifact.findings[0].vendor_links == ()
    vendor_advisories = [
        a
        for a in candidate.advisories
        if a["stage"] == "finding_evidence"
        and a["codes"] == ["unsupported_vendor_link"]
    ]
    assert len(vendor_advisories) == 1
    assert vendor_advisories[0]["field"] == "Vendor Links"
    assert vendor_advisories[0]["finding_index"] == 1
    assert all(bad_url not in json.dumps(a) for a in candidate.advisories)


@pytest.mark.parametrize(
    ("bad_link", "expected_code"),
    [
        ("https://evil.example/invented", "unsupported_vendor_link"),
        ("javascript:alert(1)", "invalid_vendor_link"),
        ("not-a-valid-url", "invalid_vendor_link"),
    ],
)
def test_bad_vendor_link_dropped_while_keeping_supported_links_and_finding(
    bad_link, expected_code
):
    advisory_link = "https://vendor.example/advisory"
    article = source(f"{CVE} affects Gateway 7 and Gateway 8.", "good")
    article["source_links"] = [advisory_link]
    result = prepared_result([article])
    result["exploitation_report"] = (
        result["exploitation_report"]
        .replace(
            "### Synthetic campaign\n",
            f"### Gateway ({CVE})\n- **CVE IDs**: {CVE}\n",
        )
        .replace(
            "- **Vendor Links**: " + ABSENT,
            f"- **Vendor Links**: {advisory_link}; {bad_link}",
        )
    )
    with pytest.raises(EvidenceError) as raised:
        resolve_reviewed_analysis(result)
    assert raised.value.code == expected_code

    candidate = resolve_reviewed_analysis(result, advisory=True)
    assert advisory_link in candidate.report
    assert bad_link not in candidate.report
    assert bad_link not in candidate.source
    artifact = parse_report_artifact(candidate.source)
    assert artifact.findings[0].vendor_links == (advisory_link,)
    dropped = [
        a
        for a in candidate.advisories
        if a["stage"] == "finding_evidence" and a["codes"] == [expected_code]
    ]
    assert len(dropped) == 1
    assert dropped[0]["field"] == "Vendor Links"
    assert dropped[0]["finding_index"] == 1
    assert all(bad_link not in json.dumps(a) for a in candidate.advisories)


def test_grouping_cannot_legitimize_uncited_vendor_link_in_advisory_mode():
    first = source(f"{CVE} is actively exploited.", "first")
    first["source_links"] = ["https://first.example/advisory"]
    second = source(f"{CVE} is actively exploited.", "second")
    second["source_links"] = ["https://second.example/advisory"]
    result = prepared_result([first, second])
    keys = {
        item["url"].rsplit("/", 1)[-1]: item["key"]
        for item in result["reporting_sources"]
    }
    row_template = (
        f"### Gateway ({CVE})\n"
        "- **Description**: A service flaw.\n"
        "- **Severity**: high\n"
        "- **Exploitation Status**: active\n"
        "- **Action**: monitor\n"
        f"- **CVE IDs**: {CVE}\n"
        "- **Reporting**: {key}\n"
        f"- **Affected Versions**: {ABSENT}\n"
        f"- **Exceptions**: {ABSENT}\n"
        f"- **Recommended Actions**: {ABSENT}\n"
        "- **Vendor Links**: {link}\n\n"
    )
    # First finding cites only "first" but tries to list "second"'s link;
    # grouping merges both findings for the same CVE, so the link MUST be
    # dropped before grouping rather than legitimized by the merged citation.
    from src.core.report_findings import report_findings

    original = result["exploitation_report"]
    existing = report_findings(original).rows[0]
    two_findings = row_template.format(
        key=keys["first"], link="https://second.example/advisory"
    ) + row_template.format(key=keys["second"], link=ABSENT)
    result["exploitation_report"] = (
        original[: existing.start] + two_findings + original[existing.end :]
    )

    candidate = resolve_reviewed_analysis(result, advisory=True)
    assert "https://second.example/advisory" not in candidate.report
    assert any(
        a["stage"] == "finding_evidence"
        and a["codes"] == ["unsupported_vendor_link"]
        and a["finding_index"] == 1
        for a in candidate.advisories
    )


def test_second_finding_position_is_recorded_on_dropped_vendor_link_and_version_field():
    other = "CVE-2026-5678"
    first = source(f"{CVE} is actively exploited.", "first")
    second = source(f"{other} is actively exploited.", "second")
    result = prepared_result([first, second])
    keys = {
        item["url"].rsplit("/", 1)[-1]: item["key"]
        for item in result["reporting_sources"]
    }
    from src.core.report_findings import report_findings

    original = result["exploitation_report"]
    existing = report_findings(original).rows[0]
    two_findings = (
        f"### Gateway Alpha ({CVE})\n"
        "- **Description**: First flaw.\n"
        "- **Severity**: high\n"
        "- **Exploitation Status**: active\n"
        "- **Action**: monitor\n"
        f"- **CVE IDs**: {CVE}\n"
        f"- **Reporting**: {keys['first']}\n"
        f"- **Affected Versions**: {ABSENT}\n"
        f"- **Exceptions**: {ABSENT}\n"
        f"- **Recommended Actions**: {ABSENT}\n"
        f"- **Vendor Links**: {ABSENT}\n\n"
        f"### Gateway Beta ({other})\n"
        "- **Description**: Second flaw.\n"
        "- **Severity**: high\n"
        "- **Exploitation Status**: active\n"
        "- **Action**: monitor\n"
        f"- **CVE IDs**: {other}\n"
        f"- **Reporting**: {keys['second']}\n"
        f"- **Affected Versions**: {ABSENT}\n"
        "- **Affected Versions Status**: supported\n"
        f"- **Exceptions**: {ABSENT}\n"
        f"- **Recommended Actions**: {ABSENT}\n"
        "- **Vendor Links**: https://evil.example/second\n\n"
    )
    result["exploitation_report"] = (
        original[: existing.start] + two_findings + original[existing.end :]
    )

    candidate = resolve_reviewed_analysis(result, advisory=True)
    assert "https://evil.example/second" not in candidate.report
    artifact = parse_report_artifact(candidate.source)
    assert len(artifact.findings) == 2
    assert artifact.findings[1].affected_versions_status.value == "not_stated"
    assert any(
        a["stage"] == "version_references"
        and a["codes"] == ["invalid_version_reference_field"]
        and a["finding_index"] == 2
        for a in candidate.advisories
    )
    assert any(
        a["stage"] == "finding_evidence"
        and a["codes"] == ["unsupported_vendor_link"]
        and a["finding_index"] == 2
        for a in candidate.advisories
    )


def test_supplied_vendor_link_is_accepted_in_advisory_mode():
    advisory_link = "https://vendor.example/advisory"
    article = source(f"{CVE} affects Gateway 7 and Gateway 8.", "good")
    article["source_links"] = [advisory_link]
    result = prepared_result([article])
    result["exploitation_report"] = (
        result["exploitation_report"]
        .replace(
            "### Synthetic campaign\n",
            f"### Gateway ({CVE})\n- **CVE IDs**: {CVE}\n",
        )
        .replace(
            "- **Vendor Links**: " + ABSENT, "- **Vendor Links**: " + advisory_link
        )
    )
    candidate = resolve_reviewed_analysis(result, advisory=True)
    assert advisory_link in candidate.report


def test_only_quality_and_coverage_codes_are_advisory():
    issues = [
        ReportValidationIssue("executive_summary_readability", "x"),
        ReportValidationIssue("missing_expected_cves", "x"),
        ReportValidationIssue("underpopulated_threat_actor_activities", "x"),
    ]
    assert blocking_issues(issues) == []
    for code in (
        "active_content",
        "error_marker",
        "empty_report",
        "missing_section",
        "duplicate_section",
        "malformed_markdown",
        "removed_source_attribution",
        "virtual_event_promotion",
        "missing_descriptive_finding_title",
    ):
        issue = ReportValidationIssue(code, "x")
        assert blocking_issues(issues + [issue]) == [issue]


def run_gate(report, config, *extra):
    return subprocess.run(
        [
            sys.executable,
            "-B",
            str(ROOT / "scripts/validate_report.py"),
            str(report),
            "--config",
            str(config),
            *extra,
        ],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )


def test_required_cve_coverage_blocks_in_strict_and_is_advisory_in_advisory(tmp_path):
    report = tmp_path / "index.md"
    report.write_text((ROOT / "index.md").read_text())

    strict_config = tmp_path / "strict.json"
    strict_config.write_text(json.dumps({"analysis": {"grounding": "strict"}}))
    strict_result = run_gate(report, strict_config, "--expected-cve", "CVE-2099-0001")
    assert strict_result.returncode == 1, strict_result.stdout
    assert "CVE-2099-0001" in strict_result.stdout

    advisory_config = tmp_path / "advisory.json"
    advisory_config.write_text(json.dumps({"analysis": {"grounding": "advisory"}}))
    advisory_result = run_gate(
        report, advisory_config, "--expected-cve", "CVE-2099-0001"
    )
    assert advisory_result.returncode == 0, advisory_result.stdout
    assert "Report content advisories (not blocking):" in advisory_result.stdout
    assert "missing_expected_cves" in advisory_result.stdout
    assert "CVE-2099-0001" in advisory_result.stdout


def test_publication_gate_still_blocks_safety_issues_when_advisory(tmp_path):
    config = tmp_path / "config.json"
    config.write_text(json.dumps({"analysis": {"grounding": "advisory"}}))
    report = tmp_path / "index.md"
    report.write_text("")
    assert run_gate(report, config).returncode == 1


def test_repository_runs_advisory_grounding():
    config = json.loads((ROOT / "config/config.json").read_text())
    assert config["analysis"]["grounding"] == "advisory"


def test_production_publisher_snapshot_carries_the_grounding_mode():
    from scripts.build_static_artifact import OPTIONAL_INPUTS, SNAPSHOT_FILES

    assert "config/config.json" in SNAPSHOT_FILES
    assert "config/config.json" in OPTIONAL_INPUTS


def test_strict_resolver_refuses_an_advisory_review_plan():
    from src.core.reviewed_report import analysis_review_plan
    from src.core.source_review import prepare_source_review

    result = prepared_result()
    articles = [source("A service advisory.", "good")]
    plan = prepare_source_review(articles, advisory=True)
    result[PLAN_KEY] = plan.packet
    with pytest.raises(SourceReviewError, match="source_review_plan_mismatch"):
        analysis_review_plan(result)


@pytest.mark.parametrize(
    ("field", "old", "new", "expected_text"),
    [
        (
            "Vendor Links",
            "- **Vendor Links**: " + ABSENT,
            "- **Vendor Links**:",
            "- **Vendor Links**: " + ABSENT,
        ),
        (
            "Exceptions",
            "- **Exceptions**: " + ABSENT,
            "- **Exceptions**:",
            "- **Exceptions**: " + ABSENT,
        ),
        (
            "Exceptions",
            "- **Exceptions**: " + ABSENT,
            "- **Exceptions**: —",
            "- **Exceptions**: " + ABSENT,
        ),
        (
            "Recommended Actions",
            "- **Recommended Actions**: " + ABSENT,
            "- **Recommended Actions**:",
            "- **Recommended Actions**: " + ABSENT,
        ),
        (
            "Affected Versions",
            "- **Affected Versions**: " + ABSENT,
            "- **Affected Versions:**",
            "- **Affected Versions**: " + UNRESOLVED,
        ),
    ],
)
def test_empty_finding_fields_block_strict_and_fallback_cleanly_in_advisory(
    field, old, new, expected_text
):
    strict = prepared_result()
    strict["exploitation_report"] = strict["exploitation_report"].replace(old, new)
    with pytest.raises(EvidenceError):
        resolve_reviewed_analysis(strict, advisory=False)

    advisory_input = prepared_result()
    advisory_input["exploitation_report"] = advisory_input[
        "exploitation_report"
    ].replace(old, new)
    candidate = resolve_reviewed_analysis(advisory_input, advisory=True)
    assert expected_text in candidate.report
    assert new + "\n" not in candidate.report
    assert any(a["field"] == field for a in candidate.advisories)
    parse_report_artifact(candidate.source)


@pytest.mark.parametrize("cve_line", ["- **CVE IDs**:", "- **CVE IDs**: —"])
def test_empty_cve_ids_field_on_non_cve_finding_is_omitted_in_advisory(cve_line):
    result = prepared_result()
    result["exploitation_report"] = result["exploitation_report"].replace(
        "- **Reporting**:", f"{cve_line}\n- **Reporting**:"
    )
    with pytest.raises((EvidenceError, ReviewedReportValidationError)):
        resolve_reviewed_analysis(result, advisory=False)

    candidate = resolve_reviewed_analysis(result, advisory=True)
    assert "**CVE IDs**" not in candidate.report
    artifact = parse_report_artifact(candidate.source)
    assert artifact.findings[0].cve_ids == ()


def test_truly_empty_bold_bullet_still_blocks_advisory_with_line_and_excerpt():
    result = prepared_result()
    result["exploitation_report"] += "\n- **FishMonger**:\n"
    with pytest.raises(ReviewedReportValidationError) as caught:
        resolve_reviewed_analysis(result, advisory=True)
    [issue] = [i for i in caught.value.issues if i.code == "malformed_markdown"]
    assert issue.markdown_reason == "missing_bold_label_description"
    assert isinstance(issue.markdown_line, int) and issue.markdown_line >= 1
    assert issue.markdown_excerpt == "- **FishMonger**:"
