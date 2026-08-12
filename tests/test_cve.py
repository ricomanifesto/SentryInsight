from src.core.cve import extract_cve_ids


def test_extract_cve_ids_normalizes_and_deduplicates_in_source_order():
    text = "CVE-2026-1234, cve 2026 1234, and CVE2025-99"

    assert extract_cve_ids(text) == ["CVE-2026-1234", "CVE-2025-99"]
