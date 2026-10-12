"""Independent source-data contract for composed rating context."""

from dataclasses import replace
import hashlib
import re
import httpx
import pytest
from markdown_it import MarkdownIt
from src.core.finding_evidence import EvidenceError, validate_finding_evidence
from src.core.finding_generation import _finding, compile_finding_records
from src.core.reporting import build_reporting_catalog
from src.core.source_markup import source_literal_value
from test_owned_relation_contract import article
from test_finding_generation_pipeline import run_real_pipeline
from test_retained_content_contract import VisibleText

A = "CVE-2026-1234"
PREFIX = "No single unqualified severity rating is supported for this finding scope."
PAYLOADS = [
    "![pixel](https://attacker.example/track)",
    "![pixel][tracking]",
    "![tracking]",
    "[label](https://attacker.example/track)",
    "[label][tracking]",
    "[tracking]: https://attacker.example/track",
    "<https://attacker.example/track>",
    "https://attacker.example/a;b?q=1&next=2",
    '<img src="https://attacker.example/track" onerror="example">',
    "<script>example</script>",
    "&lt;tag&gt; &amp; &#60;",
    "`code` and ``a ` b``",
    r"escaped \*text\*",
    "*emphasis* and **strong**",
    "unmatched `",
    "unmatched [",
    "### heading",
]


@pytest.fixture(autouse=True)
def forbidden_transport(monkeypatch):
    def forbidden(*_, **__):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


def item_for(*ratings):
    item = article(
        f"## {A}\n\n{A} exploitation status is unknown.\n\n" + "\n\n".join(ratings)
    )
    item["content_format"] = "text"
    return item


def context_field(report):
    return re.search(r"^- \*\*Severity Context\*\*: (.+)$", report, re.M)[1]


def visible(value):
    reader = VisibleText()
    reader.feed(MarkdownIt("commonmark").render(value))
    return reader


@pytest.mark.parametrize("label", ["Severity: critical", "CVSS score: 9.8"])
@pytest.mark.parametrize("payload", PAYLOADS)
def test_context_data_through_actual_pipeline(monkeypatch, tmp_path, label, payload):
    rating = label + " " + payload
    item = item_for(rating)
    original = item["content"]
    digest = hashlib.sha256(original.encode()).hexdigest()
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result
    assert item["content"] == original
    source = result["analysis_results"]["reporting_sources"][0]
    assert source["content"] == original
    assert hashlib.sha256(source["content"].encode()).hexdigest() == digest
    report = (tmp_path / "index.md").read_text()
    field = context_field(report)
    reader = visible(field + "\n\n[tracking]: https://attacker.example/track")
    assert "".join(reader.parts).rstrip("\n") == PREFIX + " " + rating
    assert not any(
        t in {"img", "a", "script", "iframe", "input", "h1", "h2", "h3", "blockquote"}
        for t, _ in reader.tags
    )
    assert field.startswith(PREFIX + " ")
    assert source_literal_value(field[len(PREFIX) + 1 :]) == rating
    page = VisibleText()
    page.feed((tmp_path / "index.html").read_text())
    assert PREFIX + " " + rating in "".join(page.parts)
    assert not any(
        "attacker.example" in a.get("src", "")
        or "attacker.example" in a.get("href", "")
        or "onerror" in a
        for _, a in page.tags
    )


@pytest.mark.parametrize(
    "left,right",
    [
        ("Severity: critical first `", "CVSS score: 9.8 second `"),
        ("Severity: critical *", "CVSS score: 9.8 *"),
        ("Severity: critical [tracking", "CVSS score: 9.8 ]"),
    ],
)
def test_each_context_item_keeps_its_literal_boundary(left, right):
    catalog = build_reporting_catalog([item_for(left, right)])
    (record,) = compile_finding_records(catalog, [A])
    field = context_field(_finding(record))
    assert (
        "".join(visible(field).parts).rstrip("\n") == PREFIX + " " + left + " " + right
    )
    tokens = MarkdownIt("commonmark").parseInline(field)[0].children
    assert [t.content for t in tokens if t.type == "code_inline"] == [left, right]


@pytest.mark.parametrize("payload", PAYLOADS)
def test_new_optional_data_field_cannot_bypass_common_encoder(payload):
    catalog = build_reporting_catalog([item_for("Severity: critical.")])
    (record,) = compile_finding_records(catalog, [A])
    record = replace(record, fields=record.fields + (("Additional Context", payload),))
    report = _finding(record)
    field = re.search(r"^- \*\*Additional Context\*\*: (.+)$", report, re.M)[1]
    assert source_literal_value(field) == payload
    reader = visible(field + "\n\n[tracking]: https://attacker.example/track")
    assert "".join(reader.parts).rstrip("\n") == payload
    assert not any(
        t in {"img", "a", "script", "iframe", "input", "h1", "h2", "h3"}
        for t, _ in reader.tags
    )


@pytest.mark.parametrize("mutation", ["alter", "drop_item", "raw_markup"])
def test_present_context_must_keep_canonical_owned_source_items(mutation):
    ratings = [
        "Severity: critical ![pixel](https://attacker.example/track)",
        "CVSS score: 9.8 pending confirmation.",
    ]
    catalog = build_reporting_catalog([item_for(*ratings)])
    (record,) = compile_finding_records(catalog, [A])
    report = "## Active Exploitation Details\n\n" + _finding(record)
    validate_finding_evidence(report, catalog)
    field = context_field(report)
    changed = (
        field.replace("pending confirmation", "alleged")
        if mutation == "alter"
        else (
            PREFIX + " " + ratings[0]
            if mutation == "drop_item"
            else PREFIX + " " + " ".join(ratings)
        )
    )
    assert changed != field
    with pytest.raises(EvidenceError):
        validate_finding_evidence(report.replace(field, changed), catalog)


def test_plain_rating_prose_and_renderer_prefix_stay_readable():
    catalog = build_reporting_catalog(
        [item_for("A critical vulnerability was not present.")]
    )
    (record,) = compile_finding_records(catalog, [A])
    assert (
        context_field(_finding(record))
        == PREFIX + " A critical vulnerability was not present."
    )


def test_required_unsupported_event_preserves_four_artifacts(monkeypatch, tmp_path):
    item = item_for("Severity: critical ![pixel](https://attacker.example/track)")
    item["content"] += f"\n\n{A} will be exploited tomorrow."
    previous = {
        n: ("previous " + n).encode()
        for n in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    }
    for n, b in previous.items():
        (tmp_path / n).write_bytes(b)
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[item], expect_model_call=False
    )
    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all((tmp_path / n).read_bytes() == b for n, b in previous.items())
