#!/usr/bin/env python3
"""Send one fixed Vertex-only Argon request after two consumed prior trials."""

from __future__ import annotations

import argparse
import asyncio
from dataclasses import replace
import json
import os
from pathlib import Path
import sys
from typing import Callable

import httpx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def helpers():
    from scripts import verify_selected_models_once

    return verify_selected_models_once


base = helpers()
PRIOR_RUNS = [
    {
        "run_id": "41777105615",
        "executor_commit": "26234bd3f1cd7e580c739c019c50bf217ed13d84",
        "case": "sentry",
    },
    {
        "run_id": "41778423600",
        "executor_commit": "f72903e6b4d1370f988044df00abe6286fcce1a1",
        "case": "grc_ai_studio",
    },
]
VERTEX_SPEC = replace(
    base.CASES[base.Case.GRC],
    provider="google-vertex/global",
    canonical_sha="a392d628f3a09a0ad2a272c80a9f155dadb53b8388b928be877fc1f1b38b4c96",
    wire_sha="655631707443f06f4e4efdc0266950a506b48ce8be2a8340a7f3f30adff39870",
    wire_bytes=17236,
)


def validate_vertex_wire(wire: bytes) -> base.PreparedTrial:
    base.require(
        type(wire) is bytes
        and len(wire) == VERTEX_SPEC.wire_bytes
        and base.sha(wire) == VERTEX_SPEC.wire_sha,
        "wire_refused",
    )
    payload = json.loads(wire)
    base.require(
        base.sha(base.canonical(payload)) == VERTEX_SPEC.canonical_sha
        and payload["provider"]["only"] == [VERTEX_SPEC.provider]
        and wire.count(b'"google-vertex/global"') == 1,
        "wire_refused",
    )
    # This exact inverse recovers the approved prior bytes, proving a provider-only change.
    original = wire.replace(b'"google-vertex/global"', b'"google-ai-studio"')
    base.validate_wire(base.Case.GRC, original)
    return base.PreparedTrial(VERTEX_SPEC, wire)


def vertex_metadata(raw: bytes) -> dict:
    payload = json.loads(raw)
    provider = payload.get("provider")
    base.require(provider in (None, "Google"), "provider_refused")
    # The shared checker owns completeness/tier/billing; optional attestation was checked above.
    payload.pop("provider", None)
    result = base.response_metadata(base.Case.GRC, base.canonical(payload))
    result["serving_provider"] = "Google" if provider == "Google" else None
    return result


class VertexClaim(base.Claim):
    """The first durable state consumes both prior allocations permanently."""

    def _initial_value(self, context: base.Context) -> dict:
        value = super()._initial_value(context)
        value["states"] = {
            "sentry": "consumed_prior_run",
            "grc_ai_studio": "consumed_prior_run",
            "grc": "pending",
        }
        value["prior_runs"] = [dict(row) for row in PRIOR_RUNS]
        value["requests"]["grc_ai_studio"] = dict(value["requests"]["grc"])
        value["requests"]["grc"].update(
            requested_provider=VERTEX_SPEC.provider,
            canonical_payload_sha256=VERTEX_SPEC.canonical_sha,
            wire_sha256=VERTEX_SPEC.wire_sha,
        )
        value["reserved_microusd"] = 608000
        return value

    def _save(self):
        base.require(
            self.value["states"]["sentry"] == "consumed_prior_run"
            and self.value["states"]["grc_ai_studio"] == "consumed_prior_run"
            and self.value["prior_runs"] == PRIOR_RUNS
            and self.value["reserved_microusd"] == 608000
            and self.value["requests"]["grc"]["requested_provider"]
            == VERTEX_SPEC.provider
            and self.value["requests"]["grc"]["wire_sha256"] == VERTEX_SPEC.wire_sha,
            "continuation_claim_refused",
        )
        super()._save()

    def start(self, case: base.Case):
        base.require(case is base.Case.GRC, "consumed_allocation_refused")
        super().start(case)

    def finish(self, case: base.Case, state: str):
        base.require(case is base.Case.GRC, "consumed_allocation_refused")
        super().finish(case, state)


def prepare_vertex(layout: base.Layout) -> base.PreparedTrial:
    before = base.source_snapshot(layout)
    wire = asyncio.run(base._worker(layout, base.Case.GRC, "prepare_vertex"))
    prepared = validate_vertex_wire(wire)
    base.require(before == base.source_snapshot(layout), "source_changed")
    return prepared


def execute_vertex(
    prepared: base.PreparedTrial,
    layout: base.Layout,
    context: base.Context,
    claim_path: Path,
    read_key: Callable[[], str],
    client: httpx.Client,
) -> dict:
    spec = VERTEX_SPEC
    base.require(prepared.spec is spec, "preparation_refused")
    validate_vertex_wire(prepared.wire)
    before = base.source_snapshot(layout)
    row: dict = {
        "case": "grc_vertex",
        "requested_model": spec.model,
        "requested_provider": spec.provider,
        "source_sha": spec.source_sha,
        "fixture_sha256": spec.fixture_sha,
        "canonical_payload_sha256": spec.canonical_sha,
        "wire_sha256": spec.wire_sha,
        "http_status": None,
        "outcome": "uncertain",
        "usage": None,
    }
    with VertexClaim(claim_path, context) as claim:
        key = read_key()
        base.require(type(key) is str and bool(key.strip()), "credential_unavailable")
        base.require(before == base.source_snapshot(layout), "source_changed")
        claim.start(base.Case.GRC)
        known_response = False
        try:
            with client.stream(
                "POST",
                base.ENDPOINT,
                content=prepared.wire,
                headers={
                    "Authorization": "Bearer " + key,
                    "Content-Type": "application/json",
                    "X-Title": "Fixed fictional model verification",
                },
                follow_redirects=False,
            ) as response:
                row["http_status"] = response.status_code
                if response.status_code != 200:
                    claim.finish(base.Case.GRC, "http_error")
                    row["outcome"] = "http_error"
                else:
                    body = bytearray()
                    for block in response.iter_bytes(chunk_size=65536):
                        body.extend(block)
                        base.require(
                            len(body) <= base.RESPONSE_LIMIT, "response_too_large"
                        )
                    metadata = vertex_metadata(bytes(body))
                    row.update(metadata)
                    claim.finish(base.Case.GRC, "response_received")
                    known_response = True
        except Exception:
            if claim.value["states"]["grc"] == "sending":
                claim.finish(base.Case.GRC, "uncertain")
            row["outcome"] = "transport_or_protocol_unknown"
        if known_response:
            try:
                host = json.loads(
                    asyncio.run(
                        base._worker(
                            layout, base.Case.GRC, "validate_vertex", bytes(body)
                        )
                    )
                )
                host = base.validate_host_metadata(base.Case.GRC, host)
                row["host"] = host
                row["outcome"] = (
                    "passed"
                    if host["outcome"] == "passed"
                    else "host_validation_failed"
                )
                if not base.continuation_known(metadata):
                    row["outcome"] = "accounting_or_tier_unknown"
            except Exception:
                row["host"] = {"outcome": "failed", "stage": "replay_unavailable"}
                row["outcome"] = "replay_unknown"
        base.require(before == base.source_snapshot(layout), "source_changed")
    usage = row.get("usage")
    actual_cost = usage.get("cost") if isinstance(usage, dict) else None
    return {
        "schema_version": 1,
        "run_id": context.run_id,
        "executor_commit": context.commit,
        "prior_runs": PRIOR_RUNS,
        "prior_sentry_state": "consumed_prior_run",
        "prior_ai_studio_state": "consumed_prior_run",
        "prior_ai_studio_cost": None,
        "actual_combined_cost": None,
        "ceiling_usd": 2,
        "upper_estimate_usd": 0.608,
        "prior_admission_bound_usd": 0.484,
        "remaining_admission_bound_usd": 0.124,
        "actual_cost": actual_cost,
        "cost_scope": "this_vertex_request_only",
        "cases": [row],
        "published": False,
        "production_ready": False,
    }


def ci_layout() -> base.Layout:
    workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    return base.Layout(
        workspace / "sources/sentry",
        workspace / "sources/grc",
        workspace / "sources/sentry/.venv/bin/python",
        workspace / "sources/grc/agent/.venv/bin/python",
        Path(os.environ["TIKTOKEN_CACHE_DIR"]),
    )


def calibrate_ci() -> None:
    """Credential-free workflow step; no live mode or case selector."""
    prepared = prepare_vertex(ci_layout())
    base.write_metadata(
        Path(os.environ["RUNNER_TEMP"]) / "selected-model-trial/calibration.json",
        {
            "outcome": "calibration_passed",
            "live_attempts": 0,
            "prior_runs": PRIOR_RUNS,
            "cases": {
                "grc_vertex": {
                    "wire_sha256": prepared.spec.wire_sha,
                    "canonical_payload_sha256": prepared.spec.canonical_sha,
                }
            },
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-commit", required=True)
    args = parser.parse_args()
    os.umask(0o077)
    try:
        context = base.validate_context(os.environ, args.expected_commit)
        base.require(
            base.git(ROOT, "rev-parse", "HEAD").decode().strip() == context.commit
            and not base.git(
                ROOT, "status", "--porcelain", "--untracked-files=no"
            ).strip(),
            "executor_changed",
        )
        directory = Path(os.environ["RUNNER_TEMP"]).resolve() / "selected-model-trial"
        base.require(
            directory.is_dir() and directory.resolve() == directory, "output_refused"
        )
        layout = ci_layout()
        with httpx.Client(
            transport=httpx.HTTPTransport(retries=0, trust_env=False), timeout=30
        ) as control:
            history = base.public_json(
                control,
                f"repos/{base.REPOSITORY}/actions/workflows/verify-nemotron.yml/runs",
                {
                    "event": "workflow_dispatch",
                    "head_sha": context.commit,
                    "per_page": 100,
                },
            )
            base.validate_prior_runs(context, history)
            before = base.remote_snapshot(control)
            prepared = prepare_vertex(layout)
            with httpx.Client(
                transport=httpx.HTTPTransport(retries=0, trust_env=False), timeout=1800
            ) as sender:
                receipt = execute_vertex(
                    prepared,
                    layout,
                    context,
                    directory / "claim.json",
                    lambda: os.environ.get("OPENROUTER_API_KEY", ""),
                    sender,
                )
            try:
                receipt["remote_reports_unchanged"] = before == base.remote_snapshot(
                    control
                )
            except base.TrialError:
                receipt["remote_reports_unchanged"] = None
            receipt["remote_main_commits"] = base.REMOTE_MAIN
            receipt["remote_report_snapshot_sha256"] = base.sha(base.canonical(before))
            base.write_metadata(directory / "trial.json", receipt)
        return (
            0
            if receipt["remote_reports_unchanged"]
            and receipt["cases"][0]["outcome"] == "passed"
            else 1
        )
    except BaseException:
        print("Continuation stopped; inspect sanitized claim and run before any retry.")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
