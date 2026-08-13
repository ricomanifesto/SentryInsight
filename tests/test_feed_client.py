import asyncio
from types import SimpleNamespace

from src.services import fetch as fetch_module
from src.services.fetch import SentryDigestFeedClient, extract_article_text


class FakeResponse:
    text = "<rss><channel><item /></channel></rss>"

    def raise_for_status(self):
        pass


class FakeHttpClient:
    async def get(self, _url):
        return FakeResponse()


class StaticArticleResponse:
    status_code = 200
    text = """
    <html>
      <head>
        <meta property="og:description" content="Attackers target a vendor service.">
      </head>
      <body>
        <nav>Unrelated advisory CVE-2025-9999</nav>
        <div class="articleBody">
          <p>Attackers are actively exploiting CVE-2026-59310 in the wild.</p>
          <p>The vulnerability enables remote code execution.</p>
        </div>
        <footer>Another unrelated advisory CVE-2024-8888</footer>
      </body>
    </html>
    """


class StaticArticleClient:
    def __init__(self, *_args, **_kwargs):
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_args):
        return None

    async def get(self, _url):
        return StaticArticleResponse()


class TrackingArticleClient:
    called = False

    def __init__(self, *_args, **_kwargs):
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_args):
        return None

    async def get(self, _url):
        type(self).called = True
        raise AssertionError("missing article links should not be fetched")


class TrackingFeedClient:
    exit_calls = 0
    should_fail = False

    def __init__(self, *_args, **_kwargs):
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_args):
        type(self).exit_calls += 1

    async def get(self, _url):
        if type(self).should_fail:
            raise RuntimeError("feed unavailable")
        return FakeResponse()


def test_fetch_articles_preserves_safe_defaults_for_sparse_feed_entries(monkeypatch):
    monkeypatch.setattr(
        fetch_module.feedparser,
        "parse",
        lambda _text: SimpleNamespace(entries=[{}]),
    )
    client = SentryDigestFeedClient("https://example.com/feed.xml")
    client.client = FakeHttpClient()

    articles = asyncio.run(client.fetch_articles())

    assert articles == [
        {
            "title": "",
            "link": "",
            "summary": "",
            "published": "",
            "source": "Unknown Source",
            "date": articles[0]["date"],
            "content": "",
            "cves": [],
        }
    ]


def test_fetch_articles_extracts_only_complete_feed_cves(monkeypatch):
    monkeypatch.setattr(
        fetch_module.feedparser,
        "parse",
        lambda _text: SimpleNamespace(
            entries=[
                {
                    "title": "Active exploitation advisory",
                    "description": (
                        "CVE-2026-593... was truncated, while CVE-2026-59310 "
                        "is complete."
                    ),
                    "link": "https://example.test/advisory",
                }
            ]
        ),
    )
    client = SentryDigestFeedClient("https://example.com/feed.xml")
    client.client = FakeHttpClient()

    articles = asyncio.run(client.fetch_articles())

    assert articles[0]["cves"] == ["CVE-2026-59310"]


def test_enrich_article_content_extracts_readable_body_and_source_cves(monkeypatch):
    monkeypatch.setattr(fetch_module.httpx, "AsyncClient", StaticArticleClient)
    client = SentryDigestFeedClient("https://example.com/feed.xml")

    articles = asyncio.run(
        client.enrich_article_content(
            [
                {
                    "title": "Vendor issue",
                    "summary": "The feed summary was truncated at CVE-2026-593...",
                    "link": "https://example.test/advisory",
                    "content": "",
                    "cves": [],
                }
            ]
        )
    )

    assert "Attackers are actively exploiting CVE-2026-59310" in articles[0]["content"]
    assert "<div" not in articles[0]["content"]
    assert articles[0]["cves"] == ["CVE-2026-59310"]
    assert "CVE-2025-9999" not in articles[0]["content"]
    assert "CVE-2024-8888" not in articles[0]["content"]


def test_extract_article_text_supports_semantic_article_without_markers():
    source_html = """
    <html><body>
      <nav>Navigation text</nav>
      <article><p>Semantic article content for CVE-2026-55040.</p></article>
    </body></html>
    """

    assert extract_article_text(source_html) == (
        "Semantic article content for CVE-2026-55040."
    )


def test_extract_article_text_supports_semantic_main_without_markers():
    source_html = """
    <html><body>
      <main><p>Primary page content for CVE-2026-45659.</p></main>
      <footer>Footer text</footer>
    </body></html>
    """

    assert extract_article_text(source_html) == (
        "Primary page content for CVE-2026-45659."
    )


def test_extract_article_text_stops_at_container_with_omitted_paragraph_end_tags():
    source_html = """
    <article><p>Primary content.<p>More content.</article>
    <footer>Unrelated CVE-2026-9999</footer>
    """

    article_text = extract_article_text(source_html)

    assert "Primary content." in article_text
    assert "More content." in article_text
    assert "CVE-2026-9999" not in article_text


def test_extract_article_text_uses_only_first_selected_article_container():
    source_html = """
    <article><p>Primary story for CVE-2026-55040.</p></article>
    <article><p>Related story for CVE-2026-9999.</p></article>
    """

    article_text = extract_article_text(source_html)

    assert "CVE-2026-55040" in article_text
    assert "CVE-2026-9999" not in article_text


def test_extract_article_text_prefers_nested_article_over_broad_main():
    source_html = """
    <main>
      <nav>Related CVE-2026-9998</nav>
      <article><p>Primary story for CVE-2026-55040.</p></article>
      <aside>Related CVE-2026-9999</aside>
    </main>
    """

    article_text = extract_article_text(source_html)

    assert "CVE-2026-55040" in article_text
    assert "CVE-2026-9998" not in article_text
    assert "CVE-2026-9999" not in article_text


def test_extract_article_text_ignores_candidates_inside_hidden_containers():
    source_html = """
    <template><article>Hidden CVE-2026-9999</article></template>
    <article><p>Visible story for CVE-2026-55040.</p></article>
    """

    article_text = extract_article_text(source_html)

    assert "CVE-2026-55040" in article_text
    assert "CVE-2026-9999" not in article_text


def test_extract_article_text_skips_empty_higher_priority_candidate():
    source_html = """
    <div class="article-body"></div>
    <article><p>Visible story for CVE-2026-55040.</p></article>
    """

    assert "CVE-2026-55040" in extract_article_text(source_html)


def test_extract_article_text_recognizes_schema_org_article_body():
    source_html = """
    <div itemprop="articleBody">
      <p>Schema article content for CVE-2026-55040.</p>
    </div>
    """

    assert "CVE-2026-55040" in extract_article_text(source_html)


def test_enrich_article_content_skips_full_fetch_when_link_is_missing(monkeypatch):
    TrackingArticleClient.called = False
    monkeypatch.setattr(fetch_module.httpx, "AsyncClient", TrackingArticleClient)
    client = SentryDigestFeedClient("https://example.com/feed.xml")

    articles = asyncio.run(
        client.enrich_article_content(
            [
                {
                    "title": "Sparse article",
                    "summary": "Summary only",
                    "link": "",
                    "content": "",
                }
            ]
        )
    )

    assert articles[0]["content"] == "Sparse article\nSummary only\n"
    assert TrackingArticleClient.called is False


def test_default_feed_client_closes_after_success(monkeypatch):
    TrackingFeedClient.exit_calls = 0
    TrackingFeedClient.should_fail = False
    monkeypatch.setattr(fetch_module.httpx, "AsyncClient", TrackingFeedClient)
    monkeypatch.setattr(
        fetch_module.feedparser,
        "parse",
        lambda _text: SimpleNamespace(entries=[]),
    )

    articles = asyncio.run(
        SentryDigestFeedClient("https://example.com/feed.xml").fetch_articles()
    )

    assert articles == []
    assert TrackingFeedClient.exit_calls == 1


def test_default_feed_client_closes_after_failure(monkeypatch):
    TrackingFeedClient.exit_calls = 0
    TrackingFeedClient.should_fail = True
    monkeypatch.setattr(fetch_module.httpx, "AsyncClient", TrackingFeedClient)

    try:
        asyncio.run(
            SentryDigestFeedClient("https://example.com/feed.xml").fetch_articles()
        )
    except RuntimeError as error:
        assert str(error) == "feed unavailable"
    else:
        raise AssertionError("fetch_articles should propagate the transport failure")

    assert TrackingFeedClient.exit_calls == 1
