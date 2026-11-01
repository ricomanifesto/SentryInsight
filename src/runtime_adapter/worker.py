"""Runtime worker for one frozen SentryInsight report-preparation job.

``run_once`` reconciles any pending control-plane action by reading the run,
claims at most one run, verifies the claimed input against the snapshot and the
live code, and resumes from the durable stage: analysis through the unchanged
``analyze_exploitation`` with a gated client, artifact preparation through the
unchanged ``generate_report`` into an isolated directory, then completion with
the artifact digest. It never schedules a retry; Runtime owns durable retries.

While ``run_once`` owns a lease, a maintenance task renews it at least every
third of the lease, concurrently with provider and artifact work, and the gate
and stage boundaries still heartbeat before each send and promotion.
Maintenance only renews that lease. A fenced or failed heartbeat stays on the
lease, so no further forward, promotion or completion follows, and maintenance
is stopped before the final Runtime report and on every exit. An event-loop or
process stall can still let the lease expire; fencing and the ambiguity rule
then govern what a later lease may do.

Caught failures map to a closed reason with a fixed Runtime code; an open or
ambiguous provider intent always dominates. Runtime-owned recovery after an
uncaught process death is distinct and leaves the product store in charge of
what the next lease may do.
"""

from __future__ import annotations

import asyncio
import dataclasses
import json
import math
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Awaitable, Callable

import httpx

from src.core.analyze import analyze_exploitation
from src.core.model_config import resolve_model, validate_model
from src.core.opencode_client import parse_model_selection
from src.core.openrouter_client import MAX_RETRY_DELAY, OpenRouterClient
from src.core.workflow import generate_report

from . import identity
from .checkpoint import (
    CheckpointStateStale,
    CheckpointStore,
    CheckpointStoreError,
    StaleLeaseWrite,
    TerminalJob,
    ledger_view,
)
from .reasons import (
    REASONS,
    error_summary,
    is_retryable,
    provider_failure_reason,
    reported_reserved,
    runtime_code,
)
from .runtime_client import TERMINAL_RUN_STATES, RuntimeApiError, RuntimeClient
from .send_gate import (
    DEFAULT_BUDGET,
    JitterPolicy,
    Lease,
    ProviderSendGate,
    RetryDispositionRecorder,
)
from .snapshot import FrozenJob, SnapshotRejected, SnapshotStore, materialize, verify

EXIT_OK, EXIT_RUNTIME, EXIT_LEASE_LOST = 0, 1, 2
DEFAULT_PROVIDER_URL = "https://openrouter.ai/api/v1"
# Bound at import: replacing asyncio.sleep to shape the legacy client's in-call
# delays must never turn lease maintenance into a busy loop.
_maintenance_wait = asyncio.sleep
_STORE_ERRORS = (
    CheckpointStoreError,
    CheckpointStateStale,
    StaleLeaseWrite,
    TerminalJob,
)
_REPORT_STAGES = {
    "finding_evidence": "report_grounding_rejected",
    "reporting_identity": "report_grounding_rejected",
    "report_validation": "report_validation_rejected",
    "report_artifact": "report_artifact_invalid",
    "report_policy": "report_policy_rejected",
    "report_output": "staging_failed",
}
_SITE_CODES = {
    "archive_conflict": "archive_conflict",
    "site_build_failed": "site_build_failed",
    "filesystem_error": "staging_failed",
}


@dataclasses.dataclass(frozen=True)
class RunResult:
    exit_code: int
    outcome: str
    reason: str | None = None
    run_id: str | None = None
    job_id: str | None = None
    persisted: bool = False
    product_reason: str | None = None
    run_state: str | None = None
    reconciled: int = 0


@dataclasses.dataclass(frozen=True)
class Failure:
    reason: str
    consume_through: int | None = None
    values: dict[str, Any] = dataclasses.field(default_factory=dict)
    fault: str | None = None
    diagnostic: dict[str, Any] | None = None


class Rejected(Exception):
    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


class LeaseLost(Exception):
    pass


class RuntimeUnavailable(Exception):
    def __init__(self, reason: str, *, product_reason: str | None = None) -> None:
        super().__init__(reason)
        self.reason = reason
        self.product_reason = product_reason


def artifact_digest(directory: Path) -> tuple[str, int, int]:
    """Digest every file's relative path and content; return digest, count, bytes."""
    lines, total = [], 0
    for path in sorted(p for p in directory.rglob("*") if p.is_file()):
        data = path.read_bytes()
        total += len(data)
        relative = path.relative_to(directory).as_posix()
        lines.append(f"{relative}\0{identity.sha256_hex(data)}\n")
    return identity.sha256_hex("".join(lines).encode("utf-8")), len(lines), total


def _control_plane(reason: str) -> bool:
    """True for reasons the worker cannot report to Runtime, so it exits."""
    return reason not in REASONS or runtime_code(reason) is None


def _stop_for(problem: str | None) -> None:
    if problem is None:
        return
    if problem == "lease_lost":
        raise LeaseLost()
    if _control_plane(problem):
        raise RuntimeUnavailable(problem)
    # A product failure on the lease, such as a maintenance fault.
    raise Rejected(problem)


def report_failure_reason(failure: Any) -> str:
    if not isinstance(failure, dict):
        return "report_artifact_invalid"
    stage = failure.get("stage")
    if stage == "site_publication":
        codes = failure.get("codes") or []
        return _SITE_CODES.get(codes[0] if codes else "", "staging_failed")
    return _REPORT_STAGES.get(str(stage), "report_artifact_invalid")


def _pinned_times(captured_at: float) -> tuple[str, str]:
    moment = datetime.fromtimestamp(captured_at, timezone.utc)
    generated_at = moment.isoformat(timespec="seconds").replace("+00:00", "Z")
    return moment.date().isoformat(), generated_at


async def admit(
    job: FrozenJob, *, store: CheckpointStore, runtime: RuntimeClient
) -> dict[str, Any]:
    """Record the job, then submit it; a lost acknowledgement is safe to repeat."""
    verify(job)
    version = job.manifest["workflow_version"]
    key = identity.idempotency_key(job.manifest_digest, version)
    store.create_job(job.manifest_digest, key)
    run, _ = await runtime.submit(
        product=identity.PRODUCT,
        workflow_name=identity.WORKFLOW_NAME,
        workflow_version=version,
        idempotency_key=key,
        input_ref=identity.input_ref(job.manifest_digest),
        max_attempts=identity.RUNTIME_MAX_ATTEMPTS,
    )
    store.record_run(job.manifest_digest, run["run_id"])
    return run


class Worker:
    def __init__(
        self,
        *,
        runtime: RuntimeClient,
        snapshots: SnapshotStore,
        store: CheckpointStore,
        artifact_root: Path,
        provider_transport: httpx.AsyncBaseTransport,
        clock: Callable[[], float],
        random: Callable[[], float],
        lease_owner: str,
        provider_api_key: str,
        lease_duration_seconds: int = 600,
        provider_timeout: float = 120.0,
        provider_base_url: str = DEFAULT_PROVIDER_URL,
        budget: int = DEFAULT_BUDGET,
        fault: Callable[[str], Awaitable[None]] | None = None,
        heartbeat_interval_seconds: float | None = None,
        heartbeat_wait: Callable[[float], Awaitable[None]] | None = None,
    ) -> None:
        # This lease-duration floor does not bound a request's total duration;
        # maintenance keeps the lease alive while a request is outstanding.
        if lease_duration_seconds < 3 * (provider_timeout + MAX_RETRY_DELAY):
            raise ValueError("lease must cover three provider request windows")
        interval = (
            lease_duration_seconds / 3
            if heartbeat_interval_seconds is None
            else float(heartbeat_interval_seconds)
        )
        if not (math.isfinite(interval) and 0 < interval <= lease_duration_seconds / 3):
            raise ValueError("heartbeat interval must be at most a third of the lease")
        self.heartbeat_interval = interval
        self.heartbeat_wait = heartbeat_wait or _maintenance_wait
        self.runtime = runtime
        self.snapshots = snapshots
        self.store = store
        self.artifact_root = Path(artifact_root)
        self.provider_transport = provider_transport
        self.clock = clock
        self.random = random
        self.lease_owner = lease_owner
        self.provider_api_key = provider_api_key
        self.lease_duration = lease_duration_seconds
        self.provider_timeout = provider_timeout
        self.provider_base_url = provider_base_url
        self.budget = budget
        self.fault = fault
        self.code_identity = identity.compute_code_identity()

    async def _fault(self, name: str) -> None:
        if self.fault is not None:
            await self.fault(name)

    async def _confirm(self, lease: Lease) -> None:
        _stop_for(await lease.confirm())

    @staticmethod
    def _check(lease: Lease) -> None:
        """Stop before a promotion once the lease is lost or unconfirmed."""
        _stop_for("lease_lost" if lease.lost else lease.problem)

    # Entry point ----------------------------------------------------------

    async def run_once(self) -> RunResult:
        try:
            reconciled, observed = await self._reconcile()
            run = await self.runtime.claim(
                product=identity.PRODUCT,
                workflow_name=identity.WORKFLOW_NAME,
                workflow_version=identity.WORKFLOW_VERSION,
                lease_owner=self.lease_owner,
                lease_duration_seconds=self.lease_duration,
            )
        except RuntimeApiError as error:
            return RunResult(EXIT_RUNTIME, "runtime_unavailable", error.reason)
        if run is None:
            return RunResult(EXIT_OK, "idle", reconciled=reconciled)
        lease = Lease(
            run_id=run["run_id"],
            owner=self.lease_owner,
            version=run["lease_version"],
            duration=self.lease_duration,
            runtime=self.runtime,
        )
        # Renew only while this invocation owns the lease; never after it returns.
        lease.maintain(self.heartbeat_interval, self.heartbeat_wait)
        try:
            result = await self._execute(run, lease, observed)
        except LeaseLost:
            result = RunResult(
                EXIT_LEASE_LOST, "lease_lost", "lease_lost", run_id=run["run_id"]
            )
        except RuntimeUnavailable as error:
            result = RunResult(
                EXIT_RUNTIME,
                "runtime_unavailable",
                error.reason,
                run_id=run["run_id"],
                persisted=error.product_reason is not None,
                product_reason=error.product_reason,
            )
        finally:
            await lease.release()
        return dataclasses.replace(result, reconciled=reconciled)

    async def _reconcile(self) -> tuple[int, dict[str, int]]:
        """Observe runs this store knows; acknowledge actions Runtime applied."""
        reconciled, observed = 0, {}
        try:
            job_ids = self.store.job_ids()
        except CheckpointStoreError:
            return 0, {}
        for job_id in job_ids:
            try:
                record = self.store.load(job_id)
            except (CheckpointStoreError, CheckpointStateStale):
                continue
            if record is None or record["run_id"] is None:
                continue
            ack = record["runtime_ack"]
            if ack and ack.get("state") in TERMINAL_RUN_STATES:
                continue
            try:
                run = await self.runtime.get_run(record["run_id"])
            except RuntimeApiError as error:
                if error.reason == "run_not_found":
                    continue
                raise
            reserved = reported_reserved(run.get("error_summary"))
            if reserved is not None:
                observed[run["run_id"]] = reserved
            action = record["pending_action"]
            if action is None or not self._applied(action, run):
                continue
            try:
                if action["kind"] == "complete":
                    self.store.advance(job_id, action["lease_version"], "completed")
                self.store.record_runtime_ack(
                    job_id,
                    action["lease_version"],
                    {"state": run["state"], "error_code": run.get("error_code")},
                )
            except _STORE_ERRORS:
                continue
            reconciled += 1
        return reconciled, observed

    @staticmethod
    def _applied(action: dict[str, Any], run: dict[str, Any]) -> bool:
        if action["kind"] == "complete":
            return run["state"] == "succeeded" and run.get("output_ref") == (
                action["output_ref"]
            )
        return (
            run["lease_version"] == action["lease_version"]
            and run["state"] in ("retry_wait", "failed")
            and run.get("error_code") == action["error_code"]
        )

    async def _execute(
        self, run: dict[str, Any], lease: Lease, observed: dict[str, int]
    ) -> RunResult:
        job_id: str | None = None
        try:
            job_id, frozen = self._verify_input(run)
            record = self._open(job_id, run, observed)
            await self._fault("after_claim")
            return await self._resume(run, lease, job_id, frozen, record)
        except (LeaseLost, RuntimeUnavailable):
            raise
        except StaleLeaseWrite:
            raise LeaseLost() from None
        except RuntimeApiError as error:
            if error.reason == "lease_fenced":
                raise LeaseLost() from None
            raise RuntimeUnavailable(error.reason) from None
        except (Rejected, SnapshotRejected) as rejection:
            failure = Failure(rejection.reason)
        except (CheckpointStoreError, CheckpointStateStale) as error:
            failure = Failure(error.reason)
        except Exception:
            # Only the fixed token leaves this handler, never the exception.
            failure = Failure("worker_unclassified")
        return await self._fail(run, lease, job_id, failure)

    # Verification and store admission -------------------------------------

    @staticmethod
    def _analysis_config(generation: dict[str, Any]) -> dict[str, Any]:
        return {
            "analysis": {
                "model": generation["model"],
                "max_tokens": generation["max_tokens"],
                "max_input_tokens": generation["max_input_tokens"],
            }
        }

    def _verify_input(self, run: dict[str, Any]) -> tuple[str, FrozenJob]:
        ref = run["input_ref"]
        if ref.get("kind") != identity.INPUT_REF_KIND:
            raise Rejected("snapshot_invalid")
        version = ref.get("manifest_version")
        if type(version) is not int:
            raise Rejected("snapshot_invalid")
        if version != identity.MANIFEST_VERSION:
            raise Rejected("unsupported_manifest_version")
        frozen = materialize(self.snapshots, ref.get("manifest_sha256"))
        manifest = frozen.manifest
        if (
            run["workflow_version"] not in identity.SUPPORTED_WORKFLOW_VERSIONS
            or manifest["workflow_version"] != run["workflow_version"]
            or manifest.get("product") != run["product"]
            or manifest.get("workflow_name") != run["workflow_name"]
            or manifest["code_identity"] != self.code_identity
        ):
            raise Rejected("unsupported_workflow_version")
        generation = manifest["generation"]
        model = resolve_model(self._analysis_config(generation))
        try:
            validate_model(model)
            selection = parse_model_selection(model)
            supported = selection is not None and selection.provider_id == "openrouter"
        except ValueError:
            supported = False
        if model != generation["model"] or not supported:
            raise Rejected("effective_config_invalid")
        return frozen.manifest_digest, frozen

    def _open(
        self, job_id: str, run: dict[str, Any], observed: dict[str, int]
    ) -> dict[str, Any]:
        key = identity.idempotency_key(job_id, run["workflow_version"])
        record = self.store.create_job(job_id, key)
        stale = (
            record["run_id"] not in (None, run["run_id"])
            or record["highest_lease_version"] > run["lease_version"]
            or ledger_view(record).reserved < observed.get(run["run_id"], 0)
        )
        try:
            self.store.record_lease(
                job_id,
                run["run_id"],
                run["lease_version"],
                attempt=run["attempt"],
                now=self.clock(),
            )
        except (StaleLeaseWrite, CheckpointStateStale):
            if not stale:
                raise
        if stale:
            # Spent budget is not restored and no accepted stage is reopened.
            raise Rejected("checkpoint_state_stale")
        record = self.store.load(job_id)
        if record is None:
            raise CheckpointStateStale()
        return record

    # Stages ------------------------------------------------------------------

    async def _resume(
        self,
        run: dict[str, Any],
        lease: Lease,
        job_id: str,
        frozen: FrozenJob,
        record: dict[str, Any],
    ) -> RunResult:
        disposition = record["disposition"]
        if disposition and disposition.get("terminal"):
            # A new lease never erases a quarantine; report it again, send nothing.
            return await self._fail(run, lease, job_id, None, existing=disposition)
        view = ledger_view(record)
        if record["artifact"] is None and view.unresolved_intent:
            for seq in view.open_reservations:
                self.store.record_outcome(
                    job_id,
                    lease.version,
                    seq,
                    {"disposition": "ambiguous", "fault": "no_disposition"},
                )
            return await self._fail(
                run, lease, job_id, Failure("provider_intent_unresolved")
            )
        if record["analysis"] is None:
            failure = self._deferral(view) or await self._analyze(lease, job_id, frozen)
            if failure is not None:
                return await self._fail(run, lease, job_id, failure)
            await self._fault("after_analysis_record")
            record = self._reload(job_id)
        if record["artifact"] is None:
            failure = await self._prepare_artifact(lease, job_id, frozen, record)
            if failure is not None:
                return await self._fail(run, lease, job_id, failure)
            await self._fault("after_artifact_record")
            record = self._reload(job_id)
        else:
            await self._ensure_artifact(job_id, frozen, record)
        return await self._complete(run, lease, job_id, record)

    def _reload(self, job_id: str) -> dict[str, Any]:
        record = self.store.load(job_id)
        if record is None:
            raise CheckpointStateStale()
        return record

    def _deferral(self, view: Any) -> Failure | None:
        """Stop without sending when nothing can be replayed and no send is allowed."""
        if view.unconsumed_resolved:
            return None
        through = view.reservations[-1]["seq"] if view.reservations else None
        if view.reserved >= self.budget:
            return Failure("provider_budget_exhausted", through)
        if view.not_before is not None and self.clock() < view.not_before:
            return Failure("provider_retry_after_deferred", through)
        return None

    async def _analyze(
        self, lease: Lease, job_id: str, frozen: FrozenJob
    ) -> Failure | None:
        await self._confirm(lease)
        generation = frozen.manifest["generation"]
        gate = ProviderSendGate(
            store=self.store,
            job_id=job_id,
            lease=lease,
            inner=self.provider_transport,
            clock=self.clock,
            budget=self.budget,
            fault=self.fault,
        )
        client = OpenRouterClient(
            api_key=self.provider_api_key,
            max_tokens=generation["max_tokens"],
            base_url=self.provider_base_url,
            timeout=self.provider_timeout,
            transport=gate,
            retry_delay_policy=JitterPolicy(gate, self.random),
        )
        recorder = RetryDispositionRecorder(client, gate)
        result = await analyze_exploitation(
            frozen.articles,
            self._analysis_config(generation),
            model_client=recorder,
        )
        if lease.lost or gate.refusal_reason == "lease_lost":
            raise LeaseLost()
        view = ledger_view(self._reload(job_id))
        through = view.reservations[-1]["seq"] if view.reservations else None

        if not result.get("error") and not result.get("skipped") and gate.delivered:
            self._check(lease)
            outcome = view.outcomes(gate.delivered[-1])[0]
            date, generated_at = _pinned_times(outcome["received_at"])
            analysis = {
                "date": date,
                "generated_at": generated_at,
                "exploitation_report": result["exploitation_report"],
                "reporting_sources": result.get("reporting_sources", []),
                "cves_identified": sorted(result.get("cves_identified", [])),
                "analyzed_article_count": result.get("analyzed_article_count"),
            }
            digest = self.store.put_blob(job_id, identity.canonical_json(analysis))
            self.store.advance(
                job_id,
                lease.version,
                "analyzed",
                analysis={"sha256": digest, "date": date, "generated_at": generated_at},
                consume_through=through,
            )
            return None

        # Only a durably recorded disposition contributes reported values.
        disposition = (recorder.disposition if recorder.persisted else None) or {}
        values = {
            key: disposition.get(key)
            for key in ("attempts", "http_status", "provider_code")
        }
        last_fault = None
        if view.reservations:
            outcomes = view.outcomes(view.reservations[-1]["seq"])
            last_fault = outcomes[0].get("fault") if outcomes else None
        if gate.unresolved or view.unresolved_intent:
            reason = "provider_intent_unresolved"
        elif gate.refusal_reason is not None:
            reason = gate.refusal_reason
        elif recorder.disposition is not None:
            reason = provider_failure_reason(
                recorder.disposition,
                reserved=view.reserved,
                budget=self.budget,
                not_before=view.not_before,
                now=self.clock(),
                last_fault=last_fault,
            )
        elif result.get("error_class") == "input_budget_exceeded":
            reason = "input_budget_exceeded"
        else:
            reason = "worker_unclassified"
        if _control_plane(reason):
            raise RuntimeUnavailable(reason)
        return Failure(reason, through, values, last_fault)

    async def _build(
        self,
        job_id: str,
        lease_version: int,
        analysis: dict[str, Any],
        frozen: FrozenJob,
    ) -> tuple[str, int, int] | Failure:
        job_dir = self.artifact_root / job_id
        staging = job_dir / f".staging-{lease_version}"
        if staging.exists():
            shutil.rmtree(staging)
        staging.mkdir(parents=True)
        state: Any = {
            "analysis_results": analysis,
            "config": {"output_path": str(staging / "index.md")},
            "status": "started",
            "articles_fingerprint": frozen.manifest["articles_fingerprint"],
        }
        final = await generate_report(state)
        if final.get("status") == "failed" or not final.get("report_path"):
            shutil.rmtree(staging, ignore_errors=True)
            failure = final.get("failure")
            diagnostic = None
            if isinstance(failure, dict):
                diagnostic = {
                    "stage": failure.get("stage"),
                    "codes": list(failure.get("codes") or []),
                    "field": failure.get("field"),
                }
            return Failure(report_failure_reason(failure), diagnostic=diagnostic)
        digest, files, size = artifact_digest(staging)
        target = job_dir / digest
        if target.exists() and artifact_digest(target)[0] == digest:
            shutil.rmtree(staging)
        else:
            if target.exists():
                shutil.rmtree(target)
            os.replace(staging, target)
        return digest, files, size

    async def _prepare_artifact(
        self, lease: Lease, job_id: str, frozen: FrozenJob, record: dict[str, Any]
    ) -> Failure | None:
        await self._confirm(lease)
        analysis = json.loads(self.store.get_blob(job_id, record["analysis"]["sha256"]))
        try:
            built = await self._build(job_id, lease.version, analysis, frozen)
        except OSError:
            return Failure("staging_failed")
        if isinstance(built, Failure):
            return built
        digest, files, size = built
        self._check(lease)
        self.store.advance(
            job_id,
            lease.version,
            "artifact_prepared",
            artifact={"sha256": digest, "files": files, "bytes": size},
        )
        return None

    async def _ensure_artifact(
        self, job_id: str, frozen: FrozenJob, record: dict[str, Any]
    ) -> None:
        expected = record["artifact"]["sha256"]
        target = self.artifact_root / job_id / expected
        if target.is_dir() and artifact_digest(target)[0] == expected:
            return
        analysis = json.loads(self.store.get_blob(job_id, record["analysis"]["sha256"]))
        built = await self._build(
            job_id, record["highest_lease_version"], analysis, frozen
        )
        if isinstance(built, Failure) or built[0] != expected:
            raise CheckpointStateStale()

    async def _complete(
        self, run: dict[str, Any], lease: Lease, job_id: str, record: dict[str, Any]
    ) -> RunResult:
        artifact = record["artifact"]
        output_ref = {
            "kind": identity.OUTPUT_REF_KIND,
            "manifest_sha256": job_id,
            "artifact_sha256": artifact["sha256"],
            "artifact_files": artifact["files"],
            "artifact_bytes": artifact["bytes"],
        }
        # Maintenance ends before the report, so no heartbeat races completion.
        await lease.release()
        await self._confirm(lease)
        self.store.set_pending_action(
            job_id,
            lease.version,
            {
                "kind": "complete",
                "run_id": run["run_id"],
                "lease_version": lease.version,
                "output_ref": output_ref,
            },
        )
        await self._fault("before_runtime_report")
        try:
            final = await self.runtime.complete(
                run["run_id"],
                lease_owner=lease.owner,
                lease_version=lease.version,
                output_ref=output_ref,
            )
        except RuntimeApiError as error:
            if error.reason == "lease_fenced":
                raise LeaseLost() from None
            raise RuntimeUnavailable(error.reason) from None
        persisted = True
        try:
            self.store.advance(job_id, lease.version, "completed")
            self.store.record_runtime_ack(
                job_id, lease.version, {"state": final["state"], "error_code": None}
            )
        except _STORE_ERRORS:
            persisted = False
        return RunResult(
            EXIT_OK,
            "completed",
            run_id=run["run_id"],
            job_id=job_id,
            persisted=persisted,
            run_state=final["state"],
        )

    # Failure reporting ------------------------------------------------------

    def _unresolved(self, job_id: str | None) -> bool:
        if job_id is None:
            return False
        try:
            record = self.store.load(job_id)
        except (CheckpointStoreError, CheckpointStateStale):
            return False
        return bool(record and ledger_view(record).unresolved_intent)

    def _reserved(self, job_id: str | None) -> int | None:
        if job_id is None:
            return None
        try:
            record = self.store.load(job_id)
        except (CheckpointStoreError, CheckpointStateStale):
            return None
        return ledger_view(record).reserved if record else None

    async def _fail(
        self,
        run: dict[str, Any],
        lease: Lease,
        job_id: str | None,
        failure: Failure | None,
        *,
        existing: dict[str, Any] | None = None,
    ) -> RunResult:
        await lease.release()
        if lease.lost:
            # A fenced lease writes no disposition and reports nothing.
            raise LeaseLost()
        if existing is not None:
            reason, code = existing["reason"], existing["runtime_code"]
            summary, persisted = existing["summary"], True
        else:
            assert failure is not None
            reason = failure.reason
            if reason in ("worker_unclassified", "checkpoint_store_failed") and (
                self._unresolved(job_id)
            ):
                reason = "provider_intent_unresolved"
            code = runtime_code(reason, fault=failure.fault)
            if code is None:
                if reason == "lease_lost":
                    raise LeaseLost()
                raise RuntimeUnavailable(reason)
            summary = error_summary(
                reason, reserved=self._reserved(job_id), **failure.values
            )
            persisted = False
            if job_id is not None:
                try:
                    self.store.record_disposition(
                        job_id,
                        lease.version,
                        {
                            "reason": reason,
                            "terminal": not is_retryable(reason),
                            "runtime_code": code,
                            "summary": summary,
                            "diagnostic": failure.diagnostic,
                        },
                        consume_through=failure.consume_through,
                    )
                    persisted = True
                except _STORE_ERRORS:
                    persisted = False
        if job_id is not None:
            try:
                self.store.set_pending_action(
                    job_id,
                    lease.version,
                    {
                        "kind": "fail",
                        "run_id": run["run_id"],
                        "lease_version": lease.version,
                        "error_code": code,
                        "error_summary": summary,
                    },
                )
            except _STORE_ERRORS:
                pass
        await self._fault("before_runtime_report")
        try:
            final = await self.runtime.fail(
                run["run_id"],
                lease_owner=lease.owner,
                lease_version=lease.version,
                error_code=code,
                error_summary=summary,
            )
        except RuntimeApiError as error:
            if error.reason == "lease_fenced":
                raise LeaseLost() from None
            raise RuntimeUnavailable(
                error.reason, product_reason=reason if persisted else None
            ) from None
        if job_id is not None:
            try:
                self.store.record_runtime_ack(
                    job_id,
                    lease.version,
                    {"state": final["state"], "error_code": code},
                )
            except _STORE_ERRORS:
                pass
        return RunResult(
            EXIT_OK,
            "failed",
            reason,
            run_id=run["run_id"],
            job_id=job_id,
            persisted=persisted,
            product_reason=reason,
            run_state=final["state"],
        )
