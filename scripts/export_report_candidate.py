#!/usr/bin/env python3
"""Retain one completed report for offline replay, without publishing it."""

from __future__ import annotations

# ruff: noqa: E402

import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.core.failure_receipt import (
    MAX_BYTES as MAX_RECEIPT_BYTES,
    FailureReceiptError,
    validate_receipt,
)
from src.core.report_artifact import parse_report_artifact
from src.core.report_validation import blocking_issues, validate_report_content

MAX_REPORT_BYTES = 2 * 1024 * 1024
DIRECTORY_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW


class CandidateExportError(RuntimeError):
    def __init__(self):
        super().__init__("Candidate export refused.")


def _require(value):
    if not value:
        raise CandidateExportError()


@contextmanager
def _directory(path: Path):
    # Open each component without following symlinks, retaining descriptors so
    # replacing an ancestor cannot redirect a later file read or write.
    _require(".." not in path.parts)
    absolute = Path(os.path.abspath(path))
    descriptor = os.open(absolute.anchor, DIRECTORY_FLAGS)
    try:
        for component in absolute.parts[1:]:
            child = os.open(component, DIRECTORY_FLAGS, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
        yield descriptor
    finally:
        os.close(descriptor)


def _read(path: Path, maximum: int, *, private=False) -> bytes:
    with _directory(path.parent) as parent:
        descriptor = os.open(
            path.name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent
        )
    with os.fdopen(descriptor, "rb") as stream:
        before = os.fstat(stream.fileno())
        _require(
            stat.S_ISREG(before.st_mode)
            and before.st_nlink == 1
            and 0 < before.st_size <= maximum
            and (not private or before.st_mode & 0o077 == 0)
        )
        data = stream.read(maximum + 1)
        after = os.fstat(stream.fileno())
        fields = ("st_dev", "st_ino", "st_size", "st_mtime_ns", "st_ctime_ns")
        _require(
            len(data) == before.st_size
            and len(data) <= maximum
            and all(getattr(before, key) == getattr(after, key) for key in fields)
            and after.st_nlink == 1
        )
    return data


def _write(directory: int, name: str, data: bytes) -> None:
    pending = f".{name}.pending"
    descriptor = os.open(
        pending,
        os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
        0o600,
        dir_fd=directory,
    )
    with os.fdopen(descriptor, "wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    os.rename(pending, name, src_dir_fd=directory, dst_dir_fd=directory)


def _store(output: Path, data: bytes, manifest: dict) -> None:
    with _directory(output.parent) as parent:
        # Claim the output exclusively; an existing directory or symlink is
        # never replaced. A complete manifest is the final commit marker.
        os.mkdir(output.name, 0o700, dir_fd=parent)
        descriptor = os.open(output.name, DIRECTORY_FLAGS, dir_fd=parent)
        try:
            _write(descriptor, "index.md", data)
            _write(
                descriptor,
                "manifest.json",
                (json.dumps(manifest, sort_keys=True, indent=2) + "\n").encode(),
            )
            os.fsync(descriptor)
        except BaseException:
            for name in (
                "index.md",
                "manifest.json",
                ".index.md.pending",
                ".manifest.json.pending",
            ):
                try:
                    os.unlink(name, dir_fd=descriptor)
                except FileNotFoundError:
                    pass
            held = os.fstat(descriptor)
            current = os.stat(output.name, dir_fd=parent, follow_symlinks=False)
            if (held.st_dev, held.st_ino) == (current.st_dev, current.st_ino):
                os.rmdir(output.name, dir_fd=parent)
            raise
        finally:
            os.close(descriptor)


def export_candidate(
    *,
    report_root: Path,
    receipt_path: Path,
    output: Path,
    run_id: str,
    run_attempt: str,
    source_revision: str,
) -> dict:
    try:
        _require(
            re.fullmatch(r"[0-9]{1,20}", run_id)
            and re.fullmatch(r"[0-9]{1,5}", run_attempt)
            and re.fullmatch(r"[a-f0-9]{40}", source_revision)
        )
        receipt = validate_receipt(
            json.loads(_read(receipt_path, MAX_RECEIPT_BYTES, private=True))
        )
        _require(
            receipt["status"] in {"completed", "completed_with_review"}
            and receipt["report_generated"] is True
            and receipt["diagnostic"] is None
            and receipt["run_id"] == run_id
            and receipt["run_attempt"] == run_attempt
            and receipt["source_revision"] == source_revision
        )
        data = _read(report_root / "index.md", MAX_REPORT_BYTES)
        artifact = parse_report_artifact(data.decode("utf-8"))
        _require(
            artifact.schema_version == 5
            and artifact.source_coverage is not None
            and artifact.source_coverage["plan"]["plan_id"] == receipt["plan_id"]
        )
        _require(
            not blocking_issues(
                validate_report_content(
                    artifact.body,
                    require_descriptive_titles=True,
                )
            )
        )
        manifest = {
            "schema_version": 1,
            "kind": "unpublished-report-candidate",
            "publication_authority": False,
            "run_id": run_id,
            "run_attempt": run_attempt,
            "source_revision": source_revision,
            "plan_id": receipt["plan_id"],
            "report_sha256": hashlib.sha256(data).hexdigest(),
            "report_bytes": len(data),
            "generated_at": artifact.generated_at.isoformat().replace("+00:00", "Z"),
        }
        _store(output, data, manifest)
        return manifest
    except (OSError, ValueError, TypeError, KeyError, FailureReceiptError):
        raise CandidateExportError() from None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("report-root", "receipt-path", "output"):
        parser.add_argument("--" + name, type=Path, required=True)
    for name in ("run-id", "run-attempt", "source-revision"):
        parser.add_argument("--" + name, required=True)
    options = parser.parse_args()
    try:
        manifest = export_candidate(**vars(options))
    except CandidateExportError:
        print("Candidate export refused.")
        return 1
    print(json.dumps(manifest, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
