# SentryInsight

## AI-Powered Cybersecurity Exploitation Analysis

SentryInsight automatically analyzes cybersecurity news feeds to identify and report on active exploitations, zero-day vulnerabilities, and critical security threats using advanced AI analysis powered by Model-Channel-Protocol (MCP) architecture.

[![Latest Exploitation Report](https://img.shields.io/badge/View-Latest%20Report-blue)](https://ricomanifesto.github.io/SentryInsight/)

## Technical Architecture

SentryInsight uses a modern LangGraph-based MCP architecture:

- **Model**: OpenAI's GPT models provide the intelligence for analysis
- **Channel**: LangGraph workflow orchestrates the data flow between components
- **Protocol**: Specialized tools handle RSS parsing and content transformation

## Integration with SentryDigest

SentryInsight is designed to work seamlessly with the [SentryDigest](https://github.com/ricomanifesto/SentryDigest) project. When SentryDigest updates its feed, it automatically triggers SentryInsight to generate a new analysis.

## License

MIT

---

*SentryInsight: Advanced cybersecurity intelligence through AI-driven MCP architecture*