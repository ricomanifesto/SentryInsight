"""Reserve before sending; the admission store owns durable request history."""

import asyncio
import json
import os
from pathlib import Path
import re
import subprocess
from typing import Protocol

from .retry_policy import DISPOSITIONS, MAX_ATTEMPTS


class AttemptBudgetError(RuntimeError):
    def __init__(self):
        super().__init__("Request budget unavailable or unresolved; no request sent")


class AttemptBudget(Protocol):
    async def reserve(self, request_sha256: str, limit: int) -> dict: ...

    async def finish(
        self, reservation: dict, disposition: str, *, retry_after: float = 0
    ) -> None: ...


def _matches(value, pattern):
    return type(value) is str and re.fullmatch(pattern, value) is not None


class MemoryAttemptBudget:
    """One local process only; independent processes need admission persistence."""

    def __init__(self):
        self.identity = None
        self.attempt = 0
        self.disposition = "not_sent"

    async def reserve(self, request_sha256: str, limit: int) -> dict:
        bound = (request_sha256, limit)
        valid = (
            _matches(request_sha256, r"[a-f0-9]{64}")
            and type(limit) is int
            and 1 <= limit <= MAX_ATTEMPTS
        )
        available = (
            (
                self.identity in (None, bound)
                and self.disposition in {"not_sent", "retryable_rejection"}
                and self.attempt < limit
            )
            if valid
            else False
        )
        if not available:
            raise AttemptBudgetError()
        # No await separates the checks from this reservation in a local loop.
        self.identity = bound
        self.attempt += 1
        self.disposition = "reserved"
        return dict(attempt=self.attempt, limit=limit, request_sha256=request_sha256)

    async def finish(
        self, reservation: dict, disposition: str, *, retry_after: float = 0
    ) -> None:
        if (
            type(reservation) is not dict
            or self.disposition != "reserved"
            or reservation.get("attempt") != self.attempt
            or (reservation.get("request_sha256"), reservation.get("limit"))
            != self.identity
            or type(disposition) is not str
            or disposition not in DISPOSITIONS
        ):
            raise AttemptBudgetError()
        self.disposition = disposition


class AdmissionAttemptBudget:
    """A single acknowledged CLI operation per reservation or completion."""

    def __init__(self, *, key: str, run_id: str, revision: str, run_attempt: str):
        if not (
            _matches(key, r"(?:run:[0-9]+|digest:[a-f0-9]{40})")
            and _matches(run_id, r"[0-9]{1,20}")
            and _matches(revision, r"[a-f0-9]{40}")
            and run_attempt == "1"
        ):
            raise AttemptBudgetError()
        self.key = key
        self.run_id = run_id
        self.revision = revision
        self.root = Path(__file__).resolve().parents[2]

    @classmethod
    def from_environment(cls):
        names = {
            "key": "SENTRYINSIGHT_ADMISSION_KEY",
            "run_id": "GITHUB_RUN_ID",
            "revision": "GITHUB_SHA",
            "run_attempt": "GITHUB_RUN_ATTEMPT",
        }
        return cls(**{name: os.environ.get(env, "") for name, env in names.items()})

    def _invoke(self, command: str, arguments: list[str]) -> dict:
        argv = [
            "node",
            "publication/cli.js",
            command,
            "--key",
            self.key,
            "--run-id",
            self.run_id,
            "--revision",
            self.revision,
            *arguments,
        ]
        # Existing checkout authentication remains available to git. Inference
        # and tracing credentials are intentionally absent from the child env.
        env = {
            k: os.environ[k]
            for k in ("PATH", "HOME", "TMPDIR", "SYSTEMROOT")
            if k in os.environ
        }
        try:
            completed = subprocess.run(
                argv,
                cwd=self.root,
                env=env,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                timeout=60,
                check=True,
            )
            if len(completed.stdout) > 4096:
                raise ValueError()
            payload = json.loads(completed.stdout)
            if type(payload) is not dict:
                raise ValueError()
            return payload
        except (OSError, ValueError, subprocess.SubprocessError):
            # A lost acknowledgement may follow a committed CAS. Never repeat
            # this command here, and never expose command/exception contents.
            raise AttemptBudgetError() from None

    async def reserve(self, request_sha256: str, limit: int) -> dict:
        reservation = await asyncio.to_thread(
            self._invoke,
            "request-reserve",
            ["--request-sha256", request_sha256, "--limit", str(limit)],
        )
        if not (
            set(reservation) == {"attempt", "limit", "request_sha256", "token"}
            and type(reservation["attempt"]) is int
            and 1 <= reservation["attempt"] <= limit
            and type(reservation["limit"]) is int
            and reservation["limit"] == limit
            and reservation["request_sha256"] == request_sha256
            and _matches(reservation["token"], r"[a-f0-9]{32}")
        ):
            raise AttemptBudgetError()
        return reservation

    async def finish(
        self, reservation: dict, disposition: str, *, retry_after: float = 0
    ) -> None:
        options = {
            "request-sha256": reservation["request_sha256"],
            "limit": reservation["limit"],
            "attempt": reservation["attempt"],
            "token": reservation["token"],
            "disposition": disposition,
            "retry-after": retry_after,
        }
        arguments = [
            part for key, value in options.items() for part in (f"--{key}", str(value))
        ]
        result = await asyncio.to_thread(self._invoke, "request-finish", arguments)
        if set(result) != {"recorded"} or result["recorded"] is not True:
            raise AttemptBudgetError()
