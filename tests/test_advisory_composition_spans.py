"""Finite composition spans, event distinction and qualification ownership."""

import importlib
import pytest
import httpx
from src.core.assertions import parse_assertions
from src.core.finding_generation import _severity
from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline

PREFIX = "Example released security advisories for two critical vulnerabilities in its "
PRODUCTS = [
    "Atlas gateways",
    "Relay servers",
    "Aurora network operating system",
    "NX-OS data center network operating system",
]
PURPOSES = [
    "to gain privileges",
    "to install custom malware on vulnerable Edge appliances",
    "to run arbitrary code",
    "to run arbitrary code with root privileges",
    "to run arbitrary code on Edge appliances",
    "to run arbitrary code with root privileges on Nexus switches",
]
LIST = "<p>All two vulnerabilities require a feature to be active:</p><ul><li>CVE-2026-1234: Gateway flaw.</li><li>CVE-2026-5678: Gateway flaw.</li></ul>"
ABSENCE = "<p>All two vulnerabilities were discovered during internal security testing, and Example said it was unaware of public announcements or malicious exploitation at the time of publishing the advisories.</p>"


def binder(text):
    return importlib.import_module("src.core.advisory_relations").bind_advisory(text)


@pytest.fixture(autouse=True)
def no_transport(monkeypatch):
    def forbidden(*a, **kw):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


@pytest.mark.parametrize("product", PRODUCTS)
@pytest.mark.parametrize("purpose", PURPOSES)
def test_composed_spans_not_sentence_templates(product, purpose):
    text = PREFIX + product + " that could be exploited " + purpose + "."
    bound = binder(text)
    assert bound is not None and bound.complete
    assert text[slice(*bound.product_span)] == product
    assert text[slice(*bound.predicate_span)] == "could be exploited " + purpose + "."
    assert bound.frame.supported and bound.frame.modal == "possible"
    assert bound.frame.polarity == "affirmative"
    assert bound.frame.qualifiers[0].kind == "purpose"
    assert bound.frame.qualifiers[0].text == purpose
    assert _severity([text]) == "critical"


@pytest.mark.parametrize("position", ["whole", "relative"])
def test_condition_ownership_is_not_discarded(position):
    base = PREFIX + "Atlas gateways that could be exploited to gain privileges"
    text = (
        "If reports are accurate, " + base + "."
        if position == "whole"
        else base + " if reports are accurate."
    )
    bound = binder(text)
    assert bound and bound.complete
    assert bound.declaration_conditions == (
        ("If reports are accurate",) if position == "whole" else ()
    )
    assert bound.relative_conditions == (
        ("if reports are accurate",) if position == "relative" else ()
    )
    assert _severity([text]) == "unknown"
    assert any(c.conditions and not c.unsupported for c in parse_assertions(text))


@pytest.mark.parametrize(
    "event",
    [
        "is actively exploited",
        "was exploited",
        "has been exploited",
        "will be exploited",
        "could have been exploited",
    ],
)
def test_declared_relative_event_is_not_misclassified_capability(event):
    text = PREFIX + "Atlas gateways that " + event + " to gain privileges."
    clauses = parse_assertions(text)
    assert any(c.unsupported for c in clauses)
    assert not any(
        c.kind == "context" and c.modal == "capability" and not c.unsupported
        for c in clauses
    )
    assert _severity([text]) == "unknown"


@pytest.mark.parametrize("event", ["is actively exploited", "was exploited"])
def test_unclassified_declaration_event_preserves_prior_artifacts(
    monkeypatch, tmp_path, event
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
    text = PREFIX + "Atlas gateways that " + event + " to gain privileges."
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article("<p>" + text + "</p>" + LIST + ABSENCE)],
        expect_model_call=False,
    )
    assert (
        result["status"] == "failed"
        and result["analysis_results"]["error"] == "unsupported_evidence_relation"
    )
    assert all((tmp_path / n).read_bytes() == data for n, data in previous.items())


@pytest.mark.parametrize(
    "tail",
    [
        "with unexplained privileges",
        "on inexplicable systems",
        "with root privileges and unclassified predicates prove exploitation",
    ],
)
def test_purpose_residual_is_never_opaque(tail):
    text = (
        PREFIX
        + "Atlas gateways that could be exploited to run arbitrary code "
        + tail
        + "."
    )
    bound = binder(text)
    assert bound and not bound.complete
    assert _severity([text]) == "unknown"
    assert any(c.unsupported for c in parse_assertions(text))


def test_negative_capability_does_not_negate_declared_rating_or_assert_observation():
    text = PREFIX + "Atlas gateways that could not be exploited to gain privileges."
    bound = binder(text)
    assert bound and bound.complete and bound.frame.polarity == "negative"
    clauses = parse_assertions(text)
    assert all(
        c.kind == "context"
        and c.modal == "capability"
        and c.polarity == "negative"
        and not c.unsupported
        for c in clauses
    )
    assert _severity([text]) == "critical"
