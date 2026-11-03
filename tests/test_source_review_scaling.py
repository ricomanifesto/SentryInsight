"""Preflight must not retain every growing prefix of a long source paragraph."""

from src.core.finding_evidence import (
    _partition_detail_spans,
    build_finding_detail_context,
)
from src.core.reporting import build_reporting_catalog
from test_version_references import source


def test_long_plain_paragraph_retains_complete_sentences_without_quadratic_context():
    content = (
        "Source evidence. " * 500
        + "Final qualification: exploitation has not been observed."
    )
    article = source(content)
    spans = _partition_detail_spans(article, []).scoped
    assert " ".join(span.text for span in spans if span.role == "body") == content
    assert sum(len(span.version_context) for span in spans) <= len(content)
    context = build_finding_detail_context(build_reporting_catalog([article]))
    assert any(
        "exploitation has not been observed" in span["text"]
        for item in context
        for span in item["spans"]
    )


def test_context_optimization_does_not_run_version_attribution_before_scope_selection():
    article = source(
        "An unrelated advisory (CVE-2026-1234 and also CVE-2026-5678) describes a service."
    )
    spans = _partition_detail_spans(article, ["CVE-2026-9999"])
    assert not any(span.role == "body" for span in spans.scoped)
