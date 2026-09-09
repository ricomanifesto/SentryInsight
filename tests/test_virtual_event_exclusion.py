import asyncio
from copy import deepcopy
from html import escape
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

from src.core.content_fingerprint import compute_articles_fingerprint
from src.core.report_validation import validate_report_content
from src.services.fetch import SentryDigestFeedClient
from src.services import fetch as fetch_module
from test_report_validation import VALID_REPORT
from test_workflow_guards import import_workflow_with_stubs

MARKERS = (
    "[Virtual Event]",
    "[vIrTuAl eVeNt]",
    "[ \tVirtual\r\n Event \n]",
    "[Virtual&nbsp;Event]",
    "&#91;Virtual&#32;Event&#93;",
    "&#x5b;Virtual&#xA0;Event&#x5d;",
    "&lbrack;Virtual&Tab;Event&rbrack;",
    "&amp;#91;Virtual&amp;nbsp;Event&amp;#93;",
    r"\[Virtual Event\]",
    r"\[ Virtual&nbsp;Event \]",
    r"\&#91;Virtual Event\&#93;",
    "[**Virtual** _Event_]",
    "&#91;<span>Virtual</span><br>Event&#93;",
    "[<em>Vir</em>tual <strong>Event</strong>]",
    "[<div>Virtual</div><div>Event</div>]",
)
ORDINARY_TEXT = (
    "Attackers exploited CVE-2026-1234 during a virtual event.",
    "Security events reveal malware activity.",
    "[Event] Attackers exploit an edge service.",
    "[Virtual Events] A security incident retrospective.",
    "Virtual Event: Incident response lessons.",
    "[Virtual Eventuality] A threat model.",
)


def news_article():
    return {
        "title": "Attackers exploited CVE-2026-1234 during a virtual event",
        "link": "https://example.test/news?edition=1#details",
        "summary": "Security events reveal active exploitation.",
        "content": "Malware is exploiting CVE-2026-1234.",
        "cves": ["CVE-2026-1234"],
        "source": "Example Source",
    }


def promotion(marker="[Virtual Event]"):
    return {
        "title": f"{marker} Exploitation and malware briefing",
        "link": "https://example.test/promotion",
        "summary": "Register for our briefing on CVE-2026-9999.",
        "content": "",
        "cves": ["CVE-2026-9999"],
    }


@pytest.mark.parametrize("marker", MARKERS)
@pytest.mark.parametrize("field", ("title", "summary", "content", "source"))
def test_feed_excludes_entire_virtual_event_record(monkeypatch, marker, field):
    tagged = news_article() | {field: f"{marker} Register now"}
    if field == "content":
        tagged[field] = [{"type": "text/html", "value": tagged[field]}]
    if field == "source":
        tagged["dc_source"] = tagged.pop("source")
    if field == "summary":
        tagged["description"] = tagged.pop("summary")
    clean = news_article()
    monkeypatch.setattr(
        fetch_module.feedparser,
        "parse",
        lambda _text, **_kwargs: SimpleNamespace(entries=[tagged, clean]),
    )
    client = SentryDigestFeedClient("https://example.test/feed.xml")
    client.client = SimpleNamespace(
        get=AsyncMock(return_value=SimpleNamespace(text="", raise_for_status=Mock()))
    )

    articles = asyncio.run(client.fetch_articles())

    assert len(articles) == 1
    assert articles[0]["title"] == clean["title"]
    assert articles[0]["link"] == clean["link"]


@pytest.mark.parametrize("marker", MARKERS)
def test_real_feedparser_content_is_checked_for_virtual_event(marker):
    rss = (
        '<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/">'
        "<channel><title>News</title><item><title>Briefing</title>"
        f"<content:encoded>{escape(marker)}</content:encoded>"
        "</item></channel></rss>"
    )
    client = SentryDigestFeedClient("https://example.test/feed.xml")
    client.client = SimpleNamespace(
        get=AsyncMock(return_value=SimpleNamespace(text=rss, raise_for_status=Mock()))
    )

    assert asyncio.run(client.fetch_articles()) == []


def test_retained_feed_content_keeps_default_sanitization_and_url_resolution():
    rss = (
        '<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/"'
        ' xml:base="https://example.test/">'
        "<channel><item><title>Malware at a virtual event</title>"
        "<content:encoded><![CDATA["
        '<a href="/story" onclick="alert(1)">Malware report</a>'
        "]]></content:encoded></item></channel></rss>"
    )
    expected = fetch_module.feedparser.parse(rss).entries[0]["content"]
    client = SentryDigestFeedClient("https://example.test/feed.xml")
    client.client = SimpleNamespace(
        get=AsyncMock(return_value=SimpleNamespace(text=rss, raise_for_status=Mock()))
    )

    result = asyncio.run(client.fetch_articles())

    assert len(result) == 1
    assert result[0]["content"] == expected
    assert "onclick" not in result[0]["content"][0]["value"]
    assert 'href="https://example.test/story"' in result[0]["content"][0]["value"]


@pytest.mark.parametrize("marker", MARKERS)
def test_virtual_event_is_excluded_before_full_content_fetch(monkeypatch, marker):
    http_client = Mock(side_effect=AssertionError("must not fetch tagged articles"))
    monkeypatch.setattr(fetch_module.httpx, "AsyncClient", http_client)
    client = SentryDigestFeedClient("https://example.test/feed.xml")
    clean = news_article()
    articles = [promotion(marker), clean]
    original = deepcopy(articles)

    result = asyncio.run(client.enrich_article_content(articles))

    assert result == [clean]
    assert result[0] is clean
    assert articles == original
    http_client.assert_not_called()


@pytest.mark.parametrize("marker", MARKERS)
def test_virtual_event_newly_revealed_by_enrichment_is_excluded(monkeypatch, marker):
    class FullContentClient:
        calls = []

        def __init__(self, **_kwargs):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *_args):
            pass

        async def get(self, url):
            self.calls.append(url)
            return SimpleNamespace(status_code=200, text=f"<p>{marker} Register</p>")

    monkeypatch.setattr(fetch_module.httpx, "AsyncClient", FullContentClient)
    client = SentryDigestFeedClient("https://example.test/feed.xml")
    tagged = promotion() | {"title": "Exploitation briefing"}
    clean = news_article()

    result = asyncio.run(client.enrich_article_content([tagged, clean]))

    assert result == [clean]
    assert FullContentClient.calls == [tagged["link"]]


@pytest.mark.parametrize("text", ORDINARY_TEXT)
def test_generic_events_are_not_virtual_event_promotions(text):
    article = news_article() | {"title": text, "content": text}
    client = SentryDigestFeedClient("https://example.test/feed.xml")
    assert asyncio.run(client.enrich_article_content([article])) == [article]
    assert validate_report_content(VALID_REPORT + f"\n{text}\n") == []


@pytest.mark.parametrize("marker", MARKERS)
def test_publication_rejects_virtual_event_markers(marker):
    issues = validate_report_content(VALID_REPORT + f"\n{marker} Register now.\n")
    assert any(issue.code == "virtual_event_promotion" for issue in issues)


def test_virtual_event_marker_can_include_image_alternative_text():
    report = VALID_REPORT + '\n[<img src="missing.png" alt="Virtual"> Event]\n'
    assert any(
        issue.code == "virtual_event_promotion"
        for issue in validate_report_content(report)
    )


@pytest.mark.parametrize("node", ("fetch_articles", "enrich_articles"))
def test_workflow_rechecks_virtual_event_in_mocked_feed_results(monkeypatch, node):
    workflow = import_workflow_with_stubs()
    clean = news_article()
    fetch = AsyncMock(return_value=[promotion(), clean])
    enrich = AsyncMock(return_value=[promotion(r"\[Virtual Event\]"), clean])
    monkeypatch.setattr(
        workflow,
        "SentryDigestFeedClient",
        lambda *_args: SimpleNamespace(
            fetch_articles=fetch, enrich_article_content=enrich
        ),
    )
    state = {"articles": [promotion(), clean], "config": {"feed_url": "test"}}

    result = asyncio.run(getattr(workflow, node)(state))

    assert result["articles"] == [clean]
    if node == "enrich_articles":
        enrich.assert_awaited_once_with([clean])


def test_workflow_excludes_virtual_event_before_filter_and_fingerprint(
    monkeypatch, tmp_path
):
    workflow = import_workflow_with_stubs()
    clean = news_article()
    fingerprint = compute_articles_fingerprint([clean])
    (tmp_path / ".sentryinsight-articles-fingerprint").write_text(fingerprint + "\n")
    relevance_filter = Mock(side_effect=lambda articles: articles)
    monkeypatch.setattr(workflow, "filter_exploitation_articles", relevance_filter)
    state = {
        "articles": [promotion(), clean],
        "config": {"output_path": str(tmp_path / "index.md")},
        "status": "started",
    }

    result = asyncio.run(workflow.filter_articles(state))

    relevance_filter.assert_called_once_with([clean])
    assert result["articles"] == result["filtered_articles"] == [clean]
    assert result["articles_fingerprint"] == fingerprint
    assert result["status"] == "completed_unchanged"
    assert workflow.should_end(result) == "unchanged"


def test_direct_workflow_analysis_cannot_receive_virtual_event(monkeypatch):
    workflow = import_workflow_with_stubs()
    analyze = AsyncMock(return_value={"analyzed_article_count": 1})
    monkeypatch.setattr(workflow, "analyze_exploitation", analyze)
    clean = news_article()
    original = deepcopy(clean)
    state = {
        "filtered_articles": [promotion(), clean],
        "config": {},
        "status": "started",
    }

    result = asyncio.run(workflow.analyze_articles(state))

    analyze.assert_awaited_once_with([clean], {})
    assert result["filtered_articles"] == [original]
    assert result["filtered_articles"][0] is clean


def test_real_graph_preserves_report_when_mocked_feed_is_all_virtual_events(
    monkeypatch, tmp_path
):
    from langgraph.graph import END, START, StateGraph

    workflow = import_workflow_with_stubs()
    monkeypatch.setattr(workflow, "StateGraph", StateGraph)
    monkeypatch.setattr(workflow, "START", START)
    monkeypatch.setattr(workflow, "END", END)
    analyze = AsyncMock(side_effect=AssertionError("no eligible analysis input"))
    enrich = AsyncMock(side_effect=lambda articles: articles)
    monkeypatch.setattr(workflow, "analyze_exploitation", analyze)
    monkeypatch.setattr(
        workflow,
        "SentryDigestFeedClient",
        lambda *_args: SimpleNamespace(
            fetch_articles=AsyncMock(return_value=[promotion()]),
            enrich_article_content=enrich,
        ),
    )
    output = tmp_path / "index.md"
    output.write_text("Last valid report")
    fingerprint = tmp_path / ".sentryinsight-articles-fingerprint"
    fingerprint.write_text("last-valid-fingerprint\n")

    result = asyncio.run(
        workflow.create_exploitation_analysis_graph().ainvoke(
            {
                "articles": [],
                "filtered_articles": [],
                "analysis_results": {},
                "config": {"feed_url": "test", "output_path": str(output)},
                "status": "started",
            }
        )
    )

    enrich.assert_awaited_once_with([])
    analyze.assert_not_awaited()
    assert result["status"] == "completed_with_warnings"
    assert output.read_text() == "Last valid report"
    assert fingerprint.read_text() == "last-valid-fingerprint\n"
    assert "report_path" not in result


@pytest.mark.parametrize("direct_analysis", (False, True))
def test_all_virtual_event_input_preserves_last_valid_publication(
    monkeypatch, tmp_path, direct_analysis
):
    workflow = import_workflow_with_stubs()
    analyze = AsyncMock(side_effect=AssertionError("no eligible analysis input"))
    monkeypatch.setattr(workflow, "analyze_exploitation", analyze)
    paths = (
        "index.md",
        "index.html",
        "current-findings.json",
        "sitemap.xml",
        "reports/index.json",
        "reports/2026-09-07.md",
        ".sentryinsight-articles-fingerprint",
    )
    for name in paths:
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"Last valid {name}\n")
    before = {name: (tmp_path / name).read_bytes() for name in paths}
    state = {
        "articles": [promotion()],
        "filtered_articles": [promotion()],
        "analysis_results": {},
        "config": {"output_path": str(tmp_path / "index.md")},
        "status": "started",
    }

    if direct_analysis:
        state = asyncio.run(workflow.analyze_articles(state))
    else:
        state = asyncio.run(workflow.filter_articles(state))
        assert workflow.should_end(state) == "no_articles"
    state = asyncio.run(workflow.generate_report(state))
    state = asyncio.run(workflow.publish_results(state))

    analyze.assert_not_awaited()
    assert state["status"] == "completed_with_warnings"
    assert "report_path" not in state
    assert {name: (tmp_path / name).read_bytes() for name in paths} == before
    assert sorted(
        p.relative_to(tmp_path).as_posix() for p in tmp_path.rglob("*") if p.is_file()
    ) == sorted(paths)


@pytest.mark.parametrize("in_attribution", (False, True))
def test_generate_report_rejects_virtual_event_before_normalization(
    tmp_path, in_attribution
):
    workflow = import_workflow_with_stubs()
    output_path = tmp_path / "index.md"
    output_path.write_text("Last valid report")
    marker = r"\[Virtual&nbsp;Event\]"
    report = VALID_REPORT.replace(
        "- **Status**: Active exploitation observed.",
        "- **Status**: Active exploitation observed.\n"
        "- **Severity**: high\n- **Exploitation Status**: active\n"
        "- **Action**: patch\n- **Reporting**: source-1e8f5cb3245d",
    )
    report += (
        f"\n## Source Attribution\n\n- {marker} Briefing\n"
        if in_attribution
        else f"\n{marker} Register now.\n"
    )
    state = {
        "analysis_results": {
            "exploitation_report": report,
            "reporting_sources": [
                {
                    "key": "source-1e8f5cb3245d",
                    "publisher": "Example Source",
                    "title": "Example report",
                    "url": "https://example.test/report",
                }
            ],
        },
        "config": {"output_path": str(output_path)},
        "status": "started",
    }

    result = asyncio.run(workflow.generate_report(state))

    assert result["status"] == "failed"
    assert any("Virtual Event" in error for error in result["report_validation_errors"])
    assert output_path.read_text() == "Last valid report"
    assert sorted(path.name for path in tmp_path.iterdir()) == ["index.md"]
