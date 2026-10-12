"""A received threat message and defensive caution have different owners."""

import pytest

from src.core.finding_evidence import collect_finding_details, recommendation_action
from src.core.recommendations import RecommendationContext, recommendation_context
from src.core.reporting import build_reporting_catalog
from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline

MESSAGE = (
    "On October 6, 2026, Example customers received a push notification through the "
    "Example app on their mobile devices, alleging customer data theft and urging "
    "the company’s staff to engage with them on Messenger."
)
CAUTION = "“However, please {negative}remain cautious of unexpected messages or calls claiming to be from Example.”"
ASSURANCE = "“We will never ask you to share passwords, security codes or payment details through an unsolicited message or call.”"


@pytest.mark.parametrize("negative", ["", "do not "])
def test_message_is_context_while_complete_caution_is_supporting_guidance(
    monkeypatch, tmp_path, negative
):
    context = recommendation_context(MESSAGE)
    assert isinstance(context, RecommendationContext) and context.owner == "narrative"
    caution = CAUTION.format(negative=negative)
    item = article(
        f"<p>Exploitation status is unknown.</p><p>{MESSAGE}</p>"
        f"<p>{caution}</p><p>{ASSURANCE}</p>"
    )
    details = collect_finding_details(
        list(build_reporting_catalog([item]).values()), []
    )
    assert MESSAGE not in [b.source_text for b in details.recommendation_blocks]
    assert caution in [b.source_text for b in details.recommendation_blocks]
    assert recommendation_action([caution]) == "none"
    directives = next(
        b for b in details.recommendation_blocks if b.source_text == caution
    )
    clauses = [c for d in directives.directives for c in getattr(d, "clauses", ())]
    assert clauses and all(
        c.polarity == ("negative" if negative else "affirmative") for c in clauses
    )
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert caution in next(
        line for line in report.splitlines() if "**Recommended Actions**:" in line
    )
    assert ASSURANCE in next(
        line for line in report.splitlines() if "**Exceptions**:" in line
    )
    assert "**Action**: none" in report


@pytest.mark.parametrize(
    "text",
    [
        MESSAGE.replace("received", "might receive"),
        MESSAGE[:-1] + " and users should install an unspecified object.",
        CAUTION.format(negative="").replace(
            "unexpected messages or calls", "an unspecified object"
        ),
        CAUTION.format(negative="")[:-2] + " and unknown predicates apply.”",
    ],
)
def test_unclassified_message_or_caution_does_not_disappear(
    monkeypatch, tmp_path, text
):
    names = (
        "index.md",
        "index.html",
        "current-findings.json",
        ".sentryinsight-articles-fingerprint",
    )
    for name in names:
        (tmp_path / name).write_bytes(b"Previous validated artifact")
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(f"<p>Exploitation status is unknown.</p><p>{text}</p>")],
        expect_model_call=False,
    )
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == b"Previous validated artifact"
        for name in names
    )
