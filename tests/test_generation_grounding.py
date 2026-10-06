import asyncio
import hashlib
import json
from unittest.mock import AsyncMock

import pytest

from src.core import finding_evidence
from src.core.reporting import build_reporting_catalog, serialize_reporting_catalog
from test_analyze_guards import import_analyze_with_stubs
from test_workflow_guards import import_workflow_with_stubs

CVE = "CVE-2026-1234"
OTHER = "CVE-2026-5678"
ABSENT = finding_evidence.ABSENT


def source(content, **extra):
    return dict(
        title="Example Gateway advisory",
        source="Example publisher",
        link="https://example.test/advisory?token=private-url-value",
        content=content,
        **extra,
    )


def finding(key, versions=ABSENT, title="Example Gateway"):
    return f"""### {title} ({CVE})
- **Description**: A service flaw.
- **Exploitation Status**: active
- **Action**: monitor
- **CVE IDs**: {CVE}
- **Reporting**: {key}
- **Affected Versions**: {versions}
- **Exceptions**: {ABSENT}
- **Recommended Actions**: {ABSENT}
- **Vendor Links**: {ABSENT}

"""


def test_prompt_exposes_validator_scope_without_losing_full_article(monkeypatch):
    analyze = import_analyze_with_stubs()
    content = (
        f"{CVE} is actively exploited.\n\n"
        "The issue has been addressed in the following versions:\n\n"
        "Example Gateway 14.1-73.41 and later releases\n\n"
        f"{OTHER} is also mentioned."
    )
    client = type("Client", (), {"generate": AsyncMock(return_value="candidate")})()
    monkeypatch.setattr(analyze, "build_model_client", lambda **_: client)
    result = asyncio.run(analyze.analyze_exploitation([source(content)], {}))
    prompt = client.generate.call_args.kwargs["user_prompt"]
    assert content in prompt
    context = json.loads(
        prompt.split("BEGIN SCOPED FINDING DETAIL EVIDENCE\n", 1)[1].split(
            "\nEND SCOPED FINDING DETAIL EVIDENCE", 1
        )[0]
    )
    scoped = next(item for item in context if item["cves"] == [CVE])
    assert "14.1-73.41" not in json.dumps(scoped)
    assert "fixed releases are not affected releases" in prompt.lower()
    assert "do not infer earlier affected ranges" in prompt.lower()
    assert result["reporting_sources"][0]["content"] == content
    assert client.generate.await_count == 1


def test_context_keeps_heading_ownership_qualifiers_and_recommendation_blocks():
    content = (
        f"## {CVE}\n\nAffected versions:\n\n"
        "Example Gateway 2.3 (Windows only)\n\n"
        "Customers should install the patch. Restart the service afterward.\n\n"
        f"## {OTHER}\n\nAffected versions:\n\nOther Product 9.0"
    )
    context = finding_evidence.build_finding_detail_context(
        build_reporting_catalog([source(content)])
    )
    scoped = next(item for item in context if item["cves"] == [CVE])
    assert "Example Gateway 2.3 (Windows only)" in json.dumps(scoped)
    assert "Other Product 9.0" not in json.dumps(scoped)
    assert any(
        span.get("source_block")
        == "Customers should install the patch. Restart the service afterward."
        for span in scoped["spans"]
    )
    assert any(span["role"] == "heading" for span in scoped["spans"])


@pytest.mark.parametrize(
    ("versions", "code"),
    [
        ("Example Gateway 14.1 is affected", "ambiguous_affected_version_clause"),
        ("Example Gateway before 14.1-73.41", "affected_version_not_grounded"),
    ],
)
def test_failure_diagnostic_identifies_finding_without_leaking_text(
    versions, code, tmp_path, caplog
):
    workflow = import_workflow_with_stubs()
    secret = "PRIVATE-SOURCE-AND-CANDIDATE-TEXT"
    catalog = build_reporting_catalog(
        [source(f"{CVE} is actively exploited.\n\n{secret}")]
    )
    key = next(iter(catalog))
    report = "## Active Exploitation Details\n\n" + finding(key)
    report += finding(key, versions, title=secret)
    output = tmp_path / "index.md"
    output.write_text("Last valid report")
    fingerprint = tmp_path / ".sentryinsight-articles-fingerprint"
    fingerprint.write_text("Last valid fingerprint")
    state = {
        "analysis_results": {
            "exploitation_report": report,
            "reporting_sources": serialize_reporting_catalog(catalog),
        },
        "config": {"output_path": str(output)},
        "status": "started",
    }
    with caplog.at_level("ERROR", logger="src.core.workflow"):
        result = asyncio.run(workflow.generate_report(state))
    message = next(
        record.getMessage()
        for record in caplog.records
        if record.getMessage().startswith("Report grounding failed: ")
    )
    diagnostic = json.loads(message.split("Report grounding failed: ", 1)[1])
    assert diagnostic["code"] == code
    assert diagnostic["finding_index"] == 2
    assert diagnostic["cves"] == [CVE]
    assert diagnostic["report_sha256"] == hashlib.sha256(report.encode()).hexdigest()
    assert diagnostic["sources"][0]["key"] == key
    assert len(diagnostic["sources"][0]["content_sha256"]) == 64
    assert secret not in caplog.text
    assert "private-url-value" not in caplog.text
    assert versions not in caplog.text
    assert result["status"] == "failed"
    assert output.read_text() == "Last valid report"
    assert fingerprint.read_text() == "Last valid fingerprint"


def test_multi_cve_patched_versions_and_inferred_ranges_still_fail_closed():
    catalog = build_reporting_catalog(
        [
            source(
                f"{CVE} is actively exploited.\n\nPatched in Example Gateway 14.1-73.41.\n\n{OTHER} is also mentioned."
            )
        ]
    )
    key = next(iter(catalog))
    prefix = "## Active Exploitation Details\n\n"
    for versions in ("Example Gateway 14.1-73.41", "Example Gateway before 14.1-73.41"):
        with pytest.raises(finding_evidence.EvidenceError):
            finding_evidence.validate_finding_evidence(
                prefix + finding(key, versions), catalog
            )
    finding_evidence.validate_finding_evidence(prefix + finding(key), catalog)


def test_ambiguous_source_scope_is_explicit_and_still_blocks_publication():
    catalog = build_reporting_catalog(
        [
            source(
                f"{CVE} is actively exploited. Customers should install the update for {OTHER}."
            )
        ]
    )
    context = finding_evidence.build_finding_detail_context(catalog)
    scoped = next(item for item in context if item["cves"] == [CVE])
    assert scoped["scope_error"] == "ambiguous_detail_scope"
    assert "spans" not in scoped
    with pytest.raises(
        finding_evidence.EvidenceError, match="ambiguous recommendation block"
    ):
        finding_evidence.validate_finding_evidence(
            "## Active Exploitation Details\n\n" + finding(next(iter(catalog))), catalog
        )


def test_scopes_retain_all_sources_including_uncited_negative_evidence():
    articles = [
        source(f"{CVE} is actively exploited.", content_kind="article"),
        dict(
            source(f"{CVE} has not been exploited."),
            link="https://example.test/negative",
        ),
    ]
    catalog = build_reporting_catalog(articles)
    context = finding_evidence.build_finding_detail_context(catalog)
    assert {item["source_key"] for item in context} == set(catalog)
    assert "has not been exploited" in json.dumps(context)
    with pytest.raises(
        finding_evidence.EvidenceError, match="unsupported exploitation status"
    ):
        finding_evidence.validate_finding_evidence(
            "## Active Exploitation Details\n\n" + finding(next(iter(catalog))), catalog
        )


def test_diagnostics_bound_sources_cves_and_unknown_metadata():
    cves = (CVE, "CVE-2026-" + "9" * 10000)
    cves += tuple(f"CVE-2026-{1000 + i}" for i in range(39))
    error = finding_evidence.EvidenceError("PRIVATE ERROR")
    error.cves = cves
    catalog = build_reporting_catalog(
        [
            dict(
                source(f"{CVE} is actively exploited.", content_kind="PRIVATE KIND"),
                link=f"https://example.test/{i}",
            )
            for i in range(40)
        ]
    )
    diagnostic = finding_evidence.grounding_failure_diagnostic(
        "PRIVATE REPORT", catalog, error
    )
    encoded = json.dumps(diagnostic)
    assert len(encoded) < 10000
    assert "PRIVATE" not in encoded
    assert len(diagnostic["sources"]) == 32
    assert diagnostic["sources_truncated"] == 8
    assert len(diagnostic["cves"]) == 32
    assert diagnostic["cves_truncated"] == 9
    assert all(item["content_kind"] == "unknown" for item in diagnostic["sources"])


def test_invalid_catalog_logs_no_untrusted_source_key(tmp_path, caplog):
    workflow = import_workflow_with_stubs()
    records = serialize_reporting_catalog(
        build_reporting_catalog([source(f"{CVE} is actively exploited.")])
    )
    records[0]["key"] = "PRIVATE INVALID KEY"
    with caplog.at_level("ERROR", logger="src.core.workflow"):
        result = asyncio.run(
            workflow.generate_report(
                {
                    "analysis_results": {
                        "exploitation_report": "PRIVATE CANDIDATE",
                        "reporting_sources": records,
                    },
                    "config": {"output_path": str(tmp_path / "index.md")},
                    "status": "started",
                }
            )
        )
    assert result["status"] == "failed"
    assert "PRIVATE" not in caplog.text
    assert "reporting_identity_rejected" in caplog.text
    assert not (tmp_path / "index.md").exists()


def test_scope_metadata_does_not_expand_unrelated_prose_for_each_cve():
    content = f"{CVE} is actively exploited.\n\n"
    content += "Unattributed context for another product.\n\n" * 200
    content += f"{OTHER} is actively exploited."
    context = finding_evidence.build_finding_detail_context(
        build_reporting_catalog([source(content)])
    )
    assert len(json.dumps(context)) < len(content)
    assert "Unattributed context" not in json.dumps(context)
    assert "actively exploited" in json.dumps(context)


@pytest.mark.parametrize(
    ("content", "expected"),
    [
        (
            f"Attackers are exploiting the service. The issue is tracked as {CVE}.",
            "unknown",
        ),
        (f"{CVE} is actively exploited.", "active"),
        (f"{CVE} may be exploited in the wild.", "potential"),
    ],
)
def test_context_includes_the_validator_exploitation_assessment(content, expected):
    catalog = build_reporting_catalog([source(content)])
    context = finding_evidence.build_finding_detail_context(catalog)
    assert context[0]["exploitation"] == {"status": expected, "conflicting": False}
    prefix = "## Active Exploitation Details\n\n"
    candidate = finding(next(iter(catalog))).replace(
        "**Exploitation Status**: active", f"**Exploitation Status**: {expected}"
    )
    finding_evidence.validate_finding_evidence(prefix + candidate, catalog)


def test_context_assessment_cannot_drop_an_uncited_negative_source():
    catalog = build_reporting_catalog(
        [
            source(f"{CVE} is actively exploited."),
            dict(
                source(f"{CVE} has not been exploited."),
                link="https://example.test/negative",
            ),
        ]
    )
    context = finding_evidence.build_finding_detail_context(catalog)
    assert all(
        item["exploitation"] == {"status": "unknown", "conflicting": True}
        for item in context
    )


@pytest.mark.parametrize("ownership", ["heading", "sentence", "paragraph"])
def test_joint_scopes_preserve_shared_details_and_recommendations(ownership):
    confirmation = f"{CVE} is actively exploited. {OTHER} is actively exploited."
    if ownership == "heading":
        details = f"## {CVE} and {OTHER}\n\nAffected versions:\n\nExample Gateway 2.3"
        recommendation = "Customers should install the update."
    elif ownership == "sentence":
        details = f"Affected versions: Example Gateway 2.3 ({CVE}, {OTHER})"
        recommendation = f"Customers should install the update for {CVE} and {OTHER}."
    else:
        details = ""
        recommendation = f"Customers should install the update for {CVE}. Apply the patch for {OTHER}."
    catalog = build_reporting_catalog(
        [source(f"{confirmation}\n\n{details}\n\n{recommendation}")]
    )
    context = finding_evidence.build_finding_detail_context(catalog)
    joint = next(item for item in context if set(item["cves"]) == {CVE, OTHER})
    assert joint["exploitation"] == {"status": "active", "conflicting": False}
    assert any(span.get("source_block") == recommendation for span in joint["spans"])
    candidate = finding(
        next(iter(catalog)), "Example Gateway 2.3" if details else ABSENT
    )
    candidate = candidate.replace(CVE, f"{CVE}, {OTHER}").replace(
        f"**Recommended Actions**: {ABSENT}",
        f"**Recommended Actions**: {recommendation}",
    )
    finding_evidence.validate_finding_evidence(
        "## Active Exploitation Details\n\n" + candidate, catalog
    )


@pytest.mark.parametrize("cves", [(), (CVE,)])
def test_diagnostic_keeps_cited_sources_ahead_of_uncited_context(cves):
    catalog = build_reporting_catalog(
        [
            dict(
                source(f"{CVE} is actively exploited."),
                link=f"https://example.test/{i}",
            )
            for i in range(40)
        ]
    )
    selected_key = list(catalog)[-1]
    error = finding_evidence.EvidenceError("rejected")
    error.cves = cves
    error.source_keys = (selected_key,)
    diagnostic = finding_evidence.grounding_failure_diagnostic(
        "candidate", catalog, error
    )
    assert diagnostic["sources"][0]["key"] == selected_key
    assert len(diagnostic["sources"]) == 32
    assert diagnostic["sources_truncated"] == 8


def test_joint_scope_includes_details_from_other_sources_naming_one_member():
    shared = source(
        f"{CVE} is actively exploited. {OTHER} is actively exploited.\n\n## {CVE} and {OTHER}\n\nAffected versions:\n\nExample Gateway 2.3"
    )
    extra = dict(
        source(
            f"{CVE} is actively exploited.\n\nAffected versions:\n\nExample Gateway 2.4"
        ),
        link="https://example.test/extra",
    )
    catalog = build_reporting_catalog([shared, extra])
    context = finding_evidence.build_finding_detail_context(catalog)
    extra_key = list(catalog)[1]
    joint_extra = next(
        item
        for item in context
        if set(item["cves"]) == {CVE, OTHER} and item["source_key"] == extra_key
    )
    assert "Example Gateway 2.4" in json.dumps(joint_extra)
    prefix = "## Active Exploitation Details\n\n"
    candidate = finding(
        next(iter(catalog)), "Example Gateway 2.3; Example Gateway 2.4"
    ).replace(CVE, f"{CVE}, {OTHER}")
    finding_evidence.validate_finding_evidence(prefix + candidate, catalog)
    with pytest.raises(
        finding_evidence.EvidenceError, match="omits supplied version list"
    ):
        finding_evidence.validate_finding_evidence(
            prefix + candidate.replace("; Example Gateway 2.4", ""), catalog
        )
