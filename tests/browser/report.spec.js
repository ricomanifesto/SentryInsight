import { expect, test } from "@playwright/test";


function collectPageFailures(page) {
  const failures = [];
  page.on("console", (message) => {
    if (message.type() === "error") failures.push(`console: ${message.text()}`);
  });
  page.on("pageerror", (error) => failures.push(`page: ${error.message}`));
  page.on("requestfailed", (request) => {
    failures.push(`request: ${request.url()} ${request.failure()?.errorText || "failed"}`);
  });
  return failures;
}


async function readReportMetadata(page) {
  return JSON.parse(await page.locator("#report-metadata").textContent());
}


function reportShape(metadata) {
  const findingLabel = metadata.finding_count === 1 ? "finding" : "findings";
  const cveLabel =
    metadata.complete_cve_count === 1 ? "complete CVE ID" : "complete CVE IDs";
  return `${metadata.finding_count} ${findingLabel} · ${metadata.complete_cve_count} ${cveLabel}`;
}


test("renders trustworthy content without JavaScript", async ({ browser }) => {
  const context = await browser.newContext({
    javaScriptEnabled: false,
    colorScheme: "dark",
  });
  const page = await context.newPage();
  const response = await page.goto("/index.html");

  expect(response?.ok()).toBeTruthy();
  await expect(page.getByRole("heading", { name: "Executive Summary" })).toBeVisible();
  const metadata = await readReportMetadata(page);
  await expect(page.locator(".report-date > time")).toHaveAttribute(
    "datetime",
    metadata.report_date,
  );
  const sectionCount = await page.locator("#report-content h2, #report-content h3").count();
  await expect(page.locator(".desktop-toc a")).toHaveCount(sectionCount);
  await expect(page.locator(".finding-heading .badge")).toHaveCount(
    metadata.finding_count * 3,
  );
  await expect(page.locator(".brand-logo-dark")).toBeVisible();
  await expect(page.locator(".brand-logo-light")).toBeHidden();
  await expect(page.getByText(reportShape(metadata))).toBeVisible();
  await expect(page.getByText("AI-assisted", { exact: false })).toBeVisible();

  await context.close();
});


test("applies a stored dark theme before the deferred client script", async ({ browser }) => {
  const context = await browser.newContext({ colorScheme: "light" });
  const page = await context.newPage();
  await page.addInitScript(() => {
    localStorage.setItem("sentryinsight-theme", "dark");
  });
  await page.route("**/assets/report.js?*", (route) => route.abort());

  await page.goto("/index.html");

  await expect(page.locator("html")).toHaveAttribute("data-theme", "dark");
  await expect(page.locator(".brand-logo-dark")).toBeVisible();
  await expect(page.locator(".brand-logo-light")).toBeHidden();
  await context.close();
});


test("uses independent accessible finding controls", async ({ page }) => {
  const failures = collectPageFailures(page);
  const response = await page.goto("/index.html");
  expect(response?.ok()).toBeTruthy();
  const metadata = await readReportMetadata(page);
  const firstFinding = metadata.findings[0];

  const disclosures = page.locator("button.finding-disclosure");
  await expect(disclosures).toHaveCount(metadata.finding_count);
  const first = page.locator(`h3#${firstFinding.slug} button.finding-disclosure`);
  await expect(first).toHaveCount(1);
  await expect(first).toHaveAttribute("aria-expanded", "true");
  const bodyId = await first.getAttribute("aria-controls");
  expect(bodyId).toBeTruthy();

  await first.press("Enter");
  await expect(first).toHaveAttribute("aria-expanded", "false");
  await expect(page.locator(`#${bodyId}`)).toBeHidden();
  await first.press("Enter");
  await expect(first).toHaveAttribute("aria-expanded", "true");

  const firstHeading = page.locator(`h3#${firstFinding.slug}`);
  const cveFinding = metadata.findings.find((finding) => finding.cve_ids.length > 0);
  if (cveFinding) {
    const cveHeading = page.locator(`h3#${cveFinding.slug}`);
    const cveDisclosure = cveHeading.locator("button.finding-disclosure");
    const cveLink = cveHeading.locator("a.cve-chip");
    await expect(cveLink).toHaveCount(cveFinding.cve_ids.length);
    const firstCveLink = cveLink.filter({ hasText: cveFinding.cve_ids[0] });
    await firstCveLink.evaluate((link) => {
      link.addEventListener("click", (event) => event.preventDefault(), { once: true });
    });
    await firstCveLink.click();
    await expect(cveDisclosure).toHaveAttribute("aria-expanded", "true");
  }

  const anchor = firstHeading.locator("a.heading-anchor");
  await expect(anchor).toHaveCount(1);
  await anchor.click();
  await expect(first).toHaveAttribute("aria-expanded", "true");
  await expect(page.locator("#copy-toast")).toContainText("Link copied");

  const badges = firstHeading.locator(".badge");
  await expect(badges).toHaveCount(3);
  await expect(
    firstHeading.locator(`.badge-severity[data-value="${firstFinding.severity}"]`),
  ).toHaveCount(1);
  await expect(
    firstHeading.locator(
      `.badge-exploitation-status[data-value="${firstFinding.exploitation_status}"]`,
    ),
  ).toHaveCount(1);
  await expect(
    firstHeading.locator(`.badge-action[data-value="${firstFinding.action}"]`),
  ).toHaveCount(1);
  expect(failures).toEqual([]);
});


test("keeps section maps clean and theme state discoverable", async ({ page }) => {
  const failures = collectPageFailures(page);
  await page.goto("/index.html");

  const tocText = await page.locator(".desktop-toc nav").innerText();
  expect(tocText).not.toContain("Active exploitation");
  expect(tocText).not.toContain("▼");

  const theme = page.locator("#theme-toggle");
  await expect(theme).toHaveAttribute("aria-pressed", "false");
  await expect(theme).toHaveText("Dark theme");
  await page.screenshot({
    path: "test-results/screenshots/report-desktop-light.png",
    fullPage: true,
  });
  await theme.click();
  await expect(theme).toHaveAttribute("aria-pressed", "true");
  await expect(theme).toHaveText("Light theme");
  await expect(page.locator("html")).toHaveAttribute("data-theme", "dark");
  await expect(page.locator(".brand-logo-dark")).toBeVisible();
  await expect(page.locator(".brand-logo-light")).toBeHidden();

  await page.screenshot({
    path: "test-results/screenshots/report-desktop-dark.png",
    fullPage: true,
  });
  expect(failures).toEqual([]);
});


test("provides a mobile section map without horizontal overflow", async ({ page }) => {
  const failures = collectPageFailures(page);
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/index.html");
  const sectionCount = await page
    .locator("#report-content h2, #report-content h3")
    .count();

  const map = page.locator("details.mobile-toc");
  await expect(map).toBeVisible();
  await map.locator("summary").click();
  await expect(map.locator("nav a")).toHaveCount(sectionCount);
  const dimensions = await page.evaluate(() => ({
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
  }));
  expect(dimensions.scrollWidth).toBeLessThanOrEqual(dimensions.clientWidth);

  await page.screenshot({
    path: "test-results/screenshots/report-mobile-light.png",
    fullPage: true,
  });
  expect(failures).toEqual([]);
});


test("renders an archive that matches its manifest", async ({ page, request }) => {
  const failures = collectPageFailures(page);
  const response = await page.goto("/reports/");
  expect(response?.ok()).toBeTruthy();
  const manifestResponse = await request.get("/reports/index.json");
  expect(manifestResponse.ok()).toBeTruthy();
  const manifest = await manifestResponse.json();
  const reportCount = manifest.reports.length;
  const reportLabel = reportCount === 1 ? "report" : "reports";

  await expect(page.getByRole("heading", { name: "Report archive" })).toBeVisible();
  await expect(page.getByText(`${reportCount} ${reportLabel} available`)).toBeVisible();
  if (reportCount === 0) {
    await expect(page.getByText("No archived reports yet")).toBeVisible();
  } else {
    await expect(page.locator(".archive-list article")).toHaveCount(reportCount);
  }
  expect(failures).toEqual([]);
});


test("renders a tablet dark-mode report without overflow", async ({ page }) => {
  const failures = collectPageFailures(page);
  await page.setViewportSize({ width: 768, height: 1024 });
  await page.goto("/index.html");
  await page.locator("#theme-toggle").click();

  await expect(page.locator("details.mobile-toc")).toBeVisible();
  await expect(page.locator(".desktop-toc")).toBeHidden();

  const dimensions = await page.evaluate(() => ({
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
  }));
  expect(dimensions.scrollWidth).toBeLessThanOrEqual(dimensions.clientWidth);
  await page.screenshot({
    path: "test-results/screenshots/report-tablet-dark.png",
    fullPage: true,
  });
  expect(failures).toEqual([]);
});


test("renders a phone dark-mode report", async ({ page }) => {
  const failures = collectPageFailures(page);
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/index.html");
  await page.locator("#theme-toggle").click();
  await page.screenshot({
    path: "test-results/screenshots/report-mobile-dark.png",
    fullPage: true,
  });
  expect(failures).toEqual([]);
});
