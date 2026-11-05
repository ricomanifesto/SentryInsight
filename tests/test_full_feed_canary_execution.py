"""All future sender/authority tests use synthetic context and mocked adapters."""

import asyncio
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import pytest
from scripts import execute_full_feed_canary as canary
from scripts.prepare_full_feed_canary import prepare


class ExecutionClock(datetime):
    @classmethod
    def now(cls, tz=None):
        return cls(2026, 11, 6, 3, 4, 5, tzinfo=timezone.utc)


class FrozenInputs(tuple):
    def __repr__(self):
        return "<closed public source packet>"


@pytest.fixture(autouse=True)
def synthetic_clock(monkeypatch, tmp_path):
    from src.core import reviewed_report

    monkeypatch.setattr(canary, "datetime", ExecutionClock)
    monkeypatch.setattr(reviewed_report, "datetime", ExecutionClock)
    # Negative controls must not depend on a committed one-shot approval being
    # absent. Positive cases explicitly populate their synthetic authority.
    disabled = json.loads(canary.MANIFEST.read_bytes())
    disabled["enabled"] = False
    manifest = tmp_path / "disabled-canary.json"
    manifest.write_text(json.dumps(disabled))
    monkeypatch.setattr(canary, "MANIFEST", manifest)


@pytest.fixture(scope="module")
def prepared(tmp_path_factory):
    feed = os.environ.get("SENTRY_FROZEN_FEED")
    if not feed:
        pytest.skip("Exact external public packet required")
    raw = Path(feed).read_bytes()
    return FrozenInputs(
        (raw, asyncio.run(prepare(raw, tmp_path_factory.mktemp("prepared"))))
    )


def settings(prepared):
    raw = json.loads(canary.MANIFEST.read_bytes())
    raw.update(
        enabled=True,
        metadata_audience_approved=True,
        billing_basis="verified_openrouter_credit_only",
        data_approval_sha256="e" * 64,
        pilot={
            "month": "2026-11",
            "activationStart": "2026-11-05T00:00:00.000Z",
            "opening": {"amountMicrousd": 0, "basisSha256": "f" * 64},
        },
    )
    context = {
        "GITHUB_ACTIONS": "true",
        "GITHUB_REPOSITORY": "ricomanifesto/SentryInsight",
        "GITHUB_ACTOR": "ricomanifesto",
        "GITHUB_EVENT_NAME": "workflow_dispatch",
        "GITHUB_REF": canary.REF,
        "GITHUB_SHA": "a" * 40,
        "GITHUB_RUN_ID": "800",
        "GITHUB_RUN_ATTEMPT": "1",
    }
    return raw, context


@pytest.mark.parametrize(
    "field,value",
    [
        ("enabled", False),
        ("pilot", None),
        ("billing_basis", None),
        ("metadata_audience_approved", False),
        ("data_approval_sha256", "z" * 64),
        ("physical_limit", True),
        ("max_output_tokens", 32001),
        ("wire_sha256", "0" * 64),
    ],
)
def test_authority_fails_closed_before_any_adapter(prepared, field, value):
    raw, context = settings(prepared)
    raw[field] = value
    with pytest.raises(ValueError):
        canary.authority(
            raw,
            "d" * 64,
            context,
            prepared[1],
            "a" * 40,
            "d" * 64,
            datetime(2026, 11, 6, tzinfo=timezone.utc),
        )


@pytest.mark.parametrize(
    "field,value",
    [
        ("GITHUB_ACTIONS", "false"),
        ("GITHUB_ACTOR", "other"),
        ("GITHUB_REF", "refs/heads/main"),
        ("GITHUB_RUN_ATTEMPT", "2"),
        ("GITHUB_SHA", "z" * 40),
    ],
)
def test_context_is_closed(prepared, field, value):
    raw, context = settings(prepared)
    context[field] = value
    with pytest.raises(ValueError):
        canary.authority(
            raw,
            "d" * 64,
            context,
            prepared[1],
            context["GITHUB_SHA"],
            "d" * 64,
            datetime(2026, 11, 6, tzinfo=timezone.utc),
        )


def test_disabled_cli_run_never_prepares_or_reads_key(tmp_path, monkeypatch):
    from argparse import Namespace

    def forbidden(*_args, **_kwargs):
        raise AssertionError("credential-private-sentinel")

    monkeypatch.setattr(canary, "worker", forbidden)
    args = Namespace(feed_file=tmp_path / "absent", scratch=tmp_path)
    assert asyncio.run(canary.run(args)) == {
        "ready": False,
        "outcome": "disabled",
        "request_entered": False,
    }


async def exercise(
    prepared,
    tmp_path,
    monkeypatch,
    *,
    gate_failure=False,
    grant_failure=False,
    is_byok=False,
    fate="nonpublish",
    transport_error=False,
    bad_permit=False,
    finish_unknown=False,
    publisher_unknown=False,
    cleanup_unknown=False,
    duplicate_field=None,
    sender_override=None,
    after_begin=None,
    custom_replayer=None,
):
    import httpx
    from scripts.rehearse_full_feed_canary import calibration, complete_body

    raw, context = settings(prepared)
    raw["output_fate"] = fate
    approved = canary.authority(
        raw,
        "d" * 64,
        context,
        prepared[1],
        "a" * 40,
        "d" * 64,
        ExecutionClock.now(timezone.utc),
    )
    events = []
    monkeypatch.setattr(canary, "source_fence", lambda _a: events.append("source"))

    class Body(httpx.AsyncByteStream):
        def __init__(self, value):
            self.value = value

        async def __aiter__(self):
            marker = (
                self.value.find(('"' + duplicate_field + '"').encode())
                if duplicate_field
                else -1
            )
            middle = marker + 4 if marker >= 0 else len(self.value) // 2
            yield self.value[:middle]
            yield self.value[middle:]

    response = json.loads(complete_body(calibration(prepared[1])))
    response["usage"]["is_byok"] = is_byok
    response_bytes = json.dumps(response).encode()
    if duplicate_field is not None:
        replacements = {
            "is_byok": (b'"is_byok": false', b'"is_byok": true, "is_byok": false'),
            "cost": (b'"cost": 0.044', b'"cost": 9.0, "cost": 0.044'),
            "model": (
                b'"model": "moonshotai/kimi-k3.1-pro"',
                b'"model": "wrong/identity", "model": "moonshotai/kimi-k3.1-pro"',
            ),
        }
        old, new = replacements[duplicate_field]
        assert old in response_bytes
        response_bytes = response_bytes.replace(old, new, 1)

    async def sender(request):
        events.append("post")
        assert request.content == prepared[1].wire
        if transport_error:
            raise httpx.ReadTimeout("credential-private-sentinel")
        if sender_override is not None:
            return await sender_override(request)
        return httpx.Response(200, stream=Body(response_bytes))

    async def control(request):
        events.append("fence")
        return httpx.Response(
            200,
            stream=Body(
                b"changed"
                if gate_failure
                else (canary.ROOT / "current-findings.json").read_bytes()
            ),
        )

    class Owner:
        blocked = False

        async def exchange(self, value):
            events.append(value["operation"])
            if value["operation"] == "begin":
                if grant_failure:
                    self.blocked = True
                    raise ValueError("credential-private-sentinel")
                if after_begin is not None:
                    after_begin()
                return {
                    "token": "unowned" if bad_permit else "b" * 32,
                    "attempt": 1,
                    "limit": 1,
                    "request_sha256": prepared[1].metadata["canonical_request_sha256"],
                }
            if value["operation"] == "finish":
                if finish_unknown:
                    self.blocked = True
                    raise ValueError("credential-private-sentinel")
                return {
                    "financial_settled": bool(
                        value["receipt"]
                        and value["receipt"]["costCoverage"] == "complete"
                    )
                }
            return {"recorded": True}

        def close(self):
            events.append("owner_close")
            if cleanup_unknown:
                raise ValueError("credential-private-sentinel")

    def read_key():
        events.append("key")
        return "synthetic-never-real"

    def publish(*_args):
        events.append("publish")
        if publisher_unknown:
            raise ValueError("credential-private-sentinel")
        return "c" * 40

    from scripts.canary_deadline import anchor_run
    import time

    budget = anchor_run(
        {
            "id": 800,
            "repository": {"full_name": context["GITHUB_REPOSITORY"]},
            "actor": {"login": "ricomanifesto"},
            "event": "workflow_dispatch",
            "head_sha": "a" * 40,
            "head_branch": canary.REF.removeprefix("refs/heads/"),
            "workflow_id": 406270829,
            "run_attempt": 1,
            "status": "in_progress",
            "created_at": "2026-11-06T03:04:05Z",
        },
        context,
        canary.DATE,
        now=ExecutionClock.now(timezone.utc),
        mono_ns=time.monotonic_ns(),
    )

    async def source_checker(approved, _deadline):
        canary.source_fence(approved)

    async def replayer(feed, expected, reply, permit, output, scratch, _deadline):
        from scripts.prepare_full_feed_canary import _prepare_owned, capture_environment
        from scripts.rehearse_full_feed_canary import ReplayPermit
        from scripts.rehearse_report_offline import (
            public_snapshot,
            compare_pages_package,
        )
        import shutil

        output.mkdir()
        for relative in public_snapshot(canary.ROOT):
            target = output / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(canary.ROOT / relative, target)
        with capture_environment(Path(os.environ["TIKTOKEN_CACHE_DIR"])):
            host = await _prepare_owned(
                feed,
                output,
                replay=reply,
                expected=expected,
                attempt_budget=ReplayPermit(permit),
            )
            if host["host_validated"]:
                compare_pages_package(output, scratch)
        return host

    async with (
        httpx.AsyncClient(transport=httpx.MockTransport(sender)) as outbound,
        httpx.AsyncClient(transport=httpx.MockTransport(control)) as inbound,
    ):
        result = await canary.execute(
            approved,
            prepared[0],
            prepared[1],
            tmp_path,
            owner_factory=lambda _a: Owner(),
            sender=outbound,
            control=inbound,
            key_reader=read_key,
            publisher=publish,
            budget=budget,
            source_checker=source_checker,
            replayer=custom_replayer or replayer,
        )
    assert "credential-private-sentinel" not in json.dumps(result)
    return events, result


@pytest.mark.parametrize("failure", ["gate_failure", "grant_failure"])
def test_pre_send_failure_never_reads_key_or_posts(
    prepared, tmp_path, monkeypatch, failure
):
    events, result = asyncio.run(
        exercise(prepared, tmp_path, monkeypatch, **{failure: True})
    )
    assert "key" not in events and "post" not in events and "publish" not in events
    assert result["request_entered"] is False


@pytest.mark.parametrize("is_byok", [True, None])
def test_unknown_or_upstream_billing_keeps_full_hold_and_never_promotes(
    prepared, tmp_path, monkeypatch, is_byok
):
    events, result = asyncio.run(
        exercise(
            prepared, tmp_path, monkeypatch, is_byok=is_byok, fate="conditional_publish"
        )
    )
    assert (
        events.count("post") == 1
        and events.count("begin") == 1
        and events.count("finish") == 1
    )
    assert "publish" not in events and "complete" not in events
    assert result["financial_state"] == "held_or_unknown"


@pytest.mark.parametrize("fate", ["nonpublish", "conditional_publish"])
def test_known_reply_uses_same_host_and_only_approved_fate(
    prepared, tmp_path, monkeypatch, fate
):
    events, result = asyncio.run(exercise(prepared, tmp_path, monkeypatch, fate=fate))
    assert (
        events.count("post") == 1
        and events.count("begin") == 1
        and events.count("finish") == 1
    )
    assert (
        events.index("begin")
        < events.index("key")
        < events.index("post")
        < events.index("finish")
    )
    assert result["host_validated"] is True and result["financial_state"] == "settled"
    assert events.count("publish") == int(fate == "conditional_publish")
    assert events[-2:] == ["complete", "owner_close"]
    assert result["serving_publication_verified"] is False


def test_transport_unknown_stops_once_without_retry_or_promotion(
    prepared, tmp_path, monkeypatch
):
    events, result = asyncio.run(
        exercise(
            prepared,
            tmp_path,
            monkeypatch,
            transport_error=True,
            fate="conditional_publish",
        )
    )
    assert (
        events.count("post") == 1
        and events.count("begin") == 1
        and events.count("finish") == 1
    )
    assert "publish" not in events and "complete" not in events
    assert result["financial_state"] == "held_or_unknown"


def test_malformed_permit_refuses_before_key_read(prepared, tmp_path, monkeypatch):
    events, result = asyncio.run(
        exercise(prepared, tmp_path, monkeypatch, bad_permit=True)
    )
    assert "key" not in events and "post" not in events and "publish" not in events
    assert result["request_entered"] is False


def test_unknown_finish_ack_is_not_retried_or_published(
    prepared, tmp_path, monkeypatch
):
    events, result = asyncio.run(
        exercise(
            prepared,
            tmp_path,
            monkeypatch,
            finish_unknown=True,
            fate="conditional_publish",
        )
    )
    assert events.count("post") == events.count("begin") == events.count("finish") == 1
    assert "publish" not in events and "complete" not in events
    assert result["financial_state"] == "held_or_unknown"


def test_unknown_publication_is_never_retried(prepared, tmp_path, monkeypatch):
    events, result = asyncio.run(
        exercise(
            prepared,
            tmp_path,
            monkeypatch,
            publisher_unknown=True,
            fate="conditional_publish",
        )
    )
    assert (
        events.count("post") == events.count("publish") == events.count("finish") == 1
    )
    assert "complete" not in events
    assert (
        result["report_commit"] is None and result["failure"] == "closed_check_refused"
    )


def test_cleanup_preserves_the_primary_send_failure(prepared, tmp_path, monkeypatch):
    events, result = asyncio.run(
        exercise(
            prepared, tmp_path, monkeypatch, transport_error=True, cleanup_unknown=True
        )
    )
    assert events.count("post") == 1 and result["phase"] == "send"
    assert result["secondary"] == ["owner_close_unknown"]


@pytest.mark.parametrize("field", ["is_byok", "cost", "model"])
def test_duplicate_response_keys_never_settle_or_promote(
    prepared, tmp_path, monkeypatch, field
):
    events, result = asyncio.run(
        exercise(
            prepared,
            tmp_path,
            monkeypatch,
            duplicate_field=field,
            fate="conditional_publish",
        )
    )
    assert events.count("post") == events.count("begin") == events.count("finish") == 1
    assert result["financial_state"] == "held_or_unknown"
    assert result["host_validated"] is False
    assert "publish" not in events and "complete" not in events


def test_cli_cleanup_preserves_disabled_observation(tmp_path, monkeypatch, capsys):
    original_worker = canary.worker

    async def fault(value, deadline):
        if value["mode"] == "cleanup":
            raise OSError("credential-private-sentinel")
        return await original_worker(value, deadline)

    monkeypatch.setattr(canary, "worker", fault)
    target = tmp_path / "receipt.json"
    monkeypatch.setattr(
        canary.sys,
        "argv",
        [
            "canary",
            "--preflight-only",
            "--feed-file",
            str(tmp_path / "absent"),
            "--expected-commit",
            "a" * 40,
            "--expected-manifest",
            "d" * 64,
            "--receipt",
            str(target),
        ],
    )
    with pytest.raises(SystemExit):
        canary.main()
    result = json.loads(target.read_text())
    assert result["outcome"] == "disabled" and result["request_entered"] is False
    assert result["secondary"] == ["scratch_cleanup_unknown"]
    captured = capsys.readouterr()
    assert (
        "credential-private-sentinel"
        not in captured.out + captured.err + target.read_text()
    )


@pytest.mark.parametrize("method", ["mkdir", "write_text"])
def test_cli_receipt_io_failure_is_safe_and_does_not_retry(
    tmp_path, monkeypatch, capsys, method
):
    calls = []

    def forbidden(*_args, **_kwargs):
        calls.append(method)
        raise OSError("credential-private-sentinel")

    async def failed_emit(*_args):
        forbidden()

    monkeypatch.setattr(canary, "emit_receipt", failed_emit)
    monkeypatch.setattr(
        canary.sys,
        "argv",
        [
            "canary",
            "--preflight-only",
            "--feed-file",
            str(tmp_path / "absent"),
            "--expected-commit",
            "a" * 40,
            "--expected-manifest",
            "d" * 64,
            "--receipt",
            str(tmp_path / "metadata.json"),
        ],
    )
    with pytest.raises(SystemExit) as stopped:
        canary.main()
    captured = capsys.readouterr()
    assert stopped.value.code == 1 and calls == [method]
    result = json.loads(captured.out)
    assert result["outcome"] == "disabled" and result["request_entered"] is False
    assert result["receipt_emission"] == "unknown"
    assert "credential-private-sentinel" not in captured.out + captured.err


def test_main_restores_exact_prior_logging_state(tmp_path, monkeypatch, capsys):
    import logging

    previous = logging.root.manager.disable
    logging.disable(logging.WARNING)
    monkeypatch.setattr(
        canary.sys,
        "argv",
        [
            "canary",
            "--preflight-only",
            "--feed-file",
            str(tmp_path / "absent"),
            "--expected-commit",
            "a" * 40,
            "--expected-manifest",
            "d" * 64,
            "--receipt",
            str(tmp_path / "metadata.json"),
        ],
    )
    try:
        canary.main()
        assert logging.root.manager.disable == logging.WARNING
    finally:
        logging.disable(previous)
    capsys.readouterr()
