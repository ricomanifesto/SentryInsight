"""Product-owned publication with the fake publisher.

Publication is separate from Runtime completion: it has its own operation key,
records intent before the effect and a receipt after it, and resolves a lost
acknowledgement by observation before any second effect.
"""

import asyncio

import pytest

from src.runtime_adapter.fakes import FakePublisher, SimulatedCrash
from src.runtime_adapter.harness import Harness
from src.runtime_adapter.publication import operation_key, publish_prepared
from src.runtime_adapter.worker import artifact_digest

TARGET = "pages:synthetic-preview"


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    async def sleep(*_args, **_kwargs):
        return None

    monkeypatch.setattr(asyncio, "sleep", sleep)


@pytest.fixture
def completed(tmp_path):
    harness = Harness(tmp_path / "world")
    job = harness.freeze()
    run = harness.admit(job)
    assert harness.run_worker().outcome == "completed"
    return harness, job, harness.run_doc(run["run_id"])


def publish(harness, job, run, publisher, **kwargs):
    return publish_prepared(
        store=harness.store(),
        job_id=job.manifest_digest,
        run=run,
        publisher=publisher,
        target=TARGET,
        **kwargs,
    )


def prepared_digest(harness, job, run):
    digest = run["output_ref"]["artifact_sha256"]
    return artifact_digest(harness.artifact_root / job.manifest_digest / digest)[0]


def test_publication_records_intent_effect_and_receipt_once(completed, tmp_path):
    harness, job, run = completed
    publisher = FakePublisher(tmp_path / "publisher.json")

    first = publish(harness, job, run, publisher)
    second = publish(harness, job, run, publisher)

    digest = run["output_ref"]["artifact_sha256"]
    assert first["state"] == second["state"] == "published"
    assert first["operation_key"] == operation_key(digest, TARGET)
    assert publisher.effects == 1
    assert publisher.current(TARGET) == digest
    record = harness.store().load(job.manifest_digest)
    assert record["publication"]["receipt"] == first["receipt"]
    assert record["stage"] == "completed"


def test_lost_acknowledgement_is_resolved_by_observation(completed, tmp_path):
    harness, job, run = completed
    publisher = FakePublisher(tmp_path / "publisher.json")
    publisher.lose_next_acknowledgement = True

    first = publish(harness, job, run, publisher)
    assert first["state"] == "unresolved"
    assert publisher.effects == 1

    second = publish(harness, job, run, FakePublisher(tmp_path / "publisher.json"))

    assert second["state"] == "published"
    assert publisher.effects == 1


def test_crash_after_effect_before_receipt_is_resolved_by_observation(
    completed, tmp_path
):
    harness, job, run = completed
    publisher = FakePublisher(tmp_path / "publisher.json")

    def crash(point):
        if point == "after_publication_effect":
            raise SimulatedCrash(point)

    with pytest.raises(SimulatedCrash):
        publish(harness, job, run, publisher, fault=crash)
    record = harness.store().load(job.manifest_digest)
    assert record["publication"]["state"] == "intent"

    result = publish(harness, job, run, FakePublisher(tmp_path / "publisher.json"))

    assert result["state"] == "published"
    assert publisher.effects == 1


def test_conflicting_remote_state_fails_closed_without_force(completed, tmp_path):
    harness, job, run = completed
    publisher = FakePublisher(tmp_path / "publisher.json")
    publisher.seed(TARGET, "f" * 64)
    before = prepared_digest(harness, job, run)

    first = publish(harness, job, run, publisher)
    second = publish(harness, job, run, publisher)

    assert first["state"] == second["state"] == "conflict"
    assert publisher.effects == 0
    assert publisher.current(TARGET) == "f" * 64
    assert prepared_digest(harness, job, run) == before
    record = harness.store().load(job.manifest_digest)
    assert record["publication"]["state"] == "conflict"


def test_expected_remote_state_permits_a_conditional_replacement(completed, tmp_path):
    harness, job, run = completed
    publisher = FakePublisher(tmp_path / "publisher.json")
    publisher.seed(TARGET, "f" * 64)

    result = publish(harness, job, run, publisher, expected_remote="f" * 64)

    assert result["state"] == "published"
    assert publisher.current(TARGET) == run["output_ref"]["artifact_sha256"]


def test_publication_requires_an_observed_completed_run(tmp_path):
    harness = Harness(tmp_path / "world")
    job = harness.freeze()
    run = harness.admit(job)
    publisher = FakePublisher(tmp_path / "publisher.json")

    result = publish(harness, job, run, publisher)

    assert result["state"] == "not_ready"
    assert publisher.effects == 0
    assert harness.store().load(job.manifest_digest)["publication"] is None


def test_observation_retries_spend_no_provider_or_lease_budget(completed, tmp_path):
    harness, job, run = completed
    publisher = FakePublisher(tmp_path / "publisher.json")
    before = harness.observe(job)
    publisher.unavailable_observations = 2

    states = [publish(harness, job, run, publisher)["state"] for _ in range(3)]

    assert states == ["unresolved", "unresolved", "published"]
    assert publisher.effects == 1
    assert harness.observe(job) == before
