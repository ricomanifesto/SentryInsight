"""Fixed clocks and actual private worker pipes; never a real transport."""

import asyncio
import base64
import time

import httpx
import pytest

from scripts import canary_deadline as clock
from scripts import execute_full_feed_canary as canary
from scripts.canary_deadline import PhaseDeadline
from test_full_feed_canary_execution import (
    exercise,
    prepared as prepared,
    synthetic_clock as synthetic_clock,
)


def test_post_ack_budget_loss_keeps_hold_without_key_or_post(
    prepared, tmp_path, monkeypatch
):
    real = time.monotonic_ns
    offset = [0]
    monkeypatch.setattr(clock.time, "monotonic_ns", lambda: real() + offset[0])
    events, result = asyncio.run(
        exercise(
            prepared,
            tmp_path,
            monkeypatch,
            after_begin=lambda: offset.__setitem__(0, 121 * 10**9),
        )
    )
    assert result["failure"] == "time_budget_refused"
    assert (
        result["request_entered"] is False
        and result["financial_state"] == "held_or_unknown"
    )
    assert events.count("begin") == events.count("finish") == 1
    assert "key" not in events and "post" not in events and "publish" not in events


def test_real_host_worker_replays_one_reply_with_original_token(
    prepared, tmp_path, monkeypatch
):
    events, result = asyncio.run(
        exercise(prepared, tmp_path, monkeypatch, custom_replayer=canary.owned_replay)
    )
    assert result["failure"] is None and result["host_validated"] is True
    assert result["financial_state"] == "settled"
    assert events.count("post") == events.count("begin") == events.count("finish") == 1
    assert result["report_commit"] is None


def test_real_prepare_worker_preserves_exact_request_bytes(prepared, tmp_path):
    from scripts.canary_host_worker import unpacked

    async def run():
        return unpacked(
            await canary.worker(
                {
                    "mode": "prepare",
                    "feed": base64.b64encode(prepared[0]).decode(),
                    "scratch": str(tmp_path / "capture"),
                },
                PhaseDeadline(time.monotonic_ns() + 20 * 10**9),
            )
        )

    value = asyncio.run(run())
    assert value.pack == prepared[1].pack and value.wire == prepared[1].wire
    assert value.metadata == prepared[1].metadata


@pytest.mark.parametrize("stage", ["headers", "body", "close"])
def test_whole_control_get_includes_headers_body_and_close(stage, monkeypatch):
    original = PhaseDeadline.timeout

    def short(self):
        return original(self.capped(0.03))

    monkeypatch.setattr(PhaseDeadline, "timeout", short)

    class Stream(httpx.AsyncByteStream):
        async def __aiter__(self):
            if stage == "body":
                await asyncio.sleep(10)
            yield b"synthetic"

        async def aclose(self):
            if stage == "close":
                await asyncio.sleep(10)

    async def handle(_request):
        if stage == "headers":
            await asyncio.sleep(10)
        return httpx.Response(200, stream=Stream())

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as client:
            await canary.bounded_get(client, "https://example.invalid/fixed")

    with pytest.raises(TimeoutError):
        asyncio.run(run())


def test_worker_failure_and_receipt_io_never_echo_private_pipe(tmp_path, capsys):
    before = sorted(
        str(path.relative_to(tmp_path))
        for path in tmp_path.rglob("*")
        if path.is_file()
    )

    async def run():
        with pytest.raises(ValueError):
            await canary.worker(
                {
                    "mode": "emit",
                    "receipt": str(tmp_path),
                    "result": {"private": "private-pipe-sentinel"},
                },
                PhaseDeadline(time.monotonic_ns() + 3 * 10**9),
            )

    asyncio.run(run())
    captured = capsys.readouterr()
    assert "private-pipe-sentinel" not in captured.out + captured.err
    assert (
        sorted(
            str(path.relative_to(tmp_path))
            for path in tmp_path.rglob("*")
            if path.is_file()
        )
        == before
    )


def test_phase_objects_cannot_be_restarted_after_await_or_cleanup():
    from test_canary_deadline import budget

    value = budget()
    for name in ("receive", "post", "cleanup"):
        first = value.phase(name, mono_ns=100 * 10**9)
        assert value.phase(name, mono_ns=200 * 10**9) is first
    assert value.phase("post").deadline_ns <= (2400 - 80) * 10**9
    assert value.phase("cleanup").deadline_ns <= (2400 - 60) * 10**9


@pytest.mark.parametrize(
    "name,value", [("RUNNER_DEBUG", "1"), ("ACTIONS_STEP_DEBUG", "TRUE")]
)
def test_no_model_wrapper_refuses_debug_before_child_creation(monkeypatch, name, value):
    from argparse import Namespace
    from scripts import readmit_original_canary as operator

    calls = []

    async def forbidden(*_args, **_kwargs):
        calls.append(True)
        raise AssertionError("private-pipe-sentinel")

    monkeypatch.setattr(operator, "run_private", forbidden)
    monkeypatch.setenv(name, value)
    with pytest.raises(ValueError):
        asyncio.run(
            operator.run(
                Namespace(expected_commit="a" * 40, expected_readmission="b" * 64)
            )
        )
    assert calls == []
