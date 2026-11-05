"""The sealed host-worker child must still find the parent's trusted Node.

Hosted runners install Node outside the child's fixed system PATH, so the
closed setup rehearsal refused before any credential or request. The parent
resolves Node once, exactly as PersistentOwner does, and the child receives
only that directory in front of its fixed PATH.
"""

import asyncio
import json
import os
from pathlib import Path
import shutil

import pytest

from scripts import execute_full_feed_canary as canary
from scripts.rehearse_full_feed_canary import environment


def fake_node(directory: Path) -> Path:
    directory.mkdir(parents=True)
    node = directory / "node"
    node.write_text("#!/bin/sh\nexit 0\n")
    node.chmod(0o755)
    return node


def capture_child(monkeypatch):
    seen = {}

    async def run_private(argv, value, deadline, *, env, cwd, limit):
        seen["argv"], seen["env"] = argv, env
        return json.dumps({"ok": {"removed": True}}).encode()

    monkeypatch.setattr(canary, "run_private", run_private)
    return seen


def test_worker_child_path_carries_only_the_parent_resolved_node(tmp_path, monkeypatch):
    toolcache = tmp_path / "hostedtoolcache" / "node" / "24.0.0" / "x64" / "bin"
    node = fake_node(toolcache)
    monkeypatch.setenv("PATH", f"{toolcache}{os.pathsep}/usr/bin{os.pathsep}/bin")
    seen = capture_child(monkeypatch)

    result = asyncio.run(canary.worker({"mode": "cleanup"}, None))

    assert result == {"removed": True}
    sealed = environment()
    child = seen["env"]
    assert child["PATH"] == f"{toolcache}{os.pathsep}{sealed['PATH']}"
    assert shutil.which("node", path=child["PATH"]) == str(node)
    # Nothing else from the parent leaks into the sealed child.
    assert set(child) - set(sealed) <= {"TIKTOKEN_CACHE_DIR"}
    assert child["GIT_ALLOW_PROTOCOL"] == "https"


def test_worker_refuses_before_spawn_without_a_trusted_node(tmp_path, monkeypatch):
    empty = tmp_path / "empty"
    empty.mkdir()
    monkeypatch.setenv("PATH", str(empty))
    seen = capture_child(monkeypatch)

    with pytest.raises(ValueError):
        asyncio.run(canary.worker({"mode": "cleanup"}, None))

    assert seen == {}
