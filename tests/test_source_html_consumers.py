"""Typed citations and Markdown tokens share the final HTML data boundary."""

import json

import httpx
import pytest

from src.core.report_artifact import parse_report_artifact
from test_finding_generation_pipeline import run_real_pipeline
from test_retained_content_contract import PAYLOADS, VisibleText, extracted

LABELS = PAYLOADS + [
    'onclick="example"',
    "![pixel](https://attacker.example/track)",
    "[untrusted](https://attacker.example/track)",
    "Plain readable title",
]


@pytest.mark.parametrize("field", ["title", "source"])
@pytest.mark.parametrize("label", LABELS)
def test_source_metadata_survives_actual_typed_html_consumer(
    monkeypatch, tmp_path, field, label
):
    def forbidden(*_, **__):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)
    item, content = extracted()
    item[field] = label
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result
    artifact = parse_report_artifact((tmp_path / "index.md").read_text())
    (reference,) = artifact.findings[0].reporting
    assert reference.title == item["title"]
    assert reference.publisher == item["source"]
    assert result["analysis_results"]["reporting_sources"][0]["content"] == content.text
    parsed = VisibleText()
    parsed.feed((tmp_path / "index.html").read_text())
    assert f'{item["source"]} — {item["title"]}' in "".join(parsed.parts)
    assert any(t == "a" and a.get("href") == reference.url for t, a in parsed.tags)
    assert not any(
        "onerror" in a or "onclick" in a or "attacker.example" in a.get("src", "")
        for _, a in parsed.tags
    )


@pytest.mark.parametrize("owner", ["reporting", "vendor"])
@pytest.mark.parametrize(
    "query", ["?onerror=example", "?onclick=example&next=1", "?q=%3Ctag%3E&next=2"]
)
def test_intended_link_attribute_data_keeps_exact_url_in_actual_pipeline(
    monkeypatch, tmp_path, owner, query
):
    item, _ = extracted()
    if owner == "reporting":
        expected = item["link"] + query
        item["link"] = expected
    else:
        expected = "https://vendor.example/advisory" + query
        item["source_links"] = [expected]
        item["source_link_contexts"][0]["url"] = expected
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result
    artifact = parse_report_artifact((tmp_path / "index.md").read_text())
    if owner == "reporting":
        assert artifact.findings[0].reporting[0].url == expected
    else:
        assert artifact.findings[0].vendor_links == (expected,)
    parsed = VisibleText()
    parsed.feed((tmp_path / "index.html").read_text())
    assert any(t == "a" and a.get("href") == expected for t, a in parsed.tags)
    assert not any("onerror" in a or "onclick" in a for _, a in parsed.tags)


def test_label_correction_does_not_bypass_malformed_source_preservation(
    monkeypatch, tmp_path
):
    item, _ = extracted()
    item["title"] = LABELS[1]
    item["source_blocks"][0]["text_sha256"] = "0" * 64
    previous = {
        name: f"previous {name}".encode()
        for name in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    }
    for name, value in previous.items():
        (tmp_path / name).write_bytes(value)
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[item], expect_model_call=False
    )
    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "invalid_retained_source"
    assert all(
        (tmp_path / name).read_bytes() == value for name, value in previous.items()
    )
    assert "onerror" not in json.dumps(result.get("diagnostics", {}))
