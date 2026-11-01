"""Product-owned publication of a prepared artifact.

Runtime completion means a validated prepared artifact; it never implies
publication. Publication is a separate operation keyed by artifact digest and
target. It records intent before any effect, observes by operation key before
every effect, publishes conditionally on the expected remote state, and records
a receipt afterwards. A lost acknowledgement is resolved by observation, never
by a second effect, and conflicting remote state fails closed with no force and
no regeneration. Only a fake publisher exists in this slice.
"""

from __future__ import annotations

from typing import Any, Callable, Protocol

from .checkpoint import CheckpointStore
from .identity import canonical_json, sha256_hex


class PublisherConflict(Exception):
    """The remote state differs from the expected state."""


class PublisherUnavailable(Exception):
    """The publisher could not be reached; the effect may or may not exist."""


class PublisherAckLost(PublisherUnavailable):
    """The effect may have been applied but its acknowledgement was lost."""


class Publisher(Protocol):
    def observe(self, operation_key: str) -> dict[str, Any] | None: ...

    def publish(
        self,
        operation_key: str,
        *,
        target: str,
        artifact_sha256: str,
        expected_remote: str | None,
    ) -> dict[str, Any]: ...


def operation_key(artifact_sha256: str, target: str) -> str:
    return sha256_hex(canonical_json({"artifact": artifact_sha256, "target": target}))


def publish_prepared(
    *,
    store: CheckpointStore,
    job_id: str,
    run: dict[str, Any],
    publisher: Publisher,
    target: str,
    expected_remote: str | None = None,
    fault: Callable[[str], None] | None = None,
) -> dict[str, Any]:
    record = store.load(job_id)
    artifact = record["artifact"] if record else None
    output = run.get("output_ref") or {}
    if (
        record is None
        or artifact is None
        or record["stage"] != "completed"
        or run.get("state") != "succeeded"
        or output.get("artifact_sha256") != artifact["sha256"]
    ):
        return {"state": "not_ready"}

    digest = artifact["sha256"]
    key = operation_key(digest, target)
    lease_version = record["highest_lease_version"]
    base = {
        "operation_key": key,
        "target": target,
        "artifact_sha256": digest,
        "expected_remote": expected_remote,
    }
    current = record["publication"]
    if current and current["operation_key"] == key:
        if current["state"] in ("published", "conflict"):
            return current
    else:
        store.record_publication(job_id, lease_version, dict(base, state="intent"))

    def settle(state: str, **extra: Any) -> dict[str, Any]:
        publication = dict(base, state=state, **extra)
        store.record_publication(job_id, lease_version, publication)
        return publication

    try:
        receipt = publisher.observe(key)
    except PublisherUnavailable:
        return settle("unresolved")
    if receipt is None:
        try:
            receipt = publisher.publish(
                key,
                target=target,
                artifact_sha256=digest,
                expected_remote=expected_remote,
            )
        except PublisherConflict:
            return settle("conflict")
        except PublisherUnavailable:
            return settle("unresolved")
        if fault is not None:
            fault("after_publication_effect")
    return settle("published", receipt=receipt["receipt_id"])
