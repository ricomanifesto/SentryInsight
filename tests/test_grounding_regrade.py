import asyncio
import json

import pytest

from evals.grounding.dataset import load_cases
from evals.grounding.regrade import regrade_saved_run
from evals.grounding.runner import run_evaluation


@pytest.fixture
def saved_run(tmp_path):
    case = load_cases()[0]

    async def task(inputs):
        if inputs.variant == "checklist":
            raise TimeoutError("not retained")
        return case.reference_report

    path = tmp_path / "original"
    asyncio.run(run_evaluation([case], task=task, output=path, repetitions=1))
    return path


def mutate(path, filename, operation):
    file = path / filename
    data = json.loads(file.read_text())
    operation(data)
    file.write_text(json.dumps(data))


def test_regrade_retains_originals_and_reports_error_denominators(saved_run, tmp_path):
    before = {p.name: p.read_bytes() for p in saved_run.iterdir()}
    output = tmp_path / "v2"
    summary = regrade_saved_run(saved_run, output)
    assert before == {p.name: p.read_bytes() for p in saved_run.iterdir()}
    assert summary["planned"] == 2
    assert summary["execution_errors"] == 1
    assert summary["field_pass_trials"] == 1
    assert summary["narrative_review_required"] == 1
    assert summary["checks"]["exploitation_status"] == {
        "pass": 1,
        "fail": 0,
        "not_evaluated": 1,
        "planned": 2,
    }
    rows = json.loads((output / "graded.json").read_text())
    assert rows[0]["original"] == json.loads((saved_run / "graded.json").read_text())[0]
    assert rows[1]["grade"]["checks"]["well_formed"]["state"] == "not_evaluated"
    manifest = json.loads((output / "manifest.json").read_text())
    assert manifest["complete"] and manifest["model_calls"] == 0
    assert manifest["input_files"]["trials.jsonl"]
    assert manifest["grader_files"]["evals/grounding/grading.py"]
    with pytest.raises(FileExistsError):
        regrade_saved_run(saved_run, output)


@pytest.mark.parametrize(
    "filename,operation",
    [
        ("manifest.json", lambda d: d.update(complete=False)),
        ("manifest.json", lambda d: d.update(planned=3)),
        ("manifest.json", lambda d: d["trial_ids"].append(d["trial_ids"][0])),
        ("manifest.json", lambda d: d.update(dataset_sha256="changed")),
        (
            "manifest.json",
            lambda d: d["source_files"].update(
                {"evals/grounding/data/answers.json": "changed"}
            ),
        ),
        ("graded.json", lambda d: d[0].update(report="changed")),
        ("graded.json", lambda d: d[0].update(input_sha256="changed")),
        ("graded.json", lambda d: d[0].update(split="holdout")),
        ("graded.json", lambda d: d[0]["checks"].update(exploitation_status=False)),
        ("graded.json", lambda d: d.append(d[0])),
    ],
)
def test_inconsistent_run_is_rejected_before_output_creation(
    saved_run, tmp_path, filename, operation
):
    mutate(saved_run, filename, operation)
    with pytest.raises(ValueError):
        regrade_saved_run(saved_run, tmp_path / "v2")
    assert not (tmp_path / "v2").exists()


def test_raw_trial_identity_cannot_be_replaced(saved_run, tmp_path):
    path = saved_run / "trials.jsonl"
    rows = [json.loads(line) for line in path.read_text().splitlines()]
    rows[0]["report"] = "changed"
    path.write_text("\n".join(json.dumps(row) for row in rows))
    with pytest.raises(ValueError):
        regrade_saved_run(saved_run, tmp_path / "v2")


def test_output_cannot_modify_original_run(saved_run):
    with pytest.raises(ValueError, match="outside"):
        regrade_saved_run(saved_run, saved_run / "v2")


def test_failure_during_final_verification_leaves_incomplete_receipt(
    saved_run, tmp_path, monkeypatch
):
    import evals.grounding.regrade as module

    snapshot = module.grader_snapshot()
    calls = iter([snapshot, {**snapshot, "changed": "yes"}])
    monkeypatch.setattr(module, "grader_snapshot", lambda: next(calls))
    output = tmp_path / "v2"
    with pytest.raises(RuntimeError, match="remains incomplete"):
        regrade_saved_run(saved_run, output)
    assert json.loads((output / "manifest.json").read_text())["complete"] is False
