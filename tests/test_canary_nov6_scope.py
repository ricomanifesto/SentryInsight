"""Replacement scope is proposed only; historical Nov6 source stays preserved."""

from datetime import datetime, timezone
import json
from pathlib import Path

import pytest

from scripts import execute_full_feed_canary as canary
from test_full_feed_canary_execution import prepared as prepared, settings


def test_replacement_uses_original_pilot_start_not_a_new_opening(prepared, monkeypatch):
    raw, context = settings(prepared)
    raw["execution_date"] = "2026-11-05"
    monkeypatch.setattr(canary, "DATE", "2026-11-05")
    approved = canary.authority(
        raw,
        "d" * 64,
        context,
        prepared[1],
        "a" * 40,
        "d" * 64,
        datetime(2026, 11, 5, tzinfo=timezone.utc),
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
            datetime(2026, 11, 5, tzinfo=timezone.utc),
        )


def test_replacement_manifest_explicitly_supersedes_next_day_scope():
    value = json.loads(Path("config/full-feed-canary.json").read_bytes())
    assert value["execution_date"] == "2026-11-05" and value["enabled"] is True
    assert value["metadata_audience_approved"] is True
    assert (
        value["data_approval_sha256"]
        == "840fe520c883c8cb92929b7285f90feed8b008512386a05a4265fa456374cba5"
    )
    assert value["pilot"]["activationStart"] == "2026-11-05T00:00:00.000Z"
    assert (
        value["pilot"]["opening"]["basisSha256"]
        == "f6f4a755142ca658dcc2d9abdf830a456515ffe51f51de9ee057b4862228f9c7"
    )


def test_replacement_capture_changes_only_legacy_processing_day_not_feed_or_wire(
    prepared, tmp_path
):
    import asyncio
    from unittest.mock import patch
    from scripts import prepare_full_feed_canary as capture

    class PriorClock(datetime):
        @classmethod
        def now(cls, tz=None):
            value = cls(2026, 11, 6, 12, tzinfo=timezone.utc)
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
        == "49249448a22817be7864e77413510cc72fbbb93f3aeaafd2a71dec8535b12407"
    )
    assert (
        capture.sha(current.pack)
        == "b74eb002a01d5676653ea06f4336e968f2fb012f3e78555b33ebaa5ce6808ce9"
    )
    old_pack, new_pack = json.loads(prior.pack), json.loads(current.pack)
    assert len(old_pack["articles"]) == len(new_pack["articles"]) == 30
    for before, after in zip(old_pack["articles"], new_pack["articles"], strict=True):
        assert before.pop("date") == "2026-11-06"
        assert after.pop("date") == "2026-11-05"
    assert old_pack == new_pack


def test_exact_replacement_payload_and_target_are_hash_pinned():
    import hashlib

    # Frozen proposed data/target fields; runtime tests require no Git ancestor
    # fetch. Approval flags alone cannot alter these pinned fields.
    for relative, excluded, expected in (
        (
            "config/full-feed-canary.json",
            ["data_approval_sha256", "enabled", "metadata_audience_approved"],
            "c893f2940305b2767914e368337c92fbf108e51b558b69fa9487336384c3d9f9",
        ),
        (
            "config/original-canary-readmission.json",
            ["approval_scope_sha256", "enabled"],
            "0bc594c961358a98dd98097b1e2e301e1d994b9bfab7b4d532e3009eb47d6a8f",
        ),
    ):
        value = json.loads(Path(relative).read_bytes())
        retained = {key: item for key, item in value.items() if key not in excluded}
        raw = json.dumps(retained, sort_keys=True, separators=(",", ":")).encode()
        assert hashlib.sha256(raw).hexdigest() == expected
        assert value["enabled"] is True


@pytest.mark.parametrize(
    "field,value",
    [
        ("original_run_id", "901"),
        ("original_day", "2026-11-06"),
        ("original_source", "b" * 40),
        ("prior_history_sha256", "b" * 64),
        ("prior_record_count", 11),
        ("original_daily_sha256", "b" * 64),
        ("supersedes_manifest_sha256", "b" * 64),
        ("version", True),
        ("extra", "unowned"),
    ],
)
def test_replacement_identity_corruption_refuses_before_any_adapter(
    prepared, field, value
):
    raw, context = settings(prepared)
    raw["daily_replacement"][field] = value
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


def test_replacement_cannot_run_on_the_previously_approved_next_day(prepared):
    raw, context = settings(prepared)
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
