"""Canonical feed re-entry and source-data presentation are separate boundaries."""

import asyncio
from dataclasses import replace
from copy import deepcopy
from types import SimpleNamespace

import pytest
from markdown_it import MarkdownIt

from src.core.reporting import (
    ReportingGroundingError,
    build_reporting_catalog,
    deserialize_reporting_catalog,
    serialize_reporting_catalog,
)
from src.services import fetch
from test_retained_content_contract import PAYLOADS, VisibleText, extracted


@pytest.mark.parametrize("fallback", ["no_link", "429", "empty", "exception"])
@pytest.mark.parametrize(
    "text", ["Payload: <script>example</script>.", "&lt;tag&gt;", ""]
)
def test_canonical_feed_reentry_preserves_exact_fallback(monkeypatch, fallback, text):
    class Client:
        def __init__(self, **_):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *_):
            pass

        async def get(self, _):
            if fallback == "exception":
                raise OSError("Retrieval failed")
            return SimpleNamespace(
                status_code=429 if fallback == "429" else 200,
                text="<nav>Not an article</nav>",
            )

    monkeypatch.setattr(fetch.httpx, "AsyncClient", Client)
    item = dict(
        title="Feed title",
        summary="Do not reconstruct",
        content=text,
        content_kind="feed",
        content_format="text",
        source="Publisher",
        source_blocks=[],
        link="" if fallback == "no_link" else "https://example.test/story",
    )
    for _ in range(2):
        (item,) = asyncio.run(
            fetch.SentryDigestFeedClient("unused").enrich_article_content([item])
        )
        assert item["content"] == text
        assert item["content_format"] == "text"
    item["link"] = "https://example.test/story"
    assert next(iter(build_reporting_catalog([item]).values())).content == text


@pytest.mark.parametrize("kind", ["feed", "article"])
def test_retained_enrichment_keeps_structure_and_link_provenance(monkeypatch, kind):
    class Client:
        def __init__(self, **_):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *_):
            pass

        async def get(self, _):
            return SimpleNamespace(status_code=429)

    monkeypatch.setattr(fetch.httpx, "AsyncClient", Client)
    item, _ = extracted("<input name=token>")
    item.update(content_kind=kind, content_format="text")
    before = deepcopy(item)
    (after,) = asyncio.run(
        fetch.SentryDigestFeedClient("unused").enrich_article_content([item])
    )
    assert after == before


@pytest.mark.parametrize("value", [[], {}, False, 0])
def test_malformed_representation_marker_is_domain_error(value):
    item, _ = extracted()
    item["content_format"] = value
    with pytest.raises(ReportingGroundingError):
        build_reporting_catalog([item])


@pytest.mark.parametrize("value", [None, "record", 1, []])
def test_malformed_source_record_is_domain_error(value):
    with pytest.raises(ReportingGroundingError):
        build_reporting_catalog([value])


@pytest.mark.parametrize("value", [None, "context", (1,), ({"url": 1},)])
def test_malformed_serialized_link_context_is_domain_error(value):
    item, _ = extracted()
    (source,) = build_reporting_catalog([item]).values()
    with pytest.raises(ReportingGroundingError):
        serialize_reporting_catalog({source.key: replace(source, link_contexts=value)})


@pytest.mark.parametrize("boundary", ["serialize", "deserialize", "document"])
@pytest.mark.parametrize("field,value", [("cells", []), ("children", [])])
def test_typed_block_cannot_smuggle_mutable_unhashable_fields(boundary, field, value):
    from src.core.source_document import source_document

    item, _ = extracted()
    (source,) = build_reporting_catalog([item]).values()
    block = replace(source.blocks[0], **{field: value})
    source = replace(source, blocks=(block, *source.blocks[1:]))
    with pytest.raises(ReportingGroundingError):
        if boundary == "serialize":
            serialize_reporting_catalog({source.key: source})
        elif boundary == "document":
            source_document(source)
        else:
            # In-memory deserialization also accepts typed blocks. It must not
            # forward a wrong-type dataclass into the document cache.
            deserialize_reporting_catalog(
                [
                    dict(
                        key=source.key,
                        url=source.url,
                        publisher=source.publisher,
                        title=source.title,
                        content=source.content,
                        blocks=source.blocks,
                    )
                ]
            )


@pytest.mark.parametrize("boundary", ["serialize", "deserialize"])
@pytest.mark.parametrize("value", [None, 42, []])
def test_canonical_provenance_type_is_not_coerced(boundary, value):
    item, _ = extracted()
    (source,) = build_reporting_catalog([item]).values()
    with pytest.raises(ReportingGroundingError):
        if boundary == "serialize":
            serialize_reporting_catalog(
                {source.key: replace(source, content_kind=value)}
            )
        else:
            records = serialize_reporting_catalog({source.key: source})
            records[0]["content_kind"] = value
            deserialize_reporting_catalog(records)


@pytest.mark.parametrize("records", [None, 42, {}, "not records"])
def test_invalid_catalog_container_is_domain_error(records):
    for boundary in (build_reporting_catalog, deserialize_reporting_catalog):
        with pytest.raises(ReportingGroundingError):
            boundary(records)


@pytest.mark.parametrize(
    "text",
    PAYLOADS
    + [
        "``<token>`` and `<other>`",
        " <token> ",
        "**Label** [link](https://example.test/) <token>",
    ],
)
def test_literal_codec_preserves_exact_data_and_never_creates_markup(text):
    from src.core.source_markup import source_literal, source_literal_value

    encoded = source_literal(text)
    assert text in encoded
    assert source_literal_value(encoded) == text
    children = MarkdownIt("commonmark").parseInline(encoded)[0].children
    assert len(children) == 1 and children[0].type == "code_inline"
    assert children[0].content == text
    parsed = VisibleText()
    parsed.feed(MarkdownIt("commonmark").render(encoded))
    assert text in "".join(parsed.parts)
    assert not any(tag in {"script", "img", "input", "a"} for tag, _ in parsed.tags)


@pytest.mark.parametrize(
    "text",
    [
        "Users should install the patch.",
        "**Label** [source](https://example.test/)",
        "`ordinary code`",
        "` <tag> ` trailing",
        "`<tag>`",
    ],
)
def test_decoder_does_not_strip_arbitrary_markdown_or_partial_literals(text):
    from src.core.source_markup import source_literal_value

    assert source_literal_value(text) == text


@pytest.mark.parametrize("payload", PAYLOADS)
def test_source_quote_keeps_renderer_owned_citation_outside_literal(payload):
    from src.core.finding_evidence import (
        source_constraint_text,
        collect_finding_details,
    )
    from src.core.source_markup import source_literal

    item, _ = extracted()
    (source,) = build_reporting_catalog([item]).values()
    details = replace(
        collect_finding_details([source], ["CVE-2026-1234"]),
        constraint_evidence=((source.url, payload),),
    )
    rendered = source_constraint_text(details)
    assert rendered == f"[Source](<{source.url}>): “{source_literal(payload)}”"
    parsed = VisibleText()
    parsed.feed(MarkdownIt("commonmark").render(rendered))
    assert payload in "".join(parsed.parts)
    assert [a["href"] for t, a in parsed.tags if t == "a"] == [source.url]


def test_encoded_detail_keeps_canonical_artifact_value_and_source_tamper_gate():
    from src.core.finding_generation import _finding, compile_finding_records
    from src.core.finding_evidence import EvidenceError, validate_finding_evidence
    from src.core.report_artifact import parse_report_artifact
    from src.core.source_markup import source_literal

    item, _ = extracted()
    catalog = build_reporting_catalog([item])
    records = compile_finding_records(catalog, {"CVE-2026-1234"})
    record = records[0]
    # Presentation unit: a typed source field contains literal data; grammar is
    # deliberately not expanded to make this constructed target a directive.
    text = "The interface displays <input name=token>."
    fields = tuple(
        (n, text if n == "Recommended Actions" else v) for n, v in record.fields
    )
    report = "## Active Exploitation Details\n\n" + _finding(
        replace(record, fields=fields)
    )
    assert f"**Recommended Actions**: {source_literal(text)}" in report
    artifact = parse_report_artifact(
        "---\nschema_version: 3\nreport_date: 2026-10-12\ngenerated_at: 2026-10-12T00:00:00Z\ndigest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-10-12/\n---\n"
        + report.replace(
            next(iter(catalog)),
            "[Publisher — Gateway advisory](https://example.test/story)",
        )
    )
    assert artifact.findings[0].recommended_actions == text
    with pytest.raises(EvidenceError):
        validate_finding_evidence(report, catalog)


def test_renderer_distinguishes_literal_code_data_from_active_raw_html():
    from scripts.build_site import _render_markdown
    from src.core.report_artifact import parse_report_artifact
    from src.core.source_markup import source_literal

    literal = '<img src="x" onerror="window.sourcePayload=1">'
    body = (
        "# Report\n\n## Active Exploitation Details\n\n### Display\n"
        "- **Severity**: unknown\n- **Exploitation Status**: unknown\n- **Action**: none\n\n"
        + source_literal(literal)
        + "\n\n"
        + literal
    )
    artifact = parse_report_artifact(
        "---\nschema_version: 1\nreport_date: 2026-10-12\ngenerated_at: 2026-10-12T00:00:00Z\n---\n"
        + body
    )
    rendered, _ = _render_markdown(artifact)
    parsed = VisibleText()
    parsed.feed(rendered)
    assert "".join(parsed.parts).count(literal) == 1
    assert not any(t == "img" or "onerror" in a for t, a in parsed.tags)
    # The unchanged conservative guard still sees no active-content marker.
    assert "onerror=" not in rendered
