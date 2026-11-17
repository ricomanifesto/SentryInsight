"""Article metadata and background links must not manufacture findings."""

import pytest

from src.core.analyze import collect_exploitation_relevant_prompt_cves
from src.core.article_prompt import format_article_summary
from src.core.exploitation_prompt import build_exploitation_prompt
from src.core.source_review import prepare_source_review
from test_version_references import source

A = "CVE-2026-1234"
B = "CVE-2026-5678"


@pytest.mark.parametrize(
    "background",
    [
        f"For background, {B} was exploited in an earlier campaign.",
        f"## Background\n\n{B} was exploited in an earlier campaign.",
        f"Related reporting: {B} was exploited in an earlier campaign.",
        f"A separate patch-only issue {B} is also mentioned.",
    ],
)
def test_background_only_metadata_does_not_force_a_standalone_finding(background):
    article = source(f"Attackers are exploiting {A}.\n\n{background}")
    article["cves"] = [A, B]
    assert collect_exploitation_relevant_prompt_cves(
        format_article_summary(article)
    ) == [A]


def test_independent_current_evidence_is_not_lost_to_a_background_mention():
    article = source(
        f"Attackers are exploiting {A}.\n\n"
        f"For background, {B} was previously discussed.\n\n"
        f"New telemetry confirms attackers are exploiting {B}."
    )
    article["cves"] = [A, B]
    assert set(
        collect_exploitation_relevant_prompt_cves(format_article_summary(article))
    ) == {A, B}


def test_prompt_groups_reporting_and_preserves_complete_evidence():
    content = f"{A} and {B} form an exploit chain.\n\nInstall the update only after backing up."
    prompt = build_exploitation_prompt(prepare_source_review([source(content)]))
    assert (
        "one finding per coherent vulnerability or explicitly supported exploit chain"
        in prompt
    )
    assert "additional articles belong in that finding's Reporting field" in prompt
    assert "Background-only mentions do not require standalone findings" in prompt
    assert "at most two concise sentences" in prompt
    assert content in prompt
    assert "complete recommendation blocks" in prompt
