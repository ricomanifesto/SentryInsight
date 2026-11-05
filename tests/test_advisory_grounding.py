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


def test_invented_vendor_link_still_blocks_in_advisory_mode():
    result = with_versions(cve_result(), BOGUS)  # an earlier advisory reason
    result["exploitation_report"] = result["exploitation_report"].replace(
        "- **Vendor Links**: " + ABSENT,
        "- **Vendor Links**: https://evil.example/patch.exe",
    )
    with pytest.raises(EvidenceError) as raised:
        resolve_reviewed_analysis(result, advisory=True)
    assert raised.value.code == "unsupported_vendor_link"


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


def test_only_quality_codes_are_advisory():
    issues = [
        ReportValidationIssue("missing_expected_cves", "x"),
        ReportValidationIssue("executive_summary_readability", "x"),
        ReportValidationIssue("underpopulated_threat_actor_activities", "x"),
    ]
    assert blocking_issues(issues) == []
    for code in (
        "active_content",
        "error_marker",
        "empty_report",
        "missing_section",
        "removed_source_attribution",
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


@pytest.mark.parametrize("mode", ["advisory", "strict"])
def test_publication_gate_follows_the_configured_mode(tmp_path, mode):
    config = tmp_path / "config.json"
    config.write_text(json.dumps({"analysis": {"grounding": mode}}))
    report = tmp_path / "index.md"
    report.write_text((ROOT / "index.md").read_text())
    result = run_gate(report, config, "--expected-cve", "CVE-2099-0001")
    assert (result.returncode == 0) is (mode == "advisory"), result.stdout


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
