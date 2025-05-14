# SentryInsight

## Automated Cybersecurity Exploitation Intelligence

SentryInsight is a sophisticated cybersecurity analysis tool that automatically monitors, analyzes, and reports on active exploitation threats from security RSS feeds. The system leverages AI to identify critical vulnerabilities, exploitation patterns, and threat actor activities.

![SentryInsight](https://img.shields.io/badge/Security-Analysis-blue)

## 🔍 Key Features

- **Automatic Feed Monitoring**: Continuously fetches security news from RSS feeds
- **Exploitation Detection**: Identifies articles with exploitation-related content
- **CVE Detection**: Extracts and correlates mentioned CVEs
- **Comprehensive Reports**: Generates structured intelligence reports with:
  - Executive summaries
  - Active exploitation details
  - Affected systems and products
  - Attack vectors and techniques
  - Threat actor activities
- **Seamless Publication**: Outputs reports in Markdown format for easy sharing

## 🏗️ Architecture

SentryInsight employs a hybrid architecture that combines the strengths of multiple AI technologies:

┌─────────────────────────────────────────────────────────────┐
│                      LangGraph Workflow                     │
├─────────┬─────────┬────────────┬────────────┬──────────────┤
│ Fetch   │ Enrich  │ Filter     │ Analyze    │ Generate     │
│ Articles│ Articles│ Exploitation│ Exploitation│ & Publish   │
└────┬────┴────┬────┴─────┬──────┴─────┬──────┴──────────────┘
     │         │          │            │
     ▼         ▼          │            ▼
┌──────────────────────┐  │   ┌─────────────────────────┐
│    MCP RSS Tools     │  │   │    LangChain + OpenAI   │
│  (Feed Processing)   │  │   │   (Content Analysis)    │
└──────────────────────┘  │   └─────────────────────────┘
                          │
                          ▼
                 ┌─────────────────────┐
                 │  Entity Extraction  │
                 │    & Filtering      │
                 └─────────────────────┘



## 🛠️ Technologies

### LangGraph
- Provides structured workflow orchestration
- Manages state throughout the analysis pipeline
- Handles conditional logic and process flow
- Creates a deterministic analysis sequence

### Model Context Protocol (MCP)
- Standardized interface for RSS feed operations
- Type-safe tool definitions with rich documentation
- Streamlined communications between components
- Modern, protocol-based tool architecture

### LangChain
- AI model integration and prompt engineering
- Text processing and transformation
- Model output parsing and structuring
- Chain-of-thought reasoning implementation

### OpenAI / GPT Models
- Content analysis and vulnerability detection
- Security intelligence synthesis
- Pattern recognition across security articles
- Natural language report generation

## 🚀 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SentryInsight.git
   cd SentryInsight
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   # Create a .env file with your OpenAI API key
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```

4. Configure the tool:
   ```bash
   # Review and edit config.json to set your preferences
   # - RSS feed sources
   # - Output paths
   # - Analysis parameters
   ```

## 📊 Usage

Run the main workflow:
```bash
python main.py
```

This will:
1. Fetch the latest security articles from configured RSS feeds
2. Enrich articles with full content
3. Filter for exploitation-relevant information
4. Generate a comprehensive exploitation report
5. Save the report to the configured output location

## 🔄 Workflow Stages

1. **Feed Fetching**: RSS feeds are retrieved using MCP tools
2. **Content Enrichment**: Articles are expanded with full content
3. **Exploitation Filtering**: Articles are filtered for security relevance
4. **Intelligence Analysis**: OpenAI analyzes content for exploitation details
5. **Report Generation**: Findings are compiled into a structured report
6. **Publication**: Reports are saved as Markdown files