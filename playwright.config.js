import { defineConfig } from "@playwright/test";

const port = process.env.PLAYWRIGHT_PORT || "4173";

export default defineConfig({
  testDir: "tests/browser",
  outputDir: "test-results/playwright",
  reporter: [["line"]],
  use: {
    baseURL: `http://127.0.0.1:${port}`,
    browserName: "chromium",
    colorScheme: "light",
    locale: "en-US",
    timezoneId: "UTC",
  },
  webServer: {
    command: `python3 -m http.server ${port} --bind 127.0.0.1 --directory test-results/pages`,
    url: `http://127.0.0.1:${port}/index.html`,
    reuseExistingServer: false,
  },
});
