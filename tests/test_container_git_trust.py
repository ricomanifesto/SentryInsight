"""Reproduce checkout's temporary-HOME trust boundary without changing owners."""

import os
from pathlib import Path
import re
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    "workflow_name", ["validate", "generate-report", "publish-production"]
)
def test_container_git_trust_is_inherited_and_limited_to_checkout(
    tmp_path, workflow_name
):
    workflow = (ROOT / ".github/workflows" / f"{workflow_name}.yml").read_text()
    job_config = workflow.split("    steps:\n", 1)[0]
    configured = dict(re.findall(r"^      (GIT_CONFIG_\w+): (.+)$", job_config, re.M))
    assert configured == {
        "GIT_CONFIG_COUNT": "'1'",
        "GIT_CONFIG_KEY_0": "safe.directory",
        "GIT_CONFIG_VALUE_0": "${{ github.workspace }}",
    }
    assert "git rev-parse --verify HEAD\n          git status --porcelain" in workflow
    assert (
        workflow.index("uses: actions/checkout@v5")
        < workflow.index("git rev-parse --verify HEAD")
        < workflow.index("name: Set up Python")
    )
    assert "safe.directory '*'" not in workflow
    assert "git config --global" not in workflow.split("name: Set up Python", 1)[0]

    home = tmp_path / "job-home"
    home.mkdir()
    checkout_home = tmp_path / "checkout-temporary-home"
    checkout_home.mkdir()
    env = {
        key: value for key, value in os.environ.items() if not key.startswith("GIT_")
    }
    env.update(
        HOME=str(home),
        XDG_CONFIG_HOME=str(home),
        GIT_CONFIG_NOSYSTEM="1",
        GIT_CONFIG_GLOBAL=str(home / ".gitconfig"),
    )

    def git(args, cwd, environment):
        return subprocess.run(
            ["git", *args], cwd=cwd, env=environment, text=True, capture_output=True
        )

    repos = [tmp_path / "checkout", tmp_path / "unrelated"]
    for repo in repos:
        repo.mkdir()
        assert git(["init", "-q"], repo, env).returncode == 0
        assert (
            git(
                [
                    "-c",
                    "user.name=Test",
                    "-c",
                    "user.email=test@example.invalid",
                    "commit",
                    "--allow-empty",
                    "-qm",
                    "Synthetic fixture",
                ],
                repo,
                env,
            ).returncode
            == 0
        )
    repo, unrelated = repos
    # Equivalent to checkout's temporary global exception, not a host config edit.
    checkout_config = checkout_home / ".gitconfig"
    checkout_env = {**env, "GIT_CONFIG_GLOBAL": str(checkout_config)}
    assert (
        git(
            ["config", "--global", "--add", "safe.directory", str(repo)],
            repo,
            checkout_env,
        ).returncode
        == 0
    )
    # Git's own test hook exercises ownership checking without chown/root/permissions.
    env["GIT_TEST_ASSUME_DIFFERENT_OWNER"] = "1"
    rejected = git(["rev-parse", "HEAD"], repo, env)
    assert rejected.returncode == 128
    assert "dubious ownership" in rejected.stderr
    assert (
        git(
            ["rev-parse", "HEAD"],
            repo,
            {**checkout_env, "GIT_TEST_ASSUME_DIFFERENT_OWNER": "1"},
        ).returncode
        == 0
    )

    env.update(
        {
            key: value.strip("'").replace("${{ github.workspace }}", str(repo))
            for key, value in configured.items()
        }
    )
    # Match the evaluation runner's inherited child-process Git calls exactly.
    script = (
        "import subprocess; "
        "subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, check=True); "
        "subprocess.run(['git', 'status', '--porcelain'], capture_output=True, check=True)"
    )
    result = subprocess.run(
        [sys.executable, "-c", script],
        cwd=repo,
        env=env,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert git(["rev-parse", "HEAD"], unrelated, env).returncode == 128
    assert not (home / ".gitconfig").exists()
    assert checkout_config.read_text().count("directory") == 1
