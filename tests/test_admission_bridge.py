"""Exercise the Python -> Node -> local Git CAS boundary without a network remote."""

import asyncio
import json
import os
from pathlib import Path
import shutil
import subprocess

import httpx
import pytest

from src.core.attempt_budget import AdmissionAttemptBudget, AttemptBudgetError
from src.core.openrouter_client import OpenRouterClient, OpenRouterError
from src.core.opencode_client import parse_model_selection


@pytest.fixture
def budget_factory(tmp_path, request):
    root = tmp_path / "repo"
    root.mkdir()
    remote = tmp_path / "remote.git"

    def command(*args):
        return subprocess.check_output(
            args, cwd=root, stderr=subprocess.DEVNULL, text=True
        ).strip()

    command("git", "init", "--bare", str(remote))
    command("git", "init", "--initial-branch=main")
    command("git", "config", "user.name", "Offline fixture")
    command("git", "config", "user.email", "fixture@example.invalid")
    command("git", "config", "commit.gpgsign", "false")
    command("git", "remote", "add", "origin", str(remote))
    shutil.copytree(
        Path(__file__).resolve().parents[1] / "publication",
        root / "publication",
        ignore=shutil.ignore_patterns("test"),
    )
    # Inject the existing clock dependency only in this disposable CLI copy.
    # Production exposes no clock override; this fixed one-use period remains
    # testable after its expiry without weakening the production gate.
    if hasattr(request, "param"):
        cli = root / "publication/cli.js"
        source = cli.read_text()
        marker = "const admission = createAdmission({"
        assert source.count(marker) == 1
        cli.write_text(
            source.replace(
                marker,
                marker + "\n      now: () => new Date('2026-11-17T16:10:00.000Z'),",
            )
        )
    command("git", "add", "publication")
    command("git", "commit", "-m", "Offline request-budget fixture")
    revision = command("git", "rev-parse", "HEAD")
    command("git", "push", "origin", "HEAD:main")
    (root / "event.json").write_text("{}")
    claim = json.loads(
        command(
            "node",
            "publication/cli.js",
            "admit",
            "--event-name",
            getattr(request, "param", "workflow_dispatch"),
            "--event-path",
            str(root / "event.json"),
            "--run-id",
            "9",
            "--run-attempt",
            "1",
        )
    )
    assert claim["decision"] == "admitted"
    command(
        "node",
        "publication/cli.js",
        "invoked",
        "--key",
        claim["admission_key"],
        "--run-id",
        "9",
    )

    def factory():
        value = AdmissionAttemptBudget(
            key=claim["admission_key"], run_id="9", revision=revision, run_attempt="1"
        )
        value.root = root
        return value

    return factory


def _seed_verification_history(budget):
    script = """
const {createStore}=require('./publication/kit/store');
const {createGit}=require('./publication/kit/git');
const store=createStore({git:createGit(process.cwd()),remote:'origin',branch:'publication-admission',site:'SentryInsight'});
store.append(()=>[
 {stage:'pilot_opening',periodStart:'2026-11-01T00:00:00.000Z',periodEnd:'2026-12-01T00:00:00.000Z',amountMicrousd:0},
 {stage:'spend_reserved',generationToken:'held',amountMicrousd:7251456},
 {stage:'spend_reserved',generationToken:'settled',amountMicrousd:7251456},
 {stage:'spend_settled',generationToken:'settled',actualMicrousd:64110,releasedMicrousd:7187346}
]).catch(()=>process.exit(1));
"""
    subprocess.run(
        ["node", "-e", script], cwd=budget.root, check=True, capture_output=True
    )


def _billing_fixture(budget):
    path = budget.root / "billing.json"
    path.write_text(
        json.dumps(
            dict(
                billing="credits-no-applicable-byok",
                coverage="all-applicable-ci-keys",
                periodStart="2026-11-01T00:00:00.000Z",
                periodEnd="2026-12-01T00:00:00.000Z",
                actualMicrousd=1400000,
                checkedAt="2026-11-17T16:00:00.000Z",
                scopeSha256="b" * 64,
            )
        )
    )
    import hashlib

    digest = hashlib.sha256(
        (
            json.dumps(json.loads(path.read_text()), sort_keys=True, indent=2) + "\n"
        ).encode()
    ).hexdigest()
    return [
        "--run-attempt",
        "1",
        "--billing-evidence",
        str(path),
        "--evidence-sha256",
        digest,
    ]


@pytest.mark.parametrize("budget_factory", ["workflow_dispatch"], indirect=True)
def test_paid_profile_is_exported_without_spend_or_network(budget_factory):
    budget = budget_factory()
    result = budget._invoke("verification-profile", [])
    assert result["profile"]["reserveMicrousd"] == 7956100
    assert result["profile"]["model"] == "moonshotai/kimi-k3.1-pro"
    assert len(result["sha256"]) == 64


@pytest.mark.parametrize("budget_factory", ["workflow_dispatch"], indirect=True)
def test_paid_cli_reservation_and_claims_survive_new_bridge_instances(budget_factory):
    first = budget_factory()
    _seed_verification_history(first)
    exported = first._invoke("verification-profile", [])
    assert first._invoke("verification-reserve", _billing_fixture(first)) == {
        "reservedMicrousd": 7956100,
        "profileSha256": exported["sha256"],
        "validUntil": 1794934800000,
    }
    with pytest.raises(AttemptBudgetError):
        budget_factory()._invoke("verification-reserve", _billing_fixture(first))
    assert budget_factory()._invoke("verification-report", ["--run-attempt", "1"]) == {
        "verified": True
    }
    options = ["--run-attempt", "1", "--slot", "0", "--request-sha256", "c" * 64]
    assert first._invoke("verification-triage", options) == {"claimed": True}
    with pytest.raises(AttemptBudgetError):
        budget_factory()._invoke("verification-triage", options)
    records = json.loads(
        subprocess.check_output(
            [
                "git",
                "--git-dir",
                str(first.root.parent / "remote.git"),
                "show",
                "publication-admission:state.json",
            ],
            text=True,
        )
    )["records"]
    assert len([row for row in records if row["stage"] == "verification_reserved"]) == 1
    assert any(
        row["stage"] == "spend_reserved" and row.get("generationToken") == "held"
        for row in records
    )


@pytest.mark.parametrize("budget_factory", ["schedule"], indirect=True)
def test_paid_cli_rejects_non_manual_admitted_episodes(budget_factory):
    budget = budget_factory()
    _seed_verification_history(budget)
    with pytest.raises(AttemptBudgetError):
        budget._invoke("verification-reserve", _billing_fixture(budget))


@pytest.mark.parametrize("budget_factory", ["workflow_dispatch"], indirect=True)
def test_paid_cli_rejects_proof_changed_after_metadata_preflight(budget_factory):
    budget = budget_factory()
    _seed_verification_history(budget)
    args = _billing_fixture(budget)
    path = budget.root / "billing.json"
    value = json.loads(path.read_text())
    value["actualMicrousd"] = 1000000
    path.write_text(json.dumps(value))
    with pytest.raises(AttemptBudgetError):
        budget._invoke("verification-reserve", args)


def test_real_bridge_reservation_survives_lost_client(budget_factory):
    first = asyncio.run(budget_factory().reserve("a" * 64, 3))
    assert first["attempt"] == 1
    with pytest.raises(AttemptBudgetError):
        asyncio.run(budget_factory().reserve("a" * 64, 3))
    asyncio.run(budget_factory().finish(first, "uncertain"))
    with pytest.raises(AttemptBudgetError):
        asyncio.run(budget_factory().reserve("a" * 64, 3))


def test_stale_event_uses_the_checked_out_revision_for_reserve_and_finish(
    budget_factory, monkeypatch
):
    fixture = budget_factory()
    for key, value in {
        "SENTRYINSIGHT_ADMISSION_KEY": fixture.key,
        "GITHUB_RUN_ID": fixture.run_id,
        "GITHUB_RUN_ATTEMPT": "1",
        "GITHUB_SHA": "a" * 40,
        "SENTRYINSIGHT_SOURCE_REVISION": fixture.revision,
    }.items():
        monkeypatch.setenv(key, value)
    budget = AdmissionAttemptBudget.from_environment()
    budget.root = fixture.root
    reservation = asyncio.run(budget.reserve("d" * 64, 3))
    assert reservation["attempt"] == 1
    assert budget.revision == fixture.revision
    asyncio.run(budget.finish(reservation, "response_received"))
    with pytest.raises(AttemptBudgetError):
        asyncio.run(budget.reserve("d" * 64, 3))
    assert os.environ["GITHUB_SHA"] == "a" * 40


@pytest.mark.parametrize("revision", ["", "bad", "A" * 40, "a" * 39])
def test_invalid_explicit_source_revision_never_falls_back(monkeypatch, revision):
    for key, value in {
        "SENTRYINSIGHT_ADMISSION_KEY": "run:9",
        "GITHUB_RUN_ID": "9",
        "GITHUB_RUN_ATTEMPT": "1",
        "GITHUB_SHA": "a" * 40,
        "SENTRYINSIGHT_SOURCE_REVISION": revision,
    }.items():
        monkeypatch.setenv(key, value)
    with pytest.raises(AttemptBudgetError):
        AdmissionAttemptBudget.from_environment()


def test_historical_budget_callers_keep_the_event_revision(monkeypatch):
    monkeypatch.delenv("SENTRYINSIGHT_SOURCE_REVISION", raising=False)
    for key, value in {
        "SENTRYINSIGHT_ADMISSION_KEY": "run:9",
        "GITHUB_RUN_ID": "9",
        "GITHUB_RUN_ATTEMPT": "1",
        "GITHUB_SHA": "a" * 40,
    }.items():
        monkeypatch.setenv(key, value)
    assert AdmissionAttemptBudget.from_environment().revision == "a" * 40


def test_real_bridge_and_client_retry_share_one_persisted_cap(budget_factory):
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(503, json={"error": {"code": 503}})

    kwargs = {
        "system_prompt": "synthetic",
        "user_prompt": "synthetic",
        "model": parse_model_selection(
            "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
        ),
    }

    def client():
        return OpenRouterClient(
            api_key="synthetic",
            attempt_budget=budget_factory(),
            transport=httpx.MockTransport(handler),
        )

    with pytest.raises(OpenRouterError):
        asyncio.run(client().generate(**kwargs))
    assert len(calls) == 3
    with pytest.raises(AttemptBudgetError):
        asyncio.run(client().generate(**kwargs))
    assert len(calls) == 3


def test_real_bridge_allows_one_output_limit_recovery_and_holds_on_second_limit(
    budget_factory,
):
    model = parse_model_selection("openrouter/nvidia/nemotron-3-ultra-550b-a55b:free")
    kwargs = {
        "system_prompt": "synthetic",
        "user_prompt": "synthetic",
        "model": model,
    }
    length_response = httpx.Response(
        200,
        json={
            "model": model.model_id,
            "choices": [{"finish_reason": "length", "message": {"content": "partial"}}],
            "usage": {
                "prompt_tokens": 70000,
                "completion_tokens": 96000,
                "reasoning_tokens": 82000,
            },
        },
    )
    complete_response = httpx.Response(
        200,
        json={
            "model": model.model_id,
            "choices": [{"finish_reason": "stop", "message": {"content": "complete"}}],
        },
    )
    recovered_calls = []

    def recover_handler(request):
        recovered_calls.append(json.loads(request.content))
        return length_response if len(recovered_calls) == 1 else complete_response

    client = OpenRouterClient(
        api_key="synthetic",
        max_tokens=96000,
        recovery_max_tokens=131072,
        attempt_budget=budget_factory(),
        transport=httpx.MockTransport(recover_handler),
    )
    assert asyncio.run(client.generate(**kwargs)) == "complete"
    assert len(recovered_calls) == 2
    assert recovered_calls[0]["max_tokens"] == 96000
    assert recovered_calls[1]["max_tokens"] == 131072
    assert "reasoning" not in recovered_calls[0]
    assert "reasoning" not in recovered_calls[1]

    # Once completed, the durable budget prevents another send in the same episode.
    with pytest.raises(AttemptBudgetError):
        asyncio.run(client.generate(**kwargs))


def test_real_bridge_blocks_third_attempt_after_two_output_limits(budget_factory):
    from src.core.openrouter_client import OpenRouterOutputLimitExceeded

    model = parse_model_selection("openrouter/nvidia/nemotron-3-ultra-550b-a55b:free")
    kwargs = {
        "system_prompt": "synthetic",
        "user_prompt": "synthetic",
        "model": model,
    }
    calls = []

    def always_length(request):
        calls.append(json.loads(request.content))
        return httpx.Response(
            200,
            json={
                "model": model.model_id,
                "choices": [
                    {"finish_reason": "length", "message": {"content": "partial"}}
                ],
            },
        )

    client = OpenRouterClient(
        api_key="synthetic",
        max_tokens=96000,
        recovery_max_tokens=131072,
        attempt_budget=budget_factory(),
        transport=httpx.MockTransport(always_length),
    )
    with pytest.raises(OpenRouterOutputLimitExceeded) as raised:
        asyncio.run(client.generate(**kwargs))
    assert len(calls) == 2
    assert raised.value.attempts == 2
    with pytest.raises(AttemptBudgetError):
        asyncio.run(client.generate(**kwargs))
    assert len(calls) == 2


@pytest.fixture
def guarded_bridge(budget_factory, tmp_path, monkeypatch):
    """Real Node CLI/CAS, with ownership checks forced only on its initial Git probe."""
    budget = budget_factory()
    real_git = shutil.which("git")
    node = shutil.which("node")
    assert real_git and node
    shim_dir = tmp_path / "bin"
    shim_dir.mkdir()
    captured = tmp_path / "child-environments.jsonl"
    shim = shim_dir / "git"
    # Use the same standalone Node runtime as the production CLI. A Python
    # shebang can need setup-python's LD_LIBRARY_PATH, which the bridge excludes.
    shim.write_text(
        f"#!{node}\n"
        "const fs = require('node:fs');\n"
        "const { spawnSync } = require('node:child_process');\n"
        f"fs.appendFileSync({json.dumps(str(captured))}, "
        "JSON.stringify(process.env) + '\\n');\n"
        "if (process.argv[2] === 'rev-parse') {\n"
        "  process.env.GIT_TEST_ASSUME_DIFFERENT_OWNER = '1';\n"
        "}\n"
        f"const result = spawnSync({json.dumps(real_git)}, process.argv.slice(2), "
        "{ env: process.env, stdio: 'inherit' });\n"
        "if (result.error) console.error(result.error.message);\n"
        "process.exit(result.status ?? 1);\n"
    )
    shim.chmod(0o700)
    home = tmp_path / "isolated-home"
    home.mkdir()
    monkeypatch.setenv("HOME", str(home))
    monkeypatch.setenv("PATH", f"{shim_dir}{os.pathsep}{os.environ['PATH']}")
    for key in tuple(os.environ):
        if key.startswith("GIT_"):
            monkeypatch.delenv(key)
    return budget, captured, real_git


def test_container_bridge_preserves_only_exact_workspace_trust(
    guarded_bridge, monkeypatch, tmp_path
):
    budget, captured, real_git = guarded_bridge
    # Without the workflow's exception the real CLI fails before reserving.
    with pytest.raises(AttemptBudgetError):
        asyncio.run(budget.reserve("b" * 64, 3))
    monkeypatch.setenv("GIT_CONFIG_COUNT", "1")
    monkeypatch.setenv("GIT_CONFIG_KEY_0", "safe.directory")
    monkeypatch.setenv("GIT_CONFIG_VALUE_0", str(budget.root.resolve()))
    excluded = {
        "OPENROUTER_API_KEY": "synthetic-inference-secret",
        "LOGFIRE_TOKEN": "synthetic-tracing-secret",
        "OTEL_EXPORTER_OTLP_HEADERS": "authorization=synthetic",
        "GIT_CONFIG_KEY_1": "http.extraHeader",
        "GIT_CONFIG_VALUE_1": "authorization=synthetic-git-secret",
        "GIT_CONFIG_PARAMETERS": "synthetic-arbitrary-git-config",
        "GIT_DIR": "/synthetic-unrelated-repository",
        "GIT_TRACE": "synthetic-trace-destination",
        "LD_LIBRARY_PATH": "/synthetic-loader-path-not-forwarded",
    }
    for key, value in excluded.items():
        monkeypatch.setenv(key, value)
    reservation = asyncio.run(budget.reserve("b" * 64, 3))
    assert reservation["attempt"] == 1  # The rejected Git probe spent no budget.
    asyncio.run(budget.finish(reservation, "uncertain"))
    with pytest.raises(AttemptBudgetError):
        asyncio.run(budget.reserve("b" * 64, 3))
    environments = [json.loads(line) for line in captured.read_text().splitlines()]
    trusted = [env for env in environments if "GIT_CONFIG_COUNT" in env]
    assert trusted
    for env in trusted:
        assert env["GIT_CONFIG_COUNT"] == "1"
        assert env["GIT_CONFIG_KEY_0"] == "safe.directory"
        assert env["GIT_CONFIG_VALUE_0"] == str(budget.root.resolve())
        assert not excluded.keys() & env.keys()
        assert "GIT_TEST_ASSUME_DIFFERENT_OWNER" not in env
    # The same inherited child environment cannot trust a different repository.
    unrelated = tmp_path / "unrelated"
    unrelated.mkdir()
    subprocess.run([real_git, "init", "-q"], cwd=unrelated, env=trusted[0], check=True)
    result = subprocess.run(
        [real_git, "rev-parse", "HEAD"],
        cwd=unrelated,
        env={**trusted[0], "GIT_TEST_ASSUME_DIFFERENT_OWNER": "1"},
        capture_output=True,
        text=True,
    )
    assert result.returncode == 128
    assert "dubious ownership" in result.stderr


@pytest.mark.parametrize(
    "count,key,value",
    [
        ("2", "safe.directory", "root"),
        ("1", "include.path", "root"),
        ("1", "safe.directory", "*"),
        ("1", "safe.directory", "unrelated"),
        ("1", "safe.directory", "."),
    ],
)
def test_container_bridge_rejects_unbounded_or_unrelated_git_trust(
    guarded_bridge, monkeypatch, count, key, value
):
    budget, captured, _ = guarded_bridge
    monkeypatch.setenv("GIT_CONFIG_COUNT", count)
    monkeypatch.setenv("GIT_CONFIG_KEY_0", key)
    monkeypatch.setenv(
        "GIT_CONFIG_VALUE_0", str(budget.root.resolve()) if value == "root" else value
    )
    with pytest.raises(AttemptBudgetError):
        asyncio.run(budget.reserve("c" * 64, 3))
    environments = [json.loads(line) for line in captured.read_text().splitlines()]
    assert environments
    assert all(not any(key.startswith("GIT_") for key in env) for env in environments)
