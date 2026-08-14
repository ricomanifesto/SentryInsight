from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import sys

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
