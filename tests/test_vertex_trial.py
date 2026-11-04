"""The extra approved Vertex request cannot repeat either consumed allocation."""

import json
import os
from pathlib import Path
import sys

import httpx
import pytest

from scripts import continue_vertex_trial_once as vertex
from scripts import verify_selected_models_once as base


@pytest.fixture(scope="module")
def layout():
    return base.Layout(
        Path(os.environ["SELECTED_TRIAL_SENTRY_SOURCE"]),
        Path(os.environ["SELECTED_TRIAL_GRC_SOURCE"]),
        Path(sys.executable),
        Path(os.environ["SELECTED_TRIAL_GRC_PYTHON"]),
        Path(os.environ["TIKTOKEN_CACHE_DIR"]),
    )


@pytest.fixture(scope="module")
def prepared(layout):
    return vertex.prepare_vertex(layout)


def response(layout, *, provider="Google", tier="default"):
    case = json.loads((layout.grc / base.CASES[base.Case.GRC].fixture).read_bytes())
    return {
        "model": "google/gemini-4-argon",
        "provider": provider,
        "service_tier": tier,
        "choices": [
            {
                "finish_reason": "stop",
                "message": {"content": json.dumps(case["calibration_plan"])},
            }
        ],
        "usage": {
            "prompt_tokens": 4000,
            "completion_tokens": 1000,
            "total_tokens": 5000,
            "cost": 0.018,
        },
    }


def test_first_durable_vertex_claim_consumes_both_prior_runs(tmp_path, monkeypatch):
    snapshots = []
    original = base.Claim._save

    def save(claim):
        snapshots.append(json.loads(json.dumps(claim.value)))
        original(claim)

    monkeypatch.setattr(base.Claim, "_save", save)
    with vertex.VertexClaim(
        tmp_path / "claim.json", base.Context("a" * 40, "12345", base.TEST_REF)
    ) as claim:
        first = snapshots[0]
        assert first["states"] == {
            "sentry": "consumed_prior_run",
            "grc_ai_studio": "consumed_prior_run",
            "grc": "pending",
        }
        assert first["reserved_microusd"] == 608000
        assert first["prior_runs"] == [
            {
                "run_id": "41777105615",
                "executor_commit": "26234bd3f1cd7e580c739c019c50bf217ed13d84",
                "case": "sentry",
            },
            {
                "run_id": "41778423600",
                "executor_commit": "f72903e6b4d1370f988044df00abe6286fcce1a1",
                "case": "grc_ai_studio",
            },
        ]
        assert first["requests"]["grc"]["requested_provider"] == "google-vertex/global"
        with pytest.raises(base.TrialError):
            claim.start(base.Case.SENTRY)
        with pytest.raises(base.TrialError):
            claim.finish(base.Case.SENTRY, "response_received")
        claim.start(base.Case.GRC)
        claim.finish(base.Case.GRC, "response_received")


def test_vertex_wire_differs_only_in_provider_pin(prepared):
    payload = json.loads(prepared.wire)
    assert payload["provider"]["only"] == ["google-vertex/global"]
    payload["provider"]["only"] = ["google-ai-studio"]
    assert base.sha(base.canonical(payload)) == base.CASES[base.Case.GRC].canonical_sha
    original = prepared.wire.replace(b'"google-vertex/global"', b'"google-ai-studio"')
    assert base.sha(original) == base.CASES[base.Case.GRC].wire_sha
    assert prepared.wire.count(b'"google-vertex/global"') == 1
    assert payload["max_tokens"] == 8000 and payload["provider"]["zdr"] is True
    assert payload["provider"]["data_collection"] == "deny"


def test_only_vertex_worker_modes_are_used(layout, monkeypatch):
    calls = []
    worker = base._worker

    async def guard(layout, case, mode, response=b""):
        calls.append((case, mode))
        assert case is base.Case.GRC and mode in {"prepare_vertex", "validate_vertex"}
        return await worker(layout, case, mode, response)

    monkeypatch.setattr(base, "_worker", guard)
    vertex.prepare_vertex(layout)
    assert calls == [(base.Case.GRC, "prepare_vertex")]


def test_exactly_one_vertex_post_and_real_grounded_replay(tmp_path, prepared, layout):
    seen = []

    def handler(request):
        seen.append(request)
        assert str(request.url) == base.ENDPOINT and request.method == "POST"
        assert request.content == prepared.wire and len(seen) == 1
        assert json.loads(request.content)["provider"]["only"] == [
            "google-vertex/global"
        ]
        return httpx.Response(200, json=response(layout))

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        receipt = vertex.execute_vertex(
            prepared,
            layout,
            base.Context("a" * 40, "12345", base.TEST_REF),
            tmp_path / "claim.json",
            lambda: "synthetic-test-key",
            client,
        )
    assert len(seen) == 1 and receipt["cases"][0]["host"]["outcome"] == "passed"
    assert (
        receipt["upper_estimate_usd"] == 0.608
        and receipt["prior_admission_bound_usd"] == 0.484
    )
    assert receipt["actual_combined_cost"] is None and receipt["actual_cost"] == 0.018
    assert receipt["prior_ai_studio_cost"] is None
    assert "synthetic-test-key" not in json.dumps(receipt)


@pytest.mark.parametrize(
    "failure", ["404", "timeout", "ai_studio", "priority", "null_tier", "replay"]
)
def test_vertex_failure_stops_with_no_repeat(
    tmp_path, prepared, layout, monkeypatch, failure
):
    seen = []

    def handler(request):
        seen.append(request)
        if failure == "404":
            return httpx.Response(404, text="untrusted-private-error")
        if failure == "timeout":
            raise httpx.ReadTimeout("untrusted-private-error")
        return httpx.Response(
            200,
            json=response(
                layout,
                provider="Google AI Studio" if failure == "ai_studio" else "Google",
                tier=(
                    "priority"
                    if failure == "priority"
                    else (None if failure == "null_tier" else "default")
                ),
            ),
        )

    async def unavailable(*_args):
        raise base.TrialError("worker_failed")

    if failure == "replay":
        monkeypatch.setattr(base, "_worker", unavailable)
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        receipt = vertex.execute_vertex(
            prepared,
            layout,
            base.Context("a" * 40, "12345", base.TEST_REF),
            tmp_path / "claim.json",
            lambda: "synthetic-test-key",
            client,
        )
    assert len(seen) == 1 and receipt["cases"][0]["outcome"] != "passed"
    assert "untrusted-private-error" not in json.dumps(receipt)
    if failure in {"404", "timeout"}:
        assert receipt["actual_cost"] is None


def test_workflow_invokes_only_vertex_entry():
    import yaml

    workflow = yaml.load(
        (base.ROOT / ".github/workflows/verify-nemotron.yml").read_text(),
        Loader=yaml.BaseLoader,
    )
    commands = "\n".join(
        step.get("run", "") for step in workflow["jobs"]["verify"]["steps"]
    )
    assert "continue_vertex_trial_once" in commands
    assert "continue_argon_trial_once" not in commands
    assert "verify_selected_models_once.py" not in commands


def test_consumed_or_mutated_preparation_cannot_read_key_or_reserve(
    tmp_path, prepared, layout
):
    from dataclasses import replace

    wrong_specs = [
        base.PreparedTrial(base.CASES[base.Case.SENTRY], prepared.wire),
        base.PreparedTrial(base.CASES[base.Case.GRC], prepared.wire),
        replace(
            prepared,
            wire=prepared.wire.replace(
                b'"google-vertex/global"', b'"google-ai-studio"'
            ),
        ),
    ]
    for value in wrong_specs:
        with httpx.Client(
            transport=httpx.MockTransport(lambda _r: pytest.fail(reason="POST"))
        ) as client:
            with pytest.raises(base.TrialError):
                vertex.execute_vertex(
                    value,
                    layout,
                    base.Context("a" * 40, "12345", base.TEST_REF),
                    tmp_path / "claim.json",
                    lambda: pytest.fail(reason="key read"),
                    client,
                )
    assert not (tmp_path / "claim.json").exists()


def test_vertex_mode_cannot_prepare_sentry(layout):
    import asyncio

    with pytest.raises(base.TrialError):
        asyncio.run(base._worker(layout, base.Case.SENTRY, "prepare_vertex"))
