"""CI exports only validated metadata and never calls last-good a new report."""

import json
from pathlib import Path

import pytest

from src.core.review_delivery import package_review, write_run_outcome
from src.core.source_review import (
    PLAN_KEY,
    SourceReviewError,
    prepare_source_review,
    write_review_packet,
)
from test_version_references import source


def run_state(tmp_path):
    plan = prepare_source_review([source("An advisory.", "good")])
    write_review_packet(plan.packet, tmp_path / ".sentryinsight-review")
    return {
        PLAN_KEY: plan.packet,
        "status": "completed_with_review",
        "report_generated": True,
    }


def test_package_carries_validated_metadata_without_bodies_or_unrelated_files(tmp_path):
    state = run_state(tmp_path)
    write_run_outcome(state, tmp_path)
    (tmp_path / "raw-response.log").write_text("never export")
    target = tmp_path / "package"
    package_review(tmp_path, target)
    assert sorted(path.name for path in target.iterdir()) == [
        state[PLAN_KEY]["plan_id"] + ".json",
        "outcome.json",
    ]
    combined = "".join(path.read_text() for path in target.iterdir())
    assert "An advisory." not in combined
    assert "never export" not in combined


@pytest.mark.parametrize(
    "fault",
    ["extra", "malformed", "symlink", "permissions", "wrong_name", "missing_plan"],
)
def test_package_fails_closed_for_invalid_queue_or_missing_active_plan(tmp_path, fault):
    state = run_state(tmp_path)
    write_run_outcome(state, tmp_path)
    queue = tmp_path / ".sentryinsight-review"
    packet = next(queue.iterdir())
    if fault == "extra":
        (queue / "raw.txt").write_text("not metadata")
    elif fault == "malformed":
        data = json.loads(packet.read_text())
        data["raw_model"] = "not metadata"
        packet.write_text(json.dumps(data))
    elif fault == "symlink":
        packet.unlink()
        packet.symlink_to(tmp_path / "missing")
    elif fault == "permissions":
        packet.chmod(0o644)
    elif fault == "wrong_name":
        packet.rename(queue / ("0" * 64 + ".json"))
    else:
        packet.unlink()
    with pytest.raises(SourceReviewError):
        package_review(tmp_path, tmp_path / "package")
    assert not (tmp_path / "package").exists()


def test_failure_before_plan_produces_fixed_no_valid_plan_outcome(tmp_path):
    result = write_run_outcome(None, tmp_path)
    assert result == {
        "schema_version": 1,
        "status": "failed",
        "report_generated": False,
        "plan_id": None,
        "outcome": "no_valid_plan",
    }
    package_review(tmp_path, tmp_path / "package")
    assert sorted(path.name for path in (tmp_path / "package").iterdir()) == [
        "outcome.json"
    ]


@pytest.mark.parametrize(
    "status",
    ["review_required", "completed_unchanged", "failed", "completed_with_warnings"],
)
def test_old_report_is_never_labelled_generated(status, tmp_path):
    state = run_state(tmp_path)
    state["status"] = status
    result = write_run_outcome(state, tmp_path)
    assert result["report_generated"] is False


def test_ci_gates_publication_on_generation_and_valid_review_delivery():
    text = Path(".github/workflows/generate-report.yml").read_text()
    assert "id: generate" in text
    assert "retention-days: 90" in text
    assert "scripts/review_sources.py package" in text
    commit = text.split("- name: Commit and push updated report", 1)[1]
    assert "steps.generate.outputs.report_generated == 'true'" in commit
    assert "steps.source-review-summary.outcome == 'success'" in commit
    evidence = text.split("- name: Upload rendered report evidence", 1)[1].split(
        "- name:", 1
    )[0]
    assert "steps.generate.outputs.report_generated == 'true'" in evidence
