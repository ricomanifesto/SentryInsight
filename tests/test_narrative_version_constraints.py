"""Bounded affirmative target prose, never inference from advice or telemetry."""

import pytest

from src.core.finding_evidence import ABSENT, EvidenceError, validate_finding_evidence
from src.core.reporting import build_reporting_catalog
from src.core.version_references import (
    build_version_reference_context,
    resolve_version_references,
)
from test_version_references import report, source

TARGET = "instances running versions 2.4.1 (July 23, 2026) or older"
ASSERTION = "Our incident response investigation identified an attack vector targeting "


def scope_for(text):
    catalog = build_reporting_catalog([source(text)])
    [scope] = build_version_reference_context(catalog)
    return catalog, scope


@pytest.mark.parametrize(
    "text,target",
    [
        (ASSERTION + TARGET + ".", TARGET),
        ("“" + ASSERTION + TARGET + ",” Gateway Project says.", TARGET),
        ('"' + ASSERTION + TARGET + '," Gateway Project said.', TARGET),
        (
            "An attack vector targets servers running version 3.2 or earlier.",
            "servers running version 3.2 or earlier",
        ),
        (
            "The investigation identified an attack vector targeting devices running versions older than 3.2.",
            "devices running versions older than 3.2",
        ),
    ],
)
def test_complete_affirmative_target_range_uses_exact_source_constraint(text, target):
    catalog, scope = scope_for(text)
    assert scope["state"] == "supported"
    assert not scope["absence_allowed"]
    [constraint] = scope["constraints"]
    assert constraint["text"] == target
    rendered = resolve_version_references(
        report(catalog, constraint["id"], cves="None", status="unknown"), catalog
    )
    assert f"**Affected Versions**: {target}" in rendered
    validate_finding_evidence(rendered, catalog)
    with pytest.raises(EvidenceError):
        resolve_version_references(
            report(catalog, cves="None", status="unknown"), catalog
        )


@pytest.mark.parametrize(
    "text",
    [
        "The investigation did not identify an attack vector targeting " + TARGET + ".",
        "The investigation may have identified an attack vector targeting "
        + TARGET
        + ".",
        "The investigation identified a suspected attack vector targeting "
        + TARGET
        + ".",
        "It is unclear whether the investigation identified an attack vector targeting "
        + TARGET
        + ".",
        ASSERTION + TARGET + " when a separate configuration is enabled.",
        ASSERTION + TARGET + "; later versions may also be affected.",
        ASSERTION + TARGET + " and urged users to install version 2.4.7.",
        ASSERTION + "instances running versions 2.4.1 or older except 2.4.0.",
        ASSERTION
        + "instances running versions 2.4.1 (users are not affected) or older.",
        ASSERTION + "instances running versions 2.4.1 (Windows only or older.",
        "We have no credible reports of thefts for users running the latest 2.4.7 release.",
        "The investigation focused on determining how an actor logged in to "
        + TARGET
        + ".",
        "“" + ASSERTION + TARGET + ",” Gateway Project denies.",
    ],
)
def test_unknown_or_mixed_target_prose_remains_blocked(text):
    catalog, scope = scope_for(text)
    assert scope["state"] == "blocked"
    assert not scope["unresolved_allowed"]
    with pytest.raises(EvidenceError):
        resolve_version_references(
            report(catalog, cves="None", status="unknown"), catalog
        )


def test_narrative_constraint_does_not_cover_other_unresolved_evidence():
    catalog, scope = scope_for(
        ASSERTION + TARGET + ".\n\nGateway versions earlier than 7 also permit access."
    )
    assert scope["state"] == "blocked"
    assert len(scope["constraints"]) == 1
    with pytest.raises(EvidenceError):
        resolve_version_references(
            report(
                catalog, scope["constraints"][0]["id"], cves="None", status="unknown"
            ),
            catalog,
        )


def test_narrative_constraint_cannot_be_omitted_or_have_qualifier_removed():
    catalog, scope = scope_for(
        "Affected versions: Gateway 3.4\n\nA separate observation follows.\n\n"
        + ASSERTION
        + TARGET
        + "."
    )
    assert scope["state"] == "supported"
    assert len(scope["constraints"]) == 2
    refs = "; ".join(c["id"] for c in scope["constraints"])
    rendered = resolve_version_references(
        report(catalog, refs, cves="None", status="unknown"), catalog
    )
    validate_finding_evidence(rendered, catalog)
    for tampered in (
        rendered.replace(" (July 23, 2026)", ""),
        rendered.replace(" or older", ""),
        rendered.replace(TARGET, ABSENT),
    ):
        with pytest.raises(EvidenceError):
            validate_finding_evidence(tampered, catalog)
    with pytest.raises(EvidenceError):
        resolve_version_references(
            report(
                catalog, scope["constraints"][0]["id"], cves="None", status="unknown"
            ),
            catalog,
        )


def test_target_range_and_exact_source_exclusion_remain_contradictory():
    catalog, scope = scope_for(
        ASSERTION
        + TARGET
        + ".\n\nAffected versions: users of "
        + TARGET
        + " are not affected."
    )
    assert scope["state"] == "blocked"
    assert "contradictory_version_constraints" in scope["failure_reasons"]
    with pytest.raises(EvidenceError):
        resolve_version_references(
            report(
                catalog, scope["constraints"][0]["id"], cves="None", status="unknown"
            ),
            catalog,
        )


def test_target_range_eval_adapter_uses_shared_resolution_offline(
    monkeypatch, tmp_path
):
    import asyncio
    from unittest.mock import AsyncMock

    from evals.grounding import model_task
    from evals.grounding.dataset import Article, TaskInput
    from src.core.reporting import serialize_reporting_catalog
    from src.core.version_references import PROTOCOL_KEY, PROTOCOL_VERSION

    monkeypatch.setenv("OPENROUTER_API_KEY", "synthetic-unused-key")
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    article = source(ASSERTION + TARGET + ".")
    catalog, scope = scope_for(article["content"])
    reference = scope["constraints"][0]["id"]
    raw = report(catalog, reference, cves="None", status="unknown")
    analyze = AsyncMock(
        return_value={
            PROTOCOL_KEY: PROTOCOL_VERSION,
            "exploitation_report": raw,
            "reporting_sources": serialize_reporting_catalog(catalog),
        }
    )
    monkeypatch.setattr(model_task, "analyze_exploitation", analyze)
    task = model_task.ModelTask(
        model="openrouter/example/model:free",
        receipts=tmp_path / "synthetic-receipts.jsonl",
        max_requests=1,
    )
    result = asyncio.run(
        task(
            TaskInput(
                name="synthetic-target-prose",
                articles=[Article(**article, source_links=[])],
                variant="baseline",
            )
        )
    )
    assert result == resolve_version_references(raw, catalog)
    validate_finding_evidence(result, catalog)
    assert analyze.await_count == 1
