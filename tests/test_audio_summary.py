from src.services.audio import extract_executive_summary


def test_extract_executive_summary_reads_named_section():
    report = """# Exploitation Report

## Executive Summary

First executive paragraph.

Second executive paragraph.

## Active Exploitation Details

### Example
- **Status**: Active.
"""

    assert extract_executive_summary(report) == (
        "First executive paragraph. Second executive paragraph."
    )


def test_extract_executive_summary_keeps_legacy_first_paragraph_fallback():
    report = """# Exploitation Report

Legacy executive paragraph.

## Active Exploitation Details

### Example
- **Status**: Active.
"""

    assert extract_executive_summary(report) == "Legacy executive paragraph."
