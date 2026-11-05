"""One mock physical request, original CAS token and actual host reply replay."""

import asyncio
from datetime import datetime, timezone
import os
from pathlib import Path
import pytest
from scripts.rehearse_full_feed_canary import rehearse


class ExecutionClock(datetime):
    @classmethod
    def now(cls, tz=None):
        value = cls(2026, 11, 6, 3, 4, 5, tzinfo=timezone.utc)
        return value if tz is not None else value.replace(tzinfo=None)


@pytest.fixture(autouse=True)
def synthetic_execution_clock(monkeypatch):
    from scripts import rehearse_full_feed_canary as bridge
    from src.core import reviewed_report

    monkeypatch.setattr(bridge, "datetime", ExecutionClock)
    monkeypatch.setattr(reviewed_report, "datetime", ExecutionClock)


def feed_bytes():
    path = os.environ.get("SENTRY_FROZEN_FEED")
    if not path:
        pytest.skip("Exact external public packet required")
    return Path(path).read_bytes()


def test_whole_feed_same_reply_reaches_actual_host_and_scratch_package(tmp_path):
    result = asyncio.run(rehearse(feed_bytes(), tmp_path))
    assert result["mock_physical_posts"] == 1
    assert result["host_replay_requests"] == 1
    assert result["physical_limit"] == 1
    assert result["whole_hold_microusd"] == 7251456
    assert result["original_token_shared"] is True
    assert result["host_validated"] is True, result["host_diagnostic"]
    assert result["scratch_promoted"] is True
    assert result["coverage_counts"]["input_sources"] == 30
    assert result["coverage_counts"]["eligible_sources"] == 25
    assert result["coverage_counts"]["review_required_sources"] == 5
    assert result["published"] is False
    assert result["financial_settled"] is False
    assert result["pages_package"]["matches_promoted_artifacts"] is True
    assert result["generated_at"] == "2026-11-06T03:04:05+00:00"
    assert result["generated_at"] != "2026-11-06T12:00:00+00:00"


@pytest.mark.parametrize(
    "scenario,replay_count",
    [
        ("invalid_grounding", 1),
        ("missing_cost", 0),
        ("empty", 0),
        ("transport_unknown", 0),
    ],
)
def test_failure_preserves_last_good_and_never_issues_another_token(
    tmp_path, scenario, replay_count
):
    result = asyncio.run(rehearse(feed_bytes(), tmp_path, scenario=scenario))
    assert result["mock_physical_posts"] == 1
    assert result["host_replay_requests"] == replay_count
    assert result["host_validated"] is False
    assert result["last_good_preserved"] is True
    assert result["second_token_blocked"] is True
    assert result["original_token_shared"] is True
    assert result["financial_outcome"] == "uncertain"
    assert result["financial_settled"] is False
    assert result["published"] is False


def test_stale_manifest_stops_before_a_grant_or_send(tmp_path):
    from datetime import datetime, timezone

    with pytest.raises(ValueError, match="Closed canary refused"):
        asyncio.run(
            rehearse(
                feed_bytes(), tmp_path, now=datetime(2026, 11, 7, tzinfo=timezone.utc)
            )
        )
    assert not (tmp_path / "financial").exists()


def test_expired_wall_clock_without_an_override_stops_before_grant(
    tmp_path, monkeypatch
):
    from scripts import rehearse_full_feed_canary as bridge

    class ExpiredClock(datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(2026, 11, 7, tzinfo=timezone.utc)

    monkeypatch.setattr(bridge, "datetime", ExpiredClock)
    with pytest.raises(ValueError, match="Closed canary refused"):
        asyncio.run(rehearse(feed_bytes(), tmp_path))
    assert not (tmp_path / "financial").exists()


def test_child_environment_never_inherits_credentials_or_startup_controls(monkeypatch):
    from scripts.rehearse_full_feed_canary import environment

    for name in (
        "OPENROUTER_API_KEY",
        "AWS_SECRET_ACCESS_KEY",
        "PYTHONPATH",
        "PYTHONHOME",
        "NODE_OPTIONS",
        "GIT_CONFIG_COUNT",
        "HTTPS_PROXY",
    ):
        monkeypatch.setenv(name, "hostile-private-sentinel")
    result = environment()
    assert not set(result) & {
        "HOME",
        "OPENROUTER_API_KEY",
        "AWS_SECRET_ACCESS_KEY",
        "PYTHONPATH",
        "PYTHONHOME",
        "NODE_OPTIONS",
        "GIT_CONFIG_COUNT",
        "HTTPS_PROXY",
    }
    assert "hostile-private-sentinel" not in str(result)
