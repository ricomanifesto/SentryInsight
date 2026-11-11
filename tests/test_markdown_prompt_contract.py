"""Prompt instructions match the fail-closed bold-list content contract."""

from src.core.exploitation_prompt import build_exploitation_prompt
from src.core.source_review import prepare_source_review


def test_prompt_requires_complete_labels_and_supported_descriptions():
    plan = prepare_source_review(
        [
            {
                "title": "Gateway advisory",
                "source": "Vendor",
                "link": "https://vendor.example/advisory",
                "content": "CVE-2026-1234 is actively exploited. Install the update.",
            }
        ]
    )
    prompt = build_exploitation_prompt(plan)
    assert "close the emphasis and include a meaningful description" in prompt
    assert "Never emit a label alone" in prompt
    assert "Do not invent a description to fill missing evidence" in prompt
