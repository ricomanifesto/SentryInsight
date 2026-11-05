"""Manual job isolation and fixed-clock-before-secret workflow contract."""

import json
from pathlib import Path

import yaml


def test_closed_timing_and_no_model_job_share_no_secret_or_automatic_trigger():
    value = yaml.load(
        Path(".github/workflows/verify-nemotron.yml").read_text(),
        Loader=yaml.BaseLoader,
    )
    assert set(value["on"]) == {"workflow_dispatch"}
    assert value["permissions"] == {"contents": "write"}
    job = value["jobs"]["canary"]
    assert job["timeout-minutes"] == "40"
    steps = job["steps"]
    clock = next(
        i
        for i, row in enumerate(steps)
        if "anchor_canary_clock.py" in row.get("run", "")
    )
    setup = next(
        i for i, row in enumerate(steps) if "setup-node" in row.get("uses", "")
    )
    secret = [i for i, row in enumerate(steps) if "secrets." in json.dumps(row)]
    assert clock < setup < secret[0] and len(secret) == 1
    assert "!inputs.readmit_original" in job["if"]
    assert steps[-1]["timeout-minutes"] == "1"
    assert "artifact_gate.outputs.retain" in steps[-1]["if"]
    operator = value["jobs"]["readmit_original"]
    assert "inputs.readmit_original && !inputs.initialize_ledger" in operator["if"]
    assert "secrets." not in json.dumps(operator)
    assert "upload-artifact" not in json.dumps(operator)
    assert "readmit_original_canary.py" in json.dumps(operator)
    assert (
        json.loads(Path("config/original-canary-readmission.json").read_bytes())[
            "enabled"
        ]
        is False
    )
