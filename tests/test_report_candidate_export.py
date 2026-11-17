"""A failed browser check can retain the exact, bounded generated report."""

import hashlib
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys

import pytest

from src.core.failure_receipt import make_receipt, write_receipt
from src.core.reviewed_report import resolve_reviewed_analysis
from src.core.source_review import PLAN_KEY
from test_report_artifact import REPORT
from test_reviewed_report import prepared_result

REVISION = "a" * 40


@pytest.fixture
def candidate_case(tmp_path):
    root = tmp_path / "report"
    root.mkdir()
    result = prepared_result()
    candidate = resolve_reviewed_analysis(result)
    data = candidate.source.encode()
    (root / "index.md").write_bytes(data)
    (root / ".env").write_text("private-key-marker")
    (root / "source-snapshot.json").write_text("private-article-marker")
    receipt = tmp_path / "outcome.json"
    write_receipt(
        receipt,
        make_receipt(
            {
                "status": "completed",
                "report_generated": True,
                PLAN_KEY: result[PLAN_KEY],
            },
            environ={
                "GITHUB_RUN_ID": "123",
                "GITHUB_RUN_ATTEMPT": "1",
                "GITHUB_SHA": REVISION,
                "SENTRYINSIGHT_ADMISSION_KEY": "run:123",
            },
        ),
    )
    return {
        "report_root": root,
        "receipt_path": receipt,
        "output": tmp_path / "candidate",
        "run_id": "123",
        "run_attempt": "1",
        "source_revision": REVISION,
    }, data


def exporter():
    return importlib.import_module("scripts.export_report_candidate")


def test_exports_exact_markdown_and_only_a_bound_manifest(candidate_case):
    options, data = candidate_case
    manifest = exporter().export_candidate(**options)
    output = options["output"]
    assert {p.name for p in output.iterdir()} == {"index.md", "manifest.json"}
    assert (output / "index.md").read_bytes() == data
    assert json.loads((output / "manifest.json").read_text()) == manifest
    assert manifest == {
        "schema_version": 1,
        "kind": "unpublished-report-candidate",
        "publication_authority": False,
        "run_id": "123",
        "run_attempt": "1",
        "source_revision": REVISION,
        "plan_id": json.loads(options["receipt_path"].read_text())["plan_id"],
        "report_sha256": hashlib.sha256(data).hexdigest(),
        "report_bytes": len(data),
        "generated_at": "2026-11-02T12:00:00Z",
    }
    assert "private-" not in (output / "manifest.json").read_text()
    assert output.stat().st_mode & 0o077 == 0
    assert all(p.stat().st_mode & 0o077 == 0 for p in output.iterdir())


@pytest.mark.parametrize(
    "field,value",
    [("run_id", "124"), ("run_attempt", "2"), ("source_revision", "b" * 40)],
)
def test_mismatched_run_identity_exports_nothing(candidate_case, field, value):
    options, data = candidate_case
    options[field] = value
    with pytest.raises(exporter().CandidateExportError):
        exporter().export_candidate(**options)
    assert not options["output"].exists()
    assert (options["report_root"] / "index.md").read_bytes() == data


@pytest.mark.parametrize("change", ["not-generated", "failed", "plan", "diagnostic"])
def test_stale_or_unconfirmed_generation_exports_nothing(candidate_case, change):
    options, _ = candidate_case
    receipt = json.loads(options["receipt_path"].read_text())
    if change == "not-generated":
        receipt["report_generated"] = False
    elif change == "failed":
        receipt["status"] = "failed"
    elif change == "plan":
        receipt["plan_id"] = "b" * 64
    else:
        receipt["diagnostic"] = {
            "stage": "report_content",
            "codes": ["missing_expected_cves"],
        }
    options["receipt_path"].write_text(json.dumps(receipt))
    with pytest.raises(exporter().CandidateExportError):
        exporter().export_candidate(**options)
    assert not options["output"].exists()


@pytest.mark.parametrize(
    "kind", ["report", "receipt", "root", "output-parent", "output"]
)
def test_symlinks_are_never_followed(candidate_case, tmp_path, kind):
    options, data = candidate_case
    if kind == "report":
        source = options["report_root"] / "index.md"
    elif kind == "receipt":
        source = options["receipt_path"]
    elif kind == "root":
        source = options["report_root"]
    else:
        outside = tmp_path / "outside"
        outside.mkdir()
        (outside / "marker").write_text("preserve")
        link = tmp_path / "alias"
        link.symlink_to(outside, target_is_directory=True)
        options["output"] = link / "candidate" if kind == "output-parent" else link
        with pytest.raises(exporter().CandidateExportError):
            exporter().export_candidate(**options)
        assert (outside / "marker").read_text() == "preserve"
        assert not (outside / "index.md").exists()
        return
    original = source.with_name(source.name + ".original")
    source.rename(original)
    source.symlink_to(original, target_is_directory=kind == "root")
    with pytest.raises(exporter().CandidateExportError):
        exporter().export_candidate(**options)
    assert not options["output"].exists()
    if kind == "report":
        assert original.read_bytes() == data


@pytest.mark.parametrize(
    "kind", ["large", "directory", "fifo", "hardlink", "historical", "active-content"]
)
def test_unsafe_or_unsupported_report_exports_nothing(candidate_case, kind):
    options, data = candidate_case
    source = options["report_root"] / "index.md"
    module = exporter()
    if kind == "large":
        source.write_bytes(b"x" * (module.MAX_REPORT_BYTES + 1))
    elif kind in {"directory", "fifo"}:
        source.unlink()
        source.mkdir() if kind == "directory" else os.mkfifo(source)
    elif kind == "hardlink":
        os.link(source, source.with_name("alias.md"))
    elif kind == "historical":
        source.write_text(REPORT)
    else:
        source.write_bytes(
            data.replace(
                b"# Exploitation Report",
                b"# Exploitation Report\n<script>private-marker</script>",
            )
        )
    with pytest.raises(module.CandidateExportError):
        module.export_candidate(**options)
    assert not options["output"].exists()


def test_report_limit_is_inclusive_and_preserves_bytes(candidate_case):
    options, data = candidate_case
    module = exporter()
    data += b"\n" * (module.MAX_REPORT_BYTES - len(data))
    (options["report_root"] / "index.md").write_bytes(data)
    module.export_candidate(**options)
    assert (options["output"] / "index.md").read_bytes() == data


def test_completed_partial_report_keeps_its_review_metadata(candidate_case):
    from src.core.report_artifact import parse_report_artifact

    options, data = candidate_case
    receipt = json.loads(options["receipt_path"].read_text())
    receipt["status"] = "completed_with_review"
    write_receipt(options["receipt_path"], receipt)
    exporter().export_candidate(**options)
    retained = (options["output"] / "index.md").read_bytes()
    assert retained == data
    coverage = parse_report_artifact(retained.decode()).source_coverage
    assert coverage is not None
    assert coverage["counts"]["review_required_sources"] == 1


def test_existing_output_is_never_overwritten(candidate_case):
    options, _ = candidate_case
    options["output"].mkdir()
    marker = options["output"] / "manifest.json"
    marker.write_text("preserve")
    with pytest.raises(exporter().CandidateExportError):
        exporter().export_candidate(**options)
    assert marker.read_text() == "preserve"


def test_write_failure_leaves_no_complete_candidate(candidate_case, monkeypatch):
    options, data = candidate_case
    module = exporter()

    def fail(_):
        raise OSError("private-error-marker")

    monkeypatch.setattr(module.os, "fsync", fail)
    with pytest.raises(module.CandidateExportError):
        module.export_candidate(**options)
    assert not options["output"].exists()
    assert (options["report_root"] / "index.md").read_bytes() == data


def test_workflow_retains_candidate_before_browser_checks_without_release_authority():
    workflow = Path(".github/workflows/generate-report.yml").read_text()
    export = workflow.split("- name: Export bounded report candidate", 1)[1].split(
        "- name:", 1
    )[0]
    upload = workflow.split("- name: Retain report candidate for seven days", 1)[
        1
    ].split("- name:", 1)[0]
    assert "steps.generate.outcome == 'success'" in export
    assert "steps.generate.outputs.report_generated == 'true'" in export
    assert "scripts/export_report_candidate.py" in export
    assert "SOURCE_REVISION: ${{ steps.source.outputs.revision }}" in export
    assert "steps.candidate-export.outcome == 'success'" in upload
    assert "retention-days: 7" in upload
    assert "path: ${{ runner.temp }}/report-candidate" in upload
    assert "path: |" not in upload
    assert workflow.index(
        "- name: Retain report candidate for seven days"
    ) < workflow.index("- name: Validate report content before publishing")
    commit = workflow.split("- name: Commit and push updated report", 1)[1].split(
        "- name:", 1
    )[0]
    assert "if: success()" in commit


def test_cli_refusal_is_bounded_and_does_not_print_report_or_paths(candidate_case):
    options, _ = candidate_case
    command = [sys.executable, "-B", "scripts/export_report_candidate.py"]
    for name, value in options.items():
        command.extend(["--" + name.replace("_", "-"), str(value)])
    command[command.index("--run-id") + 1] = "124"
    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 1
    assert result.stdout.strip() == "Candidate export refused."
    assert result.stderr == ""
