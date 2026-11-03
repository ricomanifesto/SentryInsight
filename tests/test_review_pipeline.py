"""Production source preflight and last-good behavior without provider calls."""

import asyncio
import importlib
from unittest.mock import AsyncMock


from src.core.source_review import PLAN_KEY, prepare_source_review
from test_reviewed_report import prepared_result
from test_source_review import AMBIGUOUS
from test_version_references import source


def load_modules():
    # Other legacy unit modules deliberately replace imports with stubs.
    import src.core.analyze as analyze
    import src.core.workflow as workflow

    return importlib.reload(analyze), importlib.reload(workflow)


def state_for(tmp_path, articles):
    return {
        "articles": articles,
        "filtered_articles": articles,
        "analysis_results": {},
        "status": "started",
        "config": {"output_path": str(tmp_path / "index.md")},
    }


def test_analysis_persists_full_plan_then_only_sends_eligible_sources(
    tmp_path, monkeypatch
):
    analyze, _ = load_modules()
    good, held = source("A campaign advisory.", "good"), source(AMBIGUOUS, "held")
    plan = prepare_source_review([good, held])

    async def generate(**kwargs):
        assert (
            tmp_path / ".sentryinsight-review" / (plan.packet["plan_id"] + ".json")
        ).exists()
        assert "https://example.test/held" not in kwargs["user_prompt"]
        assert "https://example.test/good" in kwargs["user_prompt"]
        return prepared_result([good, held])["exploitation_report"]

    client = AsyncMock()
    client.generate.side_effect = generate
    result = asyncio.run(
        analyze.analyze_exploitation(
            [good, held], state_for(tmp_path, [])["config"], model_client=client
        )
    )
    assert result[PLAN_KEY] == plan.packet
    assert len(result["reporting_sources"]) == 2
    assert result["analyzed_article_count"] == 1
    client.generate.assert_awaited_once()


def test_all_held_persists_queue_without_constructing_provider(tmp_path, monkeypatch):
    analyze, _ = load_modules()
    client = AsyncMock()
    result = asyncio.run(
        analyze.analyze_exploitation(
            [source(AMBIGUOUS, "held")],
            state_for(tmp_path, [])["config"],
            model_client=client,
        )
    )
    assert result["skip_reason"] == "source_review_required"
    assert list((tmp_path / ".sentryinsight-review").glob("*.json"))
    client.generate.assert_not_awaited()


def test_queue_persistence_failure_prevents_provider_call(tmp_path, monkeypatch):
    analyze, _ = load_modules()
    monkeypatch.setattr(
        analyze,
        "write_review_packet",
        lambda *_: (_ for _ in ()).throw(OSError("disk")),
    )
    client = AsyncMock()
    result = asyncio.run(
        analyze.analyze_exploitation(
            [source("A campaign advisory.", "good")],
            state_for(tmp_path, [])["config"],
            model_client=client,
        )
    )
    assert result["error_class"] == "source_review_failed"
    client.generate.assert_not_awaited()


def test_preflight_and_packet_persistence_happen_even_before_unchanged_skip(
    tmp_path, monkeypatch
):
    _, workflow = load_modules()
    articles = [source("A campaign advisory.", "good"), source(AMBIGUOUS, "held")]
    monkeypatch.setattr(workflow, "filter_exploitation_articles", lambda items: items)
    first = asyncio.run(workflow.filter_articles(state_for(tmp_path, articles)))
    (tmp_path / ".sentryinsight-articles-fingerprint").write_text(
        first["articles_fingerprint"]
    )
    for packet in (tmp_path / ".sentryinsight-review").glob("*.json"):
        packet.unlink()
    second = asyncio.run(workflow.filter_articles(state_for(tmp_path, articles)))
    assert second["status"] == "completed_unchanged"
    assert list((tmp_path / ".sentryinsight-review").glob("*.json"))
    assert second[PLAN_KEY] == first[PLAN_KEY]


def test_pending_recovery_blocks_before_analysis(tmp_path, monkeypatch):
    _, workflow = load_modules()
    from src.core.publication_transaction import JOURNAL_DIRECTORY

    (tmp_path / JOURNAL_DIRECTORY).mkdir()
    monkeypatch.setattr(workflow, "filter_exploitation_articles", lambda items: items)
    result = asyncio.run(
        workflow.filter_articles(
            state_for(tmp_path, [source("A campaign advisory.", "good")])
        )
    )
    assert result["status"] == "failed"
    assert result["failure"]["codes"] == ["publication_recovery_required"]


def test_new_generation_requires_preflight_proof_before_writing(tmp_path):
    _, workflow = load_modules()
    state = state_for(tmp_path, [])
    state["analysis_results"] = prepared_result()
    result = asyncio.run(workflow.generate_report(state))
    assert result["status"] == "failed"
    assert result["failure"]["codes"] == ["source_review_plan_missing"]
    assert not (tmp_path / "index.md").exists()


def test_partial_valid_report_advances_bound_fingerprint_and_discloses_coverage(
    tmp_path, monkeypatch
):
    _, workflow = load_modules()
    articles = [source("A campaign advisory.", "good"), source(AMBIGUOUS, "held")]
    monkeypatch.setattr(workflow, "filter_exploitation_articles", lambda items: items)
    state = asyncio.run(workflow.filter_articles(state_for(tmp_path, articles)))
    state["analysis_results"] = prepared_result(articles)
    result = asyncio.run(workflow.generate_report(state))
    assert result.get("report_generated") is True, result.get("failure")
    assert (
        tmp_path / ".sentryinsight-articles-fingerprint"
    ).read_text().strip() == state["articles_fingerprint"]
    assert "Partial source coverage" in (tmp_path / "index.html").read_text()
    assert "https://example.test/held" in (tmp_path / "index.md").read_text()
    result = asyncio.run(workflow.publish_results(result))
    assert result["status"] == "completed_with_review"


def test_analysis_catalog_cannot_omit_preflight_held_inputs(tmp_path, monkeypatch):
    _, workflow = load_modules()
    good, held = source("A campaign advisory.", "good"), source(AMBIGUOUS, "held")
    monkeypatch.setattr(workflow, "filter_exploitation_articles", lambda items: items)
    state = asyncio.run(workflow.filter_articles(state_for(tmp_path, [good, held])))
    state["analysis_results"] = prepared_result([good])
    result = asyncio.run(workflow.generate_report(state))
    assert result["status"] == "failed"
    assert result["failure"]["codes"] == ["source_review_plan_mismatch"]
    assert not (tmp_path / "index.md").exists()
