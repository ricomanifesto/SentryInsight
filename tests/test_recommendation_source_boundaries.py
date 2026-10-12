"""Frozen source ownership across audience prefixes and typed release rows.

No new audience or version grammar: unclassified prefixes remain complete and
unsupported. Existing version roles own rows before recommendation soft wraps
are joined. Full source context survives both successful and rejected plans.
"""

import pytest

from src.core.finding_evidence import recommendation_action
from src.core.report_artifact import parse_report_artifact
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article

CVE = "CVE-2026-1234"
FIRST = "Example Server 2019 Cumulative Update 14"
SECOND = "Example Server 2019 Cumulative Update 15"
TARGET = "Example Server 2019 Cumulative Update 16"


def source_for(guidance, form):
    if form in {"html", "html-wrap"}:
        body = (
            guidance.replace("should ", "should<br>")
            if form == "html-wrap"
            else guidance
        )
        return (
            f"<h2>{CVE}</h2><p>{CVE} exploitation status is unknown.</p><p>{body}</p>"
        )
    if form == "verb-wrap":
        guidance = guidance.replace("should ", "should\n")
    elif form == "prefix-wrap":
        guidance = guidance.replace(" customers", "\ncustomers")
    return f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}"


def rejected_pipeline(monkeypatch, tmp_path, content):
    prior = {
        "index.md": b"Previous report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
        ".sentryinsight-articles-fingerprint": b"previous-inputs\n",
    }
    for name, data in prior.items():
        (tmp_path / name).write_bytes(data)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(content)],
        expect_model_call=False,
    )
    assert result["status"] == "failed", result
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all((tmp_path / name).read_bytes() == data for name, data in prior.items())


def published_pipeline(monkeypatch, tmp_path, content):
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(content)]
    )
    assert result["status"] == "completed", result
    (finding,) = parse_report_artifact((tmp_path / "index.md").read_text()).findings
    return finding


@pytest.mark.parametrize("prefix", ["U.S.", "Acme Inc.", "Authorized operators, e.g."])
@pytest.mark.parametrize(
    "form", ["plain", "prefix-wrap", "verb-wrap", "html", "html-wrap"]
)
@pytest.mark.parametrize(
    "advice",
    [
        "install the update",
        "install the update immediately",
        "not install the update as soon as possible",
        "install the update, if needed",
    ],
)
def test_unclassified_audience_cannot_be_dropped_at_any_source_boundary(
    monkeypatch, tmp_path, prefix, form, advice
):
    guidance = f"{prefix} customers should {advice}."
    assert recommendation_action([guidance]) == "none"
    rejected_pipeline(monkeypatch, tmp_path, source_for(guidance, form))


@pytest.mark.parametrize("form", ["plain", "verb-wrap", "html", "html-wrap"])
@pytest.mark.parametrize("modifier", ["immediately", "as soon as possible"])
@pytest.mark.parametrize(
    "negative,conditional", [(False, False), (True, False), (False, True)]
)
def test_known_audience_keeps_complete_guidance_and_polarity(
    monkeypatch, tmp_path, form, modifier, negative, conditional
):
    guidance = (
        f"Customers should {'not ' if negative else ''}install the update {modifier}"
        + (", if needed" if conditional else "")
        + "."
    )
    finding = published_pipeline(monkeypatch, tmp_path, source_for(guidance, form))
    assert finding.action.value == ("none" if negative or conditional else "patch")
    assert finding.recommended_actions == guidance


@pytest.mark.parametrize("form", ["plain", "html", "html-wrap"])
@pytest.mark.parametrize("state", ["affected", "unaffected"])
@pytest.mark.parametrize("advice_first", [False, True])
@pytest.mark.parametrize("qualification", ["", "not ", "conditional"])
def test_explicit_version_roles_and_qualified_recommendations_keep_ordered_owners(
    monkeypatch, tmp_path, form, state, advice_first, qualification
):
    advice = (
        f"Customers should {'not ' if qualification == 'not ' else ''}install {TARGET}"
        + (", if needed" if qualification == "conditional" else "")
        + "."
    )
    row = f"Customers of {FIRST} are {state}."
    lines = [advice, row] if advice_first else [row, advice]
    if form == "plain":
        content = f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n" + "\n".join(
            lines
        )
    else:
        if form == "html-wrap":
            lines = [line.replace("should ", "should<br>") for line in lines]
        content = (
            f"<h2>{CVE}</h2><p>{CVE} exploitation status is unknown.</p><ul><li>"
            + "<br>".join(lines)
            + "</li></ul>"
        )
    finding = published_pipeline(monkeypatch, tmp_path, content)
    assert finding.action.value == ("patch" if not qualification else "none")
    assert (FIRST in finding.affected_versions) is (state == "affected")
    assert (FIRST in finding.exceptions) is (state == "unaffected")
    assert TARGET not in finding.affected_versions and TARGET not in finding.exceptions
    assert advice in finding.recommended_actions and row in finding.recommended_actions


@pytest.mark.parametrize("breaks", ["\n", "<br>", "<br><br>"])
@pytest.mark.parametrize("wrap_target", [False, True])
@pytest.mark.parametrize(
    "negative,conditional", [(False, False), (True, False), (False, True)]
)
def test_cumulative_rows_before_advice_do_not_absorb_its_named_target(
    monkeypatch, tmp_path, breaks, wrap_target, negative, conditional
):
    advice = f"Customers should {'not ' if negative else ''}install {TARGET}"
    advice += ", if needed." if conditional else "."
    raw_advice = (
        advice.replace("install ", f"install{breaks}") if wrap_target else advice
    )
    block = breaks.join([FIRST, SECOND, raw_advice])
    content = (
        f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{block}"
        if breaks == "\n"
        else f"<h2>{CVE}</h2><p>{CVE} exploitation status is unknown.</p><ul><li>{block}</li></ul>"
    )
    finding = published_pipeline(monkeypatch, tmp_path, content)
    assert finding.action.value == ("none" if negative or conditional else "patch")
    assert FIRST in finding.affected_versions and SECOND in finding.affected_versions
    assert TARGET not in finding.affected_versions
    assert (
        FIRST in finding.recommended_actions and SECOND in finding.recommended_actions
    )
    assert advice in finding.recommended_actions
