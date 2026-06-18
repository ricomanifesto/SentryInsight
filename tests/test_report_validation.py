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


class ReportValidationTests(unittest.TestCase):
    def test_valid_report_passes(self):
        self.assertEqual(validate_report_content(VALID_REPORT), [])

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

    def test_missing_required_section_fails(self):
        issues = validate_report_content("# Exploitation Report\n\nSummary only")

        self.assertTrue(any(issue.code == "missing_section" for issue in issues))

    def test_empty_report_fails(self):
        issues = validate_report_content("")

        self.assertEqual(issues[0].code, "empty_report")


if __name__ == "__main__":
    unittest.main()
