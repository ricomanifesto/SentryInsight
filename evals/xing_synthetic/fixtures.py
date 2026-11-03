"""Frozen synthetic inputs and a separate, never-transmitted answer oracle."""

import hashlib
import json
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

from src.core.analyze import analyze_exploitation
from src.core.cve import extract_cve_ids
from src.core.finding_evidence import ABSENT
from src.core.reporting import FINDING_PATTERN, reporting_key
from src.core.reviewed_report import ReviewedReport, resolve_reviewed_analysis
from src.core.source_review import PLAN_KEY, prepare_source_review
from src.core.version_references import build_version_reference_context

from .policy import MODEL, PilotError, TokenBudget, digest, payload_for

ROOT = Path(__file__).parent
SOURCES_SHA = "b2b27add746c41da2a51008495cc1db116e07312563bc4e4d5fc0acbaf304c0b"
ANSWERS_SHA = "10cb0904a5df655424883c5f1b9cbe304c013cfb9f81ec9d0b7afbb7a91f77c2"
CASE_NAMES = (
    "exact-version-boundary",
    "source-qualifiers",
    "product-and-cve-ownership",
    "non-cve-quarantine",
    "status-and-remediation",
    "long-corpus-coverage",
)
PADDING = (
    "Synthetic background describes routine defensive operations without "
    "additional claims.\n"
)


@dataclass(frozen=True)
class PreparedCase:
    name: str
    articles: list[dict]
    expected: dict
    analysis: dict
    payload: dict
    input_tokens_with_reserve: int
    request_sha256: str


def load_fixtures() -> list[dict]:
    sources = (ROOT / "sources.json").read_bytes()
    answers = (ROOT / "answers.json").read_bytes()
    if (
        hashlib.sha256(sources).hexdigest() != SOURCES_SHA
        or hashlib.sha256(answers).hexdigest() != ANSWERS_SHA
    ):
        raise PilotError("fixture_identity")
    source_data, answer_data = json.loads(sources), json.loads(answers)
    if source_data.get("synthetic") is not True:
        raise PilotError("non_synthetic_fixture")
    cases = source_data["cases"]
    if tuple(c["name"] for c in cases) != CASE_NAMES:
        raise PilotError("fixture_plan")
    for case in cases:
        case["expected"] = answer_data["cases"][case["name"]]
        for article in case["articles"]:
            if "padding" in article:
                padding = article.pop("padding")
                text = PADDING * padding["repetitions"]
                original = article["content"]
                # Positions identify the known facts' location in each source.
                article["content"] = {
                    "start": original + "\n\n" + text,
                    "middle": text + "\n\n" + original + "\n\n" + text,
                    "end": text + "\n\n" + original,
                }[padding["position"]]
            for url in [article["link"], *article["source_links"]]:
                parsed = urlsplit(url)
                if (
                    parsed.scheme != "https"
                    or parsed.hostname
                    not in {"example.invalid", "vendor.example.invalid"}
                    or parsed.username
                    or parsed.password
                ):
                    raise PilotError("non_synthetic_url")
    return cases


class CapturePrompt:
    def __init__(self):
        self.messages: list[dict[str, str]] | None = None

    async def generate(
        self, *, system_prompt, user_prompt, model=None, title="Report generation"
    ):
        if (
            model is None
            or model.provider_id != "openrouter"
            or model.model_id != MODEL
        ):
            raise PilotError("model_override")
        if self.messages is not None:
            raise PilotError("duplicate_prompt")
        self.messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        return ""


async def prepare_cases(budget: TokenBudget) -> list[PreparedCase]:
    """Real prompt/preflight, captured locally without constructing a provider."""
    prepared = []
    for case in load_fixtures():
        plan = prepare_source_review(case["articles"])
        states = [r["state"] for r in plan.packet["sources"]]
        if (
            not plan.eligible_keys
            or states.count("review_required") != case["expected"]["held"]
            or states.count("source_rejected") != case["expected"]["rejected"]
        ):
            raise PilotError("fixture_disposition")
        capture = CapturePrompt()
        with tempfile.TemporaryDirectory(prefix="xing-source-plan-") as temp:
            analysis = await analyze_exploitation(
                case["articles"],
                {
                    "analysis": {
                        "model": "openrouter/" + MODEL,
                        "max_tokens": 32_000,
                        "max_input_tokens": 200_000,
                    },
                    "output_path": str(Path(temp) / "unused.md"),
                },
                model_client=capture,
            )
        if (
            analysis.get("error")
            or analysis.get("skipped")
            or capture.messages is None
            or analysis.get(PLAN_KEY) != plan.packet
        ):
            raise PilotError("prompt_preflight")
        payload = payload_for(capture.messages, budget)
        prepared.append(
            PreparedCase(
                case["name"],
                case["articles"],
                case["expected"],
                analysis,
                payload,
                budget.count(capture.messages),
                digest(payload),
            )
        )
    return prepared


def reference_report(case: PreparedCase) -> str:
    """Offline calibration only. Never appended to a model's messages."""
    plan = prepare_source_review(case.articles)
    contracts = build_version_reference_context(plan.eligible_catalog)
    lines = [
        "# Exploitation Report\n\n## Executive Summary\n\n"
        "The supplied synthetic advisories describe the findings below.\n\n"
        "Review each source-specific status before acting.\n\n"
        "## Active Exploitation Details\n"
    ]
    for index, gold in enumerate(case.expected["findings"]):
        keys = [reporting_key(case.articles[i]["link"]) for i in gold["source_indices"]]
        scopes = [
            s
            for s in contracts
            if s["cves"] == sorted(gold["cves"]) and set(keys) & set(s["source_keys"])
        ]
        ids = sorted({c["id"] for s in scopes for c in s["constraints"]})
        value = "; ".join(ids) if ids else ABSENT
        description = {
            "active": "The source reports active exploitation.",
            "not_observed": "The supplied source reports that this vulnerability has not been exploited.",
            "unknown": "Exploitation status is unknown.",
        }[gold["status"]]
        lines.append(
            f"### Synthetic finding {chr(65 + index)}\n"
            f"- **Description**: {description}\n"
            "- **Severity**: unknown\n"
            f"- **Exploitation Status**: {gold['status']}\n"
            "- **Action**: monitor\n"
            + (f"- **CVE IDs**: {', '.join(gold['cves'])}\n" if gold["cves"] else "")
            + f"- **Reporting**: {', '.join(keys)}\n"
            f"- **Affected Versions**: {value}\n"
            f"- **Exceptions**: {gold['exceptions']}\n"
            f"- **Recommended Actions**: {gold['recommended_actions']}\n"
            f"- **Vendor Links**: {gold['vendor_links']}\n"
        )
    for heading in (
        "Affected Systems and Products",
        "Attack Vectors and Techniques",
        "Threat Actor Activities",
    ):
        lines.append(f"## {heading}\n\n{ABSENT}\n")
    return "\n".join(lines)


def normalized(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    value = re.sub(r"^Affected versions:\s*", "", value, flags=re.IGNORECASE)
    return value.removesuffix(".")


def evaluate(case: PreparedCase, report: str) -> tuple[ReviewedReport, dict[str, bool]]:
    reviewed = resolve_reviewed_analysis(
        {**case.analysis, "exploitation_report": report}
    )
    findings = list(FINDING_PATTERN.finditer(reviewed.grounded_report))
    checks = {"finding_coverage": len(findings) == len(case.expected["findings"])}
    seen = set()
    fields_ok = True
    for finding in findings:
        fields = re.findall(r"(?m)^- \*\*([^*]+)\*\*:[ \t]*([^\n]*)", finding["body"])
        if len({key for key, _ in fields}) != len(fields):
            fields_ok = False
            continue
        fields = dict(fields)
        cves = tuple(sorted(extract_cve_ids(fields.get("CVE IDs", ""))))
        keys = {k.strip() for k in fields.get("Reporting", "").split(",")}
        candidates = [
            (i, g)
            for i, g in enumerate(case.expected["findings"])
            if tuple(sorted(g["cves"])) == cves
            and {reporting_key(case.articles[n]["link"]) for n in g["source_indices"]}
            == keys
        ]
        if len(candidates) != 1 or candidates[0][0] in seen:
            fields_ok = False
            continue
        index, gold = candidates[0]
        seen.add(index)
        for label, name in (
            ("Exploitation Status", "status"),
            ("Affected Versions", "affected_versions"),
            ("Exceptions", "exceptions"),
            ("Recommended Actions", "recommended_actions"),
            ("Vendor Links", "vendor_links"),
        ):
            fields_ok &= normalized(fields.get(label, "")) == normalized(gold[name])
    checks["known_answer_fields"] = fields_ok and len(seen) == len(
        case.expected["findings"]
    )
    # Each expected source identity/disposition was checked during preparation;
    # shared resolution checks all generated claims, even those not in the oracle.
    checks["shared_grounding_gate"] = True
    counts = reviewed.coverage["counts"]
    checks["source_coverage"] = (
        counts["input_sources"] == len(case.articles)
        and counts["review_required_sources"] == case.expected["held"]
        and counts["rejected_sources"] == case.expected["rejected"]
        and counts["unrepresented_eligible_sources"] == 0
        and set(seen) == set(range(len(case.expected["findings"])))
    )
    return reviewed, checks
