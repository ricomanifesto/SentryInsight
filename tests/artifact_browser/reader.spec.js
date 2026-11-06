import path from "node:path";
import { devices, expect, test } from "@playwright/test";

const screenshotDirectory = process.env.STATIC_ARTIFACT_SCREENSHOTS;
const expectedDigest = process.env.STATIC_ARTIFACT_DIGEST;
const viewports = {
  desktop: { viewport: { width: 1440, height: 900 } },
  phone: { ...devices["Pixel 7"] },
};


function collectPageFailures(page) {
  const failures = [];
  page.on("console", (message) => {
    if (message.type() === "error") failures.push(`console: ${message.text()}`);
  });
  page.on("pageerror", (error) => failures.push(`page: ${error.message}`));
  page.on("requestfailed", (request) => {
    failures.push(`request: ${request.url()} ${request.failure()?.errorText || "failed"}`);
  });
  page.on("response", (response) => {
    if (response.status() >= 400) failures.push(`${response.status()} ${response.url()}`);
  });
  return failures;
}


async function capture(page, testInfo, name) {
  const target = screenshotDirectory
    ? path.join(screenshotDirectory, `sentryinsight-${name}.png`)
    : testInfo.outputPath(`${name}.png`);
  await page.screenshot({ path: target, fullPage: true });
}


async function readReportMetadata(page) {
  return JSON.parse(await page.locator("#report-metadata").textContent());
}


async function horizontalOverflow(page) {
  return page.evaluate(
    () => document.documentElement.scrollWidth - document.documentElement.clientWidth,
  );
}


test("the listener serves this SentryInsight artifact", async ({ request }) => {
  const response = await request.get("/index.html");
  expect(response.ok()).toBeTruthy();
  const identity = response.headers()["x-static-artifact"] || "";
  expect(identity).toMatch(/^SentryInsight [0-9a-f]{64}$/);
  if (expectedDigest) expect(identity).toBe(`SentryInsight ${expectedDigest}`);
  expect(await response.text()).toContain("SentryInsight");
});


for (const [name, options] of Object.entries(viewports)) {
  test(`current and archived reports render from the artifact on ${name}`, async ({ browser, request }, testInfo) => {
    const context = await browser.newContext({ ...options, colorScheme: "light", locale: "en-US", timezoneId: "UTC" });
    const page = await context.newPage();
    const failures = collectPageFailures(page);
    const manifest = await (await request.get("/reports/index.json")).json();

    await page.goto("/");
    const metadata = await readReportMetadata(page);
    await expect(page.locator("button.finding-disclosure")).toHaveCount(metadata.finding_count);
    for (const title of await page.locator(".finding-title").all()) {
      await expect(title).toBeVisible();
      const name = (await title.innerText()).replace(/CVE-\d{4}-\d{4,}/gi, "");
      expect(name).toMatch(/\p{L}/u);
    }
    expect(await horizontalOverflow(page)).toBeLessThanOrEqual(1);
    await capture(page, testInfo, `current-${name}`);

    const archived = manifest.reports[0];
    await page.goto(`/reports/${archived.html_path}`);
    await expect(page.locator(".report-frozen")).toHaveText("· Archived snapshot");
    await expect(page.locator("button.finding-disclosure")).toHaveCount(archived.finding_count);
    expect(await horizontalOverflow(page)).toBeLessThanOrEqual(1);
    await capture(page, testInfo, `archive-${archived.report_date}-${name}`);

    await page.goto("/reports/");
    await expect(page.locator(".archive-list article")).toHaveCount(manifest.reports.length);
    expect(failures).toEqual([]);
    await context.close();
  });
}


test("the current report is readable without JavaScript", async ({ browser }, testInfo) => {
  const context = await browser.newContext({ javaScriptEnabled: false });
  const page = await context.newPage();
  const response = await page.goto("/");
  expect(response?.ok()).toBeTruthy();
  const metadata = await readReportMetadata(page);

  const headings = page.locator("h3[id]");
  expect(await headings.count()).toBeGreaterThanOrEqual(metadata.finding_count);
  await expect(page.locator(`h3#${metadata.findings[0].slug}`)).toBeVisible();
  await capture(page, testInfo, "current-no-js");
  await context.close();
});


test("finding disclosure and the CVE handoff work from the artifact", async ({ page }) => {
  const failures = collectPageFailures(page);
  await page.goto("/index.html");
  const metadata = await readReportMetadata(page);
  const first = page.locator(`h3#${metadata.findings[0].slug} button.finding-disclosure`);
  await expect(first).toHaveAttribute("aria-expanded", "true");
  await first.click();
  await expect(first).toHaveAttribute("aria-expanded", "false");
  await first.click();
  await expect(first).toHaveAttribute("aria-expanded", "true");

  const finding = metadata.findings.find((candidate) => candidate.cve_ids.length > 0);
  expect(finding).toBeTruthy();
  const fragment = `#${finding.cve_ids[0].toLowerCase()}`;
  await page.goto(`/index.html${fragment}`);
  const heading = page.locator(`h3#${finding.slug}`);
  await expect(heading).toHaveAttribute("data-handoff-match", "true");
  await expect(heading.locator("button.finding-disclosure")).toBeFocused();
  await expect(page.locator("#handoff-status")).toContainText(`Opened finding for ${finding.cve_ids[0]}`);
  expect(failures).toEqual([]);
});


test("an archived CVE anchor lands beside its finding", async ({ page, request }) => {
  const manifest = await (await request.get("/reports/index.json")).json();
  const archived = manifest.reports.find((report) => report.cve_count > 0);
  expect(archived).toBeTruthy();
  await page.goto(`/reports/${archived.html_path}`);
  const metadata = await readReportMetadata(page);
  const finding = metadata.findings.find((candidate) => candidate.cve_ids.length > 0);
  await page.goto(`/reports/${archived.html_path}#${finding.cve_ids[0].toLowerCase()}`);
  await expect(page.locator(`#${finding.cve_ids[0].toLowerCase()}`)).toHaveCount(1);
  await expect(page.locator(`h3#${finding.slug}`)).toBeInViewport();
  const disclosure = page.locator(`h3#${finding.slug} button.finding-disclosure`);
  await disclosure.click();
  await expect(disclosure).toHaveAttribute("aria-expanded", "false");
  const oldFragment = `finding-${finding.cve_ids[0].toLowerCase()}`;
  await page.evaluate((fragment) => { window.location.hash = fragment; }, oldFragment);
  await expect(page.locator(`#${oldFragment}`)).toHaveCount(1);
  await expect(disclosure).toHaveAttribute("aria-expanded", "true");
  await expect(page.locator(`h3#${finding.slug}`)).toBeInViewport();
});
