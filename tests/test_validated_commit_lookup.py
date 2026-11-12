"""Offline trust-boundary and failure-retention contracts."""

import copy
import importlib.util
import json
import subprocess
import urllib.error
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "lookup", ROOT / "scripts/find_validated_commit.py"
)
lookup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup)
SHA = "a" * 40
SECRET = "never-print-this-token"
ENV = dict(GITHUB_SHA=SHA, GH_TOKEN=SECRET, GITHUB_REPOSITORY=lookup.REPOSITORY)
REPO = dict(id=lookup.REPOSITORY_ID, full_name=lookup.REPOSITORY)
RUN = dict(
    head_sha=SHA,
    head_branch="main",
    event="push",
    status="completed",
    conclusion="success",
    path=".github/workflows/validate.yml",
    repository=REPO,
    head_repository=REPO,
)


def execute(payload=None, *, body=None, env=None, head=SHA, error=None, status=200):
    response = Mock(status=status)
    response.read.return_value = (
        json.dumps({"workflow_runs": [RUN]} if payload is None else payload).encode()
        if body is None
        else body
    )
    response.__enter__ = Mock(return_value=response)
    response.__exit__ = Mock(return_value=False)
    opener = Mock()
    opener.open.return_value = response
    opener.open.side_effect = error
    with (
        patch.object(lookup.subprocess, "run", return_value=Mock(stdout=head)) as git,
        patch.object(
            lookup.urllib.request, "build_opener", return_value=opener
        ) as build,
    ):
        result = lookup.find_validated_commit(ENV if env is None else env)
    return result, opener, response, git, build


def test_exact_success_and_bounded_request():
    result, opener, response, git, build = execute()
    assert result
    request = opener.open.call_args.args[0]
    assert request.full_url.startswith(
        "https://api.github.com/repos/ricomanifesto/SentryInsight/actions/workflows/validate.yml/runs?"
    )
    assert "head_sha=" + SHA in request.full_url
    assert "per_page=1" in request.full_url
    assert request.get_header("Authorization") == "Bearer " + SECRET
    assert opener.open.call_args.kwargs == {"timeout": 10}
    response.read.assert_called_once_with(lookup.MAX_BYTES + 1)
    assert git.call_args.kwargs["timeout"] == 10
    assert isinstance(build.call_args.args[0], lookup.NoRedirect)


@pytest.mark.parametrize(
    "field,value",
    [
        ("head_sha", "b" * 40),
        ("head_branch", "feature"),
        ("event", "pull_request"),
        ("event", "workflow_dispatch"),
        ("status", "in_progress"),
        ("status", "queued"),
        ("conclusion", "failure"),
        ("conclusion", "skipped"),
        ("conclusion", None),
        ("path", ".github/workflows/other.yml"),
        ("repository", dict(id=9, full_name="someone/fork")),
        ("head_repository", dict(id=9, full_name="someone/fork")),
        ("repository", dict(id=lookup.REPOSITORY_ID, full_name="someone/fork")),
        ("repository", dict(id=str(lookup.REPOSITORY_ID), full_name=lookup.REPOSITORY)),
    ],
)
def test_wrong_run_rejected(field, value):
    run = copy.deepcopy(RUN)
    run[field] = value
    assert not execute({"workflow_runs": [run]})[0]


@pytest.mark.parametrize("field", list(RUN))
def test_missing_run_field_rejected(field):
    run = copy.deepcopy(RUN)
    del run[field]
    assert not execute({"workflow_runs": [run]})[0]


@pytest.mark.parametrize(
    "payload",
    [
        [],
        {},
        "secret",
        1,
        True,
        {"workflow_runs": None},
        {"workflow_runs": {}},
        {"workflow_runs": []},
        {"workflow_runs": [None]},
        {"workflow_runs": ["secret"]},
        {"workflow_runs": [RUN, RUN]},
        {"total_count": 100},
    ],
)
def test_malformed_schema_rejected(payload):
    assert not execute(payload)[0]


@pytest.mark.parametrize(
    "body", [b"bad json", b"\xff", b"null", b"x" * (lookup.MAX_BYTES + 1)]
)
def test_malformed_or_oversized_body(body):
    assert not execute(body=body)[0]


@pytest.mark.parametrize(
    "error",
    [
        TimeoutError(SECRET),
        urllib.error.URLError(SECRET),
        OSError(SECRET),
        urllib.error.HTTPError(
            "https://example.invalid/" + SECRET, 401, SECRET, {}, None
        ),
        urllib.error.HTTPError(
            "https://example.invalid/" + SECRET, 403, SECRET, {}, None
        ),
    ],
)
def test_errors_fail_closed_without_secret(error, capsys):
    assert not execute(error=error)[0]
    output = capsys.readouterr()
    assert SECRET not in output.out + output.err
    assert "full local validation" in output.out


@pytest.mark.parametrize("status", [201, 301, 302, 307, 308, 401, 403, 500])
def test_non_success_status(status):
    assert not execute(status=status)[0]


@pytest.mark.parametrize(
    "field,value",
    [
        ("GH_TOKEN", ""),
        ("GH_TOKEN", "  "),
        ("GITHUB_SHA", ""),
        ("GITHUB_SHA", "not-a-sha"),
        ("GITHUB_REPOSITORY", "someone/fork"),
    ],
)
def test_missing_or_bad_input_does_not_request(field, value):
    env = dict(ENV, **{field: value})
    result, opener, _, git, _ = execute(env=env)
    assert not result
    opener.open.assert_not_called()
    git.assert_not_called()


def test_checkout_mismatch_does_not_request():
    result, opener, *_ = execute(head="b" * 40)
    assert not result
    opener.open.assert_not_called()


@pytest.mark.parametrize(
    "error",
    [
        subprocess.TimeoutExpired("git", 10),
        subprocess.CalledProcessError(1, "git", output=SECRET),
    ],
)
def test_git_failure(error, capsys):
    with patch.object(lookup.subprocess, "run", side_effect=error):
        assert not lookup.find_validated_commit(ENV)
    assert SECRET not in capsys.readouterr().out


@pytest.mark.parametrize("code", [301, 302, 303, 307, 308])
def test_redirects_never_forward_authorization(code):
    request = lookup.urllib.request.Request(
        "https://api.github.com/", headers={"Authorization": SECRET}
    )
    assert (
        lookup.NoRedirect().redirect_request(
            request, None, code, "", {}, "https://attacker.invalid/"
        )
        is None
    )


@pytest.mark.parametrize("passed", [True, False])
def test_output_contract(passed, tmp_path, monkeypatch, capsys):
    output = tmp_path / "output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    with patch.object(lookup, "find_validated_commit", return_value=passed):
        lookup.main()
    assert output.read_text() == f"passed={str(passed).lower()}\n"
    assert SECRET not in capsys.readouterr().out


def test_failure_evidence_workflow_contract():
    for name, validation in [
        ("generate-report.yml", "Run local validation"),
        ("validate.yml", "Run validation"),
    ]:
        content = (ROOT / ".github/workflows" / name).read_text()
        assert f"- name: {validation}\n        id: local-validation" in content
        block = content.split("- name: Retain failed validation browser diagnostics\n")[
            1
        ].split("\n      - name:")[0]
        assert "if: always() && steps.local-validation.outcome == 'failure'" in block
        assert "path: test-results/playwright\n" in block
        assert "retention-days: 7\n" in block
        assert "if-no-files-found: ignore" in block
        assert "${{ github.run_id }}-${{ github.run_attempt }}" in block
        assert content.index(
            "Retain failed validation browser diagnostics"
        ) > content.index(f"- name: {validation}")
    generate = (ROOT / ".github/workflows/generate-report.yml").read_text()
    assert "run: python3 -B scripts/find_validated_commit.py" in generate
    assert "GH_TOKEN: ${{ secrets.PAT_GITHUB }}" in generate
    assert "if: steps.validated.outputs.passed != 'true'" in generate
    assert "if: steps.validated.outputs.passed == 'true'" in generate
    config = (ROOT / "playwright.config.js").read_text()
    assert 'trace: "retain-on-failure"' in config
    assert 'screenshot: "only-on-failure"' in config
    assert "retries:" not in config


@pytest.mark.parametrize(
    "value",
    [None, [], "secret", 1, True, {}, {"id": True}, {"full_name": lookup.REPOSITORY}],
)
@pytest.mark.parametrize("field", ["repository", "head_repository"])
def test_malformed_repository_rejected(field, value):
    run = copy.deepcopy(RUN)
    run[field] = value
    assert not execute({"workflow_runs": [run]})[0]


@pytest.mark.parametrize("code", [301, 302, 303, 307, 308])
def test_redirect_response_is_an_error_without_followup(code):
    opener = lookup.urllib.request.build_opener(lookup.NoRedirect())
    opener.open = Mock()
    request = lookup.urllib.request.Request(
        "https://api.github.com/", headers={"Authorization": SECRET}
    )
    with pytest.raises(urllib.error.HTTPError):
        opener.error(
            "http",
            request,
            Mock(),
            code,
            "redirect",
            {"location": "https://attacker.invalid/"},
        )
    opener.open.assert_not_called()
