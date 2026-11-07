import asyncio
from types import SimpleNamespace

from src.services import fetch as fetch_module
from src.services.fetch import SentryDigestFeedClient


class FakeResponse:
    text = "<rss><channel><item /></channel></rss>"

    def raise_for_status(self):
        pass


class FakeHttpClient:
    async def get(self, _url):
        return FakeResponse()


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
        lambda _text, **_kwargs: SimpleNamespace(entries=[{}]),
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
        }
    ]


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

    assert articles[0]["content"] == "# Sparse article\nSummary only\n"
    assert TrackingArticleClient.called is False


def test_default_feed_client_closes_after_success(monkeypatch):
    TrackingFeedClient.exit_calls = 0
    TrackingFeedClient.should_fail = False
    monkeypatch.setattr(fetch_module.httpx, "AsyncClient", TrackingFeedClient)
    monkeypatch.setattr(
        fetch_module.feedparser,
        "parse",
        lambda _text, **_kwargs: SimpleNamespace(entries=[]),
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


def test_enrichment_fetches_concurrently_over_one_client_and_keeps_order(monkeypatch):
    class ConcurrentArticleClient:
        instances = 0
        in_flight = 0
        peak = 0

        def __init__(self, *_args, **_kwargs):
            type(self).instances += 1

        async def __aenter__(self):
            return self

        async def __aexit__(self, *_args):
            return None

        async def get(self, url):
            cls = type(self)
            cls.in_flight += 1
            cls.peak = max(cls.peak, cls.in_flight)
            index = int(url.rsplit("/", 1)[-1])
            # Later articles answer first; results must still follow input order.
            await asyncio.sleep(0.001 * (20 - index))
            cls.in_flight -= 1
            return SimpleNamespace(
                status_code=200,
                text=f"<article><p>Body {index}</p></article>",
            )

    monkeypatch.setattr(fetch_module.httpx, "AsyncClient", ConcurrentArticleClient)
    articles = [
        {"title": f"Story {i}", "link": f"https://example.com/{i}", "content": ""}
        for i in range(20)
    ]

    result = asyncio.run(
        SentryDigestFeedClient("https://example.com/feed.xml").enrich_article_content(
            articles
        )
    )

    assert [article["content"] for article in result] == [
        f"Body {i}" for i in range(20)
    ]
    assert all(article["content_kind"] == "article" for article in result)
    assert ConcurrentArticleClient.instances == 1
    assert 1 < ConcurrentArticleClient.peak <= fetch_module.ARTICLE_FETCH_CONCURRENCY
