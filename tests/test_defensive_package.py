"""The shared defensive packager: synthetic git repositories only.

Every fact, product and link is fictional (example.test). Legacy decoys are
committed and then made unreadable on disk, so any read of them would fail.
No case uses a network, credential, provider, report or archive.
"""

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

import pytest

from scripts import package_defensive
from src.core import defensive_package as package
from src.core import paid_readiness as readiness

ROOT = Path(__file__).resolve().parents[1]
COMMIT = "0123456789abcdef0123456789abcdef01234567"
DECOY = "LEGACYDECOYMARKER"
COMMITTED_AT = "2026-11-21T09:30:00Z"
GIT_ENV = {
    "PATH": os.environ["PATH"],
    "HOME": os.environ.get("HOME", "/tmp"),
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_AUTHOR_NAME": "Synthetic",
    "GIT_AUTHOR_EMAIL": "synthetic@example.test",
    "GIT_COMMITTER_NAME": "Synthetic",
    "GIT_COMMITTER_EMAIL": "synthetic@example.test",
    "GIT_AUTHOR_DATE": COMMITTED_AT,
    "GIT_COMMITTER_DATE": COMMITTED_AT,
}


@pytest.fixture(autouse=True)
def synthetic_provider(monkeypatch):
    """Inert control: a fictional provider beside the production allowlist."""
    providers = dict(readiness.PROVIDERS)
    providers["synthetic"] = ("code.example.test", "/{repository}/commit/{commit}")
    monkeypatch.setattr(readiness, "PROVIDERS", providers)


def facts(severity="critical"):
    return readiness.canonical_bytes(
        {
            "schema": readiness.MANIFEST_SCHEMA,
            "approval": {"reviewed_by": "owner-review", "state": "approved"},
            "advisories": [
                {
                    "cve": "CVE-2026-0201",
                    "product": "Gateway Alpha",
                    "severity": "high",
                    "exposure": "unknown",
                    "remediation": "patch",
                    "references": [
                        {
                            "provider": "synthetic",
                            "repository": "vendor/alpha",
                            "commit": COMMIT,
                        }
                    ],
                },
                {
                    "cve": "CVE-2026-0202",
                    "product": "Gateway Bravo",
                    "severity": severity,
                    "exposure": "active",
                    "remediation": "mitigate",
                    "references": [
                        {
                            "provider": "synthetic",
                            "repository": "vendor/bravo",
                            "commit": COMMIT,
                        }
                    ],
                },
            ],
        }
    )


def git(repo, *arguments):
    return subprocess.run(
        ["git", *arguments],
        cwd=repo,
        env=GIT_ENV,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def commit(repo, files, message="synthetic"):
    for relative, data in files.items():
        target = repo / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            target.chmod(0o644)
        target.write_bytes(data)
    # Named paths only: the unreadable decoys are never staged again.
    git(repo, "add", "--", *files)
    git(repo, "commit", "--quiet", "-m", message)
    return git(repo, "rev-parse", "HEAD")


@pytest.fixture
def repo(tmp_path):
    repo = tmp_path / "source"
    repo.mkdir()
    git(repo, "init", "--quiet", "--initial-branch=main")
    inputs = {
        path: (ROOT / path).read_bytes()
        for path in package.pinned_inputs()
        if path != readiness.MANIFEST_PATH
    }
    decoys = {
        "index.md": f"# {DECOY}\n".encode(),
        "index.html": f"<p>{DECOY}</p>\n".encode(),
        "reports/2026-01-01.md": f"# {DECOY}\n".encode(),
        "reports/2026-01-01.html": f"<p>{DECOY}</p>\n".encode(),
    }
    revision = commit(repo, {**inputs, **decoys, readiness.MANIFEST_PATH: facts()})
    for name in decoys:
        (repo / name).chmod(0)
    yield repo, revision
    for name in decoys:
        if (repo / name).exists():
            (repo / name).chmod(0o644)


def out(tmp_path, name="package"):
    (tmp_path / "out").mkdir(exist_ok=True)
    return tmp_path / "out" / name


def node_digest(directory):
    script = (
        "const c=require('./publication/kit/canonical');"
        "console.log(c.inventoryDigest(c.inventoryOfDir(process.argv[1])))"
    )
    return subprocess.check_output(
        ["node", "-e", script, str(directory)], cwd=ROOT, text=True
    ).strip()


def test_local_build_proposes_the_triple_deterministically_and_matches_node(
    repo, tmp_path
):
    source, revision = repo
    first = package.build_package(
        source=source, revision=revision, output=out(tmp_path, "a")
    )
    second = package.build_package(
        source=source, revision=revision, output=out(tmp_path, "b")
    )
    assert first == second
    assert first.head == revision
    assert first.facts_sha256 == hashlib.sha256(facts()).hexdigest()
    assert first.generated_at == COMMITTED_AT
    assert node_digest(out(tmp_path, "a")) == first.package_sha256
    assert first.proposal()["schema"] == package.APPROVAL_SCHEMA


def test_legacy_decoys_are_never_read_or_included(repo, tmp_path):
    source, revision = repo
    output = out(tmp_path)
    package.build_package(source=source, revision=revision, output=output)
    files = [path for path in output.rglob("*") if path.is_file()]
    assert all(DECOY.encode() not in path.read_bytes() for path in files)
    assert {path.name for path in (output / "reports").iterdir()} <= {
        "index.html",
        "index.json",
    }
    assert "render_mode: reviewed_facts" in (output / "index.md").read_text()
    assert "sentrydigest" not in (output / "index.html").read_text().casefold()


@pytest.mark.parametrize(
    ("field", "code"),
    [
        ("head", "approval_head_mismatch"),
        ("facts_sha256", "approval_facts_mismatch"),
        ("package_sha256", "approval_package_mismatch"),
    ],
)
def test_any_approval_drift_refuses_before_output_and_keeps_prior_package(
    repo, tmp_path, field, code
):
    source, revision = repo
    proposal = package.build_package(
        source=source, revision=revision, output=out(tmp_path, "proposal")
    )
    prior = out(tmp_path, "prior")
    shutil.copytree(out(tmp_path, "proposal"), prior)
    prior_digest = package.inventory_digest(prior)[0]
    values = {
        "head": revision,
        "facts_sha256": proposal.facts_sha256,
        "package_sha256": proposal.package_sha256,
    }
    values[field] = "d" * 40 if field == "head" else "e" * 64
    with pytest.raises(package.DefensivePackageError) as caught:
        package.build_package(
            source=source,
            revision=revision,
            output=out(tmp_path, "approved"),
            approval=package.Approval(**values),
        )
    assert str(caught.value) == code
    assert not out(tmp_path, "approved").exists()
    assert package.inventory_digest(prior)[0] == prior_digest
    approved = package.build_package(
        source=source,
        revision=revision,
        output=out(tmp_path, "approved"),
        approval=package.Approval(
            revision, proposal.facts_sha256, proposal.package_sha256
        ),
    )
    assert approved.package_sha256 == proposal.package_sha256


def test_changed_facts_at_a_new_head_refuse_the_old_approval(repo, tmp_path):
    source, revision = repo
    old = package.build_package(source=source, revision=revision, output=out(tmp_path))
    changed = commit(source, {readiness.MANIFEST_PATH: facts(severity="low")})
    with pytest.raises(package.DefensivePackageError) as caught:
        package.build_package(
            source=source,
            revision=changed,
            output=out(tmp_path, "new"),
            approval=package.Approval(changed, old.facts_sha256, old.package_sha256),
        )
    assert str(caught.value) == "approval_facts_mismatch"


@pytest.mark.parametrize(
    ("facts_bytes", "code"),
    [
        (None, "facts_unavailable"),
        (b'{"schema": "x"}', "facts_invalid"),
        (json.dumps(json.loads(facts())).encode(), "facts_invalid"),
    ],
    ids=["missing", "malformed", "noncanonical"],
)
def test_missing_malformed_or_noncanonical_facts_refuse(
    repo, tmp_path, facts_bytes, code
):
    source, _ = repo
    if facts_bytes is None:
        git(source, "rm", "--quiet", readiness.MANIFEST_PATH)
        git(source, "commit", "--quiet", "-m", "drop facts")
        revision = git(source, "rev-parse", "HEAD")
    else:
        revision = commit(source, {readiness.MANIFEST_PATH: facts_bytes})
    with pytest.raises(package.DefensivePackageError) as caught:
        package.build_package(source=source, revision=revision, output=out(tmp_path))
    assert str(caught.value) == code
    assert not out(tmp_path).exists()


def test_a_symlinked_pinned_input_refuses(repo, tmp_path):
    source, _ = repo
    (source / "site" / "report.html").unlink()
    (source / "site" / "report.html").symlink_to("archive.html")
    git(source, "add", "--", "site/report.html")
    git(source, "commit", "--quiet", "-m", "symlink")
    revision = git(source, "rev-parse", "HEAD")
    with pytest.raises(package.DefensivePackageError) as caught:
        package.build_package(source=source, revision=revision, output=out(tmp_path))
    assert str(caught.value) == "pinned_input_symlink"


def _tamper_byte(root):
    with (root / "index.html").open("ab") as stream:
        stream.write(b"<!-- x -->")


def _tamper_extra(root):
    (root / "reports" / "2026-01-01.html").write_text("<p>extra</p>")


def _tamper_path(root):
    (root / "sitemap.xml").rename(root / "sitemap2.xml")


def _tamper_symlink(root):
    (root / "index.html").unlink()
    (root / "index.html").symlink_to("index.md")


@pytest.mark.parametrize(
    "tamper",
    [_tamper_byte, _tamper_extra, _tamper_path, _tamper_symlink],
    ids=["byte", "extra-file", "path", "symlink"],
)
def test_package_tampered_before_upload_fails_verification(repo, tmp_path, tamper):
    source, revision = repo
    output = out(tmp_path)
    built = package.build_package(source=source, revision=revision, output=output)
    assert package.verify_package(output, built.package_sha256) == built.package_sha256
    tamper(output)
    with pytest.raises(package.DefensivePackageError):
        package.verify_package(output, built.package_sha256)
    assert (
        package_defensive.main(
            [
                "verify",
                "--package",
                str(output),
                "--approve-package",
                built.package_sha256,
            ]
        )
        == 1
    )


def test_an_extra_report_file_from_the_renderer_refuses(repo, tmp_path, monkeypatch):
    import scripts.build_site as site

    real = site.build_site

    def with_extra(**kwargs):
        real(**kwargs)
        (kwargs["output_path"] / "reports" / "2026-01-01.html").write_text("<p>x</p>")

    monkeypatch.setattr(site, "build_site", with_extra)
    source, revision = repo
    with pytest.raises(package.DefensivePackageError) as caught:
        package.build_package(source=source, revision=revision, output=out(tmp_path))
    assert str(caught.value) == "extra_report_file"
    assert not out(tmp_path).exists()


def test_an_explicit_timestamp_is_pinned_and_a_malformed_one_refuses(repo, tmp_path):
    source, revision = repo
    built = package.build_package(
        source=source,
        revision=revision,
        output=out(tmp_path),
        generated_at="2026-11-20T00:00:00Z",
    )
    assert built.generated_at == "2026-11-20T00:00:00Z"
    with pytest.raises(package.DefensivePackageError):
        package.build_package(
            source=source,
            revision=revision,
            output=out(tmp_path, "bad"),
            generated_at="2026-11-20",
        )


def test_output_inside_the_source_refuses(repo):
    source, revision = repo
    with pytest.raises(package.DefensivePackageError) as caught:
        package.build_package(
            source=source, revision=revision, output=source / "package"
        )
    assert str(caught.value) == "output_unsafe"


def test_cli_proposes_without_approval_and_refuses_a_partial_one(
    repo, tmp_path, capsys
):
    source, revision = repo
    base = ["build", "--source", str(source), "--revision", revision]
    assert package_defensive.main([*base, "--output", str(out(tmp_path))]) == 0
    proposal = json.loads(capsys.readouterr().out)
    assert proposal["approved"] is False and proposal["head"] == revision
    partial = [*base, "--output", str(out(tmp_path, "p")), "--approve-head", revision]
    assert package_defensive.main(partial) == 1
    assert json.loads(capsys.readouterr().out) == {"refused": "approval_incomplete"}
    assert not out(tmp_path, "p").exists()


def test_an_approved_build_refuses_when_checkout_head_is_not_the_approved_head(
    repo, tmp_path
):
    source, revision = repo
    proposal = package.build_package(
        source=source, revision=revision, output=out(tmp_path)
    )
    commit(
        source, {"site/site.css": (source / "site" / "site.css").read_bytes() + b"\n"}
    )
    with pytest.raises(package.DefensivePackageError) as caught:
        package.build_package(
            source=source,
            revision=revision,
            output=out(tmp_path, "approved"),
            approval=package.Approval(
                revision, proposal.facts_sha256, proposal.package_sha256
            ),
        )
    assert str(caught.value) == "approval_checkout_mismatch"
    assert not out(tmp_path, "approved").exists()


@pytest.mark.parametrize(
    "name", ["bad\nname.html", "ctl\x01.html", "del\x7f.html", "back\\slash.html"]
)
def test_unsafe_names_refuse_before_any_byte_is_digested(
    repo, tmp_path, monkeypatch, name
):
    source, revision = repo
    output = out(tmp_path)
    built = package.build_package(source=source, revision=revision, output=output)
    (output / name).write_text("x")

    def no_digest(_):
        raise AssertionError("digested before the name check")

    monkeypatch.setattr(package, "_sha256", no_digest)
    with pytest.raises(package.DefensivePackageError) as caught:
        package.verify_package(output, built.package_sha256)
    assert str(caught.value) == "unsafe_path_name"


def test_the_closed_inventory_matches_the_node_gate_and_the_built_package(
    repo, tmp_path
):
    source, revision = repo
    output = out(tmp_path)
    package.build_package(source=source, revision=revision, output=output)
    built = {p.relative_to(output).as_posix() for p in output.rglob("*") if p.is_file()}
    assert built == package.closed_inventory()
    node = json.loads(
        subprocess.check_output(
            [
                "node",
                "-e",
                "console.log(JSON.stringify(require('./publication/kit/defensive').CLOSED_PATHS))",
            ],
            cwd=ROOT,
            text=True,
        )
    )
    assert set(node) == package.closed_inventory() and len(node) == len(set(node))
    assert not any(path.startswith("reports/2") for path in node)
