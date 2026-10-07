import asyncio
import json
from unittest.mock import AsyncMock

import pytest

from src.core import finding_evidence as evidence
from src.core.reporting import build_reporting_catalog
from test_analyze_guards import import_analyze_with_stubs
from test_generation_grounding import ABSENT, CVE, OTHER, finding, source


def reject(report, catalog):
    with pytest.raises(evidence.EvidenceError) as caught:
        evidence.validate_finding_evidence(report, catalog)
    return evidence.grounding_failure_diagnostic(report, catalog, caught.value)


def joint_case(*, unscoped_advice=False):
    # Synthetic analogue: joint version attribution, unscoped exploitation.
    advice = f"Customers should install the update for {CVE} and {OTHER}."
    if unscoped_advice:
        advice = "Customers should install the update. Check for signs of compromise."
    article = source(
        "Attackers are exploiting the plugins.\n\n"
        f"Affected versions: Commerce 2.3 ({CVE}); Forms 4.5 ({OTHER}).\n\n" + advice
    )
    catalog = build_reporting_catalog([article])
    candidate = finding(next(iter(catalog)), "Commerce 2.3; Forms 4.5")
    candidate = candidate.replace(CVE, f"{CVE}, {OTHER}")
    candidate = candidate.replace(
        "**Exploitation Status**: active", "**Exploitation Status**: unknown"
    )
    candidate = candidate.replace("A service flaw.", "Exploitation status is unknown.")
    candidate = candidate.replace(
        f"**Recommended Actions**: {ABSENT}", f"**Recommended Actions**: {advice}"
    )
    return article, catalog, "## Active Exploitation Details\n\n" + candidate


@pytest.mark.parametrize("scope", [(CVE,), (OTHER,), (CVE, OTHER)])
@pytest.mark.parametrize("mutation", [None, "badge", "prose"])
def test_unscoped_article_keeps_singleton_and_combined_findings_conservative(
    scope, mutation
):
    _, catalog, report = joint_case(unscoped_advice=True)
    if len(scope) == 1:
        # Joint version attribution and unowned advice cannot become singleton facts.
        candidate = finding(next(iter(catalog))).replace(CVE, scope[0])
        candidate = candidate.replace(
            "**Exploitation Status**: active", "**Exploitation Status**: unknown"
        ).replace("A service flaw.", "Exploitation status is unknown.")
        report = "## Active Exploitation Details\n\n" + candidate
        for name in evidence.DETAIL_FIELDS:
            assert f"**{name}**: {ABSENT}" in report
    else:
        assert "**Affected Versions**: Commerce 2.3; Forms 4.5" in report
        assert (
            "**Recommended Actions**: Customers should install the update. "
            "Check for signs of compromise." in report
        )
    context = next(
        item
        for item in evidence.build_finding_detail_context(catalog)
        if set(item["cves"]) == set(scope)
    )
    assert context["exploitation"] == {"status": "unknown", "conflicting": False}
    if len(scope) == 1:
        assert not any(span["role"] == "body" for span in context["spans"])
    evidence.validate_finding_evidence(report, catalog)
    if mutation is None:
        return
    if mutation == "badge":
        report = report.replace(
            "**Exploitation Status**: unknown", "**Exploitation Status**: active"
        )
        expected = ("unsupported_exploitation_status", "Exploitation Status")
    else:
        report = report.replace(
            "Exploitation status is unknown.", "Attackers are exploiting the plugins."
        )
        expected = ("unsupported_finding_exploitation_claim", "prose")
    diagnostic = reject(report, catalog)
    assert (diagnostic["code"], diagnostic["field"]) == expected
    assert set(diagnostic["cves"]) == set(scope)


@pytest.mark.parametrize(
    ("old", "new", "code", "field", "expected", "observed"),
    [
        (
            "**Exploitation Status**: unknown",
            "**Exploitation Status**: active",
            "unsupported_exploitation_status",
            "Exploitation Status",
            "unknown",
            "active",
        ),
        (
            "Exploitation status is unknown.",
            "Attackers are exploiting the plugins.",
            "unsupported_finding_exploitation_claim",
            "prose",
            False,
            True,
        ),
        (
            "## Active Exploitation Details",
            "## Executive Summary\n\nActive exploitation confirmed.\n\n## Active Exploitation Details",
            "unsupported_summary_exploitation_claim",
            "summary",
            False,
            True,
        ),
        (
            "Commerce 2.3; Forms 4.5",
            "Commerce 2.3",
            "missing_affected_version_entries",
            "Affected Versions",
            2,
            1,
        ),
        (
            "Commerce 2.3; Forms 4.5",
            "Commerce 2.3; Forms 4.5; SECRET Product 9.9",
            "unsupported_affected_version_entry",
            "Affected Versions",
            2,
            3,
        ),
    ],
)
def test_joint_article_distinguishes_rejected_assertions(
    old, new, code, field, expected, observed
):
    _, catalog, report = joint_case()
    evidence.validate_finding_evidence(report, catalog)
    context = evidence.build_finding_detail_context(catalog)
    assert all(item["exploitation"]["status"] == "unknown" for item in context)
    assert any(set(item["cves"]) == {CVE, OTHER} for item in context)
    diagnostic = reject(report.replace(old, new), catalog)
    assert diagnostic["code"] == code
    assert diagnostic["field"] == field
    assert diagnostic["expected"] == expected
    assert diagnostic["observed"] == observed
    assert "SECRET" not in json.dumps(diagnostic)


def test_generation_unknown_example_agrees_with_badge_and_narrative_guards(monkeypatch):
    article, catalog, candidate = joint_case()
    analyze = import_analyze_with_stubs()
    client = type("Client", (), {"generate": AsyncMock(return_value=candidate)})()
    monkeypatch.setattr(analyze, "build_model_client", lambda **_: client)
    result = asyncio.run(analyze.analyze_exploitation([article], {}))
    prompt = client.generate.call_args.kwargs["user_prompt"]
    assert (
        'Unknown-scope example: use Exploitation Status: unknown and prose "Exploitation status is unknown."'
        in prompt
    )
    assert "titles, descriptions, Status prose, and the Executive Summary" in prompt
    evidence.validate_finding_evidence(result["exploitation_report"], catalog)
    assert client.generate.await_count == 1


@pytest.mark.parametrize(
    "status",
    ["PRIVATE " * 1000, "https://secret.test/token", "", None, "observed"],
    ids=["oversized", "url", "blank", "absent", "observed"],
)
def test_status_diagnostic_never_logs_unrecognized_model_values(status):
    _, catalog, report = joint_case()
    candidate = (
        report.replace("- **Exploitation Status**: unknown\n", "")
        if status is None
        else report.replace(
            "**Exploitation Status**: unknown", f"**Exploitation Status**: {status}"
        )
    )
    diagnostic = reject(candidate, catalog)
    assert diagnostic["code"] == "unsupported_exploitation_status"
    assert diagnostic["expected"] == "unknown"
    assert diagnostic["observed"] == (
        "observed"
        if status == "observed"
        else "missing" if status is None else "invalid"
    )
    assert "PRIVATE" not in json.dumps(diagnostic)
    assert "secret.test" not in json.dumps(diagnostic)


@pytest.mark.parametrize(
    ("content", "prose", "code", "field"),
    [
        (
            f"{CVE} has not been exploited.",
            "Exploitation is unconfirmed.",
            "missing_negative_exploitation_evidence",
            "prose",
        ),
        (
            f"{CVE} is actively exploited. {CVE} has not been exploited.",
            "No exploitation has been observed.",
            "missing_conflicting_exploitation_evidence",
            "prose",
        ),
    ],
)
def test_missing_disclosures_have_safe_boolean_diagnostics(content, prose, code, field):
    catalog = build_reporting_catalog([source(content)])
    status = evidence.assess_exploitation(list(catalog.values()), [CVE]).status
    candidate = finding(next(iter(catalog))).replace(
        "**Exploitation Status**: active", f"**Exploitation Status**: {status}"
    )
    candidate = candidate.replace("A service flaw.", prose)
    diagnostic = reject("## Active Exploitation Details\n\n" + candidate, catalog)
    assert (diagnostic["code"], diagnostic["field"]) == (code, field)
    assert diagnostic["expected"] is True
    assert diagnostic["observed"] is False


@pytest.mark.parametrize(
    ("old", "new", "code", "field"),
    [
        (
            "**Action**: monitor",
            "**Action**: monitor\n- **Action**: patch",
            "duplicate_finding_field",
            None,
        ),
        (
            "**Reporting**:",
            "**Wrong Reporting**:",
            "missing_retained_source_evidence",
            "Reporting",
        ),
        (
            "**Action**: monitor",
            "**Action**: patch",
            "action_without_recommendation",
            "Action",
        ),
        (f"- **Exceptions**: {ABSENT}\n", "", "missing_detail_field", "Exceptions"),
        (
            f"**Exceptions**: {ABSENT}",
            "**Exceptions**: PRIVATE users are exempt",
            "exception_not_grounded",
            "Exceptions",
        ),
        (
            f"**Vendor Links**: {ABSENT}",
            "**Vendor Links**: not-a-url-PRIVATE",
            "invalid_vendor_link",
            "Vendor Links",
        ),
        (
            f"**Vendor Links**: {ABSENT}",
            "**Vendor Links**: https://secret.test/token",
            "unsupported_vendor_link",
            "Vendor Links",
        ),
    ],
)
def test_structural_and_detail_failures_have_distinct_codes(old, new, code, field):
    catalog = build_reporting_catalog([source(f"{CVE} is actively exploited.")])
    report = "## Active Exploitation Details\n\n" + finding(next(iter(catalog)))
    diagnostic = reject(report.replace(old, new), catalog)
    assert diagnostic["code"] == code
    assert diagnostic["field"] == field
    assert "PRIVATE" not in json.dumps(diagnostic)
    assert "secret.test" not in json.dumps(diagnostic)


def test_recommendation_omission_is_distinct_from_truncation():
    _, catalog, report = joint_case()
    advice = f"Customers should install the update for {CVE} and {OTHER}."
    missing = reject(report.replace(advice, ABSENT), catalog)
    truncated = reject(
        report.replace(advice, f"Customers should install the update for {CVE}."),
        catalog,
    )
    assert missing["code"] == "missing_source_details"
    assert truncated["code"] == "recommendation_not_grounded"
    assert missing["field"] == truncated["field"] == "Recommended Actions"


def test_untrusted_diagnostic_context_is_redacted_at_log_boundary():
    error = evidence.EvidenceError(
        "PRIVATE", field="PRIVATE", expected="PRIVATE", observed="PRIVATE"
    )
    diagnostic = evidence.grounding_failure_diagnostic("PRIVATE", {}, error)
    assert diagnostic["field"] is None
    assert diagnostic["expected"] == diagnostic["observed"] == "invalid"
    assert "PRIVATE" not in json.dumps(diagnostic)


@pytest.mark.parametrize(
    ("versions", "code"),
    [
        ("Example 2.3 (Windows]", "ambiguous_affected_version_grouping"),
        ("Example Gateway", "ambiguous_affected_version_continuation"),
        (
            "customers are recommended to install the update",
            "non_affected_version_clause",
        ),
        (
            "users of Example 2.3 are not unaffected",
            "ambiguous_affected_version_polarity",
        ),
    ],
)
def test_version_parser_failures_keep_specific_codes(versions, code):
    catalog = build_reporting_catalog([source(f"{CVE} is actively exploited.")])
    diagnostic = reject(
        "## Active Exploitation Details\n\n" + finding(next(iter(catalog)), versions),
        catalog,
    )
    assert diagnostic["code"] == code
    assert diagnostic["field"] == "Affected Versions"
