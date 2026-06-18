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

    assert articles[0]["content"] == "Sparse article\nSummary only\n"
    assert TrackingArticleClient.called is False
