"""Production-shaped combinations of failures, using only inert local inputs."""

import asyncio
import json
from pathlib import Path
from unittest.mock import AsyncMock

import httpx
import pytest

from src.core.openrouter_client import OpenRouterClient, OpenRouterError
from src.core.repair_budget import MemoryRepairBudget
from src.core.report_artifact import parse_report_artifact
from src.core.reporting import reporting_key
from test_informed_repair import (
    SOURCES,
    TITLES,
    draft,
    finding,
    install,
    run,
    source,
    world,
)
from test_report_artifact import REPORT
from test_review_pipeline import load_modules, state_for

CVE = "CVE-2099-1001"
OTHER = "CVE-2099-1002"


def missing_bold_description(row):
    return row.replace("- **Severity**", "- **Impact**\n- **Severity**")


@pytest.mark.parametrize("summary_label", ["Overview", "Impact"])
def test_malformed_section_preceding_a_finding_spends_first_repair_on_section(
    monkeypatch, summary_label
):
    plan, keys, results = world()
    first = finding(TITLES[0], keys[0])
    second = finding(TITLES[1], keys[1])
    good = draft([first, second])
    fixed_summary = good.split("## Executive Summary", 1)[1].split(
        "## Active Exploitation Details", 1
    )[0]
    mixed = good.replace(second, missing_bold_description(second)).replace(
        "Review the source details before choosing a response.",
        f"- **{summary_label}**",
    )
    worker = install(monkeypatch, ["## Executive Summary" + fixed_summary, second])

    outcome = run(results, mixed, plan, advisory=True)

    assert outcome.error is None
    assert "Section: ## Executive Summary" in worker.calls[0]["user_prompt"]
    assert TITLES[1] in worker.calls[1]["user_prompt"]
    assert [
        (x["kind"], x["finding_index"], x["outcome"]) for x in outcome.attempts
    ] == [
        ("original", None, "rejected"),
        ("repair_section", 2, "rejected"),
        ("repair_finding", 2, "repaired"),
    ]


@pytest.mark.parametrize(
    "original_id,replacement_id",
    [(CVE, OTHER), (CVE, None), (CVE, f"{CVE}, {OTHER}"), (None, OTHER)],
)
def test_syntax_repair_preserves_cve_identity_even_with_the_same_source(
    monkeypatch, original_id, replacement_id
):
    plan, keys, results = world(
        2,
        [
            f"The advisory lists separate service records {CVE} and {OTHER}.",
            SOURCES[1][0],
        ],
    )
    good = finding(TITLES[0], keys[0], **{"CVE IDs": original_id})
    wrong = finding(TITLES[0], keys[0], **{"CVE IDs": replacement_id})
    worker = install(monkeypatch, [wrong, good])

    outcome = run(
        results,
        draft([missing_bold_description(good), finding(TITLES[1], keys[1])]),
        plan,
        advisory=True,
    )

    assert outcome.error is None
    assert len(worker.calls) == 2
    assert [r.cve_ids for r in outcome.artifact.findings] == [
        (original_id,) if original_id else (),
        (),
    ]
    assert [x["outcome"] for x in outcome.attempts] == [
        "rejected",
        "splice_rejected",
        "repaired",
    ]


def test_cve_repair_may_clean_a_fragment_and_normalize_complete_identity(monkeypatch):
    plan, keys, results = world(2, [f"The advisory lists {CVE}.", SOURCES[1][0]])
    good = finding(TITLES[0], keys[0], **{"CVE IDs": CVE})
    bad = good.replace(CVE, CVE.replace("-", "\u2011") + ", CVE-2099-12")
    # The first failure is structural. Its localized replacement normalizes
    # spelling and discards a partial token, but preserves the actual identity.
    worker = install(monkeypatch, [good])

    outcome = run(
        results,
        draft([missing_bold_description(bad), finding(TITLES[1], keys[1])]),
        plan,
        advisory=True,
    )

    assert outcome.error is None
    assert len(worker.calls) == 1
    assert [row.cve_ids for row in outcome.artifact.findings] == [(CVE,), ()]


def test_global_cap_with_no_repair_response_does_not_drop_a_finding(monkeypatch):
    plan, keys, results = world(3)
    broken = missing_bold_description(finding(TITLES[1], keys[1]))
    invalid_id = finding(TITLES[2], keys[2], **{"CVE IDs": "CVE-2099-12"})
    outage = OpenRouterError("offline fixture", retryable=True, http_status=503)
    worker = install(monkeypatch, [outage])
    report = draft([finding(TITLES[0], keys[0]), broken, invalid_id])

    outcome = run(
        results, report, plan, advisory=True, budget=MemoryRepairBudget(max_repairs=2)
    )

    assert len(worker.calls) == 2
    assert outcome.artifact is None
    assert outcome.error is not None
    assert outcome.dropped_findings == ()
    assert outcome.attempts[-1]["rule"] == "malformed_markdown"
    assert outcome.attempts[-1]["finding_index"] == 2
    assert outcome.attempts[-1]["outcome"] == "budget_refused"


@pytest.mark.parametrize(
    "phases,budgets,wait,error_class",
    [
        (("transient", "length", "valid"), (96000, 96000, 131072), 1.0, None),
        (("length", "transient", "valid"), (96000, 131072, 131072), 2.0, None),
        (
            ("transient", "length", "length"),
            (96000, 96000, 131072),
            1.0,
            "model_output_limit_exceeded",
        ),
        (
            ("transient", "length", "transient"),
            (96000, 96000, 131072),
            1.0,
            "model_provider_unavailable",
        ),
        (
            ("transient", "length", "uncertain"),
            (96000, 96000, 131072),
            1.0,
            "model_request_failed",
        ),
    ],
)
def test_transient_and_output_ceiling_keep_shared_request_cap_and_last_good(
    monkeypatch, tmp_path, caplog, phases, budgets, wait, error_class
):
    analyze, workflow = load_modules()
    from src.core import model_client

    article = source("A service advisory with no assigned vulnerability ID.", "one")
    result_text = draft([finding(TITLES[0], reporting_key(article["link"]))])
    cfg = json.loads(Path("config/config.json").read_text())
    cfg["output_path"] = str(tmp_path / "index.md")
    state = state_for(tmp_path, [article])
    state["config"] = cfg
    files = {
        "index.md": REPORT,
        "index.html": "<p>Last-known-good report</p>",
        "current-findings.json": '{"schema_version":1,"finding_count":2}',
        ".sentryinsight-articles-fingerprint": "prior",
    }
    for name, text in files.items():
        (tmp_path / name).write_text(text)
    outbound = []

    def reply(request):
        payload = json.loads(request.content)
        outbound.append(payload)
        phase = phases[len(outbound) - 1]
        if phase == "uncertain":
            raise httpx.ReadTimeout("UNVERIFIED_PARTIAL_MARKER")
        if phase == "transient":
            return httpx.Response(503, json={"error": {"code": 503}})
        split = phase == "length"
        return httpx.Response(
            200,
            json={
                "model": payload["model"],
                "choices": [
                    {
                        "finish_reason": "length" if split else "stop",
                        "message": {
                            "content": (
                                "UNVERIFIED_PARTIAL_MARKER" if split else result_text
                            )
                        },
                    }
                ],
                "usage": {"completion_tokens": payload["max_tokens"] if split else 510},
            },
        )

    def mock_transport(**kwargs):
        return OpenRouterClient(transport=httpx.MockTransport(reply), **kwargs)

    sleep = AsyncMock()
    monkeypatch.setattr(asyncio, "sleep", sleep)
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    monkeypatch.setattr(model_client, "OpenRouterClient", mock_transport)
    monkeypatch.setattr(analyze, "build_model_client", model_client.build_model_client)
    monkeypatch.setattr(workflow, "filter_exploitation_articles", lambda items: items)

    async def run_pipeline():
        preflight = await workflow.filter_articles(state)
        analysis = await workflow.analyze_articles(preflight)
        return await workflow.generate_report(analysis)

    outcome = asyncio.run(run_pipeline())
    assert tuple(p["max_tokens"] for p in outbound) == budgets
    assert len({p["model"] for p in outbound}) == 1
    assert outbound[0]["messages"] == outbound[1]["messages"] == outbound[2]["messages"]
    assert all(
        not p["provider"]["allow_fallbacks"]
        and all(price == 0 for price in p["provider"]["max_price"].values())
        for p in outbound
    )
    sleep.assert_awaited_once_with(wait)
    assert "UNVERIFIED_PARTIAL_MARKER" not in caplog.text
    if error_class is None:
        assert outcome["report_generated"] is True
        assert [
            item.title
            for item in parse_report_artifact(
                (tmp_path / "index.md").read_text()
            ).findings
        ] == [TITLES[0]]
        assert (
            tmp_path / ".sentryinsight-articles-fingerprint"
        ).read_text().strip() == outcome["articles_fingerprint"]
    else:
        assert outcome["status"] == "failed"
        assert error_class in outcome["failure"]["codes"]
        assert outcome["report_generated"] is False
        assert all(
            (tmp_path / name).read_text() == original
            for name, original in files.items()
        )
        assert not (tmp_path / "reports").exists()
