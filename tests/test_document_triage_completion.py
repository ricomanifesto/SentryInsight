"""Retained guidance includes supporting instructions and qualified exceptions."""

import pytest

from src.core.finding_evidence import collect_finding_details
from src.core.reporting import build_reporting_catalog
from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline

WARNING = "The breaches have triggered a warning from Example Financial Commission and Financial Supervisory Service, urging financial consumers {polarity}to exercise vigilance and be on the lookout for potential phishing attacks and loan scams stemming from leaked data."


@pytest.mark.parametrize("polarity", ["", "not "])
def test_reported_supporting_guidance_is_retained_without_primary_badge(
    monkeypatch, tmp_path, polarity
):
    text = WARNING.format(polarity=polarity)
    item = article(f"<p>Exploitation status is unknown.</p><p>{text}</p>")
    details = collect_finding_details(
        list(build_reporting_catalog([item]).values()), []
    )
    assert details.recommendation_blocks
    clauses = [
        c
        for b in details.recommendation_blocks
        for d in b.directives
        for c in getattr(d, "clauses", ())
    ]
    assert len(clauses) == 2 and all(not c.unsupported for c in clauses)
    assert all(
        c.polarity == ("negative" if polarity else "affirmative") for c in clauses
    )
    assert all(
        c.reporter
        and c.reporter.subject
        == "Example Financial Commission and Financial Supervisory Service"
        for c in clauses
    )
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result["analysis_results"].get("error")
    report = (tmp_path / "index.md").read_text()
    assert text in next(
        line for line in report.splitlines() if "**Recommended Actions**:" in line
    )
    assert "**Action**: none" in report


@pytest.mark.parametrize(
    "change",
    [
        ("urging financial consumers", "possibly urging financial consumers"),
        ("exercise vigilance", "exercise unspecified judgment"),
        (
            "stemming from leaked data.",
            "stemming from leaked data and unknown predicates apply.",
        ),
    ],
)
def test_unclassified_warning_or_residual_preserves_prior_artifacts(
    monkeypatch, tmp_path, change
):
    text = WARNING.format(polarity="").replace(*change)
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
        articles=[article(f"<p>Exploitation status is unknown.</p><p>{text}</p>")],
        expect_model_call=False,
    )
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == b"previous validated artifact"
        for name in names
    )


EXCEPTIONS = [
    "In a separate Example Message Center update, it also noted that replacement certificates have already been delivered to systems running a supported Example version and don't require additional action if they're up to date.",
    "However, this doesn't apply to devices that receive updates from Example Update Services (EUS), which downloads updates and distributes them across enterprise networks.",
]


def test_version_guidance_and_conditional_exceptions_survive_render(
    monkeypatch, tmp_path
):
    item = article(
        "<p>Exploitation status is unknown.</p><p>Users should install the patch.</p>"
        + "".join(f"<p>{text}</p>" for text in EXCEPTIONS)
        + "<p>Example shared the following detailed guidance on the required actions by Example version:</p><ul><li>Example 11, version 25H2 and later: No action is required.</li></ul>"
    )
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result["analysis_results"].get("error")
    report = (tmp_path / "index.md").read_text()
    exceptions = next(line for line in report.splitlines() if "**Exceptions**:" in line)
    assert all(text in exceptions for text in EXCEPTIONS)
    assert "Example 11, version 25H2 and later: No action is required." in exceptions


@pytest.mark.parametrize(
    "brand", ["Example 365 Message Center", "Example 2000 Message Center"]
)
def test_named_message_center_keeps_numeric_name_tokens(monkeypatch, tmp_path, brand):
    text = EXCEPTIONS[0].replace("Example Message Center", brand)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(f"<p>Exploitation status is unknown.</p><p>{text}</p>")],
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert text in next(
        line for line in report.splitlines() if "**Exceptions**:" in line
    )
