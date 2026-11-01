"""Content-addressed snapshot store and the freeze command.

Objects are immutable and named by their SHA-256. References are store-relative
ids, never filesystem paths, and every read validates the id, containment, size,
type and digest before use. Freezing makes no network or model call.

``materialize`` and ``verify`` apply the same record, size and generation limits
as ``freeze``, so a digest-valid manifest written some other way is refused
before admission and on every claim.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from src.core.article_policy import exclude_virtual_event_promotions
from src.core.content_fingerprint import compute_articles_fingerprint
from src.core.model_config import resolve_model, validate_model
from src.core.opencode_client import parse_model_selection

from . import identity
from .durable import atomic_write_bytes

OBJECT_ID_PATTERN = re.compile(r"^[0-9a-f]{64}$")
MAX_OBJECT_BYTES = 64 * 1024
MAX_RECORDS = 100
MAX_TOTAL_BYTES = 1024 * 1024
_STRING_FIELDS = frozenset(
    {"title", "link", "source", "content", "summary", "content_kind"}
)
_LIST_FIELDS = frozenset({"source_links", "cves"})


class SnapshotRejected(Exception):
    """A snapshot or freeze input was refused; ``reason`` is a fixed token."""

    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


@dataclass(frozen=True)
class FrozenJob:
    manifest_digest: str
    manifest: dict[str, Any]
    articles: list[dict[str, Any]]


class SnapshotStore:
    def __init__(self, root: Path, *, max_object_bytes: int = MAX_OBJECT_BYTES):
        self.root = Path(root)
        self.max_object_bytes = max_object_bytes

    def object_path(self, object_id: Any) -> Path:
        if not isinstance(object_id, str) or not OBJECT_ID_PATTERN.match(object_id):
            raise SnapshotRejected("snapshot_invalid")
        return self.root / "objects" / object_id[:2] / f"{object_id}.json"

    def put(self, data: bytes) -> str:
        object_id = identity.sha256_hex(data)
        path = self.object_path(object_id)
        if not path.is_file() or path.read_bytes() != data:
            atomic_write_bytes(path, data)
        return object_id

    def get(self, object_id: Any) -> bytes:
        path = self.object_path(object_id)
        objects = (self.root / "objects").resolve()
        try:
            resolved = path.resolve()
            if not resolved.is_relative_to(objects) or not resolved.is_file():
                raise SnapshotRejected("snapshot_invalid")
            if resolved.stat().st_size > self.max_object_bytes:
                raise SnapshotRejected("snapshot_invalid")
            data = resolved.read_bytes()
        except OSError:
            raise SnapshotRejected("snapshot_invalid") from None
        if identity.sha256_hex(data) != object_id:
            raise SnapshotRejected("snapshot_invalid")
        return data

    def get_json(self, object_id: Any) -> Any:
        try:
            return json.loads(self.get(object_id))
        except ValueError:
            raise SnapshotRejected("snapshot_invalid") from None


def _validate_record(record: Any) -> dict[str, Any]:
    if not isinstance(record, dict) or not record:
        raise SnapshotRejected("snapshot_invalid")
    for key, value in record.items():
        if key in _STRING_FIELDS:
            valid = isinstance(value, str)
        elif key in _LIST_FIELDS:
            valid = isinstance(value, list) and all(isinstance(v, str) for v in value)
        else:
            valid = False
        if not valid:
            raise SnapshotRejected("snapshot_invalid")
    title, link = record.get("title"), record.get("link")
    if not isinstance(title, str) or not title.strip():
        raise SnapshotRejected("snapshot_invalid")
    if not isinstance(link, str) or not link.startswith(("https://", "http://")):
        raise SnapshotRejected("snapshot_invalid")
    return record


def _check_limits(max_tokens: Any, max_input_tokens: Any) -> None:
    if type(max_tokens) is not int or type(max_input_tokens) is not int:
        raise SnapshotRejected("effective_config_invalid")
    if max_tokens < 1 or max_input_tokens < 1:
        raise SnapshotRejected("effective_config_invalid")


def _check_model(model: Any) -> None:
    try:
        validate_model(model)
        selection = parse_model_selection(model)
        if selection is None or selection.provider_id != "openrouter":
            raise ValueError("adapter sends only through the OpenRouter client")
    except ValueError:
        raise SnapshotRejected("effective_config_invalid") from None


def _generation_inputs(config: Any) -> dict[str, Any]:
    analysis = config.get("analysis", {}) if isinstance(config, dict) else None
    if not isinstance(analysis, dict):
        raise SnapshotRejected("effective_config_invalid")
    max_tokens = analysis.get("max_tokens", 4000)
    max_input_tokens = analysis.get("max_input_tokens", 100000)
    _check_limits(max_tokens, max_input_tokens)
    model = resolve_model(config)
    _check_model(model)
    return {
        "model": model,
        "max_tokens": max_tokens,
        "max_input_tokens": max_input_tokens,
    }


def freeze(
    store: SnapshotStore,
    articles: Any,
    config: Any,
    *,
    code_identity: str,
    submission_generation: int = 0,
    workflow_version: str = identity.WORKFLOW_VERSION,
) -> FrozenJob:
    """Validate and persist one immutable job; nothing is written on refusal."""
    if not isinstance(articles, list):
        raise SnapshotRejected("snapshot_invalid")
    if len(articles) > MAX_RECORDS:
        raise SnapshotRejected("snapshot_invalid")
    encoded: list[bytes] = []
    for article in articles:
        record = _validate_record(article)
        try:
            data = identity.canonical_json(record)
        except (TypeError, ValueError):
            raise SnapshotRejected("snapshot_invalid") from None
        if len(data) > store.max_object_bytes:
            raise SnapshotRejected("snapshot_invalid")
        encoded.append(data)
    if sum(len(data) for data in encoded) > MAX_TOTAL_BYTES:
        raise SnapshotRejected("snapshot_invalid")

    records = [json.loads(data) for data in encoded]
    eligible = exclude_virtual_event_promotions(records)
    if not eligible:
        raise SnapshotRejected("empty_source_set")
    generation = _generation_inputs(config)

    manifest = {
        "manifest_version": identity.MANIFEST_VERSION,
        "product": identity.PRODUCT,
        "workflow_name": identity.WORKFLOW_NAME,
        "workflow_version": workflow_version,
        "submission_generation": submission_generation,
        "records": [identity.sha256_hex(identity.canonical_json(r)) for r in eligible],
        "generation": generation,
        "code_identity": code_identity,
        "articles_fingerprint": compute_articles_fingerprint(eligible),
    }
    for record in eligible:
        store.put(identity.canonical_json(record))
    digest = store.put(identity.canonical_json(manifest))
    return FrozenJob(digest, manifest, eligible)


def _require(condition: bool) -> None:
    if not condition:
        raise SnapshotRejected("snapshot_invalid")


def _check_manifest(manifest: Any) -> None:
    _require(isinstance(manifest, dict))
    version = manifest.get("manifest_version")
    _require(type(version) is int)
    if version != identity.MANIFEST_VERSION:
        raise SnapshotRejected("unsupported_manifest_version")
    generation = manifest.get("generation")
    _require(
        isinstance(manifest.get("workflow_version"), str)
        and isinstance(manifest.get("code_identity"), str)
        and type(manifest.get("submission_generation")) is int
        and isinstance(manifest.get("articles_fingerprint"), str)
        and isinstance(generation, dict)
        and isinstance(generation.get("model"), str)
        and type(generation.get("max_tokens")) is int
        and type(generation.get("max_input_tokens")) is int
        and isinstance(manifest.get("records"), list)
    )
    if not manifest["records"]:
        raise SnapshotRejected("empty_source_set")
    _require(len(manifest["records"]) <= MAX_RECORDS)
    _check_limits(generation["max_tokens"], generation["max_input_tokens"])
    _check_model(generation["model"])


def _check_records(
    manifest: dict[str, Any], articles: list[Any], total_bytes: int
) -> None:
    _require(total_bytes <= MAX_TOTAL_BYTES)
    for article in articles:
        _validate_record(article)
    # Freeze drops these records, so a manifest listing one was not frozen.
    _require(len(exclude_virtual_event_promotions(articles)) == len(articles))
    _require(compute_articles_fingerprint(articles) == manifest["articles_fingerprint"])


def materialize(store: SnapshotStore, manifest_digest: Any) -> FrozenJob:
    """Load a manifest and its records, verifying every digest and limit before use."""
    manifest = store.get_json(manifest_digest)
    _check_manifest(manifest)
    encoded = [store.get(ref) for ref in manifest["records"]]
    try:
        articles = [json.loads(data) for data in encoded]
    except ValueError:
        raise SnapshotRejected("snapshot_invalid") from None
    _check_records(manifest, articles, sum(len(data) for data in encoded))
    return FrozenJob(manifest_digest, manifest, articles)


def verify(job: FrozenJob, *, max_object_bytes: int = MAX_OBJECT_BYTES) -> None:
    """Apply the ``materialize`` checks to an in-memory job before admission."""
    try:
        manifest_bytes = identity.canonical_json(job.manifest)
        encoded = [identity.canonical_json(article) for article in job.articles]
    except (TypeError, ValueError):
        raise SnapshotRejected("snapshot_invalid") from None
    _require(identity.sha256_hex(manifest_bytes) == job.manifest_digest)
    _check_manifest(job.manifest)
    _require([identity.sha256_hex(data) for data in encoded] == job.manifest["records"])
    _require(all(len(data) <= max_object_bytes for data in encoded))
    _check_records(job.manifest, job.articles, sum(len(data) for data in encoded))
