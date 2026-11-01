#!/usr/bin/env python3
"""Local synthetic recovery demo for the durable execution adapter.

Runs the acceptance scenarios against the fake Runtime, fake provider and fake
publisher with an injected clock and randomness, then writes ``result.json``
and ``table.md`` into an explicit output directory outside the repository.
Nothing here contacts a real provider, Runtime, Git remote or Pages host.

Subcommands:
  run           run every scenario and write the outputs
  crash-worker  run one worker that exits abruptly at a fault point
  status        print status for every job under a demo world
"""

# ruff: noqa: E402

import argparse
import asyncio
import json
import os
import random
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

import httpx

from src.runtime_adapter.checkpoint import ledger_view
from src.runtime_adapter.fakes import (
    AcceptThenFail,
    AcceptThenWait,
    FakePublisher,
    ProviderStep,
    Respond,
    SimulatedCrash,
)
from src.runtime_adapter.harness import Harness, synthetic_delays
from src.runtime_adapter.publication import publish_prepared
from src.runtime_adapter.status import job_status, render_status
from src.runtime_adapter.synthetic import (
    FAKE_PROVIDER_KEY,
    GROUNDING_REJECTED_REPORT,
    completion_body,
)

OK = Respond(200, completion_body())
UNAVAILABLE = Respond(503, {"error": {"code": 503}})
SCRIPTS: dict[str, list[ProviderStep]] = {
    "success": [OK],
    "unavailable-then-success": [UNAVAILABLE, OK],
}
# Labels only; the values themselves never appear in the outputs.
FORBIDDEN = {
    "synthetic_key": FAKE_PROVIDER_KEY,
    "authorization_header": "Authorization",
    "bearer_token": "Bearer",
    "system_prompt": "Analyze vulnerability reporting",
    "source_text": "actively exploited in the wild",
    "model_text": "Recent exploitation activity",
    "traceback": "Traceback",
    "exception_name": "Error",
    "timeout_name": "Timeout",
    "exception_word": "Exception",
}


class Scenario:
    """One isolated synthetic world with a fresh seeded random source."""

    def __init__(self, root: Path, script: list[ProviderStep]) -> None:
        seeded = random.Random(20261031)
        self.harness = Harness(root, script, random=seeded.random)
        self.job = self.harness.freeze()
        self.run = self.harness.admit(self.job)

    def worker(self, owner: str = "worker-1", **kwargs: Any):
        with synthetic_delays(self.harness.clock):
            try:
                return self.harness.run_worker(owner, **kwargs)
            except SimulatedCrash:
                return None

    def run_doc(self) -> dict[str, Any]:
        return self.harness.run_doc(self.run["run_id"])

    def status(self) -> dict[str, Any]:
        record = self.harness.store().load(self.job.manifest_digest)
        return job_status(record, self.run_doc(), now=self.harness.clock.now())

    def outcomes(self) -> list[list[str]]:
        record = self.harness.store().load(self.job.manifest_digest)
        if record is None:
            return []
        view = ledger_view(record)
        return [
            [o["disposition"] for o in view.outcomes(entry["seq"])]
            for entry in view.reservations
        ]


def crash_at(point: str) -> Callable[[str], Any]:
    remaining = [1]

    async def fault(name: str) -> None:
        if name == point and remaining[0]:
            remaining[0] -= 1
            raise SimulatedCrash(point)

    return fault


def summarize(scenario: Scenario, expectations: dict[str, bool]) -> dict[str, Any]:
    run = scenario.run_doc()
    status = scenario.status()
    return {
        "observed": scenario.harness.observe(scenario.job),
        "runtime_state": run["state"],
        "runtime_error_code": run.get("error_code"),
        "runtime_summary": run.get("error_summary"),
        "product_reason": status["product_reason"],
        "provider_intent": status["provider_intent"],
        "artifact_sha256": status["artifact_sha256"],
        "publication": status["publication"],
        "note": status["note"],
        "status": status,
        "expectations": expectations,
        "expectations_met": all(expectations.values()),
    }


def counts(scenario: Scenario, **expected: int) -> bool:
    observed = scenario.harness.observe(scenario.job)
    return all(observed[key] == value for key, value in expected.items())


def failed_with(scenario: Scenario, code: str, reason: str) -> bool:
    run = scenario.run_doc()
    summary = run.get("error_summary") or ""
    return (
        run["state"] == "failed"
        and run.get("error_code") == code
        and summary.split(" ")[0] == reason
    )


# Scenarios ------------------------------------------------------------------


def normal(root: Path) -> dict[str, Any]:
    scenario = Scenario(root, [OK])
    scenario.worker()
    return summarize(
        scenario,
        {
            "completed": scenario.run_doc()["state"] == "succeeded",
            "one_send": counts(scenario, R=1, F=1, A=1, P=0, C=1),
            "not_published": scenario.status()["publication"] == "not_published",
        },
    )


def ambiguity_in_process(root: Path) -> dict[str, Any]:
    scenario = Scenario(root, [AcceptThenFail(lambda: httpx.ReadTimeout("x")), OK])
    scenario.worker()
    return summarize(
        scenario,
        {
            "terminal_conflict": failed_with(
                scenario, "side_effect_conflict", "provider_intent_unresolved"
            ),
            "no_second_send": counts(scenario, R=1, F=1, A=1, P=0, C=1),
        },
    )


def ambiguity_after_restart(root: Path) -> dict[str, Any]:
    scenario = Scenario(root, [AcceptThenFail(lambda: SimulatedCrash("F3b")), OK])
    scenario.worker()
    scenario.harness.expire_lease()
    scenario.worker("worker-2")
    return summarize(
        scenario,
        {
            "terminal_conflict": failed_with(
                scenario, "side_effect_conflict", "provider_intent_unresolved"
            ),
            "no_resend_on_new_lease": counts(scenario, R=1, F=1, A=1, P=0, C=2),
        },
    )


def crash_after_reservation(root: Path) -> dict[str, Any]:
    scenario = Scenario(root, [OK])
    scenario.worker(fault=crash_at("after_reservation"))
    scenario.harness.expire_lease()
    scenario.worker("worker-2")
    return summarize(
        scenario,
        {
            "terminal_conflict": failed_with(
                scenario, "side_effect_conflict", "provider_intent_unresolved"
            ),
            "reserved_not_forwarded": counts(scenario, R=1, F=0, A=0, C=2),
            "reported_unresolved": scenario.status()["provider_intent"] == "unresolved",
        },
    )


def replay_success(root: Path, reference: str | None) -> dict[str, Any]:
    scenario = Scenario(root, [OK])
    scenario.worker(fault=crash_at("after_capture"))
    scenario.harness.expire_lease()
    scenario.worker("worker-2")
    digest = scenario.status()["artifact_sha256"]
    return summarize(
        scenario,
        {
            "completed": scenario.run_doc()["state"] == "succeeded",
            "replayed_without_send": counts(scenario, R=1, F=1, A=1, P=1, C=2),
            "same_artifact_as_uninterrupted_run": digest == reference,
        },
    )


def replay_unavailable(root: Path) -> dict[str, Any]:
    scenario = Scenario(root, [UNAVAILABLE, OK])
    scenario.worker(fault=crash_at("after_capture"))
    scenario.harness.expire_lease()
    scenario.worker("worker-2")
    return summarize(
        scenario,
        {
            "completed": scenario.run_doc()["state"] == "succeeded",
            "one_more_send": counts(scenario, R=2, F=2, A=2, P=1, C=2),
        },
    )


def budget_across_leases(root: Path) -> dict[str, Any]:
    retry_later = Respond(429, {"error": {"code": 429}}, {"Retry-After": "31"})
    scenario = Scenario(root, [UNAVAILABLE, retry_later, UNAVAILABLE, OK])
    scenario.worker(fault=crash_at("after_capture"))
    scenario.harness.expire_lease()
    second = scenario.worker("worker-2")
    scenario.harness.clock.advance(60)
    scenario.worker("worker-3")
    return summarize(
        scenario,
        {
            "deferred_between_leases": bool(
                second and second.reason == "provider_retry_after_deferred"
            ),
            "terminal_budget_exhausted": failed_with(
                scenario, "side_effect_conflict", "provider_budget_exhausted"
            ),
            "fourth_forward_blocked": counts(scenario, R=3, F=3, A=3, C=3),
        },
    )


def lost_completion_ack(root: Path) -> dict[str, Any]:
    scenario = Scenario(root, [OK])
    scenario.harness.runtime_service.drop_next_response("complete")
    first = scenario.worker()
    second = scenario.worker()
    return summarize(
        scenario,
        {
            "first_exit_nonzero": bool(first and first.exit_code == 1),
            "reconciled_by_reading": bool(second and second.reconciled == 1),
            "completed_once": scenario.run_doc()["state"] == "succeeded",
            "no_new_send_or_lease": counts(scenario, R=1, F=1, A=1, C=1),
        },
    )


def long_retry_after(root: Path) -> dict[str, Any]:
    long_wait = Respond(429, {"error": {"code": 429}}, {"Retry-After": "120"})
    scenario = Scenario(root, [long_wait, OK])
    scenario.worker()
    for _ in range(2):
        scenario.harness.clock.advance(5)
        scenario.worker("worker-2")
    status = scenario.status()
    return summarize(
        scenario,
        {
            "lease_exhaustion_reported": status["note"]
            == "lease_budget_exhausted_before_provider_not_before",
            "not_before_retained": status["not_before"] is not None,
            "no_early_send": counts(scenario, R=1, F=1, A=1, C=3),
        },
    )


def auth_rejected(root: Path) -> dict[str, Any]:
    scenario = Scenario(root, [UNAVAILABLE, Respond(401), OK])
    scenario.worker()
    return summarize(
        scenario,
        {
            "terminal_auth": failed_with(
                scenario, "invalid_input", "model_auth_rejected"
            ),
            "actual_count_reported": "reserved=2"
            in (scenario.run_doc().get("error_summary") or ""),
            "not_retried": counts(scenario, R=2, F=2, C=1),
        },
    )


def overload_529(root: Path) -> dict[str, Any]:
    body = {"error": {"code": 529, "message": "fake-secret-token PROMPT-MARKER"}}
    scenario = Scenario(root, [Respond(529, body), OK])
    scenario.worker()
    summary = scenario.run_doc().get("error_summary") or ""
    return summarize(
        scenario,
        {
            "terminal_rejection": failed_with(
                scenario, "invalid_input", "model_response_rejected"
            ),
            "sanitized": "fake-secret" not in summary and "PROMPT" not in summary,
            "not_retried": counts(scenario, R=1, F=1),
        },
    )


def grounding_rejected(root: Path) -> dict[str, Any]:
    scenario = Scenario(
        root, [Respond(200, completion_body(GROUNDING_REJECTED_REPORT))]
    )
    scenario.worker()
    return summarize(
        scenario,
        {
            "terminal_invalid_result": failed_with(
                scenario, "invalid_result", "report_grounding_rejected"
            ),
            "no_regeneration": counts(scenario, R=1, F=1),
            "no_artifact": scenario.status()["artifact_sha256"] is None,
        },
    )


def artifact_reuse(root: Path, reference: str | None) -> dict[str, Any]:
    scenario = Scenario(root, [OK])
    scenario.worker(fault=crash_at("after_artifact_record"))
    scenario.harness.expire_lease()
    scenario.worker("worker-2")
    return summarize(
        scenario,
        {
            "completed": scenario.run_doc()["state"] == "succeeded",
            "zero_extra_sends": counts(scenario, R=1, F=1, A=1, C=2),
            "same_artifact_as_uninterrupted_run": scenario.status()["artifact_sha256"]
            == reference,
        },
    )


def publication(root: Path) -> dict[str, Any]:
    scenario = Scenario(root, [OK])
    scenario.worker()
    publisher = FakePublisher(root / "publisher.json")
    publisher.lose_next_acknowledgement = True

    def publish(target: str) -> dict[str, Any]:
        return publish_prepared(
            store=scenario.harness.store(),
            job_id=scenario.job.manifest_digest,
            run=scenario.run_doc(),
            publisher=publisher,
            target=target,
        )

    first = publish("pages:preview")
    second = publish("pages:preview")
    publisher.seed("pages:other", "f" * 64)
    conflict = publish("pages:other")
    return summarize(
        scenario,
        {
            "ack_lost_then_observed": first["state"] == "unresolved"
            and second["state"] == "published",
            "single_effect": publisher.effects == 1,
            "conflict_fails_closed": conflict["state"] == "conflict",
            "no_provider_spend": counts(scenario, R=1, F=1, A=1, C=1),
        },
    )


def stale_before_forward(root: Path) -> dict[str, Any]:
    scenario = Scenario(root, [OK])
    harness = scenario.harness

    async def overlap():
        paused, release = asyncio.Event(), asyncio.Event()

        async def pause(name: str) -> None:
            if name == "after_reservation":
                paused.set()
                await release.wait()

        stale = asyncio.ensure_future(harness.worker(fault=pause).run_once())
        await paused.wait()
        harness.expire_lease()
        newer = await harness.worker(owner="worker-2").run_once()
        release.set()
        return newer, await stale

    with synthetic_delays(harness.clock):
        newer, stale = asyncio.run(overlap())
    return summarize(
        scenario,
        {
            "newer_lease_stops": newer.reason == "provider_intent_unresolved",
            "stale_exits": stale.outcome == "lease_lost",
            "stale_forward_refused": counts(scenario, R=1, F=0, A=0, C=2),
        },
    )


def stale_after_forward(root: Path) -> dict[str, Any]:
    release = asyncio.Event()
    scenario = Scenario(root, [AcceptThenWait(release, OK), OK])
    harness = scenario.harness

    async def overlap():
        stale = asyncio.ensure_future(harness.worker().run_once())
        while harness.provider.accepted == 0:
            await asyncio.sleep(0)
        harness.expire_lease()
        newer = await harness.worker(owner="worker-2").run_once()
        release.set()
        return newer, await stale

    with synthetic_delays(harness.clock):
        newer, stale = asyncio.run(overlap())
    return summarize(
        scenario,
        {
            "newer_lease_stops": newer.reason == "provider_intent_unresolved",
            "stale_exits": stale.outcome == "lease_lost",
            "request_could_not_be_retracted": counts(scenario, R=1, F=1, A=1, C=2),
            "late_outcome_retained_not_promoted": scenario.outcomes()
            == [["ambiguous", "resolved"]]
            and scenario.status()["artifact_sha256"] is None,
        },
    )


def separate_process(root: Path, reference: str | None) -> dict[str, Any]:
    scenario = Scenario(root, [OK])
    crashed = subprocess.run(
        [
            sys.executable,
            str(Path(__file__).resolve()),
            "crash-worker",
            "--root",
            str(root),
            "--script",
            "success",
            "--fault",
            "after_capture",
        ],
        capture_output=True,
        text=True,
        timeout=300,
    )
    scenario.harness.expire_lease()
    scenario.worker("worker-2")
    return summarize(
        scenario,
        {
            "first_process_died": crashed.returncode == 137,
            "replayed_without_send": counts(scenario, R=1, F=1, A=1, P=1, C=2),
            "same_artifact_as_uninterrupted_run": scenario.status()["artifact_sha256"]
            == reference,
        },
    )


def run_scenarios(worlds: Path) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []

    def record(scenario_id: str, title: str, outcome: dict[str, Any]) -> None:
        results.append(dict({"id": scenario_id, "title": title}, **outcome))

    baseline = normal(worlds / "N0")
    reference = baseline["artifact_sha256"]
    record("N0", "uninterrupted completion", baseline)
    for scenario_id, title, function in (
        ("A1", "accepted request, response lost, same process", ambiguity_in_process),
        ("A2", "accepted request, process died, new lease", ambiguity_after_restart),
        ("A4", "crash after reservation, before forwarding", crash_after_reservation),
        ("A7", "captured 503 replayed, then one real send", replay_unavailable),
        ("B1", "budget bounded across crash and leases", budget_across_leases),
        ("B3", "completion acknowledgement lost", lost_completion_ack),
        ("C5", "Retry-After longer than the lease budget", long_retry_after),
        ("D5", "auth rejected after an earlier transient", auth_rejected),
        ("D6", "529 carrying secret text", overload_529),
        ("E4", "grounding rejection", grounding_rejected),
        ("E6", "publication ack lost, then conflict", publication),
        ("O2", "stale process paused before forwarding", stale_before_forward),
        ("O3", "stale forward already handed to the provider", stale_after_forward),
    ):
        record(scenario_id, title, function(worlds / scenario_id))
    for scenario_id, title, function in (
        ("A6", "captured success replayed after a crash", replay_success),
        ("E5", "crash after artifact record, artifact reused", artifact_reuse),
        ("SP1", "separate OS process crash at capture", separate_process),
    ):
        record(scenario_id, title, function(worlds / scenario_id, reference))
    return results


def render_table(results: list[dict[str, Any]]) -> str:
    rows = [
        "| id | scenario | R | F | A | P | C | Runtime | code | reason | "
        "artifact | publication | expectations |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for result in results:
        observed = result["observed"]
        artifact = result["artifact_sha256"]
        rows.append(
            "| {id} | {title} | {R} | {F} | {A} | {P} | {C} | {state} | {code} | "
            "{reason} | {artifact} | {publication} | {met} |".format(
                id=result["id"],
                title=result["title"],
                state=result["runtime_state"],
                code=result["runtime_error_code"] or "-",
                reason=result["product_reason"] or "-",
                artifact=artifact[:12] if artifact else "-",
                publication=result["publication"],
                met="met" if result["expectations_met"] else "NOT MET",
                **{key: observed[key] for key in "RFAPC"},
            )
        )
    return (
        "R reserved submissions (not a billing count), F forwards to the fake "
        "provider, A fake provider acceptances, P captured-outcome replays, "
        "C Runtime leases granted.\n\n" + "\n".join(rows) + "\n"
    )


def scan(texts: list[str], extra: dict[str, str]) -> list[str]:
    markers = dict(FORBIDDEN, **extra)
    return sorted(
        label for label, value in markers.items() if any(value in t for t in texts)
    )


def command_run(output_dir: Path) -> int:
    output_dir = output_dir.resolve()
    if output_dir.is_relative_to(REPO_ROOT):
        print("refusing an output directory inside the repository")
        return 2
    if output_dir.exists() and any(output_dir.iterdir()):
        print("refusing a non-empty output directory")
        return 2
    results = run_scenarios(output_dir / "worlds")
    table = render_table(results)
    summary: dict[str, Any] = {
        "kind": "sentryinsight runtime adapter synthetic recovery demo",
        "fakes_only": True,
        "scenarios": results,
        "all_expectations_met": all(r["expectations_met"] for r in results),
    }
    body = json.dumps(summary, indent=2, sort_keys=True)
    found = scan([body, table], {"output_path": str(output_dir)})
    summary["scan"] = {"forbidden_markers_found": found}
    (output_dir / "result.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    (output_dir / "table.md").write_text(table)
    print(table)
    print(
        "all expectations met"
        if summary["all_expectations_met"] and not found
        else "expectations NOT met"
    )
    return 0 if summary["all_expectations_met"] and not found else 1


def command_crash_worker(root: Path, script: str, fault_point: str) -> int:
    harness = Harness(root, SCRIPTS[script])

    async def die(name: str) -> None:
        if name == fault_point:
            os._exit(137)

    with synthetic_delays(harness.clock):
        harness.run_worker(fault=die)
    return 0


def command_status(root: Path) -> int:
    harness = Harness(root)
    runs = {run["run_id"]: run for run in harness.runtime_service.runs()}
    store = harness.store()
    for job_id in store.job_ids():
        record = store.load(job_id)
        run = runs.get(record["run_id"]) if record else None
        print(render_status(job_status(record, run, now=harness.clock.now())))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Local synthetic recovery demo for the durable execution adapter."
    )
    commands = parser.add_subparsers(dest="command", required=True)
    run = commands.add_parser("run", help="Run every synthetic scenario.")
    run.add_argument("--output-dir", type=Path, required=True)
    crash = commands.add_parser("crash-worker", help="Run a worker that dies.")
    crash.add_argument("--root", type=Path, required=True)
    crash.add_argument("--script", choices=sorted(SCRIPTS), required=True)
    crash.add_argument("--fault", required=True)
    status = commands.add_parser("status", help="Print status for a demo world.")
    status.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "run":
        return command_run(args.output_dir)
    if args.command == "crash-worker":
        return command_crash_worker(args.root, args.script, args.fault)
    return command_status(args.root)


if __name__ == "__main__":
    raise SystemExit(main())
