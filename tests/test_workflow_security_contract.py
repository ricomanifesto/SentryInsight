"""Offline source contracts for publication trust and credential lifetimes."""

import os
from pathlib import Path
import re
import subprocess

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def workflow(name):
    return yaml.load(
        (ROOT / ".github/workflows" / f"{name}.yml").read_text(),
        Loader=yaml.BaseLoader,
    )


def step(job, name):
    return next(item for item in job["steps"] if item.get("name") == name)


def test_every_external_workflow_action_uses_an_immutable_commit():
    for path in (ROOT / ".github/workflows").glob("*.yml"):
        document = yaml.load(path.read_text(), Loader=yaml.BaseLoader)
        for job in document["jobs"].values():
            for item in [job, *job.get("steps", [])]:
                reference = item.get("uses", "")
                if reference and not reference.startswith("./"):
                    assert re.fullmatch(r"[^@]+@[0-9a-f]{40}", reference), (
                        path.name,
                        reference,
                    )


def test_publication_admits_source_before_a_write_capable_checkout():
    document = workflow("publish-production")
    assert document["on"]["workflow_run"]["branches"] == ["main"]
    assert document["permissions"] == {"contents": "read", "actions": "read"}
    assert "concurrency" not in document
    admission = document["jobs"]["authorize"]
    assert " ".join(admission["if"].split()) == (
        "(github.event_name != 'workflow_run' && "
        "github.ref == 'refs/heads/main' && inputs.invocation != '') || "
        "(github.event_name == 'workflow_run' && "
        "github.event.workflow_run.conclusion == 'success' && "
        "github.event.workflow_run.event == 'push' && "
        "github.event.workflow_run.head_branch == 'main' && "
        "github.event.workflow_run.head_repository.full_name == github.repository)"
    )
    assert all("uses" not in item for item in admission["steps"])
    assert admission["outputs"]["source_sha"] == "${{ steps.source.outputs.sha }}"
    publisher = document["jobs"]["publish"]
    assert publisher["needs"] == "authorize"
    assert publisher["permissions"] == {"contents": "write"}
    assert publisher["concurrency"] == {
        "group": "publish-production",
        "cancel-in-progress": "false",
    }
    checkout = step(publisher, "Checkout source")
    assert checkout["with"]["ref"] == "${{ needs.authorize.outputs.source_sha }}"
    assert checkout["with"]["persist-credentials"] == "false"
    run = step(publisher, "Run publisher")
    assert run["env"]["SOURCE_SHA"] == "${{ needs.authorize.outputs.source_sha }}"
    assert run["env"]["GH_TOKEN"] == "${{ github.token }}"


@pytest.mark.parametrize(
    ("event", "invocation", "relation", "validated", "expected"),
    [
        ("workflow_run", "", "", "", True),
        ("workflow_dispatch", "publish", "ahead", "true", True),
        ("workflow_dispatch", "publish", "identical", "true", True),
        ("workflow_dispatch", "publish", "diverged", "true", False),
        ("workflow_dispatch", "publish", "behind", "true", False),
        ("workflow_dispatch", "publish", "ahead", "false", False),
        ("workflow_dispatch", "publish", "ahead", "", False),
        ("repository_dispatch", "resume", "", "", True),
        ("schedule", "resume", "", "", True),
    ],
)
def test_source_admission_preserves_validated_sha_and_resume(
    tmp_path, event, invocation, relation, validated, expected
):
    admission = workflow("publish-production")["jobs"]["authorize"]
    configured = step(admission, "Authorize source")
    script = configured["run"]
    # The only provider calls are read-only main ancestry and successful push
    # validation queries. All responses here come from an offline CLI fixture.
    assert "compare/$SOURCE_SHA...$GITHUB_SHA" in script
    assert "head_sha=$SOURCE_SHA&event=push&branch=main&status=success" in script
    for required in (
        ".head_sha == env.SOURCE_SHA",
        ".head_repository.full_name == env.GITHUB_REPOSITORY",
        '.head_branch == "main"',
        '.event == "push"',
        '.conclusion == "success"',
    ):
        assert required in script
    shim = tmp_path / "gh"
    shim.write_text(
        "#!/bin/sh\n"
        'printf "%s\\n" "$*" >> "$CALLS"\n'
        'case "$2" in\n'
        '  */compare/*) printf "%s\\n" "$RELATION" ;;\n'
        '  */actions/*) printf "%s\\n" "$VALIDATED" ;;\n'
        "  *) exit 1 ;;\n"
        "esac\n"
    )
    shim.chmod(0o700)
    output = tmp_path / "output"
    calls = tmp_path / "calls"
    selected = "a" * 40
    result = subprocess.run(
        ["bash", "-e", "-o", "pipefail", "-c", script],
        env={
            "PATH": str(tmp_path) + os.pathsep + os.environ["PATH"],
            "GITHUB_EVENT_NAME": event,
            "GITHUB_SHA": "b" * 40,
            "GITHUB_REPOSITORY": "fixture/report",
            "GITHUB_OUTPUT": str(output),
            "VALIDATED_SHA": selected if event == "workflow_run" else "",
            "REQUESTED_SHA": selected if invocation == "publish" else "",
            "INVOCATION": invocation,
            "RELATION": relation,
            "VALIDATED": validated,
            "CALLS": str(calls),
        },
        capture_output=True,
        text=True,
    )
    assert (result.returncode == 0) is expected, result.stderr
    if expected:
        expected_sha = selected if invocation != "resume" else "b" * 40
        assert output.read_text() == f"sha={expected_sha}\n"
    else:
        assert not output.exists()
    if event == "workflow_run" or invocation == "resume":
        assert not calls.exists()


def test_generation_keeps_the_pat_only_in_the_guarded_report_push():
    document = workflow("generate-report")
    assert document["permissions"] == {"contents": "read", "actions": "read"}
    job = document["jobs"]["generate-report"]
    assert job["permissions"] == {"contents": "write", "actions": "read"}
    checkout = step(job, "Checkout code")["with"]
    assert checkout["persist-credentials"] == "false"
    assert "token" not in checkout
    assert "PAT_GITHUB" not in str(document.get("env", {})) + str(job.get("env", {}))
    holders = [item["name"] for item in job["steps"] if "PAT_GITHUB" in str(item)]
    assert holders == ["Commit and push updated report"]
    push = step(job, holders[0])
    assert "github.ref == 'refs/heads/main'" in push["if"]
    assert push["env"]["GH_TOKEN"] == "${{ secrets.PAT_GITHUB }}"
    assert "secrets." not in push["run"]
    assert "git push origin HEAD:main" in push["run"]
    assert (
        "git config"
        not in push["run"].split("max_attempts=")[0].split("git commit", 1)[-1]
    )
    assert step(job, "Find Validate result for this commit")["env"]["GH_TOKEN"] == (
        "${{ github.token }}"
    )
    for name in (
        "Admit generation",
        "Record generation start",
        "Generate exploitation report",
        "Record generation outcome",
    ):
        assert step(job, name)["env"]["SENTRYINSIGHT_ADMISSION_GITHUB_TOKEN"] == (
            "${{ github.token }}"
        )


def test_pages_concurrency_and_write_permissions_follow_the_trust_guard():
    document = workflow("deploy-pages")
    assert "concurrency" not in document
    assert document["permissions"] == {"contents": "read"}
    deploy = document["jobs"]["deploy"]
    assert deploy["concurrency"] == {
        "group": "sentryinsight-pages",
        "cancel-in-progress": "true",
    }
    assert deploy["permissions"] == {
        "contents": "read",
        "pages": "write",
        "id-token": "write",
    }
    assert (
        step(deploy, "Checkout validated source")["with"]["persist-credentials"]
        == "false"
    )


def test_scoped_git_headers_match_the_canonical_origin(tmp_path):
    for name, job_name, step_name in (
        ("generate-report", "generate-report", "Admit generation"),
        ("generate-report", "generate-report", "Record generation start"),
        ("generate-report", "generate-report", "Commit and push updated report"),
        ("generate-report", "generate-report", "Record generation outcome"),
        ("publish-production", "publish", "Run publisher"),
    ):
        job = workflow(name)["jobs"][job_name]
        script = step(job, step_name)["run"]
        assert (
            'GIT_CONFIG_KEY_1="http.https://github.com/${GITHUB_REPOSITORY}.git.extraheader"'
            in script
        )
        assert "::add-mask::%s" in script
        verify = step(job, "Verify checkout Git access")["run"]
        assert (
            'git remote set-url origin "https://github.com/${GITHUB_REPOSITORY}.git"'
            in verify
        )
        result = subprocess.run(
            [
                "git",
                "config",
                "--get-urlmatch",
                "http.extraheader",
                "https://github.com/fixture/report.git",
            ],
            env={
                "PATH": os.environ["PATH"],
                "GIT_CONFIG_NOSYSTEM": "1",
                "GIT_CONFIG_GLOBAL": os.devnull,
                "GIT_CONFIG_COUNT": "1",
                "GIT_CONFIG_KEY_0": "http.https://github.com/fixture/report.git.extraheader",
                "GIT_CONFIG_VALUE_0": "fixture-header",
            },
            capture_output=True,
            text=True,
            cwd=tmp_path,
        )
        assert result.returncode == 0
        assert result.stdout.strip() == "fixture-header"
