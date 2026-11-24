"""Offline Git fixtures for queued checkouts and report publication races."""

import os
from pathlib import Path
import shlex
import shutil
import subprocess

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
MAIN = "refs/heads/main"
CHECKOUT_REF = "${{ github.ref == 'refs/heads/main' && github.ref || github.sha }}"
REPORT_FILES = (
    "index.md",
    "index.html",
    "current-findings.json",
    "reports/index.html",
    ".sentryinsight-articles-fingerprint",
)


def _workflow():
    return yaml.load(
        (ROOT / ".github/workflows/generate-report.yml").read_text(),
        Loader=yaml.BaseLoader,
    )


def _step(name):
    return next(
        step
        for step in _workflow()["jobs"]["generate-report"]["steps"]
        if step.get("name") == name
    )


def _checkout_target(event_ref, event_sha):
    """Model checkout@v5's default event SHA and the allowed branch expression.

    This checks the workflow's input contract, not a replacement Actions runner.
    All subsequent checkout, rebase and push behavior uses real local Git.
    """
    configured = _step("Checkout code")["with"].get("ref")
    if configured is None:
        return event_sha
    assert configured == CHECKOUT_REF
    return event_ref if event_ref == MAIN else event_sha


class GitWorld:
    def __init__(self, root):
        self.root = root
        self.remote = root / "remote.git"
        self.writer = root / "writer"
        self.env = {
            **os.environ,
            "GIT_CONFIG_GLOBAL": str(root / "gitconfig"),
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_ALLOW_PROTOCOL": "file",
            "GIT_TERMINAL_PROMPT": "0",
            "GIT_AUTHOR_NAME": "Fixture",
            "GIT_AUTHOR_EMAIL": "fixture@example.invalid",
            "GIT_COMMITTER_NAME": "Fixture",
            "GIT_COMMITTER_EMAIL": "fixture@example.invalid",
        }
        self.git(root, "init", "--bare", "--initial-branch=main", str(self.remote))
        self.git(root, "init", "--initial-branch=main", str(self.writer))
        self.git(self.writer, "remote", "add", "origin", str(self.remote))
        self.write_report(self.writer, "initial report")
        (self.writer / "sitemap.xml").write_text("fixture sitemap")
        self.commit(self.writer, "Initial source")
        self.git(self.writer, "push", "origin", "HEAD:main")
        # Canonical GitHub origin is translated to this local file remote.
        # No test may use a network transport or real token.
        self.git(
            root,
            "config",
            "--global",
            f"url.{self.remote.as_uri()}.insteadOf",
            "https://github.com/fixture/report.git",
        )

    def git(self, cwd, *args):
        return subprocess.run(
            ["git", *args],
            cwd=cwd,
            env=self.env,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()

    def commit(self, repo, message):
        self.git(repo, "add", "--all")
        self.git(repo, "commit", "-m", message)
        return self.git(repo, "rev-parse", "HEAD")

    def write_report(self, repo, text):
        for relative in REPORT_FILES:
            path = repo / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)

    def advance(self, path, text):
        target = self.writer / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)
        revision = self.commit(self.writer, "Concurrent main update")
        self.git(self.writer, "push", "origin", "HEAD:main")
        return revision

    def checkout(self, event_ref, event_sha):
        job = self.root / "job"
        self.git(self.root, "clone", str(self.remote), str(job))
        self.git(job, "checkout", "-B", "main", _checkout_target(event_ref, event_sha))
        return job

    def run_step(self, repo, name, **extra_env):
        script = _step(name)["run"]
        return subprocess.run(
            ["bash", "--noprofile", "--norc", "-e", "-o", "pipefail", "-c", script],
            cwd=repo,
            env={
                **self.env,
                "GITHUB_REPOSITORY": "fixture/report",
                "GH_TOKEN": "fixture-token",
                "GIT_CONFIG_COUNT": "1",
                "GIT_CONFIG_KEY_0": "safe.directory",
                "GIT_CONFIG_VALUE_0": str(repo),
                **extra_env,
            },
            capture_output=True,
            text=True,
            check=False,
        )

    def publish(self, repo, source, event_sha, **extra_env):
        output = self.root / "publish-output"
        result = self.run_step(
            repo,
            "Commit and push updated report",
            GENERATION_SOURCE_SHA=source,
            GITHUB_SHA=event_sha,
            GITHUB_OUTPUT=str(output),
            RUNNER_TEMP=str(self.root),
            ADMISSION_KEY="digest:" + "a" * 40,
            ADMISSION_FEED="https://example.invalid/commit-addressed-feed.xml",
            PUSH_RETRY_DELAY_SECONDS="0",
            **extra_env,
        )
        return result, output.read_text() if output.exists() else ""


@pytest.fixture
def world(tmp_path):
    assert shutil.which("git"), "Git is required for the workflow race fixtures"
    return GitWorld(tmp_path)


def test_queued_main_run_uses_the_preceding_runs_report_as_its_base(world):
    event_sha = world.git(world.writer, "rev-parse", "HEAD")
    # This event was queued before the first run's report reached main.
    current = world.advance("index.md", "preceding run report")
    job = world.checkout(MAIN, event_sha)
    assert world.git(job, "rev-parse", "HEAD") == current
    assert (job / "index.md").read_text() == "preceding run report"
    world.write_report(job, "queued run report")
    result, output = world.publish(job, current, event_sha)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "published=true" in output
    assert world.git(world.remote, "rev-parse", "main^") == current
    assert world.git(world.remote, "show", "main:index.md") == "queued run report"


@pytest.mark.parametrize("event_ref", ["refs/heads/preview", "refs/tags/fixture"])
def test_non_main_events_keep_their_original_pinned_revision(world, event_ref):
    event_sha = world.git(world.writer, "rev-parse", "HEAD")
    world.advance("index.md", "newer main report")
    job = world.checkout(event_ref, event_sha)
    assert world.git(job, "rev-parse", "HEAD") == event_sha
    assert (job / "index.md").read_text() == "initial report"


def test_checkout_revision_is_recorded_before_generation(world):
    initial = world.git(world.writer, "rev-parse", "HEAD")
    current = world.advance("index.md", "preceding run report")
    job = world.checkout(MAIN, initial)
    verify = _step("Verify checkout Git access")
    assert verify.get("id") == "source"
    output = world.root / "checkout-output"
    result = world.run_step(
        job, "Verify checkout Git access", GITHUB_OUTPUT=str(output)
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert output.read_text().splitlines() == [f"revision={current}"]
    steps = _workflow()["jobs"]["generate-report"]["steps"]
    assert steps.index(verify) < steps.index(_step("Admit generation"))
    assert (
        _step("Commit and push updated report")["env"]["GENERATION_SOURCE_SHA"]
        == "${{ steps.source.outputs.revision }}"
    )


def test_conflicting_main_report_advance_aborts_rebase_and_preserves_remote(world):
    source = world.git(world.writer, "rev-parse", "HEAD")
    job = world.checkout(MAIN, source)
    world.write_report(job, "unpublished generated report")
    advanced = world.advance("index.md", "concurrent update")
    result, output = world.publish(job, source, source)
    assert result.returncode != 0
    assert "published=true" not in output
    assert world.git(world.remote, "rev-parse", "main") == advanced
    assert world.git(world.remote, "show", "main:index.md") == "concurrent update"


def test_non_conflicting_main_advance_rebases_and_publishes(world):
    source = world.git(world.writer, "rev-parse", "HEAD")
    job = world.checkout(MAIN, source)
    world.write_report(job, "generated report after concurrent code update")
    advanced = world.advance("src/new-code.py", "concurrent update")
    result, output = world.publish(job, source, source)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "published=true" in output
    assert world.git(world.remote, "rev-parse", "main^") == advanced
    assert (
        world.git(world.remote, "show", "main:src/new-code.py") == "concurrent update"
    )
    assert (
        world.git(world.remote, "show", "main:index.md")
        == "generated report after concurrent code update"
    )


def test_generation_keeps_its_shared_lock_event_binding_and_publication_gates():
    workflow = _workflow()
    assert workflow["concurrency"] == {
        "group": "sentryinsight-report-generation",
        "cancel-in-progress": "false",
    }
    publish = _step("Commit and push updated report")
    assert "github.ref == 'refs/heads/main'" in publish["if"]
    assert "steps.admission.outputs.decision == 'admitted'" in publish["if"]
    assert "steps.generate.outputs.report_generated == 'true'" in publish["if"]
    assert "steps.source-review-summary.outcome == 'success'" in publish["if"]
    assert publish["env"]["ADMISSION_FEED"] == "${{ steps.admission.outputs.feed_url }}"
    assert "--force" not in publish["run"]
    assert workflow["jobs"]["resume-publication"]["with"] == {"invocation": "resume"}


def test_an_already_applied_report_reports_unpublished_and_preserves_main(world):
    source = world.git(world.writer, "rev-parse", "HEAD")
    job = world.checkout(MAIN, source)
    world.write_report(job, "same generated report")
    world.write_report(world.writer, "same generated report")
    advanced = world.advance("src/new-code.py", "concurrent code update")
    result, output = world.publish(job, source, source)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "published=false" in output
    assert world.git(world.remote, "rev-parse", "main") == advanced


def test_generation_binds_budget_diagnostics_and_tracing_to_the_checkout():
    env = _step("Generate exploitation report")["env"]
    assert (
        env["SENTRYINSIGHT_SOURCE_REVISION"] == "${{ steps.source.outputs.revision }}"
    )
    assert env["LOGFIRE_SERVICE_VERSION"] == "${{ steps.source.outputs.revision }}"
    assert "GITHUB_SHA" not in env


def test_push_race_with_non_conflicting_main_advance_rebases_and_retries_push(world):
    source = world.git(world.writer, "rev-parse", "HEAD")
    job = world.checkout(MAIN, source)
    world.write_report(job, "generated report surviving push race")
    (world.writer / "concurrent-code.py").write_text("concurrent code update")
    advanced = world.commit(world.writer, "Update arriving immediately before push")
    world.git(world.writer, "push", "origin", "HEAD:refs/heads/concurrent-update")
    real_git = shutil.which("git")
    assert real_git
    shim_dir = world.root / "bin"
    shim_dir.mkdir()
    marker = world.root / "raced-once"
    shim = shim_dir / "git"
    # Advance the remote once immediately before the first push attempt so that
    # push fails non-fast-forward and the workflow must fetch, rebase and retry.
    shim.write_text(
        "#!/bin/sh\n"
        f'if [ "$1" = push ] && [ "$3" = HEAD:main ] && [ ! -f {shlex.quote(str(marker))} ]; then\n'
        f"  touch {shlex.quote(str(marker))}\n"
        f"  {shlex.quote(real_git)} --git-dir={shlex.quote(str(world.remote))} "
        f"update-ref refs/heads/main {shlex.quote(advanced)} || exit 1\n"
        "fi\n"
        f'exec {shlex.quote(real_git)} "$@"\n'
    )
    shim.chmod(0o700)
    world.env["PATH"] = str(shim_dir) + os.pathsep + world.env["PATH"]
    result, output = world.publish(job, source, source)
    assert result.returncode == 0, result.stdout + result.stderr
    assert marker.exists()
    assert "published=true" in output
    assert world.git(world.remote, "rev-parse", "main^") == advanced
    assert (
        world.git(world.remote, "show", "main:concurrent-code.py")
        == "concurrent code update"
    )
    assert (
        world.git(world.remote, "show", "main:index.md")
        == "generated report surviving push race"
    )


def test_persistent_push_failure_stops_after_bounded_retries_without_force(world):
    source = world.git(world.writer, "rev-parse", "HEAD")
    job = world.checkout(MAIN, source)
    world.write_report(job, "unpublished generated report")
    real_git = shutil.which("git")
    assert real_git
    shim_dir = world.root / "bin"
    shim_dir.mkdir()
    counter = world.root / "push-attempts"
    shim = shim_dir / "git"
    shim.write_text(
        "#!/bin/sh\n"
        'if [ "$1" = push ] && [ "$3" = HEAD:main ]; then\n'
        f"  echo attempt >> {shlex.quote(str(counter))}\n"
        '  echo "transient push error" >&2\n'
        "  exit 1\n"
        "fi\n"
        f'exec {shlex.quote(real_git)} "$@"\n'
    )
    shim.chmod(0o700)
    world.env["PATH"] = str(shim_dir) + os.pathsep + world.env["PATH"]
    result, output = world.publish(job, source, source)
    assert result.returncode != 0
    assert "published=true" not in output
    assert len(counter.read_text().splitlines()) == 3
    assert world.git(world.remote, "rev-parse", "main") == source
    assert world.git(world.remote, "show", "main:index.md") == "initial report"
