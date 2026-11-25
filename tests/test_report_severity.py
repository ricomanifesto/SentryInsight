"""Inert severity and generation reliability checks at the publishing boundary."""

import asyncio
import json
import re

import pytest

from src.core.report_artifact import parse_report_artifact
from src.core.report_findings import report_findings
from src.core.report_severity import critical_first, restore_source_severity
from src.core.reporting import ReportingSource
from src.core.source_review import (
    PLAN_KEY,
    digest,
    prepare_source_review,
    review_articles,
)
from test_informed_repair import (
    TITLES,
    draft,
    finding,
    install,
    outcomes,
    run,
    world,
)
from test_workflow_guards import import_workflow_with_stubs

CVE = "CVE-2099-1001"
OTHER = "CVE-2099-1002"


@pytest.mark.parametrize(
    "cited,additional,expected",
    [
        (f"{CVE} is rated critical.", "", "critical"),
        (f"{CVE} is a critical-severity vulnerability.", "", "critical"),
        (f"{CVE} (critical severity) affects the example.", "", "critical"),
        (f"{CVE} has a severity of HIGH.", "", "high"),
        (f"{CVE} is rated critical.", f"{CVE} is rated medium.", "unknown"),
        (f"{CVE} is rated critical.", f"{CVE} is not critical.", "unknown"),
        (f"{CVE} is rated critical and high.", f"{CVE} is rated high.", "unknown"),
        (f"{CVE} was initially rated critical.", "", "unknown"),
        (f"{CVE} is not rated critical.", "", "unknown"),
        (f"{CVE} and {OTHER} are rated critical.", "", "unknown"),
        (f"{CVE} applies. {OTHER} is rated critical.", "", "unknown"),
        (f"{CVE} has a CVSS score of 9.9.", "", "unknown"),
        (f"A summary names {CVE}.", f"{CVE} is rated critical.", "unknown"),
    ],
)
def test_recovery_requires_unanimous_exact_evidence_with_a_cited_source(
    cited, additional, expected
):
    first = ReportingSource("one", "A", "A report", "https://example.test/one", cited)
    second = ReportingSource(
        "two", "B", "B report", "https://example.test/two", additional
    )
    original = draft([finding(TITLES[0], first.key, **{"CVE IDs": CVE})])
    catalog = {first.key: first, second.key: second}
    recovered, count = restore_source_severity(original, catalog)
    assert count == (expected != "unknown")
    row = report_findings(recovered).rows[0]
    assert row.fields()["Severity"] == expected
    assert row.cves == (CVE,)
    assert row.cited_keys == (first.key,)
    assert restore_source_severity(recovered, catalog) == (recovered, 0)


def test_does_not_guess_for_a_joint_or_no_cve_finding_or_rewrite_existing_label():
    evidence = ReportingSource(
        "one", "A", "A report", "https://example.test/one", f"{CVE} is rated critical."
    )
    original = draft(
        [
            finding(TITLES[0], evidence.key, **{"CVE IDs": f"{CVE}, {OTHER}"}),
            finding(TITLES[1], evidence.key),
            finding(TITLES[2], evidence.key, **{"CVE IDs": CVE, "Severity": "high"}),
        ]
    )
    assert restore_source_severity(original, {evidence.key: evidence}) == (original, 0)


def test_critical_partition_preserves_nonfinding_text_and_handles_terminal_row():
    original = (
        "## Active Exploitation Details\n\nIntro before findings.\n\n"
        + finding(TITLES[0], "one", Severity="medium")
        + finding(TITLES[1], "two", Severity="critical").rstrip()
    )
    ordered = critical_first(original)
    assert ordered.startswith(
        "## Active Exploitation Details\n\nIntro before findings.\n\n"
    )
    assert not ordered.endswith("\n")
    assert [row.title for row in report_findings(ordered).rows] == TITLES[:2][::-1]
    assert critical_first(ordered) == ordered


def _publish(tmp_path, plan, result, raw, *, mode="advisory"):
    articles = review_articles(plan, eligible_only=False)
    plan = prepare_source_review(articles, advisory=mode == "advisory")
    state = {
        "analysis_results": {
            **result,
            PLAN_KEY: plan.packet,
            "exploitation_report": raw,
        },
        "filtered_articles": articles,
        PLAN_KEY: plan.packet,
        "articles_fingerprint": digest(
            {"generation_schema": 5, "plan_id": plan.packet["plan_id"]}
        ),
        "config": {
            "output_path": str(tmp_path / "index.md"),
            "analysis": {"grounding": mode},
        },
        "status": "started",
    }
    return asyncio.run(import_workflow_with_stubs().generate_report(state))


def test_generation_publishes_one_stable_order_in_markdown_json_and_html(tmp_path):
    plan, keys, results = world(
        4,
        [
            f"{CVE} is rated critical.",
            "A proxy.",
            f"{OTHER} is rated critical.",
            "A switch.",
        ],
    )
    raw = draft(
        [
            finding(TITLES[0], keys[0], **{"CVE IDs": CVE, "Severity": "critical"}),
            finding(TITLES[1], keys[1], Severity="high"),
            finding(TITLES[2], keys[2], **{"CVE IDs": OTHER}),
            finding(TITLES[3], keys[3], Severity="medium"),
        ]
    )
    receipt = _publish(tmp_path, plan, results, raw)
    assert receipt["report_generated"] is True
    assert [(item["kind"], item["outcome"]) for item in receipt["repair_attempts"]] == [
        ("original", "validated")
    ]
    artifact = parse_report_artifact((tmp_path / "index.md").read_text())
    json_report = json.loads((tmp_path / "current-findings.json").read_text())
    expected = ["critical", "critical", "high", "medium"]
    assert [x.severity.value for x in artifact.findings] == expected
    assert [x.title for x in artifact.findings] == [TITLES[i] for i in (0, 2, 1, 3)]
    assert json_report["finding_count"] == 4
    assert json_report["cve_ids"] == [CVE, OTHER]
    html = (tmp_path / "index.html").read_text()
    embedded = json.loads(
        html.split('<script id="report-metadata" type="application/json">', 1)[1].split(
            "</script>", 1
        )[0]
    )
    assert [x["severity"] for x in embedded["findings"]] == expected
    assert [x["slug"] for x in embedded["findings"]] == [
        x.slug for x in artifact.findings
    ]
    assert re.findall(r'data-severity="(\w+)"', html) == expected
    assert [x.cve_ids for x in artifact.findings] == [(CVE,), (OTHER,), (), ()]
    assert artifact.source_coverage["counts"]["cited_sources"] == 4
    assert any(
        "severity_recovered_from_sources" in item["codes"]
        for item in receipt["grounding_advisories"]
    )


def test_all_unknown_critical_prose_is_a_named_advisory_not_inferred_severity(tmp_path):
    plan, keys, results = world()
    raw = draft([finding(TITLES[0], keys[0]), finding(TITLES[1], keys[1])]).replace(
        "The supplied reporting describes campaigns.",
        "The supplied reporting mentions critical vulnerabilities.",
    )
    receipt = _publish(tmp_path, plan, results, raw)
    assert receipt["report_generated"] is True
    [cue] = [
        item
        for item in receipt["grounding_advisories"]
        if "all_severity_unknown_with_critical_claim" in item["codes"]
    ]
    assert cue["field"] == "Severity"
    assert cue["observed"] == 0
    actual = parse_report_artifact((tmp_path / "index.md").read_text())
    assert [row.severity.value for row in actual.findings] == ["unknown", "unknown"]


def test_repair_targets_original_markdown_and_cve_rows_before_sorting(monkeypatch):
    plan, keys, results = world(4)
    proxy = finding(TITLES[1], keys[1], Severity="high")
    switch = finding(TITLES[3], keys[3], Severity="medium")
    stub = install(monkeypatch, [proxy, switch])
    raw = draft(
        [
            finding(TITLES[0], keys[0], Severity="critical"),
            proxy.replace("- **Severity**", "- **Impact**\n- **Severity**"),
            finding(TITLES[2], keys[2], Severity="critical"),
            finding(
                TITLES[3], keys[3], **{"Severity": "medium", "CVE IDs": "Not assigned"}
            ),
        ]
    )
    result = run(results, raw, plan)
    assert outcomes(result) == [
        ("original", "repairable", "malformed_markdown", "rejected"),
        ("repair_finding", "repairable", "invalid_cve_ids", "rejected"),
        ("repair_finding", "repairable", "invalid_cve_ids", "repaired"),
    ]
    assert [line["finding_index"] for line in result.attempts] == [2, 4, 4]
    assert len(stub.calls) == 2
    assert [row.title for row in result.artifact.findings] == [
        TITLES[i] for i in (0, 2, 1, 3)
    ]


def test_hard_artifact_failure_keeps_last_good_public_files(tmp_path):
    plan, keys, results = world()
    raw = draft([finding(TITLES[0], keys[0], Severity="critical")])
    assert _publish(tmp_path, plan, results, raw)["report_generated"] is True
    public = [
        tmp_path / name for name in ("index.md", "index.html", "current-findings.json")
    ]
    before = [p.read_bytes() for p in public]
    malformed = draft(
        [finding(TITLES[1], keys[1], **{"CVE IDs": "CVE-2099-10", "Severity": "high"})]
    )
    failed = _publish(tmp_path, plan, results, malformed)
    assert failed["status"] == "failed"
    assert failed["failure_diagnostic"]["field"] == "CVE IDs"
    assert failed["report_generated"] is False
    assert [p.read_bytes() for p in public] == before
