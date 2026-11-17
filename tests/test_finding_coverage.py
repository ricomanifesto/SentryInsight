"""Article metadata and background links must not manufacture findings."""

import json

import pytest

from src.core.analyze import collect_exploitation_relevant_prompt_cves
from src.core.article_prompt import format_article_summary
from src.core.exploitation_prompt import build_exploitation_prompt
from src.core.reporting import reporting_key
from src.core.report_validation import (
    blocking_issues,
    missing_expected_cve_ids,
    validate_report_content,
)
from src.core.source_review import prepare_source_review
from test_report_validation import VALID_REPORT
from test_version_references import source

A = "CVE-2026-1234"
B = "CVE-2026-5678"


@pytest.mark.parametrize(
    "background",
    [
        f"For background, {B} was exploited in an earlier campaign.",
        f"## Background\n\n{B} was exploited in an earlier campaign.",
        f"Related reporting: {B} was exploited in an earlier campaign.",
        f"A separate patch-only issue {B} is also mentioned.",
    ],
)
def test_background_only_metadata_does_not_force_a_standalone_finding(background):
    article = source(f"Attackers are exploiting {A}.\n\n{background}")
    article["cves"] = [A, B]
    assert collect_exploitation_relevant_prompt_cves(
        format_article_summary(article)
    ) == [A]


def test_independent_current_evidence_is_not_lost_to_a_background_mention():
    article = source(
        f"Attackers are exploiting {A}.\n\n"
        f"For background, {B} was previously discussed.\n\n"
        f"New telemetry confirms attackers are exploiting {B}."
    )
    article["cves"] = [A, B]
    assert set(
        collect_exploitation_relevant_prompt_cves(format_article_summary(article))
    ) == {A, B}


def test_prompt_groups_reporting_and_preserves_complete_evidence():
    content = f"{A} and {B} form an exploit chain.\n\nInstall the update only after backing up."
    prompt = build_exploitation_prompt(prepare_source_review([source(content)]))
    assert (
        "one finding per coherent vulnerability or explicitly supported exploit chain"
        in prompt
    )
    assert "additional articles belong in that finding's Reporting field" in prompt
    assert "Background-only mentions do not require standalone findings" in prompt
    assert "at most two concise sentences" in prompt
    assert content in prompt
    assert "complete recommendation blocks" in prompt


def required_coverage(articles, *, advisory):
    plan = prepare_source_review(articles, advisory=advisory)
    assert plan.eligible_keys
    prompt = build_exploitation_prompt(plan)
    assert "BEGIN REQUIRED CVE COVERAGE\n" in prompt
    contract = json.loads(
        prompt.split("BEGIN REQUIRED CVE COVERAGE\n", 1)[1].split(
            "\nEND REQUIRED CVE COVERAGE", 1
        )[0]
    )
    return prompt, contract


@pytest.mark.parametrize("advisory", [False, True])
def test_prompt_names_required_cves_and_their_original_reporting_keys(advisory):
    article = source(f"Attackers are actively exploiting {A}.", "primary")
    prompt, contract = required_coverage([article], advisory=advisory)
    assert contract == [{"cve": A, "reporting_keys": [reporting_key(article["link"])]}]
    assert article["content"] in prompt
    assert "Coverage does not establish active exploitation" in prompt


@pytest.mark.parametrize("advisory", [False, True])
@pytest.mark.parametrize(
    "background",
    [
        f"For background, {B} was exploited in an earlier campaign.",
        f"## Background\n\n{B} was exploited in an earlier campaign.",
        f"Related reporting: {B} was exploited in an earlier campaign.",
    ],
)
def test_prompt_inventory_excludes_background_but_keeps_its_evidence(
    advisory, background
):
    article = source(f"Attackers are exploiting {A}.\n\n{background}", "primary")
    article["cves"] = [A, B]
    prompt, contract = required_coverage([article], advisory=advisory)
    assert [row["cve"] for row in contract] == [A]
    assert background in prompt


@pytest.mark.parametrize("advisory", [False, True])
def test_negated_exploitation_does_not_manufacture_a_required_finding(advisory):
    article = source(f"There is no evidence of exploitation of {A}.", "negative")
    article["cves"] = [A]
    prompt, contract = required_coverage([article], advisory=advisory)
    assert contract == []
    assert article["content"] in prompt


@pytest.mark.parametrize("advisory", [False, True])
def test_extra_reporting_is_one_cve_obligation_with_both_source_keys(advisory):
    first = source(f"Attackers are exploiting {A}.", "first")
    second = source(f"New observations confirm exploitation of {A}.", "second")
    prompt, contract = required_coverage([second, first], advisory=advisory)
    assert contract == [
        {
            "cve": A,
            "reporting_keys": sorted(reporting_key(x["link"]) for x in [first, second]),
        }
    ]
    assert "additional articles belong in that finding's Reporting field" in prompt


@pytest.mark.parametrize("advisory", [False, True])
def test_joint_chain_lists_every_required_identity_without_forcing_separate_findings(
    advisory,
):
    article = source(f"Attackers exploit {A} and {B} together as one chain.", "chain")
    prompt, contract = required_coverage([article], advisory=advisory)
    assert contract == [
        {"cve": cve, "reporting_keys": [reporting_key(article["link"])]}
        for cve in [A, B]
    ]
    assert (
        "source-explicit chain may cover multiple listed CVEs in one finding" in prompt
    )


@pytest.mark.parametrize(
    "location", ["summary", "coverage", "attribution", "url", "description"]
)
def test_expected_cve_requires_finding_identity_not_an_incidental_mention(location):
    report = VALID_REPORT.replace(
        "### Example Vulnerability\n",
        f"### Example Vulnerability\n- **CVE IDs**: {A}\n",
    )
    if location == "summary":
        report = report.replace(
            "Recent exploitation activity", f"{B}: Recent exploitation activity"
        )
    elif location == "coverage":
        report += f"\n## Source Coverage and Review\n\nRetained source names {B}.\n"
    elif location == "attribution":
        report += f"\n## Source Attribution\n\nA source names {B}.\n"
    elif location == "url":
        report = report.replace(
            "- **Impact**:", f"- **Reporting**: https://example.test/{B}\n- **Impact**:"
        )
    else:
        report = report.replace(
            "a vulnerable service.", f"a vulnerable service; {B} is historical context."
        )
    assert missing_expected_cve_ids(report, [A, B]) == [B]


@pytest.mark.parametrize("field", ["CVE IDs", "CVE ID"])
def test_one_joint_finding_covers_each_explicit_member_of_the_chain(field):
    report = VALID_REPORT.replace(
        "### Example Vulnerability\n",
        f"### Example Vulnerability\n- **{field}**: {A}, {B}\n",
    )
    assert missing_expected_cve_ids(report, [A, B]) == []


def test_historical_cve_heading_still_supplies_finding_identity():
    report = VALID_REPORT.replace(
        "### Example Vulnerability", f"### Example Vulnerability ({A})"
    )
    assert missing_expected_cve_ids(report, [A]) == []


def test_missing_required_finding_identity_is_blocking():
    report = VALID_REPORT.replace(
        "Recent exploitation activity", f"{B}: Recent exploitation activity"
    )
    issues = validate_report_content(report, expected_cves=[B])
    assert [issue.code for issue in issues] == ["missing_expected_cves"]
    assert blocking_issues(issues) == issues


@pytest.mark.parametrize(
    "cves", [["CVE-2026-1111", "CVE-2026-2222"], ["CVE-2026-12345678"]]
)
def test_summary_source_metadata_does_not_replace_findings(cves):
    report = VALID_REPORT.replace(
        "Recent exploitation activity is concentrated in edge systems.",
        "Recent exploitation activity is concentrated in edge systems. "
        + " and ".join(cves)
        + " are included in source metadata.",
    )
    assert missing_expected_cve_ids(report, cves) == sorted(cves)
