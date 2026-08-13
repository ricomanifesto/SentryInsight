#!/usr/bin/env python3
"""Build the allowlisted artifact deployed to GitHub Pages."""

from __future__ import annotations

# ruff: noqa: E402

import argparse
import re
import shutil
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from scripts.build_site import build_site

STATIC_ASSETS = (
    "apple-touch-icon.png",
    "favicon.ico",
    "icon-192.png",
    "icon-512.png",
    "icon-small.svg",
    "icon.svg",
    "logo-lockup-dark.png",
    "logo-lockup-light.png",
    "logo.png",
    "logo.svg",
    "social-preview.png",
)
EXPECTED_TOP_LEVEL = {
    ".nojekyll",
    "assets",
    "index.html",
    "index.md",
    "reports",
    "sitemap.xml",
}


class PagesPackageError(RuntimeError):
    """Raised when the deploy artifact cannot be built safely."""


def _validate_output_target(*, repo_root: Path, output_path: Path) -> None:
    resolved_output = output_path.resolve()
    forbidden = {Path("/"), repo_root.resolve(), repo_root.resolve().parent}
    if resolved_output in forbidden or len(resolved_output.parts) < 3:
        raise PagesPackageError(f"Unsafe Pages output path: {resolved_output}")


def _copy_report_sources(*, repo_root: Path, stage: Path) -> None:
    shutil.copy2(repo_root / "index.md", stage / "index.md")
    staged_reports = stage / "reports"
    staged_reports.mkdir()
    source_reports = repo_root / "reports"
    if source_reports.exists():
        for report in source_reports.glob("????-??-??.md"):
            shutil.copy2(report, staged_reports / report.name)


def _copy_static_assets(*, repo_root: Path, stage: Path) -> None:
    source_assets = repo_root / "assets"
    target_assets = stage / "assets"
    for name in STATIC_ASSETS:
        source = source_assets / name
        if not source.is_file():
            raise PagesPackageError(f"Missing public asset: assets/{name}")
        shutil.copy2(source, target_assets / name)


def _validate_package(stage: Path) -> None:
    top_level = {path.name for path in stage.iterdir()}
    if top_level != EXPECTED_TOP_LEVEL:
        unexpected = sorted(top_level - EXPECTED_TOP_LEVEL)
        missing = sorted(EXPECTED_TOP_LEVEL - top_level)
        raise PagesPackageError(
            f"Unexpected Pages package shape; missing={missing}, unexpected={unexpected}"
        )
    for page in stage.rglob("*.html"):
        content = page.read_text()
        if re.search(r"{{[A-Z0-9_]+}}", content):
            raise PagesPackageError(
                f"Unresolved template value in {page.relative_to(stage)}"
            )


def package_pages(*, repo_root: Path, output_path: Path) -> None:
    """Rebuild and replace a Pages artifact containing public files only."""
    repo_root = repo_root.resolve()
    output_path = output_path.resolve()
    _validate_output_target(repo_root=repo_root, output_path=output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(
        prefix=".sentryinsight-pages-", dir=output_path.parent
    ) as temp_dir:
        stage = Path(temp_dir) / "public"
        stage.mkdir()
        _copy_report_sources(repo_root=repo_root, stage=stage)
        build_site(
            report_path=stage / "index.md",
            output_path=stage,
            template_path=repo_root / "site",
        )
        _copy_static_assets(repo_root=repo_root, stage=stage)
        (stage / ".nojekyll").write_text("")
        _validate_package(stage)

        if output_path.exists():
            if output_path.is_symlink() or not output_path.is_dir():
                raise PagesPackageError(
                    f"Refusing to replace non-directory Pages output: {output_path}"
                )
            shutil.rmtree(output_path)
        shutil.copytree(stage, output_path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    package_pages(repo_root=args.root, output_path=args.output)
    print(f"Packaged GitHub Pages artifact at {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
