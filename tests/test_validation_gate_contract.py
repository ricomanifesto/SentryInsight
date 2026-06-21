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
