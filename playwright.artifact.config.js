// Reader acceptance for a built static artifact, separate from the packaged-output
// suite in playwright.config.js. Requires STATIC_ARTIFACT_STORE.
import { defineConfig } from "@playwright/test";

const port = process.env.STATIC_ARTIFACT_PORT || "4175";
const store = process.env.STATIC_ARTIFACT_STORE;
const python = process.env.STATIC_ARTIFACT_PYTHON || "python3";

if (!store) {
  throw new Error(
    "STATIC_ARTIFACT_STORE must name a store built by scripts/build_static_artifact.py",
  );
}

export default defineConfig({
  testDir: "tests/artifact_browser",
  outputDir: "test-results/artifact-playwright",
  reporter: [["line"]],
  workers: 1,
  use: {
    baseURL: `http://127.0.0.1:${port}`,
    browserName: "chromium",
    colorScheme: "light",
    locale: "en-US",
    timezoneId: "UTC",
  },
  webServer: {
    command: `${python} -B scripts/serve_static_artifact.py --store ${JSON.stringify(store)} --port ${port}`,
    url: `http://127.0.0.1:${port}/index.html`,
    reuseExistingServer: false,
  },
});
