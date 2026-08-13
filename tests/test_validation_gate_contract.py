from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_local_validation_checks_root_and_docs_report_markdown():
    script = (REPO_ROOT / "scripts" / "local_validation.sh").read_text()

    assert "scripts/validate_report.py index.md" in script
    assert "scripts/validate_report.py docs/index.md" in script


def test_generate_report_workflow_checks_root_and_docs_report_markdown():
    workflow = (REPO_ROOT / ".github" / "workflows" / "generate-report.yml").read_text()

    assert "scripts/validate_report.py index.md" in workflow
    assert "scripts/validate_report.py docs/index.md" in workflow


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
