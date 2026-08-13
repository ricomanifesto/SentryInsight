import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "tests/browser",
  outputDir: "test-results/playwright",
  reporter: [["line"]],
  use: {
    baseURL: "http://127.0.0.1:4173",
    browserName: "chromium",
    colorScheme: "light",
    locale: "en-US",
    timezoneId: "UTC",
  },
  webServer: {
    command: "python3 -m http.server 4173 --bind 127.0.0.1 --directory test-results/pages",
    url: "http://127.0.0.1:4173/index.html",
    reuseExistingServer: false,
  },
});
