"""Unknown source-level qualification ownership must remain fail-closed."""

import pytest

from src.core.finding_evidence import EvidenceError, validate_finding_evidence
from src.core.reporting import build_reporting_catalog
from src.core.version_references import (
    build_version_reference_context,
    resolve_version_references,
)
from test_version_references import report, source, with_version_state

TARGET = "An attack vector targets instances running version 3.2 or earlier."
RANGE = "instances running version 3.2 or earlier"


@pytest.mark.parametrize(
    "content",
    [
        TARGET + "\n\nOnly Windows installations are impacted.",
        "Only Windows installations are impacted.\n\n" + TARGET,
        TARGET + "\n\nThis applies only when remote administration is enabled.",
        "This applies only when remote administration is enabled.\n\n" + TARGET,
        TARGET + "\n\n- Only Windows installations are impacted.",
        "## Windows installations only\n\n" + TARGET,
        "## Deployment conditions\n\nOnly Windows installations are impacted.\n\n"
        "## Attack vector\n\n" + TARGET,
        TARGET + "\n\nOnly the database product is impacted.",
        "The following statement is incorrect.\n\n" + TARGET,
        TARGET + "\n\nThe preceding statement is incorrect.",
    ],
)
def test_unknown_source_qualification_ownership_cannot_publish_an_unrestricted_range(
    content,
):
    catalog = build_reporting_catalog([source(content)])
    [scope] = build_version_reference_context(catalog)
    assert scope["state"] == "blocked"
    assert not scope["absence_allowed"]
    assert not scope["unresolved_allowed"]
    with pytest.raises(EvidenceError):
        resolve_version_references(
            report(catalog, cves="None", status="unknown"), catalog
        )
    # A forged canonical field cannot bypass the source-scope check either.
    forged = with_version_state(
        report(catalog, RANGE, cves="None", status="unknown"), "supported"
    )
    with pytest.raises(EvidenceError):
        validate_finding_evidence(forged, catalog)
