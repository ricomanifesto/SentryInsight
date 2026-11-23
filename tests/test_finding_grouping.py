"""Supporting articles are citations; unrelated issues remain separate findings."""

from itertools import permutations

import pytest

from src.core.finding_grouping import group_related_findings
from src.core.finding_evidence import EvidenceError
from src.core.report_findings import report_findings
from src.core.reporting import build_reporting_catalog
from src.core.reviewed_report import resolve_reviewed_analysis
from test_reviewed_report import prepared_result
from test_unresolved_versions import raw_report
from test_version_references import ABSENT, source

A = "CVE-2026-1234"
B = "CVE-2026-5678"


def finding(keys, cve=A):
    row = report_findings(raw_report(keys, ABSENT)).rows[0]
    return row.text.replace(
        "### Synthetic campaign", f"### Gateway flaw ({cve})"
    ).replace("- **Reporting**:", f"- **CVE IDs**: {cve}\n- **Reporting**:")


def report(*findings):
    return "## Active Exploitation Details\n\n" + "\n".join(findings)


def test_shared_two_cve_chain_has_one_entry_and_all_ids():
    catalog = build_reporting_catalog([source(f"{A} and {B} form an exploit chain.")])
    grouped = group_related_findings(
        report(finding(catalog, A), finding(catalog, B)), catalog
    )
    [row] = report_findings(grouped).rows
    assert set(row.cves) == {A, B}
    assert row.fields()["Recommended Actions"] == ABSENT
    assert group_related_findings(grouped, catalog) == grouped


@pytest.mark.parametrize(
    "content",
    [
        f"{A} and {B} are separate vulnerabilities.",
        f"{A} and {B} do not form an exploit chain.",
        f"{A} and {B} cannot form an exploit chain.",
        f"{A} and {B} work without an exploit chain.",
        f"{A} and {B} are described in this article.",
    ],
)
def test_distinct_issues_in_one_article_do_not_merge(content):
    catalog = build_reporting_catalog([source(content)])
    original = report(finding(catalog, A), finding(catalog, B))
    assert group_related_findings(original, catalog) == original


@pytest.mark.parametrize(
    "field,value",
    [
        ("Exploitation Status", "not_observed"),
        ("Affected Versions", "Gateway 7 (Windows only)"),
        ("Exceptions", "Linux deployments are unaffected."),
        ("Recommended Actions", "Do not restart before installing the update."),
        ("Action", "investigate"),
        ("Description", "A separate prerequisite and consequence."),
    ],
)
def test_chain_members_with_different_qualifiers_or_response_stay_separate(
    field, value
):
    catalog = build_reporting_catalog([source(f"{A} and {B} form an exploit chain.")])
    second = finding(catalog, B)
    old = report_findings(report(second)).rows[0].fields()[field]
    second = second.replace(f"**{field}**: {old}", f"**{field}**: {value}")
    original = report(finding(catalog, A), second)
    assert group_related_findings(original, catalog) == original


def test_extra_reporting_adds_links_to_the_original_finding():
    catalog = build_reporting_catalog(
        [source(f"{A} is described.", suffix) for suffix in ("first", "followup")]
    )
    first, second = catalog
    grouped = group_related_findings(
        report(finding([first]), finding([second])), catalog
    )
    [row] = report_findings(grouped).rows
    assert row.cited_keys == (first, second)
    assert (
        row.fields()["Description"] == "A campaign described by the supplied reporting."
    )


@pytest.mark.parametrize("order", list(permutations(range(3))))
def test_followup_article_on_one_chain_member_stays_in_the_original_issue(order):
    catalog = build_reporting_catalog(
        [
            source(f"{A} and {B} form an exploit chain.", "chain"),
            source(f"{A} is described.", "followup"),
        ]
    )
    chain, followup = catalog
    entries = [finding([chain], A), finding([chain], B), finding([followup], A)]
    grouped = group_related_findings(report(*(entries[i] for i in order)), catalog)
    [row] = report_findings(grouped).rows
    assert set(row.cves) == {A, B}
    assert set(row.cited_keys) == {chain, followup}


@pytest.mark.parametrize("separator", [" and ", " / ", ", "])
def test_existing_joint_heading_accepts_a_followup_for_one_member(separator):
    catalog = build_reporting_catalog(
        [
            source(f"{A} and {B} form an exploit chain.", "chain"),
            source(f"{A} is described.", "followup"),
        ]
    )
    chain, followup = catalog
    joint = (
        finding([chain])
        .replace(f"({A})", f"({A}{separator}{B})")
        .replace(f"**CVE IDs**: {A}", f"**CVE IDs**: {A}, {B}")
    )
    grouped = group_related_findings(report(joint, finding([followup])), catalog)
    [row] = report_findings(grouped).rows
    assert set(row.cves) == {A, B}
    assert set(row.cited_keys) == {chain, followup}


@pytest.mark.parametrize("advisory", [False, True])
def test_generation_groups_before_rendering_and_keeps_source_coverage(advisory):
    result = prepared_result([source(f"{A} and {B} form an exploit chain.")])
    key = result["reporting_sources"][0]["key"]
    original = result["exploitation_report"]
    row = report_findings(original).rows[0]
    result["exploitation_report"] = (
        original[: row.start]
        + finding([key], A)
        + finding([key], B)
        + original[row.end :]
    )
    reviewed = resolve_reviewed_analysis(result, advisory=advisory)
    [merged] = report_findings(reviewed.report).rows
    assert set(merged.cves) == {A, B}
    assert reviewed.coverage["counts"]["cited_sources"] == 1
    assert reviewed.coverage["counts"]["eligible_sources"] == 1


@pytest.mark.parametrize("advisory", [False, True])
def test_generation_keeps_both_articles_as_links_in_one_finding(advisory):
    result = prepared_result(
        [source(f"{A} is described.", suffix) for suffix in ("first", "followup")]
    )
    keys = [item["key"] for item in result["reporting_sources"]]
    original = result["exploitation_report"]
    row = report_findings(original).rows[0]
    result["exploitation_report"] = (
        original[: row.start]
        + finding([keys[0]])
        + finding([keys[1]])
        + original[row.end :]
    )
    reviewed = resolve_reviewed_analysis(result, advisory=advisory)
    assert len(report_findings(reviewed.report).rows) == 1
    assert "https://example.test/first" in reviewed.report
    assert "https://example.test/followup" in reviewed.report
    assert reviewed.coverage["counts"]["cited_sources"] == 2
    assert reviewed.coverage["counts"]["unrepresented_eligible_sources"] == 0


@pytest.mark.parametrize("advisory", [False, True])
def test_grouping_cannot_launder_an_uncited_vendor_link(advisory):
    articles = [
        source(f"{A} is described.", suffix) for suffix in ("first", "followup")
    ]
    vendor = "https://vendor.example/advisory"
    articles[1]["source_links"] = [vendor]
    result = prepared_result(articles)
    keys = [item["key"] for item in result["reporting_sources"]]
    original = result["exploitation_report"]
    row = report_findings(original).rows[0]
    first = finding([keys[0]]).replace(
        f"**Vendor Links**: {ABSENT}", f"**Vendor Links**: {vendor}"
    )
    result["exploitation_report"] = (
        original[: row.start] + first + finding([keys[1]]) + original[row.end :]
    )
    if not advisory:
        with pytest.raises(EvidenceError) as caught:
            resolve_reviewed_analysis(result, advisory=False)
        assert caught.value.code == "unsupported_vendor_link"
    else:
        reviewed = resolve_reviewed_analysis(result, advisory=True)
        assert vendor not in reviewed.report
        assert any(
            a["stage"] == "finding_evidence"
            and a["codes"] == ["unsupported_vendor_link"]
            and a["finding_index"] == 1
            for a in reviewed.advisories
        )


def test_source_only_findings_have_no_invented_shared_identity():
    catalog = build_reporting_catalog([source("A campaign is described.")])
    row = report_findings(raw_report(catalog, ABSENT)).rows[0]
    original = report(row.text, row.text)
    assert group_related_findings(original, catalog) == original
