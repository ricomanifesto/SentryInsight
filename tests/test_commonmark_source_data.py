"""Source data cannot acquire CommonMark structure in any report context."""

from copy import deepcopy
from dataclasses import replace
import hashlib
import json

import httpx
from markdown_it import MarkdownIt
import pytest

from src.core.finding_evidence import (
    EvidenceError,
    collect_finding_details,
    source_constraint_text,
    validate_finding_evidence,
)
from src.core.finding_generation import _finding, compile_finding_records
from src.core.report_artifact import ReportArtifactError, _parse_reporting
from src.core.reporting import build_reporting_catalog, resolve_reporting_keys
from src.core.source_markup import source_literal, source_literal_value
from test_analyze_guards import reference_plan_from_prompt
from test_finding_generation_pipeline import run_real_pipeline
from test_retained_content_contract import PAYLOADS, VisibleText, extracted

MARKUP = [
    "![pixel](https://attacker.example/track)",
    "![pixel][tracking]",
    "![tracking]",
    "[click](https://attacker.example/track)",
    "[click][tracking]",
    "[tracking]",
    "[tracking]: https://attacker.example/track",
    "<https://attacker.example/track>",
    "<person@attacker.example>",
    "*emphasis* and **strong**",
    "_emphasis_ and __strong__",
    r"escaped \*literal\* and \[brackets\]",
    "`code` and ``a ` b``",
    "unmatched ` tick",
    "unmatched [ label",
    "unmatched * emphasis",
    "unmatched ](https://attacker.example/track)",
    "trailing backslash\\",
    "### Injected heading",
    "- injected list",
    "1. injected list",
    "> injected quote",
    "---",
    "```fence",
    "    indented code",
    "Unicode café λ &copy; &amp; &#60;",
    *PAYLOADS,
]


def visible(markdown):
    parsed = VisibleText()
    parsed.feed(MarkdownIt("commonmark").render(markdown))
    return parsed


def test_installed_parser_exposes_its_own_raw_text_scanner():
    parser = MarkdownIt("commonmark")
    assert callable(parser.inline.terminator_re.search)
    assert not parser.inline.terminator_re.search("Users should install the patch.")
    assert parser.inline.terminator_re.search("unmatched ` tick")


@pytest.mark.parametrize("text", MARKUP)
@pytest.mark.parametrize("context", ["paragraph", "field", "quote", "link_label"])
def test_source_atom_is_exact_in_every_emission_context(text, context):
    encoded = source_literal(text)
    assert text in encoded
    assert source_literal_value(encoded) == text
    forms = {
        "paragraph": encoded,
        "field": f"- **Description**: {encoded}",
        "quote": f"[Source](<https://publisher.example/>): “{encoded}”",
        "link_label": f"[{encoded}](<https://publisher.example/>)",
    }
    # A definition elsewhere must not activate an otherwise unresolved reference.
    parsed = visible(forms[context] + "\n\n[tracking]: https://attacker.example/track")
    assert text in "".join(parsed.parts)
    assert not any(t in {"img", "script", "input", "iframe"} for t, _ in parsed.tags)
    assert [a["href"] for t, a in parsed.tags if t == "a"] == (
        ["https://publisher.example/"] if context in {"quote", "link_label"} else []
    )
    assert not any(t in {"h1", "h2", "h3", "blockquote", "pre"} for t, _ in parsed.tags)


@pytest.mark.parametrize(
    "left,right",
    [
        ("first `", "second `"),
        ("first *", "second *"),
        ("[tracking", "]"),
        ("ending \\", "*later*"),
    ],
)
def test_adjacent_source_quotes_cannot_complete_each_others_delimiters(left, right):
    parsed = visible(f"“{source_literal(left)}” “{source_literal(right)}”")
    assert f"“{left}” “{right}”" in "".join(parsed.parts)
    assert not any(t in {"a", "img", "em", "strong"} for t, _ in parsed.tags)


@pytest.mark.parametrize(
    "text",
    [
        "Users should install the patch.",
        "Ordinary prose, with parentheses (and Unicode café λ).",
    ],
)
def test_proved_plain_prose_remains_readable_without_literal_typography(text):
    assert source_literal(text) == text
    assert not any(t == "code" for t, _ in visible(source_literal(text)).tags)


@pytest.mark.parametrize(
    "text",
    [
        "line\n### heading",
        "line\rnew",
        "line\r\nnew",
        "![image]\n\n[image]: https://attacker.example/track",
    ],
)
def test_direct_multiline_presentation_input_is_rejected(text):
    with pytest.raises(ValueError, match="single-line"):
        source_literal(text)


@pytest.mark.parametrize("payload", MARKUP)
def test_reporting_label_and_destination_keep_exact_owned_data(payload):
    item, _ = extracted()
    item.update(
        title=payload,
        source="Example publisher",
        link="https://publisher.example/path(unbalanced?q=&copy;&x=1",
    )
    catalog = build_reporting_catalog([item])
    source = next(iter(catalog.values()))
    report = (
        "## Active Exploitation Details\n\n### Example\n- **Reporting**: " + source.key
    )
    resolved = resolve_reporting_keys(report, catalog)
    field = resolved.split("- **Reporting**: ", 1)[1]
    (reference,) = _parse_reporting(field)
    assert reference.title == " ".join(payload.split())
    assert reference.publisher == item["source"]
    assert reference.url == source.url
    parsed = visible(field)
    assert f"{source.publisher} — {source.title}" in "".join(parsed.parts)
    assert [a["href"] for t, a in parsed.tags if t == "a"] == [source.url]
    assert not any(t in {"img", "script", "input"} for t, _ in parsed.tags)


@pytest.mark.parametrize(
    "label",
    [
        "![x](https://attacker.example/x) — title",
        "**Publisher** — title",
        "` Publisher — [tracking] ` tail",
        "`` Publisher — [tracking] ``",
    ],
)
def test_reporting_rejects_markup_and_noncanonical_literal_labels(label):
    with pytest.raises(ReportArtifactError):
        _parse_reporting(f"[{label}](<https://publisher.example/>)")


@pytest.mark.parametrize("payload", MARKUP)
def test_evidence_quote_keeps_literal_data_and_its_intended_citation(payload):
    item, _ = extracted()
    (source,) = build_reporting_catalog([item]).values()
    url = "https://publisher.example/a(b?q=&copy;"
    details = replace(
        collect_finding_details([source], ["CVE-2026-1234"]),
        constraint_evidence=((url, payload),),
    )
    parsed = visible(source_constraint_text(details))
    assert payload in "".join(parsed.parts)
    assert [a["href"] for t, a in parsed.tags if t == "a"] == [url]
    assert not any(t == "img" for t, _ in parsed.tags)


@pytest.mark.parametrize(
    "field",
    ["Affected Versions", "Exceptions", "Recommended Actions", "Release Details"],
)
def test_data_fields_decode_exactly_and_retain_source_tamper_rejection(field):
    item, _ = extracted()
    catalog = build_reporting_catalog([item])
    (record,) = compile_finding_records(catalog, ["CVE-2026-1234"])
    text = "![pixel](https://attacker.example/track) `literal` &copy;"
    fields = [(n, v) for n, v in record.fields if n != field] + [(field, text)]
    report = "## Active Exploitation Details\n\n" + _finding(
        replace(record, fields=tuple(fields))
    )
    encoded = report.split(f"**{field}**: ", 1)[1].split("\n", 1)[0]
    assert source_literal_value(encoded) == text
    assert text in "".join(visible(encoded).parts)
    with pytest.raises(EvidenceError):
        validate_finding_evidence(report, catalog)


PIPELINE_PAYLOADS = [
    *MARKUP[:9],
    "*untrusted* `code` \\ [tracking] &copy;",
    "\n### Forged finding\n- **Action**: patch\n\n![pixel](https://attacker.example/track)",
]


@pytest.mark.parametrize("payload", PIPELINE_PAYLOADS)
def test_actual_pipeline_keeps_source_data_literal_without_real_transport(
    monkeypatch, tmp_path, payload
):
    def forbidden(*_, **__):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)
    item, content = extracted(payload)
    before = deepcopy(item)

    def select(**kwargs):
        plan = json.loads(reference_plan_from_prompt(**kwargs))
        prompt = kwargs["user_prompt"]
        assert content.text in prompt
        records = json.loads(
            prompt.split("BEGIN FINDING RECORDS\n")[1].split("\nEND FINDING RECORDS")[0]
        )
        plan["findings"][0]["excerpts"] = [
            next(
                e["id"] for e in records[0]["excerpts"] if "literal sample" in e["text"]
            )
        ]
        return json.dumps(plan)

    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[item], select_plan=select
    )
    assert result["status"] == "completed", result
    assert item == before
    assert result["analysis_results"]["reporting_sources"][0]["content"] == content.text
    parsed = VisibleText()
    parsed.feed((tmp_path / "index.html").read_text())
    assert " ".join(payload.split()) in "".join(parsed.parts)
    assert not any(
        "attacker.example" in a.get("src", "")
        or "attacker.example" in a.get("href", "")
        for _, a in parsed.tags
    )
    artifact = json.loads((tmp_path / "current-findings.json").read_text())
    assert artifact["finding_count"] == 1
    assert artifact["cve_ids"] == ["CVE-2026-1234"]
    assert all(t != "h3" or "Forged" not in str(a) for t, a in parsed.tags)


def test_malformed_source_with_markup_still_preserves_all_artifacts_before_transport(
    monkeypatch, tmp_path
):
    item, _ = extracted(MARKUP[0])
    item["source_blocks"][0]["text_sha256"] = "0" * 64
    prior = {
        name: f"previous {name}".encode()
        for name in [
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        ]
    }
    hashes = {n: hashlib.sha256(b).hexdigest() for n, b in prior.items()}
    for name, data in prior.items():
        (tmp_path / name).write_bytes(data)
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[item], expect_model_call=False
    )
    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "invalid_retained_source"
    assert {
        n: hashlib.sha256((tmp_path / n).read_bytes()).hexdigest() for n in prior
    } == hashes
