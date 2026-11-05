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
        return cls(2026, 11, 5, 3, 4, 5, tzinfo=timezone.utc)


class FrozenInputs(tuple):
    def __repr__(self):
        return "<closed public source packet>"


@pytest.fixture(autouse=True)
def synthetic_clock(monkeypatch):
    from src.core import reviewed_report

    monkeypatch.setattr(canary, "datetime", ExecutionClock)
    monkeypatch.setattr(reviewed_report, "datetime", ExecutionClock)


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
            datetime(2026, 11, 5, tzinfo=timezone.utc),
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
            datetime(2026, 11, 5, tzinfo=timezone.utc),
        )


def test_disabled_cli_run_never_prepares_or_reads_key(tmp_path, monkeypatch):
    from argparse import Namespace

    def forbidden(*_args, **_kwargs):
        raise AssertionError("credential-private-sentinel")

    monkeypatch.setattr(canary, "prepare", forbidden)
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
            yield self.value

    response = json.loads(complete_body(calibration(prepared[1])))
    response["usage"]["is_byok"] = is_byok

    async def sender(request):
        events.append("post")
        assert request.content == prepared[1].wire
        if transport_error:
            raise httpx.ReadTimeout("credential-private-sentinel")
        return httpx.Response(200, stream=Body(json.dumps(response).encode()))

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


def test_cli_cleanup_preserves_disabled_observation(tmp_path, monkeypatch, capsys):
    class Scratch:
        name = str(tmp_path / "scratch")

        def cleanup(self):
            raise ValueError("credential-private-sentinel")

    monkeypatch.setattr(
        canary.tempfile, "TemporaryDirectory", lambda **_kwargs: Scratch()
    )
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
