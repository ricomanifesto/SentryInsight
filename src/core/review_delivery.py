"""Bounded terminal receipts and metadata-only CI review packages."""

import json
import os
from pathlib import Path
import re
import shutil
import stat
import tempfile

from .source_review import (
    MAX_PACKET_BYTES,
    PLAN_KEY,
    SourceReviewError,
    canonical_json,
    packet_bytes,
    validate_review_packet,
)

OUTCOME_FILE = ".sentryinsight-review-outcome.json"
QUEUE_DIRECTORY = ".sentryinsight-review"
STATUSES = {
    "failed",
    "completed",
    "completed_with_review",
    "completed_unchanged",
    "completed_with_warnings",
    "review_required",
}


def _read_bounded(path: Path, limit: int, *, private: bool = False) -> bytes:
    try:
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
        with os.fdopen(fd, "rb") as stream:
            info = os.fstat(stream.fileno())
            if (
                not stat.S_ISREG(info.st_mode)
                or info.st_size > limit
                or (private and stat.S_IMODE(info.st_mode) != 0o600)
            ):
                raise SourceReviewError("invalid_review_delivery")
            data = stream.read(limit + 1)
        if len(data) > limit:
            raise SourceReviewError("invalid_review_delivery")
        return data
    except (OSError, ValueError):
        raise SourceReviewError("invalid_review_delivery") from None


def read_review_packet(path: Path) -> dict:
    data = _read_bounded(path, MAX_PACKET_BYTES, private=True)
    try:
        packet = validate_review_packet(json.loads(data))
        if path.name != packet["plan_id"] + ".json" or data != packet_bytes(packet):
            raise SourceReviewError("invalid_review_delivery")
        return packet
    except (ValueError, TypeError, KeyError):
        raise SourceReviewError("invalid_review_delivery") from None


def write_run_outcome(state: dict | None, root: Path) -> dict:
    state = state or {}
    plan = validate_review_packet(state[PLAN_KEY]) if PLAN_KEY in state else None
    status = state.get("status", "failed")
    if status not in STATUSES:
        status = "failed"
    outcome = {
        "schema_version": 1,
        "status": status,
        "report_generated": bool(
            state.get("report_generated") is True
            and status in {"completed", "completed_with_review"}
            and plan is not None
        ),
        "plan_id": plan["plan_id"] if plan is not None else None,
        "outcome": "review_plan_available" if plan is not None else "no_valid_plan",
    }
    root.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".review-outcome-", dir=root)
    try:
        with os.fdopen(fd, "w") as stream:
            stream.write(canonical_json(outcome) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, root / OUTCOME_FILE)
    finally:
        Path(name).unlink(missing_ok=True)
    return outcome


def _read_outcome(root: Path) -> dict:
    try:
        raw = _read_bounded(root / OUTCOME_FILE, 4096)
        result = json.loads(raw)
        if not isinstance(result, dict) or set(result) != {
            "schema_version",
            "status",
            "report_generated",
            "plan_id",
            "outcome",
        }:
            raise ValueError()
        if (
            type(result["schema_version"]) is not int
            or result["schema_version"] != 1
            or result["status"] not in STATUSES
            or type(result["report_generated"]) is not bool
        ):
            raise ValueError()
        plan_id = result["plan_id"]
        if plan_id is not None and (
            not isinstance(plan_id, str) or not re.fullmatch("[a-f0-9]{64}", plan_id)
        ):
            raise ValueError()
        if result["outcome"] != (
            "review_plan_available" if plan_id is not None else "no_valid_plan"
        ):
            raise ValueError()
        if result["report_generated"] and (
            plan_id is None
            or result["status"] not in {"completed", "completed_with_review"}
        ):
            raise ValueError()
        if raw != (canonical_json(result) + "\n").encode():
            raise ValueError()
        return result
    except (ValueError, TypeError, KeyError):
        raise SourceReviewError("invalid_review_delivery") from None


def package_review(root: Path, destination: Path) -> dict:
    """Export only canonical validated metadata; fail before creating a partial package."""
    outcome = _read_outcome(root)
    queue = root / QUEUE_DIRECTORY
    if queue.is_symlink() or (queue.exists() and not queue.is_dir()):
        raise SourceReviewError("invalid_review_delivery")
    packets = {}
    if queue.exists():
        paths = list(queue.iterdir())
        if len(paths) > 512:
            raise SourceReviewError("invalid_review_delivery")
        for path in paths:
            packet = read_review_packet(path)
            packets[packet["plan_id"]] = packet
    if outcome["plan_id"] is not None and outcome["plan_id"] not in packets:
        raise SourceReviewError("review_packet_missing")
    if destination.exists() or destination.is_symlink():
        raise SourceReviewError("review_package_exists")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(
        tempfile.mkdtemp(prefix=".review-package-", dir=destination.parent)
    )
    try:
        payloads = {
            key + ".json": packet_bytes(value) for key, value in packets.items()
        }
        payloads["outcome.json"] = (canonical_json(outcome) + "\n").encode()
        for name, payload in payloads.items():
            path = temporary / name
            with path.open("xb") as stream:
                os.fchmod(stream.fileno(), 0o600)
                stream.write(payload)
        temporary.rename(destination)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
    return outcome
