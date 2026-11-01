"""Status view, separate-process recovery and the synthetic demo."""

import asyncio
import json
import subprocess
import sys

import pytest

from src.runtime_adapter.fakes import Respond, SimulatedCrash
from src.runtime_adapter.harness import Harness
from src.runtime_adapter.identity import REPO_ROOT
from src.runtime_adapter.status import job_status, render_status
from src.runtime_adapter.synthetic import FAKE_PROVIDER_KEY, completion_body

DEMO = REPO_ROOT / "scripts" / "runtime_adapter_demo.py"
FORBIDDEN = (
    FAKE_PROVIDER_KEY,
    "Authorization",
    "Bearer",
    "Analyze vulnerability reporting",  # system prompt
    "actively exploited in the wild",  # source text
    "Recent exploitation activity",  # model text
    "Traceback",
    "Error",
    "Timeout",
    "Exception",
)


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    async def sleep(*_args, **_kwargs):
        return None

    monkeypatch.setattr(asyncio, "sleep", sleep)


def world(tmp_path, script=(Respond(200, completion_body()),)):
    harness = Harness(tmp_path / "world", script)
    job = harness.freeze()
    run = harness.admit(job)
    return harness, job, run


def status_of(harness, job, run):
    return job_status(
        harness.store().load(job.manifest_digest),
        harness.run_doc(run["run_id"]),
        now=harness.clock.now(),
    )


def assert_clean(text, *extra):
    for marker in FORBIDDEN + extra:
        assert marker not in text, marker


def test_status_distinguishes_prepared_from_published_and_reserved_from_billed(
    tmp_path,
):
    harness, job, run = world(tmp_path)
    harness.run_worker()

    status = status_of(harness, job, run)
    table = render_status(status)

    assert status["run_state"] == "succeeded"
    assert status["product_stage"] == "completed"
    assert (status["reserved"], status["budget_remaining"]) == (1, 2)
    assert (status["known_outcomes"], status["uncertain_provider_acceptance"]) == (1, 0)
    assert status["publication"] == "not_published"
    assert (
        status["artifact_sha256"]
        == harness.run_doc(run["run_id"])["output_ref"]["artifact_sha256"]
    )
    assert "reserved provider submissions (not a billing count)" in table
    assert "prepared artifact (not published)" in table
    assert "billed" not in table.replace("not a billing count", "")
    assert_clean(table, str(tmp_path))


def test_stopped_worker_state_reads_back_as_unresolved_not_billed(tmp_path):
    harness, job, run = world(tmp_path)

    async def crash(name):
        if name == "after_reservation":
            raise SimulatedCrash(name)

    with pytest.raises(SimulatedCrash):
        harness.run_worker(fault=crash)
    harness.clock.advance(10_000)

    status = status_of(harness, job, run)

    # No progress is implied without claim traffic.
    assert status["run_state"] == "running"
    assert status["uncertain_provider_acceptance"] == 1
    assert status["provider_intent"] == "unresolved"
    assert status["known_outcomes"] == 0
    assert "unresolved" in render_status(status)


def test_status_reports_lease_exhaustion_before_not_before_honestly(tmp_path):
    long_wait = Respond(429, {"error": {"code": 429}}, {"Retry-After": "120"})
    harness, job, run = world(tmp_path, [long_wait])
    harness.run_worker()
    for _ in range(2):
        harness.clock.advance(5)
        harness.run_worker()

    status = status_of(harness, job, run)

    assert status["run_state"] == "failed"
    assert status["leases_remaining"] == 0
    assert status["not_before"] is not None
    assert status["note"] == "lease_budget_exhausted_before_provider_not_before"
    assert "recovered" not in render_status(status)


def test_crash_in_a_separate_process_is_recovered_by_a_fresh_worker(tmp_path):
    harness, job, run = world(tmp_path)

    crashed = subprocess.run(
        [
            sys.executable,
            str(DEMO),
            "crash-worker",
            "--root",
            str(harness.root),
            "--script",
            "success",
            "--fault",
            "after_capture",
        ],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert crashed.returncode == 137, crashed.stderr
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}
    harness.expire_lease()

    assert harness.run_worker(owner="worker-2").outcome == "completed"

    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 1, "C": 2}
    assert harness.run_doc(run["run_id"])["state"] == "succeeded"


def test_demo_refuses_an_output_directory_inside_the_repository():
    result = subprocess.run(
        [sys.executable, str(DEMO), "run", "--output-dir", str(REPO_ROOT / "demo")],
        capture_output=True,
        text=True,
        timeout=60,
    )

    assert result.returncode == 2
    assert not (REPO_ROOT / "demo").exists()


def test_demo_runs_every_scenario_and_writes_clean_outputs(tmp_path):
    output = tmp_path / "demo"

    result = subprocess.run(
        [sys.executable, str(DEMO), "run", "--output-dir", str(output)],
        capture_output=True,
        text=True,
        timeout=600,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    summary = json.loads((output / "result.json").read_text())
    assert summary["all_expectations_met"] is True
    ids = {scenario["id"] for scenario in summary["scenarios"]}
    for required in ("A1", "A2", "A6", "B1", "E5", "E6", "SP1"):
        assert required in ids
    for scenario in summary["scenarios"]:
        assert scenario["expectations_met"] is True, scenario["id"]
        observed = scenario["observed"]
        if observed.get("R") is not None:
            assert observed["R"] <= 3
            assert observed["F"] <= observed["R"]
    exported = (
        (output / "result.json").read_text()
        + (output / "table.md").read_text()
        + result.stdout
    )
    assert_clean(exported, str(output), str(tmp_path))
    assert summary["scan"] == {"forbidden_markers_found": []}


def test_adapter_imports_do_not_configure_logging_or_logfire():
    script = """
import logging
import logfire

root_logger = logging.getLogger()
root_logger.handlers.clear()


def refuse(*_args, **_kwargs):
    raise SystemExit("adapter import configured Logfire")


logfire.configure = refuse
logfire.instrument_httpx = refuse

import src.runtime_adapter.worker
import src.runtime_adapter.harness
import src.runtime_adapter.status
import src.runtime_adapter.publication

if root_logger.handlers:
    raise SystemExit("adapter import configured root logging")
"""
    result = subprocess.run(
        [sys.executable, "-c", script], capture_output=True, text=True, check=False
    )

    assert result.returncode == 0, result.stderr
