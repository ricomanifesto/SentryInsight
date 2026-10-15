"""Independent modifier-scope and source-preservation contract."""

import hashlib
import httpx
import pytest
from src.core.finding_evidence import assess_exploitation
from src.core.reporting import build_reporting_catalog
from src.core.finding_generation import compile_finding_records
from test_owned_relation_contract import article
from test_finding_generation_pipeline import run_real_pipeline

A = "CVE-2026-1234"
B = "CVE-2026-5678"
ROWS = []


def row(group, text, expected, ids=(A,)):
    ROWS.append(dict(group=group, text=text, expected=expected, ids=ids))


# These literal expectations come from denial scope, not implementation tables.
for modifier in [
    "widely",
    "extensively",
    "actively",
    "publicly",
    "successfully",
    "currently",
    "now",
    "still",
    "newly",
    "recently",
    "yet",
    "first",
]:
    for predicate in [
        f"is not {modifier} exploited",
        f"is {modifier} not exploited",
        f"has never been {modifier} exploited",
    ]:
        row("negative-prefix", f"{A} {predicate}.", "unknown")
    row("actor-prefix", f"Attackers are not {modifier} exploiting {A}.", "unknown")
for modifier in [
    "widely",
    "extensively",
    "actively",
    "publicly",
    "successfully",
    "currently",
    "now",
    "still",
    "newly",
    "recently",
    "first",
]:
    row("positive-control", f"{A} is {modifier} exploited.", "active")
    row(
        "past-control",
        f"{A} was {modifier} exploited.",
        "unsupported" if modifier in {"currently", "now"} else "observed",
    )
for modifier in [
    "widely",
    "extensively",
    "actively",
    "publicly",
    "successfully",
    "currently",
    "now",
    "still",
    "newly",
    "recently",
]:
    row("negative-suffix", f"{A} is not exploited {modifier}.", "unknown")
    row("actor-suffix", f"Attackers are not exploiting {A} {modifier}.", "unknown")
for modifier in ["widely", "extensively"]:
    event = f"{A} is not {modifier} exploited"
    for text in [
        f"The vendor has found evidence that {event}.",
        f'"{event}," the company said.',
        f"{event} as investigators confirmed yesterday.",
        f"It is possible that {event}.",
        f"If reports are accurate, {event}.",
        f"{event} if reports are accurate.",
    ]:
        row("wrapped-denial", text, "unknown")
    for text in [
        f"The vendor has not found evidence that {A} is {modifier} exploited.",
        f"There is no evidence that {A} is {modifier} exploited.",
        f"There is no evidence of {A} being exploited {modifier}.",
        f"Exploitation of {A} has not been observed {modifier}.",
    ]:
        row("absence-qualified-proposition", text, "unknown")
    row("source-only", f"Exploitation has not been observed {modifier}.", "unknown", ())
    row(
        "quoted-owned",
        f'Example patched a modem flaw, {A}, that it said: "is not {modifier} exploited"',
        "unknown",
    )
for text, expected in [
    (f"{A} is not exploited.", "not_observed"),
    (f"{A} has never been exploited.", "not_observed"),
    (f"{A} was not exploited.", "not_observed"),
    (f"{A} is also not exploited.", "not_observed"),
    (f"{A} is not also exploited.", "unknown"),
    (f"{A} is exploited.", "active"),
    (f"{A} was exploited yesterday.", "observed"),
    (f"The vendor has not found evidence that {A} is exploited.", "not_observed"),
    (f"Exploitation of {A} has not been observed.", "not_observed"),
    (f"Exploitation of {A} has not been confirmed.", "unknown"),
    (f"Exploitation of {A} has not been observed in the wild.", "not_observed"),
    (f"No evidence of active exploitation of {A}.", "unknown"),
    (f"Active exploitation of {A} has not been observed.", "unknown"),
    (f"Active exploitation of {A} has not been detected.", "unknown"),
    (f"Active exploitation of {A} has not been confirmed.", "unknown"),
    (f"Active exploitation of {A} is confirmed.", "active"),
    (f"Exploitation of {A} has not been observed now.", "unsupported"),
    (f"{A} was not exploited yesterday.", "unknown"),
    (f"{A} is not observed exploited.", "unsupported"),
    (f"{A} is not not exploited.", "unsupported"),
    (f"{A} is not never exploited.", "unsupported"),
    (f"{A} is not oddly exploited.", "unsupported"),
    (f"{A} was currently exploited.", "unsupported"),
    (f"{A} is not widely exploited yesterday.", "unsupported"),
    (f"{A} is not widely exploited tomorrow.", "unsupported"),
    (f"{A} has not begun to be widely exploited.", "unsupported"),
    (f"{A} has begun to be widely exploited.", "observed"),
    (f"{A} never continues to be widely exploited.", "unsupported"),
    (f"{A} continues to be widely exploited.", "active"),
    (f"{A} is not only widely exploited but weaponized in the wild.", "active"),
    (
        f"{A} may not only be extensively exploited but also is weaponized in the wild.",
        "potential",
    ),
    (f"{A} is not widely exploited and weaponized in the wild.", "unknown"),
    (f"{A} is not widely exploited and is weaponized in the wild.", "active"),
    (f"{A} is not widely exploited but is exploited.", "active"),
    (f"{A} is not actively exploited but is exploited.", "unknown"),
    (f"{A} was not actively exploited but is exploited.", "active"),
    (f"{A} was exploited yesterday.\n\n{A} is not widely exploited.", "observed"),
    (f"{A} was exploited yesterday.\n\n{A} is not actively exploited.", "observed"),
    (f"{A} is exploited.\n\n{A} is not widely exploited.", "active"),
    (f"{A} is exploited.\n\n{A} is not actively exploited.", "unknown"),
    (f"{A} is not widely exploited; {B} is exploited.", "unknown"),
    (f"{A} is not widely exploited and {B} is exploited.", "unknown"),
]:
    row("independent-control", text, expected)
for possibility in ["potentially", "likely", "possibly", "probably", "unlikely"]:
    row("possibility-control", f"{A} is {possibility} exploited.", "potential")
    row("possibility-denial", f"{A} is not {possibility} exploited.", "unknown")
for tail in [
    "often",
    "sometimes",
    "always",
    "ever",
    "twice",
    "overnight",
    "worldwide",
    "abroad",
    "overseas",
    "here",
    "there",
]:
    row("bounded-tail-denial", f"{A} is not exploited {tail}.", "unknown")
row(
    "closed-exhaustive",
    "The advisory lists two known flaws that it says were not successfully exploited.",
    "unknown",
    (),
)
row(
    "closed-exhaustive-control",
    "The advisory lists two known flaws that it says were successfully exploited.",
    "observed",
    (),
)

for modifier in ["widely", "recently", "successfully"]:
    row(
        "intrusion-denial",
        f"Example Group has not {modifier} gained access by exploiting a vulnerability ({A}).",
        "unknown",
    )
    row(
        "relative-onset-denial",
        f"The vendor issued a fix for {A}, which Example Group not {modifier} began exploiting as a zero-day in June.",
        "unknown",
    )
row(
    "intrusion-control",
    f"Example Group gained access by exploiting a vulnerability ({A}).",
    "observed",
)
row(
    "relative-onset-control",
    f"The vendor issued a fix for {A}, which Example Group first began exploiting as a zero-day in June.",
    "observed",
)


@pytest.fixture(autouse=True)
def no_transport(monkeypatch):
    def forbidden(*a, **kw):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


@pytest.mark.parametrize("case", ROWS, ids=lambda x: x["group"] + "-" + x["text"])
def test_modifier_projection(case):
    item = article(case["text"])
    before = item["content"]
    a = assess_exploitation([item], case["ids"])
    actual = "unsupported" if a.unsupported else a.status
    assert actual == case["expected"], {
        "text": case["text"],
        "expected": case["expected"],
        "actual": actual,
    }
    assert item["content"] == before
    if case["expected"] == "unknown":
        assert not a.negative


@pytest.mark.parametrize(
    "text",
    [
        f"{A} is not widely exploited.",
        f"{A} is not extensively exploited.",
        f"Attackers are not widely exploiting {A}.",
        f"The vendor has not found evidence that {A} is widely exploited.",
        f'"{A} is not widely exploited," the company said.',
        f"Active exploitation of {A} has not been observed.",
        f"{A} is not actively exploited.",
    ],
)
def test_pipeline_keeps_complete_source_without_invented_absence(
    monkeypatch, tmp_path, text
):
    item = article(f"## {A}\n\n{text}")
    original = item["content"]
    digest = hashlib.sha256(original.encode()).hexdigest()
    r = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert r["status"] == "completed", r
    report = (tmp_path / "index.md").read_text()
    assert "**Exploitation Status**: unknown" in report
    assert "Supplied reporting states exploitation has not been observed" not in report
    assert text in report
    assert item["content"] == original
    src = r["analysis_results"]["reporting_sources"][0]
    assert hashlib.sha256(src["content"].encode()).hexdigest() == digest


@pytest.mark.parametrize(
    "text", [f"{A} is not widely exploited tomorrow.", f"{A} is not oddly exploited."]
)
def test_required_unknown_preserves_artifacts_before_transport(
    monkeypatch, tmp_path, text
):
    originals = {
        n: ("previous " + n).encode()
        for n in [
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        ]
    }
    for n, b in originals.items():
        (tmp_path / n).write_bytes(b)
    r = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(text)],
        expect_model_call=False,
    )
    assert r["status"] == "failed"
    assert r["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all((tmp_path / n).read_bytes() == b for n, b in originals.items())


@pytest.mark.parametrize("reverse", [False, True])
def test_source_and_cve_isolation(reverse):
    items = [
        article(f"{A} is not widely exploited.", link="https://example.test/a"),
        article(f"{B} is exploited.", link="https://example.test/b"),
    ]
    if reverse:
        items.reverse()
    catalog = build_reporting_catalog(items)
    result = {r.cves: r.status for r in compile_finding_records(catalog, [A, B])}
    assert result == {(A,): "unknown", (B,): "active"}
