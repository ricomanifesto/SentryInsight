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

**LangGraph**: Orchestrates workflow state and conditional logic
**FastMCP**: Code organization with decorators for RSS tools
**LangChain**: AI model integration and text processing
**Anthropic Claude**: Content analysis and report generation

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Add Anthropic API key:
   ```bash
   echo "ANTHROPIC_API_KEY=your-api-key-here" > .env
   ```

3. Configure feeds and output paths in `config/config.json`

## Usage

```bash
python main.py
```

Fetches articles, filters for exploitation content, analyzes threats, and saves reports to `index.md`.