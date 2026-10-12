import { expect, test } from "@playwright/test";

for (const width of [1440, 1024, 901, 900, 768, 390, 320]) {
  test(`keeps a five-CVE finding heading readable at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 1100 });
    await page.goto("/index.html");
    const heading = page.locator(".finding-heading").first();
    const cves = [76465, 76471, 76485, 76486, 76501].map(
      (number) => `CVE-2026-${number}`,
    );
    await heading.evaluate((element, cves) => {
      element.querySelector(".finding-title").textContent = cves.join(", ");
      const list = element.querySelector(".cve-list");
      const chip = list.querySelector(".cve-chip");
      list.replaceChildren(...cves.map((cve) => {
        const link = chip.cloneNode(true);
        link.textContent = cve;
        link.href = `https://nvd.nist.gov/vuln/detail/${cve}`;
        return link;
      }));
    }, cves);
    const geometry = await heading.evaluate((element) => {
      const title = element.querySelector(".finding-title");
      const support = element.querySelector(".finding-supporting");
      const titleBox = title.getBoundingClientRect();
      const supportBox = support.getBoundingClientRect();
      const row = element.getBoundingClientRect();
      const inside = (inner, outer) => inner.left >= outer.left - 1
        && inner.right <= outer.right + 1
        && inner.top >= outer.top - 1 && inner.bottom <= outer.bottom + 1;
      const range = document.createRange();
      range.selectNodeContents(title);
      return {
        titleWidth: titleBox.width,
        titleHeight: titleBox.height,
        titleLineHeight: parseFloat(getComputedStyle(title).lineHeight),
        titleFits: [...range.getClientRects()].every((rect) => inside(rect, titleBox)),
        supportFits: [...support.querySelectorAll(".badge, .cve-chip, .heading-anchor")]
          .every((child) => inside(child.getBoundingClientRect(), supportBox)),
        groupsFit: inside(titleBox, row) && inside(supportBox, row),
        groupsSeparate: titleBox.right <= supportBox.left + 1
          || titleBox.bottom <= supportBox.top + 1,
        scrollWidth: document.documentElement.scrollWidth,
        viewportWidth: document.documentElement.clientWidth,
      };
    });
    expect(geometry.titleWidth).toBeGreaterThan(150);
    expect(geometry.titleHeight).toBeLessThanOrEqual(geometry.titleLineHeight * 6);
    expect(geometry.titleFits).toBeTruthy();
    expect(geometry.supportFits).toBeTruthy();
    expect(geometry.groupsFit).toBeTruthy();
    expect(geometry.groupsSeparate).toBeTruthy();
    expect(geometry.scrollWidth).toBeLessThanOrEqual(geometry.viewportWidth);
    await expect(heading.locator(".finding-title")).toHaveText(cves.join(", "));
    await expect(heading.locator(".cve-chip")).toHaveText(cves);
    const disclosure = heading.locator("button.finding-disclosure");
    await disclosure.click();
    await expect(disclosure).toHaveAttribute("aria-expanded", "false");
    await disclosure.click();
    await expect(disclosure).toHaveAttribute("aria-expanded", "true");
  });
}
