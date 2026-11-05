"""Future fixed diagnostics only; all transmissions are synthetic MockTransport."""

import asyncio
import json

import httpx
import pytest

from scripts import execute_full_feed_canary as canary
from test_full_feed_canary_execution import (
    exercise,
    prepared as prepared,
    synthetic_clock as synthetic_clock,
)

SENTINEL = "credential-private-sentinel"


class Body(httpx.AsyncByteStream):
    def __init__(self, content=b"{}", *, error=None, close_error=None):
        self.content, self.error, self.close_error = content, error, close_error

    async def __aiter__(self):
        if self.error is not None:
            raise self.error
        yield self.content

    async def aclose(self):
        if self.close_error is not None:
            raise self.close_error


@pytest.mark.parametrize(
    "fault,expected",
    [
        ("http", "http_unauthorized"),
        ("timeout", "send_read_timeout"),
        ("network", "send_connect_error"),
        ("decode", "response_decode_refused"),
        ("cancel", "send_cancelled"),
        ("unknown", "send_unknown_failure"),
        ("dual_close", "http_unauthorized"),
        ("accounting", "accounting_refused"),
    ],
)
def test_actual_execute_retains_bounded_failure_and_full_hold(
    prepared, tmp_path, monkeypatch, capsys, fault, expected
):
    async def sender(_request):
        if fault == "timeout":
            raise httpx.ReadTimeout(SENTINEL)
        if fault == "network":
            raise httpx.ConnectError(SENTINEL)
        if fault == "cancel":
            raise asyncio.CancelledError(SENTINEL)
        if fault == "unknown":
            raise RuntimeError(SENTINEL)
        if fault == "accounting":
            from scripts.rehearse_full_feed_canary import complete_body, calibration

            value = json.loads(complete_body(calibration(prepared[1])))
            del value["usage"]["cost"]
            return httpx.Response(200, stream=Body(json.dumps(value).encode()))
        return httpx.Response(
            401 if fault in {"http", "dual_close"} else 200,
            stream=Body(
                SENTINEL.encode(),
                close_error=RuntimeError(SENTINEL) if fault == "dual_close" else None,
            ),
            headers={"X-Private": SENTINEL},
        )

    events, result = asyncio.run(
        exercise(prepared, tmp_path, monkeypatch, sender_override=sender)
    )
    assert result["failure"] == expected
    assert result["request_entered"] is True and result["accounting"] is None
    assert (
        result["financial_state"] == "held_or_unknown"
        and result["report_commit"] is None
    )
    assert events.count("post") == events.count("begin") == events.count("finish") == 1
    assert "publish" not in events and "complete" not in events
    captured = capsys.readouterr()
    retained = "".join(
        p.read_text(errors="replace") for p in tmp_path.rglob("*") if p.is_file()
    )
    assert SENTINEL not in json.dumps(result) + captured.out + captured.err + retained


@pytest.mark.parametrize(
    "status,expected",
    [
        (301, "http_redirect"),
        (401, "http_unauthorized"),
        (402, "http_payment_required"),
        (403, "http_forbidden"),
        (404, "http_not_found"),
        (408, "http_timeout_status"),
        (429, "http_rate_limited"),
        (422, "http_client_error"),
        (503, "http_server_error"),
        (201, "http_unexpected_status"),
    ],
)
def test_known_http_status_categories_never_inspect_error_body(status, expected):
    calls = []

    async def sender(request):
        calls.append(request)
        return httpx.Response(status, stream=Body(error=AssertionError(SENTINEL)))

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(sender)) as client:
            await canary.post_once(client, b"fixed synthetic wire", "synthetic key")

    with pytest.raises(ValueError) as failure:
        asyncio.run(run())
    assert getattr(failure.value, "code", None) == expected and len(calls) == 1
    assert SENTINEL not in str(failure.value)


@pytest.mark.parametrize(
    "error,expected",
    [
        (httpx.ConnectTimeout(SENTINEL), "send_connect_timeout"),
        (httpx.ReadTimeout(SENTINEL), "send_read_timeout"),
        (httpx.WriteTimeout(SENTINEL), "send_write_timeout"),
        (httpx.PoolTimeout(SENTINEL), "send_pool_timeout"),
        (httpx.ConnectError(SENTINEL), "send_connect_error"),
        (httpx.ReadError(SENTINEL), "send_read_error"),
        (httpx.WriteError(SENTINEL), "send_write_error"),
        (httpx.RemoteProtocolError(SENTINEL), "send_protocol_error"),
        (TimeoutError(SENTINEL), "send_timeout_unknown"),
        (RuntimeError(SENTINEL), "send_unknown_failure"),
        (asyncio.CancelledError(SENTINEL), "send_cancelled"),
        (httpx.TimeoutException(SENTINEL), "send_timeout"),
        (httpx.NetworkError(SENTINEL), "send_network_error"),
        (httpx.TransportError(SENTINEL), "send_transport_error"),
        (httpx.DecodingError(SENTINEL), "response_decode_failed"),
        (httpx.CloseError(SENTINEL), "response_close_failed"),
    ],
)
def test_transport_faults_are_fixed_not_exception_text(error, expected):
    calls = []

    async def sender(request):
        calls.append(request)
        raise error

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(sender)) as client:
            await canary.post_once(client, b"fixed synthetic wire", "synthetic key")

    with pytest.raises(ValueError) as failure:
        asyncio.run(run())
    assert getattr(failure.value, "code", None) == expected and len(calls) == 1
    assert SENTINEL not in str(failure.value)


@pytest.mark.parametrize(
    "fault,expected",
    [
        ("encoding", "response_encoding_refused"),
        ("size", "response_body_limit"),
        ("close", "response_close_failed"),
        ("dual", "http_unauthorized"),
        ("unknown_close", "send_unknown_failure"),
    ],
)
def test_response_boundaries_and_cleanup_primary_precedence(fault, expected):
    calls = []

    async def sender(request):
        calls.append(request)
        return httpx.Response(
            401 if fault == "dual" else 200,
            stream=Body(
                b"x" * (2 * 1024 * 1024 + 1) if fault == "size" else b"{}",
                close_error=(
                    httpx.CloseError(SENTINEL)
                    if fault == "close"
                    else (
                        RuntimeError(SENTINEL)
                        if fault in {"unknown_close", "dual"}
                        else None
                    )
                ),
            ),
            headers=(
                {"content-encoding": "private-encoding"} if fault == "encoding" else {}
            ),
        )

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(sender)) as client:
            await canary.post_once(client, b"fixed synthetic wire", "synthetic key")

    with pytest.raises(ValueError) as failure:
        asyncio.run(run())
    assert getattr(failure.value, "code", None) == expected and len(calls) == 1
    assert getattr(failure.value, "secondary", ()) == (
        ("response_close_unknown",) if fault == "dual" else ()
    )
    assert SENTINEL not in str(failure.value)


def test_only_the_owned_expired_window_is_labeled_deadline(monkeypatch):
    original = asyncio.timeout_at
    configured = []

    def expire(value):
        configured.append(value - asyncio.get_running_loop().time())
        return original(0)

    monkeypatch.setattr(canary.asyncio, "timeout_at", expire)

    async def sender(_request):
        await asyncio.sleep(0)
        raise AssertionError("unreachable")

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(sender)) as client:
            await canary.post_once(client, b"fixed synthetic wire", "synthetic key")

    with pytest.raises(ValueError) as failure:
        asyncio.run(run())
    assert getattr(failure.value, "code", None) == "send_deadline_exceeded"
    assert len(configured) == 1 and 1599 < configured[0] <= 1600
