from src.services.article_content import extract_article_content, normalize_feed_content
from src.core.analyze import format_article_summary


def test_article_owned_content_keeps_late_facts_and_excludes_sidebar():
    result = extract_article_content(
        '<html><nav>actively exploited</nav><div id="articlebody"><p>CVE-2026-1234 allows mailbox access.</p><p>'
        + "Context. " * 100
        + '</p><p>No exploitation observed in the wild.</p><ul><li>Example 2016 CU23</li><li>Example 2019 CU15</li></ul><p>Hosted customers need no action.</p><a href="https://example.test/vendor">Vendor</a></div><aside>Other flaw actively exploited</aside></html>',
        "https://example.test/news",
    )
    assert "No exploitation observed" in result.text
    assert "Example 2019 CU15" in result.text
    assert "Hosted customers" in result.text
    assert result.links == ("https://example.test/vendor",)
    assert "Other flaw" not in result.text
    assert "actively exploited" not in result.text


def test_no_article_container_is_not_misrepresented_as_full_content():
    assert (
        extract_article_content(
            "<html><nav>News</nav></html>", "https://example.test"
        ).text
        == ""
    )


def test_article_and_feed_extraction_preserve_heading_depth_for_detail_ownership():
    markup = "<article><h1>Advisory</h1><h2>CVE-2026-1234</h2><h3>Affected versions</h3><p>Example Server 2.3</p><h5>Deployment notes</h5><h6>Exceptions</h6><p>Hosted users need no action.</p></article>"
    for text in [
        extract_article_content(markup, "https://example.test").text,
        normalize_feed_content(markup),
    ]:
        assert "# Advisory" in text
        assert "## CVE-2026-1234" in text
        assert "### Affected versions" in text
        assert "##### Deployment notes" in text
        assert "###### Exceptions" in text


def test_feed_content_list_and_prompt_keep_qualifications():
    text = normalize_feed_content(
        [
            {
                "value": "<p>Intro</p><p>"
                + "Context. " * 100
                + "</p><p>No evidence of exploitation.</p>"
            }
        ]
    )
    prompt = format_article_summary({"title": "Example", "content": text})
    assert "No evidence of exploitation." in prompt
    assert "'value':" not in prompt


def test_ingestion_fetches_article_even_when_feed_has_content(monkeypatch):
    import asyncio
    from types import SimpleNamespace
    from src.services import fetch

    class Client:
        def __init__(self, **_kwargs):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *_args):
            pass

        async def get(self, _url):
            return SimpleNamespace(
                status_code=200,
                text="<article><p>CVE-2026-1234 disclosed.</p><p>No evidence of exploitation.</p></article>",
            )

    monkeypatch.setattr(fetch.httpx, "AsyncClient", Client)
    values = asyncio.run(
        fetch.SentryDigestFeedClient("unused").enrich_article_content(
            [
                {
                    "title": "Example",
                    "link": "https://example.test/advisory",
                    "content": [{"value": "Short feed snippet"}],
                }
            ]
        )
    )
    assert values[0]["content_kind"] == "article"
    assert "No evidence of exploitation." in values[0]["content"]


def test_ingestion_retains_feed_when_article_structure_is_unknown(monkeypatch):
    import asyncio
    from types import SimpleNamespace
    from src.services import fetch

    class Client:
        def __init__(self, **_kwargs):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *_args):
            pass

        async def get(self, _url):
            return SimpleNamespace(
                status_code=200, text="<html><nav>Other attacks</nav></html>"
            )

    monkeypatch.setattr(fetch.httpx, "AsyncClient", Client)
    values = asyncio.run(
        fetch.SentryDigestFeedClient("unused").enrich_article_content(
            [
                {
                    "title": "Example",
                    "link": "https://example.test/advisory",
                    "content": [{"value": "No evidence of exploitation."}],
                }
            ]
        )
    )
    assert values[0]["content_kind"] == "feed"
    assert values[0]["content"] == "No evidence of exploitation."


def test_input_budget_fails_before_model_call_instead_of_truncating(monkeypatch):
    import asyncio
    from test_analyze_guards import import_analyze_with_stubs

    analyze = import_analyze_with_stubs()

    def forbidden(**_kwargs):
        raise AssertionError("must not call provider")

    monkeypatch.setattr(analyze, "build_model_client", forbidden)
    result = asyncio.run(
        analyze.analyze_exploitation(
            [{"content": "Long complete source. " * 1000}],
            {
                "analysis": {
                    "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free",
                    "max_input_tokens": 10,
                }
            },
        )
    )
    assert "no source text was truncated" in result["error"]


def test_outer_html_list_items_keep_nested_context_and_sibling_boundaries():
    markup = "<article><ul><li>Do not:<ul><li><p>install the update</p></li><li>restart the service</li></ul></li><li>Contact support.</li></ul></article>"
    expected = "Do not: install the update; restart the service\n\nContact support."
    assert extract_article_content(markup, "https://example.test").text == expected
    assert normalize_feed_content(markup) == expected


def test_html_list_breaks_preserve_lines_without_splitting_the_outer_item():
    markup = "<article><ul><li>Affected versions:<br><br>Example Server 2.3<br>Example Server 2.4</li><li>Do not:<br> <br>install the update.</li></ul></article>"
    expected = "Affected versions:\nExample Server 2.3\nExample Server 2.4\n\nDo not:\ninstall the update."
    assert extract_article_content(markup, "https://example.test").text == expected
    assert normalize_feed_content(markup) == expected


def test_repeated_breaks_outside_lists_remain_paragraph_separators():
    for breaks in ["<br><br>", "<br> \n<br>"]:
        markup = f"<article>Background.{breaks}Install the update.</article>"
        expected = "Background.\n\nInstall the update."
        assert extract_article_content(markup, "https://example.test").text == expected
        assert normalize_feed_content(markup) == expected
