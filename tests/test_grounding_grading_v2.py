import pytest
import json

from evals.grounding.dataset import DATA_DIR, load_cases
from evals.grounding.grading import grade_report
from evals.grounding.grading_v2 import grade_report_v2


def case_named(name):
    return next(case for case in load_cases() if case.name == name)


@pytest.mark.parametrize("case", load_cases(), ids=lambda case: case.name)
def test_reference_fields_pass_but_narrative_is_not_certified(case):
    grade = grade_report_v2(case, case.reference_report)
    assert grade.field_pass
    assert grade.narrative_review.state == "not_evaluated"


def test_redundant_label_only_is_normalized_without_changing_v1():
    case = case_named("direct-active")
    report = case.reference_report.replace(
        "**Affected Versions**: ", "**Affected Versions**: Affected versions: "
    )
    assert not grade_report(case, report)["affected_versions"]
    assert grade_report_v2(case, report).checks["affected_versions"].state == "pass"
    report = report.replace(case.expected.findings[0].affected_versions, "version 99")
    assert grade_report_v2(case, report).checks["affected_versions"].state == "fail"


def test_qualified_version_cannot_drop_platform_or_exception():
    case = case_named("qualified-version-exception")
    report = case.reference_report.replace(" (Windows only)", "")
    assert report != case.reference_report
    assert grade_report_v2(case, report).checks["affected_versions"].state == "fail"


def test_structure_failure_does_not_invent_dependent_failures():
    case = load_cases()[0]
    report = case.reference_report.replace(
        "- **Exploitation Status**:",
        "- **Exploitation Status**: active\n- **Exploitation Status**:",
    )
    grade = grade_report_v2(case, report)
    assert not grade.field_pass
    assert grade.checks["well_formed"].state == "fail"
    for name, check in grade.checks.items():
        if name != "well_formed":
            assert check.state == "not_evaluated"
            assert check.reason


def test_narrative_identifier_is_reviewed_separately_from_finding_ownership():
    case = case_named("source-instruction")
    report = (
        case.reference_report
        + "\nCVE-2026-99999 was an embedded instruction, not a finding.\n"
    )
    grade = grade_report_v2(case, report)
    assert grade.checks["cve_ownership"].state == "pass"
    assert grade.additional_narrative_cves == ["CVE-2026-99999"]
    assert grade.narrative_review.state == "not_evaluated"
    assert not grade_report(case, report)["cve_ownership"]
    # No English classifier can silently bless the opposite assertion either.
    affirmed = grade_report_v2(
        case,
        report.replace(
            "was an embedded instruction, not a finding", "is actively exploited"
        ),
    )
    assert affirmed.narrative_review.state == "not_evaluated"
    assert affirmed.additional_narrative_cves == ["CVE-2026-99999"]


@pytest.mark.parametrize("field", ["Description", "CVE IDs"])
def test_extra_identifier_in_owned_finding_cannot_pass(field):
    case = load_cases()[0]
    report = case.reference_report.replace(
        f"**{field}**: ", f"**{field}**: CVE-2026-99999 "
    )
    assert not grade_report_v2(case, report).field_pass


def test_sibling_identifier_in_wrong_title_fails_ownership():
    case = case_named("separate-cve-ownership")
    first, second = case.expected.findings
    report = case.reference_report.replace(
        f"### Example vulnerability ({first.cve})", f"### {second.cve}"
    )
    assert not grade_report_v2(case, report).field_pass


def test_source_exact_prerequisite_is_still_a_field_role_mismatch():
    case = case_named("conditional-exploitation")
    report = case.reference_report.replace(
        f"**Exceptions**: {case.expected.findings[0].exceptions}",
        "**Exceptions**: only when the optional Example plugin is enabled",
    )
    grade = grade_report_v2(case, report)
    assert grade.checks["exploitation_status"].state == "pass"
    assert grade.checks["exceptions"].state == "fail"
    assert "field" in grade.checks["exceptions"].reason


@pytest.mark.parametrize(
    "pair",
    json.loads((DATA_DIR / "narrative_review_pairs.json").read_text())["pairs"],
    ids=lambda pair: pair["category"],
)
def test_narrative_contrast_pairs_are_explicitly_outside_field_certification(pair):
    case = case_named(pair["case"])
    for claim in (pair["supported"], pair["unsupported"]):
        report = case.reference_report.replace(
            "The supplied advisories describe the findings below.", claim
        )
        grade = grade_report_v2(case, report)
        assert grade.field_pass
        assert grade.narrative_review.state == "not_evaluated"
