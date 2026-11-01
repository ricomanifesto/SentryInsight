"""Snapshot reads enforce the same bounds and generation limits as freeze.

A digest-valid manifest written without ``freeze`` is refused by
``materialize``, by admission and by the worker on every claim, including a
recovery claim, so an oversized or misconfigured job never reaches the
provider.
"""

import asyncio
import json

import pytest

from src.core.content_fingerprint import compute_articles_fingerprint
from src.runtime_adapter.fakes import Respond
from src.runtime_adapter.harness import Harness
from src.runtime_adapter.identity import (
    PRODUCT,
    WORKFLOW_NAME,
    WORKFLOW_VERSION,
    canonical_json,
    idempotency_key,
    input_ref,
    sha256_hex,
)
from src.runtime_adapter.snapshot import (
    MAX_RECORDS,
    MAX_TOTAL_BYTES,
    FrozenJob,
    SnapshotRejected,
    materialize,
)
from src.runtime_adapter.synthetic import (
    completion_body,
    synthetic_articles,
    synthetic_config,
)
from src.runtime_adapter.worker import admit

OK = Respond(200, completion_body())
PROMOTION = {
    "title": "[Virtual Event] Synthetic webinar",
    "link": "https://example.test/webinar",
    "source": "Example Source",
    "content": "Register now.",
}


def large_record():
    return dict(synthetic_articles()[0], content="x" * 63_000)


def oversized_articles():
    record = large_record()
    copies = MAX_TOTAL_BYTES // len(canonical_json(record)) + 1
    assert copies <= MAX_RECORDS
    return [record] * copies


def crafted(harness, *, articles=None, generation=None):
    """Write a digest-valid manifest without ``freeze``; return it as a job."""
    job = harness.freeze()
    manifest = json.loads(json.dumps(job.manifest))
    if articles is not None:
        for article in articles:
            harness.snapshots.put(canonical_json(article))
        manifest["records"] = [sha256_hex(canonical_json(a)) for a in articles]
        manifest["articles_fingerprint"] = compute_articles_fingerprint(articles)
    if generation is not None:
        manifest["generation"].update(generation)
    digest = harness.snapshots.put(canonical_json(manifest))
    return FrozenJob(digest, manifest, job.articles if articles is None else articles)


def submit_raw(harness, job):
    """Submit a reference the way a foreign or older producer could."""
    run, _ = asyncio.run(
        harness.runtime().submit(
            product=PRODUCT,
            workflow_name=WORKFLOW_NAME,
            workflow_version=WORKFLOW_VERSION,
            idempotency_key=idempotency_key(job.manifest_digest),
            input_ref=input_ref(job.manifest_digest),
            max_attempts=3,
        )
    )
    return run


INVALID = {
    "too_many_records": (
        dict(articles=[synthetic_articles()[0]] * (MAX_RECORDS + 1)),
        "snapshot_invalid",
    ),
    "aggregate_bytes": (dict(articles=oversized_articles()), "snapshot_invalid"),
    "excluded_promotion": (
        dict(articles=synthetic_articles() + [PROMOTION]),
        "snapshot_invalid",
    ),
    "zero_max_tokens": (dict(generation={"max_tokens": 0}), "effective_config_invalid"),
    "negative_max_tokens": (
        dict(generation={"max_tokens": -1}),
        "effective_config_invalid",
    ),
    "zero_input_tokens": (
        dict(generation={"max_input_tokens": 0}),
        "effective_config_invalid",
    ),
    "negative_input_tokens": (
        dict(generation={"max_input_tokens": -5}),
        "effective_config_invalid",
    ),
    "unsupported_model": (
        dict(generation={"model": "anthropic/x"}),
        "effective_config_invalid",
    ),
}


@pytest.mark.parametrize("case", sorted(INVALID))
def test_materialize_applies_the_freeze_constraints(tmp_path, case):
    harness = Harness(tmp_path / "world", [OK])
    changes, reason = INVALID[case]
    job = crafted(harness, **changes)

    with pytest.raises(SnapshotRejected) as raised:
        materialize(harness.snapshots, job.manifest_digest)

    assert raised.value.reason == reason


@pytest.mark.parametrize(
    "articles, config, reason",
    [
        ([synthetic_articles()[0]] * (MAX_RECORDS + 1), None, "snapshot_invalid"),
        (oversized_articles(), None, "snapshot_invalid"),
        (None, synthetic_config(max_tokens=0), "effective_config_invalid"),
        (None, synthetic_config(max_input_tokens=0), "effective_config_invalid"),
    ],
)
def test_freeze_refuses_the_same_inputs(tmp_path, articles, config, reason):
    harness = Harness(tmp_path / "world", [OK])

    with pytest.raises(SnapshotRejected) as raised:
        harness.freeze(articles=articles, config=config)

    assert raised.value.reason == reason


def test_frozen_snapshot_still_materializes_at_the_limits(tmp_path):
    harness = Harness(tmp_path / "world", [OK])
    record = large_record()
    limit = MAX_TOTAL_BYTES // len(canonical_json(record))
    job = harness.freeze(
        articles=[record] * limit,
        config=synthetic_config(max_tokens=1, max_input_tokens=1),
    )

    loaded = materialize(harness.snapshots, job.manifest_digest)

    assert loaded.manifest == job.manifest
    assert len(loaded.articles) == limit


@pytest.mark.parametrize("case", ["too_many_records", "zero_max_tokens"])
def test_admission_refuses_a_job_that_bypassed_freeze(tmp_path, case):
    harness = Harness(tmp_path / "world", [OK])
    changes, reason = INVALID[case]
    job = crafted(harness, **changes)

    with pytest.raises(SnapshotRejected) as raised:
        asyncio.run(admit(job, store=harness.store(), runtime=harness.runtime()))

    assert raised.value.reason == reason
    assert harness.runtime_service.runs() == []
    assert harness.store().job_ids() == []


def test_admission_refuses_articles_that_do_not_match_the_manifest(tmp_path):
    harness = Harness(tmp_path / "world", [OK])
    job = harness.freeze()
    altered = synthetic_articles()
    altered[0]["title"] = "Different synthetic title"

    with pytest.raises(SnapshotRejected) as raised:
        asyncio.run(
            admit(
                FrozenJob(job.manifest_digest, job.manifest, altered),
                store=harness.store(),
                runtime=harness.runtime(),
            )
        )

    assert raised.value.reason == "snapshot_invalid"
    assert harness.runtime_service.runs() == []


@pytest.mark.parametrize(
    "case, code",
    [
        ("too_many_records", "invalid_input"),
        ("aggregate_bytes", "invalid_input"),
        ("zero_max_tokens", "invalid_input"),
        ("zero_input_tokens", "invalid_input"),
    ],
)
def test_worker_refuses_before_any_send(tmp_path, case, code):
    harness = Harness(tmp_path / "world", [OK])
    changes, reason = INVALID[case]
    job = crafted(harness, **changes)
    run = submit_raw(harness, job)

    result = harness.run_worker()

    assert (result.outcome, result.reason) == ("failed", reason)
    final = harness.run_doc(run["run_id"])
    assert (final["state"], final["error_code"]) == ("failed", code)
    assert final["error_summary"] == reason
    assert harness.observe(job) == {"R": None, "F": 0, "A": 0, "P": None, "C": 1}


def test_recovery_claim_refuses_before_any_send(tmp_path):
    harness = Harness(tmp_path / "world", [OK])
    changes, reason = INVALID["too_many_records"]
    job = crafted(harness, **changes)
    run = submit_raw(harness, job)
    # A worker claims and dies before verifying anything; Runtime re-leases.
    asyncio.run(
        harness.runtime().claim(
            product=PRODUCT,
            workflow_name=WORKFLOW_NAME,
            workflow_version=WORKFLOW_VERSION,
            lease_owner="dead-worker",
            lease_duration_seconds=harness.lease_duration,
        )
    )
    harness.expire_lease()

    result = harness.run_worker()

    assert (result.outcome, result.reason) == ("failed", reason)
    final = harness.run_doc(run["run_id"])
    assert (final["state"], final["attempt"]) == ("failed", 2)
    assert harness.observe(job) == {"R": None, "F": 0, "A": 0, "P": None, "C": 2}
