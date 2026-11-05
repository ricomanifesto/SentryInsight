"""One production model: the workflow default, config and code default agree.

The generation workflow's SENTRYINSIGHT_MODEL default overrides the config
file, so a model change must move all three together.
"""

import json
import re
from pathlib import Path

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
    [default] = re.findall(
        r"SENTRYINSIGHT_MODEL: \$\{\{ vars\.SENTRYINSIGHT_MODEL \|\| '([^']+)' \}\}",
        workflow,
    )
    assert default == DEFAULT_MODEL
