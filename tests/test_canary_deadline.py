"""Conservative runtime budget; synthetic public metadata and clocks only."""

from datetime import datetime, timezone
import copy
import pytest
from scripts.canary_deadline import DeadlineBudget, anchor_run

NOW = datetime(2026, 11, 5, 12, tzinfo=timezone.utc)
CONTEXT = {
    "GITHUB_ACTIONS": "true",
    "GITHUB_REPOSITORY": "ricomanifesto/SentryInsight",
    "GITHUB_ACTOR": "ricomanifesto",
    "GITHUB_EVENT_NAME": "workflow_dispatch",
    "GITHUB_REF": "refs/heads/canary/sentry-full-feed-20261105",
    "GITHUB_SHA": "a" * 40,
    "GITHUB_RUN_ID": "100",
    "GITHUB_RUN_ATTEMPT": "1",
}
META = {
    "id": 100,
    "repository": {"full_name": CONTEXT["GITHUB_REPOSITORY"]},
    "actor": {"login": "ricomanifesto"},
    "event": "workflow_dispatch",
    "head_sha": "a" * 40,
    "head_branch": "canary/sentry-full-feed-20261105",
    "workflow_id": 406270829,
    "run_attempt": 1,
    "status": "in_progress",
    "created_at": "2026-11-05T12:00:00Z",
}


def budget(**changes):
    return anchor_run(
        META, CONTEXT, "2026-11-05", now=changes.get("now", NOW), mono_ns=0
    )


def test_one_origin_survives_serialization_and_cannot_be_reanchored():
    value = budget()
    restored = DeadlineBudget.restore(value.record(), CONTEXT, "2026-11-05")
    assert restored.record() == value.record()
    assert restored.remaining(120_000_000_000) == 2280
    forged = value.record()
    forged["job_deadline_ns"] += 1
    with pytest.raises(ValueError):
        DeadlineBudget.restore(forged, CONTEXT, "2026-11-05")


@pytest.mark.parametrize("offset,allowed", [(100, True), (101, False)])
def test_gate_before_money_reservation(offset, allowed):
    if allowed:
        budget().before_reserve(now=NOW, mono_ns=offset * 10**9)
    else:
        with pytest.raises(ValueError):
            budget().before_reserve(now=NOW, mono_ns=offset * 10**9)


@pytest.mark.parametrize("offset,allowed", [(120, True), (121, False)])
def test_post_ack_gate_before_key_and_send(offset, allowed):
    if allowed:
        budget().before_send(now=NOW, mono_ns=offset * 10**9)
    else:
        with pytest.raises(ValueError):
            budget().before_send(now=NOW, mono_ns=offset * 10**9)


@pytest.mark.parametrize(
    "field,value",
    [
        ("id", 101),
        ("head_sha", "b" * 40),
        ("workflow_id", 1),
        ("event", "push"),
        ("run_attempt", 2),
        ("created_at", "2026-11-05T12:00:01Z"),
        ("status", "completed"),
        ("head_branch", "main"),
    ],
)
def test_context_forgery_or_future_time_refuses(field, value):
    meta = copy.deepcopy(META)
    meta[field] = value
    with pytest.raises(ValueError):
        anchor_run(meta, CONTEXT, "2026-11-05", now=NOW, mono_ns=0)


def test_queue_consumes_budget_and_utc_day_is_a_second_limit():
    with pytest.raises(ValueError):
        budget(now=NOW.replace(minute=2)).before_reserve(now=NOW, mono_ns=0)
    meta = {**META, "created_at": "2026-11-05T23:30:00Z"}
    late = anchor_run(
        meta, CONTEXT, "2026-11-05", now=NOW.replace(hour=23, minute=30), mono_ns=0
    )
    with pytest.raises(ValueError):
        late.before_send(now=NOW.replace(hour=23, minute=30), mono_ns=0)


def test_sampling_pause_cannot_extend_deadline(monkeypatch):
    from scripts import canary_deadline as clock

    elapsed = [0]

    class PausedClock(datetime):
        @classmethod
        def now(cls, _tz=None):
            elapsed[0] = 10 * 10**9
            return cls(2026, 11, 5, 12, 0, 10, tzinfo=timezone.utc)

    monkeypatch.setattr(clock.time, "monotonic_ns", lambda: elapsed[0])
    monkeypatch.setattr(clock, "datetime", PausedClock)
    value = clock.anchor_run(META, CONTEXT, "2026-11-05")
    assert value.anchor_monotonic_ns == 0
    assert value.remaining() <= 2390


def test_clock_file_refuses_fifo_symlink_duplicate_and_foreign_mode(tmp_path):
    import json
    import os
    import subprocess
    import sys
    from scripts.canary_deadline import load_clock, save_clock

    path = tmp_path / "clock"
    os.mkfifo(path, 0o600)
    # A real isolated process proves open itself cannot block on the FIFO.
    probe = "import sys;sys.path.insert(0,sys.argv[1]);from scripts.canary_deadline import load_clock;load_clock(sys.argv[2],{},'2026-11-05')"
    result = subprocess.run(
        [
            sys.executable,
            "-I",
            "-B",
            "-c",
            probe,
            str(__import__("pathlib").Path.cwd()),
            str(path),
        ],
        capture_output=True,
        timeout=1,
    )
    assert result.returncode != 0
    path.unlink()
    save_clock(path, budget())
    assert load_clock(path, CONTEXT, "2026-11-05").record() == budget().record()
    path.chmod(0o644)
    with pytest.raises(ValueError):
        load_clock(path, CONTEXT, "2026-11-05")

    path.chmod(0o600)
    raw = json.dumps(budget().record())
    path.write_text(raw[:-1] + ', "schema_version":1}')
    with pytest.raises(ValueError):
        load_clock(path, CONTEXT, "2026-11-05")
    link = tmp_path / "link"
    link.symlink_to(path)
    with pytest.raises(OSError):
        load_clock(link, CONTEXT, "2026-11-05")


def test_delayed_timeout_construction_cannot_start_expired_work(monkeypatch):
    import asyncio
    import time
    from scripts import canary_deadline as clock

    original = asyncio.timeout_at

    def delayed(absolute):
        time.sleep(0.04)
        return original(absolute)

    monkeypatch.setattr(clock.asyncio, "timeout_at", delayed)
    reached = []

    async def run():
        phase = clock.PhaseDeadline(time.monotonic_ns() + 20_000_000)
        with pytest.raises(ValueError):
            async with phase.timeout():
                reached.append(True)

    asyncio.run(run())
    assert reached == []


def test_same_day_forward_clock_shift_cannot_spend_the_old_day_allowance():
    value = budget()
    with pytest.raises(ValueError):
        value.before_send(now=NOW.replace(hour=23, minute=59), mono_ns=0)
