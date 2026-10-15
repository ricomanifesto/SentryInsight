"""Composed predicates preserve complete evidence through offline publication."""

import json
from pathlib import Path

import httpx
import pytest

from publication_evidence import capture_generated_evidence
from src.core import finding_generation
from src.core.content_fingerprint import FINGERPRINT_PATH
from src.core.finding_evidence import EvidenceError, validate_finding_evidence
from src.core.finding_generation import compile_finding_records
from src.core.report_artifact import parse_report_artifact
from src.core.reporting import build_reporting_catalog
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article
from test_publication_transaction import fail_install, tree
from test_publication_transaction import public as public  # noqa: F401

A = "CVE-2026-1234"
CASES = json.loads(
    (Path(__file__).parent / "fixtures/compositional_publication.json").read_text()
)


@pytest.fixture(autouse=True)
def no_transport(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real HTTP/model transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


def sources(case):
    return [
        article(text, link=f"https://example.test/composition/{i}")
        for i, text in enumerate(
            [case["source"]]
            + ([case["other_source"]] if "other_source" in case else [])
        )
    ]


@pytest.mark.parametrize("case", CASES, ids=lambda row: row["id"])
def test_complete_graph_and_all_published_views(monkeypatch, public, case):
    before = tree(public)
    inputs = sources(case)
    baseline_for = capture_generated_evidence(monkeypatch)
    accepted = case["future_status"] == "completed"
    result = run_real_pipeline(
        monkeypatch, public / "index.md", articles=inputs, expect_model_call=accepted
    )
    assert result["status"] == case["future_status"], result
    if not accepted:
        assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
        assert tree(public) == before
        return
    report = (public / "index.md").read_text()
    catalog = build_reporting_catalog(inputs)
    baseline_for(report, catalog)
    records = compile_finding_records(catalog)
    artifact = parse_report_artifact(report)
    assert len(artifact.findings) == len(records)
    for finding, record in zip(artifact.findings, records, strict=True):
        fields = dict(record.fields)
        assert finding.exploitation_status.value == record.status
        assert finding.action.value == fields["Action"]
        assert finding.recommended_actions == fields["Recommended Actions"]
        if "expected_status" in case:
            assert finding.exploitation_status.value == case["expected_status"]
        if "expected_action" in case:
            assert finding.action.value == case["expected_action"]
        for cve, status in case.get("future_state_by_cve", {}).items():
            if cve in finding.cve_ids:
                assert finding.exploitation_status.value == status
    data = json.loads((public / "current-findings.json").read_text())
    assert data["finding_count"] == len(records)
    assert set(data["cve_ids"]) == {c for r in records for c in r.cves}
    for name in (
        "index.html",
        "reports/index.html",
        "reports/index.json",
        "sitemap.xml",
        "assets/report.js",
        "assets/site.css",
        FINGERPRINT_PATH,
    ):
        assert (public / name).stat().st_size
    archive = [
        p
        for p in (public / "reports").glob("*.md")
        if p.read_bytes() == before["index.md"]["data"]
    ]
    assert len(archive) == 1
    assert archive[0].with_suffix(".html").stat().st_size


GUIDANCE = [
    ("Users should download the patch.", "none"),
    ("Users should download and install the vendor patch.", "patch"),
    ("Users should download or install the patch.", "none"),
    ("Users should not download and install the patch.", "none"),
    ("Users should download and install the patch only if exposed.", "none"),
    ("The vendor recommends users install the patch.", "patch"),
    ("The vendor does not recommend that you install the update.", "none"),
    ("The vendor does not recommend users install the patch.", "none"),
]


@pytest.mark.parametrize("advice,action", GUIDANCE)
def test_actual_generated_guidance_mutations(monkeypatch, public, advice, action):
    source = article(f"## {A}\n\nAttackers have exploited {A}.\n\n{advice}")
    catalog = build_reporting_catalog([source])
    baseline_for = capture_generated_evidence(monkeypatch)
    result = run_real_pipeline(monkeypatch, public / "index.md", articles=[source])
    assert result["status"] == "completed", result
    report = (public / "index.md").read_text()
    (finding,) = parse_report_artifact(report).findings
    assert finding.action.value == action
    assert finding.recommended_actions == advice
    baseline = baseline_for(report, catalog)
    evidence = next(
        line for line in baseline.splitlines() if "**Source Evidence**:" in line
    )
    guidance = next(
        line for line in baseline.splitlines() if "**Recommended Actions**:" in line
    )
    mutations = [
        (
            baseline.replace(
                "**Exploitation Status**: observed", "**Exploitation Status**: active"
            ),
            "unsupported_exploitation_status",
            "Exploitation Status",
        ),
        (
            baseline.replace(
                evidence, evidence.replace("have exploited", "are exploiting")
            ),
            "incomplete_source_evidence",
            "Source Evidence",
        ),
        (
            baseline.replace(guidance, "- **Recommended Actions**: Install the patch."),
            "recommendation_not_grounded",
            "Recommended Actions",
        ),
    ]
    before = tree(public)
    for damaged, code, field in mutations:
        assert damaged != baseline
        with pytest.raises(EvidenceError) as failure:
            validate_finding_evidence(damaged, catalog)
        assert (failure.value.code, failure.value.field) == (code, field)
        assert tree(public) == before
    # An arbitrary manual action edit is checked against the immutable record;
    # the evidence validator does not promise to reject arbitrary badge edits.
    if action == "none":
        damaged = report.replace("**Action**: none", "**Action**: patch")
        assert parse_report_artifact(damaged).findings[0].action.value != action


@pytest.mark.parametrize(
    "operation", ["replace_before", "replace_after", "fingerprint_partial"]
)
@pytest.mark.parametrize(
    "text",
    [
        f"{A} has been under limited, targeted exploitation.",
        f"Attackers have been exploiting {A}.\n\nUsers should download and install the patch.",
        f"{A} has been exploited.\n\nThe vendor does not recommend users install the patch.",
    ],
)
def test_composed_report_publication_faults_restore_full_tree(
    monkeypatch, public, text, operation
):
    before = tree(public)
    fired = []
    if operation.startswith("replace"):
        fired = fail_install(
            monkeypatch, public, target="index.html", after=operation.endswith("after")
        )
    else:
        original = Path.write_text

        def write(path, value, *args, **kwargs):
            if path.name == FINGERPRINT_PATH and path.parent.name == "staged":
                path.write_bytes(value[:7].encode())
                fired.append("fingerprint")
                raise OSError("fingerprint interrupted")
            return original(path, value, *args, **kwargs)

        monkeypatch.setattr(Path, "write_text", write)
    result = run_real_pipeline(
        monkeypatch, public / "index.md", articles=[article(f"## {A}\n\n{text}")]
    )
    assert fired and result["status"] == "failed"
    assert result["failure"]["stage"] == "site_publication"
    assert "report_path" not in result
    assert tree(public) == before


@pytest.mark.parametrize(
    "mutation",
    [
        "badge",
        "prose",
        "evidence",
        "preparation",
        "reporter",
        "audience",
        "negation",
        "condition",
        "target",
        "progressive",
        "potential",
        "constraints",
    ],
)
def test_generated_report_mutations_fail_before_publication(
    monkeypatch, public, tmp_path, mutation
):
    observation = f"Attackers have exploited {A}."
    advice = "The vendor recommends users download and install the vendor patch only if exposed."
    if mutation == "negation":
        advice = "The vendor does not recommend users install the patch."
    elif mutation == "progressive":
        observation = f"Attackers have not been exploiting {A}."
    elif mutation == "potential":
        observation = f"Attackers may have exploited {A}."
    text = f"## {A}\n\n{observation}\n\n{advice}"
    if mutation == "constraints":
        text += f"\n\n{A} is exploitable if SRv6, which is supported only on some Nexus 9000 models, is turned on."
    source = article(text)
    catalog = build_reporting_catalog([source])
    baseline_for = capture_generated_evidence(monkeypatch)
    accepted = tmp_path / "accepted" / "index.md"
    result = run_real_pipeline(monkeypatch, accepted, articles=[source])
    assert result["status"] == "completed", result
    baseline = baseline_for(accepted.read_text(), catalog)
    if mutation in {"badge", "progressive", "potential"}:
        old, new = {
            "badge": ("observed", "active"),
            "progressive": ("unknown", "not_observed"),
            "potential": ("potential", "observed"),
        }[mutation]
        damaged = baseline.replace(
            f"**Exploitation Status**: {old}", f"**Exploitation Status**: {new}"
        )
        code, field = "unsupported_exploitation_status", "Exploitation Status"
    elif mutation == "prose":
        start = baseline.index("## Executive Summary\n\n") + len(
            "## Executive Summary\n\n"
        )
        end = baseline.index("\n\n## Active Exploitation Details", start)
        damaged = baseline[:start] + f"{A} is actively exploited." + baseline[end:]
        code, field = "unsupported_summary_exploitation_claim", "summary"
    elif mutation == "evidence":
        line = next(
            line for line in baseline.splitlines() if "**Source Evidence**:" in line
        )
        damaged = baseline.replace(
            line, line.replace("have exploited", "are exploiting")
        )
        code, field = "incomplete_source_evidence", "Source Evidence"
    elif mutation == "constraints":
        line = next(
            line for line in baseline.splitlines() if "**Source Constraints**:" in line
        )
        damaged = baseline.replace(
            line, "- **Source Constraints**: Not stated in supplied sources."
        )
        code, field = "source_constraints_not_grounded", "Source Constraints"
    else:
        line = next(
            line for line in baseline.splitlines() if "**Recommended Actions**:" in line
        )
        removed = {
            "preparation": "download and ",
            "reporter": "The vendor recommends ",
            "audience": "users ",
            "negation": "does not ",
            "condition": " only if exposed",
            "target": "vendor patch",
        }[mutation]
        damaged = baseline.replace(line, line.replace(removed, ""))
        code, field = "recommendation_not_grounded", "Recommended Actions"
    assert damaged != baseline
    with pytest.raises(EvidenceError) as failure:
        validate_finding_evidence(damaged, catalog)
    assert (failure.value.code, failure.value.field) == (code, field)
    before = tree(public)
    original = finding_generation.render_finding_plan

    def altered(*args, **kwargs):
        generated = original(*args, **kwargs)
        assert generated == baseline
        return damaged

    monkeypatch.setattr(finding_generation, "render_finding_plan", altered)
    result = run_real_pipeline(monkeypatch, public / "index.md", articles=[source])
    assert result["status"] == "failed", result
    assert result["failure"]["codes"] == [code]
    # The diagnostic allowlist omits Source Constraints even though the
    # validator exception identifies it; preserve that existing boundary.
    assert result["failure"]["field"] == (None if mutation == "constraints" else field)
    assert tree(public) == before


def test_foreign_reference_does_not_transfer_perfect_state(monkeypatch, public):
    before = tree(public)
    inputs = [
        article(
            f"## {A}\n\nAttackers have exploited {A}.", link="https://example.test/a"
        ),
        article(
            "## CVE-2026-5678\n\nCVE-2026-5678 has not been exploited.",
            link="https://example.test/b",
        ),
    ]
    result = run_real_pipeline(
        monkeypatch, public / "index.md", articles=inputs, mutation="cross_scope"
    )
    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "invalid_generation_plan"
    assert tree(public) == before
