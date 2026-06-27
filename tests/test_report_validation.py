import unittest
from pathlib import Path

from src.core.report_validation import (
    ensure_source_attribution_section,
    render_source_attribution_section,
    validate_report_content,
)

VALID_REPORT = """# Exploitation Report

Recent exploitation activity is concentrated in edge systems.

## Active Exploitation Details

### Example Vulnerability
- **Description**: Attackers are exploiting a vulnerable service.
- **Impact**: Remote access.
- **Status**: Active exploitation observed.

## Affected Systems and Products

- **Example Product**: Affected versions are exposed.

## Attack Vectors and Techniques

- **Internet-facing service**: Attackers send crafted requests.

## Threat Actor Activities

- **Unknown actor**: Opportunistic exploitation.
"""

VALID_REPORT_WITH_SOURCE_ATTRIBUTION = VALID_REPORT + """
## Source Attribution

- **Example exploitation report**: Example Source - https://example.test/report
- **Second exploitation report**: Example Source - https://example.test/second
- **Source-only exploitation report**: Example Source
"""

SOURCE_ATTRIBUTION_FIXTURE = (
    Path(__file__).parent / "fixtures" / "source_attribution_report.md"
)


class ReportValidationTests(unittest.TestCase):
    def test_valid_report_passes(self):
        self.assertEqual(validate_report_content(VALID_REPORT), [])

    def test_dangling_bold_list_item_fails(self):
        issues = validate_report_content(
            VALID_REPORT.replace(
                "- **Unknown actor**: Opportunistic exploitation.",
                "- **FishMonger",
            )
        )

        self.assertTrue(any(issue.code == "malformed_markdown" for issue in issues))

    def test_bold_only_list_item_without_description_fails(self):
        issues = validate_report_content(
            VALID_REPORT.replace(
                "- **Unknown actor**: Opportunistic exploitation.",
                "- **FishMonger**",
            )
        )

        self.assertTrue(any(issue.code == "malformed_markdown" for issue in issues))

    def test_colon_only_bold_list_item_without_description_fails(self):
        issues = validate_report_content(
            VALID_REPORT.replace(
                "- **Unknown actor**: Opportunistic exploitation.",
                "- **FishMonger**:",
            )
        )

        self.assertTrue(any(issue.code == "malformed_markdown" for issue in issues))

    def test_punctuation_only_bold_list_item_without_description_fails(self):
        issues = validate_report_content(
            VALID_REPORT.replace(
                "- **Unknown actor**: Opportunistic exploitation.",
                "- **FishMonger**: --",
            )
        )

        self.assertTrue(any(issue.code == "malformed_markdown" for issue in issues))

    def test_inline_code_bold_list_item_description_passes(self):
        report = VALID_REPORT.replace(
            "- **Unknown actor**: Opportunistic exploitation.",
            "- **Example Package**: `@mastra/*`",
        )

        self.assertEqual(validate_report_content(report), [])

    def test_four_space_nested_dangling_bold_list_item_fails(self):
        issues = validate_report_content(
            VALID_REPORT.replace(
                "- **Unknown actor**: Opportunistic exploitation.",
                "- **Parent actor**: Coordinated exploitation.\n" "    - **FishMonger",
            )
        )

        self.assertTrue(any(issue.code == "malformed_markdown" for issue in issues))

    def test_four_space_nested_bold_list_item_with_description_passes(self):
        report = VALID_REPORT.replace(
            "- **Unknown actor**: Opportunistic exploitation.",
            "- **Parent actor**: Coordinated exploitation.\n"
            "    - **FishMonger**: Deployed a Windows backdoor.",
        )

        self.assertEqual(validate_report_content(report), [])

    def test_wrapped_bold_list_label_with_description_passes(self):
        report = VALID_REPORT.replace(
            "- **Unknown actor**: Opportunistic exploitation.",
            "- **Microsoft Defender for Endpoint and Windows Defender\n"
            "  Antivirus**: Affected versions require mitigation.",
        )

        self.assertEqual(validate_report_content(report), [])

    def test_nested_bold_marker_does_not_close_broken_parent_label(self):
        issues = validate_report_content(
            VALID_REPORT.replace(
                "- **Unknown actor**: Opportunistic exploitation.",
                "- **FishMonger\n" "  - **Campaign**: Deployed a Windows backdoor.",
            )
        )

        self.assertTrue(any(issue.code == "malformed_markdown" for issue in issues))

    def test_inline_code_strong_marker_does_not_close_broken_label(self):
        issues = validate_report_content(
            VALID_REPORT.replace(
                "- **Unknown actor**: Opportunistic exploitation.",
                "- **Package `@scope/**`: affected versions require review.",
            )
        )

        self.assertTrue(any(issue.code == "malformed_markdown" for issue in issues))

    def test_inline_code_strong_marker_with_closed_label_passes(self):
        report = VALID_REPORT.replace(
            "- **Unknown actor**: Opportunistic exploitation.",
            "- **Package `@scope/**`**: affected versions require review.",
        )

        self.assertEqual(validate_report_content(report), [])

    def test_html_entity_punctuation_only_suffix_fails(self):
        issues = validate_report_content(
            VALID_REPORT.replace(
                "- **Unknown actor**: Opportunistic exploitation.",
                "- **FishMonger**: &mdash;",
            )
        )

        self.assertTrue(any(issue.code == "malformed_markdown" for issue in issues))

    def test_numeric_html_entity_punctuation_only_suffix_fails(self):
        issues = validate_report_content(
            VALID_REPORT.replace(
                "- **Unknown actor**: Opportunistic exploitation.",
                "- **FishMonger**: &#8212;",
            )
        )

        self.assertTrue(any(issue.code == "malformed_markdown" for issue in issues))

    def test_bold_heading_with_continuation_list_passes(self):
        report = VALID_REPORT.replace(
            "- **Unknown actor**: Opportunistic exploitation.",
            "- **FishMonger**\n"
            "  - **Campaign**: Deployed a Windows variant of the SprySOCKS backdoor.",
        )

        self.assertEqual(validate_report_content(report), [])

    def test_source_attribution_report_fixture_validates_expected_rows(self):
        expected_entries = [
            "- **CISA: exploited KEV update**: Example Research - https://example.test/kev",
            "- **Parenthesized URL report**: Example Source - https://example.test/report(1)",
            "- **Source-only exploitation report**: Example Source",
        ]

        fixture_markdown = SOURCE_ATTRIBUTION_FIXTURE.read_text(encoding="utf-8")

        self.assertEqual(
            validate_report_content(
                fixture_markdown,
                require_source_attribution=True,
                source_attribution_entries=expected_entries,
            ),
            [],
        )

    def test_ensure_source_attribution_section_appends_canonical_entries(self):
        report = ensure_source_attribution_section(
            VALID_REPORT,
            [
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertIn(
            "\n## Source Attribution\n\n"
            "- **Example exploitation report**: Example Source - https://example.test/report\n",
            report,
        )
        self.assertEqual(
            validate_report_content(
                report,
                require_source_attribution=True,
                source_attribution_entries=[
                    "- **Example exploitation report**: Example Source - https://example.test/report"
                ],
            ),
            [],
        )

    def test_render_source_attribution_section_deduplicates_entries(self):
        section = render_source_attribution_section(
            [
                "- **Example exploitation report**: Example Source - https://example.test/report",
                "  - **Example exploitation report**: Example Source - https://example.test/report  ",
                "",
                "- **Second exploitation report**: Example Source - https://example.test/second",
            ]
        )

        self.assertEqual(
            section,
            "\n".join(
                [
                    "## Source Attribution",
                    "",
                    "- **Example exploitation report**: Example Source - https://example.test/report",
                    "- **Second exploitation report**: Example Source - https://example.test/second",
                    "",
                ]
            ),
        )

    def test_ensure_source_attribution_section_replaces_existing_section(self):
        report = ensure_source_attribution_section(
            VALID_REPORT
            + "\n## Source Attribution\n\n- **Article Title**: Source name - URL\n",
            [
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertNotIn("Article Title", report)
        self.assertIn(
            "- **Example exploitation report**: Example Source - https://example.test/report",
            report,
        )

    def test_ensure_source_attribution_section_removes_duplicate_stale_sections(self):
        report = ensure_source_attribution_section(
            VALID_REPORT
            + "\n## Source Attribution\n\n- No sources were provided.\n"
            + "\n## Source Attribution\n\n- **Article Title**: Source name - URL\n",
            [
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertNotIn("No sources were provided", report)
        self.assertNotIn("Article Title", report)
        self.assertEqual(report.count("## Source Attribution"), 1)
        self.assertEqual(
            validate_report_content(
                report,
                require_source_attribution=True,
                source_attribution_entries=[
                    "- **Example exploitation report**: Example Source - https://example.test/report"
                ],
            ),
            [],
        )

    def test_ensure_source_attribution_section_preserves_tilde_fenced_headings(self):
        report = ensure_source_attribution_section(
            VALID_REPORT + """
~~~markdown
## Source Attribution

- Example text inside a code block
~~~

## Source Attribution

- No sources were provided.
""",
            [
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertIn("~~~markdown\n## Source Attribution", report)
        self.assertIn("- Example text inside a code block", report)
        self.assertNotIn("No sources were provided", report)
        self.assertEqual(report.count("## Source Attribution"), 2)
        self.assertEqual(
            validate_report_content(
                report,
                require_source_attribution=True,
                source_attribution_entries=[
                    "- **Example exploitation report**: Example Source - https://example.test/report"
                ],
            ),
            [],
        )

    def test_exact_source_attribution_entries_reject_embedded_url(self):
        issues = validate_report_content(
            VALID_REPORT + """
## Source Attribution

- **Aggregator URL report**: Example Source - https://aggregator.test/?u=https://vendor.test/advisory
""",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Vendor advisory**: Vendor - https://vendor.test/advisory"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_exact_source_attribution_entries_preserve_url_case(self):
        issues = validate_report_content(
            VALID_REPORT + """
## Source Attribution

- **Vendor advisory**: Vendor - https://vendor.test/Fix
""",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Vendor advisory**: Vendor - https://vendor.test/fix"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_required_source_attribution_without_requirements_fails(self):
        issues = validate_report_content(VALID_REPORT, require_source_attribution=True)

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_missing_required_source_attribution_section_fails(self):
        issues = validate_report_content(
            VALID_REPORT,
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_blank_required_source_attribution_section_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n## Source Attribution\n\n",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_source_attribution_heading_mention_does_not_satisfy_requirement(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\nThis report should include ## Source Attribution with https://example.test/report.\n",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_source_attribution_inside_code_block_does_not_satisfy_requirement(self):
        issues = validate_report_content(
            VALID_REPORT + """
## Source Attribution

```text
https://example.test/report
```
""",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_fenced_source_attribution_section_does_not_satisfy_requirement(self):
        issues = validate_report_content(
            VALID_REPORT + """
```markdown
## Source Attribution

- **Example exploitation report**: Example Source - https://example.test/report
```
""",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_placeholder_source_attribution_entry_fails(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n## Source Attribution\n\n- **Article Title**: Source name - URL\n",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_negative_source_attribution_entry_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n## Source Attribution\n\n- No sources were provided.\n",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_source_name_only_fails_when_url_is_required(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n## Source Attribution\n\n- **Example exploitation report**: Example Source\n",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_repeated_source_name_requires_each_url(self):
        partial_report = VALID_REPORT + """
## Source Attribution

- **Example exploitation report**: Example Source - https://example.test/report
"""

        issues = validate_report_content(
            partial_report,
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Example exploitation report**: Example Source - https://example.test/report",
                "- **Second exploitation report**: Example Source - https://example.test/second",
            ],
        )
        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

        self.assertEqual(
            validate_report_content(
                VALID_REPORT_WITH_SOURCE_ATTRIBUTION,
                require_source_attribution=True,
                source_attribution_entries=[
                    "- **Example exploitation report**: Example Source - https://example.test/report",
                    "- **Second exploitation report**: Example Source - https://example.test/second",
                ],
            ),
            [],
        )

    def test_url_requirement_requires_exact_url_match(self):
        issues = validate_report_content(
            VALID_REPORT + """
## Source Attribution

- **Longer URL report**: Example Source - https://example.test/reporting
""",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_url_requirement_rejects_extension_prefix_match(self):
        issues = validate_report_content(
            VALID_REPORT + """
## Source Attribution

- **Extension URL report**: Example Source - https://example.test/report.txt
""",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_noncanonical_markdown_link_attribution_fails(self):
        issues = validate_report_content(
            VALID_REPORT + """
## Source Attribution

- **Markdown URL report**: [Example Source](https://example.test/report)
""",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_noncanonical_sentence_punctuation_attribution_fails(self):
        issues = validate_report_content(
            VALID_REPORT + """
## Source Attribution

- **Sentence URL report**: Example Source - https://example.test/report.
""",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Example exploitation report**: Example Source - https://example.test/report"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_url_requirement_allows_parentheses_in_url(self):
        self.assertEqual(
            validate_report_content(
                VALID_REPORT + """
## Source Attribution

- **Parenthesized URL report**: Example Source - https://example.test/report(1)
""",
                require_source_attribution=True,
                source_attribution_entries=[
                    "- **Parenthesized URL report**: Example Source - https://example.test/report(1)"
                ],
            ),
            [],
        )

    def test_source_only_article_requires_source_and_title(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n## Source Attribution\n\n- **Different report**: Example Source\n",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Source-only exploitation report**: Example Source"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )
        self.assertEqual(
            validate_report_content(
                VALID_REPORT_WITH_SOURCE_ATTRIBUTION,
                require_source_attribution=True,
                source_attribution_entries=[
                    "- **Source-only exploitation report**: Example Source"
                ],
            ),
            [],
        )

    def test_source_only_markers_must_appear_in_same_attribution_entry(self):
        issues = validate_report_content(
            VALID_REPORT + """
## Source Attribution

- **Source-only exploitation report**: Different Source
- **Different report**: Example Source
""",
            require_source_attribution=True,
            source_attribution_entries=[
                "- **Source-only exploitation report**: Example Source"
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_api_error_marker_fails(self):
        issues = validate_report_content(
            "# Error Generating Exploitation Report\n\nError code: 404"
        )

        self.assertTrue(any(issue.code == "error_marker" for issue in issues))

    def test_api_error_marker_matching_is_case_insensitive(self):
        issues = validate_report_content(
            "# exploitation report\n\nupstream response returned error code: 404"
        )

        self.assertTrue(any(issue.code == "error_marker" for issue in issues))

    def test_api_error_marker_in_code_block_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n```\n# Error\nError code: 404\n```\n"
        )

        self.assertTrue(any(issue.code == "error_marker" for issue in issues))

    def test_missing_required_section_fails(self):
        issues = validate_report_content("# Exploitation Report\n\nSummary only")

        self.assertTrue(any(issue.code == "missing_section" for issue in issues))

    def test_empty_report_fails(self):
        issues = validate_report_content("")

        self.assertEqual(issues[0].code, "empty_report")

    def test_script_tag_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n<script>alert('xss')</script>\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_javascript_link_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n[malicious link](javascript:alert('xss'))\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_entity_encoded_javascript_link_fails(self):
        issues = validate_report_content(
            VALID_REPORT + '\n<a href="java&#115;cript:alert(1)">click</a>\n'
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_entity_encoded_markdown_javascript_link_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n[malicious link](java&#115;cript:alert('xss'))\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_entity_encoded_reference_javascript_link_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n[malicious link][x]\n\n[x]: java&#115;cript:alert(1)\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_wrapped_reference_javascript_link_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n[malicious link][x]\n\n[x]:\n java&#115;cript:alert(1)\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_unindented_wrapped_reference_javascript_link_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n[malicious link][x]\n\n[x]:\njava&#115;cript:alert(1)\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_entity_encoded_control_character_javascript_link_fails(self):
        issues = validate_report_content(
            VALID_REPORT + '\n<a href="jav&#x09;ascript:alert(1)">click</a>\n'
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_markdown_escaped_javascript_link_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n[malicious link](javascript\\:alert('xss'))\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_inline_code_active_content_example_passes(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\nUse `javascript:alert(1)` as an example of a dangerous URL.\n"
        )

        self.assertEqual(issues, [])

    def test_inline_code_after_less_than_text_passes(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\nWhen x < y, use `javascript:alert(1)` as a blocked URL example.\n"
        )

        self.assertEqual(issues, [])

    def test_multi_backtick_inline_code_active_content_example_passes(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\nUse ``javascript:alert(1)`` as an example of a dangerous URL.\n"
        )

        self.assertEqual(issues, [])

    def test_fenced_code_active_content_example_passes(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n```html\n<script>alert('xss')</script>\n<img src=x onerror=alert(1)>\n```\n"
        )

        self.assertEqual(issues, [])

    def test_list_nested_fenced_code_active_content_example_passes(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n- Example\n\n    ```html\n    <script>alert('xss')</script>\n    ```\n"
        )

        self.assertEqual(issues, [])

    def test_over_indented_list_fence_does_not_hide_active_html(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n- Example\n\n       ```html\n<img src=x onerror=alert(1)>\n```\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_list_code_indented_fence_does_not_hide_active_html(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n- Example\n\n      ```html\n<img src=x onerror=alert(1)>\n```\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_list_nested_fence_closer_does_not_hide_later_active_html(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n- Example\n\n    ```html\n    <script>alert('safe')</script>\n    ```\n\n<img src=x onerror=alert(1)>\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_fenced_code_inside_raw_html_block_fails(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n<div>\n```html\n<img src=x onerror=alert(1)>\n```\n</div>\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_fenced_code_inside_custom_html_block_fails(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n<x-report>\n```html\n<img src=x onerror=alert(1)>\n```\n</x-report>\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_quoted_html_closer_does_not_end_raw_html_block(self):
        issues = validate_report_content(
            VALID_REPORT
            + '\n<div title="</div>">\n```html\n<img src=x onerror=alert(1)>\n```\n</div>\n'
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_nested_html_openers_do_not_hide_active_html(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n<div><div>\n</div>\n```html\n<img src=x onerror=alert(1)>\n```\n</div>\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_non_void_self_closing_html_block_does_not_hide_active_html(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n<div/>\n```html\n<img src=x onerror=alert(1)>\n```\n</div>\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_invalid_backtick_fence_info_does_not_hide_active_html(self):
        issues = validate_report_content(
            VALID_REPORT + "\n``` `\n<img src=x onerror=alert(1)>\n```\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_tab_indented_fence_does_not_hide_active_html(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\nStandalone paragraph before the tab-indented opener.\n\n\t```html\n<img src=x onerror=alert(1)>\n```\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_tilde_fenced_code_active_content_example_passes(self):
        issues = validate_report_content(
            VALID_REPORT + "\n~~~html\n<script>alert('xss')</script>\n~~~\n"
        )

        self.assertEqual(issues, [])

    def test_indented_code_active_content_example_passes(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\nParagraph before the code example.\n\n    <script>alert('xss')</script>\n"
        )

        self.assertEqual(issues, [])

    def test_indented_html_after_paragraph_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\nIntro\n    <img src=x onerror=alert(1)>\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_indented_html_list_continuation_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n- item\n\n    <img src=x onerror=alert(1)>\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_list_nested_indented_code_active_content_example_passes(self):
        issues = validate_report_content(
            VALID_REPORT + "\n- Example\n\n        <script>alert('xss')</script>\n"
        )

        self.assertEqual(issues, [])

    def test_html_event_handler_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n<img src=x onerror=alert(1)>\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_slash_separated_html_event_handler_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n<img/onerror=alert(1) src=x>\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_html_event_handler_after_quoted_angle_bracket_fails(self):
        issues = validate_report_content(
            VALID_REPORT + '\n<img title=">" src=x onerror=alert(1)>\n'
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_html_event_handler_with_backtick_attributes_fails(self):
        issues = validate_report_content(
            VALID_REPORT + '\n<img title="`" src=x onerror=alert(1) alt="`">\n'
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_html_event_handler_wrapped_in_escaped_backticks_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n\\` <img src=x onerror=alert(1)> \\`\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_html_event_handler_before_longer_backtick_run_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\nText ` <img src=x onerror=alert(1)> ``\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_inline_code_inside_raw_html_block_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n<div>\n`<img src=x onerror=alert(1)>`\n</div>\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_markdown_escaped_html_inside_raw_html_block_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n<div>\n\\<img src=x onerror=alert(1)>\n</div>\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_inline_code_after_void_html_tag_passes(self):
        issues = validate_report_content(
            VALID_REPORT + "\n<img src=x alt=test>\n`javascript:alert(1)`\n"
        )

        self.assertEqual(issues, [])

    def test_svg_event_handler_fails(self):
        issues = validate_report_content(VALID_REPORT + "\n<svg onload=alert(1)>\n")

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_entity_escaped_html_event_handler_example_passes(self):
        issues = validate_report_content(
            VALID_REPORT + "\n&lt;img src=x onerror=alert(1)&gt;\n"
        )

        self.assertEqual(issues, [])

    def test_markdown_escaped_html_event_handler_example_passes(self):
        issues = validate_report_content(
            VALID_REPORT + "\n\\<img src=x onerror=alert(1)\\>\n"
        )

        self.assertEqual(issues, [])

    def test_even_backslash_html_escape_does_not_hide_active_html(self):
        issues = validate_report_content(
            VALID_REPORT + "\n\\\\<img src=x onerror=alert(1)>\n"
        )

        self.assertTrue(any(issue.code == "active_content" for issue in issues))

    def test_markdown_escaped_script_tag_example_passes(self):
        issues = validate_report_content(
            VALID_REPORT + "\n\\<script\\>alert(1)\\</script\\>\n"
        )

        self.assertEqual(issues, [])


if __name__ == "__main__":
    unittest.main()
