#!/usr/bin/env python3
"""One closed, disabled-by-default Sentry canary; no ordinary LIVE model switch."""

import argparse
import base64
import inspect
import asyncio
from dataclasses import dataclass
from datetime import datetime, timezone
import json
import logging
import os
import re
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.prepare_full_feed_canary import (  # noqa: E402
    Prepared,
    require,
    sha,
    verify_feed,
)
from scripts.rehearse_full_feed_canary import (  # noqa: E402
    ReplayPermit,
    environment,
    financial_receipt,
    decode_response,
)

from scripts.canary_deadline import (  # noqa: E402
    BudgetError,
    PhaseDeadline,
    RECEIVE_SECONDS,
    clock_path,
    load_clock,
)
from scripts.canary_process import (  # noqa: E402
    ProcessFailure,
    spawn,
    stop,
    kill_group,
    run_private,
)  # noqa: E402

DATE = "2026-11-06"
REF = "refs/heads/canary/sentry-full-feed-20261105"
MANIFEST = ROOT / "config/full-feed-canary.json"
PUBLIC_REPORTS = (
    "https://sentryinsight.ricomanifesto.com/current-findings.json",
    "https://ricomanifesto.github.io/SentryInsight/current-findings.json",
)
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

SEND_FAILURES = frozenset(
    "http_redirect http_unauthorized http_payment_required http_forbidden "
    "http_not_found http_timeout_status http_rate_limited http_client_error "
    "http_server_error http_unexpected_status send_deadline_exceeded "
    "send_connect_timeout send_read_timeout send_write_timeout send_pool_timeout "
    "send_timeout send_timeout_unknown send_connect_error send_read_error "
    "send_write_error send_network_error send_protocol_error send_transport_error "
    "send_cancelled send_unknown_failure response_encoding_refused "
    "response_body_limit response_close_failed response_decode_failed".split()
)


class SendFailure(ValueError):
    """Fixed evidence only, never exception text or an outcome/refund claim."""

    def __init__(self, code, secondary=()):
        require(type(code) is str and code in SEND_FAILURES)
        require(
            type(secondary) is tuple and secondary in ((), ("response_close_unknown",))
        )
        super().__init__("Closed canary transport refused")
        self.code, self.secondary = code, secondary


def status_failure(status):
    if type(status) is not int:
        return "http_unexpected_status"
    known = {
        401: "http_unauthorized",
        402: "http_payment_required",
        403: "http_forbidden",
        404: "http_not_found",
        408: "http_timeout_status",
        429: "http_rate_limited",
    }
    if status in known:
        return known[status]
    for first, last, code in (
        (300, 399, "http_redirect"),
        (400, 499, "http_client_error"),
        (500, 599, "http_server_error"),
    ):
        if first <= status <= last:
            return code
    return "http_unexpected_status"


def transport_failure(error, *, own_deadline=False, close_only=False):
    import httpx

    if (
        type(error) is SendFailure
        and type(error.code) is str
        and error.code in SEND_FAILURES
    ):
        return error.code
    if isinstance(error, asyncio.CancelledError):
        return "send_deadline_exceeded" if own_deadline else "send_cancelled"
    if close_only:
        return "response_close_failed"
    for kind, code in (
        (httpx.ConnectTimeout, "send_connect_timeout"),
        (httpx.ReadTimeout, "send_read_timeout"),
        (httpx.WriteTimeout, "send_write_timeout"),
        (httpx.PoolTimeout, "send_pool_timeout"),
        (httpx.TimeoutException, "send_timeout"),
        (httpx.ConnectError, "send_connect_error"),
        (httpx.ReadError, "send_read_error"),
        (httpx.WriteError, "send_write_error"),
        (httpx.CloseError, "response_close_failed"),
        (httpx.NetworkError, "send_network_error"),
        (httpx.ProtocolError, "send_protocol_error"),
        (httpx.DecodingError, "response_decode_failed"),
        (httpx.TransportError, "send_transport_error"),
        (TimeoutError, "send_timeout_unknown"),
    ):
        if isinstance(error, kind):
            return code
    return "send_unknown_failure"


@dataclass(frozen=True)
class Authority:
    manifest: dict
    manifest_sha256: str
    context: dict


def authority(raw, digest, context, prepared, expected_commit, expected_manifest, now):
    require(type(raw) is dict and raw.get("enabled") is True)
    require(
        set(raw)
        == set(
            "schema_version enabled execution_date source_role production_main production_report_sha256 feed_sha256 source_pack_sha256 wire_sha256 canonical_request_sha256 max_output_tokens whole_hold_microusd physical_limit pilot billing_basis data_approval_sha256 metadata_audience_approved output_fate".split()
        )
    )
    require(
        digest == expected_manifest
        and re.fullmatch(r"[a-f0-9]{64}", digest) is not None
    )
    require(raw["execution_date"] == DATE == now.date().isoformat())
    require(
        context.get("GITHUB_ACTIONS") == "true"
        and context.get("GITHUB_REPOSITORY") == "ricomanifesto/SentryInsight"
    )
    require(
        context.get("GITHUB_ACTOR") == "ricomanifesto"
        and context.get("GITHUB_EVENT_NAME") == "workflow_dispatch"
    )
    require(
        context.get("GITHUB_REF") == REF and context.get("GITHUB_RUN_ATTEMPT") == "1"
    )
    require(
        context.get("GITHUB_SHA") == expected_commit
        and re.fullmatch(r"[a-f0-9]{40}", expected_commit) is not None
    )
    require(context.get("GITHUB_RUN_ID", "").isdigit())
    require(
        type(raw["schema_version"]) is int
        and raw["schema_version"] == 1
        and raw["source_role"] == "reviewed_canary_candidate"
    )
    require(
        raw["pilot"] is not None
        and raw["billing_basis"] == "verified_openrouter_credit_only"
    )
    pilot = raw["pilot"]
    require(
        type(pilot) is dict and set(pilot) == {"month", "activationStart", "opening"}
    )
    require(pilot["month"] == "2026-11" and type(pilot["opening"]) is dict)
    opening = pilot["opening"]
    require(set(opening) == {"amountMicrousd", "basisSha256"})
    require(
        type(opening["amountMicrousd"]) is int
        and 0 <= opening["amountMicrousd"] <= 20000000
    )
    require(
        type(opening["basisSha256"]) is str
        and re.fullmatch(r"[a-f0-9]{64}", opening["basisSha256"]) is not None
    )
    activation = datetime.fromisoformat(pilot["activationStart"].replace("Z", "+00:00"))
    require(
        activation.isoformat(timespec="milliseconds").replace("+00:00", "Z")
        == pilot["activationStart"]
    )
    require(
        activation.tzinfo is not None
        and activation.date().isoformat() == "2026-11-05"
        and activation <= now
    )
    require(raw["metadata_audience_approved"] is True)
    require(
        type(raw["data_approval_sha256"]) is str
        and re.fullmatch(r"[a-f0-9]{64}", raw["data_approval_sha256"]) is not None
    )
    require(raw["output_fate"] in ("nonpublish", "conditional_publish"))
    for field in (
        "feed_sha256",
        "source_pack_sha256",
        "wire_sha256",
        "canonical_request_sha256",
    ):
        require(raw[field] == prepared.metadata[field])
    require(
        sha(prepared.wire) == prepared.metadata["wire_sha256"]
        and sha(prepared.pack) == prepared.metadata["source_pack_sha256"]
    )
    for field, value in (
        ("max_output_tokens", 32000),
        ("whole_hold_microusd", 7251456),
        ("physical_limit", 1),
    ):
        require(type(raw[field]) is int and raw[field] == value)
    return Authority(raw, digest, {**context, "EXPECTED_COMMIT": expected_commit})


def git(args, *, cwd=ROOT):
    child = environment()
    child["GIT_ALLOW_PROTOCOL"] = "https"
    result = subprocess.run(
        ["/usr/bin/git", *args],
        cwd=cwd,
        env=child,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        timeout=30,
        check=True,
    )
    require(len(result.stdout) <= 8192)
    return result.stdout.decode().strip()


def source_fence(approved):
    require(git(["rev-parse", "HEAD"]) == approved.context["GITHUB_SHA"])
    require(git(["status", "--porcelain"]) == "")
    require(
        git(["remote", "get-url", "origin"])
        == "https://github.com/ricomanifesto/SentryInsight.git"
    )
    require(
        git(["ls-remote", "origin", "refs/heads/main"]).split()[0]
        == approved.manifest["production_main"]
    )


class PersistentOwner:
    """One async owned process; an unknown exchange latches before any reuse."""

    def __init__(self, approved, deadline):
        node = shutil.which("node")
        require(node is not None)
        self.argv = [node, str(ROOT / "scripts/sentry_canary_owner.cjs")]
        self.env = environment()
        self.env["GIT_ALLOW_PROTOCOL"] = "https"
        self.env.update(approved.context)
        self.deadline = deadline
        self.process = None
        self.blocked = False

    async def exchange(self, value):
        require(not self.blocked)
        try:
            ack_deadline = self.deadline.capped(20)
            async with ack_deadline.timeout():
                if self.process is None:
                    self.process = await spawn(
                        self.argv,
                        env=self.env,
                        cwd=ROOT,
                        deadline=ack_deadline,
                    )
                require(
                    self.process.stdin is not None and self.process.stdout is not None
                )
                self.process.stdin.write(
                    json.dumps(value, separators=(",", ":")).encode() + b"\n"
                )
                await self.process.stdin.drain()
                raw = await self.process.stdout.readline()
                require(0 < len(raw) <= 8192 and raw.endswith(b"\n"))
                result = decode_response(raw)
                require(type(result) is dict and set(result) == {"ok"})
                return result["ok"]
        except BaseException:
            self.blocked = True
            raise ValueError("Closed canary owner refused") from None

    async def close(self):
        if self.process is not None:
            kill_group(self.process)
            await stop(self.process, self.deadline)


async def worker(value, deadline):
    child = environment()
    child["GIT_ALLOW_PROTOCOL"] = "https"
    if os.environ.get("TIKTOKEN_CACHE_DIR"):
        child["TIKTOKEN_CACHE_DIR"] = os.environ["TIKTOKEN_CACHE_DIR"]
    raw = await run_private(
        [sys.executable, "-I", "-B", str(ROOT / "scripts/canary_host_worker.py")],
        json.dumps(value, separators=(",", ":")).encode(),
        deadline,
        env=child,
        cwd=ROOT,
        limit=8 * 1024 * 1024,
    )
    result = decode_response(raw)
    require(type(result) is dict and set(result) == {"ok"})
    return result["ok"]


def approved_value(approved):
    return {
        "manifest": approved.manifest,
        "manifest_sha256": approved.manifest_sha256,
        "context": approved.context,
    }


async def owned_source_fence(approved, deadline):
    require(
        await worker(
            {"mode": "source_fence", "approved": approved_value(approved)}, deadline
        )
        == {"verified": True}
    )


async def owned_replay(raw_feed, prepared, response, permit, output, scratch, deadline):
    from scripts.canary_host_worker import packed

    return await worker(
        {
            "mode": "replay",
            "feed": base64.b64encode(raw_feed).decode(),
            "prepared": packed(prepared),
            "response": base64.b64encode(response).decode(),
            "permit": permit,
            "output": str(output),
            "scratch": str(scratch),
        },
        deadline,
    )


async def owned_publish(output, approved, scratch, deadline):
    value = await worker(
        {
            "mode": "publish",
            "approved": approved_value(approved),
            "output": str(output),
            "scratch": str(scratch),
        },
        deadline,
    )
    require(
        type(value) is dict
        and set(value) == {"commit"}
        and re.fullmatch("[a-f0-9]{40}", value["commit"]) is not None
    )
    return value["commit"]


async def emit_receipt(result, path, deadline):
    require(
        await worker({"mode": "emit", "receipt": str(path), "result": result}, deadline)
        == {"recorded": True}
    )


async def bounded_get(client, url):
    whole = PhaseDeadline(time.monotonic_ns() + 15_000_000_000)
    async with whole.timeout():
        return await _bounded_get(client, url)


async def _bounded_get(client, url):
    async with client.stream(
        "GET", url, headers={"Accept-Encoding": "identity"}
    ) as response:
        require(
            response.status_code == 200
            and response.headers.get("content-encoding") in (None, "identity")
        )
        value = bytearray()
        async for chunk in response.aiter_raw():
            require(len(value) + len(chunk) <= 2 * 1024 * 1024)
            value.extend(chunk)
    return bytes(value)


async def report_fence(client, approved):
    for url in PUBLIC_REPORTS:
        require(
            sha(await bounded_get(client, url))
            == approved.manifest["production_report_sha256"]
        )


async def post_once(client, wire, key, *, seconds=RECEIVE_SECONDS, phase_deadline=None):
    # Only the closed prepared bytes are accepted by the caller. No json kwargs,
    # model selection, URL, tools, retries or mutable provider policy interface.
    phase_deadline = phase_deadline or PhaseDeadline(
        time.monotonic_ns() + int(seconds * 1_000_000_000)
    )
    deadline = phase_deadline.timeout()
    primary = boundary = None
    body_complete = False
    try:
        async with deadline:
            try:
                async with client.stream(
                    "POST",
                    "https://openrouter.ai/api/v1/chat/completions",
                    content=wire,
                    headers={
                        "Authorization": "Bearer " + key,
                        "Content-Type": "application/json",
                        "Accept-Encoding": "identity",
                    },
                ) as response:
                    try:
                        if response.status_code != 200:
                            raise SendFailure(status_failure(response.status_code))
                        if response.headers.get("content-encoding") not in (
                            None,
                            "identity",
                        ):
                            raise SendFailure("response_encoding_refused")
                        raw = bytearray()
                        async for chunk in response.aiter_raw():
                            if len(raw) + len(chunk) > 2 * 1024 * 1024:
                                raise SendFailure("response_body_limit")
                            raw.extend(chunk)
                        body_complete = True
                    except BaseException as error:
                        primary = error
                        raise
            except BaseException as error:
                boundary = error
                raise
    except BaseException as error:
        # Only the owned context's cancellation-to-TimeoutError conversion
        # establishes its deadline. External cancellation/unowned TimeoutError
        # must not be relabeled just because elapsed wall time looks similar.
        owned = (
            deadline.expired()
            and isinstance(error, TimeoutError)
            and isinstance(boundary, asyncio.CancelledError)
        )
        observed = (
            primary
            if primary is not None
            else boundary if boundary is not None else error
        )
        code = transport_failure(
            observed, own_deadline=owned, close_only=primary is None and body_complete
        )
        secondary = (
            ("response_close_unknown",)
            if primary is not None and boundary is not primary
            else ()
        )
        raise SendFailure(code, secondary) from None
    return bytes(raw)


def promote_report(output, approved, scratch):
    """Only the validated report tree may form one fast-forward main commit."""
    from src.core.publication_transaction import promote_artifacts
    from scripts.rehearse_report_offline import public_snapshot

    require(approved.manifest["output_fate"] == "conditional_publish")
    source_fence(approved)
    target = scratch / "promotion"
    # Fixed explicit main fetch, no rebase or write retry if main moved.
    git(
        [
            "fetch",
            "--quiet",
            "--no-tags",
            "origin",
            "refs/heads/main:refs/remotes/origin/main",
        ]
    )
    require(
        git(["rev-parse", "refs/remotes/origin/main"])
        == approved.manifest["production_main"]
    )
    git(
        [
            "worktree",
            "add",
            "--detach",
            str(target),
            approved.manifest["production_main"],
        ]
    )
    try:
        promote_artifacts(output, target)
        names = sorted(public_snapshot(output))
        require(names and len(names) <= 4096)
        git(["add", "-f", "--", *names], cwd=target)
        message = scratch / "report-message.txt"
        message.write_text(
            "Update exploitation report\n\nAdmission-Key: run:"
            + approved.context["GITHUB_RUN_ID"]
            + "\nCanary-Source: "
            + approved.context["GITHUB_SHA"]
            + "\n"
        )
        git(["commit", "-F", str(message)], cwd=target)
        commit = git(["rev-parse", "HEAD"], cwd=target)
        # Normal fast-forward push only. Any lost acknowledgement stops; there
        # is no second mutation, force, automatic rollback or inference replay.
        require(datetime.now(timezone.utc).date().isoformat() == DATE)
        git(["push", "--quiet", "origin", "HEAD:refs/heads/main"], cwd=target)
        return commit
    finally:
        git(["worktree", "remove", "--force", str(target)])


async def execute(
    approved,
    raw_feed,
    prepared,
    scratch,
    *,
    owner_factory=PersistentOwner,
    sender=None,
    control=None,
    key_reader=None,
    publisher=None,
    budget,
    source_checker=owned_source_fence,
    replayer=owned_replay,
):
    """Trusted closed-job seam; tests inject fakes, public CLI fixes all adapters."""
    import httpx

    verify_feed(raw_feed)
    require(
        isinstance(prepared, Prepared)
        and sha(prepared.wire) == approved.manifest["wire_sha256"]
    )
    setup_deadline = budget.phase("setup")
    await source_checker(approved, setup_deadline)
    own_control = control is None
    own_sender = sender is None
    control = control or httpx.AsyncClient(
        trust_env=False, follow_redirects=False, timeout=15
    )
    owner = None
    receipt = None
    posted = False
    host_ok = False
    financial = None
    commit = None
    phase = "report_fence"
    failure = None
    cleanup = []
    post_deadline = None
    try:
        async with setup_deadline.timeout():
            await report_fence(control, approved)
        budget.before_reserve(now=datetime.now(timezone.utc))
        owner = (
            PersistentOwner(approved, setup_deadline)
            if owner_factory is PersistentOwner
            else owner_factory(approved)
        )
        phase = "financial_begin"
        permit = await owner.exchange(
            {
                "operation": "begin",
                "manifestSha256": approved.manifest_sha256,
                "sourceSha256": approved.manifest["source_pack_sha256"],
                "requestSha256": approved.manifest["canonical_request_sha256"],
            }
        )
        replay = ReplayPermit(permit)
        require(type(permit["attempt"]) is int and type(permit["limit"]) is int)
        require(
            type(permit["token"]) is str
            and re.fullmatch(r"[a-f0-9]{32}", permit["token"]) is not None
        )
        require(
            permit["request_sha256"] == approved.manifest["canonical_request_sha256"]
        )
        # No key lookup/transport construction occurs before all fences and the
        # existing durable money/day/original-token acknowledgement.
        phase = "credential"
        budget.before_send(now=datetime.now(timezone.utc))
        key = key_reader() if key_reader else os.environ.get("OPENROUTER_API_KEY", "")
        require(
            type(key) is str
            and bool(key.strip())
            and "\n" not in key
            and "\r" not in key
        )
        sender = sender or httpx.AsyncClient(
            transport=httpx.AsyncHTTPTransport(retries=0, trust_env=False),
            trust_env=False,
            follow_redirects=False,
            timeout=RECEIVE_SECONDS,
        )
        phase = "send"
        require(datetime.now(timezone.utc).date().isoformat() == DATE)
        budget.before_send(now=datetime.now(timezone.utc))
        receive_deadline = budget.phase("receive")
        posted = True
        response = await post_once(
            sender, prepared.wire, key, phase_deadline=receive_deadline
        )
        post_deadline = budget.phase("post")
        if isinstance(owner, PersistentOwner):
            owner.deadline = post_deadline
        key = None
        phase = "response_decode"
        body = decode_response(response)
        require(type(body) is dict)
        phase = "accounting"
        receipt = financial_receipt(response)
        require(body["usage"].get("is_byok") is False)
        receipt["costCoverage"] = "complete"
        phase = "host_replay"
        output = scratch / "validated"
        host = await replayer(
            raw_feed, prepared, response, replay.value, output, scratch, post_deadline
        )
        require(type(host) is dict and type(host.get("host_validated")) is bool)
        host_ok = host["host_validated"]
        phase = "financial_finish"
        financial = await owner.exchange({"operation": "finish", "receipt": receipt})
        require(financial["financial_settled"] is True)
        if host_ok and approved.manifest["output_fate"] == "conditional_publish":
            phase = "promotion_fence"
            require(datetime.now(timezone.utc).date().isoformat() == DATE)
            await source_checker(approved, post_deadline)
            async with post_deadline.timeout():
                await report_fence(control, approved)
            phase = "promotion"
            post_deadline.remaining()
            require(datetime.now(timezone.utc).date().isoformat() == DATE)
            commit = (
                publisher(output, approved, scratch)
                if publisher
                else await owned_publish(output, approved, scratch, post_deadline)
            )
        phase = "admission_complete"
        await owner.exchange(
            {
                "operation": "complete",
                "outcome": "published" if commit else "not-published",
            }
        )
    except BaseException as error:
        failure = "closed_check_refused"
        if type(error) is SendFailure:
            if type(error.code) is str and error.code in SEND_FAILURES:
                failure = error.code
            else:
                failure = "send_unknown_failure"
            if type(error.secondary) is tuple and error.secondary == (
                "response_close_unknown",
            ):
                cleanup.extend(error.secondary)
        elif isinstance(error, BudgetError):
            failure = "time_budget_refused"
        elif isinstance(error, ProcessFailure):
            failure = error.code
        elif phase == "response_decode":
            failure = "response_decode_refused"
        elif phase == "accounting":
            failure = "accounting_refused"
        # Finish once only if no finish was entered. Unknown owner ACK latches;
        # it must never be retried as a diagnostic or new reservation.
        if (
            owner is not None
            and not owner.blocked
            and phase
            not in {
                "financial_finish",
                "promotion_fence",
                "promotion",
                "admission_complete",
            }
        ):
            try:
                if post_deadline is None:
                    post_deadline = budget.phase("post")
                stop_deadline = post_deadline
                if isinstance(owner, PersistentOwner):
                    owner.deadline = stop_deadline
                async with stop_deadline.timeout():
                    financial = await owner.exchange(
                        {"operation": "finish", "receipt": receipt}
                    )
            except BaseException:
                pass
    finally:
        key = None
        try:
            cleanup_deadline = budget.phase("cleanup")
        except BaseException:
            cleanup_deadline = None
        if owner is not None:
            try:
                if isinstance(owner, PersistentOwner):
                    if cleanup_deadline is None:
                        if owner.process is not None:
                            kill_group(owner.process)
                        raise BudgetError()
                    owner.deadline = cleanup_deadline.capped(3)
                    await owner.close()
                else:
                    closed = owner.close()
                    if inspect.isawaitable(closed):
                        try:
                            if cleanup_deadline is None:
                                raise BudgetError()
                            async with cleanup_deadline.capped(3).timeout():
                                await closed
                        finally:
                            if inspect.iscoroutine(closed):
                                closed.close()
            except BaseException:
                cleanup.append("owner_close_unknown")
        if own_sender and sender is not None:
            try:
                if cleanup_deadline is None:
                    raise BudgetError()
                async with cleanup_deadline.capped(3).timeout():
                    await sender.aclose()
            except BaseException:
                cleanup.append("sender_close_unknown")
        if own_control:
            try:
                if cleanup_deadline is None:
                    raise BudgetError()
                async with cleanup_deadline.capped(3).timeout():
                    await control.aclose()
            except BaseException:
                cleanup.append("control_close_unknown")
        if cleanup and failure is None:
            failure = "cleanup_unknown"
            phase = "cleanup"
    return {
        "schema_version": 1,
        "phase": phase,
        "failure": failure,
        "secondary": cleanup,
        "request_entered": posted,
        "host_validated": host_ok,
        "financial_state": (
            "settled"
            if financial and financial.get("financial_settled")
            else "held_or_unknown"
        ),
        "report_commit": commit,
        "serving_publication_verified": False,
        "output_fate": approved.manifest["output_fate"],
        "source_pack_sha256": approved.manifest["source_pack_sha256"],
        "wire_sha256": approved.manifest["wire_sha256"],
        "accounting": receipt,
    }


async def run(args):
    bytes_manifest = MANIFEST.read_bytes()
    raw = decode_response(bytes_manifest)
    # A disabled source manifest is the default, not an environment LIVE flag.
    if raw.get("enabled") is not True:
        return {"ready": False, "outcome": "disabled", "request_entered": False}
    require(
        os.environ.get("RUNNER_DEBUG") != "1"
        and os.environ.get("ACTIONS_STEP_DEBUG", "").casefold() != "true"
    )
    context = {name: os.environ.get(name, "") for name in CONTEXT}
    budget = load_clock(clock_path(), context, DATE)
    args.budget = budget
    setup_deadline = budget.phase("setup")
    from scripts.canary_host_worker import unpacked

    raw_feed = args.feed_file.read_bytes()
    prepared = unpacked(
        await worker(
            {
                "mode": "prepare",
                "feed": base64.b64encode(raw_feed).decode(),
                "scratch": str(args.scratch / "capture"),
            },
            setup_deadline,
        )
    )
    context = {name: os.environ.get(name, "") for name in CONTEXT}
    approved = authority(
        raw,
        sha(bytes_manifest),
        context,
        prepared,
        args.expected_commit,
        args.expected_manifest,
        datetime.now(timezone.utc),
    )
    await owned_source_fence(approved, setup_deadline)
    budget.before_reserve(now=datetime.now(timezone.utc))
    if args.preflight_only:
        return {
            "ready": True,
            "outcome": "preflight_only",
            "request_entered": False,
            "manifest_sha256": approved.manifest_sha256,
        }
    return await execute(approved, raw_feed, prepared, args.scratch, budget=budget)


def main():
    previous = logging.root.manager.disable
    logging.disable(logging.CRITICAL)
    try:
        return _main()
    finally:
        logging.disable(previous)


def _main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--preflight-only", action="store_true")
    modes.add_argument("--execute-approved-canary", action="store_true")
    parser.add_argument("--feed-file", type=Path, required=True)
    parser.add_argument("--expected-commit", required=True)
    parser.add_argument("--expected-manifest", required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    result: dict
    scratch = Path(tempfile.mkdtemp(prefix="closed-sentry-canary-"))
    try:
        args.scratch = scratch
        result = asyncio.run(run(args))
    except BaseException:
        result = {
            "ready": False,
            "outcome": "held_or_unknown",
            "request_entered": "unknown",
        }
    finally:
        try:
            if hasattr(args, "budget"):
                cleanup_deadline = args.budget.phase("cleanup")
            else:
                cleanup_deadline = PhaseDeadline(time.monotonic_ns() + 3_000_000_000)
            asyncio.run(
                worker({"mode": "cleanup", "scratch": str(scratch)}, cleanup_deadline)
            )
        except BaseException:
            result.setdefault("secondary", []).append("scratch_cleanup_unknown")
            if not result.get("failure"):
                result["failure"] = "cleanup_unknown"
    # Exactly this sanitized file is the only Actions artifact. Logs have their
    # separate ordinary repository retention; never output a model body/error.
    try:
        asyncio.run(emit_receipt(result, args.receipt, cleanup_deadline))
        if result.get("ready") is True and args.preflight_only:
            if os.environ.get("GITHUB_OUTPUT"):
                with open(os.environ["GITHUB_OUTPUT"], "a") as stream:
                    stream.write("ready=true\n")
    except BaseException:
        # Metadata emission is not the authoritative CAS state. Never retry a
        # possibly partial write or replace the primary in-memory observation.
        result["receipt_emission"] = "unknown"
        print(json.dumps(result, sort_keys=True))
        raise SystemExit(1) from None
    print(json.dumps(result, sort_keys=True))
    if result.get("failure") or result.get("outcome") == "held_or_unknown":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
