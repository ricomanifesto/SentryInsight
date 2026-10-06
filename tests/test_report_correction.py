import hashlib

import pytest

from scripts.correct_report import apply_correction


def spec(source):
    return {
        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "replacements": [{"before": "wrong claim", "after": "supported claim"}],
    }


def test_correction_is_deterministic_idempotent_and_rejects_other_reports():
    original = "date stays\nwrong claim\nunrelated stays\n"
    correction = spec(original)
    corrected = apply_correction(original, correction)
    assert corrected == "date stays\nsupported claim\nunrelated stays\n"
    assert apply_correction(corrected, correction) == corrected
    with pytest.raises(ValueError, match="fingerprint"):
        apply_correction(original + "new report", correction)


def test_correction_rejects_ambiguous_replacements():
    original = "wrong claim wrong claim"
    with pytest.raises(ValueError, match="exactly once"):
        apply_correction(original, spec(original))
