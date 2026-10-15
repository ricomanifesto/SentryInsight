"""Purpose infinitives preserve context without rescuing required use events."""

import httpx
import pytest

from src.core.assertion_predicates import bind_predicate
from src.core.assertions import parse_assertions
from src.core.finding_evidence import EvidenceError
from test_finding_generation import catalog_for, render

A = "CVE-2026-1234"


@pytest.fixture(autouse=True)
def no_real_transport(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


@pytest.mark.parametrize(
    "text",
    [
        "to use it in attacks",
        "also to use it in attacks",
        "to use a tool in future attacks",
        "not to use it in attacks",
        "also to use it as a key part of their toolset in future attacks",
    ],
)
def test_unowned_purpose_has_no_exploitation_assertion(text):
    frame = bind_predicate(text)
    assert frame.kind == "context" and frame.supported
    assert frame.event_binding and frame.event_binding.kind == "context"
    assert all(
        c.kind == "context" and not c.unsupported for c in parse_assertions(text)
    )


@pytest.mark.parametrize(
    "text,voice",
    [
        (f"to use {A} in attacks", "unscoped"),
        ("to use it in attacks", "actor"),
        ("to use in attacks", "vulnerability"),
        ("used in attacks", "actor"),
        ("will be used in attacks", "vulnerability"),
        ("was used in zero attacks", "vulnerability"),
        ("was used in repeated attacks", "vulnerability"),
    ],
)
def test_required_owner_or_cue_keeps_the_rejection(text, voice):
    frame = bind_predicate(text, voice=voice)
    assert frame.kind == "assertion" and not frame.supported


@pytest.mark.parametrize("quoted", [False, True])
def test_complete_correlative_purpose_survives_source_compilation(quoted):
    text = (
        "This demonstrates a keen interest by Example operators in improving "
        "their downloader, not only to avoid detection by security solutions, "
        "but also to use it as a key part of their toolset in future attacks"
    )
    text = f'"{text}," the company said.' if quoted else text + "."
    source = f"## {A}\n\n{A} exploitation status is unknown.\n\n{text}"
    records, _ = render(catalog_for(source))
    assert len(records) == 1 and records[0].status == "unknown"
    assert any(excerpt.text == text for excerpt in records[0].excerpts)


@pytest.mark.parametrize(
    "text",
    [
        "Attackers used in attacks.",
        "Attackers used a tool in attacks.",
        f"Researchers used {A} in attacks.",
        f"{A} will be used in attacks.",
        f"{A} was used in zero attacks.",
    ],
)
def test_source_scope_does_not_fill_a_required_operand(text):
    source = f"## {A}\n\n{A} exploitation status is unknown.\n\n{text}"
    with pytest.raises(EvidenceError) as error:
        render(catalog_for(source))
    assert error.value.code == "unsupported_evidence_relation"
