"""The CI interpreter must support verified HTTPS before fetching contracts."""

import importlib.util
from pathlib import Path
from types import SimpleNamespace

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/verify_python_https.py"


def load_preflight():
    spec = importlib.util.spec_from_file_location("https_preflight", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_offline_preflight_constructs_a_verifying_https_handler(monkeypatch, capsys):
    module = load_preflight()
    import socket

    def forbidden(*args, **kwargs):
        pytest.fail("Preflight must not access the network")

    monkeypatch.setattr(socket, "create_connection", forbidden)
    monkeypatch.setattr(socket, "getaddrinfo", forbidden)
    assert module.main() == 0
    assert "HTTPS preflight passed" in capsys.readouterr().out


@pytest.mark.parametrize("exception", [ImportError, OSError])
def test_ssl_import_failure_is_clear_and_does_not_expose_exception_text(
    monkeypatch, capsys, exception
):
    module = load_preflight()

    def unavailable(name):
        raise exception("PRIVATE-LOADER-TEXT")

    monkeypatch.setattr(module.importlib, "import_module", unavailable)
    assert module.main() == 1
    output = capsys.readouterr()
    assert "ssl_import_failed" in output.err
    assert exception.__name__ in output.err
    assert "PRIVATE-LOADER-TEXT" not in output.err + output.out


@pytest.mark.parametrize("failure", ["context", "handler", "verification"])
def test_incomplete_https_runtime_fails_closed(monkeypatch, capsys, failure):
    module = load_preflight()
    context = SimpleNamespace(verify_mode=2, check_hostname=failure != "verification")

    def create_context():
        if failure == "context":
            raise OSError("PRIVATE-TRUST-STORE-TEXT")
        return context

    ssl = SimpleNamespace(CERT_REQUIRED=2, create_default_context=create_context)
    request = SimpleNamespace()
    if failure != "handler":
        request.HTTPSHandler = lambda **kwargs: None
    monkeypatch.setattr(
        module.importlib,
        "import_module",
        lambda name: ssl if name == "ssl" else request,
    )
    assert module.main() == 1
    output = capsys.readouterr()
    expected = {
        "context": "tls_context_failed",
        "handler": "https_handler_missing",
        "verification": "tls_verification_disabled",
    }
    assert expected[failure] in output.err
    assert "PRIVATE" not in output.err + output.out


@pytest.mark.parametrize(
    "workflow_name", ["validate", "generate-report", "publish-production"]
)
def test_noble_jobs_align_host_cache_and_check_https_before_network(workflow_name):
    workflow = (
        SCRIPT.parents[1] / ".github/workflows" / f"{workflow_name}.yml"
    ).read_text()
    assert "runs-on: ubuntu-24.04" in workflow
    assert "python-version: '3.11'" in workflow
    check = workflow.index("python3 scripts/verify_python_https.py")
    assert (
        workflow.index("name: Set up Python")
        < check
        < workflow.index("name: Set up uv")
    )
    if workflow_name != "publish-production":
        assert check < workflow.index(
            "name: Fetch canonical reporting identity verifier"
        )
    assert "continue-on-error" not in workflow
