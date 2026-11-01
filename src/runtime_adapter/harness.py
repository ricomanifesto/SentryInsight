"""Synthetic wiring shared by the adapter tests and the local recovery demo.

Each call builds fresh adapter objects (store handle, Runtime client, worker)
that share nothing with earlier ones except durable files under ``root``, so a
new worker behaves like a restarted process. Observations come from the
durable ledger and the fakes' own records, never from a worker's result.
"""

from __future__ import annotations

import asyncio
import contextlib
from pathlib import Path
from typing import Any, Awaitable, Callable, Iterable, Iterator, Sequence

from .checkpoint import CheckpointStateStale, CheckpointStore, ledger_view
from .fakes import (
    FakeModelService,
    FakeRuntimeService,
    ManualTicker,
    ProviderStep,
    Respond,
    SyntheticClock,
)
from .identity import compute_code_identity
from .runtime_client import RuntimeClient
from .snapshot import FrozenJob, SnapshotStore, freeze
from .synthetic import (
    FAKE_PROVIDER_KEY,
    completion_body,
    synthetic_articles,
    synthetic_config,
)
from .worker import RunResult, Worker, admit

PROVIDER_URL = "https://model.example.test/api/v1"


@contextlib.contextmanager
def synthetic_delays(clock: SyntheticClock) -> Iterator[list[float]]:
    """Advance synthetic time for the legacy client's in-call delays.

    The legacy client awaits ``asyncio.sleep`` directly; the demo replaces it
    for its own process so no real-time sleep occurs. Control is still yielded
    to the event loop.
    """
    delays: list[float] = []
    original = asyncio.sleep

    async def advance(delay: float, *_args: Any, **_kwargs: Any) -> None:
        delays.append(delay)
        clock.advance(delay)
        await original(0)

    setattr(asyncio, "sleep", advance)
    try:
        yield delays
    finally:
        setattr(asyncio, "sleep", original)


class Harness:
    def __init__(
        self,
        root: Path,
        script: Sequence[ProviderStep] = (Respond(200, completion_body()),),
        *,
        retry_delay: float = 5.0,
        lease_duration: int = 600,
        random: Callable[[], float] | None = None,
    ) -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.clock = SyntheticClock(self.root / "clock.json")
        # Lease maintenance waits on this; nothing renews unless a test ticks.
        self.ticker = ManualTicker(self.clock)
        self.runtime_service = FakeRuntimeService(
            self.root / "runtime.json", self.clock, retry_delay=retry_delay
        )
        self.provider = FakeModelService(self.root / "provider.json", script)
        self.snapshots = SnapshotStore(self.root / "snapshots")
        self.store_root = self.root / "store"
        self.artifact_root = self.root / "artifacts"
        self.lease_duration = lease_duration
        self.random = random or (lambda: 0.5)

    def store(self, fault: Callable[[str], None] | None = None) -> CheckpointStore:
        return CheckpointStore(self.store_root, fault=fault)

    def runtime(self) -> RuntimeClient:
        return RuntimeClient(transport=self.runtime_service.transport())

    def freeze(self, articles=None, config=None, **kwargs: Any) -> FrozenJob:
        kwargs.setdefault("code_identity", compute_code_identity())
        return freeze(
            self.snapshots,
            synthetic_articles() if articles is None else articles,
            synthetic_config() if config is None else config,
            **kwargs,
        )

    def admit(
        self, job: FrozenJob, *, input_ref: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        if input_ref is None:
            return asyncio.run(admit(job, store=self.store(), runtime=self.runtime()))
        # A raw submission with a substituted reference, for rejection tests.
        from .identity import (
            PRODUCT,
            RUNTIME_MAX_ATTEMPTS,
            WORKFLOW_NAME,
            WORKFLOW_VERSION,
            idempotency_key,
        )

        run, _ = asyncio.run(
            self.runtime().submit(
                product=PRODUCT,
                workflow_name=WORKFLOW_NAME,
                workflow_version=WORKFLOW_VERSION,
                idempotency_key=idempotency_key(job.manifest_digest),
                input_ref=input_ref,
                max_attempts=RUNTIME_MAX_ATTEMPTS,
            )
        )
        return run

    def worker_kwargs(
        self,
        owner: str = "worker-1",
        *,
        fault: Callable[[str], Awaitable[None]] | None = None,
        store_fault: Iterable[str] = (),
        random: Callable[[], float] | None = None,
    ) -> dict[str, Any]:
        broken = frozenset(store_fault)

        def fail_writes(kind: str) -> None:
            if kind in broken:
                raise OSError("simulated store failure")

        return {
            "runtime": self.runtime(),
            "snapshots": self.snapshots,
            "store": self.store(fail_writes if broken else None),
            "artifact_root": self.artifact_root,
            "provider_transport": self.provider,
            "clock": self.clock.now,
            "random": random or self.random,
            "lease_owner": owner,
            "provider_api_key": FAKE_PROVIDER_KEY,
            "provider_base_url": PROVIDER_URL,
            "lease_duration_seconds": self.lease_duration,
            "heartbeat_wait": self.ticker.wait,
            "fault": fault,
        }

    def worker(self, owner: str = "worker-1", **kwargs: Any) -> Worker:
        return Worker(**self.worker_kwargs(owner, **kwargs))

    def run_worker(self, owner: str = "worker-1", **kwargs: Any) -> RunResult:
        return asyncio.run(self.worker(owner, **kwargs).run_once())

    def expire_lease(self) -> None:
        self.clock.advance(self.lease_duration + 1)

    def run_doc(self, run_id: str) -> dict[str, Any]:
        return next(r for r in self.runtime_service.runs() if r["run_id"] == run_id)

    def runs_for(self, job: FrozenJob) -> list[dict[str, Any]]:
        return [
            run
            for run in self.runtime_service.runs()
            if run["input_ref"].get("manifest_sha256") == job.manifest_digest
        ]

    def observe(self, job: FrozenJob) -> dict[str, int | None]:
        """R and P from the durable ledger; F and A from the fake provider's own
        ledger; C from the fake Runtime's lease events."""
        try:
            record = self.store().load(job.manifest_digest)
        except CheckpointStateStale:
            record = None
        view = ledger_view(record) if record else None
        return {
            "R": view.reserved if view else None,
            "F": self.provider.forwards,
            "A": self.provider.accepted,
            "P": view.replays if view else None,
            "C": sum(
                self.runtime_service.lease_grants(run["run_id"])
                for run in self.runs_for(job)
            ),
        }
