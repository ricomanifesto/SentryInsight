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


@pytest.mark.parametrize(
    "adjunct",
    [
        "last week",
        "today",
        "over the weekend",
        "more than 100 times",
        "yesterday",
        "earlier this month",
        "the previous year",
        "three days ago",
        "at least two times",
        "100 times last week",
        "last Friday",
        "again",
        "Monday",
        "Monday morning",
        "overnight",
        "hundreds of times",
        "last Friday night",
        "this Monday morning",
        "next Tuesday afternoon",
    ],
)
def test_nominal_time_and_frequency_adjuncts_can_publish(adjunct):
    source = article(
        f"{CVE} is affected and actively exploited {adjunct}.\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    assert assess_exploitation([source], [CVE]).status == "active"
    validate_finding_evidence(report(), build_reporting_catalog([source]))


@pytest.mark.parametrize(
    "subject", ["100 systems", "more than 100 systems", "last week's systems"]
)
def test_quantified_or_temporal_noun_subjects_are_not_predicate_adjuncts(subject):
    source = article(
        f"{CVE} is affected and exploited {subject} saw attackers exploiting the weakness."
    )
    assert assess_exploitation([source], [CVE]).status == "unknown"


@pytest.mark.parametrize(
    "cue", ["Affected versions are ", "Affected versions: ", "Versions affected: "]
)
@pytest.mark.parametrize("separator", [" and ", ", "])
def test_inline_version_lists_require_every_source_entry(cue, separator):
    source = article(
        f"{CVE} is actively exploited.\n\n{cue}Example Server 2.3{separator}Example Server 2.4.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(report(), catalog)
    validate_finding_evidence(
        report(**{"Affected Versions": "Example Server 2.3; Example Server 2.4"}),
        catalog,
    )


@pytest.mark.parametrize(
    "link",
    [
        "https://example.test/vendor#mitigation",
        "https://EXAMPLE.test:443/vendor#patch",
        "https://example.test/old/../vendor",
    ],
)
def test_copied_vendor_links_share_the_catalog_url_identity(link):
    source = article(
        f"{CVE} is actively exploited.\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall the update.",
        source_links=[link],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(report(**{"Vendor Links": link}), catalog)
    for invalid in [
        "javascript:alert(1)",
        "https://user:secret@example.test/vendor",
        "https://different.test/vendor",
    ]:
        with pytest.raises(EvidenceError, match="unsupported vendor link"):
            validate_finding_evidence(report(**{"Vendor Links": invalid}), catalog)


@pytest.mark.parametrize(
    "qualifier",
    [
        "and earlier",
        "or later",
        "and older",
        "or newer",
        "or higher",
        "and any earlier versions",
        "or all subsequent releases",
        "and up",
        "or greater",
        "and onwards",
        "or less",
    ],
)
def test_inline_version_range_cannot_be_narrowed(qualifier):
    constraint = f"Example Server 2.3 {qualifier}"
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are {constraint}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(report(), catalog)
    validate_finding_evidence(report(**{"Affected Versions": constraint}), catalog)


@pytest.mark.parametrize(
    "version_list",
    [
        "Affected versions are Example Server 1.0 and Example Server 1.0.1.",
        "Affected versions:\nExample Server 1.0\nExample Server 1.0.1",
    ],
)
def test_version_prefix_does_not_satisfy_a_distinct_source_entry(version_list):
    source = article(
        f"{CVE} is actively exploited.\n\n{version_list}\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(
            report(**{"Affected Versions": "Example Server 1.0.1"}), catalog
        )
    validate_finding_evidence(
        report(**{"Affected Versions": "Example Server 1.0; Example Server 1.0.1"}),
        catalog,
    )


@pytest.mark.parametrize(
    "continuation",
    [
        "customers should install the update",
        "admins must patch immediately",
        "further details are available from the vendor",
        "customers should install update 2.4",
    ],
)
def test_unrelated_clause_ends_an_inline_version_list(continuation):
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are Example Server 2.3, and {continuation}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    validate_finding_evidence(
        report(
            **{
                "Recommended Actions": (
                    f"Affected versions are Example Server 2.3, and {continuation}.; Install the update."
                    if continuation.startswith(("customers", "admins"))
                    else "Install the update."
                )
            }
        ),
        build_reporting_catalog([source]),
    )


@pytest.mark.parametrize("cue", ["Affected versions: ", ""])
@pytest.mark.parametrize("version", ["1.0.1", "1.0~rc1", "1.0:1", "1.0!1"])
def test_version_prefix_cannot_add_an_unsupported_version(cue, version):
    source = article(
        f"{CVE} is actively exploited.\n\n{cue}Example Server {version}\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(
        report(**{"Affected Versions": f"Example Server {version}"}), catalog
    )
    with pytest.raises(EvidenceError, match="source-supported|unsupported"):
        validate_finding_evidence(
            report(
                **{"Affected Versions": f"Example Server {version}; Example Server 1.0"}
            ),
            catalog,
        )


@pytest.mark.parametrize(
    "tail",
    [
        "and successor releases",
        "or successive generations",
        "and versions that are earlier",
        "or those that are newer",
    ],
)
def test_ambiguous_version_tail_cannot_be_silently_discarded(tail):
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are Example Server 2.3 {tail}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="ambiguous"):
        validate_finding_evidence(report(), build_reporting_catalog([source]))


@pytest.mark.parametrize(
    "clause",
    [
        "users of Example Server 2.4 are also affected",
        "customers of Example Server 2.4 are still vulnerable",
    ],
)
def test_affected_user_clause_contributes_its_version(clause):
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are Example Server 2.3, and {clause}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(report(), catalog)
    validate_finding_evidence(
        report(**{"Affected Versions": "Example Server 2.3; Example Server 2.4"}),
        catalog,
    )


@pytest.mark.parametrize("conjunction", ["and", "or"])
def test_product_name_conjunction_is_not_a_version_separator(conjunction):
    version = f"Research {conjunction} Development Server 2.3"
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are {version}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(report(**{"Affected Versions": version}), catalog)
    with pytest.raises(EvidenceError):
        validate_finding_evidence(
            report(**{"Affected Versions": "Development Server 2.3"}), catalog
        )


def test_conjunction_product_name_can_follow_another_version_entry():
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are Example Server 2.3 and Research and Development Server 2.4.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": "Example Server 2.3; Research and Development Server 2.4"
            }
        ),
        build_reporting_catalog([source]),
    )


@pytest.mark.parametrize(
    "predicate",
    [
        "are not affected",
        "are unaffected",
        "remain unaffected",
        "are no longer vulnerable",
        "were not impacted",
    ],
)
@pytest.mark.parametrize(
    "versions", ["Example Server 2.4", "Example Server 2.4 and Example Server 2.5"]
)
def test_unaffected_user_clauses_do_not_add_affected_versions(predicate, versions):
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are Example Server 2.3, and users of {versions} {predicate}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(
        report(
            **{"Exceptions": f"users of {versions} {predicate}"},
        ),
        catalog,
    )
    with pytest.raises(EvidenceError, match="unsupported"):
        validate_finding_evidence(
            report(
                **{"Exceptions": f"users of {versions} {predicate}"},
                **{"Affected Versions": "Example Server 2.3; Example Server 2.4"},
            ),
            catalog,
        )


def test_excluded_clause_does_not_hide_a_later_affected_clause():
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are Example Server 2.3 and users of Example Server 2.4 are not affected, but users of Example Server 2.5 are affected.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(
            report(
                **{"Exceptions": "users of Example Server 2.4 are not affected"},
            ),
            catalog,
        )
    validate_finding_evidence(
        report(
            **{"Exceptions": "users of Example Server 2.4 are not affected"},
            **{"Affected Versions": "Example Server 2.3; Example Server 2.5"},
        ),
        catalog,
    )


@pytest.mark.parametrize(
    "predicate",
    ["are advised to", "are recommended to", "are urged to", "are encouraged to"],
)
def test_recommendation_predicates_do_not_become_version_entries(predicate):
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are Example Server 2.3, and customers {predicate} install the update.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    validate_finding_evidence(
        report(
            **{
                "Recommended Actions": f"Affected versions are Example Server 2.3, and customers {predicate} install the update.; Install the update."
            }
        ),
        build_reporting_catalog([source]),
    )


def test_known_version_list_with_only_excluded_versions_stays_empty():
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions: users of Example Server 2.4 are not affected.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(
        report(
            **{"Exceptions": "users of Example Server 2.4 are not affected"},
            **{"Affected Versions": "Not stated in supplied sources."},
        ),
        catalog,
    )
    with pytest.raises(EvidenceError, match="unsupported"):
        validate_finding_evidence(
            report(
                **{"Exceptions": "users of Example Server 2.4 are not affected"},
                **{"Affected Versions": "Example Server 2.4"},
            ),
            catalog,
        )


@pytest.mark.parametrize("constraint", ["all supported releases", ""])
def test_unresolved_version_list_is_not_an_explicit_empty_list(constraint):
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions: {constraint}\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="omits|ambiguous"):
        validate_finding_evidence(
            report(**{"Affected Versions": "Not stated in supplied sources."}),
            build_reporting_catalog([source]),
        )


@pytest.mark.parametrize(
    "clause",
    [
        "users of Example Server 2.4 are not affected",
        "customers are recommended to install the update",
        "further details are available from the vendor",
    ],
)
def test_reported_version_field_rejects_nonaffected_source_clauses(clause):
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are Example Server 2.3, and {clause}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(
        report(
            **{
                "Recommended Actions": (
                    f"Affected versions are Example Server 2.3, and {clause}.; Install the update."
                    if "recommended" in clause
                    else "Install the update."
                ),
                "Exceptions": (
                    clause
                    if "not affected" in clause
                    else "Hosted users need no action."
                ),
            },
        ),
        catalog,
    )
    with pytest.raises(EvidenceError, match="non-affected"):
        validate_finding_evidence(
            report(
                **{
                    "Recommended Actions": (
                        f"Affected versions are Example Server 2.3, and {clause}.; Install the update."
                        if "recommended" in clause
                        else "Install the update."
                    ),
                    "Exceptions": (
                        clause
                        if "not affected" in clause
                        else "Hosted users need no action."
                    ),
                },
                **{"Affected Versions": f"Example Server 2.3; {clause}"},
            ),
            catalog,
        )


@pytest.mark.parametrize("separator", [" — ", " – ", " - ", "—", "–"])
def test_dash_delimited_version_clause_retains_its_role(separator):
    text = f"Example Server 2.3{separator}users of Example Server 2.4 are not affected"
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are {text}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(
        report(
            **{"Exceptions": "users of Example Server 2.4 are not affected"},
        ),
        catalog,
    )
    with pytest.raises(EvidenceError, match="non-affected"):
        validate_finding_evidence(
            report(
                **{"Exceptions": "users of Example Server 2.4 are not affected"},
                **{"Affected Versions": text},
            ),
            catalog,
        )


@pytest.mark.parametrize(
    "qualifier", ["users with premium licenses", "administrators only"]
)
@pytest.mark.parametrize(
    "separator", [" — ", " – ", " - ", ", ", "; ", " and ", " or "]
)
def test_dash_audience_qualifier_remains_part_of_the_version_constraint(
    qualifier, separator
):
    text = f"Example Server 2.3{separator}{qualifier}"
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are {text}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(report(**{"Affected Versions": text}), catalog)
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(report(), catalog)


@pytest.mark.parametrize("separator", [", ", "; ", " and ", " or "])
@pytest.mark.parametrize("predicate", ["are not affected", "remain unaffected"])
def test_qualified_audience_exception_is_not_an_affected_version(separator, predicate):
    text = f"Example Server 2.3{separator}users with premium licenses {predicate}"
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are {text}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(
        report(
            **{"Exceptions": f"users with premium licenses {predicate}"},
        ),
        catalog,
    )
    with pytest.raises(EvidenceError, match="non-affected"):
        validate_finding_evidence(
            report(
                **{"Exceptions": f"users with premium licenses {predicate}"},
                **{"Affected Versions": text},
            ),
            catalog,
        )


@pytest.mark.parametrize("separator", [", ", "; ", " and ", " or "])
def test_positive_audience_assertion_preserves_the_qualified_constraint(separator):
    text = f"Example Server 2.3{separator}users with premium licenses are affected"
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are {text}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(report(**{"Affected Versions": text}), catalog)
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(report(), catalog)


@pytest.mark.parametrize("separator", [", ", " — ", " / "])
@pytest.mark.parametrize(
    "predicate",
    ["are never affected", "are not currently affected", "may not be affected"],
)
def test_unrecognized_audience_predicates_cannot_fall_through_as_version_text(
    separator, predicate
):
    text = f"Example Server 2.3{separator}users with premium licenses {predicate}"
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are {text}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="ambiguous"):
        validate_finding_evidence(
            report(**{"Affected Versions": text}), build_reporting_catalog([source])
        )


@pytest.mark.parametrize("separator", [" / ", " | ", " (", " : "])
@pytest.mark.parametrize(
    "clause",
    [
        "users of Example Server 2.4 are not affected",
        "customers are recommended to install the update",
        "further details are available from the vendor",
    ],
)
def test_unsplit_embedded_clauses_cannot_fall_through_as_numeric_entries(
    separator, clause
):
    text = f"Example Server 2.3{separator}{clause}"
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are {text}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="ambiguous|non-affected"):
        validate_finding_evidence(
            report(**{"Affected Versions": text}), build_reporting_catalog([source])
        )


@pytest.mark.parametrize("separator", [", ", "; ", " and ", " / "])
@pytest.mark.parametrize("predicate", ["need", "needs"])
def test_lexical_audience_action_predicates_cannot_be_version_qualifiers(
    separator, predicate
):
    text = f"Example Server 2.3{separator}users with premium licenses {predicate} no action"
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are {text}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="ambiguous"):
        validate_finding_evidence(
            report(**{"Affected Versions": text}), build_reporting_catalog([source])
        )


@pytest.mark.parametrize(
    "exceptions",
    [
        "Not stated in supplied sources.",
        "Legacy clients are exempt.",
        "users with premium licenses are no longer affected",
    ],
)
def test_every_parsed_exclusion_is_required_in_exceptions(exceptions):
    first = "users with premium licenses are no longer affected"
    second = "users with trial licenses are no longer vulnerable"
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are Example Server 2.3, and {first}, and {second}.\n\nLegacy clients are exempt.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="Exceptions omits"):
        validate_finding_evidence(report(**{"Exceptions": exceptions}), catalog)
    validate_finding_evidence(report(**{"Exceptions": f"{first}; {second}"}), catalog)


def sectioned_advisory():
    return article(
        f"# Vendor advisory\n\n## {CVE}\n\n{CVE} is actively exploited.\n\n### Affected versions\n\nExample Server 2.3\n\n### Exceptions\n\nHosted users need no action.\n\n### Recommended actions\n\nInstall the update.\n\n## CVE-2026-5678\n\nCVE-2026-5678 is not exploited.\n\n### Affected versions\n\nOther Server 9.9\n\n### Recommended actions\n\nInstall the other patch.\n\n## General information\n\nShared Server 8.8 is available.",
        source_links=["https://example.test/vendor"],
    )


@pytest.mark.parametrize(
    "field", ["Affected Versions", "Exceptions", "Recommended Actions"]
)
def test_cve_section_details_are_retained_and_cannot_be_omitted(field):
    catalog = build_reporting_catalog([sectioned_advisory()])
    validate_finding_evidence(report(), catalog)
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(
            report(**{field: "Not stated in supplied sources."}), catalog
        )


@pytest.mark.parametrize("version", ["Other Server 9.9", "Shared Server 8.8"])
def test_detail_scope_does_not_borrow_from_sibling_cve_or_parent_sections(version):
    catalog = build_reporting_catalog([sectioned_advisory()])
    with pytest.raises(EvidenceError, match="unsupported"):
        validate_finding_evidence(
            report(**{"Affected Versions": f"Example Server 2.3; {version}"}), catalog
        )


@pytest.mark.parametrize("position", ["before", "after"])
def test_explicit_cve_sections_exclude_unowned_single_cve_details(position):
    source = sectioned_advisory()
    owned = source["content"].split("## CVE-2026-5678")[0]
    general = "## General information\n\nAffected versions are Shared Server 8.8.\n\n"
    source["content"] = general + owned if position == "before" else owned + general
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(report(), catalog)
    with pytest.raises(EvidenceError, match="unsupported"):
        validate_finding_evidence(
            report(**{"Affected Versions": "Example Server 2.3; Shared Server 8.8"}),
            catalog,
        )


def test_multi_cve_finding_requires_details_from_each_owned_section():
    source = sectioned_advisory()
    source["content"] = source["content"].replace(
        "CVE-2026-5678 is not exploited.", "CVE-2026-5678 is actively exploited."
    )
    catalog = build_reporting_catalog([source])
    combined = report(
        **{
            "Affected Versions": "Example Server 2.3; Other Server 9.9",
            "Recommended Actions": "Install the update.; Install the other patch.",
        }
    ).replace(f"- **CVE IDs**: {CVE}", f"- **CVE IDs**: {CVE}, CVE-2026-5678")
    validate_finding_evidence(combined, catalog)
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(combined.replace("; Other Server 9.9", ""), catalog)


@pytest.mark.parametrize("field", ["Exceptions", "Recommended Actions"])
@pytest.mark.parametrize("has_cve", [True, False])
def test_structural_heading_labels_cannot_ground_detail_values(field, has_cve):
    source = sectioned_advisory()
    generated = report(**{field: field})
    if not has_cve:
        source["content"] = (
            "Affected versions are Example Server 2.3.\n### Exceptions\nHosted users need no action.\n### Recommended Actions\nInstall the update."
        )
        generated = report(
            status="unknown", prose="No subject identity supplied.", **{field: field}
        ).replace(CVE, "Not assigned")
    with pytest.raises(EvidenceError, match="source-supported"):
        validate_finding_evidence(generated, build_reporting_catalog([source]))


@pytest.mark.parametrize("suffix", ["0", ".1", "-rc1"])
def test_exclusion_prefix_cannot_satisfy_another_complete_exclusion(suffix):
    first = "Example Server 2"
    second = first + suffix
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions are Example Server 2.3; users of {first} and {second} are not affected.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="Exceptions omits"):
        validate_finding_evidence(report(**{"Exceptions": second}), catalog)
    validate_finding_evidence(report(**{"Exceptions": f"{first}; {second}"}), catalog)


def test_numeric_non_version_heading_ends_affected_version_list():
    source = article(
        f"## {CVE}\n{CVE} is actively exploited.\n### Affected versions\nExample Server 2.3\n### 2. Exceptions\nHosted users need no action.\n### 3. Recommended actions\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    validate_finding_evidence(report(), build_reporting_catalog([source]))


@pytest.mark.parametrize(
    "field,detail",
    [
        (
            "Affected Versions",
            "Affected versions are Example Server 2.3 and Example Server 2.4.",
        ),
        ("Exceptions", "Hosted users need no action."),
        ("Recommended Actions", "Install the update."),
    ],
)
def test_uncited_relevant_article_cannot_hide_required_details(field, detail):
    cited = article(
        f"{CVE} is actively exploited.\nExample Server 2.3",
        source_links=["https://example.test/vendor"],
    )
    uncited = article(f"## {CVE}\n{detail}", link="https://example.test/second")
    catalog = build_reporting_catalog([cited, uncited])
    generated = report(
        **{
            "Exceptions": "Not stated in supplied sources.",
            "Recommended Actions": "Not stated in supplied sources.",
        }
    ).replace("- **Action**: patch", "- **Action**: monitor")
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(generated, catalog)
    correct = (
        "Example Server 2.3; Example Server 2.4"
        if field == "Affected Versions"
        else detail
    )
    generated = generated.replace(
        f"- **{field}**: "
        + (
            "Example Server 2.3"
            if field == "Affected Versions"
            else "Not stated in supplied sources."
        ),
        f"- **{field}**: {correct}",
    )
    validate_finding_evidence(generated, catalog)


@pytest.mark.parametrize(
    "qualifier",
    ["and earlier", "or later", "and up", "or all subsequent releases", "through 2.4"],
)
def test_multiline_version_ranges_preserve_qualifiers(qualifier):
    source = article(
        f"{CVE} is actively exploited.\nAffected versions:\nExample Server 2.3\n{qualifier}\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(report(), catalog)
    validate_finding_evidence(
        report(**{"Affected Versions": f"Example Server 2.3 {qualifier}"}), catalog
    )


@pytest.mark.parametrize("layout", ["sentences", "headings", "combined"])
def test_exception_and_action_roles_cannot_be_swapped(layout):
    details = {
        "sentences": "Hosted users need no action.\n\nInstall the update.",
        "headings": "### Exceptions\nHosted service is exempt.\n### Recommended Actions\nRestart the service.",
        "combined": "Hosted users need no action, but administrators should install the update.",
    }[layout]
    exception = (
        "Hosted service is exempt."
        if layout == "headings"
        else "Hosted users need no action"
    )
    action = (
        "Restart the service."
        if layout == "headings"
        else details if layout == "combined" else "install the update"
    )
    source = article(
        f"## {CVE}\n{CVE} is actively exploited.\nExample Server 2.3\n\n{details}",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="source-supported|semantic role"):
        validate_finding_evidence(
            report(**{"Exceptions": action, "Recommended Actions": exception}), catalog
        )
    validate_finding_evidence(
        report(**{"Exceptions": exception, "Recommended Actions": action}), catalog
    )


@pytest.mark.parametrize(
    "source_version,reported",
    [
        ("2.1.0", "1.0"),
        ("1:2.3", "2.3"),
        ("1!2.3", "2.3"),
        ("2.3-rc1", "rc1"),
        ("2.3+build1", "build1"),
    ],
)
def test_version_suffix_cannot_be_grounded_inside_a_larger_token(
    source_version, reported
):
    source = article(
        f"{CVE} is actively exploited.\nRelease {source_version} is vulnerable.\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="source-supported"):
        validate_finding_evidence(report(**{"Affected Versions": reported}), catalog)
    validate_finding_evidence(report(**{"Affected Versions": source_version}), catalog)


@pytest.mark.parametrize(
    "field,value", [("Exceptions", "install"), ("Recommended Actions", "no action")]
)
def test_ambiguous_mixed_role_span_needs_a_role_bearing_value(field, value):
    source = article(
        f"{CVE} is actively exploited.\nExample Server 2.3\nHosted users need no action, but administrators should install the update.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="semantic role"):
        validate_finding_evidence(
            report(
                **{
                    "Exceptions": "Hosted users need no action",
                    "Recommended Actions": "install the update",
                    field: value,
                }
            ),
            build_reporting_catalog([source]),
        )


@pytest.mark.parametrize(
    "prohibition,fragment",
    [
        ("Do not install the update on hosted systems.", "install the update"),
        ("Customers should not apply the patch on hosted systems.", "apply the patch"),
        ("Never restart the service during recovery.", "restart the service"),
        (
            "Avoid the unstable release and do not install the update.",
            "install the update",
        ),
        (
            "There is no need to install the update on hosted systems.",
            "install the update",
        ),
        (
            "The vendor does not recommend that you install the update.",
            "install the update",
        ),
        ("Don't install the update on hosted systems.", "install the update"),
    ],
)
def test_recommendation_cannot_discard_source_prohibition(prohibition, fragment):
    source = article(
        f"## {CVE}\n{CVE} is actively exploited.\nExample Server 2.3\nHosted users need no action.\n### Recommended Actions\n{prohibition}",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="source-supported|prohibition"):
        validate_finding_evidence(report(**{"Recommended Actions": fragment}), catalog)
    validate_finding_evidence(report(**{"Recommended Actions": prohibition}), catalog)


def test_positive_source_cannot_hide_another_sources_action_prohibition():
    positive = article(
        f"{CVE} is actively exploited.\nExample Server 2.3\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    negative = article(
        f"## {CVE}\nDo not install the update on hosted systems.",
        link="https://example.test/second",
    )
    catalog = build_reporting_catalog([positive, negative])
    with pytest.raises(EvidenceError, match="prohibition"):
        validate_finding_evidence(report(), catalog)
    validate_finding_evidence(
        report(
            **{
                "Recommended Actions": "Install the update.; Do not install the update on hosted systems."
            }
        ),
        catalog,
    )


@pytest.mark.parametrize(
    "statement",
    [
        "Customers cannot install the update on hosted systems.",
        "Customers are unable to install the update on hosted systems.",
        "Customers are forbidden to install the update on hosted systems.",
        "Only install the update after backing up the database.",
    ],
)
def test_recommendations_preserve_complete_source_statements(statement):
    source = article(
        f"## {CVE}\n{CVE} is actively exploited.\nExample Server 2.3\nHosted users need no action.\n### Recommended Actions\n{statement}",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="source-supported|complete|omits"):
        validate_finding_evidence(
            report(**{"Recommended Actions": "install the update"}), catalog
        )
    validate_finding_evidence(report(**{"Recommended Actions": statement}), catalog)


def test_source_statement_semicolons_remain_inside_the_recommendation():
    statement = "Do not install the update; wait for the fixed release."
    source = article(
        f"## {CVE}\n{CVE} is actively exploited.\nExample Server 2.3\nHosted users need no action.\n### Recommended Actions\n{statement}\n\nRestart the service.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    complete = f"{statement}; Restart the service."
    validate_finding_evidence(report(**{"Recommended Actions": complete}), catalog)
    for incomplete in [
        "Do not install the update; Restart the service.",
        "wait for the fixed release; Restart the service.",
        statement,
    ]:
        with pytest.raises(EvidenceError, match="source-supported|complete|omits"):
            validate_finding_evidence(
                report(**{"Recommended Actions": incomplete}), catalog
            )


def test_overlapping_recommendation_statements_do_not_require_duplicate_clauses():
    statement = "Do not install the update; wait for the fixed release."
    source = article(
        f"## {CVE}\n{CVE} is actively exploited.\nExample Server 2.3\nHosted users need no action.\n### Recommended Actions\n{statement}",
        source_links=["https://example.test/vendor"],
    )
    shorter = article(
        f"## {CVE}\nDo not install the update.", link="https://example.test/second"
    )
    catalog = build_reporting_catalog([source, shorter])
    validate_finding_evidence(report(**{"Recommended Actions": statement}), catalog)
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(
            report(**{"Recommended Actions": "Do not install the update."}), catalog
        )


@pytest.mark.parametrize("prefix", ["U.S.", "Acme Inc.", "Authorized operators, e.g."])
def test_recommendation_audience_abbreviations_keep_the_original_source_block(prefix):
    statement = f"{prefix} customers should install the update."
    source = article(
        f"## {CVE}\n{CVE} is actively exploited.\nExample Server 2.3\nHosted users need no action.\n\n{statement}",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="source-supported|complete"):
        validate_finding_evidence(
            report(**{"Recommended Actions": "customers should install the update."}),
            catalog,
        )
    validate_finding_evidence(report(**{"Recommended Actions": statement}), catalog)


def test_recommendation_block_with_foreign_cve_cannot_lose_its_scope():
    first = f"{CVE} customers should install the update."
    block = f"{first} CVE-2026-5678 customers should install the other patch."
    source = article(
        f"## {CVE}\n{CVE} is actively exploited.\nExample Server 2.3\nHosted users need no action.\n{block}",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(
        EvidenceError, match="ambiguous.*recommendation|recommendation.*scope"
    ):
        validate_finding_evidence(
            report(**{"Recommended Actions": first}), build_reporting_catalog([source])
        )


@pytest.mark.parametrize("punctuation", ["?", "!", "..."])
def test_recommendation_source_punctuation_is_not_discarded(punctuation):
    statement = f"Install the update{punctuation}"
    source = article(
        f"## {CVE}\n{CVE} is actively exploited.\nExample Server 2.3\nHosted users need no action.\n\n{statement}",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="source-supported|complete"):
        validate_finding_evidence(
            report(**{"Recommended Actions": "Install the update"}), catalog
        )
    validate_finding_evidence(report(**{"Recommended Actions": statement}), catalog)


@pytest.mark.parametrize(
    "wrapped,fragment",
    [
        (
            "U.S. customers should install\nthe update immediately.",
            "U.S. customers should install",
        ),
        (
            "U.S. customers should\ninstall the update immediately.",
            "install the update immediately.",
        ),
        (
            "- U.S. customers should install\n  the update immediately.",
            "- U.S. customers should install",
        ),
        (
            "- Do not:\n  - install the update\n    on hosted systems.",
            "- install the update",
        ),
    ],
)
def test_wrapped_recommendations_preserve_logical_paragraph_or_list_item(
    wrapped, fragment
):
    source = article(
        f"## {CVE}\n\n{CVE} is actively exploited.\n\nExample Server 2.3\n\nHosted users need no action.\n\n{wrapped}",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="source-supported|complete"):
        validate_finding_evidence(report(**{"Recommended Actions": fragment}), catalog)
    validate_finding_evidence(
        report(**{"Recommended Actions": " ".join(wrapped.split())}), catalog
    )


def test_recommendation_cue_can_cross_a_wrapped_line_boundary():
    source = article(
        f"## {CVE}\n\n{CVE} is actively exploited.\n\nExample Server 2.3\n\nHosted users need no action.\n\nInstall\nthe update immediately.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    absent = report(
        **{"Recommended Actions": "Not stated in supplied sources."}
    ).replace("- **Action**: patch", "- **Action**: monitor")
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(absent, catalog)
    validate_finding_evidence(
        report(**{"Recommended Actions": "Install the update immediately."}), catalog
    )


def test_html_line_break_cannot_truncate_a_recommendation_paragraph():
    source = article(
        f"<h2>{CVE}</h2><p>{CVE} is actively exploited.</p><p>Example Server 2.3</p><p>Hosted users need no action.</p><p>U.S. customers should install<br>the update immediately.</p>",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="source-supported|complete"):
        validate_finding_evidence(
            report(**{"Recommended Actions": "U.S. customers should install"}), catalog
        )
    validate_finding_evidence(
        report(
            **{
                "Recommended Actions": "U.S. customers should install the update immediately."
            }
        ),
        catalog,
    )


def test_html_line_breaks_preserve_individual_version_list_entries():
    source = article(
        f"<h2>{CVE}</h2><p>{CVE} is actively exploited.</p><p>Affected versions:<br>Example Server 2.3<br>Example Server 2.4</p><p>Hosted users need no action.</p><p>Install the update.</p>",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(
        report(**{"Affected Versions": "Example Server 2.3; Example Server 2.4"}),
        catalog,
    )
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(report(), catalog)


@pytest.mark.parametrize(
    "nested,complete",
    [
        (
            "<ul><li>install the update on hosted systems</li></ul>",
            "Do not: install the update on hosted systems",
        ),
        (
            "<h3>Hosted systems</h3><ul><li><p>install the update on hosted systems</p></li></ul>",
            "Do not: Hosted systems install the update on hosted systems",
        ),
        (
            "<ul><li>install the update on hosted systems</li><li>restart the service</li></ul>",
            "Do not: install the update on hosted systems; restart the service",
        ),
    ],
)
def test_nested_html_recommendations_keep_outer_item_qualifications(nested, complete):
    source = article(
        f"<h2>{CVE}</h2><p>{CVE} is actively exploited.</p><p>Example Server 2.3</p><p>Hosted users need no action.</p><ul><li>Do not:{nested}</li></ul>",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="source-supported|complete"):
        validate_finding_evidence(
            report(**{"Recommended Actions": "install the update on hosted systems"}),
            catalog,
        )
    validate_finding_evidence(report(**{"Recommended Actions": complete}), catalog)


@pytest.mark.parametrize(
    "intro",
    [
        "Supported releases include ",
        "Supported releases are ",
        "Supported release includes ",
        "",
    ],
)
def test_cumulative_update_lists_require_all_releases(intro):
    first = "Example Server 2019 Cumulative Update 14"
    second = "Example Server 2019 Cumulative Update 15"
    source = article(
        f"{CVE} is actively exploited.\n\n{intro}{first} and {second}.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(report(**{"Affected Versions": first}), catalog)
    validate_finding_evidence(
        report(**{"Affected Versions": f"{first}; {second}"}), catalog
    )


def test_nested_html_version_entries_remain_separate_constraints():
    source = article(
        f"<h2>{CVE}</h2><p>{CVE} is actively exploited.</p><ul><li>Affected versions:<ul><li>Example Server 2.3</li><li>Example Server 2.4</li></ul></li></ul><p>Hosted users need no action.</p><p>Install the update.</p>",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(
        report(**{"Affected Versions": "Example Server 2.3; Example Server 2.4"}),
        catalog,
    )
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(report(), catalog)


@pytest.mark.parametrize(
    "recommendation",
    [
        "Customers should install Example Server 2019 Cumulative Update 15.",
        "Customers should install\nExample Server 2019 Cumulative Update 15.",
        "Customers are advised to install Example Server 2019 Cumulative Update 15.",
        "Administrators must apply Example Server 2019 Cumulative Update 15.",
        *[
            f"Customers should install Example Server 2019 Cumulative Update 15 on {qualifier} systems."
            for qualifier in ["affected", "impacted", "vulnerable", "unaffected"]
        ],
    ],
)
def test_cumulative_update_recommendations_are_not_affected_version_lists(
    recommendation,
):
    source = article(
        f"{CVE} is actively exploited.\n\nHosted users need no action.\n\n{recommendation}",
        source_links=["https://example.test/vendor"],
    )
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": "Not stated in supplied sources.",
                "Recommended Actions": " ".join(recommendation.split()),
            }
        ),
        build_reporting_catalog([source]),
    )


@pytest.mark.parametrize("breaks", ["<br>", "<br><br>", "<br> \n<br>"])
def test_html_list_item_breaks_keep_version_entries_and_recommendation_owner(breaks):
    source = article(
        f"<h2>{CVE}</h2><p>{CVE} is actively exploited.</p>"
        f"<ul><li>Affected versions:{breaks}Example Server 2.3{breaks}Example Server 2.4</li></ul>"
        f"<p>Hosted users need no action.</p><ul><li>Do not:{breaks}install the update on hosted systems.</li></ul>",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    values = {
        "Affected Versions": "Example Server 2.3; Example Server 2.4",
        "Recommended Actions": "Do not: install the update on hosted systems.",
    }
    validate_finding_evidence(report(**values), catalog)
    for omitted in ["Example Server 2.3", "Example Server 2.4"]:
        with pytest.raises(EvidenceError, match="omits"):
            validate_finding_evidence(
                report(**{**values, "Affected Versions": omitted}), catalog
            )
    with pytest.raises(EvidenceError, match="source-supported|complete"):
        validate_finding_evidence(
            report(
                **{
                    **values,
                    "Recommended Actions": "install the update on hosted systems.",
                }
            ),
            catalog,
        )


@pytest.mark.parametrize("separator", [". ", "; ", ", "])
def test_cumulative_list_and_recommendation_share_a_paragraph_without_losing_releases(
    separator,
):
    first = "Example Server 2019 Cumulative Update 14"
    second = "Example Server 2019 Cumulative Update 15"
    paragraph = f"{first} and {second}{separator}Customers should install the update."
    source = article(
        f"{CVE} is actively exploited.\n\n{paragraph}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(
            report(**{"Affected Versions": first, "Recommended Actions": paragraph}),
            catalog,
        )
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": f"{first}; {second}",
                "Recommended Actions": paragraph,
            }
        ),
        catalog,
    )


@pytest.mark.parametrize("breaks", ["<br><br>", "<br> \n<br>"])
def test_repeated_html_breaks_outside_lists_keep_recommendation_paragraphs(breaks):
    source = article(
        f"<h2>{CVE}</h2><p>{CVE} is actively exploited.</p><p>Example Server 2.3</p>"
        f"<p>Hosted users need no action.</p><div>Background information.{breaks}Install the update.</div>",
        source_links=["https://example.test/vendor"],
    )
    validate_finding_evidence(report(), build_reporting_catalog([source]))


@pytest.mark.parametrize("breaks", ["<br>", "<br><br>"])
@pytest.mark.parametrize("repeat_release", [False, True])
def test_cumulative_rows_before_advice_remain_complete_version_evidence(
    breaks, repeat_release
):
    first = "Example Server 2019 Cumulative Update 14"
    second = "Example Server 2019 Cumulative Update 15"
    advice = f"Customers should install {first if repeat_release else 'the update'}."
    source = article(
        f"<h2>{CVE}</h2><p>{CVE} is actively exploited.</p>"
        f"<ul><li>{first}{breaks}{second}{breaks}{advice}</li></ul><p>Hosted users need no action.</p>",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    actions = f"{first} {second} {advice}"
    for value in ["Not stated in supplied sources.", first, second]:
        with pytest.raises(EvidenceError, match="omits"):
            validate_finding_evidence(
                report(**{"Affected Versions": value, "Recommended Actions": actions}),
                catalog,
            )
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": f"{first}; {second}",
                "Recommended Actions": actions,
            }
        ),
        catalog,
    )


def test_update_named_only_in_advice_cannot_ground_an_affected_version_claim():
    version = "Example Server 2019 Cumulative Update 15"
    advice = f"Customers should install {version}."
    source = article(
        f"{CVE} is actively exploited.\n\nHosted users need no action.\n\n{advice}",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="unsupported affected-version"):
        validate_finding_evidence(
            report(**{"Affected Versions": version, "Recommended Actions": advice}),
            build_reporting_catalog([source]),
        )


@pytest.mark.parametrize("wrap", [" ", "<br>"])
@pytest.mark.parametrize("audience", ["Customers", "Customers of Example Server 2.3"])
def test_advice_after_release_rows_does_not_add_its_target_update(wrap, audience):
    first = "Example Server 2019 Cumulative Update 14"
    second = "Example Server 2019 Cumulative Update 15"
    target = "Example Server 2019 Cumulative Update 16"
    advice = f"{audience} should install{wrap}{target}."
    source = article(
        f"<h2>{CVE}</h2><p>{CVE} is actively exploited.</p>"
        f"<ul><li>{first}<br>{second}<br>{advice}</li></ul><p>Hosted users need no action.</p>",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    actions = f"{first} {second} {audience} should install {target}."
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": f"{first}; {second}",
                "Recommended Actions": actions,
            }
        ),
        catalog,
    )
    with pytest.raises(EvidenceError, match="unsupported affected-version"):
        validate_finding_evidence(
            report(
                **{
                    "Affected Versions": f"{first}; {second}; {target}",
                    "Recommended Actions": actions,
                }
            ),
            catalog,
        )


def test_generic_information_about_cumulative_updates_does_not_require_versions():
    source = article(
        f"{CVE} is actively exploited.\n\nFurther information about cumulative updates is available.\n\nHosted users need no action.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    validate_finding_evidence(
        report(**{"Affected Versions": "Not stated in supplied sources."}),
        build_reporting_catalog([source]),
    )


def test_explicit_cumulative_update_exclusions_keep_their_clause_role():
    version = "Example Server 2019 Cumulative Update 15"
    source = article(
        f"{CVE} is actively exploited.\n\nAffected versions: Customers of {version} are unaffected.\n\nInstall the update.",
        source_links=["https://example.test/vendor"],
    )
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": "Not stated in supplied sources.",
                "Exceptions": version,
            }
        ),
        build_reporting_catalog([source]),
    )


@pytest.mark.parametrize("separator", ["; ", ", ", "\n"])
@pytest.mark.parametrize("state", ["affected", "unaffected"])
def test_explicit_version_roles_after_advice_take_precedence(separator, state):
    version = "Example Server 2019 Cumulative Update 15"
    target = "Example Server 2019 Cumulative Update 16"
    paragraph = f"Customers should install {target}{separator}customers of {version} are {state}."
    source = article(
        f"{CVE} is actively exploited.\n\n{paragraph}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    values = {
        "Affected Versions": (
            version if state == "affected" else "Not stated in supplied sources."
        ),
        "Exceptions": "Hosted users need no action."
        + (f"; {version}" if state == "unaffected" else ""),
        "Recommended Actions": " ".join(paragraph.split()),
    }
    validate_finding_evidence(report(**values), catalog)
    missing = (
        {"Affected Versions": "Not stated in supplied sources."}
        if state == "affected"
        else {"Exceptions": "Hosted users need no action."}
    )
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(report(**{**values, **missing}), catalog)
    with pytest.raises(EvidenceError, match="unsupported affected-version"):
        validate_finding_evidence(
            report(
                **{
                    **values,
                    "Affected Versions": (
                        f"{version}; {target}" if state == "affected" else target
                    ),
                }
            ),
            catalog,
        )


def test_recommendation_qualifiers_do_not_hide_a_separate_version_assertion():
    source = article(
        f"{CVE} is actively exploited.\n\nCustomers should install Example Server 2019 Cumulative Update 16 on affected systems / customers of Example Server 2019 Cumulative Update 15 are unaffected.\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="ambiguous affected-version clause"):
        validate_finding_evidence(
            report(**{"Affected Versions": "Not stated in supplied sources."}),
            build_reporting_catalog([source]),
        )


@pytest.mark.parametrize("separator", [" / ", " | ", "; "])
@pytest.mark.parametrize(
    "predicate",
    [
        "is affected",
        "are unaffected",
        "was impacted",
        "remains vulnerable",
        "will be affected",
        "has been affected",
        "may have been impacted",
        "will not be affected",
        "has not been vulnerable",
        "could still be affected",
        "would have remained unaffected",
        "does not remain affected",
        "won't be affected",
        "hasn't been affected",
        "isn't affected",
        "becomes affected",
    ],
)
def test_advice_cannot_hide_unclassified_version_first_assertions(separator, predicate):
    statement = f"Customers should install Example Server 2019 Cumulative Update 16 on affected systems{separator}Example Server 2019 Cumulative Update 15 {predicate}."
    source = article(
        f"{CVE} is actively exploited.\n\n{statement}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="ambiguous affected-version clause"):
        validate_finding_evidence(
            report(
                **{
                    "Affected Versions": "Not stated in supplied sources.",
                    "Recommended Actions": statement,
                }
            ),
            build_reporting_catalog([source]),
        )


@pytest.mark.parametrize(
    "predicate",
    [
        "will be affected",
        "has been affected",
        "may have been impacted",
        "will not be affected",
        "has not been vulnerable",
        "could still be affected",
        "would have remained unaffected",
        "does not remain affected",
        "won't be affected",
        "hasn't been affected",
        "isn't affected",
        "becomes affected",
    ],
)
def test_auxiliary_assertions_in_unclassified_conjunctions_fail_closed(predicate):
    statement = f"Customers should install Example Server 2019 Cumulative Update 16 on affected systems and Example Server 2019 Cumulative Update 15 {predicate}."
    source = article(
        f"{CVE} is actively exploited.\n\n{statement}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="ambiguous affected-version clause"):
        validate_finding_evidence(
            report(
                **{
                    "Affected Versions": "Not stated in supplied sources.",
                    "Recommended Actions": statement,
                }
            ),
            build_reporting_catalog([source]),
        )


@pytest.mark.parametrize("connector", [", ", " and ", " or "])
@pytest.mark.parametrize(
    "predicate",
    [
        "cannot be affected",
        "cannot possibly be affected",
        "cannot have been unaffected",
    ],
)
def test_uncontracted_cannot_assertions_cannot_be_omitted(connector, predicate):
    statement = f"Customers should install Example Server 2019 Cumulative Update 16{connector}Example Server 2019 Cumulative Update 15 {predicate}."
    source = article(
        f"{CVE} is actively exploited.\n\n{statement}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="ambiguous affected-version clause"):
        validate_finding_evidence(
            report(
                **{
                    "Affected Versions": "Not stated in supplied sources.",
                    "Recommended Actions": statement,
                }
            ),
            build_reporting_catalog([source]),
        )


@pytest.mark.parametrize("connector", [", ", " and "])
@pytest.mark.parametrize(
    "predicate",
    [
        "need not be affected",
        "ought not to be affected",
        "used to be affected",
        "does not have to be affected",
        "has not had to be affected",
        "must not be affected",
        "will likely have been affected",
    ],
)
def test_standard_modal_chains_cannot_hide_version_assertions(connector, predicate):
    statement = f"Customers should install Example Server 2019 Cumulative Update 16{connector}Example Server 2019 Cumulative Update 15 {predicate}."
    source = article(
        f"{CVE} is actively exploited.\n\n{statement}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="ambiguous affected-version clause"):
        validate_finding_evidence(
            report(
                **{
                    "Affected Versions": "Not stated in supplied sources.",
                    "Recommended Actions": statement,
                }
            ),
            build_reporting_catalog([source]),
        )


@pytest.mark.parametrize("connector", [", ", " and "])
@pytest.mark.parametrize(
    "predicate",
    [
        "is expected to be affected",
        "was supposed to be impacted",
        "is going to be vulnerable",
        "is not expected to have been affected",
        "is considered unaffected",
        "seems likely to be affected",
        "appears to remain vulnerable",
        "was deemed to be affected",
        "is reported as unaffected",
        "has been described as vulnerable",
        "counts as affected",
        "qualifies as unaffected",
    ],
)
def test_unclassified_version_states_cannot_be_absorbed_by_advice(connector, predicate):
    statement = f"Customers should install Example Server 2019 Cumulative Update 16{connector}Example Server 2019 Cumulative Update 15 {predicate}."
    source = article(
        f"{CVE} is actively exploited.\n\n{statement}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="ambiguous affected-version clause"):
        validate_finding_evidence(
            report(
                **{
                    "Affected Versions": "Not stated in supplied sources.",
                    "Recommended Actions": statement,
                }
            ),
            build_reporting_catalog([source]),
        )


@pytest.mark.parametrize(
    "description",
    [
        "on affected systems",
        "for all impacted installations",
        "to vulnerable servers",
        "within the unaffected deployments",
    ],
)
def test_advised_updates_preserve_supported_descriptive_state_phrases(description):
    statement = f"Customers are advised to install Example Server 2019 Cumulative Update 16 {description}."
    source = article(
        f"{CVE} is actively exploited.\n\n{statement}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": "Not stated in supplied sources.",
                "Recommended Actions": statement,
            }
        ),
        build_reporting_catalog([source]),
    )


@pytest.mark.parametrize("introduction", [": ", " include ", " are "])
def test_advice_introducing_affected_releases_requires_the_complete_list(introduction):
    version = "Example Server 2019 Cumulative Update 15"
    statement = f"Customers should install the fix for affected releases{introduction}{version}."
    source = article(
        f"{CVE} is actively exploited.\n\n{statement}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(
            report(
                **{
                    "Affected Versions": "Not stated in supplied sources.",
                    "Recommended Actions": statement,
                }
            ),
            catalog,
        )
    validate_finding_evidence(
        report(**{"Affected Versions": version, "Recommended Actions": statement}),
        catalog,
    )


@pytest.mark.parametrize(
    "tail", [": ", ", namely ", " including ", " such as ", " (", " running "]
)
@pytest.mark.parametrize(
    "description", ["on affected systems", "for vulnerable products"]
)
def test_descriptive_state_exemptions_cannot_hide_following_details(description, tail):
    statement = f"Customers should install the fix {description}{tail}Example Server 2019 Cumulative Update 15."
    source = article(
        f"{CVE} is actively exploited.\n\n{statement}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="ambiguous affected-version clause"):
        validate_finding_evidence(
            report(
                **{
                    "Affected Versions": "Not stated in supplied sources.",
                    "Recommended Actions": statement,
                }
            ),
            build_reporting_catalog([source]),
        )


@pytest.mark.parametrize("punctuation", [".", "!", "?", "…"])
@pytest.mark.parametrize(
    "description",
    [
        "on affected systems",
        "for vulnerable products",
        "for affected releases",
        "for affected versions",
    ],
)
def test_terminal_descriptive_advice_does_not_introduce_a_version_list(
    description, punctuation
):
    statement = f"Customers should install Example Server 2019 Cumulative Update 16 {description}{punctuation}"
    source = article(
        f"{CVE} is actively exploited.\n\n{statement}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": "Not stated in supplied sources.",
                "Recommended Actions": statement,
            }
        ),
        build_reporting_catalog([source]),
    )


@pytest.mark.parametrize("label", ["affected releases", "affected versions"])
def test_advice_list_heading_retains_following_release_lines(label):
    first = "Example Server 2019 Cumulative Update 14"
    second = "Example Server 2019 Cumulative Update 15"
    statement = f"Customers should install the fix for {label}:\n{first}\n{second}."
    source = article(
        f"{CVE} is actively exploited.\n\n{statement}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    actions = " ".join(statement.split())
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(
            report(**{"Affected Versions": first, "Recommended Actions": actions}),
            catalog,
        )
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": f"{first}; {second}",
                "Recommended Actions": actions,
            }
        ),
        catalog,
    )


@pytest.mark.parametrize("label", ["affected versions", "affected releases"])
@pytest.mark.parametrize("punctuation", [".", "!"])
@pytest.mark.parametrize("marker", ["- ", "1. "])
def test_terminal_advice_cue_owns_following_markdown_release_rows(
    label, punctuation, marker
):
    first = "Example Server 2.3"
    second = "Example Server 2.4"
    statement = f"Customers should install the fix for {label}{punctuation}"
    source = article(
        f"{CVE} is actively exploited.\n\n{statement}\n\n{marker}{first}\n{marker}{second}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    for missing in ["Not stated in supplied sources.", first]:
        with pytest.raises(EvidenceError, match="omits"):
            validate_finding_evidence(
                report(
                    **{"Affected Versions": missing, "Recommended Actions": statement}
                ),
                catalog,
            )
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": f"{first}; {second}",
                "Recommended Actions": statement,
            }
        ),
        catalog,
    )


def test_terminal_advice_cue_owns_following_html_release_rows():
    statement = "Customers should install the fix for affected versions."
    source = article(
        f"<h2>{CVE}</h2><p>{CVE} is actively exploited.</p><p>{statement}</p><ul><li>Example Server 2.3</li><li>Example Server 2.4</li></ul><p>Hosted users need no action.</p>",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(report(**{"Recommended Actions": statement}), catalog)
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": "Example Server 2.3; Example Server 2.4",
                "Recommended Actions": statement,
            }
        ),
        catalog,
    )


@pytest.mark.parametrize(
    "boundary", ["Hosted users need no action.", "## Additional information"]
)
def test_pending_advice_cue_expires_before_unrelated_release_mentions(boundary):
    statement = "Customers should install the fix for affected versions."
    source = article(
        f"{CVE} is actively exploited.\n\nHosted users need no action.\n\n{statement}\n\n{boundary}\n\n- Example Server 2.3",
        source_links=["https://example.test/vendor"],
    )
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": "Not stated in supplied sources.",
                "Recommended Actions": statement,
            }
        ),
        build_reporting_catalog([source]),
    )


@pytest.mark.parametrize(
    "introduction",
    [
        "Customers should install the fix for affected versions.",
        "Customers should install the fix for affected versions:",
    ],
)
@pytest.mark.parametrize(
    "annotation",
    [" — {cve}", " - {cve}", " | {cve}", " ({cve})", " [{cve}]", " for {cve}"],
)
def test_same_cve_annotations_do_not_remove_release_constraints(
    introduction, annotation
):
    tag = annotation.format(cve=CVE)
    first = "Example Server 2.3"
    second = "Example Server 2.4"
    source = article(
        f"{CVE} is actively exploited.\n\n{introduction}\n\n- {first}{tag}\n- {second}{tag}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    for missing in ["Not stated in supplied sources.", first]:
        with pytest.raises(EvidenceError, match="omits"):
            validate_finding_evidence(
                report(
                    **{
                        "Affected Versions": missing,
                        "Recommended Actions": introduction,
                    }
                ),
                catalog,
            )
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": f"{first}; {second}",
                "Recommended Actions": introduction,
            }
        ),
        catalog,
    )


def test_pending_list_keeps_same_cve_metadata_but_excludes_foreign_rows():
    introduction = "Customers should install the fix for affected versions."
    source = article(
        f"## {CVE}\n{CVE} is actively exploited.\n\n{introduction}\n\n{CVE}\n\n- {CVE}: Example Server 2.3\n- Example Server 9.9 — CVE-2026-9999\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(
            report(
                **{
                    "Affected Versions": "Not stated in supplied sources.",
                    "Recommended Actions": introduction,
                }
            ),
            catalog,
        )
    validate_finding_evidence(report(**{"Recommended Actions": introduction}), catalog)


@pytest.mark.parametrize(
    "version", ["Example Server 2.3", "Example Server 2.3 (Windows)"]
)
@pytest.mark.parametrize("tag", [" — {cve}.", " for {cve}."])
def test_cve_metadata_normalization_preserves_release_qualifiers(version, tag):
    introduction = "Customers should install the fix for affected versions."
    source = article(
        f"{CVE} is actively exploited.\n\n{introduction}\n\n- {version}{tag.format(cve=CVE)}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    validate_finding_evidence(
        report(**{"Affected Versions": version, "Recommended Actions": introduction}),
        build_reporting_catalog([source]),
    )


@pytest.mark.parametrize(
    "annotation",
    [" — {cve}", " - {cve}", " | {cve}", " for {cve}", " ({cve})", " [{cve}]"],
)
@pytest.mark.parametrize("qualifier", ["(Windows)", "and later"])
def test_release_qualifiers_after_cve_tags_remain_complete(annotation, qualifier):
    introduction = "Customers should install the fix for affected versions."
    version = f"Example Server 2.3 {qualifier}"
    source = article(
        f"{CVE} is actively exploited.\n\n{introduction}\n\n- Example Server 2.3{annotation.format(cve=CVE)} {qualifier}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(
        report(**{"Affected Versions": version, "Recommended Actions": introduction}),
        catalog,
    )
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(
            report(**{"Recommended Actions": introduction}), catalog
        )


@pytest.mark.parametrize("wrappers", [("(", ")"), ("[", "]")])
@pytest.mark.parametrize(
    "annotated, qualifier",
    [
        ("{cve}, Windows", "Windows"),
        ("{cve}; Windows", "Windows"),
        ("{cve} — Windows", "Windows"),
        ("Windows, {cve}", "Windows"),
        ("Windows, {cve}, x64", "Windows, x64"),
        ("{cve}, Windows, x64", "Windows, x64"),
        ("{cve}, Windows and Linux", "Windows and Linux"),
        ("Windows (x64), {cve}", "Windows (x64)"),
    ],
)
def test_wrapped_cve_metadata_preserves_complete_grouped_qualifiers(
    wrappers, annotated, qualifier
):
    left, right = wrappers
    introduction = "Customers should install the fix for affected versions."
    version = f"Example Server 2.3 {left}{qualifier}{right}"
    source = article(
        f"{CVE} is actively exploited.\n\n{introduction}\n\n- Example Server 2.3 {left}{annotated.format(cve=CVE)}{right}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(
        report(**{"Affected Versions": version, "Recommended Actions": introduction}),
        catalog,
    )
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(
            report(**{"Recommended Actions": introduction}), catalog
        )


def test_grouped_qualifiers_do_not_consume_a_following_version_entry():
    introduction = "Customers should install the fix for affected versions."
    first = "Example Server 2.3 (Windows, x64)"
    second = "Example Server 2.4 (Linux)"
    source = article(
        f"{CVE} is actively exploited.\n\n{introduction}\n\n- Example Server 2.3 ({CVE}, Windows, x64); {second}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(
            report(**{"Affected Versions": first, "Recommended Actions": introduction}),
            catalog,
        )
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": f"{first}; {second}",
                "Recommended Actions": introduction,
            }
        ),
        catalog,
    )


@pytest.mark.parametrize("wrappers", [("(", ")"), ("[", "]")])
@pytest.mark.parametrize(
    "annotated, qualifier",
    [
        ("{cve} and Windows", "Windows"),
        ("Windows and {cve}", "Windows"),
        ("Windows and {cve} and Linux", "Windows and Linux"),
        ("{cve} or Windows", "Windows"),
        ("Windows or {cve}", "Windows"),
        ("Windows or {cve} or Linux", "Windows or Linux"),
        ("Windows and ({cve}) and Linux", "Windows and Linux"),
        ("Windows and {cve} or Linux", "Windows or Linux"),
    ],
)
def test_grouped_attribution_members_preserve_remaining_connectors(
    wrappers, annotated, qualifier
):
    left, right = wrappers
    introduction = "Customers should install the fix for affected versions."
    source = article(
        f"{CVE} is actively exploited.\n\n{introduction}\n\n- Example Server 2.3 {left}{annotated.format(cve=CVE)}{right}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(
        report(
            **{
                "Affected Versions": f"Example Server 2.3 {left}{qualifier}{right}",
                "Recommended Actions": introduction,
            }
        ),
        catalog,
    )
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(
            report(**{"Recommended Actions": introduction}), catalog
        )


@pytest.mark.parametrize("connector", ["together with", "as well as"])
def test_unclassified_grouped_attribution_cannot_become_a_malformed_constraint(
    connector,
):
    introduction = "Customers should install the fix for affected versions."
    source = article(
        f"{CVE} is actively exploited.\n\n{introduction}\n\n- Example Server 2.3 ({CVE} {connector} Windows)\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    with pytest.raises(EvidenceError, match="ambiguous.*attribution"):
        validate_finding_evidence(
            report(
                **{
                    "Affected Versions": f"Example Server 2.3 ({connector} Windows)",
                    "Recommended Actions": introduction,
                }
            ),
            build_reporting_catalog([source]),
        )


@pytest.mark.parametrize("wrappers", [("(", ")"), ("[", "]")])
@pytest.mark.parametrize("connector", ["—", "–", "|", ":", ",", ";"])
def test_grouped_qualifiers_preserve_compact_connector_spacing(wrappers, connector):
    left, right = wrappers
    introduction = "Customers should install the fix for affected versions."
    version = f"Example Server 2.3 {left}Windows{connector}x64{right}"
    source = article(
        f"{CVE} is actively exploited.\n\n{introduction}\n\n- Example Server 2.3 {left}{CVE}, Windows{connector}x64{right}\n\nHosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    validate_finding_evidence(
        report(**{"Affected Versions": version, "Recommended Actions": introduction}),
        catalog,
    )
    altered = f"Example Server 2.3 {left}Windows {connector} x64{right}"
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(
            report(
                **{"Affected Versions": altered, "Recommended Actions": introduction}
            ),
            catalog,
        )


@pytest.mark.parametrize("wrappers", [("(", ")"), ("[", "]")])
@pytest.mark.parametrize("connector", ["—", "–", "|", ":", ",", ";"])
@pytest.mark.parametrize("retained_space", ["", " "])
def test_grouped_metadata_removal_preserves_connector_owned_spacing(
    wrappers, connector, retained_space
):
    left, right = wrappers
    discarded_space = "" if retained_space else " "
    introduction = "Customers should install the fix for affected versions."
    source = article(
        f"{CVE} is actively exploited.\n\n{introduction}\n\n"
        f"- Example Server 2.3 {left}Windows{discarded_space}, "
        f"{CVE}{retained_space}{connector} x64{right}\n\n"
        "Hosted users need no action.",
        source_links=["https://example.test/vendor"],
    )
    catalog = build_reporting_catalog([source])
    version = f"Example Server 2.3 {left}Windows{retained_space}{connector} x64{right}"
    validate_finding_evidence(
        report(**{"Affected Versions": version, "Recommended Actions": introduction}),
        catalog,
    )
    altered = f"Example Server 2.3 {left}Windows{discarded_space}{connector} x64{right}"
    with pytest.raises(EvidenceError, match="omits"):
        validate_finding_evidence(
            report(
                **{"Affected Versions": altered, "Recommended Actions": introduction}
            ),
            catalog,
        )
