"""Deterministic identity for frozen jobs.

A job's Runtime idempotency key and ``input_ref`` are pure functions of its
manifest digest. The manifest covers the ordered source records, the effective
generation inputs, the code identity of the generation and validation path,
the workflow version and an explicit submission generation.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

PRODUCT = "sentryinsight"
WORKFLOW_NAME = "exploitation-report"
WORKFLOW_VERSION = "1"
SUPPORTED_WORKFLOW_VERSIONS = frozenset({WORKFLOW_VERSION})
MANIFEST_VERSION = 1
# Keep the requested attempt limit constant for each workflow version.
RUNTIME_MAX_ATTEMPTS = 3
INPUT_REF_KIND = "sentryinsight.frozen_job"
OUTPUT_REF_KIND = "sentryinsight.prepared_artifact"

REPO_ROOT = Path(__file__).resolve().parents[2]
# Source that shapes the prompt, the request, validation or the built artifact.
CODE_IDENTITY_PATHS = (
    "src/core/analysis_errors.py",
    "src/core/analyze.py",
    "src/core/article_policy.py",
    "src/core/content_fingerprint.py",
    "src/core/cve.py",
    "src/core/finding_evidence.py",
    "src/core/heading_identity.py",
    "src/core/model_client.py",
    "src/core/model_config.py",
    "src/core/opencode_client.py",
    "src/core/openrouter_client.py",
    "src/core/report_artifact.py",
    "src/core/report_validation.py",
    "src/core/reporting.py",
    "src/core/workflow.py",
    "src/services/article_content.py",
    "scripts/build_site.py",
    "site",
)


def canonical_json(value: Any) -> bytes:
    """Encode JSON with one byte representation per value."""
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _identity_files(root: Path, paths: Iterable[str]) -> list[tuple[str, Path]]:
    files: list[tuple[str, Path]] = []
    for relative in paths:
        path = root / relative
        if path.is_dir():
            files.extend(
                (candidate.relative_to(root).as_posix(), candidate)
                for candidate in path.rglob("*")
                if candidate.is_file()
            )
        else:
            files.append((relative, path))
    return sorted(files)


def compute_code_identity(
    root: Path = REPO_ROOT, paths: Iterable[str] = CODE_IDENTITY_PATHS
) -> str:
    """Digest the generation and validation source as it exists on disk."""
    digest = hashlib.sha256()
    for relative, path in _identity_files(root, paths):
        digest.update(relative.encode("utf-8") + b"\0")
        digest.update(sha256_hex(path.read_bytes()).encode("ascii") + b"\n")
    return digest.hexdigest()


def idempotency_key(
    manifest_digest: str, workflow_version: str = WORKFLOW_VERSION
) -> str:
    # Include the workflow version in the idempotency key.
    return f"{PRODUCT}/{WORKFLOW_NAME}/v{workflow_version}/{manifest_digest}"


def input_ref(manifest_digest: str) -> dict[str, Any]:
    return {
        "kind": INPUT_REF_KIND,
        "manifest_sha256": manifest_digest,
        "manifest_version": MANIFEST_VERSION,
    }
