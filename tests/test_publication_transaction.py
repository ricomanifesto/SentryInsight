"""A partial local copy must not become a partially published report."""

import json
from pathlib import Path

import pytest

from src.core import publication_transaction as publication

CORE = [
    "index.md",
    "index.html",
    "current-findings.json",
    "sitemap.xml",
    ".sentryinsight-articles-fingerprint",
]


def trees(tmp_path):
    destination = tmp_path / "published"
    staged = tmp_path / "staged"
    destination.mkdir()
    staged.mkdir()
    for name in CORE:
        (destination / name).write_text("last good " + name)
        (staged / name).write_text("next " + name)
    (staged / "reports").mkdir()
    (staged / "reports/2026-11-02.md").write_text("new archive")
    return staged, destination


def assert_last_good(root):
    for name in CORE:
        assert (root / name).read_text() == "last good " + name
    assert not (root / "reports/2026-11-02.md").exists()
    assert not (root / publication.JOURNAL_DIRECTORY).exists()


def test_success_promotes_report_archive_and_fingerprint_as_one_validated_set(tmp_path):
    staged, root = trees(tmp_path)
    publication.promote_artifacts(staged, root)
    assert all((root / name).read_text() == "next " + name for name in CORE)
    assert (root / "reports/2026-11-02.md").read_text() == "new archive"
    publication.ensure_no_pending_publication(root)


@pytest.mark.parametrize("failed_name", CORE + ["reports/2026-11-02.md"])
@pytest.mark.parametrize("after_replace", [False, True])
def test_any_copy_or_fingerprint_failure_restores_all_prior_bytes(
    tmp_path, monkeypatch, failed_name, after_replace
):
    staged, root = trees(tmp_path)
    original = publication._atomic_copy
    triggered = False

    def fail_once(source, destination, **kwargs):
        nonlocal triggered
        if (
            source.is_relative_to(staged)
            and destination == root / failed_name
            and not triggered
        ):
            triggered = True
            if after_replace:
                original(source, destination, **kwargs)
            raise OSError("synthetic copy failure")
        original(source, destination, **kwargs)

    monkeypatch.setattr(publication, "_atomic_copy", fail_once)
    with pytest.raises(publication.PublicationError) as caught:
        publication.promote_artifacts(staged, root)
    assert triggered
    assert caught.value.code == "publication_rolled_back"
    assert_last_good(root)


def test_rollback_failure_keeps_recovery_material_and_blocks_another_generation(
    tmp_path, monkeypatch
):
    staged, root = trees(tmp_path)
    original = publication._atomic_copy
    calls = 0

    def fail(source, destination, **kwargs):
        nonlocal calls
        calls += 1
        if calls > 1:
            raise OSError("synthetic persistent storage failure")
        original(source, destination, **kwargs)

    monkeypatch.setattr(publication, "_atomic_copy", fail)
    with pytest.raises(publication.PublicationError) as caught:
        publication.promote_artifacts(staged, root)
    assert caught.value.code == "publication_recovery_required"
    recovery = root / publication.JOURNAL_DIRECTORY
    assert (recovery / "journal.json").is_file()
    for name in CORE:
        assert (recovery / "prior" / name).read_text() == "last good " + name
    with pytest.raises(
        publication.PublicationError, match="publication_recovery_required"
    ):
        publication.ensure_no_pending_publication(root)
    with pytest.raises(
        publication.PublicationError, match="publication_recovery_required"
    ):
        publication.promote_artifacts(staged, root)
    monkeypatch.setattr(publication, "_atomic_copy", original)
    publication.recover_publication(root)
    assert_last_good(root)


def test_recovery_preserves_intervening_edits_instead_of_overwriting_them(
    tmp_path, monkeypatch
):
    staged, root = trees(tmp_path)
    original = publication._atomic_copy
    monkeypatch.setattr(
        publication,
        "_atomic_copy",
        lambda *a, **k: (_ for _ in ()).throw(OSError("failure")),
    )
    with pytest.raises(publication.PublicationError):
        publication.promote_artifacts(staged, root)
    monkeypatch.setattr(publication, "_atomic_copy", original)
    (root / "index.md").write_text("intervening user edit")
    with pytest.raises(
        publication.PublicationError, match="publication_recovery_required"
    ):
        publication.recover_publication(root)
    assert (root / "index.md").read_text() == "intervening user edit"


@pytest.mark.parametrize("fault", ["missing_fingerprint", "unexpected_file", "symlink"])
def test_invalid_stage_is_rejected_before_any_last_good_change(tmp_path, fault):
    staged, root = trees(tmp_path)
    if fault == "missing_fingerprint":
        (staged / CORE[-1]).unlink()
    elif fault == "unexpected_file":
        (staged / "private-log.txt").write_text("not an artifact")
    else:
        (staged / "index.md").unlink()
        (staged / "index.md").symlink_to(root / "index.md")
    with pytest.raises(publication.PublicationError):
        publication.promote_artifacts(staged, root)
    assert_last_good(root)


def test_unrelated_destination_files_are_preserved(tmp_path):
    staged, root = trees(tmp_path)
    unrelated = root / "notes.txt"
    unrelated.write_text("user notes")
    publication.promote_artifacts(staged, root)
    assert unrelated.read_text() == "user notes"


@pytest.mark.parametrize("damage", ["traversal", "backup", "symlink", "unknown_field"])
def test_recovery_prevalidates_every_entry_before_restoring_any_bytes(
    tmp_path, monkeypatch, damage
):
    staged, root = trees(tmp_path)
    original = publication._atomic_copy
    monkeypatch.setattr(
        publication,
        "_atomic_copy",
        lambda *a, **k: (_ for _ in ()).throw(OSError("failure")),
    )
    with pytest.raises(publication.PublicationError):
        publication.promote_artifacts(staged, root)
    monkeypatch.setattr(publication, "_atomic_copy", original)
    journal = root / publication.JOURNAL_DIRECTORY
    path = journal / "journal.json"
    data = json.loads(path.read_text())
    if damage == "traversal":
        data["files"][-1]["path"] = "../unrelated"
    elif damage == "backup":
        (journal / "prior/index.html").write_text("corrupt")
    elif damage == "symlink":
        (journal / "prior/index.html").unlink()
        (journal / "prior/index.html").symlink_to(root / "index.html")
    else:
        data["unexpected"] = True
    path.write_text(json.dumps(data))
    before = {name: (root / name).read_bytes() for name in CORE}
    with pytest.raises(
        publication.PublicationError, match="publication_recovery_required"
    ):
        publication.recover_publication(root)
    assert before == {name: (root / name).read_bytes() for name in CORE}
    assert journal.exists()


def test_recovery_refuses_intervening_deletion(tmp_path, monkeypatch):
    staged, root = trees(tmp_path)
    original = publication._atomic_copy
    monkeypatch.setattr(
        publication,
        "_atomic_copy",
        lambda *a, **k: (_ for _ in ()).throw(OSError("failure")),
    )
    with pytest.raises(publication.PublicationError):
        publication.promote_artifacts(staged, root)
    monkeypatch.setattr(publication, "_atomic_copy", original)
    (root / "index.md").unlink()
    with pytest.raises(
        publication.PublicationError, match="publication_recovery_required"
    ):
        publication.recover_publication(root)
    assert not (root / "index.md").exists()


def test_copy_checks_staged_bytes_before_replace(tmp_path, monkeypatch):
    staged, root = trees(tmp_path)
    original = publication._atomic_copy
    changed = False

    def mutate(source, destination, **kwargs):
        nonlocal changed
        if source == staged / "index.md" and not changed:
            changed = True
            source.write_text("changed after validation")
        original(source, destination, **kwargs)

    monkeypatch.setattr(publication, "_atomic_copy", mutate)
    with pytest.raises(publication.PublicationError, match="publication_rolled_back"):
        publication.promote_artifacts(staged, root)
    assert changed
    assert_last_good(root)


def test_after_commit_cleanup_failure_is_recoverable_without_rollback(
    tmp_path, monkeypatch
):
    staged, root = trees(tmp_path)
    original = publication.shutil.rmtree

    def fail_cleanup(path, *args, **kwargs):
        if Path(path).name == "prior":
            (Path(path) / "index.md").unlink(missing_ok=True)
            raise OSError("partial cleanup")
        original(path, *args, **kwargs)

    monkeypatch.setattr(publication.shutil, "rmtree", fail_cleanup)
    assert publication.promote_artifacts(staged, root) == "publication_cleanup_pending"
    assert all((root / name).read_text() == "next " + name for name in CORE)
    with pytest.raises(
        publication.PublicationError, match="publication_recovery_required"
    ):
        publication.ensure_no_pending_publication(root)
    monkeypatch.setattr(publication.shutil, "rmtree", original)
    publication.recover_publication(root)
    publication.ensure_no_pending_publication(root)
    assert all((root / name).read_text() == "next " + name for name in CORE)


def test_directory_sync_after_commit_does_not_invent_unblocked_failure(
    tmp_path, monkeypatch
):
    staged, root = trees(tmp_path)
    original = publication._sync_directory
    failed = False

    def fail(path):
        nonlocal failed
        if (
            path == root
            and not (root / publication.JOURNAL_DIRECTORY).exists()
            and not failed
        ):
            failed = True
            raise OSError("post-commit directory sync")
        original(path)

    monkeypatch.setattr(publication, "_sync_directory", fail)
    outcome = publication.promote_artifacts(staged, root)
    assert failed
    assert outcome == "publication_cleanup_pending"
    assert all((root / name).read_text() == "next " + name for name in CORE)
    with pytest.raises(publication.PublicationError):
        publication.ensure_no_pending_publication(root)
    publication.recover_publication(root)
    publication.ensure_no_pending_publication(root)


def test_partial_cleanup_after_rollback_keeps_a_resumable_restored_manifest(
    tmp_path, monkeypatch
):
    staged, root = trees(tmp_path)
    original_copy = publication._atomic_copy
    original_remove = publication.shutil.rmtree
    failed = False

    def fail_copy(source, destination, **kwargs):
        nonlocal failed
        if source == staged / "index.md" and not failed:
            failed = True
            raise OSError("copy failure")
        original_copy(source, destination, **kwargs)

    def fail_remove(path, *args, **kwargs):
        if Path(path).name in {"prior", publication.JOURNAL_DIRECTORY}:
            backup = (
                Path(path) / "index.md"
                if Path(path).name == "prior"
                else Path(path) / "prior/index.md"
            )
            backup.unlink(missing_ok=True)
            raise OSError("partial cleanup")
        original_remove(path, *args, **kwargs)

    monkeypatch.setattr(publication, "_atomic_copy", fail_copy)
    monkeypatch.setattr(publication.shutil, "rmtree", fail_remove)
    with pytest.raises(
        publication.PublicationError, match="publication_recovery_required"
    ):
        publication.promote_artifacts(staged, root)
    assert all((root / name).read_text() == "last good " + name for name in CORE)
    monkeypatch.setattr(publication.shutil, "rmtree", original_remove)
    publication.recover_publication(root)
    assert_last_good(root)
