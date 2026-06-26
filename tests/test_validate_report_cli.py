from pathlib import Path
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate_report.py"
SOURCE_ATTRIBUTION_FIXTURE = (
    REPO_ROOT / "tests" / "fixtures" / "source_attribution_report.md"
)


def run_validator(*args):
    return subprocess.run(
        [sys.executable, "-B", str(VALIDATOR), *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def test_validate_report_cli_accepts_expected_source_attribution_entries():
    result = run_validator(
        "--require-source-attribution",
        "--source-attribution-entry",
        "- **CISA: exploited KEV update**: Example Research - https://example.test/kev",
        "--source-attribution-entry",
        "- **Parenthesized URL report**: Example Source - https://example.test/report(1)",
        "--source-attribution-entry",
        "- **Source-only exploitation report**: Example Source",
        str(SOURCE_ATTRIBUTION_FIXTURE),
    )

    assert result.returncode == 0
    assert "Report content validation passed" in result.stdout


def test_validate_report_cli_rejects_missing_source_attribution_entries():
    result = run_validator(
        "--require-source-attribution",
        "--source-attribution-entry",
        "- **Missing report**: Example Source - https://example.test/missing",
        str(SOURCE_ATTRIBUTION_FIXTURE),
    )

    assert result.returncode == 1
    assert "missing_source_attribution" in result.stdout
