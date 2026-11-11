#!/usr/bin/env python3
"""Bounded workaround for Azure mirror DNS outages on Ubuntu CI runners.

Run with sudo before Playwright's unchanged --with-deps installation. Only an
active, exact Azure Ubuntu archive URI is replaced. APT still verifies its
normal signed indexes and packages using the existing source configuration.
"""

from pathlib import Path
import re
import subprocess
import sys

AZURE = "azure.archive.ubuntu.com"
ARCHIVE = "archive.ubuntu.com"
AZURE_URI = re.compile(r"https?://azure\.archive\.ubuntu\.com/ubuntu/?$")


def azure_resolves() -> bool:
    for _ in range(2):
        try:
            result = subprocess.run(
                ["getent", "ahosts", AZURE],
                capture_output=True,
                timeout=5,
                check=False,
            )
            if result.returncode == 0 and result.stdout.strip():
                return True
        except subprocess.TimeoutExpired:
            pass
    return False


def archive_reachable() -> bool:
    try:
        return (
            subprocess.run(
                [
                    "curl",
                    "--fail",
                    "--silent",
                    "--show-error",
                    "--head",
                    "--connect-timeout",
                    "5",
                    "--max-time",
                    "15",
                    "--retry",
                    "0",
                    f"https://{ARCHIVE}/ubuntu/",
                ],
                capture_output=True,
                timeout=20,
                check=False,
            ).returncode
            == 0
        )
    except subprocess.TimeoutExpired:
        return False


def replace_uri(uri: str) -> str:
    if AZURE in uri and not AZURE_URI.fullmatch(uri):
        raise ValueError(f"Unsupported Azure archive URI: {uri}")
    if AZURE_URI.fullmatch(uri):
        return uri.replace(AZURE, ARCHIVE).replace("http://", "https://", 1)
    return uri


def replace_sources(
    text: str, suffix: str, mirror_lists: set[str] | None = None
) -> str:
    """Preserve comments, options, signing keys, suites and other repositories."""

    def source_uri(uri: str) -> str:
        if uri == "mirror+file:/etc/apt/apt-mirrors.txt" and mirror_lists is not None:
            mirror_lists.add("apt-mirrors.txt")
        return replace_uri(uri)

    if suffix == ".list":
        return re.sub(
            r"(?m)^([ \t]*deb(?:-src)?[ \t]+(?:\[[^\]\n]*\][ \t]+)?)(\S+)",
            lambda m: m[1] + source_uri(m[2]),
            text,
        )
    if suffix != ".sources":
        raise ValueError(f"Unsupported APT source format: {suffix}")
    blocks = re.split(r"(\n[ \t]*\n)", text)
    for index in range(0, len(blocks), 2):
        block = blocks[index]
        if re.search(r"(?im)^Enabled:\s*no\s*$", block):
            continue
        blocks[index] = re.sub(
            r"(?im)^(URIs:[^\n]*(?:\n[ \t]+[^\n]*)*)",
            lambda m: re.sub(
                r"(?:https?://|mirror\+file:)[^\s]+",
                lambda uri: source_uri(uri[0]),
                m[0],
            ),
            block,
        )
    return "".join(blocks)


def prepare(apt_dir: Path = Path("/etc/apt")) -> None:
    if azure_resolves():
        print("Azure Ubuntu mirror resolves; leaving APT sources unchanged.")
        return
    files = [apt_dir / "sources.list"]
    files += sorted((apt_dir / "sources.list.d").glob("*.list"))
    files += sorted((apt_dir / "sources.list.d").glob("*.sources"))
    changes = []
    mirror_lists: set[str] = set()
    for path in files:
        if not path.is_file():
            continue
        original = path.read_text()
        updated = replace_sources(original, path.suffix, mirror_lists)
        if updated != original:
            changes.append((path, updated))
    # GitHub's official runner image uses this local mirror list (priority tags
    # included), referenced by either a legacy list or deb822 source stanza:
    # actions/runner-images/images/ubuntu/scripts/build/configure-apt-sources.sh
    for name in sorted(mirror_lists):
        path = apt_dir / name
        original = path.read_text()
        updated = re.sub(
            r"(?m)^([ \t]*)(https?://\S+)",
            lambda m: m[1] + replace_uri(m[2]),
            original,
        )
        if updated != original:
            changes.append((path, updated))
    if not changes:
        print(
            "No active Azure Ubuntu mirror to replace; leaving APT sources unchanged."
        )
        return
    if not archive_reachable():
        raise ValueError(
            "Azure mirror DNS failed and the official Ubuntu archive is "
            "unreachable; APT sources were not changed."
        )
    for path, updated in changes:
        path.write_text(updated)
        print(f"Azure mirror DNS failed; switched {path} to {ARCHIVE}.")


def main() -> int:
    try:
        prepare()
    except (OSError, ValueError) as exc:
        print(f"Ubuntu mirror preflight failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
