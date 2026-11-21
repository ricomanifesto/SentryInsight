"""One closed, deterministic defensive package and its approval triple.

The package is rendered only from pinned inputs read as committed blobs at
one exact revision: the owner-reviewed fact manifest, the page templates, the
static assets and the public identity contract. It is staged in a clean
temporary tree from generated Markdown; the legacy root report, rendered pages
and dated archives are never listed, read or copied, even when present.

Approval is the triple (exact head, canonical committed facts SHA-256,
complete sorted inventory SHA-256). The inventory digest is the publication
kit's (publication/kit/canonical.js inventoryDigest): SHA-256 over sorted
"<sha256>  <path>" lines, so the Node publisher verifies the same bytes.
Without an approval the local $0 path builds and reports the proposed triple
and nothing else; with one, any difference refuses before output exists.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import os
from pathlib import Path
import re
import subprocess
import tempfile

from .paid_readiness import (
    MANIFEST_PATH,
    ReadinessRefusal,
    check_candidate_links,
    load_fact_manifest,
    render_report,
)

APPROVAL_SCHEMA = "sentryinsight/defensive-package-approval/v1"
TEMPLATE_FILES = (
    "site/archive.html",
    "site/report.html",
    "site/report.js",
    "site/site.css",
    "site/theme-bootstrap.js",
    "site/vendor/DOMPURIFY-LICENSE.txt",
    "site/vendor/dompurify.min.js",
)
CONTRACT_FILES = ("contracts/reporting-identity-v1.json",)
# The archive index the site builder always writes; never a dated report.
GENERATED_REPORT_FILES = frozenset({"index.html", "index.json"})
# Every rendered path besides the copied contract and static assets.
GENERATED_FILES = frozenset(
    {
        ".nojekyll",
        "assets/report.js",
        "assets/site.css",
        "assets/vendor/DOMPURIFY-LICENSE.txt",
        "assets/vendor/dompurify.min.js",
        "current-findings.json",
        "index.html",
        "index.md",
        "reports/index.html",
        "reports/index.json",
        "sitemap.xml",
    }
)
# Control characters (newline included) and backslashes never name a path.
_UNSAFE_NAME = re.compile(r"[\x00-\x1f\x7f\\]")
_REVISION = re.compile(r"[0-9a-f]{40}")
_HEX64 = re.compile(r"[0-9a-f]{64}")
_INSTANT = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")


class DefensivePackageError(RuntimeError):
    """A categorical refusal; the message is a fixed code, never content."""


@dataclass(frozen=True)
class Approval:
    head: str
    facts_sha256: str
    package_sha256: str

    def __post_init__(self) -> None:
        if not (
            _REVISION.fullmatch(self.head)
            and _HEX64.fullmatch(self.facts_sha256)
            and _HEX64.fullmatch(self.package_sha256)
        ):
            raise DefensivePackageError("approval_malformed")


@dataclass(frozen=True)
class PackageResult:
    head: str
    facts_sha256: str
    package_sha256: str
    file_count: int
    generated_at: str

    def proposal(self) -> dict:
        return {
            "schema": APPROVAL_SCHEMA,
            "head": self.head,
            "facts_sha256": self.facts_sha256,
            "package_sha256": self.package_sha256,
            "file_count": self.file_count,
            "generated_at": self.generated_at,
        }


def _asset_files() -> tuple[str, ...]:
    from scripts.package_pages import STATIC_ASSETS

    return tuple(f"assets/{name}" for name in STATIC_ASSETS)


def pinned_inputs() -> tuple[str, ...]:
    """Every path the package reads, all as blobs at the pinned revision."""
    return (MANIFEST_PATH, *TEMPLATE_FILES, *_asset_files(), *CONTRACT_FILES)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def closed_inventory() -> frozenset[str]:
    """Exactly the paths the packager generates; nothing else may appear."""
    return frozenset({*GENERATED_FILES, *CONTRACT_FILES, *_asset_files()})


def _check_name(relative: str) -> None:
    try:
        relative.encode("utf-8")
    except UnicodeEncodeError:
        raise DefensivePackageError("unsafe_path_name") from None
    if _UNSAFE_NAME.search(relative) or any(
        segment in {"", ".", ".."} for segment in relative.split("/")
    ):
        raise DefensivePackageError("unsafe_path_name")


def package_paths(root: Path) -> list[str]:
    """Names first, before any byte is read: safe, regular and closed."""
    paths = []
    for directory, directories, files in os.walk(root, followlinks=False):
        base = Path(directory)
        for name in [*directories, *files]:
            path = base / name
            _check_name(path.relative_to(root).as_posix())
            if path.is_symlink() or not (path.is_dir() or path.is_file()):
                raise DefensivePackageError("package_entry_not_regular")
        paths.extend((base / name).relative_to(root).as_posix() for name in files)
    if set(paths) != closed_inventory():
        raise DefensivePackageError("package_inventory_not_closed")
    return sorted(paths, key=str.encode)


def inventory_digest(root: Path) -> tuple[str, int]:
    """canonical.js inventoryDigest over the closed, name-checked inventory."""
    paths = package_paths(root)
    lines = "".join(
        f"{_sha256(root.joinpath(*relative.split('/')).read_bytes())}  {relative}\n"
        for relative in paths
    )
    return _sha256(lines.encode()), len(paths)


def verify_package(package: Path, package_sha256: str) -> str:
    """Recompute the inventory immediately before any upload or publish."""
    if not _HEX64.fullmatch(package_sha256):
        raise DefensivePackageError("approval_malformed")
    if package.is_symlink() or not package.is_dir():
        raise DefensivePackageError("package_missing")
    digest, _ = inventory_digest(package)
    if digest != package_sha256:
        raise DefensivePackageError("package_digest_mismatch")
    return digest


def _git(source: Path, *arguments: str, data: bytes | None = None) -> bytes:
    env = {key: os.environ[key] for key in ("PATH", "HOME") if key in os.environ}
    completed = subprocess.run(
        ["git", *arguments],
        cwd=source,
        env=env,
        input=data,
        capture_output=True,
        check=False,
        timeout=60,
    )
    if completed.returncode != 0:
        raise DefensivePackageError("git_unavailable")
    return completed.stdout


def _pinned_blobs(source: Path, revision: str, paths: tuple[str, ...]) -> dict:
    """Name exactly these paths; no other tree entry is listed or opened."""
    listing = _git(source, "ls-tree", "-z", "--full-tree", revision, "--", *paths)
    entries = {}
    for record in filter(None, listing.decode().split("\0")):
        header, path = record.split("\t", 1)
        mode, kind, oid = header.split(" ")
        if mode == "120000":
            raise DefensivePackageError("pinned_input_symlink")
        if kind != "blob" or mode not in {"100644", "100755"}:
            raise DefensivePackageError("pinned_input_not_regular")
        entries[path] = oid
    if MANIFEST_PATH not in entries:
        raise DefensivePackageError("facts_unavailable")
    if set(entries) != set(paths):
        raise DefensivePackageError("pinned_input_missing")
    oids = [entries[path] for path in paths]
    output = _git(
        source, "cat-file", "--batch", data="".join(f"{o}\n" for o in oids).encode()
    )
    blobs, offset = {}, 0
    for path, oid in zip(paths, oids, strict=True):
        newline = output.index(b"\n", offset)
        header_oid, kind, size = output[offset:newline].decode().split(" ")
        if header_oid != oid or kind != "blob":
            raise DefensivePackageError("pinned_input_not_regular")
        start = newline + 1
        blobs[path] = output[start : start + int(size)]
        offset = start + int(size) + 1
    return blobs


def _moment(source: Path, revision: str, generated_at: str | None) -> datetime:
    """An explicitly pinned instant, or the pinned commit's committer time."""
    if generated_at is not None:
        if not _INSTANT.fullmatch(generated_at):
            raise DefensivePackageError("generated_at_malformed")
        return datetime.fromisoformat(generated_at.replace("Z", "+00:00"))
    seconds = _git(source, "log", "-1", "--format=%ct", revision).decode().strip()
    if not seconds.isdigit():
        raise DefensivePackageError("git_unavailable")
    return datetime.fromtimestamp(int(seconds), tz=timezone.utc)


def _stage(stage: Path, blobs: dict, manifest, moment: datetime) -> None:
    from scripts.build_site import build_site
    from scripts.package_pages import _validate_package

    snapshot = stage.parent / "inputs"
    for path in (*TEMPLATE_FILES, *_asset_files(), *CONTRACT_FILES):
        target = snapshot.joinpath(*path.split("/"))
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(blobs[path])
    stage.mkdir()
    (stage / "reports").mkdir()
    (stage / "index.md").write_text(render_report(manifest, moment).source)
    build_site(
        report_path=stage / "index.md",
        output_path=stage,
        template_path=snapshot / "site",
    )
    # Rendered output only; the contract and static assets are repository code.
    check_candidate_links(stage, manifest)
    for path in (*CONTRACT_FILES, *_asset_files()):
        target = stage.joinpath(*path.split("/"))
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(blobs[path])
    (stage / ".nojekyll").write_text("")
    _validate_package(stage)
    from scripts.build_static_artifact import StaticArtifactError, check_public_tree

    try:
        # The existing public-path policy: no dot, private or implementation path.
        check_public_tree(stage)
    except StaticArtifactError:
        raise DefensivePackageError("package_public_path_invalid") from None
    if {child.name for child in (stage / "reports").iterdir()} - GENERATED_REPORT_FILES:
        raise DefensivePackageError("extra_report_file")


def build_package(
    *,
    source: Path,
    revision: str,
    output: Path,
    generated_at: str | None = None,
    approval: Approval | None = None,
) -> PackageResult:
    """Build the package for one revision; refuse before output on any drift."""
    if not _REVISION.fullmatch(revision):
        raise DefensivePackageError("revision_malformed")
    source = Path(os.path.realpath(source))
    resolved = _git(
        source, "rev-parse", "--verify", "--quiet", f"{revision}^{{commit}}"
    )
    if resolved.decode().strip() != revision:
        raise DefensivePackageError("revision_unavailable")
    if approval is not None and approval.head != revision:
        raise DefensivePackageError("approval_head_mismatch")
    if approval is not None:
        # An approved build runs only from a checkout at the approved head.
        checkout = _git(source, "rev-parse", "HEAD").decode().strip()
        if checkout != approval.head:
            raise DefensivePackageError("approval_checkout_mismatch")
    output = Path(os.path.abspath(output))
    parent = Path(os.path.realpath(output.parent))
    if (
        output.exists()
        or output.is_symlink()
        or not parent.is_dir()
        or parent == source
        or source in parent.parents
    ):
        raise DefensivePackageError("output_unsafe")
    blobs = _pinned_blobs(source, revision, pinned_inputs())
    facts = blobs[MANIFEST_PATH]
    facts_sha256 = _sha256(facts)
    if approval is not None and approval.facts_sha256 != facts_sha256:
        raise DefensivePackageError("approval_facts_mismatch")
    try:
        manifest = load_fact_manifest(facts, facts_sha256)
    except ReadinessRefusal:
        raise DefensivePackageError("facts_invalid") from None
    moment = _moment(source, revision, generated_at)
    with tempfile.TemporaryDirectory(prefix=".defensive-package-", dir=parent) as work:
        stage = Path(work) / "package"
        try:
            _stage(stage, blobs, manifest, moment)
        except ReadinessRefusal:
            raise DefensivePackageError("render_invalid") from None
        digest, count = inventory_digest(stage)
        if approval is not None and approval.package_sha256 != digest:
            raise DefensivePackageError("approval_package_mismatch")
        os.rename(stage, output)
    if approval is not None:
        verify_package(output, approval.package_sha256)
    instant = moment.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    return PackageResult(revision, facts_sha256, digest, count, instant)
