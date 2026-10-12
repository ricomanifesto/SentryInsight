"""Finite reported advice shares the directive owner, polarity and targets."""

import pytest

from src.core.finding_evidence import recommendation_action
from src.core.recommendations import parse_recommendation
from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline


@pytest.mark.parametrize(
    "text,action",
    [
        ("Example advised customers to install the patch.", "patch"),
        ("Example advised customers not to install the patch.", "none"),
        ("Example did not advise customers to install the patch.", "none"),
        ("Example advised customers to install the patch only if exposed.", "none"),
        (
            '"We strongly urge affected customers to review the advisory and upgrade impacted Example instances to the recommended versions as soon as possible," the company said.',
            "patch",
        ),
        (
            "Example recommends upgrading to a supported version of Example client or server.",
            "patch",
        ),
        (
            "Researchers recommend that users review logs and install the patch.",
            "patch",
        ),
    ],
)
def test_reported_guidance_full_pipeline_preserves_operator_and_complete_guidance(
    monkeypatch, tmp_path, text, action
):
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(
                f"<h2>CVE-2026-1234</h2><p>CVE-2026-1234 exploitation status is unknown.</p><p>{text}</p>"
            )
        ],
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert text in report and f"**Action**: {action}" in report
    assert recommendation_action([text]) == action


@pytest.mark.parametrize(
    "text",
    [
        "Example might advise customers to install the patch.",
        "Example denied that it advised customers to install the patch.",
        "Example advised mystery observers to install the patch.",
        "Example advised customers to install the patch with unclassified requirements.",
        "Example advised customers to install the patch and unidentified predicates apply.",
    ],
)
def test_unclassified_reporting_relation_stops_before_transport(
    monkeypatch, tmp_path, text
):
    paths = [
        tmp_path / n
        for n in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    ]
    for p in paths:
        p.write_bytes(b"Prior validated artifact")
    result = run_real_pipeline(
        monkeypatch,
        paths[0],
        articles=[
            article(
                f"<h2>CVE-2026-1234</h2><p>CVE-2026-1234 exploitation status is unknown.</p><p>{text}</p>"
            )
        ],
        expect_model_call=False,
    )
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(p.read_bytes() == b"Prior validated artifact" for p in paths)


def test_reporter_and_directive_polarity_have_distinct_owners():
    relation = parse_recommendation(
        "Example did not advise customers to install the patch."
    )
    assert relation and not relation.ambiguous
    clause = relation.clauses[0]
    assert clause.reporter and clause.reporter.subject == "Example"
    assert clause.reporter.polarity == "negative"
    assert clause.polarity == "affirmative"
