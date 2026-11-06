"""Acceptance for a built static artifact.

Not collected by the default `pytest tests` run: it needs a store produced by
scripts/build_static_artifact.py and the pinned source repository.

    STATIC_ARTIFACT_STORE=<store> STATIC_ARTIFACT_SOURCE=<repo> \\
        python -B -m pytest tests/static_artifact_acceptance.py -p no:cacheprovider
"""

import http.client
import json
import os
import re
import subprocess
import tempfile
import threading
import xml.etree.ElementTree as ET
from collections.abc import Iterator
from pathlib import Path

import pytest

from scripts.build_static_artifact import CurrentBuild, read_current_build
from scripts.package_pages import package_pages
from scripts.serve_static_artifact import create_artifact_server

from src.core.public_site import emitted_origin

PUBLIC_ROOT = emitted_origin("SentryInsight")
STORE = os.environ.get("STATIC_ARTIFACT_STORE")
SOURCE = os.environ.get("STATIC_ARTIFACT_SOURCE")
CONTENT_TYPES = {
    "": "application/octet-stream",
    ".css": "text/css; charset=utf-8",
    ".html": "text/html; charset=utf-8",
    ".ico": "image/x-icon",
    ".js": "text/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".md": "text/markdown; charset=utf-8",
    ".png": "image/png",
    ".svg": "image/svg+xml",
    ".txt": "text/plain; charset=utf-8",
    ".xml": "application/xml; charset=utf-8",
}
NEGATIVE_ROUTES = [
    "/scripts/package_pages.py",
    "/scripts/build_site.py",
    "/package.json",
    "/playwright.config.js",
    "/pyproject.toml",
    "/uv.lock",
    "/README.md",
    "/site/report.html",
    "/tests/test_pages_package.py",
    "/test-results/",
    "/test-results/pages/index.html",
    "/.git/HEAD",
    "/.github/workflows/deploy-pages.yml",
    "/node_modules/",
    "/AGENTS.md",
    "/.env",
    "/src/",
    "/src/core/report_artifact.py",
    "/agent/",
    "/main.py",
    "/contracts/reporting-identity-verifier-v1.py",
    "/../pyproject.toml",
    "/assets/..%2f..%2fpyproject.toml",
    "/assets/",
    "/assets/vendor/",
    "/contracts/",
    "/reports/2026-01-01.html",
]

pytestmark = pytest.mark.skipif(
    not STORE or not SOURCE,
    reason="STATIC_ARTIFACT_STORE and STATIC_ARTIFACT_SOURCE are required",
)


@pytest.fixture(scope="module")
def current() -> CurrentBuild:
    return read_current_build(Path(str(STORE)), verify=True)


@pytest.fixture(scope="module")
def address(current: CurrentBuild) -> Iterator[tuple[str, int]]:
    server = create_artifact_server(
        root=current.artifact_dir,
        site="SentryInsight",
        inventory_digest=current.inventory_digest,
        port=0,
    )
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server.server_address[0], server.server_address[1]
    finally:
        server.shutdown()
        server.server_close()


def _get(address: tuple[str, int], path: str) -> tuple[int, dict[str, str], bytes]:
    connection = http.client.HTTPConnection(*address, timeout=10)
    connection.putrequest("GET", path, skip_accept_encoding=True)
    connection.endheaders()
    response = connection.getresponse()
    body = response.read()
    connection.close()
    return response.status, dict(response.getheaders()), body


def _files(root: Path) -> dict[str, bytes]:
    files: dict[str, bytes] = {}
    for path in sorted(root.rglob("*")):
        assert not path.is_symlink(), path
        if path.is_file():
            files[path.relative_to(root).as_posix()] = path.read_bytes()
    return files


def _pinned(revision: str, relative_path: str) -> bytes:
    return subprocess.run(
        ["git", "cat-file", "blob", f"{revision}:{relative_path}"],
        cwd=str(SOURCE),
        check=True,
        capture_output=True,
    ).stdout


def _ids(html: str) -> set[str]:
    return set(re.findall(r'\sid="([^"]+)"', html))


def test_inventory_equals_the_existing_packager_output(current):
    with tempfile.TemporaryDirectory(prefix="insight-baseline-") as temp_dir:
        baseline = Path(temp_dir) / "public"
        package_pages(repo_root=Path(str(SOURCE)), output_path=baseline)
        assert _files(current.artifact_dir) == _files(baseline)


def test_every_artifact_file_equals_the_committed_projection(current):
    # The packager writes its own empty .nojekyll (the committed root copy is
    # not deployed); every other file is committed source or its projection.
    for relative_path, content in _files(current.artifact_dir).items():
        if relative_path == ".nojekyll":
            assert content == b""
            continue
        assert content == _pinned(current.source_revision, relative_path), relative_path


def test_every_file_is_served_with_its_bytes_and_type(current, address):
    for relative_path, content in _files(current.artifact_dir).items():
        status, headers, body = _get(address, f"/{relative_path}")
        assert status == 200, relative_path
        assert body == content, relative_path
        assert headers["Content-Type"] == CONTENT_TYPES[Path(relative_path).suffix]
        assert headers["X-Static-Artifact"] == (
            f"SentryInsight {current.inventory_digest}"
        )
    for route in ["/", "/reports/"]:
        status, headers, _ = _get(address, route)
        assert status == 200, route
        assert headers["Content-Type"] == "text/html; charset=utf-8", route


def test_json_and_sitemap_resolve_inside_the_artifact(current, address):
    for path in current.artifact_dir.rglob("*.json"):
        json.loads(path.read_text())
    manifest = json.loads((current.artifact_dir / "current-findings.json").read_text())
    assert manifest["report_url"] == PUBLIC_ROOT
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locations = [
        element.text or ""
        for element in ET.parse(current.artifact_dir / "sitemap.xml").findall(
            "sm:url/sm:loc", namespace
        )
    ]
    assert locations[:2] == [PUBLIC_ROOT, f"{PUBLIC_ROOT}reports/"]
    for location in locations:
        assert location.startswith(PUBLIC_ROOT), location
        status, _, _ = _get(address, f"/{location[len(PUBLIC_ROOT):]}")
        assert status == 200, location


def test_current_and_archived_reports_keep_committed_anchors(current, address):
    revision = current.source_revision
    manifest = json.loads(_pinned(revision, "current-findings.json"))
    archive = json.loads(_pinned(revision, "reports/index.json"))
    newest, oldest = archive["reports"][0], archive["reports"][-1]

    for route, committed_path, canonical, finding_count, cves in [
        (
            "/",
            "index.html",
            PUBLIC_ROOT,
            manifest["finding_count"],
            manifest["cve_ids"],
        ),
        (
            f"/reports/{newest['html_path']}",
            f"reports/{newest['html_path']}",
            f"{PUBLIC_ROOT}reports/{newest['html_path']}",
            newest["finding_count"],
            None,
        ),
        (
            f"/reports/{oldest['html_path']}",
            f"reports/{oldest['html_path']}",
            f"{PUBLIC_ROOT}reports/{oldest['html_path']}",
            oldest["finding_count"],
            None,
        ),
    ]:
        status, _, body = _get(address, route)
        served = body.decode()
        committed = _pinned(revision, committed_path).decode()
        assert status == 200, route
        assert _ids(served) == _ids(committed), route
        assert len(re.findall(r'<h3 id="[^"]+"', served)) == finding_count, route
        assert f'<link rel="canonical" href="{canonical}"' in served, route
        for cve in cves or []:
            assert f'id="{cve.lower()}"' in served, (route, cve)
        if cves is None:
            dated_cves = set(re.findall(r'id="(cve-\d{4}-\d+)"', committed))
            assert dated_cves <= _ids(served), route


@pytest.mark.parametrize("route", NEGATIVE_ROUTES)
def test_implementation_private_and_unlisted_paths_return_404(address, route):
    status, _, _ = _get(address, route)
    assert status == 404
