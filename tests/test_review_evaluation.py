"""Full-case evaluation abstains explicitly; production partials are separate."""

import asyncio
import json

import pytest

from evals.grounding.dataset import Article, TaskInput, load_cases
from evals.grounding import model_task
from test_source_review import AMBIGUOUS
from test_version_references import source


def input_for(articles):
    return TaskInput(
        name="review-case",
        articles=[
            Article(**{k: ({"source_links": [], **a})[k] for k in Article.model_fields})
            for a in articles
        ],
        variant="baseline",
    )


def task_for(tmp_path, monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "fake-test-key")
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    return model_task.ModelTask(
        model="openrouter/example/model:free",
        receipts=tmp_path / "receipts.jsonl",
        max_requests=1,
    )


def test_any_held_source_abstains_before_provider_reservation(tmp_path, monkeypatch):
    task = task_for(tmp_path, monkeypatch)

    def forbidden(*a, **k):
        raise AssertionError("provider must not be constructed")

    monkeypatch.setattr(model_task, "FreeModelClient", forbidden)
    articles = [source("An advisory.", "good"), source(AMBIGUOUS, "held")]
    with pytest.raises(model_task.SourceReviewRequired):
        asyncio.run(task(input_for(articles)))
    assert task.requests == 0
    assert list((tmp_path / ".sentryinsight-review").glob("*.json"))
    receipt = json.loads((tmp_path / "receipts.jsonl").read_text())
    assert receipt["outcome"] == "source_review_required"
    assert receipt["attempts"] == 0
    assert AMBIGUOUS not in (tmp_path / "receipts.jsonl").read_text()


def test_eval_cannot_accept_a_candidate_rejected_by_shared_live_gate(
    tmp_path, monkeypatch
):
    task = task_for(tmp_path, monkeypatch)
    from test_unresolved_versions import raw_report
    from test_version_references import ABSENT
    from src.core.source_review import prepare_source_review, SourceReviewError

    article = source("An advisory.", "good")
    plan = prepare_source_review([article])

    async def generate(self, **kwargs):
        return raw_report(plan.eligible_keys, ABSENT).replace(
            "The supplied reporting", "CVE&#45;2026&#45;9999. The supplied reporting"
        )

    monkeypatch.setattr(model_task.FreeModelClient, "generate", generate)
    with pytest.raises(SourceReviewError, match="out_of_scope_candidate_cve"):
        asyncio.run(task(input_for([article])))
    assert task.requests == 1


def test_abstention_remains_in_evaluation_denominator(tmp_path):
    from evals.grounding.runner import run_evaluation

    async def abstain(_):
        raise model_task.SourceReviewRequired()

    result = asyncio.run(
        run_evaluation(
            load_cases()[:1],
            task=abstain,
            output=tmp_path / "evaluation",
            repetitions=1,
            variants=("baseline",),
            concurrency=1,
        )
    )
    assert result["planned"] == result["recorded"] == 1
    assert result["completed"] == result["field_pass_trials"] == 0
    assert result["source_review_required"] == 1
    assert result["execution_errors"] == 0


def test_eval_result_is_bound_to_its_original_complete_inputs(tmp_path, monkeypatch):
    from test_reviewed_report import prepared_result
    from unittest.mock import AsyncMock
    from src.core.source_review import SourceReviewError

    task = task_for(tmp_path, monkeypatch)
    original = source("An advisory.", "original")
    replacement = source("A different advisory.", "replacement")
    monkeypatch.setattr(
        model_task,
        "analyze_exploitation",
        AsyncMock(return_value=prepared_result([replacement])),
    )
    with pytest.raises(SourceReviewError, match="source_review_plan_mismatch"):
        asyncio.run(task(input_for([original])))
