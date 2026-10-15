"""Finite event inflections pass the real offline publication transaction."""

import json

import httpx
import pytest

from src.core.report_artifact import parse_report_artifact
from src.core.cve import extract_cve_ids
from test_event_morphology import CASES
from test_finding_generation_pipeline import REPRESENTATIVE_ARTICLES, run_real_pipeline
from test_owned_relation_contract import article
from test_publication_transaction import tree
from test_publication_transaction import public as public  # noqa: F401


@pytest.fixture(autouse=True)
def no_transport(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


@pytest.mark.parametrize("case", CASES, ids=lambda case: case["id"])
def test_inflection_publication_or_complete_prior_tree_preservation(
    monkeypatch, public, case
):
    controls = json.loads(
        json.dumps(REPRESENTATIVE_ARTICLES)
        .replace("CVE-2026-1234", "CVE-2098-90001")
        .replace("CVE-2026-5678", "CVE-2098-90002")
    )
    expected = case["expected"]
    text = case["text"]
    # Establish relevance for each existing identity independently of the
    # event under observation. A source-only operand stays source-only: adding
    # a fabricated CVE would change which finding owns a rejected relation.
    identities = extract_cve_ids(text)
    if identities:
        text = "\n\n".join(
            [f"{cve} exploitation status is unknown." for cve in identities] + [text]
        )
    before = tree(public)
    result = run_real_pipeline(
        monkeypatch,
        public / "index.md",
        articles=[
            article(text, link="https://example.test/event-inflection"),
            *controls,
        ],
        expect_model_call=expected["compile"],
    )
    if not expected["compile"]:
        assert result["status"] == "failed"
        assert result["analysis_results"]["error"] == expected["error"]
        assert tree(public) == before
        return
    assert result["status"] == "completed", result
    report = (public / "index.md").read_text()
    findings = parse_report_artifact(report).findings
    for cve, status in expected["states"].items():
        owned = [f for f in findings if cve in f.cve_ids]
        assert owned and {f.exploitation_status.value for f in owned} == {status}
        assert {f.action.value for f in owned} == {expected["action"]}
    assert (case["text"] in report) == expected["retain_complete_source"]
    for name in (
        "index.html",
        "current-findings.json",
        "reports/index.html",
        "reports/index.json",
        "sitemap.xml",
    ):
        assert (public / name).stat().st_size
