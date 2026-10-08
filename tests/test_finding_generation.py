"""Constructed source-grounded regressions, not historical model-output replay."""

import json

import pytest

from src.core.finding_evidence import ABSENT, EvidenceError, validate_finding_evidence
from src.core.finding_generation import compile_finding_records, render_finding_plan
from src.core.reporting import build_reporting_catalog, resolve_reporting_keys
from src.core.report_validation import validate_report_content

CVE = "CVE-2026-1234"
OTHER = "CVE-2026-5678"


def catalog_for(*texts):
    return build_reporting_catalog(
        [
            dict(
                title="Example Gateway advisory",
                source="Example publisher",
                link=f"https://example.test/advisory/{index}",
                content=text,
                content_kind="article",
            )
            for index, text in enumerate(texts)
        ]
    )


def plan_for(records):
    return {
        "findings": [
            {
                "id": record.key,
                "excerpts": [item.key for item in record.excerpts[:1]],
                **{
                    role: [item.key for item in record.excerpts if role in item.roles][
                        :1
                    ]
                    for role in ("impact", "systems", "vectors", "actors")
                },
                "vendor_links": [item.key for item in record.links],
            }
            for record in records
        ]
    }


def render(catalog):
    records = compile_finding_records(catalog)
    report = render_finding_plan(json.dumps(plan_for(records)), records, catalog)
    validate_finding_evidence(report, catalog)
    assert not validate_report_content(resolve_reporting_keys(report, catalog))
    return records, report


@pytest.mark.parametrize(
    ("text", "status", "required_prose"),
    [
        (f"{CVE} is actively exploited.", "active", "active exploitation"),
        (
            f"{CVE} exploitation has not been observed.",
            "not_observed",
            "not been observed",
        ),
        (
            f"A flaw tracked as {CVE}. Attackers are exploiting another product.",
            "unknown",
            "unknown",
        ),
        (f"{CVE} could be exploited.", "potential", "potential"),
    ],
)
def test_source_state_owns_complete_finding_and_summary(text, status, required_prose):
    _, report = render(catalog_for(text))
    assert f"**Exploitation Status**: {status}" in report
    assert required_prose in report
    if status != "active":
        assert "Attackers are exploiting another product." not in report


def test_conflicting_sources_keep_negative_evidence_and_disclosure():
    _, report = render(
        catalog_for(
            f"{CVE} is actively exploited.",
            f"{CVE} exploitation has not been observed.",
        )
    )
    assert "**Exploitation Status**: unknown" in report
    assert "conflicting" in report
    assert "not been observed" in report
    assert f"{CVE} is actively exploited." not in report


def test_mixed_joint_scope_keeps_negative_evidence_without_inventing_conflict():
    records, report = render(
        catalog_for(
            f"{CVE} exploitation has not been observed.\n\n"
            f"{OTHER} is also mentioned.\n\n"
            f"Customers should install the update for {CVE} and {OTHER}."
        )
    )
    joint = next(record for record in records if len(record.cves) == 2)
    assert joint.status == "unknown"
    assert "not been observed" in joint.state_prose
    assert "conflicting" not in joint.state_prose
    assert "**Action**: patch" in report


def test_joint_details_and_complete_recommendations_survive_unknown_state():
    catalog = catalog_for(
        "Attackers are exploiting the plugins.\n\n"
        f"Affected versions: Commerce 2.3 ({CVE}); Forms 4.5 ({OTHER}).\n\n"
        f"Customers should install the update for {CVE} and {OTHER}. "
        "Restart the service only after backing up the configuration."
    )
    records, report = render(catalog)
    joint = next(record for record in records if set(record.cves) == {CVE, OTHER})
    assert "Commerce 2.3; Forms 4.5" in report
    assert "Restart the service only after backing up the configuration." in report
    assert joint.status == "unknown"
    assert "**Exploitation Status**: active" not in report


def test_range_exclusions_and_advice_are_not_rewritten_into_affected_versions():
    _, report = render(
        catalog_for(
            f"## {CVE}\n\n{CVE} exploitation has not been observed.\n\n"
            "Affected versions:\n\nExample Gateway 2.3 and earlier (Windows only)\n\n"
            "Hosted users need no action.\n\n"
            "Customers should install the update. Restart the service afterward."
        )
    )
    assert (
        "**Affected Versions**: Example Gateway 2.3 and earlier (Windows only)"
        in report
    )
    assert "**Exceptions**: Hosted users need no action." in report
    assert (
        "Customers should install the update. Restart the service afterward." in report
    )


def test_unowned_multi_cve_release_paragraph_cannot_enter_a_singleton():
    records, report = render(
        catalog_for(
            f"The interface flaw is tracked as {CVE}.\n\n"
            "Version 2.3: 2.3-100 and older versions are affected. "
            "2.3-200 and higher versions are fixed.\n\n"
            f"Another flaw is tracked as {OTHER}."
        )
    )
    assert all("2.3" not in item.text for record in records for item in record.excerpts)
    assert f"**Affected Versions**: {ABSENT}" in report
    assert "2.3-100" not in report


@pytest.mark.parametrize(
    "mutation", ["state", "prose", "versions", "extra", "omit", "duplicate", "unknown"]
)
def test_closed_plan_rejects_fact_writes_or_incomplete_coverage(mutation):
    catalog = catalog_for(f"{CVE} exploitation has not been observed.")
    records = compile_finding_records(catalog)
    plan = plan_for(records)
    entry = plan["findings"][0]
    if mutation in {"state", "prose", "versions"}:
        entry[mutation] = "Attackers are exploiting Example Gateway 9.9."
    elif mutation == "extra":
        plan["summary"] = "Active exploitation confirmed."
    elif mutation == "omit":
        plan["findings"] = []
    elif mutation == "duplicate":
        plan["findings"].append(entry)
    else:
        entry["id"] = "finding-invented"
    with pytest.raises(EvidenceError):
        render_finding_plan(json.dumps(plan), records, catalog)


def test_another_scope_excerpt_is_not_a_valid_reference():
    catalog = catalog_for(
        f"## {CVE}\n\nThe service issue is tracked as {CVE}.\n\n"
        f"## {OTHER}\n\nThe other product issue is tracked as {OTHER}."
    )
    records = compile_finding_records(catalog)
    plan = plan_for(records)
    assert records[0].excerpts and records[1].excerpts
    plan["findings"][0]["excerpts"] = [records[1].excerpts[0].key]
    with pytest.raises(EvidenceError):
        render_finding_plan(json.dumps(plan), records, catalog)


def test_ambiguous_source_constraints_stop_compilation():
    catalog = catalog_for(
        f"{CVE} is actively exploited.\n\nAffected versions:\n\n"
        "Example Gateway 2.3 is vulnerable"
    )
    with pytest.raises(EvidenceError, match="ambiguous affected-version clause"):
        compile_finding_records(catalog)


def test_useful_triage_and_substantive_source_rollups():
    catalog = build_reporting_catalog(
        [
            dict(
                title="Example Gateway security advisory",
                source="Example publisher",
                link="https://example.test/report",
                content_kind="article",
                content=(
                    f"## {CVE}\n\n{CVE} is a critical vulnerability in Example Gateway, with a CVSS score of 9.8.\n\n"
                    f"Exploitation of {CVE} has not been observed.\n\n"
                    "Example Gateway on Windows permits server-side request forgery that could expose internal data.\n\n"
                    f"Researchers link a potential campaign targeting {CVE} to Example Group.\n\n"
                    "Affected versions: Example Gateway 2.3 (Windows only).\n\n"
                    "Customers should install the patch. Restart the service only after backing up the configuration.\n\n"
                    "See the vendor security advisory for details."
                ),
                source_links=["https://vendor.example/security/advisories/example"],
                source_link_contexts=[
                    dict(
                        url="https://vendor.example/security/advisories/example",
                        label="vendor security advisory",
                        context="See the vendor security advisory for details.",
                    )
                ],
            )
        ]
    )
    records, report = render(catalog)
    assert "**Severity**: critical" in report
    assert "**Action**: patch" in report
    assert (
        "**Vendor Links**: https://vendor.example/security/advisories/example" in report
    )
    assert "only after backing up" in report
    for heading, expected in [
        ("Affected Systems and Products", "Windows"),
        ("Attack Vectors and Techniques", "server-side request forgery"),
        ("Threat Actor Activities", "Example Group"),
    ]:
        section = report.split(f"## {heading}\n", 1)[1].split("\n## ", 1)[0]
        assert expected in section
    assert len(records) == 1


def test_joint_ownership_groups_findings_without_redundant_singletons():
    catalog = catalog_for(
        f"Affected versions: Commerce 2.3 ({CVE}); Forms 4.5 ({OTHER}).\n\n"
        f"Customers should install the patch for {CVE} and {OTHER}."
    )
    records, report = render(catalog)
    assert len(records) == 1
    assert set(records[0].cves) == {CVE, OTHER}
    assert report.count("\n### ") == 1


def test_incidental_joint_mention_does_not_duplicate_or_merge_findings():
    records, _ = render(
        catalog_for(
            f"The service flaw is tracked as {CVE}.\n\n"
            f"The unrelated product flaw is tracked as {OTHER}.\n\n"
            f"The same researcher reported {CVE} and {OTHER}."
        )
    )
    assert {record.cves for record in records} == {(CVE,), (OTHER,)}


@pytest.mark.parametrize(
    "role", ["impact", "systems", "vectors", "actors", "vendor_links"]
)
def test_rollup_and_link_references_cannot_invent_values(role):
    catalog = catalog_for(f"The service flaw is tracked as {CVE}.")
    records = compile_finding_records(catalog)
    plan = plan_for(records)
    plan["findings"][0][role] = ["invented-reference"]
    with pytest.raises(EvidenceError):
        render_finding_plan(json.dumps(plan), records, catalog)


@pytest.mark.parametrize(
    "advice",
    [
        "Customers are not advised to upgrade the appliance until the hotfix is available.",
        "Customers should not install the patch.",
        "Customers must never apply the update.",
        "Customers should upgrade only if the appliance is exposed.",
        "Customers should install the update when the maintenance window begins.",
        "Customers should install the patch. Do not install it until verification completes.",
        "Customers should install neither the patch nor the update.",
    ],
)
def test_prohibited_or_conditional_advice_never_becomes_unconditional_patch(advice):
    _, report = render(
        catalog_for(f"{CVE} exploitation has not been observed.\n\n" + advice)
    )
    assert "**Action**: patch" not in report
    assert advice in report


@pytest.mark.parametrize(
    ("advice", "action"),
    [
        ("Install the update.", "patch"),
        ("Users should apply the workaround.", "mitigate"),
        (
            "Users are advised to review the logs for indicators of compromise.",
            "investigate",
        ),
        (
            "Users are advised to review the logs. Do not review the logs until access is approved.",
            "none",
        ),
        ("Users are advised to apply no workaround.", "none"),
    ],
)
def test_action_badge_preserves_complete_directive_polarity(advice, action):
    _, report = render(
        catalog_for(f"{CVE} exploitation has not been observed.\n\n" + advice)
    )
    assert f"**Action**: {action}" in report
    assert advice in report


@pytest.mark.parametrize(
    ("rating", "severity"),
    [
        ("Its CVSS score is 7.5.", "high"),
        ("Its CVSS:3.1/AV:N/AC:L vector was published.", "unknown"),
        ("It may have a CVSS score of 9.8.", "unknown"),
        ("No CVSS score of 9.8 has been assigned.", "unknown"),
        ("It is not a critical vulnerability.", "unknown"),
    ],
)
def test_severity_requires_an_explicit_unqualified_rating(rating, severity):
    _, report = render(catalog_for(f"The issue is tracked as {CVE}. {rating}"))
    assert f"**Severity**: {severity}" in report


def test_narrative_inventory_excludes_page_furniture_and_unattributed_context():
    catalog = catalog_for(
        "October 7, 2026\n\nBy Example Reporter\n\n"
        "The logo for Example Company, whose servers expose an administration interface.\n\n"
        "A different critical vulnerability has a CVSS score of 9.8.\n\n"
        f"{CVE} is a flaw in Gateway that could allow remote code execution.\n\n"
        "The unrelated company operates Windows servers."
    )
    records, report = render(catalog)
    assert dict(records[0].fields)["Severity"] == "unknown"
    texts = [item.text for item in records[0].excerpts]
    assert texts == [
        f"{CVE} is a flaw in Gateway that could allow remote code execution."
    ]
    assert "October 7" not in report
    assert "logo" not in report
    assert "unrelated company" not in report


def test_vendor_inventory_requires_owned_explicit_advisory_link_context():
    from dataclasses import asdict
    from src.services.article_content import extract_article_content

    extracted = extract_article_content(
        f'<article><p>{CVE} is a flaw in Gateway. See the <a href="https://vendor.example/advisory">vendor security advisory</a>, '
        '<a href="https://news.example/advisory-story">news coverage</a>, and <a href="https://wiki.example/Gateway">encyclopedia</a>.</p>'
        f'<p>{OTHER} has a <a href="https://vendor.example/other">security advisory</a>.</p>'
        '<figure><a href="https://images.example/advisory.png">security advisory photo</a></figure></article>',
        "https://example.test/story",
    )
    catalog = build_reporting_catalog(
        [
            dict(
                title="Example",
                source="Publisher",
                link="https://example.test/story",
                content=extracted.text,
                source_links=extracted.links,
                source_link_contexts=[asdict(item) for item in extracted.link_contexts],
            )
        ]
    )
    records = compile_finding_records(catalog)
    record = next(item for item in records if item.cves == (CVE,))
    assert [item.url for item in record.links] == ["https://vendor.example/advisory"]
    assert record.links[0].required


def test_bare_source_urls_do_not_imply_vendor_advisory_roles():
    catalog = build_reporting_catalog(
        [
            dict(
                title="Example",
                source="Publisher",
                link="https://example.test/story",
                content=f"{CVE} is a Gateway flaw.",
                source_links=["https://news.example/security/advisory"],
            )
        ]
    )
    assert compile_finding_records(catalog)[0].links == ()


def test_owned_intrusion_narrative_has_useful_technique_and_actor_roles():
    catalog = catalog_for(
        f"Example Group gained access to the service by exploiting a vulnerability ({CVE}) in Example Platform. "
        f"The vendor issued a fix for {CVE}, which the group first began exploiting as a zero-day."
    )
    records, report = render(catalog)
    assert any("vectors" in item.roles for item in records[0].excerpts)
    assert any("actors" in item.roles for item in records[0].excerpts)
    assert "Example Group" in report.split("## Threat Actor Activities", 1)[1]


def test_optional_excerpt_keeps_its_paragraph_antecedent_and_qualifications():
    paragraph = f"{CVE} is actively exploited. Its CVSS score is 7.5. The server could permit remote code execution."
    records, report = render(catalog_for(paragraph))
    assert [item.text for item in records[0].excerpts] == [paragraph]
    assert f"**Description**: {paragraph}" in report


def test_explicit_section_does_not_make_a_foreign_cve_paragraph_optional_context():
    text = f"## {CVE}\n\n{CVE} is a service flaw. Another unrelated flaw is {OTHER}."
    records = compile_finding_records(catalog_for(text))
    record = next(item for item in records if item.cves == (CVE,))
    assert all(OTHER not in item.text for item in record.excerpts)


def test_repeated_advisory_paragraphs_do_not_cross_cve_sections():
    from dataclasses import asdict
    from src.services.article_content import extract_article_content

    extracted = extract_article_content(
        f'<article><h2>{CVE}</h2><p>See the <a href="https://vendor.example/first">vendor security advisory</a>.</p>'
        f'<h2>{OTHER}</h2><p>See the <a href="https://vendor.example/second">vendor security advisory</a>.</p></article>',
        "https://example.test/story",
    )
    catalog = build_reporting_catalog(
        [
            dict(
                title="Example",
                source="Publisher",
                link="https://example.test/story",
                content=extracted.text,
                source_links=extracted.links,
                source_link_contexts=[asdict(x) for x in extracted.link_contexts],
            )
        ]
    )
    with pytest.raises(EvidenceError) as error:
        compile_finding_records(catalog)
    assert error.value.code == "ambiguous_advisory_link_scope"


@pytest.mark.parametrize(
    "metadata",
    [
        {"cves": [CVE]},
        {"title": f"Active exploitation of {CVE}"},
        {"link": f"https://example.test/{CVE}"},
    ],
)
def test_metadata_only_cve_coverage_does_not_fabricate_body_attribution(metadata):
    article = dict(
        title="Gateway exploitation",
        source="Publisher",
        link="https://example.test/story",
        content="Attackers are exploiting the gateway. The service permits mailbox access.",
    )
    article.update(metadata)
    catalog = build_reporting_catalog([article])
    records = compile_finding_records(catalog, [CVE])
    assert len(records) == 1 and records[0].cves == (CVE,)
    assert records[0].status == "unknown"
    report = render_finding_plan(json.dumps(plan_for(records)), records, catalog)
    assert "**CVE IDs**: " + CVE in report
    assert "metadata" in report
    assert "Attackers are exploiting" not in report
    validate_finding_evidence(report, catalog)
