"""Recognition diagnostic categories never include compared source values."""

from copy import deepcopy
import json

import pytest

from scripts import verify_grc_workflow_once as trial
from test_grc_analysis_contract import sources, row_from_prompt
import test_grc_analysis_contract as analysis_cases
import test_grc_full_trial as cases

contract = analysis_cases.contract
layout, prepared = cases.layout, cases.prepared
SENTINEL = "PRIVATE_SOURCE_TITLE_REASON_KEY_SENTINEL"


@pytest.mark.parametrize(
    "condition,code",
    [
        ("wrapper", "gate_wrapper"),
        ("fence", "gate_wrapper"),
        ("format", "gate_format"),
        ("binding", "gate_binding"),
        ("duplicate", "gate_duplicate"),
        ("score", "gate_score"),
        ("supplier", "gate_supplier"),
        ("shape", "gate_parsed_shape"),
        ("categories", "gate_categories"),
    ],
)
def test_observed_gate_condition_has_only_a_closed_code(contract, condition, code):
    items = sources(contract)
    prompt = contract.service._create_analysis_prompt(items)
    one, two = [
        row_from_prompt(prompt, i, item.title) for i, item in enumerate(items, 1)
    ]
    parsed = contract.service._process_analysis_response(two, items)
    text = two
    if condition == "wrapper":
        text = "# " + two
    elif condition == "fence":
        text = "```text\n" + two + "\n```"
    elif condition == "format":
        text = two + " because " + SENTINEL
    elif condition == "binding":
        text = two.replace(items[1].title, SENTINEL)
    elif condition == "duplicate":
        text = two + "\n" + two
    elif condition == "score":
        text = two.replace("score 8", "score 0")
    elif condition == "supplier":
        text = one
        parsed = contract.service._process_analysis_response(one, items)
    elif condition == "shape":
        parsed["summary"]["grc_relevant_count"] = 2
    else:
        parsed["analysis"]["regulations_mentioned"] = SENTINEL
    with pytest.raises(contract.observer.CheckRefused) as error:
        contract.observer.recognized_analysis(text, items, parsed)
    assert error.value.code == code
    trace = contract.observer.WorkerTrace("analysis")
    trace.phase = "worker_recognition_gate"
    trace.capture(error.value)
    record = trace.primary
    assert record == trial.diagnostics.record(
        "analysis", "worker_recognition_gate", code
    )
    assert SENTINEL not in json.dumps(record) + str(error.value)
    with pytest.raises(trial.TrialFailure) as parent:
        trial.worker_envelope({"diagnostic_version": 1, "error": record}, "derive")
    assert parent.value.diagnostic == record


@pytest.mark.parametrize(
    "stage,phase",
    [
        ("plan", "worker_recognition_gate"),
        ("calibration", "worker_recognition_gate"),
        ("analysis", "worker_analysis_parser"),
        ("analysis", "worker_host_validation"),
        ("analysis", "worker_import"),
    ],
)
def test_gate_codes_are_invalid_outside_the_analysis_recognition_boundary(stage, phase):
    with pytest.raises(ValueError):
        trial.diagnostics.record(stage, phase, "gate_wrapper")
    envelope = {
        "diagnostic_version": 1,
        "error": {"stage": stage, "phase": phase, "code": "gate_wrapper"},
    }
    with pytest.raises(trial.TrialFailure) as error:
        trial.worker_envelope(envelope, "derive")
    assert error.value.diagnostic["code"] == "invalid_worker_envelope"


@pytest.mark.parametrize("mutation", ["unknown", "extra", "mixed"])
def test_gate_envelope_never_admits_unknown_or_raw_fields(mutation):
    envelope = {
        "diagnostic_version": 1,
        "error": {
            "stage": "analysis",
            "phase": "worker_recognition_gate",
            "code": "gate_wrapper",
        },
    }
    if mutation == "unknown":
        envelope["error"]["code"] = SENTINEL
    elif mutation == "extra":
        envelope["error"]["observed_title"] = SENTINEL
    else:
        envelope["result"] = {"answer": SENTINEL}
    with pytest.raises(trial.TrialFailure) as error:
        trial.worker_envelope(envelope, "derive")
    assert error.value.diagnostic["code"] == "invalid_worker_envelope"
    assert SENTINEL not in str(error.value) + json.dumps(error.value.diagnostic)


@pytest.mark.parametrize("style", ["heading", "fence", "table"])
def test_real_worker_gate_code_stops_after_one_fully_accounted_post(
    tmp_path, layout, prepared, style, capsys
):
    answer = cases.reply(layout, 0)
    content = answer["choices"][0]["message"]["content"]
    rows = content.splitlines()
    if style == "heading":
        content = rows[1] + "\n# " + rows[0]
    elif style == "table":
        content = rows[1] + "\n| Article 99: Title: Unknown source score 8 relevant |"
    else:
        content = "```text\n" + content + "\n```"
    answer["choices"][0]["message"]["content"] = content
    seen = []

    def handler(request):
        seen.append(request)
        return cases.streamed(deepcopy(answer))

    result = cases.run(tmp_path, layout, prepared, handler, lambda: SENTINEL)
    assert len(seen) == 1 and result["states"]["plan"] == "pending"
    assert result["operations"][0]["usage"]["cost"] == 0.007
    assert result["diagnostics"]["failure"] == trial.diagnostics.record(
        "analysis", "worker_recognition_gate", "gate_wrapper"
    )
    assert SENTINEL not in json.dumps(result)
    assert SENTINEL not in (tmp_path / "claim.json").read_text()
    captured = capsys.readouterr()
    assert SENTINEL not in captured.out + captured.err


def test_ordered_contract_reserved_row_stops_actual_two_stage_host_workflow(
    tmp_path, layout, prepared, capsys
):
    answer = cases.reply(layout, 0)
    rows = answer["choices"][0]["message"]["content"].splitlines()
    answer["choices"][0]["message"]["content"] = (
        rows[1] + "\nArticle X: Title: Risk summary score 8 relevant"
    )
    seen = []

    def handler(request):
        stage = len(seen)
        seen.append(request)
        return cases.streamed(
            deepcopy(answer) if stage == 0 else cases.reply(layout, 1)
        )

    result = cases.run(tmp_path, layout, prepared, handler, lambda: SENTINEL)
    assert len(seen) == 1 and result["states"]["plan"] == "pending"
    claim = json.loads((tmp_path / "claim.json").read_text())
    assert claim["requests"]["plan"]["wire_sha256"] is None
    assert claim["requests"]["plan"]["canonical_payload_sha256"] is None
    assert result["outcome"] == "stopped"
    assert result["host"] is None
    assert result["published"] is False and result["production_ready"] is False
    assert result["diagnostics"]["failure"] == trial.diagnostics.record(
        "analysis", "worker_recognition_gate", "gate_format"
    )
    assert result["operations"][0]["usage"]["cost"] == 0.007
    assert SENTINEL not in json.dumps(result) + json.dumps(claim)
    captured = capsys.readouterr()
    assert SENTINEL not in captured.out + captured.err
