from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
VERIFIER = REPO_ROOT / "contracts" / "reporting-identity-verifier-v1.py"
VERIFIER_SHA256 = "1d2d2288de826cd45fc72ad3e95e86474fbb72ec4b104a305db17f3b3b32081b"


def run_verifier(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VERIFIER), *args],
        cwd=REPO_ROOT,
        capture_output=True,
        check=False,
        text=True,
    )


def test_verifier_is_the_immutable_owner_copy():
    assert hashlib.sha256(VERIFIER.read_bytes()).hexdigest() == VERIFIER_SHA256


FETCH_HELPER = REPO_ROOT / "scripts" / "fetch_reporting_identity.py"


def run_fetch_helper(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(FETCH_HELPER), *args],
        cwd=REPO_ROOT,
        capture_output=True,
        check=False,
        text=True,
    )


def test_verifier_keeps_unavailability_distinct_from_drift(tmp_path):
    unavailable = run_verifier(
        "fetch",
        "--artifact",
        "verifier",
        "--canonical-output",
        str(tmp_path / "canonical.py"),
        "--canonical-url",
        "http://127.0.0.1:9/unavailable",
        "--attempts",
        "1",
        "--timeout-seconds",
        "0.1",
    )
    assert unavailable.returncode == 2
    assert "Canonical reporting identity verifier unavailable" in unavailable.stderr
    assert "drift" not in unavailable.stderr

    canonical = tmp_path / "canonical.py"
    canonical.write_text("different\n")
    drift = run_verifier(
        "compare",
        "--artifact",
        "verifier",
        "--local-artifact",
        str(VERIFIER),
        "--canonical-artifact",
        str(canonical),
    )
    assert drift.returncode == 3
    assert "Reporting Identity Verifier drift" in drift.stderr
    assert "unavailable" not in drift.stderr


@pytest.mark.parametrize(
    ("artifact", "local_relpath"),
    [
        ("verifier", "contracts/reporting-identity-verifier-v1.py"),
        ("contract", "contracts/reporting-identity-v1.json"),
    ],
)
def test_fetch_helper_falls_back_to_digest_verified_pinned_copy(
    tmp_path, artifact, local_relpath
):
    output = tmp_path / f"canonical-{artifact}"
    result = run_fetch_helper(
        "--artifact",
        artifact,
        "--canonical-output",
        str(output),
        "--canonical-url",
        "http://127.0.0.1:9/unavailable",
        "--rounds",
        "2",
        "--backoff-seconds",
        "0",
        "--attempts",
        "1",
        "--timeout-seconds",
        "0.1",
    )
    assert result.returncode == 0, result.stdout + result.stderr
    local_path = REPO_ROOT / local_relpath
    assert output.read_bytes() == local_path.read_bytes()
    assert "::warning title=Canonical reporting identity" in result.stderr
    advisory_line = next(
        line
        for line in result.stdout.splitlines()
        if line.startswith("Reporting identity advisory: ")
    )
    advisory = json.loads(advisory_line.split("Reporting identity advisory: ", 1)[1])
    assert advisory["code"] == "canonical_identity_fetch_fallback"
    assert advisory["artifact"] == artifact
    assert advisory["fallback"] == "pinned_local"
    assert advisory["sha256"] == hashlib.sha256(local_path.read_bytes()).hexdigest()

    compared = run_verifier(
        "compare",
        "--artifact",
        artifact,
        "--local-artifact",
        str(local_path),
        "--canonical-artifact",
        str(output),
    )
    assert compared.returncode == 0, compared.stdout + compared.stderr


def test_fetch_helper_retries_and_succeeds_without_fallback_when_upstream_recovers(
    tmp_path,
):
    state_file = tmp_path / "calls.txt"
    fake_verifier = tmp_path / "fake-verifier.py"
    fake_verifier.write_text(
        "import pathlib, sys\n"
        f"state = pathlib.Path({str(state_file)!r})\n"
        "count = int(state.read_text()) + 1 if state.exists() else 1\n"
        "state.write_text(str(count))\n"
        "out = pathlib.Path(sys.argv[sys.argv.index('--canonical-output') + 1])\n"
        "if count < 2:\n"
        "    raise SystemExit(2)\n"
        "out.write_text('live canonical payload\\n')\n"
    )
    output = tmp_path / "canonical.json"
    result = run_fetch_helper(
        "--artifact",
        "contract",
        "--verifier",
        str(fake_verifier),
        "--canonical-output",
        str(output),
        "--rounds",
        "3",
        "--backoff-seconds",
        "0",
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert output.read_text() == "live canonical payload\n"
    assert state_file.read_text() == "2"
    assert "Reporting identity advisory:" not in result.stdout


def test_fetch_helper_refuses_tampered_pinned_copy(tmp_path):
    tampered = tmp_path / "tampered.json"
    tampered.write_text("tampered content\n")
    output = tmp_path / "canonical.json"
    result = run_fetch_helper(
        "--artifact",
        "contract",
        "--canonical-output",
        str(output),
        "--canonical-url",
        "http://127.0.0.1:9/unavailable",
        "--pinned-artifact",
        str(tampered),
        "--rounds",
        "1",
        "--backoff-seconds",
        "0",
        "--attempts",
        "1",
        "--timeout-seconds",
        "0.1",
    )
    assert result.returncode == 3
    assert "digest mismatch" in result.stderr
    assert not output.exists()


def test_fetch_helper_fails_closed_on_non_unavailable_error(tmp_path):
    failing_verifier = tmp_path / "failing-verifier.py"
    failing_verifier.write_text("raise SystemExit(1)\n")
    output = tmp_path / "canonical.json"
    result = run_fetch_helper(
        "--artifact",
        "contract",
        "--verifier",
        str(failing_verifier),
        "--canonical-output",
        str(output),
        "--rounds",
        "3",
        "--backoff-seconds",
        "0",
    )
    assert result.returncode == 1
    assert not output.exists()


def test_workflows_wire_reporting_identity_fallback():
    for workflow_name in ("generate-report.yml", "validate.yml"):
        workflow = (REPO_ROOT / ".github" / "workflows" / workflow_name).read_text()
        assert workflow.count("python3 scripts/fetch_reporting_identity.py") == 2
