"""Extracted text is canonical data, never another HTML parsing input."""

import asyncio
from copy import deepcopy
from dataclasses import asdict, replace
import hashlib
import html
from html.parser import HTMLParser
import json
from types import SimpleNamespace

import pytest

from src.core.analyze import format_article_summary
from src.core.reporting import (
    ReportingGroundingError,
    build_reporting_catalog,
    deserialize_reporting_catalog,
    serialize_reporting_catalog,
)
from src.core.source_document import source_document
from src.services.article_content import extract_article_content
from test_analyze_guards import reference_plan_from_prompt
from test_finding_generation_pipeline import run_real_pipeline

CVE = "CVE-2026-1234"
PAYLOADS = [
    "<script>window.sourcePayload=1</script>",
    '<img src="x" onerror="window.sourcePayload=1">',
    "<input name=token>",
    "&lt;script&gt;literal entity&lt;/script&gt;",
    "a < b && c > d; café λ",
    "`<script>window.sourcePayload=1</script>`",
]


def extracted(payload="literal sample"):
    url = "https://example.test/story"
    text = f"The Gateway interface displays {payload} as a literal sample."
    markup = (
        f"<article><h2>{CVE}</h2><p>{CVE} is actively exploited.</p>"
        f"<p>{html.escape(text)}</p><p>Users should install the patch.</p>"
        '<p>See the <a href="https://vendor.example/advisory?a=1&amp;b=2">vendor advisory</a>.</p></article>'
    )
    content = extract_article_content(markup, url)
    return (
        dict(
            title="Gateway advisory",
            source="Publisher",
            link=url,
            content_kind="article",
            content=content.text,
            source_blocks=[asdict(b) for b in content.blocks],
            source_links=list(content.links),
            source_link_contexts=[asdict(link) for link in content.link_contexts],
        ),
        content,
    )


@pytest.mark.parametrize("payload", PAYLOADS)
def test_extracted_bytes_structure_links_and_prompt_survive_roundtrip(payload):
    item, content = extracted(payload)
    catalog = build_reporting_catalog([item])
    (source,) = catalog.values()
    assert source.content.encode() == content.text.encode()
    assert source.blocks == content.blocks
    assert (
        source.links == content.links and source.link_contexts == content.link_contexts
    )
    assert content.text in format_article_summary(item)
    restored = deserialize_reporting_catalog(
        json.loads(json.dumps(serialize_reporting_catalog(catalog)))
    )
    assert restored == catalog
    document = source_document(next(iter(restored.values())))
    assert document.text == content.text
    assert all(
        content.text[span.start : span.end] == span.text for span in document.spans
    )
    assert all(
        b.text_sha256 == hashlib.sha256(content.text.encode()).hexdigest()
        for b in source.blocks
    )


@pytest.mark.parametrize("kind", ["feed", "article"])
def test_explicit_plaintext_and_raw_feed_html_have_distinct_ingress(kind):
    item, _ = extracted()
    item.pop("source_blocks")
    item.update(
        content_kind=kind, content_format="text", content="  <p>&lt;token&gt;</p>  "
    )
    (plain,) = build_reporting_catalog([item]).values()
    assert plain.content == "  <p>&lt;token&gt;</p>  "
    assert plain.content in format_article_summary(item)
    item.pop("content_format")
    (raw,) = build_reporting_catalog([item]).values()
    assert raw.content == "<token>"


@pytest.mark.parametrize("retrieved", [False, True])
def test_enrichment_marks_normalized_feed_or_article_as_text_once(
    monkeypatch, retrieved
):
    from src.services import fetch

    class Client:
        def __init__(self, **_):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *_):
            pass

        async def get(self, _):
            return SimpleNamespace(
                status_code=200 if retrieved else 429,
                text="<article><p>Displayed &lt;script&gt;sample&lt;/script&gt;.</p></article>",
            )

    monkeypatch.setattr(fetch.httpx, "AsyncClient", Client)
    (item,) = asyncio.run(
        fetch.SentryDigestFeedClient("unused").enrich_article_content(
            [
                dict(
                    title="Gateway",
                    source="Publisher",
                    link="https://example.test/story",
                    content=[
                        {
                            "value": "<p>Displayed &lt;script&gt;sample&lt;/script&gt;.</p>"
                        }
                    ],
                )
            ]
        )
    )
    assert item["content_format"] == "text"
    (source,) = build_reporting_catalog([item]).values()
    assert source.content == item["content"] == "Displayed <script>sample</script>."
    assert source.content in format_article_summary(item)


MUTATIONS = [
    "hash",
    "range",
    "range_type",
    "range_bool",
    "text",
    "text_type",
    "kind",
    "level_type",
    "table_type",
    "cells_type",
    "header_type",
    "list_type",
    "unknown_field",
    "missing_field",
    "record_type",
    "blocks_type",
    "blocks_null",
    "children_type",
    "content_type",
    "content_mutation",
    "format",
    "raw_feed_blocks",
    "link_type",
    "link_context_type",
    "link_context_text_type",
]


def damage(item, case):
    item = deepcopy(item)
    block = item["source_blocks"][0]
    changes = {
        "hash": ("text_sha256", "0" * 64),
        "range": ("start", 1),
        "range_type": ("start", "0"),
        "range_bool": ("start", False),
        "text": ("text", "PRIVATE_PAYLOAD"),
        "text_type": ("text", 42),
        "kind": ("kind", "unknown"),
        "level_type": ("level", True),
        "table_type": ("table", "0"),
        "cells_type": ("cells", [1]),
        "header_type": ("header", 1),
        "list_type": ("list_id", "1"),
        "unknown_field": ("unknown", "PRIVATE_PAYLOAD"),
        "children_type": ("children", "invalid"),
    }
    if case in changes:
        block[changes[case][0]] = changes[case][1]
    elif case == "missing_field":
        del block["text_sha256"]
    elif case == "record_type":
        item["source_blocks"][0] = 42
    elif case == "blocks_type":
        item["source_blocks"] = "invalid"
    elif case == "blocks_null":
        item["source_blocks"] = None
    elif case == "content_type":
        item["content"] = {"value": "PRIVATE_PAYLOAD"}
    elif case == "content_mutation":
        item["content"] += "PRIVATE_PAYLOAD"
    elif case == "format":
        item["content_format"] = "unknown"
    elif case == "raw_feed_blocks":
        item["content_kind"] = "feed"
    elif case == "link_type":
        item["source_links"] = "https://example.test/"
    elif case == "link_context_type":
        item["source_link_contexts"] = [42]
    elif case == "link_context_text_type":
        item["source_link_contexts"][0]["context"] = 42
    return item


@pytest.mark.parametrize("case", MUTATIONS)
def test_malformed_extracted_records_use_the_reporting_domain_error(case):
    item, _ = extracted()
    with pytest.raises(ReportingGroundingError):
        build_reporting_catalog([damage(item, case)])


@pytest.mark.parametrize(
    "case", [c for c in MUTATIONS if c not in {"format", "raw_feed_blocks"}]
)
def test_deserialized_canonical_records_reject_tampering_without_coercion(case):
    item, _ = extracted()
    (record,) = serialize_reporting_catalog(build_reporting_catalog([item]))
    broken = damage(item, case)
    for source, destination in [
        ("content", "content"),
        ("source_blocks", "blocks"),
        ("source_links", "links"),
        ("source_link_contexts", "link_contexts"),
    ]:
        record[destination] = broken[source]
    with pytest.raises(ReportingGroundingError):
        deserialize_reporting_catalog([record])


@pytest.mark.parametrize("boundary", ["serialize", "document"])
@pytest.mark.parametrize("case", ["hash", "range_type", "content_type", "header_type"])
def test_in_memory_canonical_values_are_validated_at_each_consumer(boundary, case):
    item, _ = extracted()
    (source,) = build_reporting_catalog([item]).values()
    broken = damage(item, case)
    source = replace(source, content=broken["content"], blocks=broken["source_blocks"])
    with pytest.raises(ReportingGroundingError):
        if boundary == "serialize":
            serialize_reporting_catalog({source.key: source})
        else:
            source_document(source)


@pytest.mark.parametrize("case", MUTATIONS)
def test_invalid_input_stops_before_transport_and_preserves_all_artifacts(
    monkeypatch, tmp_path, caplog, case
):
    previous = {
        "index.md": b"Previous report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
        ".sentryinsight-articles-fingerprint": b"previous inputs\n",
    }
    for name, value in previous.items():
        (tmp_path / name).write_bytes(value)
    item, _ = extracted()
    valid, _ = extracted()
    valid["link"] = "https://example.test/other"
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[valid, damage(item, case)],
        expect_model_call=False,
    )
    assert result["status"] == "failed", result
    assert result["analysis_results"]["error"] == "invalid_retained_source"
    assert all(
        (tmp_path / name).read_bytes() == value for name, value in previous.items()
    )
    assert "PRIVATE_PAYLOAD" not in caplog.text


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.tags = []

    def handle_data(self, data):
        self.parts.append(data)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


@pytest.mark.parametrize("payload", PAYLOADS)
def test_payload_roundtrip_through_real_pipeline_is_visible_literal_data(
    monkeypatch, tmp_path, payload
):
    item, content = extracted(payload)

    def select(**kwargs):
        prompt = kwargs["user_prompt"]
        assert content.text in prompt
        plan = json.loads(reference_plan_from_prompt(**kwargs))
        records = json.loads(
            prompt.split("BEGIN FINDING RECORDS\n")[1].split("\nEND FINDING RECORDS")[0]
        )
        chosen = next(
            e["id"] for e in records[0]["excerpts"] if "literal sample" in e["text"]
        )
        plan["findings"][0]["excerpts"] = [chosen]
        return json.dumps(plan)

    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[item], select_plan=select
    )
    assert result["status"] == "completed", result
    assert result["analysis_results"]["reporting_sources"][0]["content"] == content.text
    report = (tmp_path / "index.md").read_text()
    assert payload in report
    parsed = VisibleText()
    parsed.feed((tmp_path / "index.html").read_text())
    # Markdown backticks already present in retained text delimit code, not data.
    assert payload.strip("`") in "".join(parsed.parts)
    assert not any(
        "onerror" in attrs or attrs.get("src") == "x" for _, attrs in parsed.tags
    )
    assert not any(
        tag == "input" and attrs.get("name") == "token" for tag, attrs in parsed.tags
    )
