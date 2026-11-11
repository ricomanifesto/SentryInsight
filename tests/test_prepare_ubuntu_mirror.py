"""Offline coverage: no DNS, network requests or host APT writes."""

from pathlib import Path
import subprocess
from unittest.mock import Mock

import pytest

from scripts import prepare_ubuntu_mirror as mirror


@pytest.fixture
def apt(tmp_path, monkeypatch):
    (tmp_path / "sources.list.d").mkdir()
    monkeypatch.setattr(mirror, "azure_resolves", lambda: False)
    monkeypatch.setattr(mirror, "archive_reachable", lambda: True)
    return tmp_path


def test_healthy_azure_leaves_sources_byte_identical(apt, monkeypatch):
    source = apt / "sources.list"
    source.write_text("deb http://azure.archive.ubuntu.com/ubuntu noble main\n")
    original = source.read_bytes()
    monkeypatch.setattr(mirror, "azure_resolves", lambda: True)
    probe = Mock(side_effect=AssertionError("fallback must not be probed"))
    monkeypatch.setattr(mirror, "archive_reachable", probe)
    mirror.prepare(apt)
    assert source.read_bytes() == original
    probe.assert_not_called()


def test_fallback_preserves_legacy_options_comments_and_other_sources(apt):
    source = apt / "sources.list"
    original = (
        "# deb http://azure.archive.ubuntu.com/ubuntu noble main\n"
        "deb [arch=amd64 signed-by=/usr/share/keyrings/ubuntu-archive-keyring.gpg] "
        "http://azure.archive.ubuntu.com/ubuntu/ noble main restricted\n"
        "deb-src https://azure.archive.ubuntu.com/ubuntu noble-updates main\n"
        "deb http://security.ubuntu.com/ubuntu noble-security main\n"
        "deb https://packages.example.org/stable noble main\n"
    )
    source.write_text(original)
    mirror.prepare(apt)
    expected = original.splitlines(keepends=True)
    expected[1] = (
        expected[1].replace(mirror.AZURE, mirror.ARCHIVE).replace("http://", "https://")
    )
    expected[2] = expected[2].replace(mirror.AZURE, mirror.ARCHIVE)
    assert source.read_text() == "".join(expected)


def test_fallback_deb822_preserves_signing_and_disabled_stanzas(apt):
    source = apt / "sources.list.d" / "ubuntu.sources"
    active = (
        "Types: deb deb-src\n"
        "URIs: http://azure.archive.ubuntu.com/ubuntu/\n"
        " https://azure.archive.ubuntu.com/ubuntu https://example.org/ubuntu\n"
        "Suites: noble noble-updates noble-backports\n"
        "Components: main restricted universe multiverse\n"
        "Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg\n"
    )
    disabled = "\n" + active + "Enabled: no\n"
    source.write_text(active + disabled)
    mirror.prepare(apt)
    assert (
        source.read_text()
        == active.replace(mirror.AZURE, mirror.ARCHIVE).replace("http://", "https://")
        + disabled
    )


@pytest.mark.parametrize(
    "contents",
    [
        "",
        "# deb http://azure.archive.ubuntu.com/ubuntu noble main\n",
        "deb https://other.example.org/ubuntu noble main\n",
        "unrecognized http://azure.archive.ubuntu.com/ubuntu noble main\n",
    ],
)
def test_non_azure_config_is_left_to_original_installer(apt, contents):
    source = apt / "sources.list"
    source.write_text(contents)
    mirror.prepare(apt)
    assert source.read_text() == contents


def test_missing_source_files_are_left_to_original_installer(apt):
    mirror.prepare(apt)


def test_unreachable_fallback_does_not_modify_sources(apt, monkeypatch):
    source = apt / "sources.list"
    original = "deb http://azure.archive.ubuntu.com/ubuntu noble main\n"
    source.write_text(original)
    monkeypatch.setattr(mirror, "archive_reachable", lambda: False)
    with pytest.raises(ValueError, match="official Ubuntu archive is unreachable"):
        mirror.prepare(apt)
    assert source.read_text() == original


def test_all_sources_validated_before_any_write(apt):
    source = apt / "sources.list"
    original = "deb http://azure.archive.ubuntu.com/ubuntu noble main\n"
    source.write_text(original)
    (apt / "sources.list.d" / "bad.list").write_text(
        "deb http://azure.archive.ubuntu.com/custom noble main\n"
    )
    with pytest.raises(ValueError, match="Unsupported"):
        mirror.prepare(apt)
    assert source.read_text() == original


@pytest.mark.parametrize("failure", ["exit", "timeout", "empty"])
def test_dns_probe_has_two_bounded_attempts(monkeypatch, failure):
    result = subprocess.CompletedProcess([], 2 if failure == "exit" else 0, b"")
    probe = Mock(
        side_effect=(
            subprocess.TimeoutExpired("getent", 5) if failure == "timeout" else None
        ),
        return_value=result,
    )
    monkeypatch.setattr(mirror.subprocess, "run", probe)
    assert not mirror.azure_resolves()
    assert probe.call_count == 2
    for call in probe.call_args_list:
        assert call.args[0] == ["getent", "ahosts", mirror.AZURE]
        assert call.kwargs["timeout"] == 5


def test_dns_probe_recovers_on_second_attempt(monkeypatch):
    probe = Mock(
        side_effect=[
            subprocess.CompletedProcess([], 2, b""),
            subprocess.CompletedProcess([], 0, b"1.2.3.4 STREAM archive\n"),
        ]
    )
    monkeypatch.setattr(mirror.subprocess, "run", probe)
    assert mirror.azure_resolves()
    assert probe.call_count == 2


@pytest.mark.parametrize("outcome", [0, 22, 28, "timeout"])
def test_fallback_probe_is_bounded_and_uses_official_https(monkeypatch, outcome):
    probe = Mock(
        side_effect=(
            subprocess.TimeoutExpired("curl", 20) if outcome == "timeout" else None
        ),
        return_value=subprocess.CompletedProcess([], outcome),
    )
    monkeypatch.setattr(mirror.subprocess, "run", probe)
    assert mirror.archive_reachable() is (outcome == 0)
    probe.assert_called_once()
    args = probe.call_args.args[0]
    assert args[-1] == "https://archive.ubuntu.com/ubuntu/"
    assert args[args.index("--retry") + 1] == "0"
    assert args[args.index("--max-time") + 1] == "15"
    assert probe.call_args.kwargs["timeout"] == 20


def test_main_reports_failure(monkeypatch, capsys):
    monkeypatch.setattr(mirror, "prepare", Mock(side_effect=ValueError("unreachable")))
    assert mirror.main() == 1
    assert "Ubuntu mirror preflight failed: unreachable" in capsys.readouterr().err


@pytest.mark.parametrize(
    "workflow", ["validate", "generate-report", "publish-production"]
)
def test_every_browser_install_keeps_dependency_gate_with_preflight(workflow):
    root = Path(__file__).resolve().parents[1]
    text = (root / ".github" / "workflows" / f"{workflow}.yml").read_text()
    assert text.count("npx playwright install --with-deps chromium") == 1
    assert (
        "sudo python3 scripts/prepare_ubuntu_mirror.py\n"
        "          npx playwright install --with-deps chromium"
    ) in text
    assert "bash scripts/local_validation.sh" in text


@pytest.mark.parametrize("suffix", [".list", ".sources"])
def test_actual_runner_mirror_list_fallback_preserves_priorities(apt, suffix):
    # Exact runner-image mirror entries from configure-apt-sources.sh.
    reference = "mirror+file:/etc/apt/apt-mirrors.txt"
    source = apt / "sources.list.d" / f"ubuntu{suffix}"
    config = (
        f"deb [signed-by=/usr/share/keyrings/ubuntu-archive-keyring.gpg] "
        f"{reference} noble main\n"
        if suffix == ".list"
        else f"Types: deb\nURIs: {reference}\nSuites: noble noble-updates\n"
        "Components: main restricted universe multiverse\n"
        "Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg\n"
    )
    source.write_text(config)
    mirrors = apt / "apt-mirrors.txt"
    original = (
        "# http://azure.archive.ubuntu.com/ubuntu/ is Azure\n"
        "http://azure.archive.ubuntu.com/ubuntu/\tpriority:1\n"
        "https://archive.ubuntu.com/ubuntu/\tpriority:2\n"
        "https://security.ubuntu.com/ubuntu/\tpriority:3\n"
    )
    mirrors.write_text(original)
    mirror.prepare(apt)
    assert source.read_text() == config
    assert mirrors.read_text() == original.replace(
        "http://azure.archive.ubuntu.com/ubuntu/\tpriority:1",
        "https://archive.ubuntu.com/ubuntu/\tpriority:1",
    )


@pytest.mark.parametrize("disabled", [False, True])
def test_unreferenced_or_disabled_mirror_list_is_not_rewritten(apt, disabled):
    source = apt / "sources.list.d" / "ubuntu.sources"
    source.write_text(
        "Types: deb\nURIs: mirror+file:/etc/apt/apt-mirrors.txt\nEnabled: no\n"
        if disabled
        else "Types: deb\nURIs: https://other.example.org/ubuntu\n"
    )
    mirrors = apt / "apt-mirrors.txt"
    original = "http://azure.archive.ubuntu.com/ubuntu/\tpriority:1\n"
    mirrors.write_text(original)
    mirror.prepare(apt)
    assert mirrors.read_text() == original


def test_missing_active_mirror_list_fails_before_any_write(apt):
    source = apt / "sources.list"
    original = (
        "deb http://azure.archive.ubuntu.com/ubuntu noble main\n"
        "deb mirror+file:/etc/apt/apt-mirrors.txt noble-updates main\n"
    )
    source.write_text(original)
    with pytest.raises(FileNotFoundError):
        mirror.prepare(apt)
    assert source.read_text() == original


@pytest.mark.parametrize(
    "uri",
    [
        "http://azure.archive.ubuntu.com/not-ubuntu",
        "http://azure.archive.ubuntu.com.evil/ubuntu",
    ],
)
def test_unsupported_active_azure_uri_fails_closed(apt, uri):
    source = apt / "sources.list"
    original = f"deb {uri} noble main\n"
    source.write_text(original)
    with pytest.raises(ValueError, match="Unsupported Azure archive URI"):
        mirror.prepare(apt)
    assert source.read_text() == original


@pytest.mark.parametrize("use_mirror_list", [False, True])
def test_repeated_fallback_is_idempotent(apt, monkeypatch, use_mirror_list):
    source = apt / "sources.list"
    if use_mirror_list:
        source.write_text("deb mirror+file:/etc/apt/apt-mirrors.txt noble main\n")
        target = apt / "apt-mirrors.txt"
        target.write_text("http://azure.archive.ubuntu.com/ubuntu/\tpriority:1\n")
    else:
        target = source
        source.write_text("deb http://azure.archive.ubuntu.com/ubuntu noble main\n")
    mirror.prepare(apt)
    first = target.read_bytes()
    monkeypatch.setattr(mirror, "archive_reachable", Mock(side_effect=AssertionError))
    mirror.prepare(apt)
    assert target.read_bytes() == first


def test_existing_official_archive_ignores_azure_dns_outage(apt, monkeypatch):
    source = apt / "sources.list"
    original = "deb https://archive.ubuntu.com/ubuntu noble main\n"
    source.write_text(original)
    monkeypatch.setattr(mirror, "archive_reachable", Mock(side_effect=AssertionError))
    mirror.prepare(apt)
    assert source.read_text() == original
