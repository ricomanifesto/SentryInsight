#!/usr/bin/env python3
"""Retry canonical reporting identity fetches and fall back to digest-verified repo copies."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VERIFIER = REPO_ROOT / "contracts" / "reporting-identity-verifier-v1.py"
UNAVAILABLE_EXIT_CODE = 2
DRIFT_EXIT_CODE = 3

# Exact SHA-256 digests of the immutable owner-maintained artifacts pinned in
# this repository. Fallback refuses any file whose digest differs.
PINNED_ARTIFACTS: dict[str, tuple[Path, str]] = {
    "verifier": (
        REPO_ROOT / "contracts" / "reporting-identity-verifier-v1.py",
        "1d2d2288de826cd45fc72ad3e95e86474fbb72ec4b104a305db17f3b3b32081b",
    ),
    "contract": (
        REPO_ROOT / "contracts" / "reporting-identity-v1.json",
        "16c52db11b981aba115f4a1a127458def99b809c3e768028bebb66b880e33671",
    ),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch_with_fallback(
    *,
    artifact: str,
    canonical_output: Path,
    verifier: Path = DEFAULT_VERIFIER,
    canonical_url: str | None = None,
    pinned_artifact: Path | None = None,
    expected_sha256: str | None = None,
    rounds: int = 3,
    backoff_seconds: float = 5.0,
    attempts: int = 5,
    timeout_seconds: float = 15.0,
) -> int:
    if rounds < 1:
        raise ValueError("rounds must be positive")
    default_pinned, default_digest = PINNED_ARTIFACTS[artifact]
    pinned_path = pinned_artifact or default_pinned
    expected_digest = (expected_sha256 or default_digest).lower()

    command = [
        sys.executable,
        str(verifier),
        "fetch",
        "--artifact",
        artifact,
        "--canonical-output",
        str(canonical_output),
        "--attempts",
        str(attempts),
        "--timeout-seconds",
        str(timeout_seconds),
    ]
    if canonical_url:
        command.extend(["--canonical-url", canonical_url])

    for round_index in range(rounds):
        result = subprocess.run(command, check=False)
        if result.returncode == 0:
            return 0
        if result.returncode != UNAVAILABLE_EXIT_CODE:
            return result.returncode
        if round_index + 1 < rounds and backoff_seconds > 0:
            time.sleep(backoff_seconds * (2**round_index))

    try:
        pinned_bytes = pinned_path.read_bytes()
    except OSError:
        print(
            f"::error title=Pinned reporting identity {artifact} unreadable::"
            f"Pinned fallback {pinned_path} could not be read; release remains blocked.",
            file=sys.stderr,
        )
        return DRIFT_EXIT_CODE

    actual_digest = sha256_bytes(pinned_bytes)
    if actual_digest != expected_digest:
        print(
            f"::error title=Pinned reporting identity {artifact} digest mismatch::"
            f"Pinned fallback SHA-256 {actual_digest} does not match expected "
            f"{expected_digest}; release remains blocked.",
            file=sys.stderr,
        )
        return DRIFT_EXIT_CODE

    canonical_output.parent.mkdir(parents=True, exist_ok=True)
    canonical_output.write_bytes(pinned_bytes)
    advisory = {
        "code": "canonical_identity_fetch_fallback",
        "artifact": artifact,
        "fallback": "pinned_local",
        "sha256": actual_digest,
        "rounds": rounds,
    }
    print(
        f"::warning title=Canonical reporting identity {artifact} unavailable::"
        f"Falling back to digest-verified pinned copy (SHA-256 {actual_digest}).",
        file=sys.stderr,
    )
    print(f"Reporting identity advisory: {json.dumps(advisory, sort_keys=True)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Retry canonical reporting identity artifact fetches with backoff, "
            "falling back to a digest-verified pinned copy on unavailability."
        )
    )
    parser.add_argument("--artifact", choices=sorted(PINNED_ARTIFACTS), required=True)
    parser.add_argument("--canonical-output", type=Path, required=True)
    parser.add_argument("--verifier", type=Path, default=DEFAULT_VERIFIER)
    parser.add_argument("--canonical-url")
    parser.add_argument("--pinned-artifact", type=Path)
    parser.add_argument("--expected-sha256")
    parser.add_argument("--rounds", type=int, default=3)
    parser.add_argument("--backoff-seconds", type=float, default=5.0)
    parser.add_argument("--attempts", type=int, choices=range(1, 6), default=5)
    parser.add_argument("--timeout-seconds", type=float, default=15.0)
    args = parser.parse_args()
    return fetch_with_fallback(
        artifact=args.artifact,
        canonical_output=args.canonical_output,
        verifier=args.verifier,
        canonical_url=args.canonical_url,
        pinned_artifact=args.pinned_artifact,
        expected_sha256=args.expected_sha256,
        rounds=args.rounds,
        backoff_seconds=args.backoff_seconds,
        attempts=args.attempts,
        timeout_seconds=args.timeout_seconds,
    )


if __name__ == "__main__":
    raise SystemExit(main())
