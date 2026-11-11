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
def budget_factory(tmp_path):
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
            "workflow_dispatch",
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


def test_real_bridge_reservation_survives_lost_client(budget_factory):
    first = asyncio.run(budget_factory().reserve("a" * 64, 3))
    assert first["attempt"] == 1
    with pytest.raises(AttemptBudgetError):
        asyncio.run(budget_factory().reserve("a" * 64, 3))
    asyncio.run(budget_factory().finish(first, "uncertain"))
    with pytest.raises(AttemptBudgetError):
        asyncio.run(budget_factory().reserve("a" * 64, 3))


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
