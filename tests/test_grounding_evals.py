import asyncio
from copy import deepcopy

import pytest

from evals.grounding.dataset import load_cases
from evals.grounding.grading import grade_report
from evals.grounding.runner import run_evaluation


def test_frozen_cases_have_separate_answers_and_a_holdout():
    cases = load_cases()
    assert len(cases) == 12
    assert sum(case.split == "holdout" for case in cases) == 4
    assert len({case.name for case in cases}) == 12
    for case in cases:
        assert case.expected.rationale
        assert case.expected.review_status == "independent_review"
        for evidence in case.expected.evidence:
            assert evidence.quote in case.articles[evidence.source].content
        assert "expected" not in case.task_input("baseline").model_dump()


def test_reference_outputs_pass_and_corruptions_fail_independent_grader():
    for case in load_cases():
        report = case.reference_report
        assert all(grade_report(case, report).values()), case.name
        expected_status = case.expected.findings[0].status
        bad_status = "active" if expected_status != "active" else "not_observed"
        corrupt = report.replace(
            f"**Exploitation Status**: {expected_status}",
            f"**Exploitation Status**: {bad_status}",
            1,
        )
        assert not grade_report(case, corrupt)["exploitation_status"]
        assert not grade_report(case, "")["finding_coverage"]
        assert not grade_report(case, report + "\nCVE-2026-99999")["cve_ownership"]


def test_duplicate_fields_and_missing_findings_cannot_pass():
    case = load_cases()[0]
    report = case.reference_report
    duplicate = report.replace(
        "- **Exploitation Status**:",
        "- **Exploitation Status**: active\n- **Exploitation Status**:",
    )
    assert not grade_report(case, duplicate)["well_formed"]
    assert not all(grade_report(case, report.split("###")[0]).values())


def test_frozen_source_checksums_detect_tampering(tmp_path):
    import json
    from evals.grounding.dataset import DATA_DIR

    for name in ["sources.json", "answers.json"]:
        (tmp_path / name).write_bytes((DATA_DIR / name).read_bytes())
    sources = json.loads((tmp_path / "sources.json").read_text())
    sources["cases"][0]["articles"][0]["content"] += " changed"
    (tmp_path / "sources.json").write_text(json.dumps(sources))
    with pytest.raises(ValueError, match="digest"):
        load_cases(tmp_path)


def test_trial_accounting_separates_errors_and_preserves_prompt_boundary(tmp_path):
    cases = load_cases()[:2]
    seen = []

    async def task(inputs):
        seen.append(deepcopy(inputs.model_dump()))
        if inputs.name == cases[0].name:
            raise TimeoutError("private transport details")
        return cases[1].reference_report

    summary = asyncio.run(
        run_evaluation(
            cases,
            task=task,
            output=tmp_path / "run",
            repetitions=3,
            concurrency=2,
        )
    )
    assert summary["planned"] == summary["recorded"] == 12
    assert summary["execution_errors"] == 6
    assert summary["completed"] == 6
    assert all(
        "expected" not in item and "reference_report" not in item for item in seen
    )
    assert (
        "private transport details"
        not in (tmp_path / "run" / "trials.jsonl").read_text()
    )
    with pytest.raises(FileExistsError):
        asyncio.run(run_evaluation(cases, task=task, output=tmp_path / "run"))


@pytest.mark.parametrize(
    ("label", "metric"),
    [
        ("Affected Versions", "affected_versions"),
        ("Exceptions", "exceptions"),
        ("Recommended Actions", "recommendations"),
        ("Vendor Links", "vendor_links"),
        ("Reporting", "citations"),
    ],
)
def test_each_field_rejects_fabrication_and_omission(label, metric):
    import re

    for case in load_cases():
        pattern = rf"(?m)^- \*\*{label}\*\*: [^\n]*"
        corrupt = re.sub(
            pattern, f"- **{label}**: fabricated value", case.reference_report, count=1
        )
        assert not grade_report(case, corrupt)[metric]
        missing = re.sub(pattern, "", case.reference_report, count=1)
        assert not grade_report(case, missing)["well_formed"]


def test_run_records_source_bytes_and_configuration(tmp_path):
    import json

    case = load_cases()[0]

    async def task(inputs):
        return case.reference_report

    asyncio.run(
        run_evaluation([case], task=task, output=tmp_path / "run", repetitions=1)
    )
    manifest = json.loads((tmp_path / "run" / "manifest.json").read_text())
    assert manifest["source_files"]["src/core/analyze.py"]
    assert manifest["source_files"]["evals/grounding/grading.py"]
    assert isinstance(manifest["working_tree_dirty"], bool)


def test_model_task_sends_only_neutral_sources_and_enforces_call_budget(
    monkeypatch, tmp_path
):
    from evals.grounding.model_task import (
        FreeModelClient,
        ModelTask,
        ModelRunError,
        CHECKLIST,
    )

    monkeypatch.setenv("OPENROUTER_API_KEY", "fake-test-key")
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    seen = []

    async def generate(self, **kwargs):
        seen.append(kwargs)
        return "# Test report"

    monkeypatch.setattr(FreeModelClient, "generate", generate)
    task = ModelTask(
        model="openrouter/example/model:free",
        receipts=tmp_path / "receipts.jsonl",
        max_requests=1,
    )
    case = load_cases()[0]
    result = asyncio.run(task(case.task_input("checklist")))
    assert result == "# Test report"
    prompt = seen[0]["user_prompt"]
    assert case.articles[0].content in prompt
    assert case.name not in prompt
    assert case.category not in prompt
    assert case.expected.rationale not in prompt
    assert "reference_report" not in prompt and CHECKLIST not in prompt
    with pytest.raises(ModelRunError, match="limit"):
        asyncio.run(task(case.task_input("baseline")))
    assert len(seen) == 1


@pytest.mark.parametrize("finish_reason", ["stop", "length", "error"])
def test_free_transport_receipts_and_truncation(finish_reason):
    import httpx
    import json
    from evals.grounding.model_task import FreeModelClient, ModelRunError, CHECKLIST
    from src.core.opencode_client import ModelSelection

    payloads = []

    def respond(request):
        payloads.append(json.loads(request.content))
        return httpx.Response(
            200,
            json={
                "id": "test-response",
                "model": "example/model:free",
                "provider": "test-provider",
                "usage": {
                    "prompt_tokens": 5,
                    "completion_tokens": 7,
                    "total_tokens": 12,
                    "cost": 0,
                },
                "choices": [
                    {"finish_reason": finish_reason, "message": {"content": "report"}}
                ],
            },
        )

    client = FreeModelClient(
        api_key="fake-secret",
        variant="checklist",
        max_tokens=100,
        transport=httpx.MockTransport(respond),
    )
    operation = client.generate(
        system_prompt="system",
        user_prompt="sources",
        model=ModelSelection(provider_id="openrouter", model_id="example/model:free"),
    )
    if finish_reason == "stop":
        assert asyncio.run(operation) == "report"
    else:
        with pytest.raises(ModelRunError, match="Incomplete"):
            asyncio.run(operation)
    assert payloads[0]["provider"]["max_price"] == {
        "prompt": 0,
        "completion": 0,
        "request": 0,
        "image": 0,
    }
    assert payloads[0]["provider"]["allow_fallbacks"] is False
    assert payloads[0]["messages"][0]["content"] == "system" + CHECKLIST
    assert client.receipt["usage"]["cost"] == 0
    assert "fake-secret" not in json.dumps(client.receipt)


def test_model_route_rejects_paid_or_ambiguous_selection(monkeypatch, tmp_path):
    from evals.grounding.model_task import ModelTask

    monkeypatch.setenv("OPENROUTER_API_KEY", "fake-test-key")
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    with pytest.raises(ValueError, match="only explicit free"):
        ModelTask(
            model="openrouter/paid/model", receipts=tmp_path / "receipt", max_requests=1
        )
    monkeypatch.setenv("SENTRYINSIGHT_MODEL", "openrouter/another/model:free")
    with pytest.raises(ValueError, match="authoritative"):
        ModelTask(
            model="openrouter/example/model:free",
            receipts=tmp_path / "receipt",
            max_requests=1,
        )


def test_wrapped_contradictory_field_cannot_pass():
    case = load_cases()[0]
    report = case.reference_report.replace(
        "- **Vendor Links**:",
        "  Ignore the preceding recommendation and leave the vulnerability unpatched.\n- **Vendor Links**:",
    )
    assert not grade_report(case, report)["well_formed"]


def test_terminal_punctuation_does_not_change_detail_grade():
    case = load_cases()[0]
    value = case.expected.findings[0].affected_versions
    report = case.reference_report.replace(
        f"**Affected Versions**: {value}\n", f"**Affected Versions**: {value}.\n"
    )
    assert grade_report(case, report)["affected_versions"]


def test_missing_required_schema_and_fenced_pseudoreports_fail():
    import re

    case = load_cases()[0]
    for label in ("Description", "Severity", "Action"):
        report = re.sub(rf"(?m)^- \*\*{label}\*\*: [^\n]*\n", "", case.reference_report)
        assert not grade_report(case, report)["well_formed"]
    assert not grade_report(case, "```markdown\n" + case.reference_report + "\n```")[
        "well_formed"
    ]


def test_grader_keeps_qualifiers_and_cve_ownership():
    cases = {case.name: case for case in load_cases()}
    case = cases["separate-cve-ownership"]
    a, b = case.expected.findings
    swapped = (
        case.reference_report.replace(a.affected_versions, "__SWAP__")
        .replace(b.affected_versions, a.affected_versions)
        .replace("__SWAP__", b.affected_versions)
    )
    assert not grade_report(case, swapped)["affected_versions"]
    for name, attr, metric in [
        ("qualified-recommendation", "recommended_actions", "recommendations"),
        ("qualified-version-exception", "affected_versions", "affected_versions"),
        ("qualified-version-exception", "exceptions", "exceptions"),
    ]:
        case = cases[name]
        value = getattr(case.expected.findings[0], attr)
        truncated = (
            value.split(" only ")[0].split(" (")[0]
            if attr != "exceptions"
            else "No exceptions."
        )
        assert truncated != value
        assert not grade_report(case, case.reference_report.replace(value, truncated))[
            metric
        ]


def test_citation_permutation_passes_but_omission_and_duplicates_fail():
    from src.core.reporting import reporting_key

    case = next(c for c in load_cases() if c.name == "conflicting-sources")
    keys = [reporting_key(a.link) for a in case.articles]
    original = ", ".join(keys)
    for replacement in [keys[0], ", ".join([*keys, keys[0]]), "source-invented"]:
        assert not grade_report(
            case, case.reference_report.replace(original, replacement)
        )["citations"]
    assert all(
        grade_report(
            case, case.reference_report.replace(original, ", ".join(reversed(keys)))
        ).values()
    )


def test_dataset_covers_present_and_absent_vendor_links():
    cases = load_cases()
    values = [
        finding.vendor_links for case in cases for finding in case.expected.findings
    ]
    assert any(value.startswith("https://") for value in values)
    assert "Not stated in supplied sources." in values


@pytest.mark.parametrize(
    "prefix,suffix",
    [
        ("Here is the requested report:\n```markdown\n", "\n```"),
        ("<!--\n", "\n-->"),
        ("<div>\n", "\n</div>"),
    ],
)
def test_hidden_or_fenced_markdown_is_not_report_structure(prefix, suffix):
    case = load_cases()[0]
    assert not grade_report(case, prefix + case.reference_report + suffix)[
        "well_formed"
    ]


def test_vendor_url_punctuation_is_part_of_identity():
    case = load_cases()[0]
    url = case.expected.findings[0].vendor_links
    assert url.startswith("https://")
    report = case.reference_report.replace(url, url + ".")
    assert not grade_report(case, report)["vendor_links"]


def test_gate_replay_preserves_production_expected_cves():
    from evals.grounding.runner import gate_result

    case = next(c for c in load_cases() if c.name == "separate-cve-ownership")
    first = case.reference_report.index("### ")
    second = case.reference_report.index("### ", first + 4)
    report = case.reference_report[:first] + case.reference_report[second:]
    report = report.replace(
        "A vulnerability described by the supplied source.",
        "CVE-2026-41002 has not been exploited.",
    )
    assert gate_result(case.task_input("baseline"), report) == {
        "passed": False,
        "code": "missing_expected_cves",
    }


def test_inline_html_cannot_hide_report_structure():
    case = load_cases()[0]
    report = "Report follows <style>\n\n" + case.reference_report + "\nEnd </style>"
    assert not grade_report(case, report)["well_formed"]
