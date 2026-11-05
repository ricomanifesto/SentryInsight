"""Owned preemptible children, bounded private pipes, fixed failure evidence."""

import asyncio
import os
import signal
import time

from scripts.canary_deadline import PhaseDeadline


class ProcessFailure(ValueError):
    def __init__(self, code):
        if code not in {
            "worker_deadline",
            "worker_protocol",
            "worker_failed",
            "worker_cleanup",
        }:
            code = "worker_failed"
        super().__init__("Closed canary worker refused")
        self.code = code


async def stop(process):
    """Kill only the group created by this owner, including its Git children."""
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    async with PhaseDeadline(time.monotonic_ns() + 2_000_000_000).timeout():
        await process.wait()


async def spawn(argv, *, env, cwd):
    task = asyncio.create_task(
        asyncio.create_subprocess_exec(
            *argv,
            cwd=cwd,
            env=env,
            start_new_session=True,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.DEVNULL,
        )
    )
    try:
        return await asyncio.shield(task)
    except BaseException:
        # Do not lose a process whose creation completed concurrently with
        # cancellation. The subprocess API owns cleanup until it returns one.
        try:
            process = await asyncio.wait_for(asyncio.shield(task), 2)
            await stop(process)
        except BaseException:
            task.cancel()
        raise


async def run_private(argv, value, deadline: PhaseDeadline, *, env, cwd, limit):
    """A single fixed child execution; neither timeout nor cleanup retries it."""
    process = None
    primary = None
    raw = bytearray()
    try:
        async with deadline.timeout():
            process = await spawn(argv, env=env, cwd=cwd)
            if process.stdin is None or process.stdout is None:
                raise ProcessFailure("worker_protocol")

            async def write():
                process.stdin.write(value)
                await process.stdin.drain()
                process.stdin.close()
                await process.stdin.wait_closed()

            async def read():
                while chunk := await process.stdout.read(65536):
                    if len(raw) + len(chunk) > limit:
                        raise ProcessFailure("worker_protocol")
                    raw.extend(chunk)

            async with asyncio.TaskGroup() as group:
                group.create_task(write())
                group.create_task(read())
            if await process.wait() != 0:
                raise ProcessFailure("worker_failed")
    except BaseException as error:
        primary = error
    finally:
        if process is not None:
            try:
                await stop(process)
            except BaseException:
                if primary is None:
                    primary = ProcessFailure("worker_cleanup")
    if primary is not None:
        if isinstance(primary, asyncio.CancelledError):
            raise primary
        if isinstance(primary, ProcessFailure):
            raise primary from None
        if isinstance(primary, TimeoutError):
            raise ProcessFailure("worker_deadline") from None
        if isinstance(primary, BaseExceptionGroup):
            if any(
                isinstance(item, ProcessFailure) and item.code == "worker_protocol"
                for item in primary.exceptions
            ):
                raise ProcessFailure("worker_protocol") from None
        raise ProcessFailure("worker_failed") from None
    return bytes(raw)
