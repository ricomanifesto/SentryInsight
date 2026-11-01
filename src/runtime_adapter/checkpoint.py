"""Product-owned durable checkpoint store, one record per frozen job.

Every write replaces the whole record atomically under an exclusive per-job
file lock, so a reader never sees a half-written record and a check-then-write
decision (such as a reservation) is crash-consistent across processes on one
host. The ledger is append-only with a per-entry chain digest; the provider
budget is the count of reservation entries, never a separate counter.

Product writes are fenced by the Runtime ``lease_version``: only the highest
lease the store has recorded may write, except that a reservation's opener may
append that reservation's own outcome after losing the lease.

A chain detects edits, removals and reordering inside the ledger. It cannot
detect removal of a valid suffix or a whole-store rollback.
"""

from __future__ import annotations

import contextlib
import fcntl
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterator, TypeVar, cast

from .durable import atomic_write_bytes
from .identity import canonical_json, sha256_hex

STAGES = ("admitted", "claimed", "analyzed", "artifact_prepared", "completed")
_DIGEST = re.compile(r"^[0-9a-f]{64}$")
_GENERIC_ENTRY_TYPES = frozenset(
    {"refusal", "replay", "delay_sample", "retry_disposition"}
)
T = TypeVar("T")


class CheckpointStoreError(Exception):
    """The store could not be read or written; nothing is claimed durable."""

    reason = "checkpoint_store_failed"

    def __init__(self) -> None:
        super().__init__(self.reason)


class CheckpointStateStale(Exception):
    """Stored state is corrupt, tampered or inconsistent with Runtime."""

    reason = "checkpoint_state_stale"

    def __init__(self) -> None:
        super().__init__(self.reason)


class StaleLeaseWrite(Exception):
    """A write came from a lease older than the highest recorded lease."""

    reason = "lease_lost"

    def __init__(self) -> None:
        super().__init__(self.reason)


class TerminalJob(Exception):
    """The job already has a terminal disposition; no progress is accepted."""


class StageRegression(Exception):
    """A stage write would move the job backwards."""


class ReservationRefused(Exception):
    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


def _genesis(job_id: str) -> str:
    return sha256_hex(b"sentryinsight-runtime-adapter-ledger\0" + job_id.encode())


def _chain(previous: str, entry: dict[str, Any]) -> str:
    body = {key: value for key, value in entry.items() if key != "chain"}
    return sha256_hex(previous.encode("ascii") + canonical_json(body))


@dataclass(frozen=True)
class LedgerView:
    """Read-only derivations from a verified ledger."""

    entries: tuple[dict[str, Any], ...]

    def of_type(self, entry_type: str) -> list[dict[str, Any]]:
        return [entry for entry in self.entries if entry["type"] == entry_type]

    @property
    def reservations(self) -> list[dict[str, Any]]:
        return self.of_type("reservation")

    @property
    def reserved(self) -> int:
        return len(self.reservations)

    def outcomes(self, seq: int) -> list[dict[str, Any]]:
        return [
            entry for entry in self.of_type("outcome") if entry["reservation"] == seq
        ]

    def disposition(self, seq: int) -> str | None:
        # The first recorded disposition governs safety; later ones are retained.
        outcomes = self.outcomes(seq)
        return outcomes[0]["disposition"] if outcomes else None

    def _with(self, disposition: str | None) -> list[int]:
        return [
            entry["seq"]
            for entry in self.reservations
            if self.disposition(entry["seq"]) == disposition
        ]

    @property
    def open_reservations(self) -> list[int]:
        return self._with(None)

    @property
    def ambiguous_reservations(self) -> list[int]:
        return self._with("ambiguous")

    @property
    def failed_before_forward(self) -> list[int]:
        return self._with("failed_before_forward")

    @property
    def resolved(self) -> int:
        return len(self._with("resolved"))

    @property
    def unresolved_intent(self) -> bool:
        return bool(self.open_reservations or self.ambiguous_reservations)

    @property
    def not_before(self) -> int | None:
        values = [
            entry["not_before"]
            for entry in self.of_type("outcome")
            if type(entry.get("not_before")) is int
        ]
        return max(values) if values else None

    @property
    def consumed_through(self) -> int:
        return max((entry["through"] for entry in self.of_type("consumed")), default=0)

    @property
    def unconsumed_resolved(self) -> list[dict[str, Any]]:
        """Captured responses not yet consumed by an analysis or failure record."""
        through = self.consumed_through
        return [
            self.outcomes(entry["seq"])[0]
            for entry in self.reservations
            if entry["seq"] > through and self.disposition(entry["seq"]) == "resolved"
        ]

    @property
    def replays(self) -> int:
        return len(self.of_type("replay"))

    def delay_sample(self, follows: int) -> dict[str, Any] | None:
        for entry in self.of_type("delay_sample"):
            if entry["follows"] == follows:
                return entry
        return None

    def reservation(self, seq: int) -> dict[str, Any] | None:
        for entry in self.reservations:
            if entry["seq"] == seq:
                return entry
        return None


def ledger_view(record: dict[str, Any]) -> LedgerView:
    return LedgerView(tuple(record["ledger"]))


class CheckpointStore:
    def __init__(
        self, root: Path, *, fault: Callable[[str], None] | None = None
    ) -> None:
        self.root = Path(root)
        self.fault = fault

    # Paths and low-level IO -------------------------------------------------

    def _job_dir(self, job_id: str) -> Path:
        if not isinstance(job_id, str) or not _DIGEST.match(job_id):
            raise CheckpointStateStale()
        return self.root / "jobs" / job_id

    def blob_path(self, job_id: str, digest: str) -> Path:
        if not isinstance(digest, str) or not _DIGEST.match(digest):
            raise CheckpointStateStale()
        return self._job_dir(job_id) / "blobs" / digest

    def job_ids(self) -> list[str]:
        jobs = self.root / "jobs"
        try:
            return sorted(
                path.name
                for path in jobs.iterdir()
                if _DIGEST.match(path.name) and (path / "record.json").is_file()
            )
        except FileNotFoundError:
            return []
        except OSError:
            raise CheckpointStoreError() from None

    @contextlib.contextmanager
    def _locked(self, job_id: str) -> Iterator[None]:
        directory = self._job_dir(job_id)
        try:
            directory.mkdir(parents=True, exist_ok=True)
            handle = open(directory / ".lock", "a+b")
        except OSError:
            raise CheckpointStoreError() from None
        with handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)

    def _write(self, job_id: str, record: dict[str, Any], kind: str) -> None:
        try:
            if self.fault is not None:
                self.fault(kind)
            atomic_write_bytes(
                self._job_dir(job_id) / "record.json", canonical_json(record)
            )
        except OSError:
            raise CheckpointStoreError() from None

    def load(self, job_id: str) -> dict[str, Any] | None:
        path = self._job_dir(job_id) / "record.json"
        try:
            data = path.read_bytes()
        except FileNotFoundError:
            return None
        except OSError:
            raise CheckpointStoreError() from None
        try:
            record = json.loads(data)
            ledger = record["ledger"]
            valid = record["job_id"] == job_id and isinstance(ledger, list)
        except (ValueError, KeyError, TypeError):
            raise CheckpointStateStale() from None
        if not valid:
            raise CheckpointStateStale()
        previous = _genesis(job_id)
        for index, raw in enumerate(ledger):
            if not isinstance(raw, dict):
                raise CheckpointStateStale()
            entry = cast(dict[str, Any], raw)
            if entry.get("seq") != index + 1 or entry.get("chain") != _chain(
                previous, entry
            ):
                raise CheckpointStateStale()
            previous = entry["chain"]
        return record

    def _transact(
        self, job_id: str, kind: str, mutate: Callable[[dict[str, Any]], T]
    ) -> T:
        with self._locked(job_id):
            record = self.load(job_id)
            if record is None:
                raise CheckpointStateStale()
            result = mutate(record)
            self._write(job_id, record, kind)
            return result

    @staticmethod
    def _append(record: dict[str, Any], entry: dict[str, Any]) -> int:
        ledger = record["ledger"]
        entry = dict(entry, seq=len(ledger) + 1)
        previous = ledger[-1]["chain"] if ledger else _genesis(record["job_id"])
        entry["chain"] = _chain(previous, entry)
        ledger.append(entry)
        return entry["seq"]

    @staticmethod
    def _fence(record: dict[str, Any], lease_version: int) -> None:
        if lease_version != record["highest_lease_version"]:
            raise StaleLeaseWrite()

    @staticmethod
    def _require_active(record: dict[str, Any]) -> None:
        disposition = record.get("disposition")
        if disposition and disposition.get("terminal"):
            raise TerminalJob()

    # Admission and leases ---------------------------------------------------

    def create_job(self, job_id: str, idempotency_key: str) -> dict[str, Any]:
        with self._locked(job_id):
            existing = self.load(job_id)
            if existing is not None:
                if existing["idempotency_key"] != idempotency_key:
                    raise CheckpointStateStale()
                return existing
            record: dict[str, Any] = {
                "format": 1,
                "job_id": job_id,
                "idempotency_key": idempotency_key,
                "run_id": None,
                "highest_lease_version": 0,
                "leases": [],
                "stage": "admitted",
                "ledger": [],
                "analysis": None,
                "artifact": None,
                "disposition": None,
                "pending_action": None,
                "runtime_ack": None,
                "publication": None,
            }
            self._write(job_id, record, "admission")
            return record

    def record_run(self, job_id: str, run_id: str) -> None:
        def mutate(record: dict[str, Any]) -> None:
            if record["run_id"] not in (None, run_id):
                raise CheckpointStateStale()
            record["run_id"] = run_id

        self._transact(job_id, "run", mutate)

    def record_lease(
        self, job_id: str, run_id: str, lease_version: int, *, attempt: int, now: float
    ) -> None:
        def mutate(record: dict[str, Any]) -> None:
            if record["run_id"] not in (None, run_id):
                raise CheckpointStateStale()
            if lease_version < record["highest_lease_version"]:
                raise StaleLeaseWrite()
            record["run_id"] = run_id
            if lease_version > record["highest_lease_version"]:
                record["highest_lease_version"] = lease_version
                record["leases"].append(
                    {"lease_version": lease_version, "attempt": attempt, "at": now}
                )
            if STAGES.index(record["stage"]) < STAGES.index("claimed"):
                record["stage"] = "claimed"

        self._transact(job_id, "lease", mutate)

    # Provider ledger --------------------------------------------------------

    def reserve(
        self,
        job_id: str,
        lease_version: int,
        *,
        request_sha256: str,
        now: float,
        budget: int,
    ) -> int:
        """Charge one submission and record its intent in one durable write."""

        def mutate(record: dict[str, Any]) -> int:
            self._fence(record, lease_version)
            self._require_active(record)
            view = ledger_view(record)
            if view.unresolved_intent:
                raise ReservationRefused("provider_intent_unresolved")
            if view.reserved >= budget:
                raise ReservationRefused("provider_budget_exhausted")
            if view.not_before is not None and now < view.not_before:
                raise ReservationRefused("provider_retry_after_deferred")
            return self._append(
                record,
                {
                    "type": "reservation",
                    "lease_version": lease_version,
                    "request_sha256": request_sha256,
                    "reserved_at": now,
                },
            )

        return self._transact(job_id, "reservation", mutate)

    def record_outcome(
        self, job_id: str, lease_version: int, seq: int, outcome: dict[str, Any]
    ) -> None:
        def mutate(record: dict[str, Any]) -> None:
            reservation = ledger_view(record).reservation(seq)
            if reservation is None:
                raise CheckpointStateStale()
            if lease_version != record["highest_lease_version"] and (
                reservation["lease_version"] != lease_version
            ):
                raise StaleLeaseWrite()
            entry = dict(outcome, type="outcome", reservation=seq)
            entry["lease_version"] = lease_version
            self._append(record, entry)

        self._transact(job_id, "outcome", mutate)

    def append(self, job_id: str, lease_version: int, entry: dict[str, Any]) -> int:
        if entry.get("type") not in _GENERIC_ENTRY_TYPES:
            raise ValueError("unsupported ledger entry type")

        def mutate(record: dict[str, Any]) -> int:
            self._fence(record, lease_version)
            return self._append(record, dict(entry, lease_version=lease_version))

        return self._transact(job_id, str(entry["type"]), mutate)

    # Stages, dispositions and control-plane actions -------------------------

    def advance(
        self,
        job_id: str,
        lease_version: int,
        stage: str,
        *,
        consume_through: int | None = None,
        **fields: Any,
    ) -> None:
        unknown = set(fields) - {"analysis", "artifact"}
        if stage not in STAGES or unknown:
            raise ValueError("unsupported stage write")

        def mutate(record: dict[str, Any]) -> None:
            self._fence(record, lease_version)
            self._require_active(record)
            if STAGES.index(stage) < STAGES.index(record["stage"]):
                raise StageRegression(stage)
            record["stage"] = stage
            record.update(fields)
            if consume_through is not None:
                self._consume(record, lease_version, consume_through, stage)

        self._transact(job_id, stage, mutate)

    def _consume(
        self, record: dict[str, Any], lease_version: int, through: int, by: str
    ) -> None:
        if through > ledger_view(record).consumed_through:
            self._append(
                record,
                {
                    "type": "consumed",
                    "through": through,
                    "by": by,
                    "lease_version": lease_version,
                },
            )

    def record_disposition(
        self,
        job_id: str,
        lease_version: int,
        disposition: dict[str, Any],
        *,
        consume_through: int | None = None,
    ) -> None:
        def mutate(record: dict[str, Any]) -> None:
            self._fence(record, lease_version)
            self._require_active(record)
            record["disposition"] = dict(disposition, lease_version=lease_version)
            if consume_through is not None:
                self._consume(record, lease_version, consume_through, "failure")

        self._transact(job_id, "disposition", mutate)

    def set_pending_action(
        self, job_id: str, lease_version: int, action: dict[str, Any] | None
    ) -> None:
        def mutate(record: dict[str, Any]) -> None:
            self._fence(record, lease_version)
            record["pending_action"] = action

        self._transact(job_id, "pending_action", mutate)

    def record_runtime_ack(
        self, job_id: str, lease_version: int, ack: dict[str, Any]
    ) -> None:
        def mutate(record: dict[str, Any]) -> None:
            self._fence(record, lease_version)
            record["pending_action"] = None
            record["runtime_ack"] = ack

        self._transact(job_id, "runtime_ack", mutate)

    def record_publication(
        self, job_id: str, lease_version: int, publication: dict[str, Any]
    ) -> None:
        def mutate(record: dict[str, Any]) -> None:
            self._fence(record, lease_version)
            record["publication"] = publication

        self._transact(job_id, "publication", mutate)

    # Private blobs ----------------------------------------------------------

    def put_blob(self, job_id: str, data: bytes) -> str:
        digest = sha256_hex(data)
        try:
            if self.fault is not None:
                self.fault("blob")
            atomic_write_bytes(self.blob_path(job_id, digest), data)
        except OSError:
            raise CheckpointStoreError() from None
        return digest

    def get_blob(self, job_id: str, digest: str) -> bytes:
        path = self.blob_path(job_id, digest)
        try:
            data = path.read_bytes()
        except FileNotFoundError:
            raise CheckpointStateStale() from None
        except OSError:
            raise CheckpointStoreError() from None
        if sha256_hex(data) != digest:
            raise CheckpointStateStale()
        return data
