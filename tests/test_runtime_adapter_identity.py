"""Frozen job identity and snapshot admission for the Runtime adapter."""

import json
import os
import shutil

import pytest

from src.core.content_fingerprint import compute_articles_fingerprint
from src.runtime_adapter import identity
from src.runtime_adapter.snapshot import (
    SnapshotRejected,
    SnapshotStore,
    freeze,
    materialize,
)
from src.runtime_adapter.synthetic import synthetic_articles, synthetic_config

CODE = "c" * 64


def frozen(tmp_path, articles=None, config=None, **kwargs):
    store = SnapshotStore(tmp_path / "snapshots")
    kwargs.setdefault("code_identity", CODE)
    return store, freeze(
        store,
        synthetic_articles() if articles is None else articles,
        synthetic_config() if config is None else config,
        **kwargs,
    )


def test_freeze_is_a_pure_function_of_the_manifest(tmp_path):
    _, first = frozen(tmp_path / "a")
    _, second = frozen(tmp_path / "b")

    assert first.manifest_digest == second.manifest_digest
    key = identity.idempotency_key(first.manifest_digest)
    assert key == identity.idempotency_key(second.manifest_digest)
    assert f"/v{identity.WORKFLOW_VERSION}/" in key
    assert identity.input_ref(first.manifest_digest) == {
        "kind": "sentryinsight.frozen_job",
        "manifest_sha256": first.manifest_digest,
        "manifest_version": 1,
    }
    assert first.manifest["articles_fingerprint"] == compute_articles_fingerprint(
        synthetic_articles()
    )


def changed_order():
    articles = synthetic_articles() + [
        {
            "title": "Second synthetic report",
            "link": "https://example.test/second",
            "source": "Example Source",
            "content": "CVE-2026-5678 is described without exploitation.",
        }
    ]
    return articles[::-1], articles


@pytest.mark.parametrize(
    "change",
    [
        "record_order",
        "record_content",
        "model",
        "max_tokens",
        "code_identity",
        "submission_generation",
        "workflow_version",
    ],
)
def test_every_identity_input_changes_key_and_input_ref(tmp_path, change):
    articles, config, kwargs = synthetic_articles(), synthetic_config(), {}
    base_articles = synthetic_articles()
    if change == "record_order":
        articles, base_articles = changed_order()
    elif change == "record_content":
        articles[0]["content"] += " Additional synthetic sentence."
    elif change == "model":
        config["analysis"]["model"] = "openrouter/example/other-model:free"
    elif change == "max_tokens":
        config["analysis"]["max_tokens"] = 1234
    elif change == "code_identity":
        kwargs["code_identity"] = "d" * 64
    elif change == "submission_generation":
        kwargs["submission_generation"] = 1
    elif change == "workflow_version":
        kwargs["workflow_version"] = "2"

    _, base = frozen(tmp_path / "base", articles=base_articles)
    _, other = frozen(tmp_path / "other", articles=articles, config=config, **kwargs)

    assert other.manifest_digest != base.manifest_digest
    assert identity.idempotency_key(other.manifest_digest) != (
        identity.idempotency_key(base.manifest_digest)
    )
    assert identity.input_ref(other.manifest_digest) != identity.input_ref(
        base.manifest_digest
    )


def test_code_identity_tracks_generation_and_validation_source(tmp_path):
    root = tmp_path / "copy"
    for relative in identity.CODE_IDENTITY_PATHS:
        source = identity.REPO_ROOT / relative
        destination = root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.is_dir():
            shutil.copytree(source, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(source, destination)

    original = identity.compute_code_identity(root)
    assert original == identity.compute_code_identity(identity.REPO_ROOT)

    prompt_module = root / "src" / "core" / "analyze.py"
    prompt_module.write_text(prompt_module.read_text() + "\n# prompt change\n")
    assert identity.compute_code_identity(root) != original


def test_materialize_round_trips_records_in_order(tmp_path):
    reversed_articles, _ = changed_order()
    store, job = frozen(tmp_path, articles=reversed_articles)

    loaded = materialize(store, job.manifest_digest)

    assert loaded.manifest_digest == job.manifest_digest
    assert loaded.articles == reversed_articles
    assert loaded.manifest == job.manifest


def oversized_articles():
    articles = synthetic_articles()
    articles[0]["content"] = "x" * (70 * 1024)
    return articles


@pytest.mark.parametrize(
    "articles, reason",
    [
        ([], "empty_source_set"),
        ("not a list", "snapshot_invalid"),
        (["not an object"], "snapshot_invalid"),
        ([{"title": "No link", "source": "S", "content": "c"}], "snapshot_invalid"),
        ([{"title": 7, "link": "https://example.test/a"}], "snapshot_invalid"),
        ([{"title": "Bad scheme", "link": "file:///etc/passwd"}], "snapshot_invalid"),
        (
            [{"title": "T", "link": "https://example.test/a", "extra": object()}],
            "snapshot_invalid",
        ),
        (oversized_articles(), "snapshot_invalid"),
        (
            [
                {
                    "title": "[Virtual Event] Synthetic webinar",
                    "link": "https://example.test/webinar",
                    "source": "Example Source",
                    "content": "Register now.",
                }
            ],
            "empty_source_set",
        ),
    ],
)
def test_freeze_rejects_inadmissible_inputs_before_any_write(
    tmp_path, articles, reason
):
    store = SnapshotStore(tmp_path / "snapshots")

    with pytest.raises(SnapshotRejected) as raised:
        freeze(store, articles, synthetic_config(), code_identity=CODE)

    assert raised.value.reason == reason
    assert str(raised.value) == reason
    assert not any((tmp_path / "snapshots").rglob("*.json"))


@pytest.mark.parametrize(
    "model", ["", "claude-sonnet-4-20250514", "Not A Model", "anthropic/x"]
)
def test_freeze_rejects_invalid_effective_model(tmp_path, model):
    config = synthetic_config()
    config["analysis"]["model"] = model
    if model == "":
        config["analysis"].pop("model")
        config["analysis"]["max_tokens"] = "not-an-int"

    with pytest.raises(SnapshotRejected) as raised:
        freeze(
            SnapshotStore(tmp_path), synthetic_articles(), config, code_identity=CODE
        )

    assert raised.value.reason == "effective_config_invalid"


@pytest.mark.parametrize(
    "manifest_id",
    [
        "../../outside",
        "/etc/passwd",
        "A" * 64,
        "0" * 63,
        "",
        None,
        7,
    ],
)
def test_materialize_rejects_unsafe_or_missing_references(tmp_path, manifest_id):
    store, _ = frozen(tmp_path)

    with pytest.raises(SnapshotRejected) as raised:
        materialize(store, manifest_id)

    assert raised.value.reason == "snapshot_invalid"


def test_materialize_rejects_missing_tampered_and_oversize_objects(tmp_path):
    store, job = frozen(tmp_path)
    record_id = job.manifest["records"][0]

    with pytest.raises(SnapshotRejected):
        materialize(store, "f" * 64)

    path = store.object_path(record_id)
    original = path.read_bytes()
    path.write_bytes(original.replace(b"exploited", b"EXPLOITED"))
    with pytest.raises(SnapshotRejected) as raised:
        materialize(store, job.manifest_digest)
    assert raised.value.reason == "snapshot_invalid"

    path.write_bytes(b" " * (store.max_object_bytes + 1))
    with pytest.raises(SnapshotRejected) as raised:
        materialize(store, job.manifest_digest)
    assert raised.value.reason == "snapshot_invalid"


def put_manifest(store, manifest):
    return store.put(identity.canonical_json(manifest))


def test_materialize_rejects_malformed_or_unsupported_manifests(tmp_path):
    store, job = frozen(tmp_path)

    with pytest.raises(SnapshotRejected) as raised:
        materialize(store, store.put(b"not json"))
    assert raised.value.reason == "snapshot_invalid"

    with pytest.raises(SnapshotRejected) as raised:
        materialize(store, put_manifest(store, ["not", "an", "object"]))
    assert raised.value.reason == "snapshot_invalid"

    future = dict(job.manifest, manifest_version=2)
    with pytest.raises(SnapshotRejected) as raised:
        materialize(store, put_manifest(store, future))
    assert raised.value.reason == "unsupported_manifest_version"

    empty = dict(job.manifest, records=[])
    with pytest.raises(SnapshotRejected) as raised:
        materialize(store, put_manifest(store, empty))
    assert raised.value.reason == "empty_source_set"

    escaping = dict(job.manifest, records=["../" + job.manifest["records"][0]])
    with pytest.raises(SnapshotRejected) as raised:
        materialize(store, put_manifest(store, escaping))
    assert raised.value.reason == "snapshot_invalid"


def test_partially_written_object_is_never_admitted(tmp_path, monkeypatch):
    store = SnapshotStore(tmp_path)
    data = identity.canonical_json({"partial": True})
    object_id = identity.sha256_hex(data)

    def crash(*_args, **_kwargs):
        raise OSError("simulated crash before rename")

    monkeypatch.setattr(os, "replace", crash)
    with pytest.raises(OSError):
        store.put(data)
    monkeypatch.undo()

    assert not store.object_path(object_id).exists()
    with pytest.raises(SnapshotRejected):
        store.get(object_id)
    assert store.put(data) == object_id
    assert json.loads(store.get(object_id)) == {"partial": True}
