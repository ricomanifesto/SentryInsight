"""Independent next-boundary oracle, frozen before production edits.

Unknown required qualifiers reject; current grammar gains no new conditions.
The accepted collection format and semantics are independent expectations.
"""

import copy
import json
import httpx
import pytest

from src.core.assertions import parse_assertions
from src.core.report_artifact import parse_report_artifact
from test_assertion_subject_contract import rejected, publish
from test_finding_generation_pipeline import run_real_pipeline, REPRESENTATIVE_ARTICLES
from test_retained_content_contract import VisibleText

A, B = "CVE-2026-1234", "CVE-2026-5678"
# These are independent expected dispositions, not production token lists.
REJECTED_QUALIFIERS = [
    "as long as reports are accurate",
    "so long as reports are accurate",
    "on condition that reports are accurate",
    "in the event that reports are accurate",
    "assuming that reports are accurate",
    "provided that reports are accurate",
    "only when reports are accurate",
    "in the wild as long as reports are accurate",
    "in attacks on condition that reports are accurate",
    "as a zero-day as long as reports are accurate",
    "under an unclassified qualification",
    "with an unclassified qualifier that changes the claim",
    "in the wild under an unclassified qualification",
    "after public disclosure as long as reports are accurate",
    "as was confirmed yesterday under an unclassified qualification",
    "yesterday in an unclassified semantic relationship",
]
POSITIVE_QUALIFIERS = [
    ("in the wild", "active"),
    ("in attacks", "active"),
    ("worldwide", "active"),
    ("after public disclosure", "active"),
    ("before a patch", "active"),
    ("after it was publicly disclosed", "active"),
    ("worldwide after patches were released", "active"),
    ("because a patch was unavailable", "active"),
    ("before the vendor had issued an update", "active"),
    ("as was confirmed yesterday", "active"),
    ("if reports are accurate", "unknown"),
    ("unless reports are inaccurate", "unknown"),
]
URLS = [
    "https://vendor.example/advisory",
    "https://vendor.example/advisory;session=1",
    "https://vendor.example/advisory?session=1;next=2",
    "https://vendor.example/a;b;c?x=1;y=2&next=3",
    "https://vendor.example/advisory?next=https://other.example/a;b",
    "https://vendor.example/a%3Bb?x=%3B",
    "https://vendor.example/a%20b?x=a%20b;y=2",
]


@pytest.fixture(autouse=True)
def no_real_transport(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


@pytest.mark.parametrize("tail", REJECTED_QUALIFIERS)
@pytest.mark.parametrize("voice", ["passive", "actor", "joint", "source-only"])
def test_unknown_adjunct_has_no_supported_projection(tail, voice):
    prefix = {
        "passive": f"{A} is exploited",
        "actor": f"Threat actors are exploiting {A}",
        "joint": f"{A} and {B} are exploited",
        "source-only": "Attackers are exploiting the gateway",
    }[voice]
    text = f"{prefix} {tail}."
    clauses = parse_assertions(text)
    assert any(c.unsupported for c in clauses), [(c.text, c.status) for c in clauses]
    assert not any(c.status == "active" for c in clauses)


@pytest.mark.parametrize("tail", REJECTED_QUALIFIERS)
def test_unknown_required_adjunct_preserves_four_artifacts(monkeypatch, tmp_path, tail):
    rejected(monkeypatch, tmp_path, f"{A} is exploited {tail}.")


@pytest.mark.parametrize("tail,status", POSITIVE_QUALIFIERS)
def test_supported_qualifier_keeps_whole_event(monkeypatch, tmp_path, tail, status):
    text = f"{A} is actively exploited {tail}."
    clauses = parse_assertions(text)
    assert len(clauses) == 1 and not clauses[0].unsupported
    assert clauses[0].text == text and clauses[0].status == status
    publish(monkeypatch, tmp_path, text, [A], [status])


@pytest.mark.parametrize("url", URLS)
def test_advisory_identity_through_actual_graph(monkeypatch, tmp_path, url):
    items = copy.deepcopy(REPRESENTATIVE_ARTICLES)
    items[0]["source_links"] = [url]
    items[0]["source_link_contexts"][0]["url"] = url
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=items)
    assert result["status"] == "completed", result
    artifact = parse_report_artifact((tmp_path / "index.md").read_text())
    finding = next(f for f in artifact.findings if A in f.cve_ids)
    assert finding.vendor_links == (url,)
    data = json.loads((tmp_path / "current-findings.json").read_text())
    assert A in data["cve_ids"]
    visible = VisibleText()
    visible.feed((tmp_path / "index.html").read_text())
    assert any(tag == "a" and attrs.get("href") == url for tag, attrs in visible.tags)


@pytest.mark.parametrize("url", URLS)
def test_new_collection_has_one_canonical_complete_encoding(monkeypatch, tmp_path, url):
    items = copy.deepcopy(REPRESENTATIVE_ARTICLES)
    items[0]["source_links"] = [url]
    items[0]["source_link_contexts"][0]["url"] = url
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=items)
    assert result["status"] == "completed", result
    expected = "urls-v1:" + json.dumps([url], ensure_ascii=True, separators=(",", ":"))
    assert f"- **Vendor Links**: {expected}\n" in (tmp_path / "index.md").read_text()
