import { execFileSync } from "node:child_process";
import { writeFileSync } from "node:fs";
import { expect, test } from "@playwright/test";

let rendered;
test.beforeAll(() => {
  rendered = JSON.parse(execFileSync(".venv/bin/python", ["-B", "-c", `
import json, sys, tempfile
from pathlib import Path
sys.path.insert(0, "tests")
from src.core.report_findings import report_findings
from src.core.reporting import deserialize_reporting_catalog, resolve_reporting_keys
from src.core.reviewed_report import resolve_reviewed_analysis
from src.core.version_references import resolve_analysis_version_references
from test_finding_grouping import A, B, finding
from test_reviewed_report import prepared_result
from test_version_references import source
from test_site_builder import build_fixture
C = "CVE-2026-9999"
result = prepared_result([
    source(f"{A} and {B} form an exploit chain.", "chain"),
    source(f"{A} is described in follow-up reporting.", "followup"),
    source(f"{C} is a separate service issue.", "distinct"),
])
keys = {item["url"].rsplit("/", 1)[-1]: item["key"] for item in result["reporting_sources"]}
original = result["exploitation_report"]
row = report_findings(original).rows[0]
entries = (finding([keys["chain"], keys["followup"]], A) + finding([keys["chain"]], B)
    + finding([keys["distinct"]], C).replace("Gateway flaw", "Separate service flaw"))
result["exploitation_report"] = original[:row.start] + entries + original[row.end:]
candidate = resolve_reviewed_analysis(result)
catalog = deserialize_reporting_catalog(result["reporting_sources"])
before = resolve_reporting_keys(resolve_analysis_version_references(result), catalog)
before_source = candidate.source.replace(candidate.report, before)
with tempfile.TemporaryDirectory() as directory:
    for name in ("before", "after"):
        (Path(directory) / name).mkdir()
    roots = {name: build_fixture(Path(directory) / name, text) for name, text in
        [("before", before_source), ("after", candidate.source)]}
    print(json.dumps({name: (root / "index.html").read_text() for name, root in roots.items()}))
`], { encoding: "utf8" }));
});

for (const [name, viewport] of Object.entries({
  desktop: { width: 1440, height: 900 },
  phone: { width: 393, height: 851 },
})) {
  test(`related reporting stays within its finding on ${name}`, async ({ page }) => {
    await page.setViewportSize(viewport);
    const errors = [];
    page.on("pageerror", (error) => errors.push(error.message));
    for (const state of ["before", "after"]) {
      await page.route(`**/grouping-${state}.html`, (route) => route.fulfill({
        contentType: "text/html", body: rendered[state],
      }));
    }
    await page.goto("/grouping-before.html");
    await expect(page.locator(".finding-heading")).toHaveCount(3);
    const beforeHeight = await page.evaluate(() => document.documentElement.scrollHeight);
    await page.goto("/grouping-after.html");
    await expect(page.locator(".finding-heading")).toHaveCount(2);
    const metadata = JSON.parse(await page.locator("#report-metadata").textContent());
    expect(metadata.findings.map((item) => item.cve_ids.length)).toEqual([2, 1]);
    expect(metadata.source_coverage.counts.cited_sources).toBe(3);
    const reporting = page.locator(".finding-reporting").first();
    await expect(reporting.locator('a[href="https://example.test/chain"]')).toBeVisible();
    await expect(reporting.locator('a[href="https://example.test/followup"]')).toBeVisible();
    await expect(page.locator(".finding-heading").last()).toContainText("Separate service flaw");
    const afterHeight = await page.evaluate(() => document.documentElement.scrollHeight);
    expect(afterHeight).toBeLessThan(beforeHeight);
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1)).toBe(true);
    expect(errors).toEqual([]);
    writeFileSync(`test-results/grouping-layout-${name}.json`, JSON.stringify({ beforeHeight, afterHeight, viewport }));
    await page.screenshot({ path: `test-results/screenshots/grouping-${name}.png`, fullPage: true });
  });
}
