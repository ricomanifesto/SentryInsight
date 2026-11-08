"""An ordinary successful run exports bounded telemetry and no content.

The failure-path tests use sentinel strings; this replays a complete run that
publishes a report, with shadow article triage deciding every article, and
checks that no article title, text, URL, source link or model prose reaches
any exported span while the run, stage and triage attributes are present.
"""

import asyncio
import importlib
import json
import types
from unittest.mock import AsyncMock

from src.core import exploitation_triage as triage
from src.core.exploitation_triage import ArticleDecision, DecisionResult, LABELS
from test_derivation_counts import _report

TITLE = "SENTINELTITLE"
BODY = "SENTINELBODY"
URL = "sentinelurl"
LINK = "sentinelvendorlink"
PROSE = "SENTINELPROSE"


def _article(index: int) -> dict:
    cve = f"CVE-2026-{41100 + index}"
    return {
        "title": f"Synthetic advisory {TITLE} {index}",
        "source": "Fictional Security Bulletin",
        "link": f"https://example.test/{URL}-{index:02d}",
        "content": (
            f"{cve} is actively exploited. {BODY}.\n\n"
            f"Affected versions: Example Gateway 1.{index}.\n\n"
            "Customers should install the patch."
        ),
        "content_kind": "article",
        "source_links": [f"https://vendor.example.test/{LINK}/{41100 + index}"],
    }


class ShadowClient:
    async def classify(self, articles):
        rest = 0.005
        return DecisionResult(
            tuple(
                ArticleDecision(
                    index,
                    "exploitation_relevant",
                    {
                        key: 0.99 if key == "exploitation_relevant" else rest
                        for key in LABELS
                    },
                    0.9,
                )
                for index in range(len(articles))
            ),
            ("typesafe/jev-1.13",),
            120,
            0.0001,
            0,
            0.01,
        )


def test_successful_shadow_run_exports_attributes_and_no_content(
    capfire, monkeypatch, tmp_path
):
    import src.core.workflow as workflow

    workflow = importlib.reload(workflow)
    articles = [_article(index) for index in range(2)]
    report = _report(articles).replace(
        "The supplied advisories describe the findings below.",
        f"The supplied advisories describe the findings below ({PROSE}).",
    )
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    monkeypatch.setattr(
        workflow,
        "load_config",
        lambda: {
            "feed_url": "test",
            "output_path": str(tmp_path / "index.md"),
            "analysis": {"triage": {"mode": "shadow"}},
        },
    )
    monkeypatch.setattr(
        workflow,
        "SentryDigestFeedClient",
        lambda *_args: types.SimpleNamespace(
            fetch_articles=AsyncMock(return_value=articles),
            enrich_article_content=AsyncMock(side_effect=lambda items: items),
        ),
    )
    monkeypatch.setattr(workflow, "filter_exploitation_articles", lambda items: items)
    monkeypatch.setattr(triage, "_default_client", lambda _settings: ShadowClient())
    monkeypatch.setenv(triage.RECEIPT_ENV_PATH, str(tmp_path / "triage.json"))
    client = AsyncMock()
    client.generate.return_value = report
    real_analyze = workflow.analyze_exploitation

    async def analyze_with_client(items, config):
        return await real_analyze(items, config, model_client=client)

    monkeypatch.setattr(workflow, "analyze_exploitation", analyze_with_client)

    result = asyncio.run(workflow.run_exploitation_analysis())

    assert result["report_generated"] is True, result.get("failure")
    spans = capfire.exporter.exported_spans_as_dict(parse_json_attributes=True)
    by_name = {span["name"]: span for span in spans}
    root = by_name["sentryinsight.run"]
    for stage in ("fetch", "enrich", "filter", "analyze", "generate", "publish"):
        span = by_name[f"sentryinsight.{stage}"]
        assert span["parent"]["span_id"] == root["context"]["span_id"]
    filter_attributes = by_name["sentryinsight.filter"]["attributes"]
    assert filter_attributes["triage.mode"] == "shadow"
    assert filter_attributes["triage.status"] == "decided"
    payload = json.dumps(spans)
    for sentinel in (TITLE, BODY, URL, LINK, PROSE):
        assert sentinel not in payload, sentinel
    # The article text did reach the model and the published report.
    assert TITLE in (tmp_path / "index.md").read_text()
