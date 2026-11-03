import { execFileSync } from "node:child_process";
import { expect, test } from "@playwright/test";

let rendered;
test.beforeAll(() => {
  // Exercise the shared gate and renderer using synthetic source metadata only.
  rendered = execFileSync(".venv/bin/python", ["-B", "-c", `
import sys, tempfile
from pathlib import Path
sys.path.insert(0, "tests")
from src.core.reviewed_report import resolve_reviewed_analysis
from test_reviewed_report import prepared_result
from test_source_review import AMBIGUOUS
from test_unresolved_versions import raw_report
from test_version_references import ABSENT, source
from test_site_builder import build_fixture
articles = [
    source("An independent advisory.", "cited"),
    source("A separate advisory.", "uncited"),
    source(AMBIGUOUS, "held"),
    source("Affected versions:", "rejected"),
]
articles[2]["title"] = "<img src=x onerror=alert(1)> held article"
result = prepared_result(articles)
cited = next(row["key"] for row in result["source_review_plan"]["sources"] if row["url"].endswith("/cited"))
result["exploitation_report"] = raw_report([cited], ABSENT)
candidate = resolve_reviewed_analysis(result)
with tempfile.TemporaryDirectory() as directory:
    root = build_fixture(Path(directory), candidate.source)
    print((root / "index.html").read_text())
`], { encoding: "utf8" });
});

for (const javaScriptEnabled of [true, false]) {
  for (const width of [1280, 390]) {
    test(`coverage remains distinct from findings at width ${width} with JavaScript ${javaScriptEnabled}`, async ({ browser }) => {
      const context = await browser.newContext({ javaScriptEnabled, viewport: { width, height: 900 } });
      const page = await context.newPage();
      const failures = [];
      page.on("pageerror", (error) => failures.push(error.message));
      await page.route("**/synthetic-source-coverage.html", (route) => route.fulfill({
        status: 200, contentType: "text/html", body: rendered,
      }));
      await page.goto("/synthetic-source-coverage.html");
      const notice = page.locator("#source-coverage-notice");
      await expect(notice).toBeVisible();
      await expect(notice).toContainText("Partial source coverage.");
      await expect(notice).toContainText("1 of 4 input sources are cited.");
      await expect(notice).toContainText("1 await review; 1 failed source validation.");

      const coverage = page.getByRole("region", { name: "Source Coverage and Review" });
      await notice.getByRole("link", { name: "Review source dispositions" }).click();
      await expect(coverage).toBeVisible();
      await expect(coverage.getByRole("table")).toBeVisible();
      await expect(coverage.locator("tbody tr")).toHaveCount(4);
      for (const [suffix, disposition] of [
        ["cited", "Cited in validated findings"],
        ["uncited", "Eligible input; not represented"],
        ["held", "Awaiting human review"],
        ["rejected", "Rejected by source validation"],
      ]) {
        const row = coverage.getByRole("row").filter({ has: page.locator(`a[href="https://example.test/${suffix}"]`) });
        await expect(row).toContainText(disposition);
        await expect(row.getByRole("link")).toBeVisible();
      }
      await expect(coverage).toContainText("An unrepresented source has not been declared irrelevant or reviewed.");
      await expect(coverage.locator("img")).toHaveCount(0);
      const metadata = JSON.parse(await page.locator("#report-metadata").textContent());
      expect(metadata.schema_version).toBe(5);
      expect(metadata.finding_count).toBe(1);
      expect(metadata.source_coverage.counts.input_sources).toBe(4);
      await expect(page.locator(".finding-heading")).toHaveCount(1);
      await expect(page.locator(".finding-reporting")).not.toContainText("held article");
      if (javaScriptEnabled) {
        await page.locator("button.finding-disclosure").click();
        await expect(coverage).toBeVisible();
        await expect(notice).toBeVisible();
      }
      expect(failures).toEqual([]);
      await context.close();
    });
  }
}
