#!/usr/bin/env python3
"""Fetch and compare versioned Sentry reporting identity artifacts."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

CANONICAL_ROOT = (
    "https://raw.githubusercontent.com/ricomanifesto/SentryDigest/" "main/contracts"
)
CANONICAL_URLS = {
    "contract": f"{CANONICAL_ROOT}/reporting-identity-v1.json",
    "verifier": f"{CANONICAL_ROOT}/reporting-identity-verifier-v1.py",
}
ARTIFACT_LABELS = {
    "contract": "reporting identity contract",
    "verifier": "reporting identity verifier",
}
MAX_ARTIFACT_BYTES = 1_000_000
DEFAULT_ATTEMPTS = 4
UNAVAILABLE_EXIT_CODE = 2
DRIFT_EXIT_CODE = 3


class CanonicalArtifactUnavailable(RuntimeError):
    """The canonical artifact could not be read safely."""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch_canonical_artifact(
    url: str, timeout_seconds: float, attempts: int = DEFAULT_ATTEMPTS
) -> bytes:
    if attempts < 1:
        raise ValueError("attempts must be positive")
    request = Request(url, headers={"User-Agent": "Sentry-reporting-verifier/1"})
    for attempt in range(attempts):
        try:
            with urlopen(request, timeout=timeout_seconds) as response:  # noqa: S310
                content = response.read(MAX_ARTIFACT_BYTES + 1)
            break
        except (HTTPError, URLError, TimeoutError, OSError, ValueError) as error:
            if attempt + 1 == attempts:
                raise CanonicalArtifactUnavailable from error
            time.sleep(2**attempt)

    if len(content) > MAX_ARTIFACT_BYTES:
        raise CanonicalArtifactUnavailable
    return content


def report_unavailable(artifact: str) -> int:
    label = ARTIFACT_LABELS[artifact]
    print(
        f"::error title=Canonical {label} unavailable::"
        f"The canonical {label} could not be retrieved; release remains blocked.",
        file=sys.stderr,
    )
    return UNAVAILABLE_EXIT_CODE


def fetch_artifact(
    artifact: str,
    canonical_url: str,
    canonical_output: Path,
    timeout_seconds: float,
    attempts: int = DEFAULT_ATTEMPTS,
) -> int:
    try:
        canonical_bytes = fetch_canonical_artifact(
            canonical_url, timeout_seconds, attempts=attempts
        )
        canonical_output.write_bytes(canonical_bytes)
    except (CanonicalArtifactUnavailable, OSError):
        return report_unavailable(artifact)

    label = ARTIFACT_LABELS[artifact]
    print(f"Canonical {label} fetched: SHA-256 {sha256(canonical_bytes)}")
    return 0


def compare_artifact(
    artifact: str, local_artifact: Path, canonical_artifact: Path
) -> int:
    label = ARTIFACT_LABELS[artifact]
    try:
        local_bytes = local_artifact.read_bytes()
    except OSError:
        print(
            f"::error title={label.title()} drift::"
            f"The repository-local {label} is missing or unreadable.",
            file=sys.stderr,
        )
        return DRIFT_EXIT_CODE

    try:
        canonical_bytes = canonical_artifact.read_bytes()
    except OSError:
        return report_unavailable(artifact)

    local_hash = sha256(local_bytes)
    canonical_hash = sha256(canonical_bytes)
    if local_bytes != canonical_bytes:
        print(
            f"::error title={label.title()} drift::"
            f"Local SHA-256 {local_hash} does not match canonical SHA-256 "
            f"{canonical_hash}; release remains blocked.",
            file=sys.stderr,
        )
        return DRIFT_EXIT_CODE

    print(f"{label.title()} verified: SHA-256 {local_hash}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)

    fetch_parser = commands.add_parser("fetch")
    fetch_parser.add_argument("--artifact", choices=CANONICAL_URLS, required=True)
    fetch_parser.add_argument("--canonical-url")
    fetch_parser.add_argument("--canonical-output", type=Path, required=True)
    fetch_parser.add_argument("--timeout-seconds", type=float, default=15.0)
    fetch_parser.add_argument(
        "--attempts", type=int, choices=range(1, 6), default=DEFAULT_ATTEMPTS
    )

    compare_parser = commands.add_parser("compare")
    compare_parser.add_argument("--artifact", choices=CANONICAL_URLS, required=True)
    compare_parser.add_argument("--local-artifact", type=Path, required=True)
    compare_parser.add_argument("--canonical-artifact", type=Path, required=True)

    args = parser.parse_args()
    if args.command == "fetch":
        canonical_url = args.canonical_url or CANONICAL_URLS[args.artifact]
        return fetch_artifact(
            args.artifact,
            canonical_url,
            args.canonical_output,
            args.timeout_seconds,
            args.attempts,
        )
    return compare_artifact(args.artifact, args.local_artifact, args.canonical_artifact)


if __name__ == "__main__":
    raise SystemExit(main())
