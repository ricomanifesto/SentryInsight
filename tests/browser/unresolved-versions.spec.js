import { execFileSync } from "node:child_process";
import { expect, test } from "@playwright/test";

// Exercise the real resolver, artifact parser and renderer with a synthetic
// source. No provider call or production report is involved.
let rendered;
test.beforeAll(() => {
  rendered = execFileSync(".venv/bin/python", ["-B", "-c", `
import sys, tempfile
from pathlib import Path
sys.path.insert(0, "tests")
from test_unresolved_versions import artifact_text, raw_report, unresolved_catalog, unresolved_refs
from test_site_builder import build_fixture
from src.core.version_references import resolve_version_references
catalog = unresolved_catalog()
reference = unresolved_refs(catalog)[0]["id"]
report = resolve_version_references(raw_report(catalog, reference), catalog)
with tempfile.TemporaryDirectory() as directory:
    root = build_fixture(Path(directory), artifact_text(report, catalog))
    print((root / "index.html").read_text())
`], { encoding: "utf8" });
});

for (const javaScriptEnabled of [true, false]) {
  test(`unresolved versions stay visible with JavaScript ${javaScriptEnabled}`, async ({ browser }) => {
    const context = await browser.newContext({ javaScriptEnabled });
    const page = await context.newPage();
    const failures = [];
    page.on("pageerror", (error) => failures.push(error.message));
    await page.route("**/synthetic-unresolved.html", (route) => route.fulfill({
      status: 200, contentType: "text/html", body: rendered,
    }));
    await page.goto("/synthetic-unresolved.html");
    await expect(page.getByRole("note")).toContainText("1 finding has unresolved affected-version evidence");
    await expect(page.locator(".finding-reporting")).toContainText("Affected versions unresolved.");
    await expect(page.locator(".finding-reporting")).toContainText("Review the linked reporting");
    await expect(page.locator(".reporting-source")).toHaveAttribute("href", "https://example.test/one");
    await expect(page.locator("#report-content")).toContainText("Unresolved from supplied sources.");
    await expect(page.locator("#report-content")).not.toContainText("Affected Versions Status");
    const metadata = JSON.parse(await page.locator("#report-metadata").textContent());
    expect(metadata.schema_version).toBe(4);
    expect(metadata.unresolved_version_count).toBe(1);
    expect(metadata.findings[0].affected_versions_status).toBe("unresolved");
    expect(failures).toEqual([]);
    await context.close();
  });
}
