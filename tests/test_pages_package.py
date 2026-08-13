from pathlib import Path

from scripts.package_pages import package_pages

ROOT = Path(__file__).resolve().parents[1]


def test_pages_package_contains_only_finished_public_artifacts(tmp_path):
    output_path = tmp_path / "public"

    package_pages(repo_root=ROOT, output_path=output_path)

    assert {path.name for path in output_path.iterdir()} == {
        ".nojekyll",
        "assets",
        "index.html",
        "index.md",
        "reports",
        "sitemap.xml",
    }
    assert not (output_path / "site").exists()
    assert not (output_path / "tests").exists()
    assert not (output_path / "scripts").exists()
    assert not (output_path / "README.md").exists()
    assert not (output_path / ".github").exists()
    assert not list(output_path.rglob("*.py"))
    assert not list(output_path.rglob("*.yml"))
    assert not list(output_path.rglob("*.yaml"))
    assert not list(output_path.rglob("package*.json"))


def test_pages_package_rebuilds_deterministically_without_template_placeholders(
    tmp_path,
):
    first = tmp_path / "first"
    second = tmp_path / "second"

    package_pages(repo_root=ROOT, output_path=first)
    package_pages(repo_root=ROOT, output_path=second)

    first_files = {
        path.relative_to(first): path.read_bytes()
        for path in first.rglob("*")
        if path.is_file()
    }
    second_files = {
        path.relative_to(second): path.read_bytes()
        for path in second.rglob("*")
        if path.is_file()
    }
    assert first_files == second_files
    for relative_path, content in first_files.items():
        if relative_path.suffix == ".html":
            assert b"{{" not in content
