"""Proposed composition oracle: independent substitutions, no production edits."""

import pytest
import httpx
from src.core.assertions import parse_assertions
from src.core.finding_generation import _severity
from src.core.reporting import build_reporting_catalog
from src.core.source_document import source_document
from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline
from src.core.report_artifact import parse_report_artifact

A = "CVE-2026-1234"
B = "CVE-2026-5678"
PREFIX = "Example released security advisories for two critical vulnerabilities in its "
POSITIVE = [
    "NX-OS data center network operating system that could be exploited to run arbitrary code with root privileges on Nexus switches.",
    "Atlas gateways that could be exploited to gain privileges.",
    "Relay servers that could be exploited to install custom malware on vulnerable Edge appliances.",
    "Aurora network operating system that could be exploited to run arbitrary code with root privileges on Edge appliances.",
    "Orion software that could be exploited to gain privileges.",
]
UNKNOWN = [
    "Atlas gateways that could be exploited for unexplained reasons.",
    "Atlas gateways that could be exploited to gain privileges and unclassified predicates prove exploitation.",
    "Atlas gateways that will be exploited to gain privileges.",
    "Atlas mysteriously protected gateways that could be exploited to gain privileges.",
    "Atlas gateways that could be exploited to invent arbitrary outcomes.",
    "Atlas gateways that could be exploited to gain privileges as long as reports are accurate.",
]
LIST = f"<p>All two vulnerabilities require a feature to be active:</p><ul><li>{A}: Gateway flaw.</li><li>{B}: Gateway flaw.</li></ul>"
ABSENCE = "<p>All two vulnerabilities were discovered during internal security testing, and Example said it was unaware of public announcements or malicious exploitation at the time of publishing the advisories.</p>"


@pytest.fixture(autouse=True)
def no_transport(monkeypatch):
    def forbidden(*a, **k):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


@pytest.mark.parametrize("tail", POSITIVE)
def test_independent_product_purpose_substitution(tail):
    text = PREFIX + tail
    assert _severity([text]) == "critical"
    clauses = parse_assertions(text)
    assert clauses and all(not c.unsupported for c in clauses)
    assert all(c.kind == "context" and c.modal == "capability" for c in clauses)
    assert all(c.text == text for c in clauses)


@pytest.mark.parametrize("tail", POSITIVE)
def test_substitutions_reach_complete_graph(monkeypatch, tmp_path, tail):
    text = PREFIX + tail
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article("<p>" + text + "</p>" + LIST + ABSENCE)],
    )
    assert result["status"] == "completed"
    report = (tmp_path / "index.md").read_text()
    (finding,) = parse_report_artifact(report).findings
    assert finding.cve_ids == (A, B) and finding.severity.value == "critical"
    assert finding.exploitation_status.value == "not_observed"
    assert text in report


@pytest.mark.parametrize("tail", UNKNOWN)
def test_unknown_continuation_cannot_establish_rating(tail):
    assert _severity([PREFIX + tail]) == "unknown"
    assert any(c.unsupported for c in parse_assertions(PREFIX + tail))


@pytest.mark.parametrize("tail", UNKNOWN)
def test_unknown_owned_continuation_preserves_all_artifacts(
    monkeypatch, tmp_path, tail
):
    previous = {
        n: b"previous validated bytes"
        for n in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    }
    for n, data in previous.items():
        (tmp_path / n).write_bytes(data)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article("<p>" + PREFIX + tail + "</p>" + LIST + ABSENCE)],
        expect_model_call=False,
    )
    assert (
        result["status"] == "failed"
        and result["analysis_results"]["error"] == "unsupported_evidence_relation"
    )
    assert all((tmp_path / n).read_bytes() == data for n, data in previous.items())


@pytest.mark.parametrize(
    "text",
    [
        "If reports are accurate, " + PREFIX + POSITIVE[0],
        PREFIX + POSITIVE[0][:-1] + " if reports are accurate.",
        PREFIX + POSITIVE[0][:-1] + " but the vendor withdrew the rating.",
        "The vendor denied that " + PREFIX[0].lower() + PREFIX[1:] + POSITIVE[0],
    ],
)
def test_qualified_or_rejected_complete_rating_stays_unknown(text):
    assert _severity([text]) == "unknown"


def test_declaration_cannot_borrow_group_from_another_source():
    first = article("<p>" + PREFIX + POSITIVE[0] + "</p>")
    second = article(LIST + ABSENCE)
    first["link"] = "https://example.test/first"
    second["link"] = "https://example.test/second"
    catalog = build_reporting_catalog([first, second])
    intro = next(
        s
        for src in catalog.values()
        for s in source_document(src).spans
        if s.text == PREFIX + POSITIVE[0]
    )
    assert not intro.reference and not intro.reference_kind
