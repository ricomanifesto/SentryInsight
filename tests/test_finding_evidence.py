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
    validate_finding_evidence(report(), build_reporting_catalog([source]))


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
    validate_finding_evidence(report(), build_reporting_catalog([source]))


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
                "Exceptions": (
                    clause
                    if "not affected" in clause
                    else "Hosted users need no action."
                )
            },
        ),
        catalog,
    )
    with pytest.raises(EvidenceError, match="non-affected"):
        validate_finding_evidence(
            report(
                **{
                    "Exceptions": (
                        clause
                        if "not affected" in clause
                        else "Hosted users need no action."
                    )
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
        **{"Affected Versions": "Example Server 2.3; Other Server 9.9"}
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
        f"{CVE} is actively exploited.\nAffected versions:\nExample Server 2.3\n{qualifier}\nHosted users need no action.\nInstall the update.",
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
        "sentences": "Hosted users need no action.\nInstall the update.",
        "headings": "### Exceptions\nHosted service is exempt.\n### Recommended Actions\nRestart the service.",
        "combined": "Hosted users need no action, but administrators should install the update.",
    }[layout]
    exception = (
        "Hosted service is exempt."
        if layout == "headings"
        else "Hosted users need no action"
    )
    action = "Restart the service." if layout == "headings" else "install the update"
    source = article(
        f"## {CVE}\n{CVE} is actively exploited.\nExample Server 2.3\n{details}",
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
        f"{CVE} is actively exploited.\nRelease {source_version} is vulnerable.\nHosted users need no action.\nInstall the update.",
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
        f"{CVE} is actively exploited.\nExample Server 2.3\nHosted users need no action.\nInstall the update.",
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
