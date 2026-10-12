"""Complete source-owned directive and context relations preserve their operands."""

import json
import httpx
import pytest

from src.core.recommendations import parse_recommendation
from src.core.finding_evidence import recommendation_action
from src.core.report_artifact import parse_report_artifact
from test_directive_modifier_contract import pipeline
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article

A = "CVE-2026-1234"
B = "CVE-2026-5678"

# Existing verbs and argument/action pairs, explicit participle forms only.
FRAMES = [
    ("install", "installed", "the patch", "patch", "needs to"),
    ("apply", "applied", "the update", "patch", "needs to"),
    ("patch", "patched", "the systems", "patch", "need to"),
    ("upgrade", "upgraded", "the appliance", "patch", "needs to"),
    ("update", "updated", "the appliance", "patch", "needs to"),
    ("mitigate", "mitigated", "the vulnerability", "mitigate", "needs to"),
    ("investigate", "investigated", "suspicious activity", "investigate", "needs to"),
    ("review", "reviewed", "the logs", "investigate", "need to"),
    ("monitor", "monitored", "logs", "monitor", "need to"),
    ("restart", "restarted", "the service", "none", "needs to"),
]


@pytest.fixture(autouse=True)
def prohibit_real_transport(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real network/model transport forbidden in oracle")

    monkeypatch.setattr(httpx.Client, "request", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "request", forbidden)


def instruction(frame, voice, modal, qualification):
    verb, participle, target, _, needs = frame
    finite = ("need to" if voice == "active" else needs) if modal == "need" else modal
    negative = "not " if qualification == "negative" else ""
    if voice == "active":
        text = f"Users {finite} {negative}{verb} {target}"
    else:
        text = f"{target[0].upper() + target[1:]} {finite} {negative}be {participle}"
    return text + (", if needed" if qualification == "conditional" else "") + "."


@pytest.mark.parametrize("frame", FRAMES, ids=[f[0] for f in FRAMES])
@pytest.mark.parametrize("voice", ["active", "passive"])
@pytest.mark.parametrize("modal", ["should", "must", "need"])
@pytest.mark.parametrize("qualification", ["affirmative", "negative", "conditional"])
def test_complete_voice_frame_equivalence(frame, voice, modal, qualification):
    text = instruction(frame, voice, modal, qualification)
    parsed = parse_recommendation(text)
    assert parsed is not None and not parsed.ambiguous
    assert parsed.source_text == text
    assert len(parsed.clauses) == 1
    clause = parsed.clauses[0]
    assert clause.verb == frame[0]
    assert clause.polarity == (
        "negative" if qualification == "negative" else "affirmative"
    )
    assert clause.conditions == (
        ("if needed",) if qualification == "conditional" else ()
    )
    assert clause.object_text == (
        frame[2] if voice == "active" else frame[2][0].upper() + frame[2][1:]
    )
    assert recommendation_action([text]) == (
        frame[3] if qualification == "affirmative" else "none"
    )


@pytest.mark.parametrize("frame", FRAMES, ids=[f[0] for f in FRAMES])
@pytest.mark.parametrize("qualification", ["affirmative", "negative", "conditional"])
def test_passive_guidance_is_mandatory_through_graph(
    monkeypatch, tmp_path, frame, qualification
):
    text = instruction(frame, "passive", "should", qualification)
    pipeline(
        monkeypatch,
        tmp_path,
        text,
        frame[3] if qualification == "affirmative" else "none",
    )


ACCEPTED = [
    ("The patch should be installed unless unclassified decisions favor it.", "none"),
    ("The patch should be installed immediately.", "patch"),
    ("The update must be applied as soon as possible.", "patch"),
    ("If needed, the patch should be installed.", "none"),
    ("Unless reports are accurate, the patch should be installed.", "none"),
    ("The patch must not be installed immediately.", "none"),
    ("The patch and the update should be applied.", "patch"),
    ("Logs and traffic should be monitored.", "monitor"),
    ("The patch and the workaround should be applied.", "patch"),
    ("The appliance should be upgraded to version 2.0.", "patch"),
    ("Version 2.0 should be installed.", "patch"),
    ("The patch should be installed to address the vulnerability.", "patch"),
    ("Logs should be monitored to detect suspicious activity.", "monitor"),
    ('"The patch should be installed," the company said.', "patch"),
    ("The patch should be installed and logs should be monitored.", "patch"),
    ("The patch should be installed but logs must not be monitored.", "patch"),
    ("The patch should be installed but the patch must not be installed.", "none"),
    ("The patch should be installed or the workaround should be applied.", "none"),
    ("The patch should be installed and applied.", "patch"),
]


@pytest.mark.parametrize("text,action", ACCEPTED)
def test_composed_passive_contexts_keep_full_guidance(
    monkeypatch, tmp_path, text, action
):
    pipeline(monkeypatch, tmp_path, text, action)


@pytest.mark.parametrize("connector", [" and ", ", but ", " then ", "; "])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("second_voice", ["active", "passive"])
def test_independent_clause_conditions_do_not_cross_voices(
    monkeypatch, tmp_path, connector, reverse, second_voice
):
    pieces = [
        "The patch should be installed immediately",
        (
            "logs should be monitored, if needed"
            if second_voice == "passive"
            else "users should monitor logs, if needed"
        ),
    ]
    if reverse:
        pieces.reverse()
    pipeline(monkeypatch, tmp_path, connector.join(pieces) + ".", "patch")


UNSUPPORTED = [
    "The patch should have been installed.",
    "The patch must have been applied.",
    "The patch should be being installed.",
    "The patch should be able to be installed.",
    "The patch should begin to be installed.",
    "The patch is advised to be installed.",
    "The patch should unexpectedly be installed.",
    "The patch should be installed inexplicably.",
    "The patch should be installed immediately immediately.",
    "The patch should be installed by an unknown party.",
    "The patch should be invented.",
    "The patch should probably be installed.",
    "It is unclear whether the patch should be installed.",
    "The report should be installed.",
    "The unclassified asset should be applied.",
    "The patch that users deny should be installed.",
    "The patch should be installed and unrelated predicates prove compliance.",
    "The patch should be installed; operators should perform an unclassified action.",
    "The patch should be installed and the report should be monitored.",
]


@pytest.mark.parametrize("text", UNSUPPORTED)
def test_required_unknown_passive_relation_is_terminal(monkeypatch, tmp_path, text):
    pipeline(monkeypatch, tmp_path, text, None)


@pytest.mark.parametrize(
    "text", ["The patch was installed.", "The update has been applied."]
)
def test_declarative_completion_is_not_advice(monkeypatch, tmp_path, text):
    assert recommendation_action([text]) == "none"
    source = f"## {A}\n\n{A} exploitation status is unknown.\n\n{text}"
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(source)]
    )
    assert result["status"] == "completed", result
    (finding,) = parse_report_artifact((tmp_path / "index.md").read_text()).findings
    assert finding.action.value == "none"
    assert finding.recommended_actions == "Not stated in supplied sources."


@pytest.mark.parametrize("scope", ["single", "joint", "source_only", "foreign"])
def test_passive_guidance_respects_document_scope(monkeypatch, tmp_path, scope):
    text = "The patch should be installed."
    if scope == "source_only":
        source = "Attackers are actively exploiting the gateway.\n\n" + text
        ids = ()
    elif scope == "joint":
        source = f"## {A} and {B}\n\n{A} and {B} are actively exploited.\n\n{text}"
        ids = (A, B)
    else:
        source = f"## {A}\n\n{A} exploitation status is unknown.\n\n{text}"
        ids = (A,)
    articles = [article(source)]
    if scope == "foreign":
        articles.append(
            article(
                f"## {B}\n\n{B} exploitation status is unknown.\n\nUsers should monitor logs.",
                link="https://example.test/foreign",
            )
        )
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=articles)
    assert result["status"] == "completed", result
    findings = parse_report_artifact((tmp_path / "index.md").read_text()).findings
    target = [f for f in findings if f.cve_ids == ids]
    assert len(target) == 1
    assert target[0].action.value == "patch" and target[0].recommended_actions == text
    if scope == "foreign":
        (other,) = [f for f in findings if f.cve_ids == (B,)]
        assert other.action.value == "monitor"
        assert other.recommended_actions == "Users should monitor logs."
    else:
        assert len(findings) == 1
    saved = json.loads((tmp_path / "current-findings.json").read_text())
    assert saved["finding_count"] == len(findings)


@pytest.mark.parametrize("reverse", [False, True])
def test_qualified_condition_does_not_suppress_an_independent_patch(
    monkeypatch, tmp_path, reverse
):
    pieces = [
        "Logs should be monitored unless unclassified decisions favor it",
        "Users should install the patch",
    ]
    if reverse:
        pieces.reverse()
    pipeline(monkeypatch, tmp_path, "; ".join(pieces) + ".", "patch")
