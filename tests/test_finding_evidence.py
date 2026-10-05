import pytest

from src.core.finding_evidence import (
    EvidenceError,
    assess_exploitation,
    validate_finding_evidence,
)
from src.core.reporting import build_reporting_catalog, reporting_key

CVE = "CVE-2026-1234"
URL = "https://example.test/advisory"


def article(content, **extra):
    return {
        "title": f"Example Server {CVE}",
        "source": "Vendor",
        "link": URL,
        "content": content,
        **extra,
    }


def report(status="active", prose="Active exploitation confirmed.", **fields):
    values = {
        "Affected Versions": "Example Server 2.3",
        "Exceptions": "Hosted users need no action.",
        "Recommended Actions": "Install the update.",
        "Vendor Links": "https://example.test/vendor",
    }
    values.update(fields)
    return (
        f"""# Exploitation Report

## Executive Summary

Example Server: {prose}

## Active Exploitation Details

### Example Server ({CVE})
- **Description**: A server vulnerability.
- **Status**: {prose}
- **Severity**: high
- **Exploitation Status**: {status}
- **Action**: patch
- **CVE IDs**: {CVE}
- **Reporting**: {reporting_key(URL)}
"""
        + "\n".join(f"- **{key}**: {value}" for key, value in values.items())
        + "\n\n## Affected Systems and Products\n\nSee findings.\n\n## Attack Vectors and Techniques\n\nNot stated in supplied sources.\n\n## Threat Actor Activities\n\nNot stated in supplied sources.\n"
    )


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        (f"{CVE} is actively exploited in the wild.", "active"),
        (f"{CVE} has an Exploitation More Likely assessment.", "potential"),
        (
            f"There is no evidence that {CVE} has been exploited in the wild. Exploitation More Likely.",
            "not_observed",
        ),
        (f"{CVE} allows privilege escalation.", "unknown"),
        (f"{CVE} exploitation status is unknown.", "unknown"),
        (f"{CVE} may be exploited in the wild.", "potential"),
        (f"{CVE} was not exploited in the wild.", "not_observed"),
    ],
)
def test_source_evidence_states(text, expected):
    assert assess_exploitation([article(text)], [CVE]).status == expected


def test_section_heading_and_unrelated_vulnerability_cannot_confirm_exploitation():
    source = article(
        f"{CVE} permits mailbox access.\n\nNo evidence of the flaw being weaponized in the wild.\n\nWarlock is exploiting SharePoint vulnerabilities in attacks."
    )
    result = assess_exploitation([source], [CVE])
    assert result.status == "not_observed"
    assert result.negative


def test_multi_cve_and_conflicting_sources_preserve_uncertainty():
    source = article(
        f"{CVE} is not exploited. CVE-2026-5678 is actively exploited in the wild."
    )
    assert assess_exploitation([source], [CVE]).status == "not_observed"
    assert assess_exploitation([source], ["CVE-2026-5678"]).status == "active"
    result = assess_exploitation(
        [
            source,
            article(
                f"{CVE} is actively exploited in attacks.",
                link="https://example.test/second",
            ),
        ],
        [CVE],
    )
    assert result.status == "unknown"
    assert result.conflicting


def test_negative_tail_is_preserved_and_blocks_badge_and_prose():
    source = article(
        "Context. " * 100
        + f"\n\nNo evidence that {CVE} has been exploited in the wild."
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="exploitation"):
        validate_finding_evidence(report(), catalog)
    with pytest.raises(EvidenceError, match="prose|claim"):
        validate_finding_evidence(report(status="not_observed"), catalog)


def test_missing_source_evidence_fails_closed():
    with pytest.raises(EvidenceError, match="retained"):
        validate_finding_evidence(report(), build_reporting_catalog([article("")]))


def test_supported_finding_details_and_links_are_retained():
    source = article(
        f"{CVE} is actively exploited in the wild.\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    validate_finding_evidence(report(), build_reporting_catalog([source]))
    for fields in [
        {"Affected Versions": "Example Server 99.0"},
        {"Exceptions": "Everyone is exempt."},
        {"Vendor Links": "https://fake.test/advisory"},
    ]:
        with pytest.raises(EvidenceError):
            validate_finding_evidence(
                report(**fields), build_reporting_catalog([source])
            )


def test_nonconfirmed_summary_cannot_inherit_another_findings_active_state():
    source = article(f"No evidence that {CVE} has been exploited in the wild.")
    text = report(
        "not_observed",
        "No exploitation observed.",
        **{
            key: "Not stated in supplied sources."
            for key in [
                "Affected Versions",
                "Exceptions",
                "Recommended Actions",
                "Vendor Links",
            ]
        },
    )
    text = text.replace("- **Action**: patch", "- **Action**: none")
    text = text.replace(
        "Example Server: No exploitation observed.",
        "Confirmed active exploitation affects Example Server.",
    )
    with pytest.raises(EvidenceError, match="summary|claim|prose"):
        validate_finding_evidence(text, build_reporting_catalog([source]))


def test_citing_only_positive_source_cannot_discard_known_negative_source():
    positive = article(f"{CVE} is actively exploited in the wild.")
    negative = article(
        f"No evidence that {CVE} has been exploited.",
        link="https://example.test/negative",
    )
    with pytest.raises(EvidenceError, match="exploitation|conflict"):
        validate_finding_evidence(
            report(), build_reporting_catalog([positive, negative])
        )


def test_known_versions_and_exceptions_cannot_be_reported_absent():
    source = article(
        f"{CVE} is actively exploited in the wild.\n\nAffected versions:\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    for field in ["Affected Versions", "Exceptions", "Recommended Actions"]:
        with pytest.raises(EvidenceError, match="omits"):
            validate_finding_evidence(
                report(**{field: "Not stated in supplied sources."}),
                build_reporting_catalog([source]),
            )


@pytest.mark.parametrize(
    "content",
    [
        f"# {CVE} active exploitation\n\nDetails are unknown.",
        f"{CVE} is not known to be actively exploited.",
        f"{CVE} exploitation has not been observed.",
    ],
)
def test_headings_and_additional_negations_never_confirm(content):
    assert assess_exploitation([article(content)], [CVE]).status != "active"


def test_version_list_cannot_be_partially_dropped():
    source = article(
        f"{CVE} is actively exploited in the wild.\n\nAffected versions:\n\nExample Server 2.3\n\nExample Server 2.4\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(report(), build_reporting_catalog([source]))


def test_one_cve_cannot_confirm_every_cve_in_a_combined_finding():
    source = article(
        f"{CVE} is actively exploited in the wild. CVE-2026-5678 is newly disclosed."
    )
    assert assess_exploitation([source], [CVE, "CVE-2026-5678"]).status == "unknown"


def test_unknown_language_does_not_fall_through_to_confirmation():
    source = article(f"It is unknown whether {CVE} is actively exploited.")
    assert assess_exploitation([source], [CVE]).status == "unknown"


def test_patch_badge_requires_a_supported_recommendation():
    source = article(f"{CVE} is actively exploited in the wild.")
    text = report(
        **{
            key: "Not stated in supplied sources."
            for key in [
                "Affected Versions",
                "Exceptions",
                "Recommended Actions",
                "Vendor Links",
            ]
        }
    )
    with pytest.raises(EvidenceError, match="action|patch"):
        validate_finding_evidence(text, build_reporting_catalog([source]))


def test_evidence_failure_preserves_existing_report_and_fingerprint(tmp_path):
    import asyncio
    from src.core.reporting import serialize_reporting_catalog
    from test_workflow_guards import import_workflow_with_stubs

    workflow = import_workflow_with_stubs()
    output = tmp_path / "index.md"
    output.write_text("Last validated report")
    fingerprint = tmp_path / ".sentryinsight-articles-fingerprint"
    fingerprint.write_text("previous")
    state = {
        "analysis_results": {
            "exploitation_report": report(),
            "reporting_sources": serialize_reporting_catalog(
                build_reporting_catalog(
                    [article(f"No evidence that {CVE} has been exploited.")]
                )
            ),
        },
        "config": {"output_path": str(output)},
        "status": "started",
        "articles_fingerprint": "next",
    }
    result = asyncio.run(workflow.generate_report(state))
    assert result["status"] == "failed"
    assert output.read_text() == "Last validated report"
    assert fingerprint.read_text() == "previous"
    assert not (tmp_path / "index.html").exists()


@pytest.mark.parametrize("word", ["observed", "detected", "confirmed"])
def test_passive_negative_statement_is_not_observed(word):
    assert (
        assess_exploitation(
            [article(f"{CVE} exploitation has not been {word}.")], [CVE]
        ).status
        == "not_observed"
    )


def test_confirmed_exploitation_with_possible_impact_stays_confirmed():
    assert (
        assess_exploitation(
            [
                article(
                    f"{CVE} is actively exploited and could allow remote code execution."
                )
            ],
            [CVE],
        ).status
        == "active"
    )


@pytest.mark.parametrize("variant", ["title", "formatted"])
def test_unsupported_claims_in_titles_and_rendered_prose_are_rejected(variant):
    source = article(
        f"No evidence that {CVE} has been exploited.\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    text = report("not_observed", "No evidence of exploitation.")
    if variant == "title":
        text = text.replace(
            "### Example Server", "### Active exploitation of Example Server"
        )
    else:
        text = text.replace(
            "No evidence of exploitation.",
            "No evidence of exploitation. Active **exploitation** confirmed.",
        )
    with pytest.raises(EvidenceError, match="claim|prose"):
        validate_finding_evidence(text, build_reporting_catalog([source]))


def test_unknown_which_clause_does_not_confirm_exploitation():
    source = article(f"It is unknown which attackers are exploiting {CVE}.")
    assert assess_exploitation([source], [CVE]).status == "unknown"


def test_uncertain_subject_cannot_confirm_a_following_ambiguous_clause():
    source = article(
        f"It is unknown whether {CVE} is actively exploited and attackers are exploiting it."
    )
    assert assess_exploitation([source], [CVE]).status == "unknown"


def test_conflicting_clauses_cannot_hide_confirmed_source_evidence():
    source = article(
        f"No evidence of exploitation of {CVE}, but {CVE} is actively exploited in attacks."
    )
    result = assess_exploitation([source], [CVE])
    assert result.status == "unknown"
    assert result.conflicting


@pytest.mark.parametrize(
    "claim",
    [
        "Active exploitation confirmed and could be exploited to gain privileges.",
        "No evidence of exploitation, but active exploitation confirmed.",
        "![Active exploitation confirmed](https://example.test/missing.png)",
        "![Active **exploitation** confirmed](https://example.test/missing.png)",
        "Active\nexploitation confirmed.",
    ],
)
def test_rendered_claims_cannot_hide_in_clauses_or_accessible_text(claim):
    source = article(
        f"No evidence that {CVE} has been exploited.\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    text = report("not_observed", "No evidence of exploitation.")
    text = text.replace("- **Severity**:", claim + "\n- **Severity**:")
    with pytest.raises(EvidenceError, match="claim|prose"):
        validate_finding_evidence(text, build_reporting_catalog([source]))


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        (
            f"{CVE} allows remote code execution and is actively exploited in attacks.",
            "active",
        ),
        (
            f"{CVE} allows remote code execution, and is actively exploited in attacks.",
            "active",
        ),
        (
            f"{CVE} could allow remote code execution but is actively exploited in attacks.",
            "active",
        ),
        (
            f"{CVE} allows remote code execution and is actively exploited and has now been patched.",
            "active",
        ),
        (
            f"{CVE} allows remote code execution and has not been exploited.",
            "not_observed",
        ),
        (f"{CVE} allows remote code execution and may be exploited.", "potential"),
        (
            f"It is unknown whether {CVE} allows remote code execution and is actively exploited.",
            "unknown",
        ),
        (
            f"It is unknown whether {CVE} allows remote code execution and {CVE} is actively exploited.",
            "unknown",
        ),
        (f"{CVE} might be actively exploited and weaponized in the wild.", "potential"),
        (
            f"{CVE} was not actively exploited and weaponized in the wild.",
            "not_observed",
        ),
        (
            f"{CVE} allows remote code execution and another flaw is actively exploited.",
            "unknown",
        ),
        (
            f"{CVE} allows remote code execution but attackers are exploiting another flaw.",
            "unknown",
        ),
        (
            f"{CVE} allows remote code execution; is actively exploited in attacks.",
            "unknown",
        ),
        (
            f"{CVE} allows remote code execution. It is actively exploited in attacks.",
            "unknown",
        ),
        (
            f"{CVE} allows remote code execution and another flaw is disclosed and is actively exploited.",
            "unknown",
        ),
    ],
)
def test_subject_and_stance_are_preserved_across_predicates(text, expected):
    assert assess_exploitation([article(text)], [CVE]).status == expected


def test_coordinated_negative_and_positive_evidence_remain_conflicting():
    result = assess_exploitation(
        [article(f"{CVE} is not exploited but is actively exploited in attacks.")],
        [CVE],
    )
    assert result.status == "unknown"
    assert result.conflicting


def test_coordinated_confirmation_can_publish_without_repeating_the_cve():
    source = article(
        f"{CVE} allows remote code execution and is actively exploited in attacks.\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    validate_finding_evidence(report(), build_reporting_catalog([source]))


@pytest.mark.parametrize("location", ["summary", "finding"])
def test_summary_checks_the_same_rendered_statements_as_findings(location):
    source = article(
        f"No evidence that {CVE} has been exploited.\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    text = report("not_observed", "No evidence of exploitation.")
    if location == "summary":
        text = text.replace(
            "Example Server: No evidence of exploitation.",
            "The vulnerability is actively\nexploited in attacks.",
        )
    else:
        text = text.replace(
            "- **Severity**:",
            "\n```\nActive exploitation confirmed.\n```\n- **Severity**:",
        )
    with pytest.raises(EvidenceError, match="summary|claim|prose"):
        validate_finding_evidence(text, build_reporting_catalog([source]))


@pytest.mark.parametrize(
    ("claim", "expected"),
    [
        (
            f"It is unknown whether {CVE} was exploited, but is now actively exploited in attacks.",
            "active",
        ),
        (f"{CVE} could be actively exploited, but weaponized in the wild.", "active"),
        (f"{CVE} was not actively exploited, but weaponized in the wild.", "unknown"),
    ],
)
def test_adversative_predicates_start_a_new_evidence_assertion(claim, expected):
    result = assess_exploitation([article(claim)], [CVE])
    assert result.status == expected
    if expected == "unknown":
        assert result.conflicting


@pytest.mark.parametrize(
    "claim",
    [
        f"It is unknown whether {CVE} was exploited, but is now actively exploited in attacks.",
        f"{CVE} could be actively exploited, but weaponized in the wild.",
        f"{CVE} was not actively exploited, but weaponized in the wild.",
    ],
)
def test_adversative_assertions_cannot_hide_unsupported_report_claims(claim):
    source = article(
        f"No evidence that {CVE} has been exploited.\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    text = report("not_observed", "No evidence of exploitation.")
    text = text.replace("- **Severity**:", claim + "\n- **Severity**:")
    with pytest.raises(EvidenceError, match="claim|prose"):
        validate_finding_evidence(text, build_reporting_catalog([source]))


@pytest.mark.parametrize("opener", ["not only", "not just", "not merely"])
@pytest.mark.parametrize(
    "scope,expected",
    [
        ("It is unknown whether", "unknown"),
        ("It is possible that", "potential"),
        ("", "active"),
    ],
)
def test_correlative_predicates_keep_their_shared_scope(opener, scope, expected):
    source = article(
        f"{scope} {CVE} is {opener} actively exploited but also weaponized in the wild."
    )
    assert assess_exploitation([source], [CVE]).status == expected


def test_correlative_modal_scope_applies_to_repeated_finite_predicate():
    source = article(
        f"{CVE} might not only be actively exploited but also is weaponized in the wild."
    )
    assert assess_exploitation([source], [CVE]).status == "potential"


def test_correlative_pair_does_not_capture_a_later_adversative():
    source = article(
        f"It is unknown whether {CVE} is not only exploitable but also affected, but is now actively exploited in attacks."
    )
    assert assess_exploitation([source], [CVE]).status == "active"


def test_uncertain_correlative_evidence_cannot_publish_as_active():
    source = article(
        f"It is unknown whether {CVE} is not only actively exploited but also weaponized in the wild.\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="unsupported exploitation status"):
        validate_finding_evidence(report(), build_reporting_catalog([source]))
    validate_finding_evidence(
        report(
            "unknown",
            f"It is unknown whether {CVE} is not only actively exploited but also weaponized in the wild.",
        ),
        build_reporting_catalog([source]),
    )


def test_uncertainty_inside_one_correlative_part_does_not_qualify_both():
    claim = f"{CVE} is not only potentially exploited but also is actively exploited in attacks."
    assert assess_exploitation([article(claim)], [CVE]).status == "active"
    source = article(
        f"No evidence that {CVE} has been exploited.\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    text = report("not_observed", "No evidence of exploitation.")
    text = text.replace("- **Severity**:", claim + "\n- **Severity**:")
    with pytest.raises(EvidenceError, match="claim|prose"):
        validate_finding_evidence(text, build_reporting_catalog([source]))


@pytest.mark.parametrize(
    "qualifier", ["potentially", "likely", "possibly", "probably", "unlikely"]
)
def test_local_uncertainty_adverbs_preserve_subject_and_publish_as_potential(qualifier):
    claim = f"{CVE} is not only affected but also {qualifier} exploited in attacks."
    source = article(
        claim
        + "\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    assert assess_exploitation([source], [CVE]).status == "potential"
    validate_finding_evidence(
        report("potential", claim), build_reporting_catalog([source])
    )


@pytest.mark.parametrize("modifier", ["newly", "recently"])
def test_temporal_adverbs_do_not_discard_confirmed_subject(modifier):
    source = article(
        f"{CVE} is affected and {modifier} is actively exploited in attacks."
    )
    assert assess_exploitation([source], [CVE]).status == "active"


def test_a_noun_ending_in_ly_is_not_a_predicate_modifier():
    source = article(f"{CVE} is affected and family is actively exploited in attacks.")
    assert assess_exploitation([source], [CVE]).status == "unknown"


@pytest.mark.parametrize(
    "subject",
    [
        "newly affected issue",
        "recently exploited flaw",
        "affected systems",
        "also vulnerable servers",
        "potentially exploitable bugs",
        "newly weaponized exploits",
    ],
)
def test_participial_noun_subject_ends_coordinated_cve_attribution(subject):
    source = article(
        f"{CVE} is affected and {subject} is actively exploited in attacks."
    )
    assert assess_exploitation([source], [CVE]).status == "unknown"
    with pytest.raises(EvidenceError, match="unsupported exploitation status"):
        validate_finding_evidence(report(), build_reporting_catalog([source]))


@pytest.mark.parametrize(
    "predicate",
    [
        "recently exploited in attacks",
        "actively exploited by attackers",
        "weaponized in the wild",
        "affected",
        "vulnerable to attack",
    ],
)
def test_predicate_complements_retain_subject_for_a_later_assertion(predicate):
    source = article(
        f"{CVE} is affected and {predicate} and is actively exploited in attacks."
    )
    assert assess_exploitation([source], [CVE]).status == "active"


@pytest.mark.parametrize(
    "adjunct", ["worldwide", "after public disclosure", "before a patch", "extensively"]
)
def test_coordinated_exploitation_with_adjuncts_can_publish(adjunct):
    source = article(
        f"{CVE} is affected and actively exploited {adjunct}.\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    assert assess_exploitation([source], [CVE]).status == "active"
    validate_finding_evidence(report(), build_reporting_catalog([source]))


@pytest.mark.parametrize(
    "adjunct",
    [
        "after it was publicly disclosed",
        "worldwide after patches were released",
        "because a patch was unavailable",
        "before the vendor had issued an update",
    ],
)
def test_finite_dependent_adjunct_preserves_the_exploitation_subject(adjunct):
    source = article(
        f"{CVE} is affected and actively exploited {adjunct}.\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    assert assess_exploitation([source], [CVE]).status == "active"
    validate_finding_evidence(report(), build_reporting_catalog([source]))


@pytest.mark.parametrize(
    "subject", ["exploited systems", "newly affected systems", "vulnerable servers"]
)
@pytest.mark.parametrize("verb", ["saw", "reported", "experienced"])
def test_lexical_assertion_after_a_new_subject_cannot_inherit_the_cve(subject, verb):
    source = article(
        f"{CVE} is affected and {subject} {verb} attackers exploiting the weakness."
    )
    assert assess_exploitation([source], [CVE]).status == "unknown"
    with pytest.raises(EvidenceError, match="unsupported exploitation status"):
        validate_finding_evidence(report(), build_reporting_catalog([source]))
