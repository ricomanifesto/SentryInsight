#!/usr/bin/env python3
"""Loopback server for static artifact acceptance.

Serves one artifact directory only: no directory listings, no symlinks, and
404 for anything that is not a file inside the artifact. Python's http.server
lists index-less directories, so it is not used for acceptance.
"""

from __future__ import annotations

import argparse
import os
import sys
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.build_static_artifact import read_current_build  # noqa: E402

CONTENT_TYPES = {
    ".css": "text/css; charset=utf-8",
    ".html": "text/html; charset=utf-8",
    ".ico": "image/x-icon",
    ".js": "text/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".md": "text/markdown; charset=utf-8",
    ".png": "image/png",
    ".svg": "image/svg+xml",
    ".txt": "text/plain; charset=utf-8",
    ".webmanifest": "application/manifest+json; charset=utf-8",
    ".xml": "application/xml; charset=utf-8",
}


def _request_segments(raw_path: str) -> list[str] | None:
    decoded = unquote(raw_path, errors="strict")
    if not decoded.startswith("/") or "\\" in decoded or "\0" in decoded:
        return None
    segments = decoded[1:].split("/")
    if segments[-1] == "":
        segments.pop()
    if any(segment in {"", ".", ".."} for segment in segments):
        return None
    return segments


def _resolve_inside(root: Path, segments: list[str]) -> Path | None:
    current = root
    for segment in segments:
        current = current / segment
        if current.is_symlink() or not os.path.lexists(current):
            return None
    return current


def create_artifact_server(
    *, root: Path, site: str, inventory_digest: str, port: int, host: str = "127.0.0.1"
) -> ThreadingHTTPServer:
    """Return a server bound to host:port that serves only `root`."""
    artifact_root = Path(os.path.realpath(root))
    identity = f"{site} {inventory_digest}"

    class ArtifactHandler(BaseHTTPRequestHandler):
        server_version = "StaticArtifact"
        sys_version = ""

        def log_message(self, format: str, *args: object) -> None:
            return

        def _send(
            self, status: int, headers: dict[str, str], body: bytes = b""
        ) -> None:
            self.send_response(status)
            self.send_header("X-Static-Artifact", identity)
            self.send_header("Cache-Control", "no-store")
            for name, value in headers.items():
                self.send_header(name, value)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)

        def _not_found(self) -> None:
            self._send(
                HTTPStatus.NOT_FOUND,
                {"Content-Type": "text/plain; charset=utf-8"},
                b"Not found\n",
            )

        def _method_not_allowed(self) -> None:
            self._send(
                HTTPStatus.METHOD_NOT_ALLOWED,
                {"Allow": "GET, HEAD", "Content-Type": "text/plain; charset=utf-8"},
                b"Method not allowed\n",
            )

        do_POST = do_PUT = do_DELETE = do_PATCH = do_OPTIONS = _method_not_allowed

        def do_HEAD(self) -> None:
            self.do_GET()

        def do_GET(self) -> None:
            url = urlsplit(self.path)
            try:
                segments = _request_segments(url.path)
            except UnicodeDecodeError:
                segments = None
            target = (
                None if segments is None else _resolve_inside(artifact_root, segments)
            )
            if target is None:
                self._not_found()
                return
            if target.is_dir():
                index = target / "index.html"
                if index.is_symlink() or not index.is_file():
                    self._not_found()
                    return
                if not url.path.endswith("/"):
                    query = f"?{url.query}" if url.query else ""
                    location = f"{url.path}/{query}"
                    self._send(HTTPStatus.MOVED_PERMANENTLY, {"Location": location})
                    return
                target = index
            elif not target.is_file() or url.path.endswith("/"):
                self._not_found()
                return
            content_type = CONTENT_TYPES.get(target.suffix, "application/octet-stream")
            body = target.read_bytes()
            self._send(HTTPStatus.OK, {"Content-Type": content_type}, body)

    return ThreadingHTTPServer((host, port), ArtifactHandler)


def main() -> int:
    parser = argparse.ArgumentParser(description="Serve a built static artifact.")
    parser.add_argument("--store", type=Path, required=True)
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "4175")))
    args = parser.parse_args()
    current = read_current_build(args.store, verify=True)
    server = create_artifact_server(
        root=current.artifact_dir,
        site=current.site,
        inventory_digest=current.inventory_digest,
        port=args.port,
    )
    print(
        f"{current.site} artifact {current.inventory_digest} listening on "
        f"http://127.0.0.1:{args.port}",
        flush=True,
    )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
