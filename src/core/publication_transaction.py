"""Rollback-backed promotion of a validated, bounded static report tree.

The journal contains prior public artifacts and hashes only. A pending or
damaged journal blocks new generation until explicit recovery succeeds.
"""

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import tempfile
from typing import TypedDict


class JournalEntry(TypedDict):
    path: str
    prior_sha256: str | None
    next_sha256: str


JOURNAL_DIRECTORY = ".sentryinsight-publication"
COMPLETED_DIRECTORY = ".sentryinsight-publication-complete"
CORE = {
    "index.md",
    "index.html",
    "current-findings.json",
    "sitemap.xml",
    ".sentryinsight-articles-fingerprint",
}
ASSETS = {
    "assets/site.css",
    "assets/report.js",
    "assets/theme-bootstrap.js",
    "assets/vendor/dompurify.min.js",
    "assets/vendor/DOMPURIFY-LICENSE.txt",
}
MAX_FILES = 4096
MAX_JOURNAL_BYTES = 2 * 1024 * 1024


class PublicationError(ValueError):
    def __init__(self, code: str):
        self.code = code
        super().__init__(code)


def _allowed(name: str) -> bool:
    return name in CORE | ASSETS | {"reports/index.json", "reports/index.html"} or bool(
        re.fullmatch(r"reports/\d{4}-\d{2}-\d{2}\.(?:md|html)", name)
    )


def _safe_path(root: Path, name: str) -> Path:
    if not _allowed(name):
        raise PublicationError("publication_recovery_required")
    target = root / name
    for path in [root, *target.relative_to(root).parents]:
        # Relative parents are checked below using their absolute counterpart.
        absolute = path if path.is_absolute() else root / path
        if absolute.is_symlink():
            raise PublicationError("publication_recovery_required")
    if target.is_symlink() or (target.exists() and not target.is_file()):
        raise PublicationError("publication_recovery_required")
    return target


def _hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _sync_directory(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _atomic_copy(
    source: Path, destination: Path, *, expected_sha256: str | None = None
) -> None:
    created = [parent for parent in destination.parents if not parent.exists()]
    destination.parent.mkdir(parents=True, exist_ok=True)
    for directory in reversed(created):
        _sync_directory(directory.parent)
    fd, name = tempfile.mkstemp(prefix=".sentryinsight-", dir=destination.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "wb") as output, source.open("rb") as incoming:
            shutil.copyfileobj(incoming, output)
            os.fchmod(output.fileno(), stat.S_IMODE(source.stat().st_mode))
            output.flush()
            os.fsync(output.fileno())
        if expected_sha256 is not None and _hash(temporary) != expected_sha256:
            raise PublicationError("invalid_publication_stage")
        os.replace(temporary, destination)
        _sync_directory(destination.parent)
    finally:
        temporary.unlink(missing_ok=True)


def ensure_no_pending_publication(root: Path) -> None:
    for name in (JOURNAL_DIRECTORY, COMPLETED_DIRECTORY):
        journal = root / name
        if journal.exists() or journal.is_symlink():
            raise PublicationError("publication_recovery_required")


def _load_journal(
    root: Path, *, completed: bool = False
) -> tuple[Path, list[dict], list[str]]:
    journal = root / (COMPLETED_DIRECTORY if completed else JOURNAL_DIRECTORY)
    path = journal / "journal.json"
    if journal.is_symlink() or path.is_symlink() or not path.is_file():
        raise PublicationError("publication_recovery_required")
    if path.stat().st_size > MAX_JOURNAL_BYTES:
        raise PublicationError("publication_recovery_required")
    data = json.loads(path.read_text())
    if (
        not isinstance(data, dict)
        or set(data) != {"schema_version", "files", "created_directories", "target"}
        or data["schema_version"] != 1
        or data["target"] not in {"prior", "next"}
    ):
        raise PublicationError("publication_recovery_required")
    entries, directories = data["files"], data["created_directories"]
    if (
        not isinstance(entries, list)
        or not 1 <= len(entries) <= MAX_FILES
        or not isinstance(directories, list)
    ):
        raise PublicationError("publication_recovery_required")
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {
            "path",
            "prior_sha256",
            "next_sha256",
        }:
            raise PublicationError("publication_recovery_required")
        name = entry["path"]
        if not isinstance(name, str) or name in seen:
            raise PublicationError("publication_recovery_required")
        seen.add(name)
        destination = _safe_path(root, name)
        prior, following = entry["prior_sha256"], entry["next_sha256"]
        if not isinstance(following, str) or not re.fullmatch(
            "[a-f0-9]{64}", following
        ):
            raise PublicationError("publication_recovery_required")
        if prior is not None and not completed:
            backup = _safe_path(journal / "prior", name)
            if (
                not isinstance(prior, str)
                or not re.fullmatch("[a-f0-9]{64}", prior)
                or not backup.is_file()
                or _hash(backup) != prior
            ):
                raise PublicationError("publication_recovery_required")
        current = _hash(destination) if destination.exists() else None
        expected = prior if data["target"] == "prior" else following
        if current not in ({expected} if completed else {prior, following}):
            raise PublicationError("publication_recovery_required")
    if (
        not CORE <= seen
        or len(set(directories)) != len(directories)
        or any(
            name not in {"reports", "assets", "assets/vendor"} for name in directories
        )
    ):
        raise PublicationError("publication_recovery_required")
    for name in directories:
        if (root / name).is_symlink():
            raise PublicationError("publication_recovery_required")
    return journal, entries, directories


def _cleanup_completed(root: Path) -> bool:
    """Best-effort cleanup after the commit point; retain its manifest until last."""
    journal = root / COMPLETED_DIRECTORY
    try:
        # Sync the commit rename before discarding any backup. If this fails,
        # the complete manifest and backups remain and the next run is blocked.
        _sync_directory(root)
        if (journal / "prior").exists():
            shutil.rmtree(journal / "prior")
        if set(path.name for path in journal.iterdir()) != {"journal.json"}:
            return False
        payload = (journal / "journal.json").read_bytes()
        (journal / "journal.json").unlink()
        try:
            journal.rmdir()
        except OSError:
            (journal / "journal.json").write_bytes(payload)
            return False
        # A completed rename may reappear after a crash if removal is not
        # durable. Its manifest verifies the already committed bytes on recovery.
        try:
            _sync_directory(root)
        except OSError:
            pass
        return True
    except OSError:
        return False


def recover_publication(root: Path) -> None:
    """Restore a pending promotion, or finish cleanup of a committed promotion."""
    root = root.resolve()
    try:
        completed = (root / COMPLETED_DIRECTORY).exists()
        if completed and (root / JOURNAL_DIRECTORY).exists():
            raise PublicationError("publication_recovery_required")
        journal, entries, directories = _load_journal(root, completed=completed)
        if completed:
            if not _cleanup_completed(root):
                raise PublicationError("publication_recovery_required")
            return
        # All paths and bytes are checked before the first restoration.
        for entry in entries:
            destination = _safe_path(root, entry["path"])
            if entry["prior_sha256"] is None:
                destination.unlink(missing_ok=True)
                if destination.parent.exists():
                    _sync_directory(destination.parent)
            else:
                _atomic_copy(
                    journal / "prior" / entry["path"],
                    destination,
                    expected_sha256=entry["prior_sha256"],
                )
        for name in sorted(directories, key=lambda item: item.count("/"), reverse=True):
            directory = root / name
            if directory.exists() and not any(directory.iterdir()):
                directory.rmdir()
        # No failure may remove backups before all restoration has completed.
        _sync_directory(root)
        payload = json.loads((journal / "journal.json").read_text())
        payload["target"] = "prior"
        fd, name = tempfile.mkstemp(prefix=".restored-", dir=journal)
        temporary = Path(name)
        try:
            with os.fdopen(fd, "w") as stream:
                json.dump(payload, stream, sort_keys=True)
                stream.flush()
                os.fsync(stream.fileno())
            temporary.replace(journal / "journal.json")
        finally:
            temporary.unlink(missing_ok=True)
        _sync_directory(journal)
        journal.rename(root / COMPLETED_DIRECTORY)
        if not _cleanup_completed(root):
            raise PublicationError("publication_recovery_required")
    except (OSError, ValueError, TypeError, KeyError):
        raise PublicationError("publication_recovery_required") from None


def promote_artifacts(staged: Path, root: Path) -> str:
    """Promote a previously validated stage, restoring every touched file on error."""
    if staged.is_symlink() or root.is_symlink():
        raise PublicationError("invalid_publication_stage")
    staged, root = staged.resolve(), root.resolve()
    ensure_no_pending_publication(root)
    names = []
    for path in staged.rglob("*"):
        name = path.relative_to(staged).as_posix()
        if path.is_symlink() or (not path.is_dir() and not path.is_file()):
            raise PublicationError("invalid_publication_stage")
        if path.is_file():
            if not _allowed(name):
                raise PublicationError("invalid_publication_stage")
            _safe_path(root, name)
            names.append(name)
    if not CORE <= set(names) or len(names) > MAX_FILES:
        raise PublicationError("invalid_publication_stage")
    names.sort(key=lambda name: (name == "index.html", name))
    root.mkdir(parents=True, exist_ok=True)
    journal = root / JOURNAL_DIRECTORY
    try:
        journal.mkdir(mode=0o700)
    except FileExistsError:
        raise PublicationError("publication_recovery_required") from None
    ready = False
    try:
        entries: list[JournalEntry] = []
        directories = set()
        for name in names:
            destination = _safe_path(root, name)
            prior = None
            if destination.exists():
                backup = journal / "prior" / name
                backup.parent.mkdir(parents=True, exist_ok=True)
                # Backups are completed before any canonical path is touched.
                shutil.copy2(destination, backup)
                with backup.open("rb") as stream:
                    os.fsync(stream.fileno())
                prior = _hash(backup)
            for parent in destination.relative_to(root).parents:
                if parent != Path(".") and not (root / parent).exists():
                    directories.add(parent.as_posix())
            entries.append(
                {
                    "path": name,
                    "prior_sha256": prior,
                    "next_sha256": _hash(staged / name),
                }
            )
        payload = {
            "schema_version": 1,
            "target": "next",
            "files": entries,
            "created_directories": sorted(directories),
        }
        with (journal / "journal.json").open("x") as stream:
            json.dump(payload, stream, sort_keys=True)
            stream.flush()
            os.fsync(stream.fileno())
        for directory in sorted(
            (path for path in journal.rglob("*") if path.is_dir()),
            key=lambda path: len(path.parts),
            reverse=True,
        ):
            _sync_directory(directory)
        _sync_directory(journal)
        _sync_directory(root)
        ready = True
        for entry in entries:
            source = staged / entry["path"]
            if _hash(source) != entry["next_sha256"]:
                raise PublicationError("invalid_publication_stage")
            destination = _safe_path(root, entry["path"])
            current = _hash(destination) if destination.exists() else None
            if current != entry["prior_sha256"]:
                raise PublicationError("publication_recovery_required")
            _atomic_copy(source, destination, expected_sha256=entry["next_sha256"])
        _sync_directory(root)
    except (OSError, ValueError):
        if not ready:
            try:
                shutil.rmtree(journal)
            except OSError:
                raise PublicationError("publication_recovery_required") from None
            raise PublicationError("publication_rolled_back") from None
        recover_publication(root)
        raise PublicationError("publication_rolled_back") from None

    # Commit point: all validated files and their directories are durable and
    # the complete recovery manifest moves atomically to a committed state.
    # Cleanup cannot turn this complete publication into a misleading failure.
    try:
        journal.rename(root / COMPLETED_DIRECTORY)
    except OSError:
        # An operation can take effect before its caller observes an error.
        # Inspect the manifest location and hashes instead of repeating it or
        # describing committed bytes as a rollback.
        completed = root / COMPLETED_DIRECTORY
        if completed.exists() and not journal.exists():
            _load_journal(root, completed=True)
        elif journal.exists() and not completed.exists():
            recover_publication(root)
            raise PublicationError("publication_rolled_back") from None
        else:
            raise PublicationError("publication_recovery_required") from None
    return (
        "publication_complete"
        if _cleanup_completed(root)
        else "publication_cleanup_pending"
    )
