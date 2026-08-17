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
  const cveLabel = metadata.complete_cve_count === 1 ? "CVE" : "CVEs";
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
  await expect(page.locator("h1 time")).toHaveAttribute(
    "datetime",
    metadata.report_date,
  );
  await expect(page.locator("h1 .report-kicker")).toHaveText("Exploitation Report");
  const editionLabel = new Intl.DateTimeFormat("en-US", {
    timeZone: "UTC",
    month: "long",
    day: "numeric",
    year: "numeric",
  }).format(new Date(`${metadata.report_date}T00:00:00Z`));
  await expect(
    page.getByRole("heading", {
      level: 1,
      name: `Exploitation Report ${editionLabel}`,
    }),
  ).toBeVisible();
  const sectionCount = await page.locator("#report-content h2, #report-content h3").count();
  await expect(page.locator(".desktop-toc a")).toHaveCount(sectionCount);
  await expect(page.locator(".finding-heading .badge")).toHaveCount(
    metadata.finding_count * 3,
  );
  await expect(page.locator("html")).toHaveAttribute("data-theme", "light");
  await expect(page.locator(".brand-logo-light")).toBeVisible();
  await expect(page.locator(".brand-logo-dark")).toBeHidden();
  await expect(page.getByText(reportShape(metadata))).toBeVisible();
  await expect(page.getByText("AI-assisted", { exact: false })).toBeVisible();
  const reportingCount = metadata.findings.reduce(
    (count, finding) => count + finding.reporting.length,
    0,
  );
  await expect(page.locator(".finding-reporting")).toHaveCount(metadata.finding_count);
  await expect(page.locator(".reporting-source")).toHaveCount(reportingCount);
  await expect(page.locator(".reporting-context")).toHaveCount(reportingCount);
  await expect(page.locator(".report-method a")).toHaveAttribute(
    "href",
    metadata.digest_issue_url,
  );
  await expect(page.locator(".reporting-source").first()).toHaveAttribute(
    "rel",
    "noopener noreferrer",
  );

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


test("defaults to light when the operating system prefers dark", async ({ browser }) => {
  const context = await browser.newContext({ colorScheme: "dark" });
  const page = await context.newPage();

  await page.goto("/index.html");

  await expect(page.locator("html")).toHaveAttribute("data-theme", "light");
  await expect(page.locator(".brand-logo-light")).toBeVisible();
  await expect(page.locator(".brand-logo-dark")).toBeHidden();
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


test("receives a CVE handoff at the matching finding and focuses its control", async ({ page }) => {
  const failures = collectPageFailures(page);
  await page.goto("/index.html");
  const metadata = await readReportMetadata(page);
  const finding = metadata.findings.find((candidate) => candidate.cve_ids.length > 0);
  expect(finding).toBeTruthy();
  const cve = finding.cve_ids[0];
  const fragment = `#${cve.toLowerCase()}`;

  await page.goto(`/index.html${fragment}`);

  const heading = page.locator(`h3#${finding.slug}`);
  const disclosure = heading.locator("button.finding-disclosure");
  await expect(page).toHaveURL(new RegExp(`${fragment}$`, "i"));
  await expect(heading).toHaveAttribute("data-handoff-match", "true");
  await expect(disclosure).toBeFocused();
  await expect(page.locator("#handoff-status")).toContainText(`Opened finding for ${cve}`);
  await page.screenshot({
    path: "test-results/screenshots/report-cve-handoff.png",
    fullPage: true,
  });
  expect(failures).toEqual([]);
});


test("lands a CVE handoff beside its finding without JavaScript", async ({ browser }) => {
  const context = await browser.newContext({ javaScriptEnabled: false });
  const page = await context.newPage();
  await page.goto("/index.html");
  const metadata = await readReportMetadata(page);
  const finding = metadata.findings.find((candidate) => candidate.cve_ids.length > 0);
  expect(finding).toBeTruthy();
  const cve = finding.cve_ids[0];

  await page.goto(`/index.html#${cve.toLowerCase()}`);

  await expect(page).toHaveURL(new RegExp(`#${cve.toLowerCase()}$`, "i"));
  await expect(page.locator(`#${cve.toLowerCase()}`)).toHaveCount(1);
  await expect(page.locator(`h3#${finding.slug}`)).toBeInViewport();
  await context.close();
});


test("keeps an unmatched CVE handoff honest at the current-report front door", async ({ page }) => {
  const failures = collectPageFailures(page);

  await page.goto("/index.html#cve-2099-9999");

  await expect(page.locator("#handoff-status")).toContainText(
    "No current finding matches CVE-2099-9999. Showing the current report.",
  );
  await expect(page.locator('.finding-heading[data-handoff-match="true"]')).toHaveCount(0);
  await expect(page.getByRole("heading", { level: 1 })).toBeVisible();
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


test("uses an editorial hierarchy instead of repeated outlined cards", async ({ page }) => {
  const failures = collectPageFailures(page);
  await page.goto("/index.html");

  const styles = await page.evaluate(() => {
    const borderWidths = (selector) => {
      const style = getComputedStyle(document.querySelector(selector));
      return [
        style.borderTopWidth,
        style.borderRightWidth,
        style.borderBottomWidth,
        style.borderLeftWidth,
      ];
    };
    return {
      actions: borderWidths(".site-actions a"),
      executiveSummary: borderWidths(".executive-summary-card"),
      findingHeading: borderWidths(".finding-heading"),
      findingBody: borderWidths(".finding-body"),
      reporting: borderWidths(".finding-reporting"),
      badge: borderWidths(".badge"),
    };
  });

  expect(styles.actions).toEqual(["0px", "0px", "0px", "0px"]);
  expect(styles.executiveSummary).toEqual(["0px", "0px", "0px", "0px"]);
  expect(styles.findingHeading).toEqual(["2px", "0px", "0px", "0px"]);
  expect(styles.findingBody).toEqual(["0px", "0px", "0px", "0px"]);
  expect(styles.reporting).toEqual(["0px", "0px", "0px", "3px"]);
  expect(styles.badge).toEqual(["0px", "0px", "0px", "0px"]);
  expect(failures).toEqual([]);
});


test("uses a disciplined native type system and keeps disclosure controls together", async ({ page }) => {
  const failures = collectPageFailures(page);
  await page.goto("/index.html");

  const styles = await page.evaluate(() => {
    const disclosure = document.querySelector(".finding-disclosure");
    const icon = disclosure.querySelector(".disclosure-icon").getBoundingClientRect();
    const title = disclosure.querySelector(".finding-title").getBoundingClientRect();
    return {
      bodyFamily: getComputedStyle(document.body).fontFamily,
      generatedSize: getComputedStyle(document.querySelector(".report-generated")).fontSize,
      badgeSize: getComputedStyle(document.querySelector(".badge")).fontSize,
      iconBeforeTitle: icon.right <= title.left + 1,
      metadataChildren: document.querySelector(".report-date").children.length,
    };
  });

  expect(styles.bodyFamily).not.toContain("Inter");
  expect(styles.generatedSize).toBe("14px");
  expect(styles.badgeSize).toBe("14px");
  expect(styles.iconBeforeTitle).toBeTruthy();
  expect(styles.metadataChildren).toBe(2);
  expect(failures).toEqual([]);
});


test("aligns the report chrome with the centered reading shell", async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto("/index.html");

  const bounds = await page.evaluate(() => {
    const contentBounds = (selector) => {
      const element = document.querySelector(selector);
      const rect = element.getBoundingClientRect();
      const styles = getComputedStyle(element);
      return {
        left: rect.left + Number.parseFloat(styles.paddingLeft),
        right: rect.right - Number.parseFloat(styles.paddingRight),
      };
    };
    const shell = document.querySelector(".page-shell").getBoundingClientRect();
    return {
      shell: { left: shell.left, right: shell.right },
      header: contentBounds(".site-header"),
      date: contentBounds(".report-date"),
      method: contentBounds(".report-method"),
    };
  });

  for (const region of [bounds.header, bounds.date, bounds.method]) {
    expect(region.left).toBeCloseTo(bounds.shell.left, 0);
    expect(region.right).toBeCloseTo(bounds.shell.right, 0);
  }
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
  const headerBox = await page.locator(".site-header").boundingBox();
  expect(headerBox?.height).toBeLessThanOrEqual(100);
  const compactChrome = await page.evaluate(() => ({
    methodLabelDisplay: getComputedStyle(
      document.querySelector(".report-method strong"),
    ).display,
    shapeWhiteSpace: getComputedStyle(document.querySelector(".report-shape")).whiteSpace,
  }));
  expect(compactChrome.methodLabelDisplay).toBe("inline");
  expect(compactChrome.shapeWhiteSpace).toBe("nowrap");
  await expect(page.locator('.site-header a[href$=".md"]')).toHaveCount(0);
  await expect(page.locator('.site-footer a[href$=".md"]')).toHaveCount(1);

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
  await expect(page.locator(".archive-context")).toContainText(
    "Reports accumulate through daily rollovers",
  );
  await expect(page.getByText(`${reportCount} ${reportLabel} available`)).toBeVisible();
  if (reportCount === 0) {
    await expect(page.getByText("No archived reports yet")).toBeVisible();
  } else {
    await expect(page.locator(".archive-list article")).toHaveCount(reportCount);
  }
  expect(failures).toEqual([]);
});


test("keeps a relative clock only on the current report", async ({ page, request }) => {
  const failures = collectPageFailures(page);
  await page.goto("/index.html");
  await expect(page.locator("#report-age")).toContainText("updated");
  await expect(page.locator(".report-frozen")).toHaveCount(0);

  const manifestResponse = await request.get("/reports/index.json");
  expect(manifestResponse.ok()).toBeTruthy();
  const manifest = await manifestResponse.json();
  expect(manifest.reports.length).toBeGreaterThan(0);
  await page.goto(`/reports/${manifest.reports[0].html_path}`);
  await expect(page.locator("#report-age")).toHaveCount(0);
  await expect(page.locator(".report-frozen")).toHaveText("· Archived snapshot");
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
