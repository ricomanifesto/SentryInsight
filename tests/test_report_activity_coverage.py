"""Independent body-to-rollup coverage contracts; source grounding stays separate."""

import json
from pathlib import Path
import subprocess
import sys

import pytest

from src.core.finding_evidence import EvidenceError, validate_finding_evidence
from src.core.report_activity_coverage import _partition
from src.core.report_validation import validate_report_content
from src.core.reporting import resolve_reporting_keys
from test_finding_generation import catalog_for, render

CASES = json.loads(
    (Path(__file__).parent / "fixtures/report_activity_coverage.json").read_text()
)["cases"]
REPO = Path(__file__).resolve().parents[1]
CODE = "underpopulated_threat_actor_activities"


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_complete_owned_report_activity_coverage(case):
    issues = validate_report_content(case["markdown"])
    assert any(issue.code == CODE for issue in issues) == case["expected"][CODE]


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_standalone_cli_matches_api_on_identical_markdown(case, tmp_path):
    path = tmp_path / "report.md"
    path.write_text(case["markdown"])
    issues = validate_report_content(path.read_text())
    result = subprocess.run(
        [sys.executable, "-B", str(REPO / "scripts/validate_report.py"), str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == bool(issues), result.stderr
    assert (CODE in result.stdout) == any(issue.code == CODE for issue in issues)
    assert path.read_text() == case["markdown"]


def test_internal_coverage_never_certifies_fabricated_source_activity():
    catalog = catalog_for("Threat actors are not exploiting CVE-2026-1234.")
    _, report = render(catalog)
    fabricated = report.replace("are not exploiting", "are exploiting")
    assert fabricated != report
    assert not any(
        issue.code == CODE
        for issue in validate_report_content(
            resolve_reporting_keys(fabricated, catalog)
        )
    )
    with pytest.raises(EvidenceError):
        validate_finding_evidence(fabricated, catalog)


def test_repeated_atom_partition_has_bounded_ambiguity():
    assert (
        _partition(" ".join(["activity"] * 5000), {"activity", "activity activity"})
        is None
    )
    assert (
        _partition(" ".join(["activity"] * 5000), {"activity"}) == ("activity",) * 5000
    )


def test_noncanonical_unpadded_code_cannot_supply_coverage():
    case = next(c for c in CASES if c["id"] == "canonical-literal-encoding")
    report = case["markdown"].replace(
        "` Threat actors exploit *literal* service names. `",
        "`Threat actors exploit *literal* service names.`",
    )
    assert report != case["markdown"]
    assert any(issue.code == CODE for issue in validate_report_content(report))


@pytest.mark.parametrize(
    "url",
    [
        "https://",
        "https://example.test:bad/",
        "https://user:pass@example.test/",
        "/relative",
    ],
)
def test_malformed_reporting_identity_cannot_supply_coverage(url):
    case = next(c for c in CASES if c["id"] == "repeated-complete-literal")
    report = case["markdown"].replace("https://example.test/source-a", url)
    assert any(issue.code == CODE for issue in validate_report_content(report))
