"""The findings table shared by every stage that reads finding sections."""

import hashlib
import uuid

import pytest

from src.core.finding_evidence import (
    EvidenceError,
    validate_finding_evidence,
    validate_vendor_links,
)
from src.core.report_findings import report_findings
from src.core.reporting import (
    ReportingGroundingError,
    build_reporting_catalog,
    reporting_key,
    resolve_reporting_keys,
)

URL = "https://example.test/advisory"
KEY = reporting_key(URL)

REPORT = f"""# Exploitation Report

## Executive Summary

Two findings.

## Active Exploitation Details

Preamble before the first finding.

### Example Server (CVE-2026-1001)
- **Severity**: high
- **CVE IDs**: CVE-2026-1002, CVE-2026-1001
- **Reporting**: {KEY}, source-000000000000
- **Severity**: critical

### CVE-2026-1003 in Widget
- **Reporting**:   {KEY}
- **Vendor Links**: https://different.test/vendor

## Affected Systems and Products

See findings.
"""


def test_rows_hold_each_finding_with_its_offsets_and_identity():
    table = report_findings(REPORT)
    first, second = table.rows

    assert table.has_section
    assert REPORT[table.section_start :].startswith("Preamble")
    assert REPORT[table.section_end :].startswith("## Affected Systems")
    for row in table.rows:
        assert REPORT[row.start : row.end] == row.text
        assert REPORT[row.body_start : row.end] == row.body
        assert row.sha256 == hashlib.sha256(row.text.encode()).hexdigest()
    assert (first.index, first.title) == (1, "Example Server (CVE-2026-1001)")
    # Duplicates stay visible in pairs; the map keeps the last value.
    assert [name for name, _ in first.pairs].count("Severity") == 2
    assert first.fields()["Severity"] == "critical"
    # The CVE IDs field comes before the heading, in source order.
    assert first.cves == ("CVE-2026-1002", "CVE-2026-1001")
    assert first.cited_keys == (KEY, "source-000000000000")
    assert second.index == 2
    assert second.cves == ("CVE-2026-1003",)
    assert [field["value"] for field in second.reporting_fields] == [KEY]


def test_fields_returns_a_fresh_map():
    row = report_findings(REPORT).rows[0]
    row.fields()["Severity"] = "low"
    assert row.fields()["Severity"] == "critical"


def test_absent_and_empty_sections_are_distinct():
    absent = report_findings("# Report\n\n## Executive Summary\n\nNone.\n")
    empty = report_findings("## Active Exploitation Details\n\nNo findings.\n")
    assert (absent.has_section, absent.rows) == (False, ())
    assert (empty.has_section, empty.rows) == (True, ())


def test_outside_and_render_keep_every_byte_outside_the_edits():
    table = report_findings(REPORT)
    assert table.outside() == (
        REPORT[: REPORT.index("## Active")] + REPORT[table.section_end :]
    )
    assert table.render([]) == REPORT
    first, second = table.rows
    rendered = table.render(
        [(first.start, first.end, "### A\n"), (second.start, second.end, "### B\n")]
    )
    assert rendered == (REPORT[: first.start] + "### A\n### B\n" + REPORT[second.end :])


def test_stages_reading_the_same_text_share_one_table():
    report = REPORT.replace("Two findings.", f"Run {uuid.uuid4().hex}.")
    catalog = build_reporting_catalog(
        [{"title": "Advisory", "source": "Vendor", "link": URL, "content": "Text."}]
    )
    before = report_findings.cache_info()

    with pytest.raises(EvidenceError) as vendor:
        validate_vendor_links(report, catalog)
    with pytest.raises(EvidenceError):
        validate_finding_evidence(report, catalog)
    with pytest.raises(ReportingGroundingError):
        resolve_reporting_keys(report, catalog)

    after = report_findings.cache_info()
    assert after.misses - before.misses == 1
    assert after.hits - before.hits >= 2
    row = report_findings(report).rows[1]
    assert vendor.value.code == "unsupported_vendor_link"
    assert (vendor.value.finding_index, vendor.value.cves) == (2, row.cves)
    assert vendor.value.source_keys == (KEY,)
    assert vendor.value.finding_sha256 == row.sha256
