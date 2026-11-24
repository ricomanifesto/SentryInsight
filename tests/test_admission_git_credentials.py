"""The admission child gets only repository-scoped, short-lived Git auth."""

import base64
from pathlib import Path
import subprocess
from types import SimpleNamespace

import pytest

from src.core.attempt_budget import AdmissionAttemptBudget, AttemptBudgetError

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("trusted", [True, False])
def test_admission_reconstructs_only_its_scoped_git_credentials(monkeypatch, trusted):
    calls = []
    real_run = subprocess.run
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    monkeypatch.setenv("GITHUB_REPOSITORY", "fixture/report")
    monkeypatch.setenv("SENTRYINSIGHT_ADMISSION_GITHUB_TOKEN", "fixture-session-token")
    monkeypatch.setenv("GIT_CONFIG_COUNT", "1")
    monkeypatch.setenv("GIT_CONFIG_KEY_0", "safe.directory")
    monkeypatch.setenv("GIT_CONFIG_VALUE_0", str(ROOT) if trusted else "/other")
    monkeypatch.setenv("GIT_CONFIG_KEY_1", "unused-fixture-config")
    monkeypatch.setenv("GIT_CONFIG_VALUE_1", "unused-fixture-value")
    monkeypatch.setenv("OPENROUTER_API_KEY", "fixture-model-key")
    monkeypatch.setenv("PAT_GITHUB", "fixture-pat")

    def run(*args, **kwargs):
        calls.append(kwargs)
        return SimpleNamespace(stdout=b"{}")

    monkeypatch.setattr(subprocess, "run", run)
    budget = AdmissionAttemptBudget(
        key="run:7", run_id="7", revision="a" * 40, run_attempt="1"
    )
    if not trusted:
        with pytest.raises(AttemptBudgetError):
            budget._invoke("request-reserve", [])
        assert not calls
        return
    assert budget._invoke("request-reserve", []) == {}
    child = calls[0]["env"]
    assert child["GIT_CONFIG_COUNT"] == "2"
    assert child["GIT_CONFIG_KEY_0"] == "safe.directory"
    assert child["GIT_CONFIG_VALUE_0"] == str(ROOT)
    assert (
        child["GIT_CONFIG_KEY_1"]
        == "http.https://github.com/fixture/report.git.extraheader"
    )
    scheme, encoded = child["GIT_CONFIG_VALUE_1"].rsplit(" ", 1)
    assert scheme == "AUTHORIZATION: basic"
    assert base64.b64decode(encoded) == b"x-access-token:fixture-session-token"
    assert not {
        "OPENROUTER_API_KEY",
        "PAT_GITHUB",
        "SENTRYINSIGHT_ADMISSION_GITHUB_TOKEN",
    }.intersection(child)
    assert calls[0]["stderr"] == subprocess.DEVNULL
    matched = real_run(
        [
            "git",
            "config",
            "--get-urlmatch",
            "http.extraheader",
            "https://github.com/fixture/report.git",
        ],
        env=child,
        capture_output=True,
        text=True,
    )
    assert matched.returncode == 0
    assert matched.stdout.strip() == child["GIT_CONFIG_VALUE_1"]


def test_admission_auth_never_writes_git_configuration(monkeypatch):
    root = str(ROOT)
    for key, value in {
        "GITHUB_ACTIONS": "true",
        "GITHUB_REPOSITORY": "fixture/report",
        "SENTRYINSIGHT_ADMISSION_GITHUB_TOKEN": "fixture-session-token",
        "GIT_CONFIG_COUNT": "1",
        "GIT_CONFIG_KEY_0": "safe.directory",
        "GIT_CONFIG_VALUE_0": root,
    }.items():
        monkeypatch.setenv(key, value)
    calls = []

    def run(argv, **kwargs):
        calls.append((argv, kwargs))
        return SimpleNamespace(stdout=b"{}")

    monkeypatch.setattr(subprocess, "run", run)
    budget = AdmissionAttemptBudget(
        key="run:7", run_id="7", revision="a" * 40, run_attempt="1"
    )
    budget._invoke("request-finish", [])
    assert len(calls) == 1
    assert calls[0][0][:3] == ["node", "publication/cli.js", "request-finish"]
    assert "fixture-session-token" not in str(calls[0][0])
