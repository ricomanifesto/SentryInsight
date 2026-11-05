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
