"""Closed canary clock: verified public run origin, never a spend permission."""

from dataclasses import dataclass, field
import asyncio
from datetime import datetime, timedelta, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import stat
import time

JOB_SECONDS = 2400
RECEIVE_SECONDS = 1600
SETUP_SECONDS = 120
POST_SECONDS = 600
CLEANUP_SECONDS = 80
LOCAL_CLEANUP_SECONDS = 20
ARTIFACT_SECONDS = 60
WORKFLOW_ID = 406270829
REF = "refs/heads/canary/sentry-full-feed-20261105"
NS = 1_000_000_000
CONTEXT = (
    "GITHUB_ACTIONS",
    "GITHUB_REPOSITORY",
    "GITHUB_ACTOR",
    "GITHUB_EVENT_NAME",
    "GITHUB_REF",
    "GITHUB_SHA",
    "GITHUB_RUN_ID",
    "GITHUB_RUN_ATTEMPT",
)


class BudgetError(ValueError):
    def __init__(self):
        super().__init__("Closed canary time budget refused")


def need(value):
    if not value:
        raise BudgetError()


def utc(value):
    need(
        isinstance(value, datetime)
        and value.tzinfo is not None
        and value.utcoffset() == timedelta(0)
    )
    return value


def micros(value):
    delta = utc(value) - datetime(1970, 1, 1, tzinfo=timezone.utc)
    return (delta.days * 86400 + delta.seconds) * 1_000_000 + delta.microseconds


def context_identity(context):
    need(
        type(context) is dict and all(type(context.get(key)) is str for key in CONTEXT)
    )
    need(
        context["GITHUB_ACTIONS"] == "true"
        and context["GITHUB_REPOSITORY"] == "ricomanifesto/SentryInsight"
        and context["GITHUB_ACTOR"] == "ricomanifesto"
        and context["GITHUB_EVENT_NAME"] == "workflow_dispatch"
        and context["GITHUB_REF"] == REF
        and context["GITHUB_RUN_ATTEMPT"] == "1"
    )
    need(
        re.fullmatch("[a-f0-9]{40}", context["GITHUB_SHA"]) is not None
        and re.fullmatch("[0-9]{1,20}", context["GITHUB_RUN_ID"]) is not None
    )
    return hashlib.sha256(
        json.dumps(
            {key: context[key] for key in CONTEXT},
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
    ).hexdigest()


@dataclass(frozen=True)
class PhaseDeadline:
    deadline_ns: int

    def remaining(self, mono_ns=None):
        current = time.monotonic_ns() if mono_ns is None else mono_ns
        need(type(current) is int)
        seconds = (self.deadline_ns - current) / NS
        need(math.isfinite(seconds) and seconds > 0)
        return seconds

    def capped(self, seconds):
        return PhaseDeadline(
            min(self.deadline_ns, time.monotonic_ns() + int(seconds * NS))
        )

    def timeout(self):
        # Default-loop and system monotonic clocks have the same rate. Sample
        # the loop first: an intervening scheduling pause only shortens time.
        loop_sample = asyncio.get_running_loop().time()
        mono_sample = time.monotonic_ns()
        self.remaining(mono_sample)
        return AbsoluteTimeout(
            self,
            asyncio.timeout_at(loop_sample + (self.deadline_ns - mono_sample) / NS),
        )


class AbsoluteTimeout:
    """Recheck when construction and entry are separated by a pause."""

    def __init__(self, phase, context):
        self.phase, self.context = phase, context

    async def __aenter__(self):
        self.phase.remaining()
        return await self.context.__aenter__()

    async def __aexit__(self, *args):
        return await self.context.__aexit__(*args)

    def expired(self):
        return self.context.expired()


@dataclass(frozen=True)
class DeadlineBudget:
    execution_date: str
    context_sha256: str
    created_us: int
    anchor_wall_us: int
    anchor_monotonic_ns: int
    job_deadline_ns: int
    day_deadline_ns: int
    _phases: dict = field(default_factory=dict, compare=False, repr=False)

    def record(self):
        return {
            "schema_version": 1,
            **{key: value for key, value in self.__dict__.items() if key != "_phases"},
        }

    @classmethod
    def restore(cls, record, context, date):
        fields = {
            "execution_date",
            "context_sha256",
            "created_us",
            "anchor_wall_us",
            "anchor_monotonic_ns",
            "job_deadline_ns",
            "day_deadline_ns",
        }
        need(
            type(record) is dict
            and set(record) == fields | {"schema_version"}
            and type(record["schema_version"]) is int
            and record["schema_version"] == 1
        )
        need(
            all(
                type(record[key]) is int
                for key in fields - {"execution_date", "context_sha256"}
            )
        )
        need(
            record["execution_date"] == date
            and record["context_sha256"] == context_identity(context)
        )
        value = cls(**{key: record[key] for key in fields})
        day = datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        need(
            value.created_us <= value.anchor_wall_us and value.anchor_monotonic_ns >= 0
        )
        need(micros(day) <= value.anchor_wall_us < micros(day + timedelta(days=1)))
        need(
            value.job_deadline_ns
            == value.anchor_monotonic_ns
            + (value.created_us + JOB_SECONDS * 1_000_000 - value.anchor_wall_us) * 1000
        )
        need(
            value.day_deadline_ns
            == value.anchor_monotonic_ns
            + (micros(day + timedelta(days=1)) - value.anchor_wall_us) * 1000
        )
        return value

    def remaining(self, mono_ns=None):
        current = time.monotonic_ns() if mono_ns is None else mono_ns
        need(type(current) is int and current >= self.anchor_monotonic_ns)
        return (min(self.job_deadline_ns, self.day_deadline_ns) - current) / NS

    def gate(self, seconds, *, now=None, mono_ns=None):
        wall = utc(now or datetime.now(timezone.utc))
        need(wall.date().isoformat() == self.execution_date)
        next_day = datetime.strptime(self.execution_date, "%Y-%m-%d").replace(
            tzinfo=timezone.utc
        ) + timedelta(days=1)
        # A forward wall-clock change may shorten the UTC allowance; it can
        # never extend the already anchored monotonic job/day deadlines.
        need((next_day - wall).total_seconds() >= seconds)
        need(self.remaining(mono_ns) >= seconds)

    def before_reserve(self, *, now=None, mono_ns=None):
        self.gate(
            20 + RECEIVE_SECONDS + POST_SECONDS + CLEANUP_SECONDS,
            now=now,
            mono_ns=mono_ns,
        )

    def before_send(self, *, now=None, mono_ns=None):
        self.gate(
            RECEIVE_SECONDS + POST_SECONDS + CLEANUP_SECONDS, now=now, mono_ns=mono_ns
        )

    def phase(self, name, *, mono_ns=None):
        if name in self._phases:
            return self._phases[name]
        current = time.monotonic_ns() if mono_ns is None else mono_ns
        need(type(current) is int and current >= self.anchor_monotonic_ns)
        end = min(self.job_deadline_ns, self.day_deadline_ns)
        if name == "setup":
            end -= (RECEIVE_SECONDS + POST_SECONDS + CLEANUP_SECONDS) * NS
        elif name == "receive":
            end = min(
                current + RECEIVE_SECONDS * NS,
                end - (POST_SECONDS + CLEANUP_SECONDS) * NS,
            )
        elif name == "post":
            end = min(current + POST_SECONDS * NS, end - CLEANUP_SECONDS * NS)
        elif name == "cleanup":
            end = min(current + LOCAL_CLEANUP_SECONDS * NS, end - ARTIFACT_SECONDS * NS)
        elif name == "artifact":
            end = min(current + ARTIFACT_SECONDS * NS, end)
        else:
            raise BudgetError()
        value = PhaseDeadline(end)
        value.remaining(current)
        self._phases[name] = value
        return value


def anchor_run(metadata, context, date, *, now=None, mono_ns=None):
    mono = time.monotonic_ns() if mono_ns is None else mono_ns
    wall = utc(now or datetime.now(timezone.utc))
    identity = context_identity(context)
    need(type(metadata) is dict and type(mono) is int and mono >= 0)
    need(
        type(metadata.get("id")) is int
        and str(metadata["id"]) == context["GITHUB_RUN_ID"]
    )
    need(
        metadata.get("repository", {}).get("full_name") == context["GITHUB_REPOSITORY"]
        and metadata.get("actor", {}).get("login") == context["GITHUB_ACTOR"]
    )
    need(
        metadata.get("event") == "workflow_dispatch"
        and metadata.get("head_sha") == context["GITHUB_SHA"]
        and metadata.get("head_branch") == REF.removeprefix("refs/heads/")
    )
    need(
        type(metadata.get("workflow_id")) is int
        and metadata["workflow_id"] == WORKFLOW_ID
        and type(metadata.get("run_attempt")) is int
        and metadata["run_attempt"] == 1
        and metadata.get("status") == "in_progress"
    )
    raw = metadata.get("created_at")
    need(
        type(raw) is str
        and re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", raw)
    )
    created = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    need(created <= wall and wall.date().isoformat() == date)
    end = datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=timezone.utc) + timedelta(
        days=1
    )
    value = DeadlineBudget(
        date,
        identity,
        micros(created),
        micros(wall),
        mono,
        mono + (micros(created) + JOB_SECONDS * 1_000_000 - micros(wall)) * 1000,
        mono + (micros(end) - micros(wall)) * 1000,
    )
    value.remaining(mono)
    return value


def clock_path():
    root = os.environ.get("RUNNER_TEMP")
    if not isinstance(root, str) or not Path(root).is_absolute():
        raise BudgetError()
    return Path(root) / "sentry-canary-clock.json"


def save_clock(path, value):
    descriptor = os.open(
        path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600
    )
    with os.fdopen(descriptor, "wb") as stream:
        stream.write(
            json.dumps(value.record(), sort_keys=True, separators=(",", ":")).encode()
        )
        stream.flush()
        os.fsync(stream.fileno())


def strict_json(raw):
    def unique(pairs):
        value = {}
        for key, item in pairs:
            need(key not in value)
            value[key] = item
        return value

    return json.loads(raw, object_pairs_hook=unique)


def load_clock(path, context, date):
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(descriptor, "rb") as stream:
        info = os.fstat(stream.fileno())
        need(
            stat.S_ISREG(info.st_mode)
            and info.st_uid == os.geteuid()
            and info.st_nlink == 1
            and stat.S_IMODE(info.st_mode) == 0o600
            and info.st_size <= 2048
        )

        record = strict_json(stream.read(2049))
    return DeadlineBudget.restore(record, context, date)
