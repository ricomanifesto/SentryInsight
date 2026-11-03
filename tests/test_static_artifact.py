import hashlib
import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from collections.abc import Iterator
from pathlib import Path

import pytest

from scripts.build_static_artifact import (
    DEPLOY_CONFIG,
    StaticArtifactError,
    build_static_artifact,
    check_public_tree,
    read_current_build,
)
from scripts.package_pages import EXPECTED_TOP_LEVEL, package_pages

ROOT = Path(__file__).resolve().parents[1]
PACKAGER_INPUTS = (
    "index.md",
    "reports",
    "site",
    "assets",
    "contracts",
    "scripts",
    "src",
)
GIT_ENV = {
    **os.environ,
    "GIT_CONFIG_GLOBAL": os.devnull,
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_AUTHOR_NAME": "Fixture",
    "GIT_AUTHOR_EMAIL": "fixture@example.invalid",
    "GIT_COMMITTER_NAME": "Fixture",
    "GIT_COMMITTER_EMAIL": "fixture@example.invalid",
}


def _git(cwd: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        env=GIT_ENV,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def _clone_packager_inputs(target: Path) -> None:
    _git(
        ROOT,
        "clone",
        "--quiet",
        "--shared",
        "--no-checkout",
        str(ROOT),
        str(target),
    )
    _git(target, "checkout", "--quiet", "HEAD", "--", *PACKAGER_INPUTS)


class Fixture:
    def __init__(self, workspace: Path, template: Path) -> None:
        self.workspace = workspace
        self.source = workspace / "source"
        self.output = workspace / "store"
        self.receipts = workspace / "receipts"
        shutil.copytree(template, self.source, symlinks=True)
        self.revision = _git(self.source, "rev-parse", "HEAD")

    def build(self, **overrides):
        options = {
            "source": self.source,
            "revision": self.revision,
            "output": self.output,
            "receipts": self.receipts,
            **overrides,
        }
        return build_static_artifact(**options)

    def commit(self, message: str, *paths: str) -> str:
        _git(self.source, "add", "--force", "--", *paths)
        _git(self.source, "commit", "--quiet", "--no-gpg-sign", "-m", message)
        return _git(self.source, "rev-parse", "HEAD")

    def revise_template(self, comment: str) -> str:
        stylesheet = self.source / "site" / "site.css"
        stylesheet.write_text(stylesheet.read_text() + f"\n{comment}\n")
        return self.commit(comment, "site/site.css")

    def newest_report(self) -> Path:
        return sorted((self.source / "reports").glob("????-??-??.md"))[-1]


@pytest.fixture(scope="module")
def template() -> Iterator[Path]:
    with tempfile.TemporaryDirectory(prefix="insight-artifact-template-") as temp_dir:
        source = Path(temp_dir) / "source"
        _clone_packager_inputs(source)
        yield source


@pytest.fixture
def fixture(template: Path) -> Iterator[Fixture]:
    with tempfile.TemporaryDirectory(prefix="insight-artifact-") as temp_dir:
        yield Fixture(Path(temp_dir), template)


def _current_digest(fixture: Fixture) -> str:
    return read_current_build(fixture.output).inventory_digest


def _snapshot(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def test_artifact_equals_the_existing_pages_package(fixture):
    result = fixture.build()
    baseline = fixture.workspace / "baseline"
    package_pages(repo_root=fixture.source, output_path=baseline)

    assert {path.name for path in result.artifact_dir.iterdir()} == EXPECTED_TOP_LEVEL
    assert _snapshot(result.artifact_dir) == _snapshot(baseline)
    assert _current_digest(fixture) == result.inventory_digest
    assert not (fixture.output / ".lock").exists()
    assert sorted(path.name for path in fixture.output.iterdir()) == [
        "builds",
        "current.json",
    ]


def test_rebuild_into_another_store_is_byte_identical(fixture):
    first = fixture.build()
    second = fixture.build(output=fixture.workspace / "second-store")
    repeat = fixture.build()

    assert len(first.inventory_digest) == 64
    assert second.inventory_digest == first.inventory_digest
    assert _snapshot(second.artifact_dir) == _snapshot(first.artifact_dir)
    assert _snapshot(second.deploy_dir) == _snapshot(first.deploy_dir)
    assert repeat.reused_existing_build is True
    assert repeat.build_dir == first.build_dir


def test_deploy_layout_carries_only_version_and_artifact_bytes(fixture):
    result = fixture.build()
    output_dir = result.deploy_dir / ".vercel" / "output"

    assert DEPLOY_CONFIG == {"version": 3}
    assert sorted(path.name for path in result.deploy_dir.iterdir()) == [".vercel"]
    assert sorted(path.name for path in output_dir.iterdir()) == [
        "config.json",
        "static",
    ]
    assert json.loads((output_dir / "config.json").read_text()) == {"version": 3}
    assert _snapshot(output_dir / "static") == _snapshot(result.artifact_dir)


def test_receipt_binds_site_revision_inventory_and_packager_command(fixture):
    result = fixture.build()
    receipt = json.loads(result.receipt_path.read_text())

    assert result.receipt_path.parent == fixture.receipts.resolve()
    assert receipt["site"] == "SentryInsight"
    assert receipt["source_revision"] == fixture.revision
    assert receipt["inventory_digest"] == result.inventory_digest
    assert receipt["file_count"] == result.file_count
    assert receipt["total_bytes"] == result.total_bytes
    lines = "".join(
        f"{entry['sha256']} {entry['bytes']} {entry['path']}\n"
        for entry in receipt["inventory"]
    )
    assert hashlib.sha256(lines.encode()).hexdigest() == result.inventory_digest
    assert receipt["inventory"] == sorted(
        receipt["inventory"], key=lambda entry: entry["path"].encode()
    )
    for entry in receipt["inventory"]:
        content = (result.artifact_dir / entry["path"]).read_bytes()
        assert entry["sha256"] == hashlib.sha256(content).hexdigest()
    assert receipt["deploy_layout"]["config"] == {"version": 3}
    deploy_layout = receipt["deploy_layout"]
    assert deploy_layout["static_inventory_digest"] == result.inventory_digest
    assert any(
        "scripts/package_pages.py" in " ".join(command["argv"])
        for command in receipt["commands"]
    )
    assert all(command["exit_status"] == 0 for command in receipt["commands"])
    names = [path.name for path in result.artifact_dir.rglob("*")]
    assert not [name for name in names if "receipt" in name]


def test_untracked_and_private_files_never_enter_the_artifact(fixture):
    baseline = fixture.workspace / "baseline"
    package_pages(repo_root=fixture.source, output_path=baseline)
    report = fixture.newest_report()
    planted = {
        ".env": "TOKEN=private\n",
        "AGENTS.md": "private\n",
        "test-results/x.html": "<p>private</p>\n",
        "build-receipt.json": '{"inventory_digest": "0"}\n',
        "reports/2099-01-01.md": report.read_text(),
    }
    for relative_path, content in planted.items():
        target = fixture.source / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
    (fixture.source / "assets" / "linked.png").symlink_to("logo.png")

    result = fixture.build()

    assert _snapshot(result.artifact_dir) == _snapshot(baseline)
    names = {path.name for path in result.artifact_dir.rglob("*")}
    assert not names & {".env", "AGENTS.md", "x.html", "build-receipt.json"}
    assert "2099-01-01.html" not in names
    assert "linked.png" not in names


def test_input_drift_fails_and_keeps_the_last_good_build(fixture):
    accepted = fixture.build()
    before = _snapshot(fixture.output)
    report = fixture.newest_report()
    report.write_text(report.read_text() + "\nLocal edit.\n")

    with pytest.raises(
        StaticArtifactError, match=rf"{report.name}.*differs from pinned"
    ):
        fixture.build()
    assert _snapshot(fixture.output) == before
    assert _current_digest(fixture) == accepted.inventory_digest


def test_staged_input_change_fails_even_when_the_worktree_matches(fixture):
    original = (fixture.source / "index.md").read_text()
    (fixture.source / "index.md").write_text(original + "\nStaged.\n")
    _git(fixture.source, "add", "index.md")
    (fixture.source / "index.md").write_text(original)

    with pytest.raises(StaticArtifactError, match=r"index\.md.*index differs"):
        fixture.build()


def test_missing_input_fails_and_keeps_the_last_good_build(fixture):
    fixture.build()
    before = _snapshot(fixture.output)
    (fixture.source / "site" / "report.html").unlink()

    with pytest.raises(StaticArtifactError, match=r"site/report\.html.*missing"):
        fixture.build()
    assert _snapshot(fixture.output) == before


def test_tracked_symlink_input_is_refused(fixture):
    link = fixture.source / "reports" / "2099-01-01.md"
    link.symlink_to(fixture.newest_report().name)
    revision = fixture.commit("symlink report", "reports/2099-01-01.md")

    with pytest.raises(StaticArtifactError, match=r"reports/2099-01-01\.md.*symlink"):
        fixture.build(revision=revision)


def test_packager_failure_on_malformed_report_keeps_the_last_good_build(fixture):
    accepted = fixture.build()
    before = _snapshot(fixture.output)
    (fixture.source / "reports" / "2099-01-01.md").write_text("not a report\n")
    revision = fixture.commit("malformed report", "reports/2099-01-01.md")

    with pytest.raises(StaticArtifactError, match=r"package_pages\.py.*exit status"):
        fixture.build(revision=revision)
    assert _snapshot(fixture.output) == before
    assert _current_digest(fixture) == accepted.inventory_digest
    assert not [path for path in fixture.output.iterdir() if path.name.startswith(".")]


@pytest.mark.parametrize("hook", ["before_promote", "before_pointer_swap"])
def test_promotion_failure_keeps_the_accepted_build(fixture, hook):
    accepted = fixture.build()
    before = _snapshot(fixture.output / accepted.build_dir)
    revision = fixture.revise_template("/* revised */")

    def interrupt() -> None:
        raise RuntimeError(f"injected {hook}")

    with pytest.raises(RuntimeError, match=f"injected {hook}"):
        fixture.build(revision=revision, hooks={hook: interrupt})
    assert _current_digest(fixture) == accepted.inventory_digest
    assert _snapshot(fixture.output / accepted.build_dir) == before
    assert not [path for path in fixture.output.iterdir() if path.name.startswith(".")]


def _child_build(fixture: Fixture, revision: str, hook: str, body: str):
    script = "\n".join(
        [
            "import os, signal, sys, time",
            "from pathlib import Path",
            f"sys.path.insert(0, {str(ROOT)!r})",
            "from scripts.build_static_artifact import build_static_artifact",
            "def hook():",
            *(f"    {line}" for line in body.splitlines()),
            "build_static_artifact(",
            f"    source=Path({str(fixture.source)!r}),",
            f"    revision={revision!r},",
            f"    output=Path({str(fixture.output)!r}),",
            f"    receipts=Path({str(fixture.receipts)!r}),",
            f"    hooks={{{hook!r}: hook}},",
            ")",
        ]
    )
    return subprocess.Popen([sys.executable, "-B", "-c", script], env=GIT_ENV)


def test_interrupted_promotion_blocks_until_the_stale_lock_is_cleared(fixture):
    accepted = fixture.build()
    before = _snapshot(fixture.output / accepted.build_dir)
    revision = fixture.revise_template("/* interrupted */")

    child = _child_build(
        fixture, revision, "before_pointer_swap", "os.kill(os.getpid(), signal.SIGKILL)"
    )
    assert child.wait(timeout=120) == -signal.SIGKILL
    assert _current_digest(fixture) == accepted.inventory_digest
    assert _snapshot(fixture.output / accepted.build_dir) == before
    with pytest.raises(
        StaticArtifactError, match=r"(?s)locked by pid \d+.*not running"
    ):
        fixture.build(revision=revision)

    (fixture.output / ".lock").unlink()
    recovered = fixture.build(revision=revision)
    assert recovered.inventory_digest != accepted.inventory_digest
    assert _current_digest(fixture) == recovered.inventory_digest
    assert not [p for p in fixture.output.iterdir() if p.name.startswith(".staging-")]


def test_second_writer_fails_while_the_first_holds_the_lock(fixture):
    paused = fixture.workspace / "paused"
    release = fixture.workspace / "release"
    child = _child_build(
        fixture,
        fixture.revision,
        "before_promote",
        f"Path({str(paused)!r}).touch()\n"
        f"while not Path({str(release)!r}).exists():\n"
        "    time.sleep(0.025)",
    )
    try:
        deadline = time.monotonic() + 120
        while not paused.exists():
            assert child.poll() is None
            assert time.monotonic() < deadline
            time.sleep(0.025)
        with pytest.raises(StaticArtifactError, match=r"locked by pid \d+"):
            fixture.build()
    finally:
        release.touch()
    assert child.wait(timeout=120) == 0
    assert _current_digest(fixture)


def test_public_tree_tripwire_refuses_private_and_unsafe_files(tmp_path):
    allowed = tmp_path / "allowed"
    (allowed / "reports").mkdir(parents=True)
    (allowed / ".nojekyll").write_text("")
    (allowed / "index.html").write_text("<p>ok</p>\n")
    check_public_tree(allowed)

    for relative_path in [
        ".env",
        "AGENTS.md",
        "reports/build-receipt.json",
        "reports/build.log",
        "reports/screenshot.png",
        "test-results/x.html",
        "reports/.hidden.html",
        "scripts/package_pages.py",
        "assets/site.css.map",
    ]:
        root = tmp_path / relative_path.replace("/", "_")
        target = root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("planted\n")
        pattern = relative_path.replace(".", r"\.")
        with pytest.raises(StaticArtifactError, match=pattern):
            check_public_tree(root)

    linked = tmp_path / "linked"
    linked.mkdir()
    (linked / "index.html").symlink_to(allowed / "index.html")
    with pytest.raises(StaticArtifactError, match=r"index\.html.*regular file"):
        check_public_tree(linked)


def test_size_ceiling_fails_explicitly(fixture):
    with pytest.raises(
        StaticArtifactError, match=r"exceeds the 1024-byte file ceiling"
    ):
        fixture.build(limits={"max_file_bytes": 1024, "max_total_bytes": 1 << 30})
    with pytest.raises(
        StaticArtifactError, match=r"total .* exceeds the 4096-byte ceiling"
    ):
        fixture.build(limits={"max_file_bytes": 1 << 30, "max_total_bytes": 4096})
    assert not (fixture.output / "current.json").exists()


def test_unsafe_outputs_and_revisions_are_refused(fixture):
    with pytest.raises(StaticArtifactError, match="inside the source tree"):
        fixture.build(output=fixture.source / "public")
    with pytest.raises(StaticArtifactError, match="inside the output store"):
        fixture.build(receipts=fixture.output / "receipts")
    with pytest.raises(StaticArtifactError, match="full commit id"):
        fixture.build(revision="HEAD")
    with pytest.raises(StaticArtifactError, match="not a commit"):
        fixture.build(revision="0" * 40)


@pytest.mark.parametrize(
    ("relative_path", "change", "expected"),
    [
        (
            "contracts/reporting-identity-v1.json",
            lambda text: text[:-8],
            r"contracts/reporting-identity-v1\.json is not valid JSON",
        ),
        (
            "index.md",
            lambda text: text + "\nSee [details](javascript:alert(1)).\n",
            r"(?s)report validation .*validate_report\.py.*exit status",
        ),
    ],
)
def test_invalid_committed_content_fails_and_keeps_the_accepted_build(
    fixture, relative_path, change, expected
):
    accepted = fixture.build()
    before = _snapshot(fixture.output)
    target = fixture.source / relative_path
    target.write_text(change(target.read_text()))
    revision = fixture.commit(f"invalid {relative_path}", relative_path)

    with pytest.raises(StaticArtifactError, match=expected):
        fixture.build(revision=revision)
    assert _snapshot(fixture.output) == before
    assert _current_digest(fixture) == accepted.inventory_digest


def test_report_validation_runs_before_packaging(fixture):
    receipt = json.loads(fixture.build().receipt_path.read_text())
    commands = [" ".join(command["argv"]) for command in receipt["commands"]]

    validation = [i for i, cmd in enumerate(commands) if "validate_report.py" in cmd]
    packaging = [i for i, cmd in enumerate(commands) if "package_pages.py" in cmd]
    assert validation and packaging
    assert validation[0] < packaging[0]
