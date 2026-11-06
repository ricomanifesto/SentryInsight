"""New publications need readable names; old artifact formats remain readable."""

import pytest

from src.core.report_validation import blocking_issues, validate_report_content
from src.core.reviewed_report import (
    ReviewedReportValidationError,
    resolve_reviewed_analysis,
)
from src.core.validation_diagnostics import validation_diagnostic
from test_reviewed_report import prepared_result
from test_unresolved_versions import raw_report
from test_version_references import ABSENT


@pytest.mark.parametrize(
    "title",
    [
        "CVE-2026-1234",
        "`CVE-2026-1234`",
        "**CVE-2026-1234**",
        "CVE-2026-1234 / CVE-2026-5678",
        "CVE-2026-1234 and CVE-2026-5678",
        "[CVE-2026-1234](https://example.com)",
        "---",
    ],
)
def test_new_publication_rejects_headings_without_a_descriptive_name(title):
    report = raw_report(["source-example"], ABSENT).replace(
        "### Synthetic campaign", f"### {title}"
    )
    issues = validate_report_content(report, require_descriptive_titles=True)
    assert "missing_descriptive_finding_title" in {i.code for i in issues}
    assert blocking_issues(issues) == issues
    assert not validate_report_content(report)  # Historical content compatibility.


@pytest.mark.parametrize(
    "title",
    [
        "OpenSSH authentication bypass (CVE-2026-1234)",
        "Plex2Shell",
        "製品の認証回避",
        "`OpenSSH authentication bypass` (CVE-2026-1234)",
        "`OpenSSH authentication bypass`",
    ],
)
def test_descriptive_names_remain_valid(title):
    report = raw_report(["source-example"], ABSENT).replace(
        "### Synthetic campaign", f"### {title}"
    )
    assert not validate_report_content(report, require_descriptive_titles=True)


@pytest.mark.parametrize("advisory", [False, True])
def test_generated_title_requirement_is_blocking_in_both_policies(advisory):
    result = prepared_result()
    result["exploitation_report"] = result["exploitation_report"].replace(
        "### Synthetic campaign", "### ---"
    )
    with pytest.raises(ReviewedReportValidationError) as caught:
        resolve_reviewed_analysis(result, advisory=advisory)
    assert "missing_descriptive_finding_title" in {i.code for i in caught.value.issues}
    assert (
        "missing_descriptive_finding_title"
        in validation_diagnostic("report_content", caught.value)["codes"]
    )


def test_cli_blocks_identifier_only_titles_under_default_advisory_policy(
    tmp_path, monkeypatch
):
    from scripts.validate_report import main

    report = tmp_path / "report.md"
    report.write_text(
        raw_report(["source-example"], ABSENT).replace(
            "### Synthetic campaign", "### CVE-2026-1234"
        )
    )
    monkeypatch.setattr("sys.argv", ["validate_report.py", str(report)])
    assert main() == 1


@pytest.mark.parametrize(
    "quoted", ["> ## Supporting notes", "- Notes\n\n  ## Supporting notes"]
)
def test_nested_section_heading_cannot_hide_a_later_identifier_only_finding(quoted):
    report = raw_report(["source-example"], ABSENT).replace(
        "## Affected Systems and Products",
        f"{quoted}\n\n### CVE-2026-1234\n\nA second finding.\n\n## Affected Systems and Products",
    )
    issues = validate_report_content(report, require_descriptive_titles=True)
    assert "missing_descriptive_finding_title" in {issue.code for issue in issues}


def test_quoted_cve_heading_is_not_a_finding_title():
    report = raw_report(["source-example"], ABSENT).replace(
        "## Affected Systems and Products",
        "> ### CVE-2026-1234\n\n## Affected Systems and Products",
    )
    assert not validate_report_content(report, require_descriptive_titles=True)
