"""Composed owners pass the real offline graph or preserve prior publication."""

import json

import httpx
import pytest

from src.core.cve import extract_cve_ids
from src.core.report_artifact import parse_report_artifact
from test_owned_composition import CASES, ordered
from test_owned_relation_contract import article
from test_finding_generation_pipeline import REPRESENTATIVE_ARTICLES, run_real_pipeline
from test_publication_transaction import tree
from test_publication_transaction import public as public  # noqa: F401

IDS = {
    "do-0000",
    "do-0002",
    "do-0012",
    "do-0024",
    "do-0288",
    "do-0289",
    "do-0290",
    "do-0336",
    "do-boundary-0000",
    "observation-0000",
    "observation-0001",
    "observation-0002",
    "observation-negation-0000",
    "observation-negation-0002",
    "observation-negation-0005",
    "observation-boundary-0000",
    "observation-boundary-0006",
    "patch-direct-0000",
    "patch-direct-0006",
    "patch-direct-0007",
    "patch-direct-0009",
    "patch-direct-0036",
    "patch-direct-0048",
    "patch-reported-0001",
    "patch-reported-0005",
    "patch-qualified-0001",
    "patch-joint-0000",
    "patch-independent-0000",
    "patch-source-only-0000",
    "patch-conflict-0000",
    "patch-boundary-0000",
    "combined-0000",
    "combined-0001",
    "combined-0003",
    "combined-0004",
}


@pytest.fixture(autouse=True)
def no_transport(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


@pytest.mark.parametrize(
    "case", [c for c in CASES if c["id"] in IDS], ids=lambda c: c["id"]
)
def test_complete_composition_publication_or_prior_tree_preservation(
    monkeypatch, public, case
):
    controls = json.loads(
        json.dumps(REPRESENTATIVE_ARTICLES)
        .replace("CVE-2026-1234", "CVE-2098-90001")
        .replace("CVE-2026-5678", "CVE-2098-90002")
    )
    articles = []
    for index, text in enumerate(case["sources"]):
        # Eligibility is established independently; ownership still comes only
        # from the original body/section or exact source-only membership.
        identities = extract_cve_ids(text)
        prelude = "\n\n".join(
            f"{cve} exploitation status is unknown." for cve in identities
        )
        articles.append(
            article(
                (prelude + "\n\n" if prelude else "") + text,
                link=f"https://example.test/composition/{index}",
                **case["metadata"],
            )
        )
    before = tree(public)
    result = run_real_pipeline(
        monkeypatch,
        public / "index.md",
        articles=[*articles, *controls],
        expect_model_call=case["expected"]["compile"],
    )
    if not case["expected"]["compile"]:
        assert result["status"] == "failed"
        assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
        assert tree(public) == before
        return
    assert result["status"] == "completed", result
    report = (public / "index.md").read_text()
    findings = parse_report_artifact(report).findings
    actual = [
        {
            "cves": list(f.cve_ids),
            "status": f.exploitation_status.value,
            "action": f.action.value,
        }
        for f in findings
        if any(
            r.url.startswith("https://example.test/composition/") for r in f.reporting
        )
    ]
    assert ordered(actual) == ordered(case["expected"]["records"])
    if "\n" not in case["text"]:
        assert case["text"] in report
    for name in (
        "index.html",
        "current-findings.json",
        "reports/index.html",
        "reports/index.json",
        "sitemap.xml",
    ):
        assert (public / name).stat().st_size
