from pathlib import Path

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
    assert "astral-sh/setup-uv@v6" in workflow
    assert "actions/setup-node@v6" in workflow
    assert "npm ci" in workflow
    assert "npx playwright install --with-deps chromium" in workflow
    assert "bash scripts/local_validation.sh" in workflow
    assert "actions/upload-artifact@v4" in workflow
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
    assert "npx playwright install --with-deps chromium" in workflow
    assert workflow.index(
        "npx playwright install --with-deps chromium"
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
