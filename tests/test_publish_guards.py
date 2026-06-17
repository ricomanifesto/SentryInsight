import asyncio
import tempfile
import unittest
from pathlib import Path

from src.services.publish import publish_to_github_pages


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


class PublishGuardTests(unittest.TestCase):
    def test_invalid_report_is_not_written_to_pages_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_dir = Path(tmpdir) / "docs"
            result = asyncio.run(
                publish_to_github_pages(
                    {
                        "exploitation_report": (
                            "# Error Generating Exploitation Report\n\n"
                            "Error code: 404"
                        ),
                        "date": "2026-06-17",
                    },
                    {"enabled": True, "repo_directory": str(repo_dir)},
                )
            )

            self.assertFalse(result)
            self.assertTrue(repo_dir.exists())
            self.assertFalse((repo_dir / "index.md").exists())

    def test_valid_report_writes_pages_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_dir = Path(tmpdir) / "docs"
            result = asyncio.run(
                publish_to_github_pages(
                    {
                        "exploitation_report": VALID_REPORT,
                        "date": "2026-06-17",
                    },
                    {"enabled": True, "repo_directory": str(repo_dir)},
                )
            )

            self.assertTrue(result)
            self.assertIn(VALID_REPORT, (repo_dir / "index.md").read_text())
            self.assertTrue((repo_dir / "navigation.md").exists())
            self.assertTrue((repo_dir / "_config.yml").exists())


if __name__ == "__main__":
    unittest.main()
