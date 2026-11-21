"""The actual workflow wiring of the defensive publication gate.

Static reads of the committed workflow files plus each promotion guard's own
shell, executed locally with synthetic values. Nothing is dispatched.
"""

import json
from pathlib import Path
import re
import subprocess

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
HEAD = "a" * 40
DIGEST = "b" * 64
PROMOTION = ("publish-production.yml", "deploy-pages.yml")


def load(name):
    text = (WORKFLOWS / name).read_text()
    return text, yaml.safe_load(text)


def triggers(workflow):
    return workflow[True]


def executable(text):
    return "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("#")
    )


def guard(name):
    _, workflow = load(name)
    [job] = workflow["jobs"].values()
    step = job["steps"][0]
    assert step["name"].startswith("Refuse anything but the first manual main attempt")
    return step["run"]


def test_validate_is_synthetic_only_with_no_screenshot_or_upload():
    text, workflow = load("validate.yml")
    assert set(triggers(workflow)) == {"pull_request", "push"}
    assert triggers(workflow)["push"] == {"branches": ["main"]}
    script = (ROOT / "scripts" / "validate_synthetic.sh").read_text()
    # Every step that runs, except the two that exclude and prove absence.
    exclusion = {
        "Checkout code without live report paths or real facts",
        "Prove live report paths and real facts are absent",
    }
    running = "\n".join(
        json.dumps(step)
        for step in workflow["jobs"]["validate"]["steps"]
        if step["name"] not in exclusion
    )
    for body in (running, executable(script)):
        for forbidden in (
            "upload-artifact",
            "screenshot",
            "test:browser",
            "package_pages",
            "validate_report",
            "build_static_artifact",
            "index.md",
            "local_validation.sh",
            "tests -q",
        ):
            assert forbidden not in body, forbidden
    assert "bash scripts/validate_synthetic.sh" in text
    steps = workflow["jobs"]["validate"]["steps"]
    checkout = steps[0]
    assert checkout["with"]["sparse-checkout-cone-mode"] is False
    patterns = checkout["with"]["sparse-checkout"].split()
    assert patterns[0] == "/*"
    held = (
        "index.md",
        "index.html",
        "current-findings.json",
        "sitemap.xml",
        "reports/",
        "corrections/",
        "config/paid-readiness-facts.json",
        "config/paid-readiness-surface.json",
    )
    for path in held:
        assert f"!/{path}" in patterns, path
    names = [step["name"] for step in steps]
    proof = names.index("Prove live report paths and real facts are absent")
    assert proof < names.index("Run synthetic validation")
    for path in held:
        assert path.rstrip("/") in steps[proof]["run"], path
    assert "tests/test_defensive_package.py" in script


@pytest.mark.parametrize("name", PROMOTION)
def test_promotion_is_manual_only_with_the_approval_triple(name):
    text, workflow = load(name)
    assert set(triggers(workflow)) == {"workflow_dispatch"}
    inputs = triggers(workflow)["workflow_dispatch"]["inputs"]
    assert set(inputs) == {
        "approved_head",
        "approved_facts_sha256",
        "approved_package_sha256",
    }
    assert all(spec["required"] is True for spec in inputs.values())
    [job] = workflow["jobs"].values()
    assert (
        job["if"]
        == "github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main'"
    )
    for forbidden in (
        "workflow_run",
        "workflow_call",
        "schedule",
        "package_pages",
        "resume",
        "rollback",
    ):
        assert forbidden not in executable(text), forbidden


CASES = [
    ("workflow_dispatch", "refs/heads/main", "1", HEAD, HEAD, DIGEST, DIGEST, True),
    ("workflow_run", "refs/heads/main", "1", HEAD, HEAD, DIGEST, DIGEST, False),
    ("pull_request", "refs/pull/1/merge", "1", HEAD, HEAD, DIGEST, DIGEST, False),
    ("schedule", "refs/heads/main", "1", HEAD, HEAD, DIGEST, DIGEST, False),
    ("workflow_dispatch", "refs/heads/preview", "1", HEAD, HEAD, DIGEST, DIGEST, False),
    ("workflow_dispatch", "refs/heads/main", "2", HEAD, HEAD, DIGEST, DIGEST, False),
    (
        "workflow_dispatch",
        "refs/heads/main",
        "1",
        "c" * 40,
        HEAD,
        DIGEST,
        DIGEST,
        False,
    ),
    ("workflow_dispatch", "refs/heads/main", "1", HEAD, HEAD, "", DIGEST, False),
    ("workflow_dispatch", "refs/heads/main", "1", HEAD, HEAD, DIGEST, "B" * 64, False),
]


@pytest.mark.parametrize("name", PROMOTION)
@pytest.mark.parametrize(
    "event,ref,attempt,sha,head,facts,package,allowed",
    CASES,
    ids=[
        "manual-main",
        "workflow-run",
        "pull-request",
        "schedule",
        "preview-branch",
        "rerun",
        "wrong-head",
        "missing-facts",
        "malformed-package",
    ],
)
def test_actual_promotion_guard_fails_closed(
    name, event, ref, attempt, sha, head, facts, package, allowed
):
    result = subprocess.run(
        ["bash", "-c", guard(name)],
        env={
            "PATH": "/usr/bin:/bin",
            "GITHUB_EVENT_NAME": event,
            "GITHUB_REF": ref,
            "GITHUB_RUN_ATTEMPT": attempt,
            "GITHUB_SHA": sha,
            "APPROVED_HEAD": head,
            "APPROVED_FACTS": facts,
            "APPROVED_PACKAGE": package,
        },
        capture_output=True,
        text=True,
    )
    assert (result.returncode == 0) is allowed


def test_both_publish_entry_points_verify_the_same_triple_with_one_packager():
    assert guard("publish-production.yml") == guard("deploy-pages.yml")
    production, _ = load("publish-production.yml")
    pages, workflow = load("deploy-pages.yml")
    assert re.search(
        r'node publication/cli.js publish --source "\$APPROVED_HEAD" \\\s+'
        r'--approved-head "\$APPROVED_HEAD" \\\s+'
        r'--approved-facts-sha256 "\$APPROVED_FACTS" \\\s+'
        r'--approved-package-sha256 "\$APPROVED_PACKAGE"',
        production,
    )
    steps = workflow["jobs"]["deploy"]["steps"]
    names = [step["name"] for step in steps]
    build = steps[names.index("Build the approved defensive package")]["run"]
    verify = steps[names.index("Re-verify the approved bytes before upload")]["run"]
    upload = steps[names.index("Upload Pages artifact")]
    for flag in (
        '--approve-head "$APPROVED_HEAD"',
        '--approve-facts "$APPROVED_FACTS"',
        '--approve-package "$APPROVED_PACKAGE"',
    ):
        assert flag in build
    assert "scripts/package_defensive.py build" in build
    assert "scripts/package_defensive.py verify" in verify
    assert (
        names.index("Build the approved defensive package")
        < names.index("Re-verify the approved bytes before upload")
        < names.index("Upload Pages artifact")
    )
    assert upload["with"]["path"] == "${{ runner.temp }}/defensive/package"
    # Both reach the same shared packager: the Node publisher spawns it.
    kit = (ROOT / "publication" / "kit" / "defensive.js").read_text()
    assert "path.join('scripts', 'package_defensive.py')" in kit


def test_no_other_workflow_can_publish_deploy_or_resume():
    for path in sorted(WORKFLOWS.glob("*.yml")):
        text = executable(path.read_text())
        workflow = yaml.safe_load(path.read_text())
        on = triggers(workflow)
        if isinstance(on, dict) and "workflow_run" in on:
            assert on["workflow_run"]["workflows"] != ["Validate"], path.name
        assert "uses: ./.github/workflows/publish-production.yml" not in text, path.name
        assert not re.search(r"cli\.js (resume|rollback)", text), path.name
        if path.name not in PROMOTION:
            for forbidden in (
                "upload-pages-artifact",
                "deploy-pages@",
                "cli.js publish",
            ):
                assert forbidden not in text, (path.name, forbidden)


def test_generator_is_manual_and_its_paid_job_never_checks_out_legacy_bytes():
    text, workflow = load("generate-report.yml")
    assert set(triggers(workflow)) == {"workflow_dispatch"}
    # The hosted legacy generator is held: with paid_verification false no
    # job runs, so no legacy checkout, upload, screenshot or push is reachable.
    assert set(workflow["jobs"]) == {"paid-readiness"}
    assert workflow["jobs"]["paid-readiness"]["if"] == (
        "github.event_name == 'workflow_dispatch' && "
        "github.event.inputs.paid_verification == 'true'"
    )
    for held in (
        "git push",
        "Commit and push",
        "main.py",
        "screenshot",
        "test:browser",
        "package_pages",
        "local_validation",
    ):
        assert held not in executable(text), held
    steps = workflow["jobs"]["paid-readiness"]["steps"]
    checkout = next(
        step for step in steps if step.get("uses", "").startswith("actions/checkout")
    )
    assert checkout["with"]["sparse-checkout-cone-mode"] is False
    patterns = checkout["with"]["sparse-checkout"].split()
    assert patterns[0] == "/*"
    for legacy in (
        "index.md",
        "index.html",
        "current-findings.json",
        "sitemap.xml",
        "reports/",
    ):
        assert f"!/{legacy}" in patterns
    assert set(
        re.findall(
            r"secrets\.([A-Z_]+)", executable(text[text.index("  paid-readiness:") :])
        )
    ) == {
        "PAT_GITHUB",
        "OPENROUTER_API_KEY",
    }


def test_source_branch_previews_are_suppressed_in_candidate_config():
    assert json.loads((ROOT / "vercel.json").read_text()) == {
        "git": {"deploymentEnabled": False}
    }


@pytest.mark.parametrize(
    "present",
    [None, "index.md", "reports/2026-01-01.md", "config/paid-readiness-facts.json"],
)
def test_actual_validate_absence_proof_refuses_any_live_path(tmp_path, present):
    _, workflow = load("validate.yml")
    steps = workflow["jobs"]["validate"]["steps"]
    script = next(
        s["run"]
        for s in steps
        if s["name"] == "Prove live report paths and real facts are absent"
    )
    env = {
        "PATH": "/usr/bin:/bin",
        "HOME": str(tmp_path),
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_AUTHOR_NAME": "Synthetic",
        "GIT_AUTHOR_EMAIL": "synthetic@example.test",
        "GIT_COMMITTER_NAME": "Synthetic",
        "GIT_COMMITTER_EMAIL": "synthetic@example.test",
    }
    subprocess.run(["git", "init", "--quiet"], cwd=tmp_path, env=env, check=True)
    subprocess.run(
        ["git", "commit", "--quiet", "--allow-empty", "-m", "synthetic"],
        cwd=tmp_path,
        env=env,
        check=True,
    )
    if present:
        target = tmp_path / present
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("synthetic decoy\n")
    result = subprocess.run(
        ["bash", "-c", script], cwd=tmp_path, env=env, capture_output=True, text=True
    )
    assert (result.returncode == 0) is (present is None)
