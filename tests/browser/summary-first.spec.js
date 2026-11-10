import { expect, test } from "@playwright/test";

// The report opens on its own first section. Page-level material sits in a
// closing "About this report" section, reached from the metadata line and
// both section lists. Checked on the newest report and on archived reports of
// each format, at desktop and phone sizes, with and without scripts.

async function reportPaths(request) {
  const manifest = await (await request.get("/reports/index.json")).json();
  const newestArchived = manifest.reports[0].html_path; // a schema-5 report
  const oldest = manifest.reports[manifest.reports.length - 1].html_path; // schema 2
  return [
    ["current", "/index.html"],
    ["archived schema 5", `/reports/${newestArchived}`],
    ["archived schema 2", `/reports/${oldest}`],
  ];
}

function firstLine() {
  const title = document.querySelector("#report-content h1");
  // With scripts on, the existing summary card wraps the heading and its
  // paragraphs; the first element after the title is then that card.
  const next = title.nextElementSibling;
  const heading = next.tagName === "H2" ? next : next.firstElementChild;
  const paragraph = [...document.querySelectorAll("#report-content p")].find(
    (p) => heading.compareDocumentPosition(p) & Node.DOCUMENT_POSITION_FOLLOWING,
  );
  const range = document.createRange();
  range.selectNodeContents(paragraph);
  const line = range.getClientRects()[0];
  return {
    headingTag: heading.tagName,
    heading: heading.textContent.trim(),
    top: line.top,
    bottom: line.bottom,
    viewport: window.innerHeight,
    scrollY: window.scrollY,
  };
}

for (const [width, height] of [[1440, 900], [390, 844]]) {
  for (const javaScriptEnabled of [true, false]) {
    for (const colorScheme of ["light", "dark"]) {
      test(`the summary's first line is on the first screen at ${width}x${height}, scripts ${javaScriptEnabled ? "on" : "off"}, ${colorScheme}`, async ({ browser, request }) => {
        const context = await browser.newContext({ viewport: { width, height }, javaScriptEnabled, colorScheme });
        const page = await context.newPage();
        for (const [label, path] of await reportPaths(request)) {
          await page.goto(path);
          const line = await page.evaluate(firstLine);
          expect(line.headingTag, label).toBe("H2");
          expect(line.scrollY, label).toBe(0);
          expect(line.top, label).toBeGreaterThanOrEqual(0);
          expect(line.bottom, `${label}: ${line.heading}`).toBeLessThanOrEqual(line.viewport);
          const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
          expect(overflow, label).toBeLessThanOrEqual(0);
        }
        await context.close();
      });
    }
  }
}

test("nothing page-level precedes the first section, and About this report holds it once", async ({ page, request }) => {
  for (const [label, path] of await reportPaths(request)) {
    await page.goto(path);
    const layout = await page.evaluate(() => {
      const first = document.querySelector("#report-content h1").nextElementSibling;
      const before = (node) => node.compareDocumentPosition(first) & Node.DOCUMENT_POSITION_FOLLOWING;
      const about = document.querySelector("section.about-report");
      return {
        movedBefore: [...document.querySelectorAll('.report-method, [role="note"], #cve-history-summary')].filter(before).length,
        method: document.querySelectorAll(".report-method").length,
        methodInAbout: about.querySelectorAll(".report-method").length,
        notesOutsideAbout: [...document.querySelectorAll('[role="note"]')].filter((n) => !about.contains(n)).length,
        aboutHeading: about.querySelector("h2").textContent,
        aboutBeforeCoverage: (() => {
          const coverage = document.getElementById("source-coverage-and-review");
          return coverage ? Boolean(about.compareDocumentPosition(coverage) & Node.DOCUMENT_POSITION_FOLLOWING) : null;
        })(),
      };
    });
    expect(layout.movedBefore, label).toBe(0);
    expect([layout.method, layout.methodInAbout, layout.notesOutsideAbout], label).toEqual([1, 1, 0]);
    expect(layout.aboutHeading, label).toBe("About this report");
    if (layout.aboutBeforeCoverage !== null) expect(layout.aboutBeforeCoverage, label).toBe(true);
  }
});

test("keyboard: skip link, the About entry and the coverage notice link each land where they say", async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto("/index.html");
  await page.keyboard.press("Tab");
  await expect(page.locator(".skip-link")).toBeFocused();
  await page.keyboard.press("Enter");
  await expect(page).toHaveURL(/#report-content$/);

  const aboutId = await page.locator("section.about-report h2").getAttribute("id");
  const entry = page.locator(`.desktop-toc a[href="#${aboutId}"]`);
  await expect(entry).toHaveText("About this report");
  await entry.focus();
  await page.keyboard.press("Enter");
  await expect(page).toHaveURL(new RegExp(`#${aboutId}$`));
  await expect(page.locator(`[id="${aboutId}"]`)).toBeInViewport();

  const notice = page.locator("#source-coverage-notice a");
  if (await notice.count()) {
    await notice.focus();
    await page.keyboard.press("Enter");
    await expect(page).toHaveURL(/#source-coverage-and-review$/);
    await expect(page.locator("#source-coverage-and-review")).toBeInViewport();
  }

  const metaLink = page.locator(".report-date a.report-about");
  await expect(metaLink).toHaveText("AI-assisted · About this report");
  await expect(metaLink).toHaveAttribute("href", `#${aboutId}`);
});

test("the phone section list includes About this report in page order", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/index.html");
  const map = page.locator("details.mobile-toc");
  await map.locator("summary").click();
  const hrefs = await map.locator("nav a").evaluateAll((links) => links.map((a) => a.getAttribute("href").slice(1)));
  const order = await page.evaluate(() => [...document.querySelectorAll("#report-content h2, #report-content h3")].map((h) => h.id));
  expect(hrefs).toEqual(order);
  expect(hrefs).toContain(await page.locator("section.about-report h2").getAttribute("id"));
});
