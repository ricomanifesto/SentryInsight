"""Separate bounded repair-request budget backed by the admission CAS store.

Each informed repair request reserves its own repair slot (``repair_reserved`` /
``repair_finished``) bound to its own ``request_sha256`` and counted against
``MAX_REPAIR_REQUESTS_PER_RUN``. It never shares keys with or reopens the
original generation episode (``request_reserved`` / ``request_finished``).
"""

from __future__ import annotations

import asyncio
import base64
import json
import os
from pathlib import Path
import re
import subprocess
from typing import Protocol

from .attempt_budget import AttemptBudgetError
from .retry_policy import DISPOSITIONS

MAX_REPAIR_REQUESTS_PER_RUN = 6
MAX_REPAIR_ROUNDS_PER_FINDING = 3
MAX_FULL_REPORT_REPAIRS = 1


class RepairBudgetError(RuntimeError):
    def __init__(self, message: str = "Repair budget unavailable or exhausted"):
        super().__init__(message)


class RepairBudget(Protocol):
    @property
    def max_repairs(self) -> int: ...

    async def reserve(self, request_sha256: str) -> dict: ...

    async def finish(
        self, reservation: dict, disposition: str, *, retry_after: float = 0
    ) -> None: ...


def _matches(value: object, pattern: str) -> bool:
    return type(value) is str and re.fullmatch(pattern, value) is not None


class MemoryRepairBudget:
    """In-process bounded repair budget for local runs and offline tests."""

    def __init__(self, *, max_repairs: int = MAX_REPAIR_REQUESTS_PER_RUN):
        if (
            type(max_repairs) is not int
            or not 1 <= max_repairs <= MAX_REPAIR_REQUESTS_PER_RUN
        ):
            raise RepairBudgetError("Invalid repair budget limit")
        self._max_repairs = max_repairs
        self.slot = 0
        self.active: dict | None = None
        self.history: list[dict] = []

    @property
    def max_repairs(self) -> int:
        return self._max_repairs

    async def reserve(self, request_sha256: str) -> dict:
        if not _matches(request_sha256, r"[a-f0-9]{64}"):
            raise RepairBudgetError("Invalid repair request digest")
        if self.active is not None:
            raise RepairBudgetError("Previous repair slot is unresolved")
        if self.slot >= self._max_repairs:
            raise RepairBudgetError("Repair request cap reached")
        self.slot += 1
        reservation = {
            "slot": self.slot,
            "max_repairs": self._max_repairs,
            "request_sha256": request_sha256,
        }
        self.active = reservation
        return dict(reservation)

    async def finish(
        self, reservation: dict, disposition: str, *, retry_after: float = 0
    ) -> None:
        if (
            type(reservation) is not dict
            or self.active is None
            or reservation.get("slot") != self.active["slot"]
            or reservation.get("request_sha256") != self.active["request_sha256"]
            or reservation.get("max_repairs") != self._max_repairs
            or type(disposition) is not str
            or disposition not in DISPOSITIONS
        ):
            raise RepairBudgetError("Invalid repair slot completion")
        self.history.append(
            {
                **self.active,
                "disposition": disposition,
                "retry_after": retry_after,
            }
        )
        self.active = None


class AdmissionRepairBudget:
    """Durable CAS-backed repair budget sharing the publication-admission store."""

    def __init__(
        self,
        *,
        key: str,
        run_id: str,
        revision: str,
        run_attempt: str,
        max_repairs: int = MAX_REPAIR_REQUESTS_PER_RUN,
    ):
        if not (
            _matches(key, r"(?:run:[0-9]+|digest:[a-f0-9]{40})")
            and _matches(run_id, r"[0-9]{1,20}")
            and _matches(revision, r"[a-f0-9]{40}")
            and run_attempt == "1"
            and type(max_repairs) is int
            and 1 <= max_repairs <= MAX_REPAIR_REQUESTS_PER_RUN
        ):
            raise RepairBudgetError("Invalid admission repair budget identity")
        self.key = key
        self.run_id = run_id
        self.revision = revision
        self._max_repairs = max_repairs
        self.root = Path(__file__).resolve().parents[2]

    @property
    def max_repairs(self) -> int:
        return self._max_repairs

    @classmethod
    def from_environment(
        cls, *, max_repairs: int = MAX_REPAIR_REQUESTS_PER_RUN
    ) -> AdmissionRepairBudget:
        names = {
            "key": "SENTRYINSIGHT_ADMISSION_KEY",
            "run_id": "GITHUB_RUN_ID",
            "revision": "GITHUB_SHA",
            "run_attempt": "GITHUB_RUN_ATTEMPT",
        }
        values = {name: os.environ.get(env, "") for name, env in names.items()}
        values["revision"] = os.environ.get(
            "SENTRYINSIGHT_SOURCE_REVISION", values["revision"]
        )
        return cls(
            key=values["key"],
            run_id=values["run_id"],
            revision=values["revision"],
            run_attempt=values["run_attempt"],
            max_repairs=max_repairs,
        )

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
        env = {
            k: os.environ[k]
            for k in ("PATH", "HOME", "TMPDIR", "SYSTEMROOT")
            if k in os.environ
        }
        root = str(self.root.resolve())
        if (
            os.environ.get("GIT_CONFIG_COUNT") == "1"
            and os.environ.get("GIT_CONFIG_KEY_0") == "safe.directory"
            and os.environ.get("GIT_CONFIG_VALUE_0") == root
        ):
            env.update(
                GIT_CONFIG_COUNT="1",
                GIT_CONFIG_KEY_0="safe.directory",
                GIT_CONFIG_VALUE_0=root,
            )
        token = os.environ.get("SENTRYINSIGHT_ADMISSION_GITHUB_TOKEN")
        if token:
            repository = os.environ.get("GITHUB_REPOSITORY", "")
            if not (
                os.environ.get("GITHUB_ACTIONS") == "true"
                and env.get("GIT_CONFIG_VALUE_0") == root
                and re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository)
            ):
                raise RepairBudgetError()
            authorization = base64.b64encode(
                f"x-access-token:{token}".encode()
            ).decode()
            env.update(
                GIT_CONFIG_COUNT="2",
                GIT_CONFIG_KEY_1=f"http.https://github.com/{repository}.git.extraheader",
                GIT_CONFIG_VALUE_1=f"AUTHORIZATION: basic {authorization}",
            )
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
            raise RepairBudgetError() from None

    async def reserve(self, request_sha256: str) -> dict:
        reservation = await asyncio.to_thread(
            self._invoke,
            "repair-reserve",
            [
                "--request-sha256",
                request_sha256,
                "--max-repairs",
                str(self._max_repairs),
            ],
        )
        if not (
            set(reservation) == {"slot", "max_repairs", "request_sha256", "token"}
            and type(reservation["slot"]) is int
            and 1 <= reservation["slot"] <= self._max_repairs
            and type(reservation["max_repairs"]) is int
            and reservation["max_repairs"] == self._max_repairs
            and reservation["request_sha256"] == request_sha256
            and _matches(reservation["token"], r"[a-f0-9]{32}")
        ):
            raise RepairBudgetError()
        return reservation

    async def finish(
        self, reservation: dict, disposition: str, *, retry_after: float = 0
    ) -> None:
        options = {
            "request-sha256": reservation["request_sha256"],
            "max-repairs": reservation["max_repairs"],
            "slot": reservation["slot"],
            "token": reservation["token"],
            "disposition": disposition,
            "retry-after": retry_after,
        }
        arguments = [
            part for key, value in options.items() for part in (f"--{key}", str(value))
        ]
        result = await asyncio.to_thread(self._invoke, "repair-finish", arguments)
        if set(result) != {"recorded"} or result["recorded"] is not True:
            raise RepairBudgetError()


class RepairSlotAttemptBudget:
    """Single-send ``AttemptBudget`` adapter binding one OpenRouter repair call
    to one slot in a ``RepairBudget``."""

    def __init__(self, repair_budget: RepairBudget):
        self._budget = repair_budget
        self._used = False
        self.last_reservation: dict | None = None

    async def reserve(self, request_sha256: str, limit: int) -> dict:
        if self._used or limit != 1:
            raise AttemptBudgetError()
        self._used = True
        try:
            reservation = await self._budget.reserve(request_sha256)
        except RepairBudgetError:
            raise AttemptBudgetError() from None
        self.last_reservation = reservation
        return {
            **reservation,
            "attempt": 1,
            "limit": 1,
        }

    async def finish(
        self, reservation: dict, disposition: str, *, retry_after: float = 0
    ) -> None:
        try:
            await self._budget.finish(reservation, disposition, retry_after=retry_after)
        except RepairBudgetError:
            raise AttemptBudgetError() from None


def build_repair_budget(
    *, max_repairs: int = MAX_REPAIR_REQUESTS_PER_RUN
) -> RepairBudget:
    """Return the durable admission repair budget in CI, or an in-process one locally."""
    durable = os.getenv("SENTRYINSIGHT_ATTEMPT_STORE")
    if durable:
        if durable != "admission":
            raise RepairBudgetError("Unsupported attempt store for repair")
        return AdmissionRepairBudget.from_environment(max_repairs=max_repairs)
    return MemoryRepairBudget(max_repairs=max_repairs)
