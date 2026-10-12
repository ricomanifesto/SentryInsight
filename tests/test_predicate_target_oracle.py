"""Frozen finite verbal operators, complete targets and strict residuals."""

import httpx
import pytest
from src.core.assertions import parse_assertions
from src.core.finding_evidence import assess_exploitation
from test_owned_relation_contract import article
from test_assertion_subject_contract import publish
from test_finding_generation_pipeline import run_real_pipeline

A, B, C = "CVE-2026-1234", "CVE-2026-5678", "CVE-2026-9012"
cases = []


def add(name, text, owners=(), states=(), conditions=(), rejected=False):
    cases.append(
        dict(
            name=name,
            text=text,
            owners=owners,
            states=states,
            conditions=conditions or [[] for _ in states],
            rejected=rejected,
        )
    )


targets = [(A, [A]), (f"{A} and {B}", [A, B]), (f"{A}, {B}, and {C}", [A, B, C])]
for index, (target, ids) in enumerate(targets):
    for voice in ("passive", "actor"):
        for mode, state in [
            ("current", "active"),
            ("past", "observed"),
            ("negative", "not_observed"),
            ("possible", "potential"),
            ("conditional", "unknown"),
        ]:
            if voice == "passive":
                copula = "is" if len(ids) == 1 else "are"
                pred = {
                    "current": f"{copula} actively exploited",
                    "past": "was exploited" if len(ids) == 1 else "were exploited",
                    "negative": f"{copula} not exploited",
                    "possible": "may be exploited",
                    "conditional": f"{copula} actively exploited",
                }[mode]
                text = f"{target} {pred} in the wild"
            else:
                pred = {
                    "current": "are actively exploiting",
                    "past": "exploited",
                    "negative": "are not exploiting",
                    "possible": "may be exploiting",
                    "conditional": "are actively exploiting",
                }[mode]
                text = f"The threat actors {pred} {target} in the wild"
            condition = ["if reports are accurate"] if mode == "conditional" else []
            if condition:
                text += ", " + condition[0]
            add(
                f"ordinary-{voice}-{index}-{mode}",
                text + ".",
                [ids],
                [state],
                [condition],
            )
        for past in (False, True):
            operator = (
                "continued"
                if past
                else (
                    "continues" if voice == "passive" and len(ids) == 1 else "continue"
                )
            )
            core = (
                f"{target} {operator} to be actively exploited in the wild"
                if voice == "passive"
                else f"The threat actors {operator} to exploit {target} in the wild"
            )
            for wrapper, state in [
                ("direct", "observed" if past else "active"),
                ("unknown", "unknown"),
                ("possible", "potential"),
                ("conditional", "unknown"),
            ]:
                text = {
                    "direct": core,
                    "unknown": "It is unknown whether " + core,
                    "possible": "It is possible that " + core,
                    "conditional": core + ", if reports are accurate",
                }[wrapper]
                condition = (
                    ["if reports are accurate"] if wrapper == "conditional" else []
                )
                add(
                    f"continuation-{voice}-{index}-{past}-{wrapper}",
                    text + ".",
                    [ids],
                    [state],
                    [condition],
                )

for pred, status in [
    ("are actively exploiting", "active"),
    ("exploited", "observed"),
    ("continue to exploit", "active"),
    ("continued to exploit", "observed"),
]:
    add(
        "source-only-" + pred.replace(" ", "-"),
        f"Attackers {pred} the gateway.",
        [[]],
        [status],
    )

for connector in [" and ", ", but ", "; ", " whereas "]:
    for reverse in (False, True):
        clauses = [
            f"Attackers continue to exploit {A} and {B}",
            f"{C} is not exploited, if reports are accurate",
        ]
        ids, states, conditions = (
            [[A, B], [C]],
            ["active", "unknown"],
            [[], ["if reports are accurate"]],
        )
        if reverse:
            clauses.reverse()
            ids.reverse()
            states.reverse()
            conditions.reverse()
        add(
            f"independent-{connector.strip()}-{reverse}",
            connector.join(clauses) + ".",
            ids,
            states,
            conditions,
        )

rejected = [
    f"Attackers do not continue to exploit {A}.",
    f"The attacker does not continue to exploit {A}.",
    f"Attackers did not continue to exploit {A}.",
    f"Attackers never continue to exploit {A}.",
    f"Attackers continue not to exploit {A}.",
    f"{A} does not continue to be exploited.",
    f"{A} continued not to be exploited.",
    f"{A} never continues to be exploited.",
    f"Attackers may continue to exploit {A}.",
    f"Attackers can continue to exploit {A}.",
    f"Attackers will continue to exploit {A}.",
    f"Attackers have continued to exploit {A}.",
    f"Attackers have been continuing to exploit {A}.",
    f"{A} may continue to be exploited.",
    f"{A} has continued to be exploited.",
    f"Attackers intend to exploit {A}.",
    f"Attackers can exploit {A}.",
    f"Attackers continue continue to exploit {A}.",
    f"Attackers apparently continue to exploit {A}.",
    f"The alleged attackers continue to exploit {A}.",
    f"Attackers continue to exploit {A} or {B}.",
    f"Attackers continue to exploit {A} / {B}.",
    f"Attackers continue to exploit {A} and consider exploiting {B}.",
    f"Attackers continue to exploit {A} unexpectedly consider exploiting {B}.",
    f"{A} continues to be exploited, only when exposed.",
    f"It is unknown whether Attackers can continue to exploit {A}.",
    "Attackers continue to exploit the unexplained remote gateway.",
    f"The threat actors are actively exploiting {A} and consider exploiting {B}.",
]
for index, text in enumerate(rejected):
    add(f"unsupported-{index}", text, rejected=True)


for case in cases:
    if case["name"] == "independent-and-False":
        case["rejected"] = True
CASES = cases


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["name"])
def test_independent_owned_relation_oracle(case):
    clauses = parse_assertions(case["text"])
    if case["rejected"]:
        assert any(c.unsupported for c in clauses), clauses
        return
    assert len(clauses) == len(case["owners"]), clauses
    assert [list(c.cves) for c in clauses] == case["owners"]
    assert [c.status for c in clauses] == case["states"]
    assert [list(c.conditions) for c in clauses] == case["conditions"]
    assert not any(c.unsupported for c in clauses), clauses
    for ids, state in zip(case["owners"], case["states"]):
        assessment = assess_exploitation([article(case["text"])], ids)
        assert not assessment.unsupported
        assert assessment.status == state


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["name"])
def test_real_graph_oracle(monkeypatch, tmp_path, case):
    def forbidden(*_, **__):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)
    if not case["rejected"]:
        ids = list(dict.fromkeys(cve for group in case["owners"] for cve in group))
        findings = publish(monkeypatch, tmp_path, case["text"], ids, case["states"])
        assert sorted(tuple(f.cve_ids) for f in findings) == sorted(
            tuple(group) for group in case["owners"]
        )
        return
    previous = {
        name: ("previous " + name).encode()
        for name in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    }
    for name, content in previous.items():
        (tmp_path / name).write_bytes(content)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(case["text"])],
        expect_model_call=False,
    )
    assert result["status"] == "failed", result
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == data for name, data in previous.items()
    )
