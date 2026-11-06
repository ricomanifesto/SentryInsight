import { expect, test } from "@playwright/test";

async function cveFinding(page, metadata) {
  const current = metadata.findings.find((item) => item.cve_ids.length);
  if (current) return current;
  // A valid current report may contain campaigns without CVE identifiers.
  // Keep its title checks, then exercise bookmarks on a CVE-bearing archive.
  const archive = await (await page.request.get("/reports/index.json")).json();
  for (const entry of archive.reports) {
    if (!entry.cve_count) continue;
    await page.goto(`/reports/${entry.html_path}`);
    const archived = JSON.parse(await page.locator("#report-metadata").textContent());
    const finding = archived.findings.find((item) => item.cve_ids.length);
    if (finding) return finding;
  }
  return null;
}

for (const [name, viewport] of Object.entries({
  desktop: { width: 1440, height: 900 },
  phone: { width: 393, height: 851 },
})) {
  test(`descriptive titles and copied CVE heading links work on ${name}`, async ({ page }) => {
    await page.setViewportSize(viewport);
    await page.goto("/index.html");
    const metadata = JSON.parse(await page.locator("#report-metadata").textContent());
    const titles = page.locator(".finding-title");
    await expect(titles).toHaveCount(metadata.finding_count);
    for (const title of await titles.all()) {
      await expect(title).toBeVisible();
      const text = (await title.innerText()).replace(/CVE-\d{4}-\d{4,}/gi, "");
      expect(text).toMatch(/\p{L}/u);
    }

    const finding = await cveFinding(page, metadata);
    expect(finding).toBeTruthy();
    const heading = page.locator(`h3#${finding.slug}`);
    const disclosure = heading.locator("button.finding-disclosure");
    await disclosure.click();
    await expect(disclosure).toHaveAttribute("aria-expanded", "false");
    const oldFragment = `finding-${finding.cve_ids[0].toLowerCase()}`;
    await page.evaluate((fragment) => { window.location.hash = fragment; }, oldFragment);
    await expect(page.locator(`#${oldFragment}`)).toHaveCount(1);
    await expect(disclosure).toHaveAttribute("aria-expanded", "true");
    await expect(heading).toBeInViewport();
    await page.screenshot({ path: `test-results/screenshots/title-repair-${name}.png` });
  });
}
