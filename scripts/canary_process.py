"""Owned preemptible children, bounded private pipes, fixed failure evidence."""

import asyncio
import os
import signal

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


def kill_group(process):
    """Signalling has no await; even expiry cannot skip killing our own group."""
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    if process.stdin is not None:
        process.stdin.close()


async def stop(process, deadline):
    async with deadline.timeout():
        # Drain only private pipes after killing the group; discard all bytes.
        # Waiting on returncode alone can leave pipe transports unclosed.
        await process.communicate()
        await process.wait()


async def spawn(argv, *, env, cwd, deadline):
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
        process = None
        try:
            async with deadline.timeout():
                process = await asyncio.shield(task)
        except BaseException:
            if task.done() and not task.cancelled():
                try:
                    process = task.result()
                except BaseException:
                    pass
            else:
                # The subprocess API owns cleanup until it returns a Process.
                # If it returns concurrently with cancellation, synchronously
                # kill that owned group without another unreserved await.
                def kill_late(done):
                    try:
                        kill_group(done.result())
                    except BaseException:
                        pass

                task.add_done_callback(kill_late)
                task.cancel()
        if process is not None:
            kill_group(process)
            try:
                async with deadline.timeout():
                    await stop(process, deadline)
            except BaseException:
                pass
        raise


async def run_private(argv, value, deadline: PhaseDeadline, *, env, cwd, limit):
    """A single fixed child execution; neither timeout nor cleanup retries it."""
    process = None
    primary = None
    raw = bytearray()
    try:
        # Shutdown/reap belongs INSIDE the supplied phase, never a fresh tail.
        work = PhaseDeadline(deadline.deadline_ns - 2_000_000_000)
        async with work.timeout():
            process = await spawn(argv, env=env, cwd=cwd, deadline=deadline)
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
                kill_group(process)
                async with deadline.timeout():
                    await stop(process, deadline)
            except BaseException:
                if primary is None:
                    primary = ProcessFailure("worker_cleanup")
    if primary is not None:
        if isinstance(primary, asyncio.CancelledError):
            raise primary
        if isinstance(primary, ProcessFailure):
            raise primary from None
        from scripts.canary_deadline import BudgetError

        if isinstance(primary, (TimeoutError, BudgetError)):
            raise ProcessFailure("worker_deadline") from None
        if isinstance(primary, BaseExceptionGroup):
            if any(
                isinstance(item, ProcessFailure) and item.code == "worker_protocol"
                for item in primary.exceptions
            ):
                raise ProcessFailure("worker_protocol") from None
        raise ProcessFailure("worker_failed") from None
    return bytes(raw)
