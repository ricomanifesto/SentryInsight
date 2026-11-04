#!/usr/bin/env python3
"""One manual, nonpublishing trial of two fixed fictional requests."""

from __future__ import annotations

import argparse
import asyncio
from dataclasses import dataclass, field
from enum import Enum
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
from typing import Callable, Mapping

import httpx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

REPOSITORY = "ricomanifesto/SentryInsight"
TEST_REF = "refs/heads/test/selected-model-fixtures-20261104"
WORKFLOW = ".github/workflows/verify-nemotron.yml"
ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
RESPONSE_LIMIT = 4 * 1024 * 1024
CEILING_MICROUSD = 2_000_000
REMOTE_MAIN = {
    "SentryInsight": "1e8e9d082b29f4d64d5f75138d360cc894a33032",
    "GRCInsight": "72c2b9aee2ca467846cb8cd661b2e22cd6bb9045",
}


class TrialError(RuntimeError):
    """An application-owned code; never include a child/provider exception."""


class Case(str, Enum):
    SENTRY = "sentry"
    GRC = "grc"


@dataclass(frozen=True)
class TrialSpec:
    model: str
    provider: str
    source_sha: str
    fixture: str
    fixture_sha: str
    canonical_sha: str
    wire_sha: str
    wire_bytes: int
    input_reserve: int
    max_tokens: int
    reserve_microusd: int


CASES = {
    Case.SENTRY: TrialSpec(
        "moonshotai/kimi-k3.1-pro",
        "moonshotai/mxfp4",
        "4833a2907cff7690a333d9c80825c8339a270e2d",
        "evals/nemotron_verification/case.json",
        "2d8c314d1a5c5b6234ad8a0f7be2bb4c93668385c8135381d7c9aded83b02040",
        "4a75f3fec71dc716eab1ed3089e2b0ab10ef2258fbb73d85eca3f444c3c264ef",
        "64f3e2a80ea363fef9a70a0b6eec8a0620abd2bb44c9a808abc2f1a55b93bdc7",
        14437,
        20000,
        32000,
        360000,
    ),
    Case.GRC: TrialSpec(
        "google/gemini-4-argon",
        "google-ai-studio",
        "800d2f572dc1b4d2a26f4c74fe9b08f33e455c6a",
        "agent/tests/fixtures/selected_model_case.json",
        "f21bbf7ad30e72e485ecfb6ae6ce078fcd98959d4f0d3c5a28eab0f2b3955b08",
        "8399bd5051d790cd3db83dad81b6d2375b699822677db9633e8403c8dce7b0dc",
        "8dd9b63173ec908ff8ab428c8ac4459d6b94c22e768b5cabf87a96e33010e294",
        17232,
        22000,
        8000,
        124000,
    ),
}


@dataclass(frozen=True)
class PreparedTrial:
    spec: TrialSpec
    wire: bytes = field(repr=False)


@dataclass(frozen=True)
class Layout:
    sentry: Path
    grc: Path
    sentry_python: Path
    grc_python: Path
    tokenizer: Path


@dataclass(frozen=True)
class Context:
    commit: str
    run_id: str
    ref: str


def require(condition: object, code: str) -> None:
    if not condition:
        raise TrialError(code)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def validate_context(env: Mapping[str, str], expected: str) -> Context:
    require(re.fullmatch(r"[a-f0-9]{40}", expected), "context_refused")
    fixed = {
        "GITHUB_ACTIONS": "true",
        "GITHUB_REPOSITORY": REPOSITORY,
        "GITHUB_EVENT_NAME": "workflow_dispatch",
        "GITHUB_REF": TEST_REF,
        "GITHUB_SHA": expected,
        "GITHUB_RUN_ATTEMPT": "1",
        "GITHUB_ACTOR": "ricomanifesto",
        "GITHUB_TRIGGERING_ACTOR": "ricomanifesto",
        "GITHUB_WORKFLOW_REF": f"{REPOSITORY}/{WORKFLOW}@{TEST_REF}",
    }
    require(
        all(env.get(key) == value for key, value in fixed.items()), "context_refused"
    )
    run_id = env.get("GITHUB_RUN_ID", "")
    require(re.fullmatch(r"[0-9]{1,20}", run_id), "context_refused")
    return Context(expected, run_id, TEST_REF)


def validate_prior_runs(context: Context, value: dict) -> None:
    rows = value.get("workflow_runs")
    if not isinstance(rows, list) or len(rows) != 1 or value.get("total_count") != 1:
        raise TrialError("prior_run_or_history_unknown")
    row = rows[0]
    require(type(row) is dict, "prior_run_or_history_unknown")
    require(
        row.get("id") == int(context.run_id)
        and row.get("head_sha") == context.commit
        and row.get("head_branch") == context.ref.removeprefix("refs/heads/")
        and row.get("event") == "workflow_dispatch"
        and row.get("run_attempt") == 1
        and row.get("actor", {}).get("login") == "ricomanifesto"
        and row.get("triggering_actor", {}).get("login") == "ricomanifesto"
        and str(row.get("path", "")).split("@", 1)[0] == WORKFLOW,
        "prior_run_or_history_unknown",
    )


def validate_wire(case: Case, wire: bytes) -> PreparedTrial:
    spec = CASES[case]
    require(
        type(wire) is bytes
        and len(wire) == spec.wire_bytes
        and sha(wire) == spec.wire_sha,
        "wire_refused",
    )
    payload = json.loads(wire)
    require(sha(canonical(payload)) == spec.canonical_sha, "wire_refused")
    keys = {
        "model",
        "max_tokens",
        "stream",
        "messages",
        "provider",
        "reasoning",
        "service_tier",
    }
    if case is Case.GRC:
        keys.add("response_format")
    require(
        set(payload) == keys
        and payload["model"] == spec.model
        and type(payload["max_tokens"]) is int
        and payload["max_tokens"] == spec.max_tokens
        and payload["stream"] is False
        and payload["service_tier"] == "default"
        and payload["reasoning"] == {"effort": "low", "exclude": True}
        and payload["provider"]
        == {
            "only": [spec.provider],
            "allow_fallbacks": False,
            "require_parameters": True,
            "data_collection": "deny",
            "zdr": True,
            "max_price": {"prompt": 2, "completion": 10, "request": 0},
        },
        "wire_refused",
    )
    messages = payload["messages"]
    require(
        type(messages) is list
        and len(messages) == 2
        and [row.get("role") for row in messages] == ["system", "user"]
        and all(
            set(row) == {"role", "content"} and type(row["content"]) is str
            for row in messages
        ),
        "wire_refused",
    )
    complete = {"messages": messages}
    if case is Case.GRC:
        complete["response_format"] = payload["response_format"]
    # Sentry's previously frozen bound counts the messages serialization alone.
    encoded = json.dumps(
        messages if case is Case.SENTRY else complete, ensure_ascii=True
    ).encode()
    require(len(encoded) + 4096 <= spec.input_reserve, "input_reserve_refused")
    return PreparedTrial(spec, wire)


def git(source: Path, *args: str) -> bytes:
    env = {
        "PATH": os.environ.get("PATH", os.defpath),
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_CONFIG_GLOBAL": "/dev/null",
        "GIT_TERMINAL_PROMPT": "0",
    }
    try:
        return subprocess.check_output(
            ["git", "--no-optional-locks", *args],
            cwd=source,
            env=env,
            stderr=subprocess.DEVNULL,
            timeout=15,
        )
    except Exception:
        raise TrialError("source_refused") from None


def source_snapshot(layout: Layout) -> dict:
    result = {}
    for case, source in ((Case.SENTRY, layout.sentry), (Case.GRC, layout.grc)):
        require(
            git(source, "rev-parse", "HEAD").decode().strip() == CASES[case].source_sha,
            "source_refused",
        )
        require(
            not git(source, "status", "--porcelain", "--untracked-files=no").strip(),
            "source_refused",
        )
        require(
            sha((source / CASES[case].fixture).read_bytes()) == CASES[case].fixture_sha,
            "fixture_refused",
        )
        paths = git(source, "ls-files", "-z").decode().split("\0")
        # Source and all tracked public artifacts are read, never written.
        result[case.value] = {
            path: sha((source / path).read_bytes()) for path in paths if path
        }
    return result


def worker_environment(
    scratch: Path, tokenizer: Path, inherited: Mapping[str, str]
) -> dict[str, str]:
    return {
        "PATH": inherited.get("PATH", os.defpath),
        "HOME": str(scratch),
        "TMPDIR": str(scratch),
        "TRIAL_WORKER_SCRATCH": str(scratch),
        "TIKTOKEN_CACHE_DIR": str(tokenizer),
        "PYTHONDONTWRITEBYTECODE": "1",
        "OTEL_SDK_DISABLED": "true",
        "LOGFIRE_SEND_TO_LOGFIRE": "false",
        "LANGSMITH_TRACING": "false",
        "LANGCHAIN_TRACING_V2": "false",
        "AWS_CONFIG_FILE": "/dev/null",
        "AWS_SHARED_CREDENTIALS_FILE": "/dev/null",
        "AWS_EC2_METADATA_DISABLED": "true",
        "AWS_ACCESS_KEY_ID": "synthetic",
        "AWS_SECRET_ACCESS_KEY": "synthetic",
    }


async def _worker(
    layout: Layout, case: Case, mode: str, response: bytes = b""
) -> bytes:
    python = layout.sentry_python if case is Case.SENTRY else layout.grc_python
    source = layout.sentry if case is Case.SENTRY else layout.grc
    limit = 65536 if mode in {"prepare", "prepare_vertex"} else 16384
    require(len(response) <= 6 * 1024 * 1024, "worker_input_refused")
    with tempfile.TemporaryDirectory(prefix="selected-model-worker-") as directory:
        scratch = Path(directory)
        process = await asyncio.create_subprocess_exec(
            str(python),
            "-B",
            str(ROOT / "scripts/selected_model_fixture_worker.py"),
            mode,
            case.value,
            str(source.resolve()),
            cwd=scratch,
            env=worker_environment(scratch, layout.tokenizer, os.environ),
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.DEVNULL,
        )
        try:
            async with asyncio.timeout(90):
                assert process.stdin is not None and process.stdout is not None
                process.stdin.write(response)
                await process.stdin.drain()
                process.stdin.close()
                output = bytearray()
                while block := await process.stdout.read(
                    min(4096, limit + 1 - len(output))
                ):
                    output.extend(block)
                    require(len(output) <= limit, "worker_output_refused")
                await process.wait()
                require(process.returncode == 0, "worker_failed")
                return bytes(output)
        except BaseException:
            if process.returncode is None:
                process.kill()
            await process.wait()
            raise TrialError("worker_failed") from None


def prepare_all(layout: Layout) -> dict[Case, PreparedTrial]:
    before = source_snapshot(layout)
    values = {
        case: validate_wire(case, asyncio.run(_worker(layout, case, "prepare")))
        for case in Case
    }
    require(before == source_snapshot(layout), "source_changed")
    return values


class Claim:
    """One open, exclusive private inode; crashes never rearm this claim."""

    def __init__(self, path: Path, context: Context):
        self.path = path
        self.fd = -1
        self.value = self._initial_value(context)
        require(self.value["reserved_microusd"] <= CEILING_MICROUSD, "budget_refused")
        self._open()

    def _initial_value(self, context: Context) -> dict:
        return {
            "run_id": context.run_id,
            "commit": context.commit,
            "ref": context.ref,
            "ceiling_microusd": CEILING_MICROUSD,
            "reserved_microusd": sum(spec.reserve_microusd for spec in CASES.values()),
            "states": {case.value: "pending" for case in Case},
            "requests": {
                case.value: {
                    "source_sha": spec.source_sha,
                    "fixture_sha256": spec.fixture_sha,
                    "canonical_payload_sha256": spec.canonical_sha,
                    "wire_sha256": spec.wire_sha,
                    "requested_model": spec.model,
                    "requested_provider": spec.provider,
                    "input_reserve": spec.input_reserve,
                    "max_tokens": spec.max_tokens,
                    "reserve_microusd": spec.reserve_microusd,
                }
                for case, spec in CASES.items()
            },
        }

    def _open(self):
        path = self.path
        try:
            parent = path.parent.lstat()
            require(
                stat.S_ISDIR(parent.st_mode)
                and stat.S_IMODE(parent.st_mode) == 0o700
                and parent.st_uid == os.getuid(),
                "claim_directory_refused",
            )
            self.directory_identity = (parent.st_dev, parent.st_ino)
            self.fd = os.open(
                path,
                os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_NONBLOCK,
                0o600,
            )
            self.identity = (os.fstat(self.fd).st_dev, os.fstat(self.fd).st_ino)
            self._save()
            directory = os.open(
                path.parent,
                os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_NONBLOCK,
            )
            try:
                parent_fd = os.fstat(directory)
                require(
                    (parent_fd.st_dev, parent_fd.st_ino) == self.directory_identity,
                    "claim_directory_refused",
                )
                os.fsync(directory)
            finally:
                os.close(directory)
        except Exception:
            self.close()
            raise TrialError("claim_unavailable_or_used") from None

    def _save(self):
        parent = self.path.parent.lstat()
        require(
            stat.S_ISDIR(parent.st_mode)
            and stat.S_IMODE(parent.st_mode) == 0o700
            and parent.st_uid == os.getuid()
            and (parent.st_dev, parent.st_ino) == self.directory_identity,
            "claim_directory_refused",
        )
        current = os.fstat(self.fd)
        named = self.path.lstat()
        for value in (current, named):
            require(
                stat.S_ISREG(value.st_mode)
                and stat.S_IMODE(value.st_mode) == 0o600
                and value.st_uid == os.getuid()
                and value.st_nlink == 1
                and (value.st_dev, value.st_ino) == self.identity,
                "claim_refused",
            )
        raw = canonical(self.value)
        os.lseek(self.fd, 0, os.SEEK_SET)
        offset = 0
        while offset < len(raw):
            written = os.write(self.fd, raw[offset:])
            require(written > 0, "claim_refused")
            offset += written
        os.ftruncate(self.fd, len(raw))
        os.fsync(self.fd)

    def start(self, case: Case):
        require(self.value["states"][case.value] == "pending", "claim_already_consumed")
        self.value["states"][case.value] = "sending"
        self._save()

    def finish(self, case: Case, state: str):
        require(self.value["states"][case.value] == "sending", "claim_refused")
        require(
            state in {"response_received", "uncertain", "http_error", "protocol_error"},
            "claim_refused",
        )
        self.value["states"][case.value] = state
        self._save()

    def close(self):
        if self.fd >= 0:
            os.close(self.fd)
            self.fd = -1

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        self.close()


def response_metadata(case: Case, raw: bytes) -> dict:
    from src.core.model_route import validate_completion

    try:
        payload = json.loads(raw)
        require(type(payload) is dict, "protocol_error")
        usage = validate_completion(payload, CASES[case].model, CASES[case].max_tokens)
        if usage is not None:
            require(
                usage.get("prompt_tokens", 0) <= CASES[case].input_reserve,
                "accounting_refused",
            )
            cost = usage.get("cost")
            require(
                cost is None or cost * 1_000_000 <= CASES[case].reserve_microusd,
                "accounting_refused",
            )
        generation = payload.get("id")
        if not isinstance(generation, str) or not re.fullmatch(
            r"gen-[A-Za-z0-9_-]{1,120}", generation
        ):
            generation = None
        allowed_provider = "Moonshot AI" if case is Case.SENTRY else "Google AI Studio"
        require(payload.get("provider") in (None, allowed_provider), "provider_refused")
        return {
            "resolved_model": payload["model"],
            "actual_service_tier": payload.get("service_tier"),
            "serving_provider": (
                allowed_provider
                if payload.get("provider") == allowed_provider
                else None
            ),
            "generation_id": generation,
            "usage": usage,
        }
    except Exception:
        raise TrialError("protocol_or_accounting_error") from None


def continuation_known(metadata: dict) -> bool:
    """No next allocation after unknown tier or incomplete/inconsistent billing."""
    usage = metadata.get("usage")
    return (
        metadata.get("actual_service_tier") == "default"
        and isinstance(usage, dict)
        and all(
            name in usage
            for name in ("prompt_tokens", "completion_tokens", "total_tokens", "cost")
        )
        and usage["total_tokens"] == usage["prompt_tokens"] + usage["completion_tokens"]
    )


def execute(
    prepared: dict[Case, PreparedTrial],
    layout: Layout,
    context: Context,
    claim_path: Path,
    read_key: Callable[[], str],
    client: httpx.Client,
) -> dict:
    require(set(prepared) == set(Case), "preparation_refused")
    for case in Case:
        require(prepared[case].spec is CASES[case], "preparation_refused")
        validate_wire(case, prepared[case].wire)
    before = source_snapshot(layout)
    rows: list[dict] = []
    with Claim(claim_path, context) as claim:
        key = read_key()
        require(type(key) is str and bool(key.strip()), "credential_unavailable")
        for case in Case:
            spec = CASES[case]
            require(before == source_snapshot(layout), "source_changed")
            row: dict = {
                "case": case.value,
                "requested_model": spec.model,
                "requested_provider": spec.provider,
                "source_sha": spec.source_sha,
                "fixture_sha256": spec.fixture_sha,
                "canonical_payload_sha256": spec.canonical_sha,
                "wire_sha256": spec.wire_sha,
                "http_status": None,
                "outcome": "uncertain",
                "usage": None,
            }
            claim.start(case)  # This acknowledgement is required before entering HTTP.
            rows.append(row)
            try:
                with client.stream(
                    "POST",
                    ENDPOINT,
                    content=prepared[case].wire,
                    headers={
                        "Authorization": "Bearer " + key,
                        "Content-Type": "application/json",
                        "X-Title": "Fixed fictional model verification",
                    },
                    follow_redirects=False,
                ) as response:
                    row["http_status"] = response.status_code
                    if response.status_code != 200:
                        claim.finish(case, "http_error")
                        row["outcome"] = "http_error"
                        break  # Do not read or log an untrusted error body.
                    body = bytearray()
                    for block in response.iter_bytes(chunk_size=65536):
                        body.extend(block)
                        require(len(body) <= RESPONSE_LIMIT, "response_too_large")
                metadata = response_metadata(case, bytes(body))
                row.update(metadata)
                claim.finish(case, "response_received")
            except Exception:
                if claim.value["states"][case.value] == "sending":
                    claim.finish(case, "uncertain")
                row["outcome"] = "transport_or_protocol_unknown"
                break
            try:
                host = json.loads(
                    asyncio.run(_worker(layout, case, "validate", bytes(body)))
                )
                host = validate_host_metadata(case, host)
                row["host"] = host
                row["outcome"] = (
                    "passed"
                    if host["outcome"] == "passed"
                    else "host_validation_failed"
                )
            except Exception:
                row["host"] = {"outcome": "failed", "stage": "replay_unavailable"}
                row["outcome"] = "replay_unknown"
                break
            if not continuation_known(metadata):
                row["outcome"] = "accounting_or_tier_unknown"
                break
            # A known complete response may fail host quality; no repair call.
        require(before == source_snapshot(layout), "source_changed")
    costs = [
        row["usage"].get("cost") if isinstance(row.get("usage"), dict) else None
        for row in rows
    ]
    actual_cost = (
        sum(costs)
        if costs and all(type(value) in (int, float) for value in costs)
        else None
    )
    return {
        "schema_version": 1,
        "run_id": context.run_id,
        "executor_commit": context.commit,
        "ceiling_usd": 2,
        "upper_estimate_usd": 0.484,
        "actual_cost": actual_cost,
        "cost_scope": "executed_cases_only",
        "cases": rows,
        "published": False,
        "production_ready": False,
    }


def public_json(client: httpx.Client, path: str, params: dict | None = None) -> dict:
    try:
        with client.stream(
            "GET",
            "https://api.github.com/" + path,
            params=params,
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2026-03-10",
            },
            follow_redirects=False,
        ) as response:
            require(response.status_code == 200, "remote_fence_unavailable")
            body = bytearray()
            for chunk in response.iter_bytes(chunk_size=65536):
                body.extend(chunk)
                require(len(body) <= 2_000_000, "remote_fence_unavailable")
        value = json.loads(body)
        require(type(value) is dict, "remote_fence_unavailable")
        return value
    except Exception:
        raise TrialError("remote_fence_unavailable") from None


def remote_snapshot(client: httpx.Client) -> dict:
    result = {}
    for repo in REMOTE_MAIN:
        ref = public_json(client, f"repos/ricomanifesto/{repo}/git/ref/heads/main")
        commit = ref.get("object", {}).get("sha", "")
        require(commit == REMOTE_MAIN[repo], "remote_main_changed")
        tree = public_json(
            client, f"repos/ricomanifesto/{repo}/git/trees/{commit}", {"recursive": "1"}
        )
        require(
            tree.get("truncated") is False and type(tree.get("tree")) is list,
            "remote_fence_unavailable",
        )
        blobs = {
            row["path"]: row["sha"]
            for row in tree["tree"]
            if row.get("type") == "blob"
            and (
                row.get("path", "").startswith(("reports/", "site/"))
                or row.get("path")
                in {
                    "index.md",
                    "index.html",
                    "current-findings.json",
                    ".sentryinsight-articles-fingerprint",
                }
            )
        }
        require(blobs, "remote_fence_unavailable")
        result[repo] = {"commit": commit, "report_blobs": blobs}
    return result


def validate_host_metadata(case: Case, value: dict) -> dict:
    if not isinstance(value, dict):
        raise TrialError("worker_failed")
    if value == {"outcome": "failed", "stage": "host_rejected"}:
        return value
    keys = {"outcome", "stage", "source_count", "rendered_sha256"}
    counts = (
        {"eligible_sources": 1, "held_sources": 1}
        if case is Case.SENTRY
        else {"regulatory_changes": 0}
    )
    keys.update(counts)
    if case is Case.GRC:
        keys.add("grounded_control_findings")
    require(
        set(value) == keys
        and value.get("outcome") == "passed"
        and value.get("stage") == "host_rendered"
        and type(value.get("source_count")) is int
        and value["source_count"] == 2
        and all(
            type(value.get(key)) is int and value[key] == count
            for key, count in counts.items()
        )
        and type(value.get("rendered_sha256")) is str
        and re.fullmatch(r"[a-f0-9]{64}", value["rendered_sha256"]),
        "worker_failed",
    )
    if case is Case.GRC:
        require(
            type(value.get("grounded_control_findings")) is int
            and 1 <= value["grounded_control_findings"] <= 100,
            "worker_failed",
        )
    return value


def write_metadata(path: Path, value: dict) -> None:
    raw = canonical(value) + b"\n"
    require(len(raw) <= 32768, "receipt_too_large")
    fd = os.open(
        path,
        os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_NONBLOCK,
        0o600,
    )
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
    except BaseException:
        raise TrialError("receipt_unavailable") from None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--offline-only", action="store_true")
    mode.add_argument("--live", action="store_true")
    parser.add_argument("--expected-commit", default="")
    parser.add_argument("--sentry-source", required=True, type=Path)
    parser.add_argument("--grc-source", required=True, type=Path)
    parser.add_argument("--sentry-python", required=True, type=Path)
    parser.add_argument("--grc-python", required=True, type=Path)
    parser.add_argument("--tokenizer", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    os.umask(0o077)
    try:
        layout = Layout(
            args.sentry_source,
            args.grc_source,
            args.sentry_python,
            args.grc_python,
            args.tokenizer,
        )
        if args.offline_only:
            prepared = prepare_all(layout)
            write_metadata(
                args.output,
                {
                    "outcome": "calibration_passed",
                    "live_attempts": 0,
                    "cases": {
                        case.value: {
                            "wire_sha256": value.spec.wire_sha,
                            "canonical_payload_sha256": value.spec.canonical_sha,
                        }
                        for case, value in prepared.items()
                    },
                },
            )
            return 0
        context = validate_context(os.environ, args.expected_commit)
        require(
            git(ROOT, "rev-parse", "HEAD").decode().strip() == context.commit
            and not git(ROOT, "status", "--porcelain", "--untracked-files=no").strip(),
            "executor_changed",
        )
        directory = Path(os.environ["RUNNER_TEMP"]).resolve() / "selected-model-trial"
        require(
            args.output.resolve() == directory / "trial.json" and directory.is_dir(),
            "output_refused",
        )
        with httpx.Client(
            transport=httpx.HTTPTransport(retries=0, trust_env=False), timeout=30
        ) as control:
            history = public_json(
                control,
                f"repos/{REPOSITORY}/actions/workflows/verify-nemotron.yml/runs",
                {
                    "event": "workflow_dispatch",
                    "head_sha": context.commit,
                    "per_page": 100,
                },
            )
            validate_prior_runs(context, history)
            before = remote_snapshot(control)
            prepared = prepare_all(layout)
            with httpx.Client(
                transport=httpx.HTTPTransport(retries=0, trust_env=False), timeout=1800
            ) as sender:
                receipt = execute(
                    prepared,
                    layout,
                    context,
                    directory / "claim.json",
                    lambda: os.environ.get("OPENROUTER_API_KEY", ""),
                    sender,
                )
            try:
                receipt["remote_reports_unchanged"] = before == remote_snapshot(control)
            except TrialError:
                receipt["remote_reports_unchanged"] = None
            receipt["remote_main_commits"] = REMOTE_MAIN
            receipt["remote_report_snapshot_sha256"] = sha(canonical(before))
            write_metadata(args.output, receipt)
        return (
            0
            if receipt["remote_reports_unchanged"]
            and len(receipt["cases"]) == 2
            and all(row["outcome"] == "passed" for row in receipt["cases"])
            else 1
        )
    except BaseException:
        print("Trial stopped; inspect the sanitized claim and run before any retry.")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
