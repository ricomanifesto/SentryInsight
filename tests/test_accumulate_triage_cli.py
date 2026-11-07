from __future__ import annotations

import json

import pytest

from scripts.accumulate_triage import main
from src.core import exploitation_triage as triage
from test_triage_accumulator import DROP, KEEP, published_report, receipt

ARTICLE = {"link": "https://example.com/cited", "title": "Cited", "source": "Ex"}
OTHER = {"link": "https://example.com/other", "title": "Other", "source": "Ex"}


def write(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")
    return path


@pytest.fixture
def repo(tmp_path):
    root = tmp_path / "repo"
    (root / "reports").mkdir(parents=True)
    (root / "reports" / "2026-08-13.md").write_text(
        published_report([ARTICLE]), encoding="utf-8"
    )
    receipts = tmp_path / "receipts"
    receipts.mkdir()
    write(
        receipts / "run-1.json",
        receipt([(triage.url_sha256(ARTICLE), DROP), (triage.url_sha256(OTHER), KEEP)]),
    )
    return root, receipts, tmp_path


def run(capsys, *args):
    code = main([str(arg) for arg in args])
    captured = capsys.readouterr()
    return code, captured.out, captured.err


def test_derives_published_hashes_from_report_links(repo, capsys):
    root, receipts, _ = repo
    code, out, _ = run(capsys, "--receipts", receipts, "--root", root)
    assert code == 0
    result = json.loads(out)
    assert result["counts"]["cited"] == 1
    assert result["counts"]["cited_and_dropped"] == 1
    assert result["counts"]["unique_decided"] == 2
    assert result["bounds"]["verdict"] == "no_plan"
    assert "example.com" not in out and "Cited" not in out


def test_explicit_published_list_and_plan(repo, capsys):
    root, receipts, tmp = repo
    published = write(tmp / "published.json", [triage.url_sha256(OTHER)])
    plan = write(
        tmp / "plan.json",
        {"epsilon_drop": 0.5, "epsilon_miss": 0.2, "delta": 0.05, "checkpoints": [25]},
    )
    code, out, _ = run(
        capsys,
        "--receipts",
        receipts / "run-1.json",
        "--published",
        published,
        "--plan",
        plan,
        "--root",
        root,
    )
    result = json.loads(out)
    assert code == 0
    assert result["counts"]["cited_and_dropped"] == 0
    assert result["bounds"]["verdict"] == "continue"


def test_ledger_is_write_once_and_update_is_idempotent(repo, capsys):
    root, receipts, tmp = repo
    ledger = tmp / "ledger.json"
    assert (
        run(capsys, "--receipts", receipts, "--root", root, "--ledger", ledger)[0] == 0
    )
    first = ledger.read_text()

    code, _, err = run(
        capsys, "--receipts", receipts, "--root", root, "--ledger", ledger
    )
    assert code == 2 and "--update" in err
    assert ledger.read_text() == first

    write(receipts / "run-2.json", receipt([(triage.url_sha256(OTHER), DROP)]))
    args = ("--receipts", receipts, "--root", root, "--ledger", ledger, "--update")
    assert run(capsys, *args)[0] == 0
    updated = json.loads(ledger.read_text())
    assert len(updated["runs"]) == 2
    assert updated["conflicting"] == 1
    assert run(capsys, *args)[0] == 0
    assert json.loads(ledger.read_text()) == updated
    text = ledger.read_text()
    assert "example.com" not in text and "Cited" not in text


def test_unknown_receipt_schema_is_refused(repo, capsys):
    root, receipts, _ = repo
    value = json.loads((receipts / "run-1.json").read_text())
    value["schema_version"] = 2
    write(receipts / "run-1.json", value)
    code, out, err = run(capsys, "--receipts", receipts, "--root", root)
    assert code == 2 and out == ""
    assert "schema_version" in err


def test_plan_is_registered_in_the_ledger_and_cannot_change(repo, capsys):
    root, receipts, tmp = repo
    ledger = tmp / "ledger.json"
    plan = {
        "epsilon_drop": 0.5,
        "epsilon_miss": 0.2,
        "delta": 0.05,
        "checkpoints": [1, 2],
    }
    plan_path = write(tmp / "plan.json", plan)
    base = ("--receipts", receipts, "--root", root, "--ledger", ledger)
    assert run(capsys, *base, "--plan", plan_path)[0] == 0
    stored = json.loads(ledger.read_text())
    assert stored["plan"] == plan
    assert stored["frozen"]["drop"] == [
        {"checkpoint": 1, "events": 1},
        {"checkpoint": 2, "events": 1},
    ]

    # Updates reuse the stored plan and keep reached looks frozen.
    write(receipts / "run-2.json", receipt([(triage.url_sha256(OTHER), DROP)]))
    code, out, _ = run(capsys, *base, "--update")
    assert code == 0
    assert json.loads(ledger.read_text())["frozen"] == stored["frozen"]
    assert json.loads(out)["bounds"]["frozen"] == stored["frozen"]

    changed = write(tmp / "changed.json", {**plan, "epsilon_miss": 0.5})
    code, _, err = run(capsys, *base, "--update", "--plan", changed)
    assert code == 2 and "pre-registered" in err
