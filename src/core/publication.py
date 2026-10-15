"""Recoverable publication of one report generation in the existing site layout.

The lock serializes cooperating publishers and fingerprint readers. The journal
protects handled I/O failures and retry; individual replacements are visible to
other readers, and this is not a power-loss atomic filesystem transaction.
"""

from contextlib import contextmanager
import fcntl
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import tempfile
from typing import Any, Callable, Iterator

from scripts.build_site import (
    ArchiveConflictError,
    SiteBuildError,
    archive_previous_report,
    build_site,
)
from .content_fingerprint import FINGERPRINT_PATH, read_stored_fingerprint
from .report_artifact import ReportArtifact


class PublicationError(OSError):
    code = "filesystem_error"


class PublicationBusy(PublicationError):
    code = "publication_busy"


class PublicationRecoveryRequired(PublicationError):
    code = "publication_recovery_required"


def _info(path: Path) -> dict[str, Any] | None:
    try:
        value = path.lstat()
    except FileNotFoundError:
        return None
    if stat.S_ISREG(value.st_mode):
        return {
            "kind": "file",
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "size": value.st_size,
            "mode": stat.S_IMODE(value.st_mode),
            "mtime_ns": value.st_mtime_ns,
        }
    if stat.S_ISDIR(value.st_mode):
        return {
            "kind": "directory",
            "mode": stat.S_IMODE(value.st_mode),
            "dev": value.st_dev,
            "ino": value.st_ino,
        }
    raise PublicationError(f"Refusing non-regular publication participant: {path}")


def _require_directory(path: Path) -> None:
    value = _info(path)
    if value is not None and value["kind"] != "directory":
        raise PublicationError(f"Expected publication directory: {path}")


def _root(output_root: Path) -> Path:
    # Resolve parent aliases (e.g. macOS /var) without following the root itself.
    absolute = Path(os.path.abspath(output_root))
    if absolute == absolute.parent:
        raise PublicationError("A filesystem root cannot be a publication root")
    root = absolute.parent.resolve() / absolute.name
    _require_directory(root)
    return root


def _control(root: Path) -> Path:
    """Find the permanent coordinator, including when the public root is absent.

    Search all ancestors before choosing an anchor. A publisher creates this
    directory before any public directories, so subsequent publishers find the
    same lock even after the previously absent parent chain has been created.
    Neither the directory nor its lock inode is ever removed or auto-stolen.
    """
    name = ".sentryinsight-publication-" + hashlib.sha256(os.fsencode(root)).hexdigest()
    found = [
        parent / name
        for parent in root.parents
        if (parent / name).exists() or (parent / name).is_symlink()
    ]
    if len(found) > 1:
        raise PublicationRecoveryRequired("Ambiguous publication coordinators")
    if found:
        control = found[0]
    else:
        anchor = next(parent for parent in root.parents if parent.exists())
        _require_directory(anchor)
        control = anchor / name
        try:
            control.mkdir(mode=0o700)
        except FileExistsError:
            pass
    value = control.lstat()
    if (
        not stat.S_ISDIR(value.st_mode)
        or value.st_uid != os.getuid()
        or stat.S_IMODE(value.st_mode) != 0o700
    ):
        raise PublicationRecoveryRequired("Unsafe publication coordinator")
    return control


@contextmanager
def _ownership(root: Path) -> Iterator[Path]:
    control = _control(root)
    lock = control / "lock"
    fd = os.open(lock, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        info = os.fstat(fd)
        if (
            not stat.S_ISREG(info.st_mode)
            or info.st_nlink != 1
            or info.st_uid != os.getuid()
            or stat.S_IMODE(info.st_mode) != 0o600
        ):
            raise PublicationRecoveryRequired("Unsafe publication ownership file")
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise PublicationBusy("Another publisher owns this output root") from exc
        if lock.lstat().st_ino != info.st_ino:
            raise PublicationRecoveryRequired("Publication ownership file changed")
        yield control
    finally:
        os.close(fd)


def _save(control: Path, journal: dict[str, Any]) -> None:
    # Never write a partially serialized journal over the last valid intent.
    fd, name = tempfile.mkstemp(prefix="journal-", dir=control)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "w") as stream:
            json.dump(journal, stream, sort_keys=True)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(control / "transaction.json")
    except OSError as primary:
        try:
            temporary.unlink(missing_ok=True)
        except OSError as cleanup:
            primary.add_note(f"Journal temporary cleanup failed: {cleanup}")
        raise
    else:
        temporary.unlink(missing_ok=True)


def _relative(value: Any) -> str:
    if not isinstance(value, str):
        raise ValueError("Non-string manifest path")
    path = Path(value)
    if (
        not value
        or path.is_absolute()
        or ".." in path.parts
        or str(path) != value
        or value == "."
    ):
        raise ValueError("Unsafe manifest path")
    return value


def _metadata(value: Any, kind: str) -> None:
    if value is None:
        return
    keys = (
        {"kind", "sha256", "size", "mode", "mtime_ns"}
        if kind == "file"
        else {"kind", "mode", "dev", "ino"}
    )
    if not isinstance(value, dict) or set(value) != keys or value["kind"] != kind:
        raise ValueError("Invalid manifest metadata")
    for key in keys - {"kind", "sha256"}:
        if type(value[key]) is not int or value[key] < 0:
            raise ValueError("Invalid manifest metadata number")
    if value["mode"] > 0o7777:
        raise ValueError("Invalid manifest mode")
    if kind == "file" and (
        not isinstance(value["sha256"], str)
        or len(value["sha256"]) != 64
        or any(c not in "0123456789abcdef" for c in value["sha256"])
    ):
        raise ValueError("Invalid manifest hash")


def _directories(root: Path, anchor: Path, names: list[str]) -> list[Path]:
    paths = set()
    for name in names:
        parent = (root / name).parent
        while parent != anchor:
            paths.add(parent)
            parent = parent.parent
    return sorted(paths, key=lambda path: (len(path.parts), str(path)))


def _validate(control: Path, root: Path, journal: Any) -> Path:
    """Validate structure and containment without mutating any participant."""
    if not isinstance(journal, dict) or set(journal) != {
        "version",
        "root",
        "workspace",
        "phase",
        "files",
        "directories",
        "touched",
        "created",
        "workspace_info",
    }:
        raise ValueError("Invalid publication journal shape")
    if journal["version"] != 1 or journal["root"] != str(root):
        raise ValueError("Publication journal belongs to another root/version")
    if journal["phase"] not in {
        "preparing",
        "prepared",
        "installing",
        "rolling_back",
        "rolled_back",
        "committed",
    }:
        raise ValueError("Unknown publication journal state")
    name = _relative(journal["workspace"])
    if "/" in name or not name.startswith("workspace-"):
        raise ValueError("Invalid transaction workspace")
    workspace = control / name
    _require_directory(workspace)
    _metadata(journal["workspace_info"], "directory")
    if journal["workspace_info"] is None:
        raise ValueError("Missing transaction workspace identity")
    if workspace.exists():
        if _info(workspace) != journal["workspace_info"]:
            raise ValueError("Transaction workspace identity changed")
        owner = workspace / "owner.json"
        if (
            _info(owner) is None
            and journal["phase"]
            in {"committed", "rolled_back", "preparing", "prepared"}
            and not list(workspace.iterdir())
        ):
            pass  # Cleanup removed the marker but directory removal failed.
        elif _info(owner) is None or json.loads(owner.read_text()) != {
            "root": str(root),
            "workspace": name,
        }:
            raise ValueError("Transaction workspace ownership mismatch")
    elif journal["phase"] not in {"committed", "rolled_back", "preparing", "prepared"}:
        raise ValueError("Missing recovery workspace")
    for field in ("files", "directories", "touched", "created"):
        if not isinstance(journal[field], list):
            raise ValueError("Invalid journal collection")
    names = []
    for entry in journal["files"]:
        if not isinstance(entry, dict) or set(entry) != {"path", "old", "new"}:
            raise ValueError("Invalid file entry")
        names.append(_relative(entry["path"]))
        _metadata(entry["old"], "file")
        _metadata(entry["new"], "file")
        if entry["new"] is None:
            raise ValueError("Missing prepared file metadata")
    if len(set(names)) != len(names):
        raise ValueError("Duplicate manifest file")
    expected_dirs = _directories(root, control.parent, names)
    dir_names = [str(path.relative_to(control.parent)) for path in expected_dirs]
    if len(journal["directories"]) != len(dir_names):
        raise ValueError("Incomplete directory manifest")
    for entry, name in zip(journal["directories"], dir_names):
        if not isinstance(entry, dict) or set(entry) != {"path", "old"}:
            raise ValueError("Invalid directory entry")
        if entry["path"] != name:
            raise ValueError("Invalid directory containment/order")
        _metadata(entry["old"], "directory")
    if any(str(root / name) in {str(p) for p in expected_dirs} for name in names):
        raise ValueError("Conflicting file and directory participants")
    for field, allowed in (("touched", names), ("created", dir_names)):
        values = journal[field]
        if any(not isinstance(v, str) for v in values):
            raise ValueError("Invalid intent path")
        if len(set(values)) != len(values) or not set(values) <= set(allowed):
            raise ValueError("Invalid intent set")
    missing_dirs = [e["path"] for e in journal["directories"] if e["old"] is None]
    if journal["created"] != missing_dirs[: len(journal["created"])]:
        raise ValueError("Invalid directory intent order")
    if journal["touched"] != names[: len(journal["touched"])]:
        raise ValueError("Invalid file intent order")
    if journal["phase"] in {"preparing", "prepared"} and (
        journal["touched"] or journal["created"]
    ):
        raise ValueError("Preparation journal contains public mutation intents")
    if journal["phase"] == "preparing" and (names or dir_names):
        raise ValueError("Incomplete prepared manifest")
    if journal["phase"] == "committed" and (
        journal["touched"] != names or journal["created"] != missing_dirs
    ):
        raise ValueError("Incomplete committed manifest")
    return workspace


def _participants(control: Path, root: Path, journal: dict[str, Any]) -> None:
    # Directories first: never read through a changed ancestor or symlink.
    for entry in journal["directories"]:
        actual = _info(control.parent / entry["path"])
        if entry["old"] is not None:
            if actual != entry["old"]:
                raise PublicationError("An original publication directory changed")
        elif actual is not None and (
            entry["path"] not in journal["created"] or actual["kind"] != "directory"
        ):
            raise PublicationError("An absent publication directory changed")
    for entry in journal["files"]:
        actual = _info(root / entry["path"])
        allowed = [entry["old"]]
        if entry["path"] in journal["touched"]:
            allowed.append(entry["new"])
        if actual not in allowed:
            raise PublicationError("A publication file changed outside the transaction")


def _originals(workspace: Path, journal: dict[str, Any]) -> None:
    _require_directory(workspace / "originals")
    for index, entry in enumerate(journal["files"]):
        if (
            entry["old"] is not None
            and _info(workspace / "originals" / str(index)) != entry["old"]
        ):
            raise PublicationError(
                "An original recovery snapshot is missing or changed"
            )


def _cleanup(control: Path, workspace: Path) -> None:
    """Delete only a validated, terminal transaction's private workspace."""
    if workspace.exists():
        # Keep the ownership marker until all other contents are gone.
        for path in workspace.iterdir():
            if path.name == "owner.json":
                continue
            if path.is_dir() and not path.is_symlink():
                shutil.rmtree(path)
            else:
                path.unlink()
        (workspace / "owner.json").unlink(missing_ok=True)
        workspace.rmdir()
    (control / "transaction.json").unlink(missing_ok=True)


def _finish_commit(control: Path, workspace: Path) -> bool:
    # A cleanup error cannot turn verified commitment into a preservation claim.
    try:
        _cleanup(control, workspace)
    except OSError:
        return True
    return False


def _rollback(control: Path, root: Path, journal: dict[str, Any]) -> None:
    workspace = _validate(control, root, journal)
    _originals(workspace, journal)
    _participants(control, root, journal)
    temporary_info = _info(workspace / "restore")
    if temporary_info is not None and temporary_info["kind"] != "file":
        raise PublicationError("Invalid recovery temporary participant")
    journal["phase"] = "rolling_back"
    _save(control, journal)
    errors = []
    for index, entry in reversed(list(enumerate(journal["files"]))):
        if entry["path"] not in journal["touched"]:
            continue
        try:
            destination = root / entry["path"]
            if _info(destination) == entry["old"]:
                continue
            if entry["old"] is None:
                destination.unlink()
            else:
                temporary = workspace / "restore"
                shutil.copy2(workspace / "originals" / str(index), temporary)
                temporary.replace(destination)
        except OSError as exc:
            errors.append(str(exc))
    for name in reversed(journal["created"]):
        try:
            path = control.parent / name
            if path.exists():
                path.rmdir()  # Refuse unexpected occupants; never recursive here.
        except OSError as exc:
            errors.append(str(exc))
    # Verify all required restoration effects, including failures after effect.
    for entry in journal["files"]:
        if _info(root / entry["path"]) != entry["old"]:
            errors.append("Original file not restored")
    for entry in journal["directories"]:
        if _info(control.parent / entry["path"]) != entry["old"]:
            errors.append("Original directory not restored")
    if errors:
        raise PublicationRecoveryRequired("Recovery failed: " + "; ".join(errors))
    journal["phase"] = "rolled_back"
    _save(control, journal)
    _cleanup(control, workspace)


def _recover(control: Path, root: Path) -> bool:
    path = control / "transaction.json"
    try:
        if _info(path) is None:
            return True
        journal = json.loads(path.read_text())
        workspace = _validate(control, root, journal)
        if journal["phase"] in {"committed", "rolled_back", "preparing", "prepared"}:
            _cleanup(control, workspace)
            return True
        _rollback(control, root, journal)
        return not path.exists()
    except (OSError, ValueError, TypeError, KeyError) as exc:
        raise PublicationRecoveryRequired(
            f"Publication recovery required: {exc}"
        ) from exc


def read_publication_fingerprint(output_root: Path) -> str | None:
    """Resolve recovery under the publication lock before any cache decision."""
    root = _root(output_root)
    with _ownership(root) as control:
        if not _recover(control, root):
            raise PublicationRecoveryRequired("Publication cleanup is still pending")
        path = root / FINGERPRINT_PATH
        value = _info(path)
        if value is not None and value["kind"] != "file":
            raise PublicationError("Invalid fingerprint participant")
        return read_stored_fingerprint(str(path))


def publish_report_artifacts(
    artifact: ReportArtifact,
    report_source: str,
    output_root: Path,
    fingerprint: str | None,
    templates: Path,
    *,
    builder: Callable[..., Any] = build_site,
) -> bool:
    """Install one complete generation; return whether committed cleanup remains."""
    root = _root(output_root)
    with _ownership(root) as control:
        if not _recover(control, root):
            raise PublicationRecoveryRequired("Publication cleanup is still pending")
        workspace = Path(tempfile.mkdtemp(prefix="workspace-", dir=control))
        (workspace / "owner.json").write_text(
            json.dumps(
                {
                    "root": str(root),
                    "workspace": workspace.name,
                }
            )
        )
        journal: dict[str, Any] = {
            "version": 1,
            "root": str(root),
            "workspace": workspace.name,
            "workspace_info": _info(workspace),
            "phase": "preparing",
            "files": [],
            "directories": [],
            "touched": [],
            "created": [],
        }
        try:
            _save(control, journal)
            staged = workspace / "staged"
            reports = staged / "reports"
            reports.mkdir(parents=True)
            _require_directory(root / "reports")
            for path in (root / "reports").glob("????-??-??.md"):
                archived = _info(path)
                if archived is None or archived["kind"] != "file":
                    raise PublicationError("Invalid archive participant")
                shutil.copy2(path, reports / path.name)
            current = root / "index.md"
            if _info(current) is not None:
                archive_previous_report(
                    current_source=current.read_text(),
                    next_report=artifact,
                    reports_path=reports,
                )
            (staged / "index.md").write_text(report_source)
            builder(
                report_path=staged / "index.md",
                output_path=staged,
                template_path=templates,
            )
            if fingerprint:
                (staged / FINGERPRINT_PATH).write_text(fingerprint + "\n")
            names = sorted(
                (
                    str(path.relative_to(staged))
                    for path in staged.rglob("*")
                    if path.is_file()
                ),
                key=lambda name: (name == FINGERPRINT_PATH, name == "index.html", name),
            )
            dirs = _directories(root, control.parent, names)
            for path in dirs:
                _require_directory(path)
            originals = workspace / "originals"
            originals.mkdir()
            prepared = workspace / "prepared"
            prepared.mkdir()
            files: list[dict[str, Any]] = []
            for index, name in enumerate(names):
                old, new = _info(root / name), _info(staged / name)
                if old is not None:
                    if old["kind"] != "file":
                        raise PublicationError("Invalid publication destination")
                    shutil.copy2(root / name, originals / str(index))
                shutil.copy2(staged / name, prepared / str(index))
                if _info(prepared / str(index)) != new:
                    raise PublicationError("Prepared payload verification failed")
                files.append({"path": name, "old": old, "new": new})
            journal.update(
                phase="prepared",
                files=files,
                directories=[
                    {"path": str(p.relative_to(control.parent)), "old": _info(p)}
                    for p in dirs
                ],
            )
            _validate(control, root, journal)
            _originals(workspace, journal)
            _participants(control, root, journal)
            _save(control, journal)
            journal["phase"] = "installing"
            _save(control, journal)
            for entry in journal["directories"]:
                if entry["old"] is None:
                    journal["created"].append(entry["path"])
                    _save(control, journal)
                    (control.parent / entry["path"]).mkdir()
            for index, entry in enumerate(files):
                journal["touched"].append(entry["path"])
                _save(control, journal)
                (prepared / str(index)).replace(root / entry["path"])
                _save(control, journal)
            if any(_info(root / e["path"]) != e["new"] for e in files):
                raise PublicationError("Published manifest verification failed")
            journal["phase"] = "committed"
            _save(control, journal)
        except (OSError, ValueError, ArchiveConflictError, SiteBuildError) as primary:
            # A journal replacement can report an error after taking effect.
            # In-memory intent is conservative even if the last save failed.
            try:
                persisted = control / "transaction.json"
                if (
                    persisted.exists()
                    and json.loads(persisted.read_text()).get("phase") == "committed"
                ):
                    return _finish_commit(control, workspace)
                if journal["phase"] in {"installing", "committed", "rolling_back"}:
                    _rollback(control, root, journal)
                else:
                    _cleanup(control, workspace)
            except (OSError, ValueError, TypeError, KeyError) as recovery:
                raise PublicationRecoveryRequired(
                    f"Publication failed: {primary}; recovery failed: {recovery}"
                ) from primary
            raise
        return _finish_commit(control, workspace)
