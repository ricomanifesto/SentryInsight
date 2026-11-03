import http.client
import threading
from collections.abc import Iterator
from pathlib import Path

import pytest

from scripts.serve_static_artifact import create_artifact_server

FILES = {
    "index.html": "<!doctype html><title>Current</title>\n",
    "index.md": "# Current\n",
    "reports/index.html": "<!doctype html><title>Archive</title>\n",
    "reports/index.json": '{"schema_version": 1}\n',
    "reports/2026-01-01.html": "<!doctype html><title>Dated</title>\n",
    "reports/2026-01-01.md": "# Dated\n",
    "assets/icon.svg": '<svg xmlns="http://www.w3.org/2000/svg"></svg>\n',
    "assets/favicon.ico": "ico",
    "assets/logo.png": "png",
    "assets/site.css": "body{}\n",
    "assets/report.js": "void 0;\n",
    "assets/vendor/DOMPURIFY-LICENSE.txt": "license\n",
    "sitemap.xml": "<urlset></urlset>\n",
    "site.webmanifest": "{}\n",
    ".nojekyll": "",
}
DIGEST = "b" * 64


@pytest.fixture
def server_address(tmp_path: Path) -> Iterator[tuple[str, int]]:
    root = tmp_path / "artifact"
    for relative_path, content in FILES.items():
        target = root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
    (tmp_path / "secret.txt").write_text("outside\n")
    (root / "assets" / "linked.txt").symlink_to(tmp_path / "secret.txt")
    (root / "linked-dir").symlink_to(root / "reports")

    server = create_artifact_server(
        root=root, site="SentryInsight", inventory_digest=DIGEST, port=0
    )
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server.server_address[0], server.server_address[1]
    finally:
        server.shutdown()
        server.server_close()


def _request(address: tuple[str, int], path: str, method: str = "GET"):
    connection = http.client.HTTPConnection(*address, timeout=10)
    connection.putrequest(method, path, skip_accept_encoding=True)
    connection.endheaders()
    response = connection.getresponse()
    body = response.read()
    connection.close()
    return response.status, dict(response.getheaders()), body


def test_serves_files_with_explicit_types_and_identity(server_address):
    expectations = {
        "/": ("text/html; charset=utf-8", FILES["index.html"]),
        "/index.html": ("text/html; charset=utf-8", FILES["index.html"]),
        "/index.md": ("text/markdown; charset=utf-8", FILES["index.md"]),
        "/reports/": ("text/html; charset=utf-8", FILES["reports/index.html"]),
        "/reports/index.json": (
            "application/json; charset=utf-8",
            FILES["reports/index.json"],
        ),
        "/reports/2026-01-01.html": (
            "text/html; charset=utf-8",
            FILES["reports/2026-01-01.html"],
        ),
        "/assets/icon.svg": ("image/svg+xml", FILES["assets/icon.svg"]),
        "/assets/favicon.ico": ("image/x-icon", FILES["assets/favicon.ico"]),
        "/assets/logo.png": ("image/png", FILES["assets/logo.png"]),
        "/assets/site.css?v=0123456789ab": (
            "text/css; charset=utf-8",
            FILES["assets/site.css"],
        ),
        "/assets/report.js": (
            "text/javascript; charset=utf-8",
            FILES["assets/report.js"],
        ),
        "/assets/vendor/DOMPURIFY-LICENSE.txt": (
            "text/plain; charset=utf-8",
            FILES["assets/vendor/DOMPURIFY-LICENSE.txt"],
        ),
        "/sitemap.xml": ("application/xml; charset=utf-8", FILES["sitemap.xml"]),
        "/site.webmanifest": (
            "application/manifest+json; charset=utf-8",
            FILES["site.webmanifest"],
        ),
        "/.nojekyll": ("application/octet-stream", ""),
    }
    for route, (content_type, body) in expectations.items():
        status, headers, content = _request(server_address, route)
        assert status == 200, route
        assert headers["Content-Type"] == content_type, route
        assert content == body.encode(), route
        assert headers["X-Static-Artifact"] == f"SentryInsight {DIGEST}", route

    status, headers, content = _request(server_address, "/sitemap.xml", "HEAD")
    assert status == 200
    assert content == b""


def test_redirects_an_indexed_directory_without_its_slash(server_address):
    status, headers, _ = _request(server_address, "/reports?from=test")

    assert status == 301
    assert headers["Location"] == "/reports/?from=test"


@pytest.mark.parametrize(
    "route",
    [
        "/assets/",
        "/assets",
        "/missing.html",
        "/index.html/",
        "/assets/linked.txt",
        "/linked-dir/",
        "/linked-dir/index.html",
        "/../secret.txt",
        "/%2e%2e/secret.txt",
        "/assets/..%2f..%2fsecret.txt",
        "/assets/..%5c..%5csecret.txt",
        "/index.html%00.png",
        "/.git/HEAD",
        "/package.json",
        "//etc/passwd",
    ],
)
def test_returns_404_without_listing_symlinks_or_traversal(server_address, route):
    status, _, content = _request(server_address, route)

    assert status == 404
    assert b"outside" not in content
    assert b"Directory listing" not in content
    assert b"<a href" not in content


def test_rejects_methods_other_than_get_and_head(server_address):
    status, headers, _ = _request(server_address, "/index.html", "POST")

    assert status == 405
    assert headers["Allow"] == "GET, HEAD"
