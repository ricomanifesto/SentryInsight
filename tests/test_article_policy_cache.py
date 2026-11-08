"""The virtual-event decision is derived once per distinct article text."""

import uuid

from src.core import article_policy
from src.core.article_policy import (
    contains_virtual_event_tag,
    exclude_virtual_event_promotions,
    is_virtual_event_promotion,
)


def test_each_distinct_text_is_rendered_once_across_repeated_stages(monkeypatch):
    marker = uuid.uuid4().hex
    articles = [
        {
            "title": f"Patch {marker} {i}",
            "summary": "Ordinary advisory.",
            "content": f"Body {i}",
        }
        for i in range(3)
    ] + [{"title": f"[Virtual Event] Webinar {marker}", "content": "Join us."}]
    renders = []
    original = article_policy.MARKDOWN_PARSER.render

    def counted(text, *args, **kwargs):
        renders.append(text)
        return original(text, *args, **kwargs)

    monkeypatch.setattr(article_policy.MARKDOWN_PARSER, "render", counted)
    # The workflow re-checks the same records at fetch, enrich, filter and analyze.
    for _ in range(5):
        kept = exclude_virtual_event_promotions(articles)
    assert kept == articles[:3]
    first_pass = len(renders)
    for _ in range(5):
        assert [is_virtual_event_promotion(article) for article in articles] == [
            False,
            False,
            False,
            True,
        ]
    assert len(renders) == first_pass
    # The tagged title matches before any render; plain texts render once each.
    assert len(renders) == len(set(renders))


def test_cached_decisions_match_fresh_ones():
    texts = [
        "[virtual event] lowercase",
        "&#91;Virtual Event&#93; escaped",
        "<p>\\[Virtual Event\\] escaped markdown</p>",
        "Virtual event without brackets",
        "",
    ]
    cached = [contains_virtual_event_tag(text) for text in texts]
    fresh = [contains_virtual_event_tag.__wrapped__(text) for text in texts]
    assert cached == fresh == [True, True, True, False, False]
