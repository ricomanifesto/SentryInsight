import unittest

from src.core.report_validation import validate_report_content

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


class ReportValidationTests(unittest.TestCase):
    def test_valid_report_passes(self):
        self.assertEqual(validate_report_content(VALID_REPORT), [])

    def test_required_source_attribution_without_requirements_fails(self):
        issues = validate_report_content(VALID_REPORT, require_source_attribution=True)

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_missing_required_source_attribution_section_fails(self):
        issues = validate_report_content(
            VALID_REPORT,
            require_source_attribution=True,
            source_attribution_requirements=[["https://example.test/report"]],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_blank_required_source_attribution_section_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n## Source Attribution\n\n",
            require_source_attribution=True,
            source_attribution_requirements=[["https://example.test/report"]],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_source_attribution_heading_mention_does_not_satisfy_requirement(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\nThis report should include ## Source Attribution with https://example.test/report.\n",
            require_source_attribution=True,
            source_attribution_requirements=[["https://example.test/report"]],
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
            source_attribution_requirements=[["https://example.test/report"]],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_placeholder_source_attribution_entry_fails(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n## Source Attribution\n\n- **Article Title**: Source name - URL\n",
            require_source_attribution=True,
            source_attribution_requirements=[["https://example.test/report"]],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_negative_source_attribution_entry_fails(self):
        issues = validate_report_content(
            VALID_REPORT + "\n## Source Attribution\n\n- No sources were provided.\n",
            require_source_attribution=True,
            source_attribution_requirements=[["https://example.test/report"]],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

    def test_source_name_only_fails_when_url_is_required(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n## Source Attribution\n\n- **Example exploitation report**: Example Source\n",
            require_source_attribution=True,
            source_attribution_requirements=[["https://example.test/report"]],
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
            source_attribution_requirements=[
                ["https://example.test/report"],
                ["https://example.test/second"],
            ],
        )
        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )

        self.assertEqual(
            validate_report_content(
                VALID_REPORT_WITH_SOURCE_ATTRIBUTION,
                require_source_attribution=True,
                source_attribution_requirements=[
                    ["https://example.test/report"],
                    ["https://example.test/second"],
                ],
            ),
            [],
        )

    def test_source_only_article_requires_source_and_title(self):
        issues = validate_report_content(
            VALID_REPORT
            + "\n## Source Attribution\n\n- **Different report**: Example Source\n",
            require_source_attribution=True,
            source_attribution_requirements=[
                ["Example Source", "Source-only exploitation report"]
            ],
        )

        self.assertTrue(
            any(issue.code == "missing_source_attribution" for issue in issues)
        )
        self.assertEqual(
            validate_report_content(
                VALID_REPORT_WITH_SOURCE_ATTRIBUTION,
                require_source_attribution=True,
                source_attribution_requirements=[
                    ["Example Source", "Source-only exploitation report"]
                ],
            ),
            [],
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
