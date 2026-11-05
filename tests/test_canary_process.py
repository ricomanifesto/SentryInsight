"""Synthetic process ownership; no provider, Git remote or real credential."""

import asyncio
import json
import os
import sys
import time

import pytest

from scripts.canary_deadline import PhaseDeadline
from scripts.canary_process import ProcessFailure, run_private


def deadline(seconds=3):
    return PhaseDeadline(time.monotonic_ns() + int(seconds * 1_000_000_000))


def run(code, *, timeout=3, limit=8192, value=b"private-pipe-sentinel"):
    return asyncio.run(
        run_private(
            [sys.executable, "-I", "-B", "-c", code],
            value,
            deadline(timeout),
            env={"PATH": os.defpath},
            cwd="/tmp",
            limit=limit,
        )
    )


def test_private_input_never_enters_child_environment_or_argv():
    result = run(
        "import json,os,sys; v=sys.stdin.buffer.read(); "
        "print(json.dumps([len(v), sorted(os.environ), sys.argv]))"
    )
    length, names, argv = json.loads(result)
    assert length == len(b"private-pipe-sentinel")
    assert not any("KEY" in key or "PYTHON" in key for key in names)
    assert "private-pipe-sentinel" not in json.dumps(argv)


@pytest.mark.parametrize(
    "code,timeout,limit,expected",
    [
        ("import time; time.sleep(10)", 0.05, 8192, "worker_deadline"),
        ("print('x'*9000)", 3, 8192, "worker_protocol"),
        (
            "import sys; sys.stderr.write('private-pipe-sentinel'); sys.exit(7)",
            3,
            8192,
            "worker_failed",
        ),
    ],
)
def test_failure_is_bounded_fixed_and_child_is_reaped(
    code, timeout, limit, expected, capsys
):
    started = time.monotonic()
    with pytest.raises(ProcessFailure) as error:
        run(code, timeout=timeout, limit=limit)
    assert error.value.code == expected
    assert time.monotonic() - started < 4
    captured = capsys.readouterr()
    assert "private-pipe-sentinel" not in str(error.value) + captured.out + captured.err


def test_external_cancel_propagates_after_owned_child_cleanup():
    async def exercise():
        task = asyncio.create_task(
            run_private(
                [sys.executable, "-I", "-c", "import time; time.sleep(10)"],
                b"",
                deadline(),
                env={},
                cwd="/tmp",
                limit=100,
            )
        )
        await asyncio.sleep(0.05)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task

    asyncio.run(exercise())


def test_cancellation_at_spawn_return_does_not_orphan_process(monkeypatch):
    from scripts import canary_process as owner

    original = owner.asyncio.create_subprocess_exec
    created = []
    outer = []

    async def race(*args, **kwargs):
        process = await original(*args, **kwargs)
        created.append(process)
        asyncio.get_running_loop().call_soon(outer[0].cancel)
        return process

    monkeypatch.setattr(owner.asyncio, "create_subprocess_exec", race)

    async def exercise():
        task = asyncio.create_task(
            run_private(
                [sys.executable, "-I", "-c", "import time;time.sleep(10)"],
                b"",
                deadline(),
                env={},
                cwd="/tmp",
                limit=10,
            )
        )
        outer.append(task)
        with pytest.raises(asyncio.CancelledError):
            await task

    asyncio.run(exercise())
    assert len(created) == 1 and created[0].returncode is not None


def test_cleanup_failure_never_replaces_primary_protocol_failure(monkeypatch):
    from scripts import canary_process as owner

    original = owner.stop

    async def fail_after_reap(process):
        await original(process)
        raise RuntimeError("private-pipe-sentinel")

    monkeypatch.setattr(owner, "stop", fail_after_reap)
    with pytest.raises(ProcessFailure) as error:
        run("print('x'*9000)")
    assert error.value.code == "worker_protocol"
