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
