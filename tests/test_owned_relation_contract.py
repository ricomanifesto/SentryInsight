"""Frozen ownership oracle: v1, before the implementation replacement.

Assertion grammar: CVE/actor subject + finite/passive predicate; nominal
exploitation assessment; past access-by-exploiting and CVE-relative intrusion.
Operators: explicit/inherited subject; finite auxiliary; negation; possibility;
epistemic scope; additive/adversative/correlative coordination; reporting adjunct.
Reporting adjuncts own their reporter and confirmation tense. They never supply
an exploitation predicate's modality, polarity or tense. Unknown semantic forms
are unsupported, distinct from a parsed explicit-unknown claim.

Directive grammar: audience [complete nominal qualifier] + modal + action frame,
or whole-object imperative; inherited/repeated audience/modal; coordinated
objects/clauses; same-block references; leading/trailing conditions. The closed
verb/argument table is retained. Reported/epistemic advice is qualified, never
an affirmative command. Unclassified subject bridges/objects are unsupported.

The tables below are independent expected facts, not projections of parser
constants. Existing statement, historical, directive, frame and cardinality
regressions are also part of this frozen grammar. No production edits precede
this oracle. Unsupported required cases are decision points, not new productions.
"""

import json

import pytest

from src.core.finding_evidence import assess_exploitation, recommendation_action
from src.core.recommendations import parse_recommendation
from src.core.reporting import build_reporting_catalog
from test_finding_generation_pipeline import run_real_pipeline

CVE = "CVE-2026-1234"
OTHER = "CVE-2026-5678"


def article(content, **metadata):
    return dict(
        title=metadata.get("title", "Example advisory"),
        source="Example publisher",
        link=metadata.get("link", "https://example.test/owned"),
        content_kind="article",
        content=content,
        **({"cves": metadata["cves"]} if "cves" in metadata else {}),
    )


# Reporting participants and tense are independently varied, never transformed
# into predicate qualifiers by their spelling or incidental confirmation date.
@pytest.mark.parametrize("reporter", ["investigators", "researchers", "the vendor"])
@pytest.mark.parametrize("confirmation", ["confirmed yesterday", "confirm today"])
@pytest.mark.parametrize(
    "predicate,status",
    [
        ("is actively exploited", "active"),
        ("was actively exploited", "observed"),
        ("is not actively exploited", "not_observed"),
        ("may be actively exploited", "potential"),
        ("exploitation status is unknown", "unknown"),
    ],
)
def test_reporting_relation_does_not_own_exploitation_predicate(
    reporter, confirmation, predicate, status
):
    text = f"{CVE} {predicate} as {reporter} {confirmation}."
    assessment = assess_exploitation([article(text)], [CVE])
    assert assessment.status == status
    assert not getattr(assessment, "unsupported", ())


@pytest.mark.parametrize("modal", ["should", "must", "are advised to"])
@pytest.mark.parametrize(
    "second,expected,polarity,conditional",
    [
        ("monitor logs", "patch", "affirmative", False),
        ("not monitor logs", "patch", "negative", False),
        ("monitor logs if exposed", "patch", "affirmative", True),
        ("not install the patch", "none", "negative", False),
        ("install the patch only if exposed", "none", "affirmative", True),
    ],
)
@pytest.mark.parametrize("connector", ["and", "but"])
def test_repeated_modal_owns_a_separate_directive_relation(
    modal, second, expected, polarity, conditional, connector
):
    text = f"Users should install the patch {connector} {modal} {second}."
    parsed = parse_recommendation(text)
    assert parsed is not None and not parsed.ambiguous
    assert len(parsed.clauses) == 2
    assert parsed.clauses[1].modal == modal
    assert parsed.clauses[1].polarity == polarity
    assert bool(parsed.clauses[1].conditions) == conditional
    assert recommendation_action([text]) == expected


@pytest.mark.parametrize(
    "metadata",
    [
        {"title": f"{CVE} advisory"},
        {"cves": [CVE]},
        {"link": f"https://example.test/{CVE}"},
    ],
)
@pytest.mark.parametrize(
    "content",
    ["Exploitation has not been observed.", "Exploitation status is unknown."],
)
def test_metadata_identity_is_independent_of_required_positive_coverage(
    monkeypatch, tmp_path, metadata, content
):
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(content, **metadata)]
    )
    assert result["status"] == "completed", result
    data = json.loads((tmp_path / "current-findings.json").read_text())
    assert data["cve_ids"] == [CVE]
    report = (tmp_path / "index.md").read_text()
    assert "**Exploitation Status**: active" not in report
    assert "Attribution Context" in report


@pytest.mark.parametrize(
    "text",
    [
        f"{CVE} is thought by some analysts to be actively exploited.",
        f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\nUsers with an unclassified relation should install the patch.",
    ],
)
def test_required_unsupported_relation_blocks_without_a_model_call(
    monkeypatch, tmp_path, text
):
    output = tmp_path / "index.md"
    output.write_text("Previous validated report")
    result = run_real_pipeline(
        monkeypatch, output, articles=[article(text)], expect_model_call=False
    )
    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert output.read_text() == "Previous validated report"


def test_unrelated_article_prose_is_not_a_required_semantic_relation(
    monkeypatch, tmp_path
):
    text = f"{CVE} is actively exploited."
    context = "Investigators discussed an unfamiliar linguistic construction during an interview."
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(text), article(context, link="https://example.test/context")],
    )
    assert result["status"] == "completed", result
    assert len(result["analysis_results"]["reporting_sources"]) == 2
    assert json.loads((tmp_path / "current-findings.json").read_text())["cve_ids"] == [
        CVE
    ]


def test_other_cve_and_contrary_source_cannot_lend_predicate_ownership():
    sources = [
        article(
            f"{CVE} was exploited in attacks yesterday. {OTHER} is actively exploited as investigators confirmed yesterday."
        ),
        article(
            f"{CVE} exploitation has not been observed.",
            link="https://example.test/negative",
        ),
    ]
    catalog = build_reporting_catalog(sources)
    result = assess_exploitation(list(catalog.values()), [CVE])
    assert result.status == "unknown" and result.conflicting
    assert result.negative and result.positive
