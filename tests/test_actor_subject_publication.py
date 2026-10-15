"""Accepted actor facts through the real offline graph and publication gate."""

import json

import httpx
import pytest

from src.core.cve import extract_cve_ids
from src.core.report_artifact import parse_report_artifact
from test_actor_subject_contract import FROZEN, A
from test_analyze_guards import reference_plan_from_prompt
from test_finding_generation_pipeline import run_real_pipeline, REPRESENTATIVE_ARTICLES
from test_owned_relation_contract import article
from test_publication_transaction import tree
from test_publication_transaction import public as public  # noqa: F401

CASES = [
    case
    for case in FROZEN["typed_cases"]
    if len(case["sources"]) == 1
    and not case["sources"][0].get("document_context")
    and case["id"] != "ordinary-use-context"
]


@pytest.fixture(autouse=True)
def no_transport(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


def inputs_for(case):
    # Existing independent breadth controls have disjoint identities, so they
    # cannot settle the actor finding's status or supply its participants.
    controls = json.loads(
        json.dumps(REPRESENTATIVE_ARTICLES)
        .replace("CVE-2026-1234", "CVE-2098-90001")
        .replace("CVE-2026-5678", "CVE-2098-90002")
    )
    return [
        article(case["sources"][0]["text"], link="https://example.test/actor"),
        *controls,
    ]


@pytest.mark.parametrize("case", CASES, ids=lambda case: case["id"])
def test_owned_actor_publication_and_required_rejection(monkeypatch, public, case):
    before = tree(public)
    rejected = case.get("expected_unsupported", False)
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
    states = dict(case.get("states", {}))
    if "expected_status" in case:
        states.update(
            {
                cve: case["expected_status"]
                for cve in extract_cve_ids(case["sources"][0]["text"])
            }
        )
    for cve, status in states.items():
        owned = [finding for finding in findings if cve in finding.cve_ids]
        assert owned and {finding.exploitation_status.value for finding in owned} == {
            status
        }
    if case.get("extra_roles"):
        actors = report.split("## Threat Actor Activities", 1)[1].split("\n## ", 1)[0]
        assert case["sources"][0]["text"] in actors
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
        "foreign_actor",
        "missing_actor",
        "fabricated_actor",
        "drop_identity",
    ],
)
def test_actor_plan_cannot_rewrite_or_cross_owners(monkeypatch, public, mutation):
    case = next(case for case in CASES if case["id"] == "condition-wrapper")
    before = tree(public)

    def select(**kwargs):
        plan = json.loads(reference_plan_from_prompt(**kwargs))
        context = json.loads(
            kwargs["user_prompt"]
            .split("BEGIN FINDING RECORDS\n", 1)[1]
            .split("\nEND FINDING RECORDS", 1)[0]
        )
        owned = next(record for record in context if A in record["cves"])
        entry = next(row for row in plan["findings"] if row["id"] == owned["id"])
        if mutation == "stronger_status":
            entry["status"] = "active"
        elif mutation == "strip_qualification":
            entry["actor_text"] = "Hackers are actively exploiting CVE-2026-1234."
        elif mutation == "foreign_actor":
            foreign = next(
                row
                for row in plan["findings"]
                if row["id"] != owned["id"] and row["actors"]
            )
            entry["actors"] = foreign["actors"]
        elif mutation == "missing_actor":
            entry["actors"] = []
        elif mutation == "fabricated_actor":
            entry["actors"] = ["publisher-context"]
        else:
            entry["cves"] = []
        return json.dumps(plan)

    result = run_real_pipeline(
        monkeypatch, public / "index.md", articles=inputs_for(case), select_plan=select
    )
    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "invalid_generation_plan"
    assert tree(public) == before
