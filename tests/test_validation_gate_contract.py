import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_local_validation_checks_canonical_report_and_generated_site():
    script = (REPO_ROOT / "scripts" / "local_validation.sh").read_text()

    assert "scripts/validate_report.py index.md" in script
    assert "scripts/build_site.py --check" in script
    assert "scripts/package_pages.py" in script
    assert "docs/index.md" not in script


def test_generate_report_workflow_checks_canonical_report_and_generated_site():
    workflow = (REPO_ROOT / ".github" / "workflows" / "generate-report.yml").read_text()

    assert "scripts/validate_report.py index.md" in workflow
    assert "scripts/build_site.py --check" in workflow
    assert "scripts/validate_report.py docs/index.md" not in workflow


def test_validation_and_generation_use_the_owner_reporting_identity_verifier():
    verifier = "contracts/reporting-identity-verifier-v1.py"
    for workflow_name in ("validate.yml", "generate-report.yml"):
        workflow = (REPO_ROOT / ".github" / "workflows" / workflow_name).read_text()
        assert "Fetch canonical reporting identity verifier" in workflow
        assert "Check reporting identity verifier drift" in workflow
        assert "Fetch canonical reporting identity contract" in workflow
        assert "Check reporting identity contract drift" in workflow
        assert workflow.count(f"python3 {verifier} fetch") == 2
        assert workflow.count(f"python3 {verifier} compare") == 2
        assert "--artifact verifier" in workflow
        assert "--artifact contract" in workflow
        assert "curl " not in workflow
        assert "cmp -s" not in workflow
        assert workflow.index("Set up Python") < workflow.index(
            "Fetch canonical reporting identity verifier"
        )
        assert workflow.index(
            "Fetch canonical reporting identity verifier"
        ) < workflow.index("Check reporting identity verifier drift")
        assert workflow.index(
            "Fetch canonical reporting identity contract"
        ) < workflow.index("Check reporting identity contract drift")


def test_generate_report_workflow_stages_canonical_site_without_audio_or_docs():
    workflow = (REPO_ROOT / ".github" / "workflows" / "generate-report.yml").read_text()

    assert (
        "git add -f index.md index.html current-findings.json sitemap.xml" in workflow
    )
    assert "git add -f reports/" in workflow
    assert "git add -f assets/site.css assets/report.js assets/vendor/" in workflow
    assert "executive_summary.mp3" not in workflow
    assert "docs/" not in workflow
    assert "ELEVENLABS_API_KEY" not in workflow


def test_generate_report_workflow_skips_noop_report_pushes():
    workflow = (REPO_ROOT / ".github" / "workflows" / "generate-report.yml").read_text()

    assert "git diff --cached --quiet" in workflow
    assert 'echo "No report changes to commit"' in workflow
    assert "exit 0" in workflow
    assert 'git commit -m "Update exploitation report [automated]" ||' not in workflow


def test_generate_report_workflow_rebases_before_report_push():
    workflow = (REPO_ROOT / ".github" / "workflows" / "generate-report.yml").read_text()

    assert "git pull --rebase origin main" in workflow
    assert "HEAD:main" in workflow


def test_generate_report_workflow_serializes_provider_calls_and_publication():
    workflow = (REPO_ROOT / ".github" / "workflows" / "generate-report.yml").read_text()

    assert "concurrency:" in workflow
    assert "group: sentryinsight-report-generation" in workflow
    assert "cancel-in-progress: false" in workflow


def test_pull_requests_run_the_full_local_validation_gate():
    workflow = (REPO_ROOT / ".github" / "workflows" / "validate.yml").read_text()

    assert "pull_request:" in workflow
    assert "actions/setup-python@v6" in workflow
    assert "astral-sh/setup-uv@eb1897b8dc4b5d5bfe39a428a8f2304605e0983c" in workflow
    assert "actions/setup-node@v6" in workflow
    assert "npm ci" in workflow
    assert 'require("@playwright/test").chromium.launch()' in workflow
    assert "bash scripts/local_validation.sh" in workflow
    assert (
        "actions/upload-artifact@b7c566a772e6b6bfb58ed0dc250532a479d7789f" in workflow
    )
    assert "test-results/screenshots" in workflow
    assert "id: report-evidence" in workflow
    assert "steps.report-evidence.outputs.artifact-url" in workflow
    assert "GITHUB_STEP_SUMMARY" in workflow
    assert "Rendered report review" in workflow


def test_generation_workflow_installs_the_locked_browser_runtime_before_validation():
    workflow = (REPO_ROOT / ".github" / "workflows" / "generate-report.yml").read_text()

    assert "actions/setup-node@v6" in workflow
    assert "cache: npm" in workflow
    assert "npm ci" in workflow
    assert 'require("@playwright/test").chromium.launch()' in workflow
    assert workflow.index(
        'require("@playwright/test").chromium.launch()'
    ) < workflow.index("bash scripts/local_validation.sh")
    generation_step = workflow.index("uv run python main.py")
    final_browser_step = workflow.rindex("npm run test:browser")
    assert generation_step < final_browser_step
    assert "actions/upload-artifact@v4" in workflow
    assert "test-results/screenshots" in workflow
    assert "id: generated-report-evidence" in workflow
    assert "steps.generated-report-evidence.outputs.artifact-url" in workflow
    assert "GITHUB_STEP_SUMMARY" in workflow


def test_pages_workflow_deploys_only_a_packaged_artifact_after_validation():
    workflow = (REPO_ROOT / ".github" / "workflows" / "deploy-pages.yml").read_text()

    assert "workflow_run:" in workflow
    assert 'workflows: ["Validate"]' in workflow
    assert "github.event.workflow_run.conclusion == 'success'" in workflow
    assert "github.event.workflow_run.head_sha" in workflow
    assert "scripts/package_pages.py --output" in workflow
    assert "actions/configure-pages@v6" in workflow
    assert "actions/upload-pages-artifact@v5" in workflow
    assert "actions/deploy-pages@v5" in workflow
    assert "pages: write" in workflow
    assert "id-token: write" in workflow


@pytest.mark.parametrize(
    "workflow_name", ["validate", "generate-report", "publish-production"]
)
def test_browser_jobs_use_version_matched_immutable_official_runtime(workflow_name):
    workflow = (
        REPO_ROOT / ".github" / "workflows" / f"{workflow_name}.yml"
    ).read_text()
    package = json.loads((REPO_ROOT / "package.json").read_text())
    lock = json.loads((REPO_ROOT / "package-lock.json").read_text())
    version = package["devDependencies"]["@playwright/test"]
    assert version == "1.62.1"
    for name in ("@playwright/test", "playwright", "playwright-core"):
        assert lock["packages"][f"node_modules/{name}"]["version"] == version
    # Verified official MCR OCI index for this exact Playwright release.
    digest = "dcc5531e97840b9b5e794f2814476b21571c5124a3fca2267d73041f56e7580e"
    assert (
        f"      image: mcr.microsoft.com/playwright:v{version}-noble@sha256:{digest}"
        in workflow
    )
    assert "    container:\n" in workflow
    assert "    defaults:\n      run:\n        shell: bash\n" in workflow
    container_settings = workflow.split("    container:\n", 1)[1].split(
        "    defaults:", 1
    )[0]
    assert "options:" not in container_settings
    assert "prepare_ubuntu_mirror" not in workflow
    assert "playwright install" not in workflow
    assert "apt-get" not in workflow
    assert "actions/setup-python@v6" in workflow
    assert "python-version: '3.11'" in workflow
    assert "astral-sh/setup-uv@" in workflow
    assert "actions/setup-node@v6" in workflow
    assert "node-version: '24'" in workflow
    smoke = (
        'node -e \'require("@playwright/test").chromium.launch()'
        ".then(browser => browser.close())"
        ".catch(error => { console.error(error); process.exit(1); })'"
    )
    assert smoke in workflow
    assert workflow.index("npm ci") < workflow.index(smoke)
    assert workflow.index(smoke) < workflow.index("bash scripts/local_validation.sh")


def test_container_runtime_preserves_full_validation_and_publisher_bash_semantics():
    validation = (REPO_ROOT / "scripts" / "local_validation.sh").read_text()
    for gate in (
        "set -euo pipefail",
        "uv sync --group dev --frozen",
        "uv run ruff check .",
        "uv run black --check .",
        "uv run ty check",
        "-m pytest tests -q -p no:cacheprovider",
        "scripts/validate_report.py index.md",
        "scripts/build_site.py --check",
        "scripts/package_pages.py",
        "npm ci",
        "npm run test:browser",
    ):
        assert gate in validation
    publisher = (
        REPO_ROOT / ".github" / "workflows" / "publish-production.yml"
    ).read_text()
    assert "source .venv/bin/activate" in publisher
    assert "uv sync --group dev --frozen" in publisher
    assert "if: github.event_name != 'workflow_run'" in publisher
    assert "node publication/cli.js" in publisher
    generation = (
        REPO_ROOT / ".github" / "workflows" / "generate-report.yml"
    ).read_text()
    assert "if: steps.validated.outputs.passed != 'true'" in generation


def test_generation_lookup_uses_existing_python_and_fail_closed_output():
    generation = (REPO_ROOT / ".github/workflows/generate-report.yml").read_text()
    assert "run: python3 -B scripts/find_validated_commit.py" in generation
    helper = (REPO_ROOT / "scripts/find_validated_commit.py").read_text()
    assert "except Exception:" in helper
    assert "return False" in helper.split("except Exception:")[1]
    assert "passed={str(passed).lower()}" in helper
    assert "if: steps.validated.outputs.passed != 'true'" in generation
