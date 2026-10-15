"""Actual offline graph, complete source ownership and failed publication."""

import json
from pathlib import Path

import httpx
import pytest

from src.core.report_artifact import parse_report_artifact
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article
from test_publication_transaction import tree
from test_publication_transaction import public as public  # noqa: F401

FROZEN = json.loads(
    (Path(__file__).parent / "fixtures/valency_attack_publication.json").read_text()
)
SOURCES = {c["id"]: c for c in FROZEN["sources"]}
A = "CVE-2026-1234"


@pytest.fixture(autouse=True)
def no_transport(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


@pytest.mark.parametrize("case", FROZEN["cases"], ids=lambda c: c["id"])
def test_frozen_graph_outcomes(monkeypatch, public, case):
    source = SOURCES[case["case_id"]]
    inputs = [
        article(
            s["content"],
            title=case.get("title_override", s["title"]),
            link=f"https://example.test/graph/{i}",
        )
        for i, s in enumerate(source["sources"])
    ]
    before = tree(public)
    result = run_real_pipeline(
        monkeypatch,
        public / "index.md",
        articles=inputs,
        expect_model_call=case["expected_error"] != "unsupported_evidence_relation",
        mutation=case.get("mutation"),
    )
    assert result["status"] == case["expected_status"], result
    assert result["analysis_results"].get("error") == case["expected_error"]
    if result["status"] == "failed":
        assert tree(public) == before
        return
    text = (public / "index.md").read_text()
    findings = parse_report_artifact(text).findings
    owned = [f for f in findings if A in f.cve_ids]
    assert owned
    expected = source["expected"]
    assert {f.exploitation_status.value for f in owned} == {expected["status"]}
    assert {f.action.value for f in owned} == {expected["action"]}
    assert {f.severity.value for f in findings} == {"unknown"}
    if expected["complete_guidance"]:
        assert expected["complete_guidance"] in text
    for name in (
        "index.html",
        "current-findings.json",
        "reports/index.html",
        "reports/index.json",
        "sitemap.xml",
    ):
        assert (public / name).stat().st_size


@pytest.mark.parametrize("case", FROZEN["owners"], ids=lambda c: c["id"])
def test_owned_graph_and_invalid_plans(monkeypatch, public, case):
    before = tree(public)
    inputs = [
        article(s, title=case["titles"][i], link=f"https://example.test/owners/{i}")
        for i, s in enumerate(case["sources"])
    ]
    result = run_real_pipeline(
        monkeypatch,
        public / "index.md",
        articles=inputs,
        expect_model_call=case.get("error") != "unsupported_evidence_relation",
        mutation=case.get("mutation"),
    )
    assert result["status"] == case["expected_status"]
    assert result["analysis_results"].get("error") == case.get("error")
    if case["expected_status"] == "failed":
        assert tree(public) == before
        return
    findings = parse_report_artifact((public / "index.md").read_text()).findings
    assert {
        cve: f.exploitation_status.value for f in findings for cve in f.cve_ids
    } == case["states"]
    assert {f.action.value for f in findings} == {"none"}
    assert {f.severity.value for f in findings} == {"unknown"}
