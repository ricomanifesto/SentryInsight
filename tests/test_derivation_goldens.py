"""Packet, plan, prompt, resolved-report and archive outputs stay byte-identical."""

import json

from goldens.capture import GOLDEN, capture


def test_derivations_match_frozen_goldens():
    expected = json.loads(GOLDEN.read_text())
    actual = capture()
    assert actual["archived_reports"] == expected["archived_reports"]
    for name, entry in expected["eval_cases"].items():
        assert actual["eval_cases"][name] == entry, name
    assert actual == expected
