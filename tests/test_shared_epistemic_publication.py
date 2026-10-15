"""Qualified evidence and failed plans through the real offline publication gate."""

import json
import re

import httpx
import pytest

from src.core.report_artifact import parse_report_artifact
from test_analyze_guards import reference_plan_from_prompt
from test_finding_generation_pipeline import REPRESENTATIVE_ARTICLES, run_real_pipeline
from test_owned_relation_contract import article
from test_publication_transaction import tree
from test_publication_transaction import public as public  # noqa: F401
from test_shared_epistemic_contract import CASES, CVE


@pytest.fixture(autouse=True)
def no_transport(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


def inputs_for(case):
    controls = json.loads(
        json.dumps(REPRESENTATIVE_ARTICLES)
        .replace("CVE-2026-1234", "CVE-2098-90001")
        .replace("CVE-2026-5678", "CVE-2098-90002")
    )
    text = case["text"]
    if case["expected"]["unsupported"]:
        # Required-relation rejection applies to a selected finding. Supply
        # existing relevance independently; the rejected operand stays intact.
        text = f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{text}"
    return [article(text, link="https://example.test/qualified-event"), *controls]


@pytest.mark.parametrize("case", CASES, ids=lambda case: case["id"])
def test_qualified_publication_or_prior_tree_preservation(monkeypatch, public, case):
    before = tree(public)
    rejected = case["expected"]["unsupported"]
    result = run_real_pipeline(
        monkeypatch,
        public / "index.md",
        articles=inputs_for(case),
        expect_model_call=not rejected,
    )
    if rejected:
        assert result["status"] == "failed"
        assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
        assert tree(public) == before
        return
    assert result["status"] == "completed", result
    report = (public / "index.md").read_text()
    findings = parse_report_artifact(report).findings
    for owner, status in case["expected"]["states"].items():
        wanted = (
            set(case["expected"]["joint_cves"])
            if owner == "joint"
            else {owner} if owner else set()
        )
        owned = [finding for finding in findings if set(finding.cve_ids) == wanted]
        assert owned and {finding.exploitation_status.value for finding in owned} == {
            status
        }
    for statement in re.split(r"(?<=[.!?])\s+", case["text"]):
        assert statement in report
    for name in (
        "index.html",
        "current-findings.json",
        "reports/index.html",
        "reports/index.json",
        "sitemap.xml",
    ):
        assert (public / name).stat().st_size


@pytest.mark.parametrize(
    "mutation",
    [
        "stronger_status",
        "strip_qualification",
        "foreign_source",
        "drop_identity",
        "missing_finding",
        "fabricated_evidence",
    ],
)
def test_plan_cannot_strengthen_or_replace_qualified_evidence(
    monkeypatch, public, mutation
):
    case = next(case for case in CASES if case["id"] == "reported-003")
    before = tree(public)

    def select(**kwargs):
        plan = json.loads(reference_plan_from_prompt(**kwargs))
        context = json.loads(
            kwargs["user_prompt"]
            .split("BEGIN FINDING RECORDS\n", 1)[1]
            .split("\nEND FINDING RECORDS", 1)[0]
        )
        owned = next(record for record in context if CVE in record["cves"])
        entry = next(row for row in plan["findings"] if row["id"] == owned["id"])
        if mutation == "stronger_status":
            entry["status"] = "active"
        elif mutation == "strip_qualification":
            entry["evidence_text"] = f"Hackers are exploiting {CVE}."
        elif mutation == "foreign_source":
            foreign = next(
                row
                for row in plan["findings"]
                if row["id"] != owned["id"] and row["actors"]
            )
            entry["actors"] = foreign["actors"]
        elif mutation == "drop_identity":
            entry["cves"] = []
        elif mutation == "missing_finding":
            plan["findings"].remove(entry)
        else:
            entry["actors"] = ["invented-confirmation"]
        return json.dumps(plan)

    result = run_real_pipeline(
        monkeypatch, public / "index.md", articles=inputs_for(case), select_plan=select
    )
    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "invalid_generation_plan"
    assert tree(public) == before
