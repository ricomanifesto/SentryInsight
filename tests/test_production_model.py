"""One production model: the workflow default, config and code default agree.

The generation workflow's SENTRYINSIGHT_MODEL default overrides the config
file, so a model change must move all three together.
"""

import json
import re
import subprocess
from pathlib import Path

import pytest

from src.core.model_config import DEFAULT_MODEL

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_MODEL = "openrouter/nvidia/nemotron-3.5-super-vl:free"


def test_production_model_is_the_healthy_free_route():
    assert DEFAULT_MODEL == PRODUCTION_MODEL
    assert PRODUCTION_MODEL.endswith(":free")


def test_config_and_workflow_default_match_the_code_default():
    config = json.loads((ROOT / "config/config.json").read_text())
    assert config["analysis"]["model"] == DEFAULT_MODEL
    workflow = (ROOT / ".github/workflows/generate-report.yml").read_text()
    defaults = re.findall(
        r"vars\.SENTRYINSIGHT_MODEL \|\| '([^']+)'",
        workflow,
    )
    assert len(defaults) == 2  # admission and generation
    assert set(defaults) == {DEFAULT_MODEL}


def admit_step():
    workflow = (ROOT / ".github/workflows/generate-report.yml").read_text()
    start = workflow.index("      - name: Admit generation")
    return workflow[start : workflow.index("\n      - name:", start + 1)]


def test_free_route_failures_never_block_the_next_generation():
    step = admit_step()
    assert "GENERATION_MODEL: ${{ vars.SENTRYINSIGHT_MODEL ||" in step
    assert 'case "$GENERATION_MODEL" in *:free) READMIT=true ;; esac' in step
    assert step.index("READMIT=true ;; esac") < step.index(
        "node publication/cli.js admit"
    )
    assert '--readmit "$READMIT"' in step


@pytest.mark.parametrize(
    ("model", "requested", "readmit"),
    [
        ("openrouter/nvidia/nemotron-3.5-super-vl:free", "false", "true"),
        ("openrouter/moonshotai/kimi-k3.1-pro", "false", "false"),
        ("openrouter/moonshotai/kimi-k3.1-pro", "true", "true"),
    ],
)
def test_only_free_routes_readmit_automatically(model, requested, readmit):
    script = (
        'case "$GENERATION_MODEL" in *:free) READMIT=true ;; esac; printf %s "$READMIT"'
    )
    result = subprocess.run(
        ["bash", "-c", script],
        env={"GENERATION_MODEL": model, "READMIT": requested, "PATH": "/usr/bin:/bin"},
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout == readmit
