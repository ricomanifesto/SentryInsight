"""Publication effects, rollback, retry and ownership, without model transport."""

import asyncio
import copy
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys

import pytest

from src.core import publication as pub
from src.core.content_fingerprint import FINGERPRINT_PATH
from src.core.report_artifact import parse_report_artifact
from test_report_artifact import REPORT

FILES = [
    "assets/report.js",
    "assets/site.css",
    "assets/vendor/dom.js",
    "current-findings.json",
    "index.md",
    "reports/2026-08-12.html",
    "reports/2026-08-12.md",
    "reports/index.html",
    "reports/index.json",
    "sitemap.xml",
    "index.html",
    FINGERPRINT_PATH,
]


def tree(root):
    if not root.exists():
        return None
    result = {}
    for path in [root, *sorted(root.rglob("*"))]:
        info = path.lstat()
        value = {"mode": stat.S_IMODE(info.st_mode)}
        if path.is_symlink():
            value["link"] = os.readlink(path)
        elif path.is_file():
            value.update(data=path.read_bytes(), mtime_ns=info.st_mtime_ns)
        else:
            value["directory"] = True
        result[str(path.relative_to(root))] = value
    return result


def build(**kwargs):
    root = kwargs["output_path"]
    for name in FILES:
        if name in {"index.md", FINGERPRINT_PATH, "reports/2026-08-12.md"}:
            continue
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("new " + name)


def publish(root):
    return pub.publish_report_artifacts(
        parse_report_artifact(REPORT),
        REPORT,
        root,
        "new-fingerprint",
        Path("site"),
        builder=build,
    )


@pytest.fixture
def public(tmp_path):
    root = tmp_path / "public"
    root.mkdir()
    for name in FILES:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("old " + name)
        path.chmod(0o640)
        os.utime(path, ns=(123456789000, 123456789000))
    (root / "index.md").write_text(REPORT.replace("2026-08-13", "2026-08-12"))
    (root / "reports/2026-08-12.md").write_text((root / "index.md").read_text())
    (root / "unowned").write_text("keep")
    (root / ".index.html.sentryinsight.tmp").write_text("keep temporary name")
    (root / "empty").mkdir()
    return root


def fail_install(
    monkeypatch, root, *, target=FINGERPRINT_PATH, after=True, restore=False
):
    original = Path.replace
    fired = []

    def replace(source, destination):
        if source.name == "restore" and restore:
            fired.append("restore")
            raise OSError("restore denied")
        if destination == root / target and source.name != "restore":
            if after:
                original(source, destination)
            fired.append("install")
            raise OSError("install failed")
        return original(source, destination)

    monkeypatch.setattr(Path, "replace", replace)
    return fired


@pytest.mark.parametrize("name", FILES)
@pytest.mark.parametrize("after", [False, True])
def test_each_replacement_failure_restores_complete_original(
    public, monkeypatch, name, after
):
    before = tree(public)
    fired = fail_install(monkeypatch, public, target=name, after=after)
    with pytest.raises(OSError, match="install failed"):
        publish(public)
    assert fired == ["install"]
    assert tree(public) == before
    assert not (pub._control(public) / "transaction.json").exists()


@pytest.mark.parametrize("index", range(len(FILES)))
@pytest.mark.parametrize("after", [False, True])
def test_backup_read_or_partial_write_failure_leaves_original(
    public, monkeypatch, index, after
):
    before = tree(public)
    original = shutil.copy2
    fired = []

    def copy_file(source, destination, *args, **kwargs):
        if Path(destination).parent.name == "originals" and Path(
            destination
        ).name == str(index):
            if after:
                Path(destination).write_bytes(b"partial backup")
            fired.append(index)
            raise OSError("snapshot unavailable")
        return original(source, destination, *args, **kwargs)

    monkeypatch.setattr(shutil, "copy2", copy_file)
    with pytest.raises(OSError, match="snapshot unavailable"):
        publish(public)
    assert fired == [index]
    assert tree(public) == before


@pytest.mark.parametrize("shape", ["empty", "absent", "nested_absent"])
@pytest.mark.parametrize("after", [False, True])
def test_absent_paths_and_directory_chain_are_restored(
    tmp_path, monkeypatch, shape, after
):
    root = tmp_path / "public"
    if shape == "empty":
        root.mkdir()
        (root / "keep").mkdir()
    if shape == "nested_absent":
        root = root / "nested" / "leaf"
    before = tree(tmp_path / "public")
    fired = fail_install(monkeypatch, root, after=after)
    with pytest.raises(OSError):
        publish(root)
    assert fired == ["install"]
    assert tree(tmp_path / "public") == before


@pytest.mark.parametrize(
    "shape", ["file_parent", "directory_target", "parent_link", "file_link"]
)
def test_preflight_rejects_types_and_symlinks_without_mutation(public, tmp_path, shape):
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "sentinel").write_text("outside")
    if shape in {"file_parent", "parent_link"}:
        shutil.rmtree(public / "assets")
        if shape == "file_parent":
            (public / "assets").write_text("unowned")
        else:
            (public / "assets").symlink_to(outside)
    else:
        path = public / "current-findings.json"
        path.unlink()
        if shape == "directory_target":
            path.mkdir()
        else:
            path.symlink_to(outside / "sentinel")
    before, external = tree(public), tree(outside)
    with pytest.raises(OSError):
        publish(public)
    assert tree(public) == before
    assert tree(outside) == external


def pending(public, monkeypatch):
    before = tree(public)
    with monkeypatch.context() as patch:
        fired = fail_install(patch, public, restore=True)
        with pytest.raises(
            pub.PublicationRecoveryRequired, match="install failed.*restore denied"
        ):
            publish(public)
    assert fired.count("install") == 1 and fired.count("restore") > 1
    control = pub._control(public)
    journal = json.loads((control / "transaction.json").read_text())
    workspace = control / journal["workspace"]
    return before, control, workspace, journal


def test_restoration_failure_retains_originals_and_retry_recovers(public, monkeypatch):
    before, control, workspace, journal = pending(public, monkeypatch)
    assert len(list((workspace / "originals").iterdir())) == len(FILES)
    assert (
        pub.read_publication_fingerprint(public)
        == before[FINGERPRINT_PATH]["data"].decode().strip()
    )
    assert tree(public) == before
    assert not (control / "transaction.json").exists()


def test_retry_after_partial_restore_is_idempotent(public, monkeypatch):
    before, control, workspace, journal = pending(public, monkeypatch)
    original = Path.replace
    restored = []

    def restore(source, destination):
        if source.name == "restore":
            restored.append(str(destination))
            if len(restored) == 3:
                raise OSError("recovery retry interrupted")
        return original(source, destination)

    with monkeypatch.context() as patch:
        patch.setattr(Path, "replace", restore)
        with pytest.raises(pub.PublicationRecoveryRequired, match="retry interrupted"):
            pub.read_publication_fingerprint(public)
    assert len(restored) > 3  # All other required restores were attempted.
    assert tree(public) != before
    pub.read_publication_fingerprint(public)
    assert tree(public) == before


def test_unreadable_backup_blocks_all_restoration(public, monkeypatch):
    _, _, workspace, _ = pending(public, monkeypatch)
    before = tree(public)
    original = Path.read_bytes
    fired = []

    def read(path):
        if path == workspace / "originals/0":
            fired.append(True)
            raise PermissionError("backup unreadable")
        return original(path)

    with monkeypatch.context() as patch:
        patch.setattr(Path, "read_bytes", read)
        with pytest.raises(pub.PublicationRecoveryRequired, match="backup unreadable"):
            pub.read_publication_fingerprint(public)
    assert fired
    assert tree(public) == before
    assert (workspace / "originals/0").exists()
    pub.read_publication_fingerprint(public)


@pytest.mark.parametrize("kind", ["file", "directory", "occupied_directory"])
@pytest.mark.parametrize("after", [False, True])
def test_removal_failure_retains_recovery_until_owned_paths_can_be_removed(
    tmp_path, monkeypatch, kind, after
):
    root = tmp_path / "public"
    original_unlink, original_rmdir = Path.unlink, Path.rmdir
    fired = []

    def unlink(path, *args, **kwargs):
        if kind == "file" and path == root / FINGERPRINT_PATH:
            if after:
                original_unlink(path, *args, **kwargs)
            fired.append("unlink")
            raise OSError("new file removal denied")
        return original_unlink(path, *args, **kwargs)

    def rmdir(path):
        if (
            kind in {"directory", "occupied_directory"}
            and path == root / "assets/vendor"
        ):
            fired.append("rmdir")
            if kind == "occupied_directory":
                (path / "unowned").write_text("preserve")
            else:
                if after:
                    original_rmdir(path)
                raise OSError("new directory removal denied")
        return original_rmdir(path)

    with monkeypatch.context() as patch:
        fail_install(patch, root)
        patch.setattr(Path, "unlink", unlink)
        patch.setattr(Path, "rmdir", rmdir)
        with pytest.raises(pub.PublicationRecoveryRequired):
            publish(root)
    assert fired
    if kind == "occupied_directory":
        with pytest.raises(pub.PublicationRecoveryRequired):
            pub.read_publication_fingerprint(root)
        assert (root / "assets/vendor/unowned").read_text() == "preserve"
        (root / "assets/vendor/unowned").unlink()  # Owner resolves the obstruction.
    pub.read_publication_fingerprint(root)
    assert not root.exists()


@pytest.mark.parametrize("after", [False, True])
def test_restore_replacement_failure_before_or_after_effect_can_retry(
    public, monkeypatch, after
):
    before, _, workspace, _ = pending(public, monkeypatch)
    original = Path.replace
    fired = []

    def replace(source, destination):
        if source.name == "restore":
            if after:
                original(source, destination)
            fired.append(True)
            raise OSError("restore replacement interrupted")
        return original(source, destination)

    with monkeypatch.context() as patch:
        patch.setattr(Path, "replace", replace)
        with pytest.raises(
            pub.PublicationRecoveryRequired, match="replacement interrupted"
        ):
            pub.read_publication_fingerprint(public)
    assert fired
    assert len(list((workspace / "originals").iterdir())) == len(FILES)
    pub.read_publication_fingerprint(public)
    assert tree(public) == before


@pytest.mark.parametrize("when", ["intent", "result", "commit_before", "commit_after"])
def test_journal_errors_have_unambiguous_commit_or_rollback(public, monkeypatch, when):
    before = tree(public)
    original = pub._save
    fired = []
    calls = {}

    def save(control, journal):
        count = len(journal["touched"])
        key = (journal["phase"], count)
        calls[key] = calls.get(key, 0) + 1
        match = (
            when == "intent"
            and key == ("installing", 5)
            and calls[key] == 1
            or when == "result"
            and key == ("installing", 5)
            and calls[key] == 2
            or when.startswith("commit")
            and journal["phase"] == "committed"
        )
        if match and not fired:
            fired.append(when)
            if when == "commit_after":
                original(control, journal)
            raise OSError("journal write failed")
        return original(control, journal)

    monkeypatch.setattr(pub, "_save", save)
    if when == "commit_after":
        assert publish(public) is False
        assert (public / FINGERPRINT_PATH).read_text() == "new-fingerprint\n"
    else:
        with pytest.raises(OSError, match="journal write failed"):
            publish(public)
        assert tree(public) == before
    assert fired == [when]


def test_committed_cleanup_failure_never_rolls_back(public, monkeypatch):
    original = shutil.rmtree
    fired = []

    def remove(path, *args, **kwargs):
        if Path(path).name == "originals":
            fired.append(True)
            raise PermissionError("cleanup denied")
        return original(path, *args, **kwargs)

    with monkeypatch.context() as patch:
        patch.setattr(shutil, "rmtree", remove)
        assert publish(public) is True
        assert (public / FINGERPRINT_PATH).read_text() == "new-fingerprint\n"
    committed = tree(public)
    assert fired
    assert pub.read_publication_fingerprint(public) == "new-fingerprint"
    assert tree(public) == committed


@pytest.mark.parametrize("operation", ["marker", "workspace", "journal"])
@pytest.mark.parametrize("after", [False, True])
@pytest.mark.parametrize("committed", [False, True])
def test_terminal_cleanup_retries_each_before_and_after_effect_failure(
    public, monkeypatch, operation, after, committed
):
    before = tree(public)
    unlink, rmdir = Path.unlink, Path.rmdir
    fired = []

    def remove(path, *args, **kwargs):
        match = (
            (operation == "marker" and path.name == "owner.json")
            or (operation == "workspace" and path.name.startswith("workspace-"))
            or (operation == "journal" and path.name == "transaction.json")
        )
        original = rmdir if operation == "workspace" and match else unlink
        if match and not fired:
            if after:
                original(path, *args, **kwargs)
            fired.append(operation)
            raise OSError("terminal cleanup interrupted")
        return original(path, *args, **kwargs)

    with monkeypatch.context() as patch:
        patch.setattr(Path, "unlink" if operation != "workspace" else "rmdir", remove)
        if committed:
            assert publish(public) is True
        else:
            fail_install(patch, public)
            with pytest.raises(OSError, match="install failed"):
                publish(public)
            assert tree(public) == before
    assert fired == [operation]
    terminal = tree(public)
    pub.read_publication_fingerprint(public)
    assert tree(public) == terminal
    assert not (pub._control(public) / "transaction.json").exists()


@pytest.mark.parametrize(
    "change",
    [
        "traversal",
        "workspace",
        "phase",
        "root",
        "duplicate",
        "missing_backup",
        "parent_symlink",
        "file_type",
        "restore_symlink",
    ],
)
def test_invalid_recovery_is_rejected_before_any_public_mutation(
    public, monkeypatch, tmp_path, change
):
    _, control, workspace, journal = pending(public, monkeypatch)
    damaged = copy.deepcopy(journal)
    if change == "traversal":
        damaged["files"][0]["path"] = "../outside"
    elif change == "workspace":
        damaged["workspace"] = "../outside"
    elif change == "phase":
        damaged["phase"] = "preparing"
    elif change == "root":
        damaged["root"] = str(tmp_path)
    elif change == "duplicate":
        damaged["files"].append(damaged["files"][0])
    elif change == "missing_backup":
        (workspace / "originals/0").unlink()
    elif change == "parent_symlink":
        (public / "assets").rename(public / "saved-assets")
        (public / "assets").symlink_to(public / "saved-assets")
    elif change == "file_type":
        (public / "current-findings.json").unlink()
        (public / "current-findings.json").mkdir()
    else:
        outside = tmp_path / "outside-restore"
        outside.write_text("unowned")
        (workspace / "restore").unlink(missing_ok=True)
        (workspace / "restore").symlink_to(outside)
    (control / "transaction.json").write_text(json.dumps(damaged))
    before, backups = tree(public), tree(workspace / "originals")
    with pytest.raises(pub.PublicationRecoveryRequired):
        pub.read_publication_fingerprint(public)
    assert tree(public) == before
    assert tree(workspace / "originals") == backups
    if change == "restore_symlink":
        assert outside.read_text() == "unowned"


def test_pending_recovery_blocks_fingerprint_skip_and_analysis(public, monkeypatch):
    from test_workflow_guards import import_workflow_with_stubs

    _, _, workspace, _ = pending(public, monkeypatch)
    (workspace / "originals/0").write_bytes(b"corrupt backup")
    workflow = import_workflow_with_stubs()
    state = {
        "articles": [{"title": "unchanged"}],
        "config": {"output_path": str(public / "index.md")},
        "status": "started",
    }
    monkeypatch.setattr(
        workflow, "compute_articles_fingerprint", lambda _: "new-fingerprint"
    )
    result = asyncio.run(workflow.filter_articles(state))
    assert result["status"] == "failed"
    assert result["failure"]["codes"] == ["publication_recovery_required"]
    assert workflow.should_end(result) == "error"


def test_competing_process_cannot_publish_or_steal_ownership(public):
    with pub._ownership(public) as control:
        inode = (control / "lock").stat().st_ino
        script = """
from pathlib import Path
from src.core.publication import read_publication_fingerprint, PublicationBusy
import sys
try:
    read_publication_fingerprint(Path(sys.argv[1]))
except PublicationBusy:
    sys.exit(0)
sys.exit(1)
"""
        result = subprocess.run(
            [sys.executable, "-B", "-c", script, str(public)], capture_output=True
        )
        assert result.returncode == 0, result.stderr.decode()
        with pytest.raises(pub.PublicationBusy):
            publish(public)
        assert (control / "lock").stat().st_ino == inode
    assert pub.read_publication_fingerprint(public)
    assert (control / "lock").stat().st_ino == inode


def test_success_preserves_unowned_names_and_absent_fingerprint(public):
    before = tree(public)
    pub.publish_report_artifacts(
        parse_report_artifact(REPORT), REPORT, public, None, Path("site"), builder=build
    )
    after = tree(public)
    for name in ["unowned", "empty", ".index.html.sentryinsight.tmp", FINGERPRINT_PATH]:
        assert after[name] == before[name]


@pytest.mark.parametrize(
    "operation", ["replace_before", "replace_after", "fingerprint_partial"]
)
def test_actual_graph_returns_failed_state_and_preserves_tree(
    public, monkeypatch, operation
):
    from test_finding_generation_pipeline import run_real_pipeline

    before = tree(public)
    fired = []
    if operation.startswith("replace"):
        fired = fail_install(
            monkeypatch, public, target="index.html", after=operation.endswith("after")
        )
    else:
        original = Path.write_text

        def write(path, value, *args, **kwargs):
            if path.name == FINGERPRINT_PATH and path.parent.name == "staged":
                path.write_bytes(value[:7].encode())
                fired.append("fingerprint")
                raise OSError("fingerprint write interrupted")
            return original(path, value, *args, **kwargs)

        monkeypatch.setattr(Path, "write_text", write)
    result = run_real_pipeline(monkeypatch, public / "index.md")
    assert fired
    assert result["status"] == "failed"
    assert result["failure"]["stage"] == "site_publication"
    assert "report_path" not in result
    assert tree(public) == before


def test_actual_graph_stops_before_model_when_recovery_is_blocked(public, monkeypatch):
    from test_finding_generation_pipeline import run_real_pipeline

    _, _, workspace, _ = pending(public, monkeypatch)
    (workspace / "originals/0").write_bytes(b"unavailable original")
    before = tree(public)
    result = run_real_pipeline(
        monkeypatch, public / "index.md", expect_model_call=False
    )
    assert result["status"] == "failed"
    assert result["failure"]["codes"] == ["publication_recovery_required"]
    assert tree(public) == before
