#!/usr/bin/env python3
"""Build the SentryInsight static artifact and a prebuilt deploy layout.

The existing Pages packager renders the accepted Markdown at a pinned revision,
unchanged. This wrapper verifies that every packager input on disk equals the
pinned Git blob, runs the pinned packager on a snapshot of those inputs, and
promotes the result as an immutable build behind an atomically replaced
pointer. A failed or interrupted build never replaces the accepted artifact.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import secrets
import shutil
import socket
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

SITE = "SentryInsight"
DEPLOY_CONFIG: dict[str, int] = {"version": 3}
# Tripwires against accidental inclusion (node_modules, caches, evidence), not
# hosting limits. The measured package is about 4 MB.
DEFAULT_LIMITS: dict[str, int] = {
    "max_file_bytes": 2 * 1024 * 1024,
    "max_total_bytes": 32 * 1024 * 1024,
}
PACKAGER = "scripts/package_pages.py"
SNAPSHOT_FILES = frozenset(
    {
        "config/config.json",
        "contracts/reporting-identity-v1.json",
        "index.md",
        "publication/site.json",
        "scripts/build_site.py",
        "scripts/package_pages.py",
        "scripts/validate_report.py",
    }
)
SNAPSHOT_PREFIXES = ("assets/", "site/", "src/")
# The public site configuration exists only from the revision that introduced
# it; earlier revisions build without it.
# The configuration selects advisory grounding for the report gate; without it
# the gate stays strict.
OPTIONAL_INPUTS = frozenset({"publication/site.json", "config/config.json"})
REQUIRED_INPUTS = (
    "index.md",
    "site/archive.html",
    "site/report.html",
    *sorted(SNAPSHOT_FILES - {"index.md"} - OPTIONAL_INPUTS),
)
DATED_REPORT = re.compile(r"^reports/\d{4}-\d{2}-\d{2}\.md$")
ALLOWED_DOT_FILES = frozenset({".nojekyll"})
PRIVATE_NAMES = frozenset(
    {
        "__pycache__",
        "agent-instructions.md",
        "agent.md",
        "agent_instructions.md",
        "agents.md",
        "assistant-instructions.md",
        "assistant_instructions.md",
        "claude.md",
        "copilot-instructions.md",
        "gemini.md",
        "node_modules",
        "playwright-report",
        "test-results",
        "thumbs.db",
        "venv",
    }
)
IMPLEMENTATION_FILE = re.compile(
    r"(\.(py|go|sh|ya?ml|toml|lock|map)|^package(-lock)?\.json)$", re.IGNORECASE
)
PRIVATE_EVIDENCE = re.compile(r"(receipt|screenshot|\.log$)", re.IGNORECASE)
FULL_COMMIT_ID = re.compile(r"^([0-9a-f]{40}|[0-9a-f]{64})$")
POINTER = "current.json"
LOCK = ".lock"
STAGING_PREFIX = ".staging-"

Hooks = Mapping[str, Callable[[], None]]


class StaticArtifactError(RuntimeError):
    """Raised when the static artifact cannot be built or promoted safely."""


@dataclass(frozen=True)
class TreeEntry:
    mode: str
    kind: str
    oid: str
    path: str


@dataclass(frozen=True)
class CurrentBuild:
    site: str
    source_revision: str
    inventory_digest: str
    file_count: int
    total_bytes: int
    build_dir: str
    artifact_dir: Path
    deploy_dir: Path


@dataclass(frozen=True)
class BuildResult:
    site: str
    source_revision: str
    inventory_digest: str
    file_count: int
    total_bytes: int
    build_dir: str
    artifact_dir: Path
    deploy_dir: Path
    receipt_path: Path
    reused_existing_build: bool


class Git:
    """Runs read-only Git commands in the source and records each one."""

    def __init__(self, source: Path, commands: list[dict[str, object]]) -> None:
        self.source = source
        self.commands = commands

    def try_run(self, *args: str) -> str | None:
        argv = ["git", *args]
        completed = subprocess.run(
            argv, cwd=self.source, capture_output=True, text=True, check=False
        )
        self.commands.append({"argv": argv, "exit_status": completed.returncode})
        if completed.returncode != 0:
            return None
        return completed.stdout

    def run(self, *args: str) -> str:
        output = self.try_run(*args)
        if output is None:
            raise StaticArtifactError(f"git {' '.join(args)} failed in {self.source}")
        return output

    def read_blobs(self, oids: list[str]) -> list[bytes]:
        """Read blobs straight from the object store, independent of the worktree."""
        if not oids:
            return []
        argv = ["git", "cat-file", "--batch"]
        completed = subprocess.run(
            argv,
            cwd=self.source,
            input="".join(f"{oid}\n" for oid in oids).encode(),
            capture_output=True,
            check=False,
        )
        self.commands.append({"argv": argv, "exit_status": completed.returncode})
        if completed.returncode != 0:
            raise StaticArtifactError(f"git cat-file --batch failed in {self.source}")
        blobs = []
        output = completed.stdout
        offset = 0
        for oid in oids:
            newline = output.index(b"\n", offset)
            header_oid, kind, size = output[offset:newline].decode().split(" ")
            if header_oid != oid or kind != "blob":
                raise StaticArtifactError(f"git object {oid} is not a readable blob")
            start = newline + 1
            blobs.append(output[start : start + int(size)])
            offset = start + int(size) + 1
        return blobs


def check_public_path(relative_path: str) -> None:
    """Refuse paths that must never be published from the artifact."""
    if relative_path.startswith("/") or "\\" in relative_path or "\0" in relative_path:
        raise StaticArtifactError(f"{relative_path} is not a safe relative path")
    segments = relative_path.split("/")
    for segment in segments:
        if segment in {"", ".", ".."}:
            raise StaticArtifactError(f"{relative_path} escapes the artifact root")
        if segment.startswith(".") and relative_path not in ALLOWED_DOT_FILES:
            raise StaticArtifactError(
                f"{relative_path} is a dot path and must not be published"
            )
        if segment.lower() in PRIVATE_NAMES:
            raise StaticArtifactError(
                f"{relative_path} is a private or implementation path "
                "and must not be published"
            )
    if relative_path.lower().startswith("docs/notes/"):
        raise StaticArtifactError(
            f"{relative_path} is a private or implementation path "
            "and must not be published"
        )
    if IMPLEMENTATION_FILE.search(segments[-1]):
        raise StaticArtifactError(
            f"{relative_path} is an implementation file and must not be published"
        )
    if PRIVATE_EVIDENCE.search(segments[-1]):
        raise StaticArtifactError(
            f"{relative_path} looks like private evidence (receipt, log or screenshot)"
        )


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _git_blob_id(object_format: str, data: bytes) -> str:
    digest = hashlib.new(object_format)
    digest.update(f"blob {len(data)}\0".encode())
    digest.update(data)
    return digest.hexdigest()


def _inventory_digest(inventory: list[dict[str, object]]) -> str:
    lines = "".join(
        f"{entry['sha256']} {entry['bytes']} {entry['path']}\n" for entry in inventory
    )
    return _sha256(lines.encode())


def _is_within(child: Path, parent: Path) -> bool:
    return child == parent or parent in child.parents


def _inventory_of(
    root: Path, limits: Mapping[str, int]
) -> tuple[list[dict[str, object]], int, str]:
    inventory: list[dict[str, object]] = []
    for directory, directory_names, file_names in os.walk(root, followlinks=False):
        base = Path(directory)
        for name in [*directory_names, *file_names]:
            path = base / name
            relative_path = path.relative_to(root).as_posix()
            if path.is_symlink() or not (path.is_dir() or path.is_file()):
                raise StaticArtifactError(
                    f"{relative_path} is not a regular file or directory"
                )
        for name in file_names:
            path = base / name
            relative_path = path.relative_to(root).as_posix()
            check_public_path(relative_path)
            data = path.read_bytes()
            if len(data) > limits["max_file_bytes"]:
                raise StaticArtifactError(
                    f"{relative_path} is {len(data)} bytes, which exceeds the "
                    f"{limits['max_file_bytes']}-byte file ceiling"
                )
            inventory.append(
                {"path": relative_path, "bytes": len(data), "sha256": _sha256(data)}
            )
    inventory.sort(key=lambda entry: str(entry["path"]).encode())
    total = sum(int(str(entry["bytes"])) for entry in inventory)
    if total > limits["max_total_bytes"]:
        raise StaticArtifactError(
            f"artifact total of {total} bytes exceeds the "
            f"{limits['max_total_bytes']}-byte ceiling"
        )
    return inventory, total, _inventory_digest(inventory)


def check_public_tree(root: Path, limits: Mapping[str, int] = DEFAULT_LIMITS) -> str:
    """Validate a staged public tree and return its inventory digest."""
    return _inventory_of(root, limits)[2]


def _check_content_syntax(root: Path, inventory: list[dict[str, object]]) -> None:
    """Refuse public JSON and XML that does not parse."""
    for entry in inventory:
        relative_path = str(entry["path"])
        suffix = Path(relative_path).suffix
        if suffix not in {".json", ".webmanifest", ".xml"}:
            continue
        data = root.joinpath(*relative_path.split("/")).read_bytes()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            raise StaticArtifactError(f"{relative_path} is not valid UTF-8") from None
        if suffix == ".xml":
            try:
                ET.fromstring(data)
            except ET.ParseError as error:
                raise StaticArtifactError(
                    f"{relative_path} is not well-formed XML: {error}"
                ) from None
        else:
            try:
                json.loads(text)
            except ValueError as error:
                raise StaticArtifactError(
                    f"{relative_path} is not valid JSON: {error}"
                ) from None


def _fsync_directory(directory: Path) -> None:
    descriptor = os.open(directory, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _write_durable(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    try:
        view = memoryview(data)
        while view:
            view = view[os.write(descriptor, view) :]
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _write_atomic(path: Path, data: bytes) -> None:
    temporary = path.with_name(f".{path.name}.tmp-{os.getpid()}-{secrets.token_hex(4)}")
    _write_durable(temporary, data)
    os.replace(temporary, path)
    _fsync_directory(path.parent)


def _resolve_revision(git: Git, revision: str) -> None:
    if not FULL_COMMIT_ID.match(revision):
        raise StaticArtifactError(
            f"revision must be a full commit id, got {revision!r}"
        )
    resolved = git.try_run("rev-parse", "--verify", "--quiet", f"{revision}^{{commit}}")
    if resolved is None or resolved.strip() != revision:
        raise StaticArtifactError(f"{revision} is not a commit in {git.source}")


def _read_tree(git: Git, revision: str) -> list[TreeEntry]:
    entries = []
    for record in git.run("ls-tree", "-r", "-z", "--full-tree", revision).split("\0"):
        if not record:
            continue
        header, path = record.split("\t", 1)
        mode, kind, oid = header.split(" ")
        entries.append(TreeEntry(mode=mode, kind=kind, oid=oid, path=path))
    return entries


def _read_pinned_bytes(
    *,
    git: Git,
    source: Path,
    revision: str,
    object_format: str,
    entries: list[TreeEntry],
) -> list[tuple[str, bytes]]:
    index_output = git.run(
        "diff-index", "--cached", "-z", "--name-only", revision, "--"
    )
    index_differs = set(filter(None, index_output.split("\0")))
    files = []
    for entry in entries:
        if entry.mode == "120000":
            raise StaticArtifactError(
                f"{entry.path} is a symlink at the pinned revision; "
                "symlinks are refused"
            )
        if entry.kind != "blob" or entry.mode not in {"100644", "100755"}:
            raise StaticArtifactError(
                f"{entry.path} has unsupported mode {entry.mode} at the pinned revision"
            )
        if entry.path in index_differs:
            raise StaticArtifactError(
                f"{entry.path}: index differs from pinned revision {revision}"
            )
        path = source.joinpath(*entry.path.split("/"))
        if not path.exists() and not path.is_symlink():
            raise StaticArtifactError(
                f"{entry.path} is tracked at {revision} "
                "but missing from the source tree"
            )
        if path.is_symlink() or not path.is_file():
            raise StaticArtifactError(
                f"{entry.path} is not a regular file on disk; symlinks are refused"
            )
        data = path.read_bytes()
        if _git_blob_id(object_format, data) != entry.oid:
            raise StaticArtifactError(
                f"{entry.path} differs from pinned revision {revision} on disk"
            )
        files.append((entry.path, data))
    return files


def _select_packager_inputs(entries: list[TreeEntry], revision: str) -> list[TreeEntry]:
    selected = [
        entry
        for entry in entries
        if entry.path in SNAPSHOT_FILES
        or DATED_REPORT.match(entry.path)
        or entry.path.startswith(SNAPSHOT_PREFIXES)
    ]
    present = {entry.path for entry in selected}
    for required in REQUIRED_INPUTS:
        if required not in present:
            raise StaticArtifactError(f"{required} is required at revision {revision}")
    return sorted(selected, key=lambda entry: entry.path.encode())


def _stage_artifact(
    *,
    git: Git,
    source: Path,
    revision: str,
    object_format: str,
    stage: Path,
    commands: list[dict[str, object]],
) -> dict[str, object]:
    inputs = _select_packager_inputs(_read_tree(git, revision), revision)
    files = _read_pinned_bytes(
        git=git,
        source=source,
        revision=revision,
        object_format=object_format,
        entries=inputs,
    )
    snapshot = stage / "source"
    for relative_path, data in files:
        _write_durable(snapshot.joinpath(*relative_path.split("/")), data)
    environment = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}

    # The repository's report validation gate, before the packager renders it.
    argv = [
        sys.executable,
        "-B",
        str(snapshot / "scripts" / "validate_report.py"),
        str(snapshot / "index.md"),
    ]
    completed = subprocess.run(
        argv, cwd=snapshot, env=environment, capture_output=True, text=True, check=False
    )
    commands.append({"argv": argv, "exit_status": completed.returncode})
    if completed.returncode != 0:
        detail = (completed.stdout or completed.stderr).strip().splitlines()[-5:]
        raise StaticArtifactError(
            f"report validation {argv[2]} failed with exit status "
            f"{completed.returncode}: {' | '.join(detail)}"
        )

    argv = [
        sys.executable,
        "-B",
        str(snapshot / PACKAGER),
        "--root",
        str(snapshot),
        "--output",
        str(stage / "artifact"),
    ]
    completed = subprocess.run(
        argv,
        cwd=snapshot,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    commands.append({"argv": argv, "exit_status": completed.returncode})
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout).strip().splitlines()[-5:]
        raise StaticArtifactError(
            f"packager {snapshot / PACKAGER} failed with exit status "
            f"{completed.returncode}: {' | '.join(detail)}"
        )
    shutil.rmtree(snapshot)
    return {
        "packager": PACKAGER,
        "packager_inputs": [
            {"path": relative_path, "sha256": _sha256(data)}
            for relative_path, data in files
        ],
    }


def _check_staged_artifact(
    *, git: Git, revision: str, stage: Path, commands: list[dict[str, object]]
) -> None:
    """Site validation of the staged artifact; the packager already validated it."""


def _assert_deploy_layout(
    deploy_dir: Path, expected_digest: str, limits: Mapping[str, int]
) -> str:
    output = deploy_dir / ".vercel" / "output"
    if [path.name for path in deploy_dir.iterdir()] != [".vercel"] or [
        path.name for path in (deploy_dir / ".vercel").iterdir()
    ] != ["output"]:
        raise StaticArtifactError("deploy layout must contain only .vercel/output")
    if sorted(path.name for path in output.iterdir()) != ["config.json", "static"]:
        raise StaticArtifactError(
            "deploy layout output must contain only config.json and static/"
        )
    if json.loads((output / "config.json").read_text()) != DEPLOY_CONFIG:
        raise StaticArtifactError(
            "deploy config must carry only the Build Output API version, "
            "with no routes, headers, redirects or identifiers"
        )
    static_digest = _inventory_of(output / "static", limits)[2]
    if static_digest != expected_digest:
        raise StaticArtifactError("deploy layout static files differ from the artifact")
    return static_digest


def _write_deploy_layout(artifact_dir: Path, deploy_dir: Path) -> None:
    output = deploy_dir / ".vercel" / "output"
    for path in sorted(artifact_dir.rglob("*")):
        if path.is_file():
            target = output / "static" / path.relative_to(artifact_dir)
            _write_durable(target, path.read_bytes())
    _write_durable(output / "config.json", (json.dumps(DEPLOY_CONFIG) + "\n").encode())


def _acquire_lock(store: Path) -> Callable[[], None]:
    lock_path = store / LOCK
    try:
        descriptor = os.open(lock_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    except FileExistsError:
        try:
            holder = json.loads(lock_path.read_text())
        except (OSError, ValueError):
            holder = {}
        pid = holder.get("pid")
        running = holder.get("hostname") != socket.gethostname()
        if not running and isinstance(pid, int):
            try:
                os.kill(pid, 0)
                running = True
            except ProcessLookupError:
                running = False
            except PermissionError:
                running = True
        state = (
            f"running on {holder.get('hostname', 'an unknown host')}; "
            "builds of one store are serialized"
            if running
            else "not running; a previous build was interrupted. Confirm no builder "
            f"is active, then remove {lock_path}"
        )
        raise StaticArtifactError(
            f"output store {store} is locked by pid {pid} ({state})"
        ) from None
    try:
        record = {
            "pid": os.getpid(),
            "hostname": socket.gethostname(),
            "started_at": _now(),
        }
        os.write(descriptor, (json.dumps(record) + "\n").encode())
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    return lambda: lock_path.unlink(missing_ok=True)


def _remove_interrupted_staging(store: Path) -> None:
    for path in store.iterdir():
        if path.name.startswith(STAGING_PREFIX):
            shutil.rmtree(path)
        elif path.name.startswith(f".{POINTER}.tmp-"):
            path.unlink()


def _now() -> str:
    moment = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
    return moment.replace("+00:00", "Z")


def read_current_build(store: Path, *, verify: bool = False) -> CurrentBuild:
    """Return the accepted build named by the store pointer."""
    pointer_path = store / POINTER
    pointer = json.loads(pointer_path.read_text())
    if (
        pointer.get("site") != SITE
        or pointer.get("build") != f"builds/{pointer.get('inventory_digest')}"
    ):
        raise StaticArtifactError(f"{pointer_path} does not describe a {SITE} build")
    build_dir = store / pointer["build"]
    current = CurrentBuild(
        site=pointer["site"],
        source_revision=pointer["source_revision"],
        inventory_digest=pointer["inventory_digest"],
        file_count=pointer["file_count"],
        total_bytes=pointer["total_bytes"],
        build_dir=pointer["build"],
        artifact_dir=build_dir / "artifact",
        deploy_dir=build_dir / "deploy",
    )
    if verify and check_public_tree(current.artifact_dir) != current.inventory_digest:
        raise StaticArtifactError(
            f"{current.artifact_dir} no longer matches {current.inventory_digest}"
        )
    return current


def build_static_artifact(
    *,
    revision: str,
    output: Path,
    receipts: Path,
    source: Path = Path(__file__).resolve().parents[1],
    limits: Mapping[str, int] = DEFAULT_LIMITS,
    hooks: Hooks | None = None,
    invocation: list[str] | None = None,
) -> BuildResult:
    """Build, verify and promote the artifact for one pinned revision."""
    started_at = _now()
    hooks = hooks or {}
    source_root = Path(os.path.realpath(source))
    store = Path(os.path.realpath(output))
    receipts_root = Path(os.path.realpath(receipts))
    if store == Path(store.anchor):
        raise StaticArtifactError("output store must not be the filesystem root")
    if _is_within(store, source_root):
        raise StaticArtifactError(f"output store {store} is inside the source tree")
    if _is_within(receipts_root, store):
        raise StaticArtifactError(
            f"receipts directory {receipts_root} is inside the output store"
        )
    if _is_within(receipts_root, source_root):
        raise StaticArtifactError(
            f"receipts directory {receipts_root} is inside the source tree"
        )

    commands: list[dict[str, object]] = []
    git = Git(source_root, commands)
    if Path(os.path.realpath(git.run("rev-parse", "--show-toplevel").strip())) != (
        source_root
    ):
        raise StaticArtifactError(f"source {source_root} must be the repository root")
    object_format = git.run("rev-parse", "--show-object-format").strip()
    _resolve_revision(git, revision)
    source_head = git.run("rev-parse", "HEAD").strip()

    store.mkdir(parents=True, exist_ok=True)
    release_lock = _acquire_lock(store)
    stage: Path | None = None
    try:
        _remove_interrupted_staging(store)
        stage = Path(
            os.path.realpath(
                store / f"{STAGING_PREFIX}{os.getpid()}-{secrets.token_hex(4)}"
            )
        )
        stage.mkdir()
        details = _stage_artifact(
            git=git,
            source=source_root,
            revision=revision,
            object_format=object_format,
            stage=stage,
            commands=commands,
        )
        if sorted(path.name for path in stage.iterdir()) != ["artifact"]:
            raise StaticArtifactError("packager left unexpected files in the stage")
        inventory, total_bytes, digest = _inventory_of(stage / "artifact", limits)
        _check_content_syntax(stage / "artifact", inventory)
        _check_staged_artifact(
            git=git, revision=revision, stage=stage, commands=commands
        )
        _write_deploy_layout(stage / "artifact", stage / "deploy")
        static_digest = _assert_deploy_layout(stage / "deploy", digest, limits)
        build_relative = f"builds/{digest}"
        build_dir = store / "builds" / digest

        if "before_promote" in hooks:
            hooks["before_promote"]()
        build_dir.parent.mkdir(parents=True, exist_ok=True)
        reused_existing_build = build_dir.exists()
        if reused_existing_build:
            if (
                _inventory_of(build_dir / "artifact", limits)[2] != digest
                or _assert_deploy_layout(build_dir / "deploy", digest, limits)
                != static_digest
            ):
                raise StaticArtifactError(
                    f"{build_dir} exists but does not match its digest; "
                    "refusing to overwrite an accepted build"
                )
            shutil.rmtree(stage)
        else:
            os.rename(stage, build_dir)
            _fsync_directory(build_dir.parent)
        stage = None

        pointer_path = store / POINTER
        previous_pointer = pointer_path.read_bytes() if pointer_path.exists() else None
        pointer = {
            "schema": "static-artifact-pointer/v1",
            "site": SITE,
            "source_revision": revision,
            "inventory_digest": digest,
            "build": build_relative,
            "file_count": len(inventory),
            "total_bytes": total_bytes,
        }
        if "before_pointer_swap" in hooks:
            hooks["before_pointer_swap"]()
        _write_atomic(pointer_path, (json.dumps(pointer, indent=2) + "\n").encode())

        finished_at = _now()
        receipt = {
            "schema": "static-artifact-receipt/v1",
            "site": SITE,
            "result": "success",
            "source_revision": revision,
            "source_head": source_head,
            "object_format": object_format,
            "inventory_digest": digest,
            "inventory_digest_format": (
                'sha256 over "<sha256> <bytes> <path>\\n" lines sorted by path'
            ),
            "file_count": len(inventory),
            "total_bytes": total_bytes,
            "inventory": inventory,
            **details,
            "deploy_layout": {
                "path": f"{build_relative}/deploy/.vercel/output",
                "config": DEPLOY_CONFIG,
                "static_inventory_digest": static_digest,
            },
            "output_store": str(store),
            "build": build_relative,
            "reused_existing_build": reused_existing_build,
            "limits": dict(limits),
            "builder": {
                "path": "scripts/build_static_artifact.py",
                "sha256": _sha256(Path(__file__).read_bytes()),
                "python": sys.version.split()[0],
            },
            "invocation": invocation,
            "commands": commands,
            "started_at": started_at,
            "finished_at": finished_at,
        }
        stamp = re.sub(r"[-:.]", "", finished_at)
        receipt_path = receipts_root / (
            f"{SITE.lower()}-{stamp}-{digest[:12]}-{secrets.token_hex(3)}.json"
        )
        try:
            receipts_root.mkdir(parents=True, exist_ok=True)
            _write_atomic(receipt_path, (json.dumps(receipt, indent=2) + "\n").encode())
        except BaseException:
            if previous_pointer is None:
                pointer_path.unlink(missing_ok=True)
            else:
                _write_atomic(pointer_path, previous_pointer)
            raise

        return BuildResult(
            site=SITE,
            source_revision=revision,
            inventory_digest=digest,
            file_count=len(inventory),
            total_bytes=total_bytes,
            build_dir=build_relative,
            artifact_dir=build_dir / "artifact",
            deploy_dir=build_dir / "deploy",
            receipt_path=receipt_path,
            reused_existing_build=reused_existing_build,
        )
    finally:
        if stage is not None:
            shutil.rmtree(stage, ignore_errors=True)
        release_lock()


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the static artifact.")
    parser.add_argument(
        "--source", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument("--revision", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--receipts", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = build_static_artifact(
            source=args.source,
            revision=args.revision,
            output=args.output,
            receipts=args.receipts,
            invocation=[sys.executable, *sys.argv],
        )
    except StaticArtifactError as error:
        print(f"static artifact build failed: {error}", file=sys.stderr)
        return 1
    summary = {
        "site": result.site,
        "source_revision": result.source_revision,
        "inventory_digest": result.inventory_digest,
        "file_count": result.file_count,
        "total_bytes": result.total_bytes,
        "build": result.build_dir,
        "reused_existing_build": result.reused_existing_build,
        "receipt": str(result.receipt_path),
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
