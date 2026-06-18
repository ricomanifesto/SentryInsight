# SentryInsight

<div align="center">
  <img src="assets/logo.png" alt="SentryInsight Logo" width="400"/>
</div>

Automated cybersecurity threat intelligence that monitors RSS feeds and generates exploitation reports using AI analysis.

[![Latest Exploitation Report](https://img.shields.io/badge/View-Latest%20Report-blue)](https://ricomanifesto.github.io/SentryInsight/)

## Features

- Monitors security RSS feeds for exploitation content
- Extracts and correlates CVE mentions
- Generates reports with executive summaries, affected systems, attack vectors, and threat actor activities
- Integrates with [SentryDigest](https://github.com/ricomanifesto/SentryDigest) for automated analysis triggers

## Architecture

- **LangGraph**: Orchestrates workflow state and conditional logic
- **FastMCP**: Code organization with decorators for RSS tools
- **OpenCode**: Provider-switchable report generation

## Setup

1. Install dependencies:
   ```bash
   uv sync --group dev
   ```

2. Start an OpenCode server with access to your preferred model provider:
   ```bash
   opencode serve --port 4096
   ```

3. Configure feeds, output paths, and the default model in `config/config.json`.
   Model IDs use `provider/model` format. Override the model for one
   environment with:
   ```bash
   export SENTRYINSIGHT_MODEL=openrouter/nvidia/nemotron-3-ultra-550b-a55b:free
   ```
   If OpenCode is not listening on `http://127.0.0.1:4096`, set:
   ```bash
   export OPENCODE_BASE_URL=http://127.0.0.1:4096
   ```

## Usage

```bash
uv run python main.py
```

Fetches articles, filters for exploitation content, analyzes threats, and saves reports to `index.md`.

Validate a generated report before publishing:

```bash
bash scripts/local_validation.sh
```
