"""Explicit complete host inputs for existing generation guard regressions.

Legacy canonical examples use exact source constraints; convert only exact
matching constraints to the live reference protocol. Invalid claims stay invalid.
"""

import re

from src.core.cve import extract_cve_ids
from src.core.reporting import (
    deserialize_reporting_catalog,
    serialize_reporting_catalog,
    FINDING_PATTERN,
    REPORTING_FIELD_PATTERN,
)
from src.core.source_review import (
    PLAN_KEY,
    plan_reporting_catalog,
    review_articles,
    digest,
)
from src.core.version_references import (
    PROTOCOL_KEY,
    PROTOCOL_VERSION,
    build_version_reference_context,
)


def reviewed_analysis(result):
    catalog = deserialize_reporting_catalog(result["reporting_sources"])
    plan = plan_reporting_catalog(catalog, {key: [] for key in catalog})
    result = {
        **result,
        PLAN_KEY: plan.packet,
        "reporting_sources": serialize_reporting_catalog(plan.catalog),
        "reporting_metadata_cves": {key: [] for key in catalog},
    }
    if PROTOCOL_KEY not in result:
        scopes = build_version_reference_context(catalog)

        def replace(finding):
            cves = sorted(
                extract_cve_ids(
                    finding["heading"]
                    + " "
                    + (
                        re.search(r"CVE IDs\*\*:\s*(.*)", finding["body"])[1]
                        if re.search(r"CVE IDs\*\*:\s*(.*)", finding["body"])
                        else ""
                    )
                )
            )
            reporting = REPORTING_FIELD_PATTERN.search(finding["body"])
            keys = (
                {key.strip() for key in reporting["value"].split(",")}
                if reporting
                else set()
            )
            body = finding["body"]
            for scope in scopes:
                if scope["cves"] != cves or not keys.intersection(scope["source_keys"]):
                    continue
                for constraint in scope["constraints"]:
                    field = re.search(r"(\*\*Affected Versions\*\*: )([^\n]+)", body)
                    if field and re.sub(r",\s*", ",", field[2]) == re.sub(
                        r",\s*", ",", constraint["text"]
                    ):
                        body = (
                            body[: field.start(2)]
                            + constraint["id"]
                            + body[field.end(2) :]
                        )
            return finding["heading"] + body

        result["exploitation_report"] = FINDING_PATTERN.sub(
            replace, result["exploitation_report"]
        )
        result[PROTOCOL_KEY] = PROTOCOL_VERSION
    return result, plan


def reviewed_state(state):
    if state.get("status") == "failed" or not state.get("analysis_results", {}).get(
        "reporting_sources"
    ):
        return state
    result, plan = reviewed_analysis(state["analysis_results"])
    state.update(
        analysis_results=result,
        filtered_articles=review_articles(plan, eligible_only=False),
        source_review_plan=plan.packet,
        articles_fingerprint=digest(
            {"generation_schema": 5, "plan_id": plan.packet["plan_id"]}
        ),
    )
    return state
