"""Frozen complete-span and collection boundary contracts, before code edits."""

import json
import re

import pytest

from src.core.assertions import parse_assertions
from src.core.reporting import ReportingGroundingError
from test_assertion_qualifier_contract import REJECTED_QUALIFIERS, URLS
from test_assertion_subject_contract import publish, rejected

A, B = "CVE-2026-1234", "CVE-2026-5678"


@pytest.mark.parametrize(
    "text,spans",
    [
        (
            "in the wild yesterday",
            [("context", "in the wild"), ("temporal", "yesterday")],
        ),
        ("as a zero-day in June", [("role", "as a zero-day"), ("temporal", "in June")]),
        (
            "worldwide after patches were released",
            [("context", "worldwide"), ("temporal", "after patches were released")],
        ),
        ("as was confirmed yesterday", [("reporter", "as was confirmed yesterday")]),
        ("by the threat actors", [("agent", "by the threat actors")]),
        ("100 times last week", [("temporal", "100 times"), ("temporal", "last week")]),
        ("in Example Platform", [("context", "in Example Platform")]),
        (
            "for weeks to install custom malware on vulnerable VPN appliances",
            [
                ("temporal", "for weeks"),
                ("purpose", "to install custom malware on vulnerable VPN appliances"),
            ],
        ),
        (
            "as a zero-day against Example's own cloud service, the company said on August 6",
            [
                ("role", "as a zero-day"),
                ("context", "against Example's own cloud service"),
                ("reporter", "the company said on August 6"),
            ],
        ),
        (f"for {A}, {B}", [("identity", f"for {A}, {B}")]),
    ],
)
def test_qualifier_owner_returns_exact_complete_spans(text, spans):
    from src.core.assertion_qualifiers import bind_qualifiers

    bound = bind_qualifiers(text)
    assert bound.complete and bound.end == len(text)
    assert [(s.kind, s.text) for s in bound.spans] == spans
    assert all(text[s.start : s.end] == s.text for s in bound.spans)
    assert all(a.end <= b.start for a, b in zip(bound.spans, bound.spans[1:]))


@pytest.mark.parametrize("text", REJECTED_QUALIFIERS)
def test_qualifier_owner_preserves_unclassified_residual(text):
    from src.core.assertion_qualifiers import bind_qualifiers

    result = bind_qualifiers(text)
    assert not result.complete
    assert 0 <= result.end < len(text)
    assert result.residual == text[result.end :]


@pytest.mark.parametrize(
    "predicate",
    [
        "was exploited",
        "is not exploited",
        "might be exploited",
        "might not be exploited",
    ],
)
@pytest.mark.parametrize(
    "tail",
    ["as long as reports are accurate", "in the wild as long as reports are accurate"],
)
def test_polarity_or_modal_does_not_rescue_unknown_qualification(
    monkeypatch, tmp_path, predicate, tail
):
    rejected(monkeypatch, tmp_path, f"{A} {predicate} {tail}.")


@pytest.mark.parametrize("connector", [" and ", ", but ", "; ", " whereas "])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize(
    "tail", ["if reports are accurate", "as long as reports are accurate"]
)
def test_qualification_cannot_lend_state_or_hide_later_clause(
    monkeypatch, tmp_path, connector, reverse, tail
):
    parts = [
        f"{A} is actively exploited in the wild {tail}",
        f"{B} was exploited yesterday",
    ]
    if reverse:
        parts.reverse()
    text = connector.join(parts) + "."
    clauses = parse_assertions(text)
    other = next(c for c in clauses if c.cves == (B,))
    assert other.status == "observed" and not other.unsupported and not other.conditions
    primary = next(c for c in clauses if c.cves == (A,))
    assert primary.text.strip(" .") == parts[1 if reverse else 0]
    if tail.startswith("if"):
        assert primary.conditions == (tail,) and primary.status == "unknown"
        publish(monkeypatch, tmp_path, text, [A, B], ["unknown", "observed"])
    else:
        assert primary.unsupported and primary.assertion_status is None


@pytest.mark.parametrize(
    "urls",
    [[URLS[0]], [URLS[1]], [URLS[3], URLS[0], URLS[1]], [URLS[1], URLS[1]], URLS],
)
def test_complete_collection_round_trip(urls):
    from src.core.reporting import serialize_url_collection, parse_url_collection

    expected = "urls-v1:" + json.dumps(urls, separators=(",", ":"))
    assert serialize_url_collection(urls) == expected
    assert parse_url_collection(expected) == tuple(urls)


@pytest.mark.parametrize(
    "value",
    [
        'urls-v2:["https://example.test/"]',
        'urls-v1:"https://example.test/"',
        "urls-v1:null",
        "urls-v1:{}",
        "urls-v1:[null]",
        "urls-v1:[1]",
        'urls-v1:[""]',
        "urls-v1:[] trailing",
        'urls-v1:["https://example.test/"]{}',
        'urls-v1: ["https://example.test/"]',
        'urls-v1:["https:\\/\\/example.test/"]',
        'urls-v1:["https://EXAMPLE.test:443/"]',
        'urls-v1:["javascript:alert(1)"]',
        'urls-v1:["https://user:secret@example.test/"]',
        'urls-v1:["https://example.test:invalid/"]',
    ],
)
def test_codec_rejects_malformed_noncanonical_or_partial_field(value):
    from src.core.reporting import parse_url_collection

    with pytest.raises(ReportingGroundingError):
        parse_url_collection(value)


@pytest.mark.parametrize(
    "value,expected",
    [
        ("https://EXAMPLE.test:443/a#fragment", ("https://example.test/a",)),
        (
            "https://example.test/a; https://example.test/b",
            ("https://example.test/a", "https://example.test/b"),
        ),
        (
            "https://example.test/a;https://example.test/b",
            ("https://example.test/a", "https://example.test/b"),
        ),
        (
            "https://example.test/a; https://example.test/a",
            ("https://example.test/a", "https://example.test/a"),
        ),
    ],
)
def test_legacy_read_is_explicit_and_unchanged(value, expected):
    from src.core.reporting import parse_url_collection

    assert parse_url_collection(value) == expected


def test_ambiguous_legacy_field_is_not_silently_reinterpreted():
    from src.core.reporting import parse_url_collection

    with pytest.raises(ReportingGroundingError):
        parse_url_collection("https://example.test/advisory;session=1")


@pytest.mark.parametrize(
    "event",
    [
        f"{A} is exploited",
        f"{A} has been exploited",
        "the flaw being weaponized",
    ],
)
@pytest.mark.parametrize(
    "tail",
    [
        "as long as reports are accurate",
        "in the wild under an unclassified qualification",
    ],
)
def test_negative_evidence_envelope_cannot_bypass_qualifier_owner(
    monkeypatch, tmp_path, event, tail
):
    prefix = (
        "No evidence of "
        if event.startswith("the flaw")
        else "There is no evidence that "
    )
    rejected(monkeypatch, tmp_path, prefix + event + " " + tail + ".")


@pytest.mark.parametrize(
    "text",
    [
        f"There is no evidence that {A} has been exploited in the wild.",
        "No evidence of the flaw being weaponized in the wild.",
        "No evidence of exploitation.",
        "No exploitation has been observed.",
        "No known exploitation of CVE-2026-1234.",
    ],
)
def test_negative_evidence_retains_existing_complete_meaning(text):
    (clause,) = parse_assertions(text)
    assert not clause.unsupported and clause.status == "not_observed"
    assert clause.text == text


def test_context_complement_is_owned_by_its_existing_predicate():
    from src.core.assertion_qualifiers import bind_qualifiers

    bound = bind_qualifiers("to attack", complement="vulnerable")
    assert bound.complete and bound.spans[0].kind == "context"
    assert not bind_qualifiers("to attack").complete
    assert not bind_qualifiers(
        "to attack as long as reports are accurate", complement="vulnerable"
    ).complete


@pytest.mark.parametrize(
    "tail", ["in The Event That Reports Are Accurate", "in Reports Are Accurate"]
)
def test_unclassified_capitalized_clause_is_not_a_named_platform(
    monkeypatch, tmp_path, tail
):
    rejected(monkeypatch, tmp_path, f"{A} is exploited {tail}.")


@pytest.mark.parametrize("value", [None, 1, {}, [None]])
def test_collection_types_reach_domain_error(value):
    from src.core.reporting import parse_url_collection, serialize_url_collection

    with pytest.raises(ReportingGroundingError):
        parse_url_collection(value)
    with pytest.raises(ReportingGroundingError):
        serialize_url_collection(value)


def test_predicate_frame_qualifier_offsets_share_its_source_coordinate_system():
    from src.core.assertion_predicates import bind_predicate

    text = f"are actively exploiting {A} in the wild yesterday"
    frame = bind_predicate(text, voice="actor")
    assert frame.supported
    assert [(q.kind, q.text) for q in frame.qualifiers] == [
        ("context", "in the wild"),
        ("temporal", "yesterday"),
    ]
    assert all(text[q.start : q.end] == q.text for q in frame.qualifiers)
    assert all(
        frame.adjunct_span[0] <= q.start < q.end <= frame.adjunct_span[1]
        for q in frame.qualifiers
    )


@pytest.mark.parametrize(
    "field",
    [
        'urls-v1:["https://vendor.example/a;session=1"] trailing',
        'urls-v1:["https://vendor.example/a;session=1",null]',
        'urls-v2:["https://vendor.example/a;session=1"]',
        'urls-v1:["https://unowned.example/a;session=1"]',
    ],
)
def test_corrupted_emitted_collection_preserves_previous_artifacts(
    monkeypatch, tmp_path, caplog, field
):
    from src.core import finding_generation
    from test_finding_generation_pipeline import run_real_pipeline

    original = finding_generation.render_finding_plan

    def corrupted(*args, **kwargs):
        report = original(*args, **kwargs)
        return re.sub(
            r"(?m)^- \*\*Vendor Links\*\*: .*$",
            lambda _: "- **Vendor Links**: " + field,
            report,
            count=1,
        )

    monkeypatch.setattr(finding_generation, "render_finding_plan", corrupted)
    names = (
        "index.md",
        "index.html",
        "current-findings.json",
        ".sentryinsight-articles-fingerprint",
    )
    previous = {name: f"previous {name}".encode() for name in names}
    for name, data in previous.items():
        (tmp_path / name).write_bytes(data)
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md")
    assert result["status"] == "failed"
    assert result["report_validation_errors"]
    diagnostics = [
        json.loads(record.getMessage().split("Report grounding failed: ", 1)[1])
        for record in caplog.records
        if record.getMessage().startswith("Report grounding failed: ")
    ]
    assert diagnostics[-1]["code"] in {"invalid_vendor_link", "unsupported_vendor_link"}
    assert all(
        (tmp_path / name).read_bytes() == data for name, data in previous.items()
    )


def test_multiple_advisories_keep_exact_collection_order_through_graph(
    monkeypatch, tmp_path
):
    from copy import deepcopy
    from src.core.report_artifact import parse_report_artifact
    from test_finding_generation_pipeline import (
        run_real_pipeline,
        REPRESENTATIVE_ARTICLES,
    )

    items = deepcopy(REPRESENTATIVE_ARTICLES)
    expected = [URLS[1], URLS[4]]
    item = items[0]
    item["source_links"] = expected
    item["source_link_contexts"] = [
        dict(item["source_link_contexts"][0], url=url) for url in expected
    ]
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=items)
    assert result["status"] == "completed", result
    findings = parse_report_artifact((tmp_path / "index.md").read_text()).findings
    assert next(f for f in findings if A in f.cve_ids).vendor_links == tuple(expected)
