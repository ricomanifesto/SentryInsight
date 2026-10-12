"""Capability coordinations retain each predicate; purpose is not an event."""

import pytest
import json
from src.core.assertions import parse_assertions
from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline

BODY = "In the discovery and login phases the agent acts without step-by-step supervision and autonomously maps unfamiliar login surfaces, discovers security weaknesses, and generates purpose-built automation to exploit them."


def test_complete_agent_capability_coordination_is_context_at_pipeline_boundary(
    monkeypatch, tmp_path
):
    clauses = parse_assertions(BODY)
    assert clauses and all(c.kind == "context" and not c.unsupported for c in clauses)
    assert {c.verb for c in clauses} == {"acts", "maps", "discovers", "generates"}

    def plan(**kwargs):
        from test_analyze_guards import reference_plan_from_prompt

        records = json.loads(
            kwargs["user_prompt"]
            .split("BEGIN FINDING RECORDS\n", 1)[1]
            .split("\nEND FINDING RECORDS", 1)[0]
        )
        candidate = next(e for e in records[0]["excerpts"] if e["text"] == BODY)
        result = json.loads(reference_plan_from_prompt(**kwargs))
        result["findings"][0]["excerpts"] = [candidate["id"]]
        return json.dumps(result)

    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        select_plan=plan,
        articles=[
            article(
                f"<h2>CVE-2026-1234</h2><p>CVE-2026-1234 exploitation status is unknown.</p><p>{BODY}</p>"
            )
        ],
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert BODY in report and "**Exploitation Status**: unknown" in report


@pytest.mark.parametrize(
    "tail",
    ["and unclassified predicates apply", "and it will have exploited CVE-2026-1234"],
)
def test_capability_cannot_swallow_unclassified_residual(monkeypatch, tmp_path, tail):
    text = BODY.rstrip(".") + " " + tail + "."
    paths = [
        tmp_path / n
        for n in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    ]
    for p in paths:
        p.write_bytes(b"Prior validated artifact")
    result = run_real_pipeline(
        monkeypatch,
        paths[0],
        articles=[article(f"<h2>CVE-2026-1234</h2><p>{text}</p>")],
        expect_model_call=False,
    )
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(p.read_bytes() == b"Prior validated artifact" for p in paths)
