from __future__ import annotations

import pytest

from src.core.report_artifact import ReportArtifactError, parse_report_artifact
from src.core.reporting import (
    ReportingGroundingError,
    build_reporting_catalog,
    reporting_key,
    resolve_reporting_keys,
)

from test_report_artifact import REPORT

ARTICLES = [
    {
        "title": "Critical vendor flaw exploited",
        "source": "Example Security",
        "link": "https://example.com/security/advisory",
        "summary": "Attackers exploit CVE-2026-1234 in the wild.",
        "cves": ["CVE-2026-1234"],
    },
    {
        "title": "Independent follow-up",
        "source": "Research Team",
        "link": "https://research.example.net/follow-up",
        "summary": "Researchers independently observed exploitation.",
    },
]


def _v2_report(reporting: str) -> str:
    return (
        REPORT.replace("schema_version: 1", "schema_version: 2")
        .replace(
            "generated_at: 2026-08-13T13:21:22Z",
            "generated_at: 2026-08-13T13:21:22Z\n"
            "digest_issue_url: https://ricomanifesto.github.io/"
            "SentryDigest/archive/2026-08-13/",
        )
        .replace(
            "- **CVE IDs**: CVE-2026-1234, CVE-2026-12345678",
            "- **CVE IDs**: CVE-2026-1234, CVE-2026-12345678\n"
            f"- **Reporting**: {reporting}",
        )
        .replace(
            "- **Action**: investigate",
            "- **Action**: investigate\n"
            "- **Reporting**: [Research Team — Independent follow-up]"
            "(https://research.example.net/follow-up)",
        )
    )


def test_reporting_keys_are_stable_and_catalog_only_contains_safe_input_urls():
    catalog = build_reporting_catalog(ARTICLES)

    assert reporting_key(ARTICLES[0]["link"]) == "source-cc16b55febdc"
    assert tuple(catalog) == ("source-cc16b55febdc", "source-3cf317481a19")
    assert catalog["source-cc16b55febdc"].publisher == "Example Security"


def test_model_source_keys_resolve_to_input_owned_markdown_links():
    key = reporting_key(ARTICLES[0]["link"])
    model_report = REPORT.replace(
        "- **CVE IDs**: CVE-2026-1234, CVE-2026-12345678",
        "- **CVE IDs**: CVE-2026-1234, CVE-2026-12345678\n" f"- **Reporting**: {key}",
    ).replace(
        "- **Action**: investigate",
        f"- **Action**: investigate\n- **Reporting**: {reporting_key(ARTICLES[1]['link'])}",
    )

    resolved = resolve_reporting_keys(model_report, build_reporting_catalog(ARTICLES))

    assert (
        "[Example Security — Critical vendor flaw exploited]"
        "(https://example.com/security/advisory)" in resolved
    )
    assert "source-cc16b55febdc" not in resolved


def test_model_cannot_publish_an_unknown_or_authored_reporting_url():
    catalog = build_reporting_catalog(ARTICLES)
    for value in (
        "source-000000000000",
        "[Invented](https://invented.example/report)",
    ):
        model_report = REPORT.replace(
            "- **CVE IDs**: CVE-2026-1234, CVE-2026-12345678",
            "- **CVE IDs**: CVE-2026-1234, CVE-2026-12345678\n"
            f"- **Reporting**: {value}",
        )
        with pytest.raises(ReportingGroundingError):
            resolve_reporting_keys(model_report, catalog)


def test_schema_v2_requires_valid_reporting_on_every_finding():
    report = _v2_report(
        "[Example Security — Critical vendor flaw exploited]"
        "(https://example.com/security/advisory)"
    )
    artifact = parse_report_artifact(report)

    assert artifact.schema_version == 2
    assert artifact.digest_issue_url.endswith("/archive/2026-08-13/")
    assert artifact.findings[0].reporting[0].publisher == "Example Security"
    assert artifact.findings[0].reporting[0].digest_fragment == "reporting-cc16b55febdc"

    with pytest.raises(ReportArtifactError, match="Reporting"):
        parse_report_artifact(report.replace("- **Reporting**:", "- **Evidence**:", 1))


@pytest.mark.parametrize(
    "digest_url",
    [
        "https://ricomanifesto.github.io/SentryDigest/",
        "https://ricomanifesto.github.io/SentryDigest/archive/2026-08-12/",
        "javascript:alert(1)",
    ],
)
def test_schema_v2_requires_the_report_date_digest_issue(digest_url):
    report = _v2_report(
        "[Example Security — Critical vendor flaw exploited]"
        "(https://example.com/security/advisory)"
    )
    report = report.replace(
        "https://ricomanifesto.github.io/SentryDigest/archive/2026-08-13/",
        digest_url,
    )

    with pytest.raises(ReportArtifactError, match="digest_issue_url"):
        parse_report_artifact(report)
