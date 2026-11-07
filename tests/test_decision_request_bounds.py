"""Byte bounds of one decision request, pinned against the batcher constants.

``build_batches`` encodes with ``ensure_ascii=False``, so a character costs at
most four UTF-8 bytes, except C0 control characters, which JSON escapes as six
bytes (``\\u0001``). Title and text are truncated, so they alone can never make
one article exceed ``MAX_REQUEST_BYTES``. CVE identifiers are not truncated: the
pattern accepts any number of sequence digits and structured ``cves`` entries
are copied as given, so only they can make a single article reach
``input_limit``, which makes triage fall back to the complete article set.
"""

import pytest

from src.core import exploitation_decisions as decisions

WORST_CHARS = ("\x01", "\U0001f600", '"', "\\", "a")


@pytest.mark.parametrize("char", WORST_CHARS)
def test_truncated_title_and_text_alone_stay_under_the_request_cap(char):
    article = {
        "title": char * (decisions.TITLE_CHARS + 50),
        "content": char * (decisions.TEXT_CHARS + 500),
    }
    alone = decisions.build_batches([article])
    assert len(alone) == 1
    worst = 6 * (decisions.TITLE_CHARS + decisions.TEXT_CHARS)
    empty = len(decisions.build_batches([{"title": "", "content": ""}])[0][0])
    assert len(alone[0][0]) <= empty + worst < decisions.MAX_REQUEST_BYTES


def test_the_last_permitted_article_key_still_fits():
    # The key appears three times; the longest key is article_63.
    article = {"title": "\x01" * 200, "content": "\x01" * 1500}
    articles = [article] * decisions.MAX_ARTICLES
    batches = decisions.build_batches(articles)
    assert sorted(i for _, indices in batches for i in indices) == list(range(64))
    assert all(len(body) <= decisions.MAX_REQUEST_BYTES for body, _ in batches)


@pytest.mark.parametrize(
    "article",
    [
        {"title": "t", "content": "CVE-2026-" + "1" * 30000},
        {"title": "t", "content": "x", "cves": ["Z" * 30000]},
    ],
)
def test_only_untruncated_cve_identifiers_can_reach_the_input_limit(article):
    with pytest.raises(decisions.DecisionError, match="input_limit"):
        decisions.build_batches([article])
