# SentryInsight

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-lockup-dark.png">
    <img src="assets/logo-lockup-light.png" alt="SentryInsight" width="440">
  </picture>
</div>

SentryInsight reads security news and publishes a report about vulnerabilities that are being exploited or need urgent review.

**[Read the latest exploitation report](https://ricomanifesto.github.io/SentryInsight/)**

## What the Report Answers

- What is being exploited?
- Which products and systems are affected?
- How does the attack work?
- Which CVEs and source articles support the finding?
- What should a defender review next?

Each published report is available as a web page and Markdown file. Older reports remain in the [dated archive](https://ricomanifesto.github.io/SentryInsight/reports/).

## How It Works

1. SentryInsight reads the RSS feed from [SentryDigest](https://github.com/ricomanifesto/SentryDigest).
2. It filters for exploitation-related articles and builds a report with LangGraph.
3. It uses OpenRouter when `OPENROUTER_API_KEY` is set. Local development can use an OpenCode server instead.
4. It writes the canonical report to `index.md`, builds the matching static pages, and archives the previous report when the report date changes.
5. Validation must pass before the GitHub Pages artifact can be deployed.

Every current finding cites one or more SentryDigest article identities. Those identities follow SentryDigest's [reporting identity contract](https://github.com/ricomanifesto/SentryDigest/blob/main/contracts/README.md), which keeps links stable across all three reporting projects.

## Run It Locally

SentryInsight requires Python 3.11 and [`uv`](https://docs.astral.sh/uv/):

```bash
uv sync --group dev --frozen
```

For direct OpenRouter access:

```bash
export OPENROUTER_API_KEY=...
export SENTRYINSIGHT_MODEL=openrouter/nvidia/nemotron-3-ultra-550b-a55b:free
uv run python main.py
```

The default model is set in `config/config.json`. `SENTRYINSIGHT_MODEL` overrides it for one environment.

To use a local OpenCode server instead, leave `OPENROUTER_API_KEY` unset:

```bash
opencode serve --port 4096
uv run python main.py
```

Set `OPENCODE_BASE_URL` if the server is not listening on `http://127.0.0.1:4096`.

Report generation fetches live feeds and calls the configured model service. Local validation does neither.

## Validation

Install Chromium once, then run the full local gate:

```bash
npm ci
npx playwright install chromium
bash scripts/local_validation.sh
```

The script installs locked Python and Node dependencies, runs linting, formatting, type checks, and tests, verifies the report and packaged Pages files, and exercises the current and archived pages in Chromium. Browser checks cover accessibility, responsive layouts, stable CVE links, and light and dark themes.

## Publishing

- `.github/workflows/generate-report.yml` runs after a SentryDigest update, once daily as a backup, or by manual trigger.
- `.github/workflows/validate.yml` checks pushes and pull requests.
- `.github/workflows/deploy-pages.yml` publishes only after validation succeeds on `main`.

The public Pages package contains only the finished report, archive, assets, sitemap, and the versioned reporting contract.
