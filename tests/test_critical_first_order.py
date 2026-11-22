"""Critical findings first, every other severity equal, stable inside both groups.

The order is applied once, late, to the fresh candidate. Historical artifacts,
other sections and finding/source coverage are unchanged, and the real site
renderer shows the same order with valid disclosure and anchor wiring.
"""

import json
from html.parser import HTMLParser
from pathlib import Path

import pytest

from scripts.build_site import build_site
from src.core import report_validation, reviewed_report
from src.core.report_artifact import parse_report_artifact, slugify
from src.core.report_findings import report_findings
from src.core.report_validation import (
    ReportPreparationError,
    order_active_findings,
    prepare_generated_report,
)
from src.core.reviewed_report import (
    ReviewedReportValidationError,
    resolve_reviewed_analysis,
)
from report_recovery_fixtures import (
    ALPHA_ADVISORY,
    BETA_ADVISORY,
    TRAILER,
    article,
    finding,
    id_for,
    key_for,
    prepared_result,
    report,
    standard_articles,
)

ROOT = Path(__file__).resolve().parents[1]
LABELS = ("Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel")
SEVERITIES = (
    "Critical",
    "Critical",
    "Critical",
    "Critical",
    "Unknown",
    "Critical",
    "Unknown",
    "Unknown",
)
EXPECTED = ("Alpha", "Bravo", "Charlie", "Delta", "Foxtrot", "Echo", "Golf", "Hotel")
REQUIRED_CVE = "CVE-2099-900001"


def title(label):
    return f"Synthetic {label} gateway campaign"


def findings_for(severities, labels=None):
    labels = labels or LABELS[: len(severities)]
    return "".join(
        finding(title(label), [key_for("alpha")], severity=severity)
        for label, severity in zip(labels, severities, strict=True)
    )


def titles(text):
    return [row.title for row in report_findings(text).rows]


def labels_of(text):
    return [value.split()[1] for value in titles(text)]


# Unit: the ordering function


def test_mixed_severities_put_critical_first_and_keep_both_groups_stable():
    text = report(
        findings_for(
            ["medium", "high", "critical", "unknown", "critical"],
            ["Alpha", "Bravo", "Charlie", "Delta", "Echo"],
        )
    )
    ordered = order_active_findings(text)
    assert labels_of(ordered) == ["Charlie", "Echo", "Alpha", "Bravo", "Delta"]
    assert sorted(row.text for row in report_findings(ordered).rows) == sorted(
        row.text for row in report_findings(text).rows
    )


@pytest.mark.parametrize(
    "severities",
    [
        ["critical", "critical", "high"],
        ["high", "medium", "low", "unknown"],
        ["unknown", "low", "medium", "high"],
        ["critical"],
        ["low"],
        ["Critical", "CRITICAL", "critical"],
    ],
    ids=[
        "already-ordered",
        "no-critical",
        "no-critical-reverse",
        "single-critical",
        "single-other",
        "all-critical",
    ],
)
def test_already_ordered_or_single_group_reports_are_byte_identical(severities):
    text = report(findings_for(severities))
    assert order_active_findings(text) is text


def test_critical_last_moves_first_with_case_insensitive_values():
    text = report(findings_for(["Unknown", "High", "CRITICAL"]))
    assert labels_of(order_active_findings(text)) == ["Charlie", "Alpha", "Bravo"]


def test_text_outside_the_finding_blocks_is_unchanged():
    summary = (
        "A critical campaign is described below. Exploitation status is unknown.\n\n"
        "Review the source details before choosing a response.\n\n"
    )
    trailer = TRAILER.replace(
        "## Attack Vectors and Techniques\n\n",
        "### Critical notes\n\n- A critical component is named.\n\n"
        "## Attack Vectors and Techniques\n\n",
    )
    text = report(
        findings_for(["unknown", "critical"]), summary=summary, trailer=trailer
    )
    ordered = order_active_findings(text)
    before, after = report_findings(text), report_findings(ordered)
    assert labels_of(ordered) == ["Bravo", "Alpha"]
    assert ordered[: after.rows[0].start] == text[: before.rows[0].start]
    assert ordered[after.rows[-1].end :] == text[before.rows[-1].end :]
    assert len(ordered) == len(text)


def test_report_without_a_finding_section_is_unchanged():
    text = "# Exploitation Report\n\n## Executive Summary\n\nNothing to order.\n"
    assert order_active_findings(text) is text


FENCED_SECTION = (
    "```\n## Active Exploitation Details\n```\n\n"
    "Review the source details before choosing a response.\n\n"
)


@pytest.mark.parametrize(
    "mutate",
    [
        lambda text: text.replace(
            "Review the source details before choosing a response.\n\n",
            FENCED_SECTION,
        ),
        lambda text: text.replace(
            "- **Vendor Links**",
            "```\n### Hidden heading\n```\n- **Vendor Links**",
            1,
        ),
        lambda text: text.replace(
            "- **Vendor Links**",
            "```\n- **Severity**: critical\n```\n- **Vendor Links**",
            1,
        ),
        lambda text: text.replace("- **Severity**: unknown\n", "", 1),
        lambda text: text.replace("**Severity**: unknown", "**Severity**: urgent", 1),
        lambda text: text.replace(
            "- **Severity**: unknown\n",
            "- **Severity**: unknown\n- **Severity**: critical\n",
            1,
        ),
    ],
    ids=[
        "fenced-section-lookalike",
        "fenced-heading-lookalike",
        "fenced-severity-lookalike",
        "missing-severity",
        "unknown-severity-value",
        "repeated-severity",
    ],
)
def test_ambiguous_or_unrankable_structure_rejects_the_candidate(mutate):
    text = mutate(report(findings_for(["unknown", "critical"])))
    with pytest.raises(ReportPreparationError):
        order_active_findings(text)


def test_a_reorder_that_changes_a_reference_target_is_rejected():
    text = report(findings_for(["unknown", "critical"]))
    rows = report_findings(text).rows
    first = rows[0].text.rstrip("\n") + "\n\n[ref]: https://a.example.test/one\n\n"
    second = rows[1].text.rstrip("\n") + "\n\n[ref]: https://b.example.test/two\n\n"
    text = text[: rows[0].start] + first + second + text[rows[1].end :]
    with pytest.raises(ReportPreparationError) as caught:
        order_active_findings(text)
    assert str(caught.value) == "finding_order_changes_reference_targets"


def test_shared_preparation_does_not_reorder():
    text = report(findings_for(["unknown", "critical"]))
    assert prepare_generated_report(text) == text


# Pipeline and renderer


def eight_finding_report():
    rows = []
    for label, severity in zip(LABELS, SEVERITIES, strict=True):
        keys = [key_for("alpha")]
        links = "Not stated in supplied sources."
        if label == "Echo":
            links = id_for("alpha", ALPHA_ADVISORY)
        if label == "Foxtrot":
            keys = [key_for("alpha"), key_for("beta")]
            links = id_for("beta", BETA_ADVISORY)
        rows.append(finding(title(label), keys, severity=severity, vendor_links=links))
    return report("".join(rows))


def resolve(text, *, advisory=False, articles=None):
    return resolve_reviewed_analysis(
        prepared_result(articles or standard_articles(), text), advisory=advisory
    )


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.controls, self.bodies = [], [], []
        self.anchors, self.toc, self.titles, self.hrefs = [], [], [], []
        self._title = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = (attributes.get("class") or "").split()
        if "id" in attributes:
            self.ids.append(attributes["id"])
        if tag == "button" and "finding-disclosure" in classes:
            self.controls.append(attributes.get("aria-controls"))
        if tag == "div" and "finding-body" in classes:
            self.bodies.append(attributes.get("id"))
        if tag == "a" and "href" in attributes:
            self.hrefs.append(attributes["href"])
            if "heading-anchor" in classes:
                self.anchors.append(attributes["href"])
            if "finding-link" in classes:
                self.toc.append(attributes["href"])
        if tag == "span" and "finding-title" in classes:
            self._title = True
            self.titles.append("")

    def handle_endtag(self, tag):
        if tag == "span":
            self._title = False

    def handle_data(self, data):
        if self._title:
            self.titles[-1] += data


@pytest.mark.parametrize("advisory", [False, True], ids=["strict", "advisory"])
def test_eight_findings_render_critical_first_in_markdown_and_html(
    advisory, tmp_path, monkeypatch
):
    articles = standard_articles()
    articles[1] = article(
        "beta", [BETA_ADVISORY], f"{REQUIRED_CVE} may be exploited in the wild."
    )
    original_report = eight_finding_report()
    original = next(
        row.text
        for row in report_findings(original_report).rows
        if row.title == title("Foxtrot")
    )
    grounded = finding(
        title("Foxtrot"),
        [key_for("beta")],
        severity="Critical",
        vendor_links=id_for("beta", BETA_ADVISORY, articles),
    ).replace(
        "- **Exploitation Status**: unknown\n",
        f"- **Exploitation Status**: potential\n- **CVE IDs**: {REQUIRED_CVE}\n",
        1,
    )
    text = original_report.replace(original, grounded, 1)
    candidate = resolve(text, advisory=advisory, articles=articles)
    with monkeypatch.context() as patch:
        patch.setattr(reviewed_report, "order_active_findings", lambda value: value)
        unordered = resolve(text, advisory=advisory, articles=articles)

    # Markdown: five Critical then three Unknown, stable inside both groups.
    assert labels_of(candidate.report) == list(EXPECTED)
    assert labels_of(unordered.report) == list(LABELS)
    ordered_rows = report_findings(candidate.report)
    unordered_rows = report_findings(unordered.report)
    assert sorted(row.text for row in ordered_rows.rows) == sorted(
        row.text for row in unordered_rows.rows
    )
    assert ordered_rows.outside() == unordered_rows.outside()
    assert candidate.coverage == unordered.coverage
    assert "link-" not in candidate.source
    artifact = parse_report_artifact(candidate.source)
    severities = [item.severity.value for item in artifact.findings]
    assert severities == ["critical"] * 5 + ["unknown"] * 3
    by_title = {item.title: item for item in artifact.findings}
    assert by_title[title("Echo")].vendor_links == (ALPHA_ADVISORY,)
    assert by_title[title("Foxtrot")].vendor_links == (BETA_ADVISORY,)
    assert by_title[title("Foxtrot")].cve_ids == (REQUIRED_CVE,)

    # HTML from the real site renderer.
    report_path = tmp_path / "index.md"
    report_path.write_text(candidate.source)
    output = tmp_path / "site"
    build_site(report_path=report_path, output_path=output, template_path=ROOT / "site")
    page = Page()
    page.feed((output / "index.html").read_text())
    slugs = [slugify(title(label)) for label in EXPECTED]
    assert page.titles == [title(label) for label in EXPECTED]
    assert len(set(slugs)) == 8
    assert page.controls == [f"{slug}-details" for slug in slugs]
    assert page.bodies == page.controls
    # Every disclosure target and heading anchor names exactly one element.
    for identifier in [*slugs, *page.controls]:
        assert page.ids.count(identifier) == 1
    assert page.anchors == [f"#{slug}" for slug in slugs]
    # The desktop and mobile navigation list the findings in the same order.
    assert page.toc == [f"#{slug}" for slug in slugs] * 2
    assert not any(href.lower().startswith("javascript:") for href in page.hrefs)
    manifest = json.loads((output / "current-findings.json").read_text())
    assert manifest["finding_count"] == 8
    assert manifest["cve_ids"] == [REQUIRED_CVE]

    missing_identity = original_report.replace(original, "", 1)
    narrative_only = missing_identity.replace(
        "Review the source details before choosing a response.",
        f"Review the source details for {REQUIRED_CVE} before choosing a response.",
        1,
    )
    for rejected in (missing_identity, narrative_only):
        with pytest.raises(ReviewedReportValidationError) as caught:
            resolve(rejected, advisory=advisory, articles=articles)
        assert [issue.code for issue in caught.value.issues] == [
            "missing_expected_cves"
        ]


@pytest.mark.parametrize("advisory", [False, True], ids=["strict", "advisory"])
def test_unrankable_candidate_is_a_handled_malformed_markdown_rejection(advisory):
    text = report(findings_for(["unknown", "critical"])).replace(
        "**Severity**: unknown", "**Severity**: urgent", 1
    )
    with pytest.raises(ReviewedReportValidationError) as caught:
        resolve(text, advisory=advisory)
    assert [issue.code for issue in caught.value.issues] == ["malformed_markdown"]


def test_historical_noncritical_first_artifact_parses_in_file_order(monkeypatch):
    monkeypatch.setattr(reviewed_report, "order_active_findings", lambda value: value)
    unordered = resolve(eight_finding_report())
    artifact = parse_report_artifact(unordered.source)
    assert [item.title for item in artifact.findings] == [
        title(label) for label in LABELS
    ]


@pytest.mark.parametrize("advisory", [False, True], ids=["strict", "advisory"])
def test_critical_first_ordering_is_applied_exactly_once(
    advisory, tmp_path, monkeypatch
):
    real_order = order_active_findings
    calls: list[dict[str, object]] = []
    stages: list[str] = []

    def spy_order(markdown: str) -> str:
        ordered = real_order(markdown)
        calls.append(
            {
                "stage": stages[-1] if stages else None,
                "before_labels": labels_of(markdown),
                "after_labels": labels_of(ordered),
                "has_link_id": "link-" in markdown,
            }
        )
        return ordered

    monkeypatch.setattr(reviewed_report, "order_active_findings", spy_order)
    monkeypatch.setattr(report_validation, "order_active_findings", spy_order)

    raw_report = eight_finding_report()
    candidate = resolve_reviewed_analysis(
        prepared_result(standard_articles(), raw_report),
        on_stage=stages.append,
        advisory=advisory,
    )
    artifact = parse_report_artifact(candidate.source)
    report_path = tmp_path / "index.md"
    report_path.write_text(candidate.source)
    output = tmp_path / "site"
    build_site(report_path=report_path, output_path=output, template_path=ROOT / "site")

    assert len(calls) == 1
    assert calls[0] == {
        "stage": "finding_evidence",
        "before_labels": list(LABELS),
        "after_labels": list(EXPECTED),
        "has_link_id": False,
    }
    assert labels_of(candidate.report) == list(EXPECTED)
    assert [item.title for item in artifact.findings] == [
        title(label) for label in EXPECTED
    ]
    assert (
        report_findings(candidate.grounded_report).outside()
        == report_findings(raw_report).outside()
    )
    assert real_order(candidate.grounded_report) is candidate.grounded_report

    page = Page()
    page.feed((output / "index.html").read_text())
    assert page.titles == [title(label) for label in EXPECTED]
