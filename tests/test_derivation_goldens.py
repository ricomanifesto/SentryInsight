"""Packet, plan, prompt, resolved-report and archive outputs stay byte-identical."""

import json
import shutil

import pytest

from goldens.capture import GOLDEN, ROOT, capture, capture_archives


def test_derivations_match_frozen_goldens():
    expected = json.loads(GOLDEN.read_text())
    actual = capture(archive_names=expected["archived_reports"])
    assert actual["archived_reports"] == expected["archived_reports"]
    for name, entry in expected["eval_cases"].items():
        assert actual["eval_cases"][name] == entry, name
    assert actual == expected


def _frozen_reports(tmp_path):
    frozen = json.loads(GOLDEN.read_text())["archived_reports"]
    for name in frozen:
        shutil.copyfile(ROOT / "reports" / name, tmp_path / name)
    return frozen


def test_a_newly_archived_report_leaves_the_frozen_goldens_intact(tmp_path):
    # Normal generation archives the previous report under reports/; that new
    # file is not a frozen fixture and must not fail validation.
    frozen = _frozen_reports(tmp_path)
    newest = max(frozen)
    shutil.copyfile(tmp_path / newest, tmp_path / "2099-01-01.md")

    assert capture_archives(tmp_path, frozen) == frozen


def test_a_changed_frozen_archive_is_still_detected(tmp_path):
    frozen = _frozen_reports(tmp_path)
    oldest = min(frozen)
    path = tmp_path / oldest
    path.write_text(path.read_text() + "\n")

    assert capture_archives(tmp_path, frozen)[oldest] != frozen[oldest]


def test_a_missing_frozen_archive_fails(tmp_path):
    frozen = _frozen_reports(tmp_path)
    (tmp_path / min(frozen)).unlink()

    with pytest.raises(FileNotFoundError):
        capture_archives(tmp_path, frozen)
