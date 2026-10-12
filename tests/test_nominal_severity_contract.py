"""Frozen nominal evidence-operation and complete scoped-rating contract."""

import json
import httpx
import pytest
from src.core.assertions import parse_assertions
from src.core.finding_evidence import assess_exploitation, source_assertions
from src.core.finding_generation import _severity
from src.core.report_artifact import parse_report_artifact
from test_finding_generation import catalog_for, render
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article
from test_assertion_subject_contract import publish, rejected

A = "CVE-2026-1234"
B = "CVE-2026-5678"

# Literal state table: confirmation absence is uncertainty; observation/detection
# absence is qualified non-observation. A reporting finite never asserts ongoing
# exploitation without an explicit active event qualifier.
NOMINAL_TABLE = {
    ("confirmed", "has not been"): "unknown",
    ("observed", "has not been"): "not_observed",
    ("detected", "has not been"): "not_observed",
    ("confirmed", "has been"): "observed",
    ("observed", "has been"): "observed",
    ("detected", "has been"): "observed",
    ("confirmed", "was"): "observed",
    ("observed", "was"): "observed",
    ("detected", "was"): "observed",
    ("confirmed", "is"): "observed",
    ("observed", "is"): "observed",
    ("detected", "is"): "observed",
}
NOMINAL = []
for (op, aux), expected in NOMINAL_TABLE.items():
    for shape, head, ids in [
        ("prefix", f"{A} exploitation", [A]),
        ("of", f"Exploitation of {A}", [A]),
        ("joint", f"Exploitation of {A} and {B}", [A, B]),
        ("source", "Exploitation", []),
    ]:
        NOMINAL.append(
            dict(
                id=f"{shape}-{aux}-{op}",
                text=f"{head} {aux} {op}.",
                expected=expected,
                cves=ids,
            )
        )
for op in ("confirmed", "observed", "detected"):
    for prefix in ("Possible", "Potential"):
        for aux in ("has been", "has not been"):
            NOMINAL.append(
                dict(
                    id=f"{prefix}-{aux}-{op}",
                    text=f"{prefix} exploitation of {A} {aux} {op}.",
                    expected="unknown" if aux == "has not been" else "potential",
                    cves=[A],
                )
            )
    for aux in ("has been", "has not been", "is", "was"):
        text = f"Exploitation of {A} {aux} {op}."
        for wrapper in ("It is unknown whether ", "If reports are accurate, "):
            NOMINAL.append(
                dict(
                    id=f"{wrapper}-{aux}-{op}",
                    text=wrapper + text,
                    expected="unknown",
                    cves=[A],
                )
            )
        NOMINAL.append(
            dict(
                id=f"future-{aux}-{op}",
                text=text[:-1] + " tomorrow.",
                expected="unsupported",
                cves=[A],
            )
        )
for text, expected in [
    (f"Active exploitation of {A} is confirmed.", "active"),
    (f"Active exploitation of {A} was observed.", "observed"),
    (f"Active exploitation of {A} has not been confirmed.", "unknown"),
    (f"Exploitation of {A} was confirmed yesterday.", "observed"),
    (f"Exploitation of {A} is confirmed as was confirmed yesterday.", "observed"),
    (f"No exploitation of {A} confirmed.", "unknown"),
    (f"No exploitation of {A} observed.", "not_observed"),
    (f"No exploitation of {A} detected.", "not_observed"),
    (f"No evidence of exploitation of {A}.", "not_observed"),
    (
        f"Exploitation of {A} has not been confirmed and unclassified predicates prove exploitation.",
        "unsupported",
    ),
    (f"Exploitation of {A} was not confirmed.", "unsupported"),
    (f"Exploitation of {A} might have been confirmed.", "unsupported"),
    (f"Exploitation of {A} has not been invented.", "unsupported"),
    (f"The vendor denied that exploitation of {A} has been confirmed.", "unsupported"),
]:
    NOMINAL.append(dict(id=text, text=text, expected=expected, cves=[A]))

RATINGS = [
    ("A critical vulnerability was not present.", "unknown"),
    ("The vendor ruled out a critical vulnerability.", "unknown"),
    ("A critical vulnerability may be present.", "unknown"),
    ("A critical vulnerability is possible.", "unknown"),
    ("A critical vulnerability is present if reports are accurate.", "unknown"),
    ("A critical vulnerability was alleged.", "unknown"),
    ("A critical vulnerability was present.", "critical"),
    ("It is a critical vulnerability.", "critical"),
    ("It is not a critical vulnerability.", "unknown"),
    ("It may be a critical vulnerability.", "unknown"),
    ("two critical vulnerabilities", "critical"),
    ("two high-severity flaws", "high"),
    ("not critical vulnerabilities", "unknown"),
    ("Severity: critical.", "critical"),
    ("Severity rating: high.", "high"),
    ("It is rated medium.", "medium"),
    ("It was rated low.", "low"),
    ("It is not rated critical.", "unknown"),
    ("Severity: critical was not confirmed.", "unknown"),
    ("Severity: critical if the report is accurate.", "unknown"),
    ("Severity: critical pending confirmation.", "unknown"),
    ("Severity: critical for unexplained reasons.", "unknown"),
    ("Its CVSS score is 7.5.", "high"),
    ("It carries a CVSS score of 10.0.", "critical"),
    ("The vulnerability carries a CVSS score of 9.5 out of 10.0.", "critical"),
    ("CVSS score of 9.8 was not assigned.", "unknown"),
    ("No CVSS score of 9.8 has been assigned.", "unknown"),
    ("It may have a CVSS score of 9.8.", "unknown"),
    ("CVSS score: 9.8 pending confirmation.", "unknown"),
    ("CVSS score: 9.8 if reports are accurate.", "unknown"),
    ("CVSS score: 9.8 was rejected.", "unknown"),
    ("Its CVSS:3.1/AV:N/AC:L vector was published.", "unknown"),
    ("Severity: high. Its CVSS score is 9.8.", "unknown"),
    ("Severity: critical. Its CVSS score is 9.8.", "critical"),
    ("Severity: critical. Its CVSS score may be 9.8.", "unknown"),
    ("A critical infrastructure service was discussed.", "unknown"),
    (
        "CVE-2026-1234 is a critical vulnerability in Example Gateway, with a CVSS score of 9.8.",
        "critical",
    ),
]
for value, expected in [
    ("0.0", "unknown"),
    ("0.1", "low"),
    ("3.9", "low"),
    ("4.0", "medium"),
    ("6.9", "medium"),
    ("7.0", "high"),
    ("8.9", "high"),
    ("9.0", "critical"),
    ("10.0", "critical"),
    ("10.1", "unknown"),
    ("9.80", "unknown"),
]:
    RATINGS.append((f"CVSS score: {value}.", expected))


@pytest.fixture(autouse=True)
def no_real_transport(monkeypatch):
    def forbidden(*a, **kw):
        raise AssertionError("Real HTTP/model transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


@pytest.mark.parametrize("row", NOMINAL, ids=lambda r: r["id"])
def test_nominal_reporting_event_contract(row):
    clauses = parse_assertions(row["text"])
    assert clauses
    if row["expected"] == "unsupported":
        assert any(c.unsupported for c in clauses)
    else:
        assert not any(c.unsupported for c in clauses)
        assert {c.status for c in clauses if c.kind == "assertion"} == {row["expected"]}
        assert {v for c in clauses for v in c.cves} == set(row["cves"])


@pytest.mark.parametrize("text,state", RATINGS)
def test_complete_rating_contract(text, state):
    assert _severity([text]) == state


@pytest.mark.parametrize(
    "op,state",
    [
        ("confirmed", "unknown"),
        ("observed", "not_observed"),
        ("detected", "not_observed"),
    ],
)
@pytest.mark.parametrize("joint", [False, True])
def test_nominal_rendered_pipeline_retains_evidence(
    monkeypatch, tmp_path, op, state, joint
):
    ids = [A, B] if joint else [A]
    text = f'Exploitation of {" and ".join(ids)} has not been {op}.'
    findings = publish(monkeypatch, tmp_path, text, ids, [state])
    assert len(findings) == 1 and findings[0].cve_ids == tuple(ids)
    report = (tmp_path / "index.md").read_text()
    assert text in report
    if op == "confirmed":
        assert (
            "Some supplied reporting states exploitation has not been observed."
            not in report
        )


@pytest.mark.parametrize(
    "text",
    [
        f"Exploitation of {A} has not been confirmed tomorrow.",
        f"If reports are accurate, exploitation of {A} has not been confirmed tomorrow.",
        f"Exploitation of {A} has not been confirmed and unclassified predicates prove exploitation.",
        f"Exploitation of {A} might have been confirmed.",
    ],
)
def test_unsupported_nominal_preserves_artifacts(monkeypatch, tmp_path, text):
    rejected(monkeypatch, tmp_path, text)


@pytest.mark.parametrize(
    "rating,state", [r for r in RATINGS[:37] if r[0] != "not critical vulnerabilities"]
)
def test_rating_real_pipeline_preserves_complete_claim(
    monkeypatch, tmp_path, rating, state
):
    text = f"## {A}\n\n{A} exploitation has not been observed.\n\n{rating}"
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(text)]
    )
    assert result["status"] == "completed", result["analysis_results"].get("error")
    report = (tmp_path / "index.md").read_text()
    (finding,) = parse_report_artifact(report).findings
    assert finding.severity.value == state
    # The exact rating relation must remain in the record's retained evidence
    # inventory; presentation cannot silently delete it to obtain an unknown badge.
    records, _ = render(catalog_for(text))
    assert (
        any(rating in e.text for r in records for e in r.excerpts) or rating in report
    )


@pytest.mark.parametrize("reverse", [False, True])
def test_independent_nominal_owners_are_not_reporter_polarity_wildcards(reverse):
    parts = [
        f"Exploitation of {A} has not been confirmed.",
        f"Exploitation of {B} has not been observed.",
    ]
    text = " ".join(reversed(parts) if reverse else parts)
    s = article(text)
    a = assess_exploitation([s], [A])
    b = assess_exploitation([s], [B])
    assert a.status == "unknown" and not a.negative
    assert b.status == "not_observed" and b.negative
    assert all(
        p in " ".join(r.source_text for r in source_assertions(s)) for p in parts
    )


@pytest.mark.parametrize("reverse", [False, True])
def test_complete_scoped_ratings_do_not_cross_independent_findings(reverse):
    parts = [
        f"## {A}\n\n{A} exploitation has not been observed.\n\nA critical vulnerability was not present.",
        f"## {B}\n\n{B} exploitation has not been observed.\n\nIts CVSS score is 7.5.",
    ]
    records, _ = render(catalog_for("\n\n".join(reversed(parts) if reverse else parts)))
    assert {r.cves: dict(r.fields)["Severity"] for r in records} == {
        (A,): "unknown",
        (B,): "high",
    }


@pytest.mark.parametrize(
    "text,state",
    [
        (f"{A} and {B} are critical vulnerabilities.", "critical"),
        (
            f"{A} and {B} are critical vulnerabilities if reports are accurate.",
            "unknown",
        ),
    ],
)
def test_joint_rating_preserves_complete_joint_scope(text, state):
    records, _ = render(
        catalog_for(f"Exploitation of {A} and {B} has not been observed.\n\n{text}")
    )
    assert len(records) == 1 and records[0].cves == (A, B)
    assert dict(records[0].fields)["Severity"] == state


def test_separate_source_only_ratings_do_not_share_scope():
    records, _ = render(
        catalog_for(
            "Exploitation has not been observed.\n\nA critical vulnerability was not present.",
            "Exploitation has not been observed.\n\nIts CVSS score is 7.5.",
        )
    )
    assert len(records) == 2 and all(not r.cves for r in records)
    assert sorted(dict(r.fields)["Severity"] for r in records) == ["high", "unknown"]


def test_existing_unclassified_required_fragment_is_not_rescued_by_rating(
    monkeypatch, tmp_path
):
    previous = {
        name: b"previous valid bytes"
        for name in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    }
    for name, data in previous.items():
        (tmp_path / name).write_bytes(data)
    text = f"## {A}\n\n{A} exploitation has not been observed.\n\nnot critical vulnerabilities"
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(text)],
        expect_model_call=False,
    )
    assert result["status"] == "failed"
    assert all(
        (tmp_path / name).read_bytes() == data for name, data in previous.items()
    )


@pytest.mark.parametrize(
    "text,state",
    [
        (f"Exploitation of {A} is confirmed.", "observed"),
        (f"Exploitation of {A} is observed.", "observed"),
        (f"Exploitation of {A} has been confirmed.", "observed"),
        (f"Active exploitation of {A} is confirmed.", "active"),
    ],
)
def test_nominal_reporter_time_does_not_invent_ongoing_activity(
    monkeypatch, tmp_path, text, state
):
    publish(monkeypatch, tmp_path, text, [A], [state])


@pytest.mark.parametrize("scope", [A, f"{A} and {B}"])
def test_unconfirmed_source_cannot_ground_nonobservation_tamper(scope):
    from src.core.finding_evidence import validate_finding_evidence, EvidenceError

    catalog = catalog_for(f"Exploitation of {scope} has not been confirmed.")
    _, report = render(catalog)
    tampered = report.replace(
        "**Exploitation Status**: unknown", "**Exploitation Status**: not_observed"
    )
    with pytest.raises(EvidenceError):
        validate_finding_evidence(tampered, catalog)


def test_model_plan_cannot_supply_its_own_severity(monkeypatch, tmp_path):
    from test_analyze_guards import reference_plan_from_prompt

    previous = {
        name: b"previous valid bytes"
        for name in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    }
    for name, data in previous.items():
        (tmp_path / name).write_bytes(data)

    def wrong(**kwargs):
        value = json.loads(reference_plan_from_prompt(**kwargs))
        value["findings"][0]["severity"] = "critical"
        return json.dumps(value)

    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(
                f"## {A}\n\n{A} exploitation has not been observed.\n\nA critical vulnerability was not present."
            )
        ],
        select_plan=wrong,
    )
    assert result["status"] == "failed"
    assert all(
        (tmp_path / name).read_bytes() == data for name, data in previous.items()
    )


def test_foreign_rejected_rating_does_not_erase_independent_positive_rating():
    text = f"## {A}\n\n{A} exploitation has not been observed.\n\nIts CVSS score is 9.8.\n\n## {B}\n\n{B} exploitation has not been observed.\n\nA critical vulnerability was not present."
    records, _ = render(catalog_for(text))
    assert {r.cves: dict(r.fields)["Severity"] for r in records} == {
        (A,): "critical",
        (B,): "unknown",
    }
