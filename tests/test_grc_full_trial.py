"""Only the fixed fictional GRC analysis and derived plan may be sent."""

import asyncio
import base64
from copy import deepcopy
from dataclasses import replace
import json
import os
from pathlib import Path

import httpx
import pytest

from scripts import verify_grc_workflow_once as trial
from scripts import verify_selected_models_once as base


def forbidden(*_args, **_kwargs):
    raise AssertionError("Unexpected credential, layout or transport access")


@pytest.fixture(scope="module")
def layout():
    return trial.Layout(
        Path(os.environ["GRC_FULL_SOURCE"]), Path(os.environ["GRC_FULL_PYTHON"])
    )


@pytest.fixture(scope="module")
def prepared(layout):
    return asyncio.run(trial.prepare(layout))


def reply(layout, stage, *, content=None):
    if content is None:
        if stage:
            case = json.loads(
                (
                    layout.source / "agent/tests/fixtures/selected_model_case.json"
                ).read_bytes()
            )
            content = json.dumps(case["calibration_plan"])
        else:
            content = json.loads(
                (
                    trial.ROOT
                    / "scripts/grc_workflow_fixture/selected_workflow_case.json"
                ).read_bytes()
            )["analysis_response"]
    return {
        "model": trial.MODEL,
        "provider": "Google",
        "service_tier": None,
        "id": "gen-synthetic",
        "choices": [{"finish_reason": "stop", "message": {"content": content}}],
        "usage": {
            "prompt_tokens": 2000,
            "completion_tokens": 300,
            "total_tokens": 2300,
            "cost": 0.007,
            "completion_tokens_details": {"reasoning_tokens": 100},
        },
    }


def streamed(value, *, status=200, headers=None):
    raw = json.dumps(value).encode() if not isinstance(value, bytes) else value
    return httpx.Response(status, stream=httpx.ByteStream(raw), headers=headers)


def run(tmp_path, layout, prepared, handler, read_key=lambda: "synthetic-never-real"):
    async def execute():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            return await trial.execute(
                prepared,
                layout,
                base.Context("a" * 40, "12345", base.TEST_REF),
                tmp_path / "claim.json",
                read_key,
                client,
            )

    return asyncio.run(execute())


def test_both_financial_reservations_are_fixed_before_sending():
    assert trial.INPUT_RESERVES == (8000, 24000)
    assert trial.OUTPUT_TOKENS == 8000
    assert trial.RESERVATIONS == (96000, 128000)
    assert sum(trial.RESERVATIONS) == 224000


def test_manifest_matches_the_closed_scope_and_reservations():
    manifest = json.loads(
        (trial.ROOT / "scripts/grc_workflow_fixture/manifest.json").read_bytes()
    )
    assert (
        manifest["source_commit"] == trial.SOURCE_COMMIT
        and manifest["source_tree"] == trial.SOURCE_TREE
    )
    assert (
        manifest["source_fixture_sha256"] == trial.CASE_SHA
        and manifest["workflow_fixture_sha256"] == trial.WORKFLOW_SHA
    )
    assert (
        manifest["model"] == trial.MODEL and manifest["provider_only"] == trial.PROVIDER
    )
    assert manifest["total_reservation_microusd"] == sum(trial.RESERVATIONS)
    assert (
        tuple(row["input_reserve"] for row in manifest["stages"])
        == trial.INPUT_RESERVES
    )
    assert (
        tuple(row["canonical_payload_sha256"] for row in manifest["stages"])
        == trial.CANONICAL
    )
    assert (
        tuple(row["calibration_wire_sha256"] for row in manifest["stages"])
        == trial.WIRE
    )
    assert manifest["new_execution_approval_required"] is True


def test_actual_full_workflow_preserves_both_frozen_prompt_and_wire_hashes(prepared):
    assert tuple(base.sha(raw) for raw in prepared.wires) == trial.WIRE
    assert (
        tuple(base.sha(base.canonical(json.loads(raw))) for raw in prepared.wires)
        == trial.CANONICAL
    )
    assert tuple(map(len, prepared.wires)) == trial.WIRE_BYTES


def test_two_posts_durable_reservation_and_null_metadata_pass(
    tmp_path, layout, prepared
):
    seen = []

    def key():
        claim = json.loads((tmp_path / "claim.json").read_bytes())
        assert claim["reserved_microusd"] == 224000
        assert claim["states"] == {"analysis": "pending", "plan": "pending"}
        assert claim["historical_allocations"] == "consumed_not_reused"
        return "synthetic-never-real"

    def handler(request):
        stage = len(seen)
        claim = json.loads((tmp_path / "claim.json").read_bytes())
        assert claim["states"][("analysis", "plan")[stage]] == "sending"
        assert claim["requests"][("analysis", "plan")[stage]][
            "wire_sha256"
        ] == base.sha(request.content)
        assert str(request.url) == base.ENDPOINT and request.method == "POST"
        assert request.content == prepared.wires[stage]
        assert "cookie" not in request.headers
        assert request.headers["accept-encoding"] == "identity"
        seen.append(request)
        value = reply(layout, stage)
        value.pop("provider")
        if stage:
            value.pop("service_tier")
        return streamed(value, headers={"set-cookie": "untrusted=session"})

    result = run(tmp_path, layout, prepared, handler, key)
    assert len(seen) == 2 and result["outcome"] == "passed"
    assert result["states"] == {
        "analysis": "response_received",
        "plan": "response_received",
    }
    assert (
        result["actual_cost"] == 0.014
        and result["host"]["grounded_control_findings"] == 1
    )
    assert all(
        row["actual_service_tier"] is None and row["serving_provider"] is None
        for row in result["operations"]
    )
    assert result["published"] is False and result["production_ready"] is False
    assert "synthetic-never-real" not in json.dumps(result)
    with pytest.raises(base.TrialError):
        run(
            tmp_path,
            layout,
            prepared,
            forbidden,
            forbidden,
        )


@pytest.mark.parametrize(
    "failure",
    [
        "401",
        "404",
        "timeout",
        "malformed",
        "model",
        "priority",
        "provider",
        "truncated",
        "cost_missing",
        "cost_bool",
        "cost_high",
        "tokens_missing",
        "tokens_total",
        "reasoning",
        "compressed",
        "large",
        "fallback",
        "unknown_title",
        "duplicate",
        "bullet",
        "markdown",
        "worker",
        "worker_protocol",
    ],
)
def test_first_stage_failure_never_sends_plan(
    tmp_path, layout, prepared, monkeypatch, failure
):
    seen = []
    answer = reply(layout, 0)
    if failure in {"fallback", "unknown_title", "duplicate", "bullet", "markdown"}:
        content = answer["choices"][0]["message"]["content"]
        answer["choices"][0]["message"]["content"] = (
            "Unrecognized prose that used to trigger fallback-to-all."
            if failure == "fallback"
            else (
                content.replace("Fictional supplier access incident", "Unknown source")
                if failure == "unknown_title"
                else (
                    "\n".join("- " + line for line in content.splitlines())
                    if failure == "bullet"
                    else (
                        "\n".join("**" + line + "**" for line in content.splitlines())
                        if failure == "markdown"
                        else content + "\n" + content.splitlines()[1]
                    )
                )
            )
        )
    mutations = {
        "model": (answer, "model", "moonshotai/kimi-k3.1-pro"),
        "priority": (answer, "service_tier", "priority"),
        "provider": (answer, "provider", "Google AI Studio"),
        "truncated": (answer["choices"][0], "finish_reason", "length"),
        "cost_bool": (answer["usage"], "cost", False),
        "cost_high": (answer["usage"], "cost", 0.5),
        "tokens_total": (answer["usage"], "total_tokens", 1),
        "reasoning": (
            answer["usage"]["completion_tokens_details"],
            "reasoning_tokens",
            301,
        ),
    }
    if failure in mutations:
        mapping, name, value = mutations[failure]
        mapping[name] = value
    if failure == "cost_missing":
        answer["usage"].pop("cost")
    if failure == "tokens_missing":
        answer["usage"].pop("prompt_tokens")
    if failure in {"worker", "worker_protocol"}:

        async def unavailable(*_args, **_kwargs):
            if failure == "worker":
                raise base.TrialError("worker_unavailable")
            return {"wires": [], "raw_private": "untrusted-private"}

        monkeypatch.setattr(trial, "worker", unavailable)

    def handler(request):
        seen.append(request)
        if failure == "timeout":
            raise httpx.ReadTimeout("untrusted-private")
        if failure in {"401", "404"}:
            return streamed(b"untrusted-private", status=int(failure))
        if failure == "malformed":
            return streamed(b"untrusted-private")
        if failure == "compressed":
            return streamed(b"untrusted-private", headers={"content-encoding": "gzip"})
        if failure == "large":
            return streamed(b"x" * (trial.RESPONSE_LIMIT + 1))
        return streamed(answer)

    result = run(tmp_path, layout, prepared, handler)
    assert len(seen) == 1 and result["outcome"] == "stopped"
    assert result["states"]["plan"] == "pending"
    assert result["actual_cost"] is None
    assert "untrusted-private" not in json.dumps(result)


def test_real_parser_derives_only_closed_fields_and_host_reconciled_counts(
    layout, prepared
):
    answer = reply(
        layout,
        0,
        content=(
            "Article 2: Title: Fictional supplier access incident score 8 relevant\nRegulations: GDPR and NIST"
        ),
    )
    derived = asyncio.run(
        trial.worker(layout, "derive", (json.dumps(answer).encode(),))
    )
    wire = trial.validate_derived(prepared, derived)
    value = json.loads(wire)
    assert derived["derived"]["grc_relevant_count"] in (1, 2)
    assert set(derived["derived"]["regulations"]) == {"GDPR", "NIST"}
    assert "Regulations: GDPR and NIST" not in value["messages"][1]["content"]
    assert "- Regulations/Frameworks:" in value["messages"][1]["content"]


@pytest.mark.parametrize(
    "mutation", ["source", "schema", "system", "answer", "count", "regulation"]
)
def test_derived_body_cannot_expand_sources_schema_or_insert_raw_answer(
    layout, prepared, mutation
):
    value = asyncio.run(
        trial.worker(layout, "derive", (json.dumps(reply(layout, 0)).encode(),))
    )
    value = deepcopy(value)
    payload = json.loads(base64.b64decode(value["wires"][1]))
    if mutation == "count":
        value["derived"]["grc_relevant_count"] = 3
    elif mutation == "regulation":
        value["derived"]["regulations"] = ["Unbounded invented regulation"]
    elif mutation == "schema":
        payload["response_format"] = {"type": "json_object"}
    elif mutation == "system":
        payload["messages"][0]["content"] += " modified"
    else:
        payload["messages"][1]["content"] += (
            " https://outside.example.test/"
            if mutation == "source"
            else reply(layout, 0)["choices"][0]["message"]["content"]
        )
    value["wires"][1] = base64.b64encode(json.dumps(payload).encode()).decode()
    with pytest.raises(base.TrialError):
        trial.validate_derived(prepared, value)


@pytest.mark.parametrize(
    "failure", ["grounding", "empty", "truncated", "auth", "cost", "replay"]
)
def test_second_stage_failure_stops_after_two_posts(
    tmp_path, layout, prepared, monkeypatch, failure
):
    seen = []
    original = trial.worker

    async def replay_unavailable(layout, mode, responses=()):
        if mode == "replay":
            raise base.TrialError("worker_unavailable")
        return await original(layout, mode, responses)

    if failure == "replay":
        monkeypatch.setattr(trial, "worker", replay_unavailable)

    def handler(request):
        stage = len(seen)
        seen.append(request)
        answer = reply(layout, stage)
        if stage:
            if failure == "auth":
                return streamed(b"private", status=401)
            if failure == "cost":
                answer["usage"].pop("cost")
            if failure == "truncated":
                answer["choices"][0]["finish_reason"] = "length"
            if failure in {"grounding", "empty"}:
                plan = json.loads(answer["choices"][0]["message"]["content"])
                if failure == "grounding":
                    plan["control_implications"][0][
                        "evidence_excerpt"
                    ] = "Unsupported assertion"
                else:
                    plan["control_implications"] = []
                answer["choices"][0]["message"]["content"] = json.dumps(plan)
        return streamed(answer)

    result = run(tmp_path, layout, prepared, handler)
    assert (
        len(seen) == 2
        and result["outcome"] == "stopped"
        and result["published"] is False
    )


def test_mutated_preparation_refuses_before_key_claim_and_transport(
    tmp_path, layout, prepared
):
    wrong = replace(
        prepared,
        wires=(
            prepared.wires[0].replace(b"google-vertex/global", b"google-ai-studio"),
            prepared.wires[1],
        ),
    )
    with pytest.raises(base.TrialError):
        run(
            tmp_path,
            layout,
            wrong,
            forbidden,
            forbidden,
        )
    assert not (tmp_path / "claim.json").exists()


def test_context_refuses_before_layout_source_or_key_access(monkeypatch):
    import sys

    monkeypatch.setattr(sys, "argv", ["grc-trial", "--expected-commit", "a" * 40])
    monkeypatch.setenv("GITHUB_ACTIONS", "false")
    monkeypatch.setattr(trial, "ci_layout", forbidden)
    assert trial.main() == 1


def test_claim_fsync_precedes_each_send_and_forbids_rearming(tmp_path, monkeypatch):
    syncs = []
    original = os.fsync

    def sync(fd):
        syncs.append(fd)
        original(fd)

    monkeypatch.setattr(base.os, "fsync", sync)
    context = base.Context("a" * 40, "12345", base.TEST_REF)
    with trial.WorkflowClaim(tmp_path / "claim.json", context) as claim:
        assert len(syncs) == 2  # Initial file and containing directory are durable.
        with pytest.raises(base.TrialError):
            claim.start_stage(1)
        claim.start_stage(0)
        assert len(syncs) == 3
        claim.finish_stage(0, "response_received")
        with pytest.raises(base.TrialError):
            claim.start_stage(0)
        for stage in (True, -1, 2):
            with pytest.raises(base.TrialError):
                claim.start_stage(stage)
        with pytest.raises((base.TrialError, KeyError)):
            claim.start(base.Case.SENTRY)
    with pytest.raises(base.TrialError):
        trial.WorkflowClaim(tmp_path / "claim.json", context)


def test_worker_never_inherits_actual_credentials_or_source_configuration():
    environment = trial.worker_environment(Path("/scratch"))
    assert "OPENROUTER_API_KEY" not in environment
    assert (
        environment["AWS_ACCESS_KEY_ID"]
        == environment["AWS_SECRET_ACCESS_KEY"]
        == "synthetic"
    )
    assert (
        environment["AWS_CONFIG_FILE"]
        == environment["AWS_SHARED_CREDENTIALS_FILE"]
        == "/dev/null"
    )
    assert environment["OTEL_SDK_DISABLED"] == "true"
    assert environment["PYTHONHASHSEED"] == "0"
    assert {name for name in environment if name.startswith("PYTHON")} == {
        "PYTHONHASHSEED",
        "PYTHONDONTWRITEBYTECODE",
    }


def test_worker_ignores_hostile_parent_python_controls_and_secret(
    layout, prepared, monkeypatch
):
    for name in ("PYTHONPATH", "PYTHONHOME", "PYTHONUSERBASE", "PYTHONSTARTUP"):
        monkeypatch.setenv(name, "/untrusted/not-used")
    monkeypatch.setenv("OPENROUTER_API_KEY", "synthetic-parent-only-not-used")
    value = asyncio.run(trial.worker(layout, "prepare"))
    assert trial.decoded_wires(value, 1) == (prepared.wires[0],)


def test_multi_regulation_derivation_and_replay_are_stable_across_fresh_workers(
    tmp_path, layout, prepared
):
    answer = reply(layout, 0)
    answer["choices"][0]["message"][
        "content"
    ] += "\nRegulations: GDPR, NIST and ISO 27001"
    raw = json.dumps(answer).encode()
    first = asyncio.run(trial.worker(layout, "derive", (raw,)))
    second = asyncio.run(trial.worker(layout, "derive", (raw,)))
    assert first == second
    assert set(first["derived"]["regulations"]) == {"GDPR", "NIST", "ISO 27001"}
    assert trial.validate_derived(prepared, first) == trial.validate_derived(
        prepared, second
    )
    seen = []

    def handler(request):
        stage = len(seen)
        seen.append(request)
        return streamed(answer if stage == 0 else reply(layout, 1))

    result = run(tmp_path, layout, prepared, handler)
    assert len(seen) == 2 and result["outcome"] == "passed"


def test_manual_workflow_is_grc_only_nonpublishing_and_secret_scoped():
    value = (trial.ROOT / ".github/workflows/verify-nemotron.yml").read_text()
    assert "workflow_dispatch:" in value and "contents: read" in value
    assert value.count("secrets.OPENROUTER_API_KEY") == 1
    assert "verify_grc_workflow_once.py" in value
    assert (
        "continue_vertex_trial_once" not in value
        and "continue_argon_trial_once" not in value
    )
    assert "sources/sentry" not in value and "TIKTOKEN" not in value
    assert "ref: " + trial.SOURCE_COMMIT in value
    assert "retention-days: 7" in value
    assert "runner.debug != '1'" in value
    assert "aws " not in value and "publish" not in value.lower().replace(
        "nonpublishing", ""
    )
    assert (
        json.loads((trial.ROOT / "vercel.json").read_bytes())["git"][
            "deploymentEnabled"
        ]
        is False
    )
