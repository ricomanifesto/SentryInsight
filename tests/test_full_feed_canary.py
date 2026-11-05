"""Closed frozen-feed capture; no provider or article request is permitted."""

import asyncio
import os
from pathlib import Path
import pytest
from scripts.prepare_full_feed_canary import prepare, verify_feed


def test_feed_mutation_refuses_before_host_or_transport():
    with pytest.raises(ValueError, match="Closed canary refused"):
        verify_feed(b"<rss>different source</rss>")


def test_actual_frozen_full_feed_uses_actual_prompt_and_quarantine(tmp_path):
    feed = os.environ.get("SENTRY_FROZEN_FEED")
    if not feed:
        pytest.skip(
            "Exact external public feed packet is supplied for canary preparation"
        )
    value = asyncio.run(prepare(Path(feed).read_bytes(), tmp_path))
    assert value.metadata["input_sources"] == 30
    assert value.metadata["eligible_sources"] == 25
    assert value.metadata["held_sources"] == 5
    assert value.metadata["mock_capture_requests"] == 1
    assert value.metadata["external_requests"] == 0
    assert value.metadata["source_pack_sha256"]
    assert value.metadata["wire_sha256"]
    assert value.metadata["max_tokens"] == 32000
    assert value.metadata["published"] is False
    assert value.metadata["output_fate"] == "approval_required_before_any_real_send"


@pytest.mark.parametrize("override", ["openrouter/unapproved/paid", "opencode/unowned"])
def test_ambient_credentials_model_gateway_and_tracing_cannot_escape_capture(
    tmp_path, monkeypatch, override
):
    feed = os.environ.get("SENTRY_FROZEN_FEED")
    if not feed:
        pytest.skip("Exact external public packet required")
    import httpx
    from src.core.opencode_client import OpenCodeClient

    entries = []

    async def forbidden(*_args, **_kwargs):
        entries.append("real_transport")
        raise AssertionError("hostile-synthetic-secret-never-output")

    monkeypatch.setattr(httpx.AsyncHTTPTransport, "handle_async_request", forbidden)
    monkeypatch.setattr(OpenCodeClient, "generate", forbidden)
    hostile = {
        "SENTRYINSIGHT_MODEL": override,
        "OPENROUTER_API_KEY": "hostile-synthetic-secret-never-output",
        "OPENCODE_SERVER_URL": "https://hostile.invalid",
        "OTEL_EXPORTER_OTLP_ENDPOINT": "https://hostile.invalid",
        "LOGFIRE_TOKEN": "hostile-synthetic-secret-never-output",
        "LANGSMITH_API_KEY": "hostile-synthetic-secret-never-output",
        "LANGSMITH_TRACING": "true",
        "PYTHONPATH": "/hostile-untrusted",
    }
    for name, value in hostile.items():
        monkeypatch.setenv(name, value)
    result = asyncio.run(prepare(Path(feed).read_bytes(), tmp_path))
    assert entries == []
    assert result.metadata["mock_capture_requests"] == 1
    assert result.metadata["external_requests"] == 0
    assert b"hostile" not in result.wire
    assert "hostile" not in str(result.metadata)
    assert os.environ["OPENROUTER_API_KEY"] == hostile["OPENROUTER_API_KEY"]


def test_current_path_denies_real_http_and_socket_even_with_hostile_environment(
    monkeypatch,
):
    import httpx
    import socket
    from scripts.prepare_full_feed_canary import capture_environment

    monkeypatch.setenv("OPENROUTER_API_KEY", "hostile-synthetic-secret")
    cache = Path(os.environ["TIKTOKEN_CACHE_DIR"])
    with capture_environment(cache):
        assert "OPENROUTER_API_KEY" not in os.environ
        assert "SENTRYINSIGHT_MODEL" not in os.environ
        assert "HOME" not in os.environ
        assert os.environ["OTEL_SDK_DISABLED"] == "true"
        with pytest.raises(ValueError, match="Closed canary refused"):
            socket.create_connection(("hostile.invalid", 443))
        with httpx.Client(trust_env=False) as client:
            with pytest.raises(ValueError, match="Closed canary refused"):
                client.get("https://hostile.invalid")
