"""Durable checkpoint store: atomic writes, chained ledger, lease fencing
and the crash-consistent reservation decision."""

import json
import os
import subprocess
import sys
import textwrap

import pytest

from src.runtime_adapter.checkpoint import (
    CheckpointStateStale,
    CheckpointStore,
    CheckpointStoreError,
    ReservationRefused,
    StageRegression,
    StaleLeaseWrite,
    TerminalJob,
    ledger_view,
)

JOB = "a" * 64
KEY = "sentryinsight/exploitation-report/v1/" + JOB
REQUEST = "b" * 64


def store_with_lease(tmp_path, lease_version=1, **kwargs):
    store = CheckpointStore(tmp_path / "store", **kwargs)
    store.create_job(JOB, KEY)
    store.record_run(JOB, "run-1")
    store.record_lease(JOB, "run-1", lease_version, attempt=lease_version, now=100)
    return store


def reserve(store, lease_version=1, now=100):
    return store.reserve(JOB, lease_version, request_sha256=REQUEST, now=now, budget=3)


def resolve(store, seq, lease_version=1, **fields):
    outcome = {"disposition": "resolved", "http_status": 503, "received_at": 100}
    outcome.update(fields)
    store.record_outcome(JOB, lease_version, seq, outcome)


def test_admission_is_idempotent_and_survives_a_fresh_instance(tmp_path):
    store = CheckpointStore(tmp_path)
    first = store.create_job(JOB, KEY)
    second = store.create_job(JOB, KEY)

    reopened = CheckpointStore(tmp_path).load(JOB)
    assert first == second == reopened
    assert reopened["stage"] == "admitted"
    assert ledger_view(reopened).reserved == 0
    assert CheckpointStore(tmp_path).job_ids() == [JOB]


def test_reservation_is_one_write_and_blocks_a_second_open_intent(tmp_path):
    store = store_with_lease(tmp_path)

    seq = reserve(store)
    view = ledger_view(CheckpointStore(tmp_path / "store").load(JOB))

    assert view.reserved == 1
    assert view.open_reservations == [seq]
    with pytest.raises(ReservationRefused) as raised:
        reserve(store)
    assert raised.value.reason == "provider_intent_unresolved"
    assert ledger_view(store.load(JOB)).reserved == 1


def test_ambiguous_disposition_blocks_every_later_reservation(tmp_path):
    store = store_with_lease(tmp_path)
    seq = reserve(store)
    store.record_outcome(
        JOB, 1, seq, {"disposition": "ambiguous", "fault": "read_timeout"}
    )
    store.record_lease(JOB, "run-1", 2, attempt=2, now=200)

    with pytest.raises(ReservationRefused) as raised:
        reserve(store, lease_version=2)

    assert raised.value.reason == "provider_intent_unresolved"
    assert ledger_view(store.load(JOB)).ambiguous_reservations == [seq]


def test_budget_is_derived_from_ledger_and_never_exceeded(tmp_path):
    store = store_with_lease(tmp_path)
    for _ in range(3):
        resolve(store, reserve(store))

    with pytest.raises(ReservationRefused) as raised:
        reserve(store)

    assert raised.value.reason == "provider_budget_exhausted"
    view = ledger_view(store.load(JOB))
    assert view.reserved == 3
    assert view.resolved == 3


def test_not_before_is_enforced_at_the_reservation_decision(tmp_path):
    store = store_with_lease(tmp_path)
    resolve(store, reserve(store), not_before=160)

    with pytest.raises(ReservationRefused) as raised:
        reserve(store, now=159)
    assert raised.value.reason == "provider_retry_after_deferred"
    reserve(store, now=160)
    assert ledger_view(store.load(JOB)).reserved == 2
    assert ledger_view(store.load(JOB)).not_before == 160


def test_failed_before_forward_keeps_the_charge_and_permits_the_next_send(tmp_path):
    store = store_with_lease(tmp_path)
    first = reserve(store)
    store.record_outcome(
        JOB, 1, first, {"disposition": "failed_before_forward", "fault": "connect"}
    )

    second = reserve(store)

    view = ledger_view(store.load(JOB))
    assert [entry["seq"] for entry in view.reservations] == [first, second]
    assert view.reserved == 2
    assert view.failed_before_forward == [first]


def test_lease_versions_are_monotonic_and_fence_stale_product_writes(tmp_path):
    store = store_with_lease(tmp_path)
    stale_seq = reserve(store)
    store.record_lease(JOB, "run-1", 2, attempt=2, now=200)
    store.record_lease(JOB, "run-1", 2, attempt=2, now=200)

    with pytest.raises(StaleLeaseWrite):
        store.record_lease(JOB, "run-1", 1, attempt=1, now=300)
    for write in (
        lambda: reserve(store, lease_version=1),
        lambda: store.advance(JOB, 1, "analyzed", analysis={"sha256": "x"}),
        lambda: store.record_disposition(JOB, 1, {"reason": "x", "terminal": True}),
        lambda: store.set_pending_action(JOB, 1, {"kind": "complete"}),
        lambda: store.record_publication(JOB, 1, {"state": "intent"}),
        lambda: store.append(JOB, 1, {"type": "refusal", "reason": "x"}),
    ):
        with pytest.raises(StaleLeaseWrite):
            write()

    store.record_outcome(
        JOB, 2, stale_seq, {"disposition": "ambiguous", "fault": "no_disposition"}
    )
    # The stale opener may still append its own reservation's outcome.
    resolve(store, stale_seq, lease_version=1, http_status=200)

    record = store.load(JOB)
    view = ledger_view(record)
    assert record["highest_lease_version"] == 2
    assert view.disposition(stale_seq) == "ambiguous"
    assert [entry["disposition"] for entry in view.outcomes(stale_seq)] == [
        "ambiguous",
        "resolved",
    ]
    assert record["stage"] == "claimed"


def test_stale_writer_cannot_record_outcome_for_a_newer_reservation(tmp_path):
    store = store_with_lease(tmp_path)
    store.record_lease(JOB, "run-1", 2, attempt=2, now=200)
    newer = reserve(store, lease_version=2)

    with pytest.raises(StaleLeaseWrite):
        resolve(store, newer, lease_version=1)


def test_stage_is_monotonic_and_terminal_dispositions_are_sticky(tmp_path):
    store = store_with_lease(tmp_path)
    store.advance(JOB, 1, "analyzed", analysis={"sha256": "x"})

    with pytest.raises(StageRegression):
        store.advance(JOB, 1, "claimed")

    store.record_disposition(
        JOB, 1, {"reason": "report_grounding_rejected", "terminal": True}
    )
    store.record_lease(JOB, "run-1", 2, attempt=2, now=200)
    with pytest.raises(TerminalJob):
        store.advance(JOB, 2, "artifact_prepared", artifact={"sha256": "y"})
    with pytest.raises(TerminalJob):
        store.record_disposition(
            JOB, 2, {"reason": "provider_transient_response", "terminal": False}
        )
    with pytest.raises(TerminalJob):
        reserve(store, lease_version=2)

    record = store.load(JOB)
    assert record["disposition"]["reason"] == "report_grounding_rejected"
    assert record["stage"] == "analyzed"


def tamper(tmp_path, change):
    path = tmp_path / "store" / "jobs" / JOB / "record.json"
    record = json.loads(path.read_text())
    change(record)
    path.write_text(json.dumps(record))


@pytest.mark.parametrize(
    "change",
    [
        lambda record: record["ledger"][0].update(request_sha256="c" * 64),
        lambda record: record["ledger"].pop(0),
        lambda record: record["ledger"].reverse(),
        lambda record: record["ledger"][1].update(chain="0" * 64),
    ],
    ids=["edited", "middle_removed", "reordered", "chain_overwritten"],
)
def test_ledger_chain_break_is_rejected_as_stale(tmp_path, change):
    store = store_with_lease(tmp_path)
    resolve(store, reserve(store))
    reserve(store)

    tamper(tmp_path, change)

    with pytest.raises(CheckpointStateStale):
        store.load(JOB)


def test_valid_prefix_truncation_is_not_detected_by_the_chain_alone(tmp_path):
    # A hash chain cannot detect removal of a valid suffix.
    store = store_with_lease(tmp_path)
    resolve(store, reserve(store))
    reserve(store)

    tamper(tmp_path, lambda record: record["ledger"].pop())

    assert ledger_view(store.load(JOB)).reserved == 1


def test_corrupt_record_is_rejected_as_stale(tmp_path):
    store = store_with_lease(tmp_path)
    (tmp_path / "store" / "jobs" / JOB / "record.json").write_text("{not json")

    with pytest.raises(CheckpointStateStale):
        store.load(JOB)


def test_failed_reservation_write_is_not_durable(tmp_path):
    def fail_reservations(kind):
        if kind == "reservation":
            raise OSError("simulated disk failure")

    store = store_with_lease(tmp_path, fault=fail_reservations)

    with pytest.raises(CheckpointStoreError) as raised:
        reserve(store)

    assert raised.value.reason == "checkpoint_store_failed"
    assert ledger_view(CheckpointStore(tmp_path / "store").load(JOB)).reserved == 0


def test_crash_during_replace_leaves_the_previous_record(tmp_path, monkeypatch):
    store = store_with_lease(tmp_path)
    before = store.load(JOB)

    def crash(*_args, **_kwargs):
        raise OSError("simulated crash before rename")

    monkeypatch.setattr(os, "replace", crash)
    with pytest.raises(CheckpointStoreError):
        reserve(store)
    monkeypatch.undo()

    assert store.load(JOB) == before
    leftovers = [
        path.name
        for path in (tmp_path / "store" / "jobs" / JOB).iterdir()
        if path.name.endswith(".tmp")
    ]
    assert leftovers == []


def test_private_blobs_are_content_addressed_and_verified(tmp_path):
    store = store_with_lease(tmp_path)
    digest = store.put_blob(JOB, b"captured body")

    assert store.get_blob(JOB, digest) == b"captured body"
    store.blob_path(JOB, digest).write_bytes(b"corrupted body")
    with pytest.raises(CheckpointStateStale):
        store.get_blob(JOB, digest)
    with pytest.raises(CheckpointStateStale):
        store.get_blob(JOB, "../" + digest)


def test_concurrent_processes_cannot_open_two_reservations(tmp_path):
    store = store_with_lease(tmp_path)
    script = textwrap.dedent(f"""
        import sys
        from pathlib import Path
        from src.runtime_adapter.checkpoint import CheckpointStore, ReservationRefused
        store = CheckpointStore(Path(sys.argv[1]))
        try:
            store.reserve({JOB!r}, 1, request_sha256={REQUEST!r}, now=100, budget=3)
            print("reserved")
        except ReservationRefused as refused:
            print(refused.reason)
        """)
    processes = [
        subprocess.Popen(
            [sys.executable, "-c", script, str(tmp_path / "store")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for _ in range(4)
    ]
    results = []
    for process in processes:
        stdout, stderr = process.communicate(timeout=60)
        assert process.returncode == 0, stderr
        results.append(stdout.strip())

    assert sorted(results) == ["provider_intent_unresolved"] * 3 + ["reserved"]
    assert ledger_view(store.load(JOB)).reserved == 1
