"""A finite advisory declaration can own one complete following CVE list."""

import pytest

from src.core.finding_generation import _severity
from src.core.source_document import source_document
from src.core.reporting import build_reporting_catalog
from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline

INTRO = "Example released security advisories for two critical vulnerabilities in its NX-OS data center network operating system that could be exploited to run arbitrary code with root privileges on Nexus switches."
LIST = "<p>All two vulnerabilities require a feature to be active:</p><ul><li>CVE-2026-1234: Gateway flaw.</li><li>CVE-2026-5678: Gateway flaw.</li></ul>"
ABSENCE = "<p>All two vulnerabilities were discovered during internal security testing, and Example said it was unaware of public announcements or malicious exploitation at the time of publishing the advisories.</p>"


def document(item):
    return source_document(next(iter(build_reporting_catalog([item]).values())))


@pytest.mark.parametrize(
    "text,state",
    [
        ("two critical vulnerabilities", "critical"),
        ("two high-severity flaws", "high"),
        ("not critical vulnerabilities", "unknown"),
    ],
)
def test_plural_explicit_ratings_keep_polarity(text, state):
    assert _severity([text]) == state


def test_declared_list_severity_is_retained_without_inventing_activity(
    monkeypatch, tmp_path
):
    item = article(f"<p>{INTRO}</p>" + LIST + ABSENCE)
    doc = document(item)
    intro = next(s for s in doc.spans if s.text == INTRO)
    assert (
        set(intro.reference) == {"CVE-2026-1234", "CVE-2026-5678"}
        and intro.reference_valid
    )
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result["analysis_results"].get("error")
    report = (tmp_path / "index.md").read_text()
    assert "**Severity**: critical" in report
    assert "**Exploitation Status**: not_observed" in report


@pytest.mark.parametrize(
    "between",
    ["<h2>Another story</h2>", "<p>CVE-2026-9999 is a separate vulnerability.</p>"],
)
def test_declaration_does_not_borrow_a_later_different_story_list(between):
    item = article(f"<p>{INTRO}</p>" + between + LIST + ABSENCE)
    intro = next(s for s in document(item).spans if s.text == INTRO)
    assert not intro.reference


def test_ambiguous_same_cardinality_is_not_an_owned_severity():
    other = LIST.replace("1234", "9998").replace("5678", "9999")
    item = article(f"<p>{INTRO}</p>" + LIST + other)
    intro = next(s for s in document(item).spans if s.text == INTRO)
    assert not intro.reference_valid


def test_owned_declaration_cannot_hide_an_unknown_event_residual(monkeypatch, tmp_path):
    text = INTRO.rstrip(".") + " and unclassified predicates prove exploitation."
    names = (
        "index.md",
        "index.html",
        "current-findings.json",
        ".sentryinsight-articles-fingerprint",
    )
    for name in names:
        (tmp_path / name).write_bytes(b"previous validated artifact")
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(f"<p>{text}</p>" + LIST + ABSENCE)],
        expect_model_call=False,
    )
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == b"previous validated artifact"
        for name in names
    )
