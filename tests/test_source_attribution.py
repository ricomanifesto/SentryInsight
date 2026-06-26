import unittest

from src.core.source_attribution import (
    collect_source_attribution_entries,
)


class SourceAttributionTests(unittest.TestCase):
    def test_unknown_source_sentinel_does_not_require_attribution(self):
        self.assertEqual(
            collect_source_attribution_entries(
                [
                    {
                        "title": "Metadata-light report",
                        "source": "Unknown Source",
                        "summary": "Summary only",
                    }
                ]
            ),
            [],
        )

    def test_unknown_source_sentinel_does_not_replace_real_url_attribution(self):
        self.assertEqual(
            collect_source_attribution_entries(
                [
                    {
                        "title": "URL-backed report",
                        "source": "Unknown Source",
                        "link": "https://example.test/report",
                        "summary": "Summary only",
                    }
                ]
            ),
            ["- **URL-backed report**: https://example.test/report"],
        )

    def test_source_attribution_entries_collapse_metadata_whitespace(self):
        self.assertEqual(
            collect_source_attribution_entries(
                [
                    {
                        "title": "Multiline\n exploitation\t report",
                        "source": "Example\n Research\tTeam",
                        "link": "https://example.test/\n report",
                    }
                ]
            ),
            [
                "- **Multiline exploitation report**: "
                "Example Research Team - https://example.test/report"
            ],
        )

    def test_source_attribution_entries_deduplicate_canonical_rows(self):
        self.assertEqual(
            collect_source_attribution_entries(
                [
                    {
                        "title": "First report",
                        "source": "Example Source",
                        "link": "https://example.test/first",
                    },
                    {
                        "title": "First report",
                        "source": "Example Source",
                        "link": "https://example.test/first",
                    },
                    {
                        "title": "Second report",
                        "source": "Example Source",
                        "link": "https://example.test/second",
                    },
                ]
            ),
            [
                "- **First report**: Example Source - https://example.test/first",
                "- **Second report**: Example Source - https://example.test/second",
            ],
        )

    def test_source_attribution_entries_escape_markdown_text_metadata(self):
        self.assertEqual(
            collect_source_attribution_entries(
                [
                    {
                        "title": r"Critical **edge** [gateway] _update_ \ <em>`advisory`</em> & ~~notes~~",
                        "source": r"Vendor **Research** [Team] _analysis_ \ <desk>`notes`</desk> & ~~feed~~",
                        "link": "https://example.test/report(1)",
                    }
                ]
            ),
            [
                r"- **Critical \*\*edge\*\* \[gateway\] \_update\_ \\ "
                r"\<em\>\`advisory\`\</em\> \& \~\~notes\~\~**: "
                r"Vendor \*\*Research\*\* \[Team\] \_analysis\_ \\ "
                r"\<desk\>\`notes\`\</desk\> \& \~\~feed\~\~ - "
                "https://example.test/report(1)"
            ],
        )


if __name__ == "__main__":
    unittest.main()
