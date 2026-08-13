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


test("renders trustworthy content without JavaScript", async ({ browser }) => {
  const context = await browser.newContext({ javaScriptEnabled: false });
  const page = await context.newPage();
  const response = await page.goto("/index.html");

  expect(response?.ok()).toBeTruthy();
  await expect(page.getByText("Report for Thursday, August 13, 2026")).toBeVisible();
  await expect(page.getByRole("heading", { name: "Executive Summary" })).toBeVisible();
  await expect(page.getByText("Active exploitation campaigns have intensified")).toBeVisible();
  await expect(page.locator(".desktop-toc a")).toHaveCount(14);

  await context.close();
});


test("uses independent accessible finding controls", async ({ page }) => {
  const failures = collectPageFailures(page);
  const response = await page.goto("/index.html");
  expect(response?.ok()).toBeTruthy();

  const disclosures = page.locator("button.finding-disclosure");
  await expect(disclosures).toHaveCount(9);
  const first = disclosures.filter({ hasText: "Microsoft SharePoint" });
  await expect(first).toHaveCount(1);
  await expect(first).toHaveAttribute("aria-expanded", "true");
  const bodyId = await first.getAttribute("aria-controls");
  expect(bodyId).toBeTruthy();

  await first.press("Enter");
  await expect(first).toHaveAttribute("aria-expanded", "false");
  await expect(page.locator(`#${bodyId}`)).toBeHidden();
  await first.press("Enter");
  await expect(first).toHaveAttribute("aria-expanded", "true");

  const sharePointHeading = page.locator(
    "h3#microsoft-sharepoint-authentication-bypass-cve-2026-55040"
  );
  const sharePointCve = sharePointHeading.locator("a.cve-chip");
  await expect(sharePointCve).toHaveCount(1);
  await sharePointCve.evaluate((link) => {
    link.addEventListener("click", (event) => event.preventDefault(), { once: true });
  });
  await sharePointCve.click();
  await expect(first).toHaveAttribute("aria-expanded", "true");

  const anchor = sharePointHeading.locator("a.heading-anchor");
  await expect(anchor).toHaveCount(1);
  await anchor.click();
  await expect(first).toHaveAttribute("aria-expanded", "true");
  await expect(page.locator("#copy-toast")).toContainText("Link copied");

  const badges = sharePointHeading.locator(".badge");
  await expect(badges).toHaveCount(3);
  await expect(badges).toHaveText([
    "Critical",
    "Active exploitation",
    "Patch",
  ]);
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

  const map = page.locator("details.mobile-toc");
  await expect(map).toBeVisible();
  await map.locator("summary").click();
  await expect(map.locator("nav a")).toHaveCount(14);
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


test("renders an honest empty archive before the first rollover", async ({ page }) => {
  const failures = collectPageFailures(page);
  const response = await page.goto("/reports/");
  expect(response?.ok()).toBeTruthy();

  await expect(page.getByRole("heading", { name: "Report archive" })).toBeVisible();
  await expect(page.getByText("0 reports available")).toBeVisible();
  await expect(page.getByText("No archived reports yet")).toBeVisible();
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
