"""Production publication: public-site configuration, report URL boundary,
static-builder inputs, the publisher workflow and generation admission."""

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CURRENT_REPORT = (ROOT / "index.md").read_text()
SITE_CONFIG = json.loads((ROOT / "publication" / "site.json").read_text())
LEGAL_STATES = (
    {"mode": "disabled", "proof": "off"},
    {"mode": "prepare", "proof": "off"},
    {"mode": "prepare", "proof": "on"},
    {"mode": "active", "proof": "on"},
)
PAGES = "https://ricomanifesto.github.io"
PRODUCTION = {
    "SentryDigest": "https://sentrydigest.ricomanifesto.com/",
    "SentryInsight": "https://sentryinsight.ricomanifesto.com/",
    "GRCInsight": "https://grcinsight.ricomanifesto.com/",
}


def _emitted(site: str) -> str:
    origins = SITE_CONFIG["origins"][site]
    return origins[origins["emitted"]]


def _with_state(tmp_path, publication: dict, emitted: str) -> Path:
    config = json.loads(json.dumps(SITE_CONFIG))
    config["publication"] = publication
    for origins in config["origins"].values():
        origins["emitted"] = emitted
    path = tmp_path / "site.json"
    path.write_text(json.dumps(config, indent=2) + "\n")
    return path


def _under_config(config_path: Path, script: str) -> dict:
    """Runs script with public_site reading config_path; returns its JSON."""
    prelude = (
        "import json, sys\n"
        "from pathlib import Path\n"
        "import src.core.public_site as public_site\n"
        f"public_site.SITE_CONFIG_PATH = Path({str(config_path)!r})\n"
    )
    result = subprocess.run(
        [sys.executable, "-B", "-c", prelude + script],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    return json.loads(result.stdout)


def _report_with(url: str) -> str:
    return re.sub(
        r"^digest_issue_url: .*$",
        f"digest_issue_url: {url}",
        CURRENT_REPORT,
        count=1,
        flags=re.M,
    )


def _report_date() -> str:
    return re.search(r"^report_date: (\S+)$", CURRENT_REPORT, re.M).group(1)


def _workflow(name: str) -> str:
    return (ROOT / ".github" / "workflows" / name).read_text()


def test_publication_configuration_is_a_legal_activation_state():
    # Any legal state passes the ordinary gates; the shipped initial state is
    # verified separately as a candidate fact.
    config = SITE_CONFIG
    assert config["site"] == "SentryInsight"
    assert config["publication"] in LEGAL_STATES
    for site, production in PRODUCTION.items():
        origins = config["origins"][site]
        assert origins["legacy"] == f"{PAGES}/{site}/"
        assert origins["production"] == production
        assert origins["emitted"] in ("legacy", "production")
    assert "consumers" not in config
    assert config["payload_builder"] == [
        "python3",
        "-B",
        "scripts/build_static_artifact.py",
    ]


def test_public_site_derives_emitted_and_accepted_origins():
    from src.core.public_site import accepted_origins, emitted_origin

    assert emitted_origin("SentryInsight") == _emitted("SentryInsight")
    assert emitted_origin("SentryDigest") == _emitted("SentryDigest")
    assert accepted_origins("SentryDigest") == (
        "https://ricomanifesto.github.io/SentryDigest/",
        "https://sentrydigest.ricomanifesto.com/",
    )


def test_digest_issue_url_is_accepted_under_exactly_one_configured_root():
    from src.core.report_artifact import (
        DIGEST_ARCHIVE_ROOT,
        DIGEST_ARCHIVE_ROOTS,
        ReportArtifactError,
        parse_report_artifact,
    )

    assert DIGEST_ARCHIVE_ROOT == f"{_emitted('SentryDigest')}archive/"
    assert DIGEST_ARCHIVE_ROOTS == (
        "https://ricomanifesto.github.io/SentryDigest/archive/",
        "https://sentrydigest.ricomanifesto.com/archive/",
    )
    day = _report_date()
    assert parse_report_artifact(CURRENT_REPORT).digest_issue_url in (
        f"{root}{day}/" for root in DIGEST_ARCHIVE_ROOTS
    )
    for root in DIGEST_ARCHIVE_ROOTS:
        artifact = parse_report_artifact(_report_with(f"{root}{day}/"))
        assert artifact.digest_issue_url == f"{root}{day}/"
    for url in [
        "https://sentrydigest.ricomanifesto.com/archive/2000-01-01/",
        f"https://sentrydigest-x.vercel.app/archive/{day}/",
        f"https://sentrydigest.ricomanifesto.com/SentryDigest/archive/{day}/",
        f"https://ricomanifesto.github.io/SentryDigest/archive/{day}",
    ]:
        with pytest.raises(ReportArtifactError, match="digest_issue_url"):
            parse_report_artifact(_report_with(url))


def test_report_metadata_and_site_urls_come_from_the_emitted_origins():
    from scripts import build_site

    assert build_site.PUBLIC_ROOT == _emitted("SentryInsight")
    # The generation workflow module needs the full model environment to
    # import; its URL boundary is checked in source instead.
    source = (ROOT / "src" / "core" / "workflow.py").read_text()
    assert "ricomanifesto.github.io" not in source
    assert "    DIGEST_ARCHIVE_ROOT,\n" in source
    assert 'f"digest_issue_url: {DIGEST_ARCHIVE_ROOT}{report_date}/\\n"' in source


@pytest.mark.parametrize("publication", LEGAL_STATES)
@pytest.mark.parametrize("emitted", ["legacy", "production"])
def test_every_legal_state_and_emission_keeps_historical_reports_valid(
    tmp_path, publication, emitted
):
    config_path = _with_state(tmp_path, publication, emitted)
    observed = _under_config(
        config_path,
        """
from scripts import build_site
from src.core import report_artifact
reports = sorted(Path("reports").glob("????-??-??.md"))
for report in reports:
    report_artifact.parse_report_artifact(report.read_text())
print(json.dumps({
    "public_root": build_site.PUBLIC_ROOT,
    "digest_root": report_artifact.DIGEST_ARCHIVE_ROOT,
    "accepted": list(report_artifact.DIGEST_ARCHIVE_ROOTS),
    "reports": len(reports),
}))
""",
    )
    origin = PRODUCTION if emitted == "production" else None
    expected_insight = origin["SentryInsight"] if origin else f"{PAGES}/SentryInsight/"
    expected_digest = origin["SentryDigest"] if origin else f"{PAGES}/SentryDigest/"
    assert observed["public_root"] == expected_insight
    assert observed["digest_root"] == f"{expected_digest}archive/"
    # Historical reports keep the origin they were written with and still
    # parse, because both configured Digest roots stay accepted.
    assert observed["accepted"] == [
        f"{PAGES}/SentryDigest/archive/",
        f"{PRODUCTION['SentryDigest']}archive/",
    ]
    assert observed["reports"] > 0


def test_static_builder_snapshots_the_public_site_configuration():
    from scripts.build_static_artifact import SNAPSHOT_FILES

    assert "publication/site.json" in SNAPSHOT_FILES


@pytest.mark.skipif(shutil.which("node") is None, reason="node is required")
def test_shared_publication_kit():
    test_dir = ROOT / "publication" / "test"
    tests = sorted(str(path) for path in test_dir.glob("*.test.js"))
    result = subprocess.run(
        ["node", "--test", "--test-concurrency=1", *tests],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout[-4000:] + result.stderr[-2000:]


def test_publisher_runs_after_validation_or_through_the_manual_gate():
    workflow = _workflow("publish-production.yml")
    assert re.search(
        r"workflow_run:\n\s+workflows: \[\"Validate\"\]\n\s+branches: \[main\]\n"
        r"\s+types: \[completed\]",
        workflow,
    )
    assert "workflow_dispatch:" in workflow
    assert re.search(
        r"^  workflow_call:\n    inputs:\n      invocation:\n", workflow, re.M
    )
    assert re.search(r"^permissions:\n  contents: write\n", workflow, re.M)
    assert "group: publish-production\n  cancel-in-progress: false" in workflow
    assert "inputs.invocation != ''" in workflow
    assert "github.event.workflow_run.conclusion == 'success'" in workflow
    assert "github.event.workflow_run.event == 'push'" in workflow
    assert "github.event.workflow_run.head_sha || inputs.source_sha" in workflow
    # Every publish that Validate did not already gate runs the repository
    # gate on the exact source, whichever event started it.
    assert re.search(
        r"- name: Run repository gate\n\s+if: github\.event_name != 'workflow_run'"
        r" && \(inputs\.invocation \|\| 'publish'\) == 'publish'\n"
        r"[\s\S]*?bash scripts/local_validation\.sh",
        workflow,
    )
    assert "actions: write" not in workflow and "secrets." not in workflow


def test_an_unchanged_generation_resumes_the_current_release():
    workflow = _workflow("generate-report.yml")
    assert re.search(
        r"generate-report:\n\s+runs-on: ubuntu-latest\n\s+outputs:\n"
        r"\s+published: \$\{\{ steps\.publish\.outputs\.published \}\}",
        workflow,
    )
    # A pushed report is published after Validate; otherwise the same single
    # publisher resumes the current release, never promoting new source.
    assert re.search(
        r"\n  resume-publication:\n    needs: generate-report\n"
        r"    if: always\(\) && needs\.generate-report\.outputs\.published != 'true'\n"
        r"    permissions:\n      contents: write\n"
        r"    uses: \./\.github/workflows/publish-production\.yml\n"
        r"    with:\n      invocation: resume\n",
        workflow,
    )
    assert "source_sha" not in workflow.split("resume-publication:")[1]


def test_pages_mirror_is_retained_behind_the_report_gate():
    workflow = _workflow("deploy-pages.yml")
    assert "scripts/package_pages.py --output _site" in workflow
    assert "actions/deploy-pages" in workflow
    # Manual and Validate-triggered deployments both pass the substantive
    # report gate first; a failure stops the job before anything is uploaded,
    # so the last deployed Pages output stays live.
    gate = workflow.index("- name: Validate report content")
    package = workflow.index("- name: Build public artifact")
    upload = workflow.index("- name: Upload Pages artifact")
    deploy = workflow.index("- name: Deploy Pages artifact")
    assert gate < package < upload < deploy
    assert "uv run python scripts/validate_report.py index.md" in workflow[gate:package]
    assert "continue-on-error" not in workflow
    assert "always()" not in workflow[gate:]


def test_report_gate_refuses_a_parseable_report_without_its_sections(tmp_path):
    from src.core.report_artifact import parse_report_artifact

    probe = re.sub(r"^## Executive Summary\n", "", CURRENT_REPORT, count=1, flags=re.M)
    assert probe != CURRENT_REPORT
    parse_report_artifact(probe)
    report = tmp_path / "index.md"
    report.write_text(probe)
    result = subprocess.run(
        [sys.executable, "-B", "scripts/validate_report.py", str(report)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert "missing_section" in result.stdout


def test_generation_is_admitted_bound_and_recorded():
    workflow = _workflow("generate-report.yml")
    admit = workflow.index("- name: Admit generation")
    generate = workflow.index("- name: Generate exploitation report")
    assert admit < generate
    assert "node publication/cli.js admit" in workflow
    assert re.search(
        r"- name: Generate exploitation report\n\s+id: generate\n\s+if: "
        r"steps\.admission\.outputs\.decision == 'admitted'",
        workflow,
    )
    bind = workflow.index("- name: Bind generator input to the admitted feed snapshot")
    invoked = workflow.index("- name: Record generation start")
    assert admit < bind < invoked < generate
    assert "c.feed_url = process.env.FEED_URL" in workflow
    assert re.search(
        r"- name: Restore generator configuration\n\s+if: always\(\)[^\n]*\n"
        r"\s+run: git checkout -- config/config\.json",
        workflow,
    )
    restore = workflow.index("- name: Restore generator configuration")
    commit = workflow.index("- name: Commit and push updated report")
    assert generate < restore < commit
    assert 'git commit -F "$RUNNER_TEMP/report-commit-message.txt"' in workflow
    assert "node publication/cli.js complete" in workflow
    assert "readmit:" in workflow
    assert re.search(
        r"repository_dispatch:\n\s+types: \[sentrydigest-updated\]", workflow
    )
    assert "cancel-in-progress: false" in workflow


def _commit_message_template(workflow: str) -> str:
    match = re.search(
        r"printf '([^']+)' \"\$ADMISSION_KEY\" \"\$\{ADMISSION_FEED:-none\}\"", workflow
    )
    assert match, "report commit message template not found"
    return match.group(1)


@pytest.mark.skipif(shutil.which("node") is None, reason="node is required")
def test_report_commits_carry_exact_recoverable_admission_trailers(tmp_path):
    workflow = _workflow("generate-report.yml")
    template = _commit_message_template(workflow)
    assert re.search(
        r"ADMISSION_FEED: \$\{\{ steps\.admission\.outputs\.feed_url \}\}", workflow
    )
    repo = tmp_path / "repo"
    repo.mkdir()
    env = {
        "GIT_CONFIG_GLOBAL": "/dev/null",
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_AUTHOR_NAME": "Fixture",
        "GIT_AUTHOR_EMAIL": "fixture@example.invalid",
        "GIT_COMMITTER_NAME": "Fixture",
        "GIT_COMMITTER_EMAIL": "fixture@example.invalid",
        "PATH": __import__("os").environ["PATH"],
    }
    feed = (
        "https://raw.githubusercontent.com/ricomanifesto/SentryDigest/"
        + "2" * 40
        + "/site/feed.xml"
    )

    def commit(key: str, feed_url: str, text: str) -> str:
        (repo / "index.md").write_text(text)
        message = repo / "message.txt"
        subprocess.run(
            [
                "bash",
                "-c",
                f'printf \'{template}\' "$1" "${{2:-none}}" > message.txt',
                "_",
                key,
                feed_url,
            ],
            cwd=repo,
            env=env,
            check=True,
        )
        subprocess.run(["git", "add", "index.md"], cwd=repo, env=env, check=True)
        subprocess.run(
            ["git", "commit", "-q", "-F", str(message)], cwd=repo, env=env, check=True
        )
        return subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo,
            env=env,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()

    subprocess.run(
        ["git", "init", "-q", "--initial-branch=main"], cwd=repo, env=env, check=True
    )
    commit("run:12", "", "scheduled report\n")
    bound = commit("digest:" + "3" * 40, feed, "event report\n")
    script = (
        "const { createGit } = require(process.argv[1] + '/publication/kit/git');"
        "const { findAdmissionReport } = require(process.argv[1] + '/publication/kit/admission');"
        "const git = createGit(process.argv[2]);"
        "const find = (key, feedUrl) => findAdmissionReport({ git, ref: 'HEAD', key, feedUrl, reportPath: 'index.md' });"
        "process.stdout.write(JSON.stringify(["
        "find('run:1'), Boolean(find('run:12')), find('digest:' + '3'.repeat(40)),"
        " find('digest:' + '3'.repeat(40), process.argv[3])]));"
    )
    result = subprocess.run(
        ["node", "-e", script, str(ROOT), str(repo), feed],
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout) == [None, True, None, bound]
