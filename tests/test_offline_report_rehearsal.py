"""Run the real graph in a fresh process, independent of legacy module stubs."""

import asyncio
import json
import os
from pathlib import Path
import socket
import subprocess
import sys

import httpx
import pytest

from scripts.rehearse_report_offline import (
    CACHE_FILE,
    ROOT,
    SCENARIOS,
    offline_environment,
)


@pytest.fixture
def tokenizer_cache():
    cache = os.environ.get("TIKTOKEN_CACHE_DIR")
    if not cache or not (Path(cache) / CACHE_FILE).is_file():
        pytest.fail("Set TIKTOKEN_CACHE_DIR to an existing verified tokenizer cache")
    return Path(cache)


def run_cli(cache, *arguments):
    return subprocess.run(
        [
            sys.executable,
            "-B",
            str(ROOT / "scripts/rehearse_report_offline.py"),
            "--offline-only",
            "--tokenizer-cache",
            str(cache),
            *arguments,
        ],
        cwd=ROOT,
        env={
            "PATH": os.environ.get("PATH", os.defpath),
            "OPENROUTER_API_KEY": "inherited-secret-must-not-be-used",
            "LOGFIRE_TOKEN": "inherited-secret-must-not-be-used",
            "SENTRYINSIGHT_MODEL": "unapproved/model",
        },
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=120,
    )


@pytest.fixture(scope="module")
def rehearsal():
    cache = os.environ.get("TIKTOKEN_CACHE_DIR")
    if not cache:
        pytest.fail("Set TIKTOKEN_CACHE_DIR to an existing verified tokenizer cache")
    completed = run_cli(Path(cache))
    assert completed.returncode == 0, completed.stderr
    assert completed.stderr == ""
    assert len(completed.stdout.encode()) < 24576
    return completed.stdout, json.loads(completed.stdout)


def test_real_graph_renders_partial_coverage_and_preserves_tracked_artifacts(rehearsal):
    raw, receipt = rehearsal
    assert set(receipt) == {
        "schema_version",
        "code_commit",
        "rehearsal_source_sha256",
        "fixture_sha256",
        "outcome",
        "offline_only",
        "published",
        "live_requests",
        "provider_boundary",
        "admission_boundary",
        "telemetry_configured",
        "production_ready",
        "tracked_public_artifacts_unchanged",
        "tracked_public_artifact_count",
        "tracked_public_tree_sha256",
        "scenarios",
        "github_permissions_verified",
    }
    assert receipt["outcome"] == "offline_rehearsal_passed"
    assert receipt["tracked_public_artifacts_unchanged"] is True
    assert receipt["tracked_public_artifact_count"] > 50
    assert receipt["published"] is receipt["production_ready"] is False
    assert receipt["github_permissions_verified"] is False
    assert receipt["live_requests"] == 0
    scenarios = {row["scenario"]: row for row in receipt["scenarios"]}
    scenario_fields = {
        "scenario",
        "status",
        "stages",
        "mock_requests",
        "request_limit",
        "request_sha256",
        "input_tokens_cl100k_including_256_reserve",
        "requested_model",
        "resolved_model",
        "finish_reason",
        "request",
        "diagnostic",
        "retry",
        "durable_history",
        "restart_blocked",
        "report_generated",
        "coverage_counts",
        "pages_package",
        "scratch_artifact_count",
        "scratch_tree_sha256",
        "last_good_preserved",
    }
    assert all(set(row) == scenario_fields for row in scenarios.values())
    assert tuple(scenarios) == SCENARIOS
    valid = scenarios["partial_success"]
    assert valid["stages"] == [
        "fetch_articles",
        "enrich_articles",
        "filter_articles",
        "analyze_articles",
        "generate_report",
        "publish_results",
    ]
    assert valid["status"] == "completed_with_review"
    assert valid["scratch_artifact_count"] == 11
    assert valid["pages_package"]["matches_promoted_artifacts"] is True
    assert valid["pages_package"]["artifact_count"] > valid["scratch_artifact_count"]
    assert valid["input_tokens_cl100k_including_256_reserve"] == 2948
    assert valid["coverage_counts"] == {
        "input_sources": 2,
        "eligible_sources": 1,
        "cited_sources": 1,
        "review_required_sources": 1,
        "rejected_sources": 0,
        "unrepresented_eligible_sources": 0,
    }
    assert scenarios["all_held"]["mock_requests"] == 0
    assert scenarios["all_held"]["stages"] == [
        "fetch_articles",
        "enrich_articles",
        "filter_articles",
    ]
    for row in scenarios.values():
        if row["scenario"] not in {"partial_success", "transient_then_success"}:
            assert row["last_good_preserved"] is True
    for marker in (
        "inherited-secret",
        "offline-synthetic-key",
        "Authorization",
        "Executive Summary",
        "Customers should",
        "example.test",
        "/tmp/",
        "source-1c0c9e871590",
        "calibration_response",
    ):
        assert marker not in raw


def test_actual_cli_budget_caps_retries_and_holds_restarted_graphs(rehearsal):
    scenarios = {row["scenario"]: row for row in rehearsal[1]["scenarios"]}
    success = scenarios["transient_then_success"]
    assert success["mock_requests"] == 2
    assert success["durable_history"] == {
        "reserved": 2,
        "finished": 2,
        "dispositions": ["retryable_rejection", "response_received"],
    }
    cap = scenarios["transient_cap"]
    assert cap["mock_requests"] == cap["request_limit"] == 3
    assert cap["durable_history"]["reserved"] == 3
    assert cap["restart_blocked"] is True
    uncertain = scenarios["uncertain_transport"]
    assert uncertain["durable_history"] == {
        "reserved": 1,
        "finished": 1,
        "dispositions": ["uncertain"],
    }
    assert uncertain["restart_blocked"] is True
    lost = scenarios["lost_completion_ack"]
    assert lost["request"]["state"] == "uncertain"
    assert lost["durable_history"]["dispositions"] == ["response_received"]
    assert lost["restart_blocked"] is True


def test_real_validators_and_output_limit_refuse_promotion(rehearsal):
    scenarios = {row["scenario"]: row for row in rehearsal[1]["scenarios"]}
    evidence = scenarios["unsupported_evidence"]["diagnostic"]
    assert evidence["stage"] == "finding_evidence"
    assert evidence["codes"] == ["exception_not_grounded"]
    version = scenarios["invalid_version_reference"]["diagnostic"]
    assert version["stage"] == "version_references"
    assert version["codes"] == ["unsupported_version_reference"]
    truncated = scenarios["output_truncated"]
    assert truncated["finish_reason"] == "length"
    assert truncated["request"]["state"] == "permanent_rejection"
    assert "model_output_limit_exceeded" in truncated["diagnostic"]["codes"]
    assert truncated["report_generated"] is False


def test_resolved_model_mismatch_keeps_last_good_and_does_not_replay(rehearsal):
    scenarios = {row["scenario"]: row for row in rehearsal[1]["scenarios"]}
    mismatch = scenarios["model_identity_mismatch"]
    assert mismatch["mock_requests"] == 1 and mismatch["restart_blocked"] is True
    assert mismatch["finish_reason"] == "stop" and mismatch["resolved_model"] is None
    assert mismatch["request"]["state"] == "permanent_rejection"
    assert "model_identity_mismatch" in mismatch["diagnostic"]["codes"]
    assert mismatch["last_good_preserved"] is True
    assert mismatch["report_generated"] is False


def test_environment_denies_network_and_removes_credentials(tmp_path, tokenizer_cache):
    original_home = os.environ.get("HOME")
    with offline_environment(tmp_path, tokenizer_cache):
        assert os.environ.get("OPENROUTER_API_KEY") is None
        assert os.environ.get("LOGFIRE_TOKEN") is None
        assert os.environ["HOME"] != original_home
        with pytest.raises(RuntimeError, match="forbids network"):
            socket.create_connection(("example.invalid", 443))
        with pytest.raises(RuntimeError, match="forbids network"):
            httpx.get("https://example.invalid")

        async def request():
            async with httpx.AsyncClient() as client:
                await client.get("https://example.invalid")

        with pytest.raises(RuntimeError, match="forbids network"):
            asyncio.run(request())
        for javascript in (
            "fetch('https://example.invalid')",
            "require('node:net').connect(443, 'example.invalid')",
        ):
            denied = subprocess.run(
                ["node", "-e", javascript],
                capture_output=True,
                timeout=10,
            )
            assert denied.returncode != 0
            assert b"offline network denied" in denied.stderr
        denied = subprocess.run(
            ["git", "ls-remote", "https://example.invalid/repository"],
            capture_output=True,
            timeout=10,
        )
        assert denied.returncode != 0
        assert b"transport 'https' not allowed" in denied.stderr


def test_receipt_is_deterministic_and_cli_has_no_live_mode(rehearsal, tokenizer_cache):
    repeated = run_cli(tokenizer_cache)
    assert repeated.returncode == 0
    assert repeated.stdout == rehearsal[0]
    refused = run_cli(tokenizer_cache, "--live")
    assert refused.returncode == 2
    assert "unrecognized arguments: --live" in refused.stderr


def test_missing_cache_cannot_trigger_an_implicit_download(tmp_path):
    completed = run_cli(tmp_path)
    assert completed.returncode == 1
    assert completed.stdout == ""
    assert json.loads(completed.stderr) == {
        "offline_only": True,
        "outcome": "offline_rehearsal_failed",
        "published": False,
    }
    assert list(tmp_path.iterdir()) == []
