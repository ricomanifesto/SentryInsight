"""Source inputs and separately maintained answer keys."""

import hashlib
import json
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from src.core.reporting import reporting_key

DATA_DIR = Path(__file__).parent / "data"
ABSENT = "Not stated in supplied sources."


def digest(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


class Record(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class Article(Record):
    title: str
    source: str
    link: str
    content: str
    content_kind: Literal["article"]
    source_links: list[str]


class Evidence(Record):
    source: int = Field(ge=0)
    quote: str = Field(min_length=1)


class ExpectedFinding(Record):
    cve: str = Field(pattern=r"^CVE-\d{4}-\d{4,}$")
    status: Literal["active", "observed", "potential", "not_observed", "unknown"]
    affected_versions: str
    exceptions: str
    recommended_actions: str
    vendor_links: str
    source_indices: list[int] = Field(min_length=1)


class AnswerKey(Record):
    source_sha256: str
    review_status: Literal["provisional", "independent_review", "human_review"]
    rationale: str = Field(min_length=1)
    evidence: list[Evidence] = Field(min_length=1)
    findings: list[ExpectedFinding] = Field(min_length=1)


class TaskInput(Record):
    name: str
    articles: list[Article]
    variant: Literal["baseline", "checklist"]
    repetition: int = 1


class SourceCase(Record):
    name: str = Field(pattern=r"^[a-z][a-z0-9-]+$")
    split: Literal["development", "holdout"]
    category: str
    articles: list[Article] = Field(min_length=1)
    expected: AnswerKey

    def task_input(self, variant, repetition=1) -> TaskInput:
        return TaskInput(
            name=self.name,
            articles=[article.model_copy(deep=True) for article in self.articles],
            variant=variant,
            repetition=repetition,
        )

    @property
    def reference_report(self) -> str:
        """Calibration fixture, not a model output or independent quality result."""
        blocks = [
            "# Exploitation Report\n\n## Executive Summary\n\n"
            "The supplied advisories describe the findings below.\n\n"
            "Review the source-specific status and details before acting.\n\n"
            "## Active Exploitation Details\n"
        ]
        for finding in self.expected.findings:
            keys = ", ".join(
                reporting_key(self.articles[index].link)
                for index in finding.source_indices
            )
            blocks.append(
                f"### Example vulnerability ({finding.cve})\n"
                "- **Description**: A vulnerability described by the supplied source.\n"
                "- **Severity**: unknown\n"
                f"- **Exploitation Status**: {finding.status}\n"
                "- **Action**: monitor\n"
                f"- **CVE IDs**: {finding.cve}\n"
                f"- **Reporting**: {keys}\n"
                f"- **Affected Versions**: {finding.affected_versions}\n"
                f"- **Exceptions**: {finding.exceptions}\n"
                f"- **Recommended Actions**: {finding.recommended_actions}\n"
                f"- **Vendor Links**: {finding.vendor_links}\n"
            )
        blocks.extend(
            f"## {title}\n\n{ABSENT}\n"
            for title in (
                "Affected Systems and Products",
                "Attack Vectors and Techniques",
                "Threat Actor Activities",
            )
        )
        return "\n".join(blocks)


def load_cases(directory: Path = DATA_DIR) -> list[SourceCase]:
    sources = json.loads((directory / "sources.json").read_text())
    answers = json.loads((directory / "answers.json").read_text())
    if sources["version"] != 1 or answers["version"] != 1:
        raise ValueError("Unsupported dataset version")
    cases = []
    names = [item["name"] for item in sources["cases"]]
    if len(set(names)) != len(names) or set(names) != set(answers["cases"]):
        raise ValueError("Duplicate or unmatched case identities")
    for item in sources["cases"]:
        case = SourceCase(**item, expected=answers["cases"][item["name"]])
        if digest(item["articles"]) != case.expected.source_sha256:
            raise ValueError(f"Source digest mismatch: {case.name}")
        for evidence in case.expected.evidence:
            if evidence.source >= len(case.articles) or evidence.quote not in (
                case.articles[evidence.source].content
            ):
                raise ValueError(f"Missing evidence span: {case.name}")
        cves = [finding.cve for finding in case.expected.findings]
        if len(set(cves)) != len(cves):
            raise ValueError(f"Duplicate expected finding: {case.name}")
        for finding in case.expected.findings:
            indices = finding.source_indices
            if len(set(indices)) != len(indices) or any(
                i < 0 or i >= len(case.articles) for i in indices
            ):
                raise ValueError(f"Invalid expected source identity: {case.name}")
        cases.append(case)
    if not cases:
        raise ValueError("Empty dataset")
    return cases
