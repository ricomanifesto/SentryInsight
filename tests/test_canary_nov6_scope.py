"""A fresh fixed-snapshot scope is inert; the old pilot identity never moves."""

from datetime import datetime, timezone
import json
from pathlib import Path

import pytest

from scripts import execute_full_feed_canary as canary
from test_full_feed_canary_execution import prepared as prepared, settings


def test_next_day_uses_original_pilot_start_not_a_new_opening(prepared, monkeypatch):
    raw, context = settings(prepared)
    raw["execution_date"] = "2026-11-06"
    monkeypatch.setattr(canary, "DATE", "2026-11-06")
    approved = canary.authority(
        raw,
        "d" * 64,
        context,
        prepared[1],
        "a" * 40,
        "d" * 64,
        datetime(2026, 11, 6, tzinfo=timezone.utc),
    )
    assert approved.manifest["pilot"]["activationStart"] == "2026-11-05T00:00:00.000Z"
    assert approved.manifest["whole_hold_microusd"] == 7251456
    raw["pilot"]["activationStart"] = "2026-11-06T00:00:00.000Z"
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


def test_future_manifest_cannot_reuse_old_execution_authority():
    value = json.loads(Path("config/full-feed-canary.json").read_bytes())
    assert value["execution_date"] == "2026-11-06" and value["enabled"] is False
    assert value["metadata_audience_approved"] is False
    assert value["data_approval_sha256"] is None
    assert value["pilot"]["activationStart"] == "2026-11-05T00:00:00.000Z"
    assert (
        value["pilot"]["opening"]["basisSha256"]
        == "f6f4a755142ca658dcc2d9abdf830a456515ffe51f51de9ee057b4862228f9c7"
    )


def test_rederived_pack_changes_only_legacy_processing_date_not_feed_or_wire(
    prepared, tmp_path
):
    import asyncio
    from unittest.mock import patch
    from scripts import prepare_full_feed_canary as capture

    class PriorClock(datetime):
        @classmethod
        def now(cls, tz=None):
            value = cls(2026, 11, 5, 12, tzinfo=timezone.utc)
            return value if tz is not None else value.replace(tzinfo=None)

    with patch.object(capture, "FixedClock", PriorClock):
        prior = asyncio.run(capture.prepare(prepared[0], tmp_path / "prior"))
    current = prepared[1]
    assert prior.wire == current.wire
    assert (
        capture.sha(current.wire)
        == "a260b0a92a35926c8201e80c9b44fd4edbeb84c00b05f600c1856de57a4ca440"
    )
    assert (
        capture.sha(prior.pack)
        == "b74eb002a01d5676653ea06f4336e968f2fb012f3e78555b33ebaa5ce6808ce9"
    )
    assert (
        capture.sha(current.pack)
        == "49249448a22817be7864e77413510cc72fbbb93f3aeaafd2a71dec8535b12407"
    )
    old_pack, new_pack = json.loads(prior.pack), json.loads(current.pack)
    assert len(old_pack["articles"]) == len(new_pack["articles"]) == 30
    for before, after in zip(old_pack["articles"], new_pack["articles"], strict=True):
        assert before.pop("date") == "2026-11-05"
        assert after.pop("date") == "2026-11-06"
    assert old_pack == new_pack
