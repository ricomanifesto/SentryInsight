"""Exercise the Python -> Node -> local Git CAS boundary without a network remote."""

import asyncio
import json
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
