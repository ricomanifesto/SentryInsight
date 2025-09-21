# Exploitation Report

Current cybersecurity landscape reveals critical active exploitation targeting managed file transfer systems, enterprise mobile management platforms, and AI-powered services. The most severe activity includes a maximum CVSS 10.0 vulnerability in Fortra GoAnywhere MFT allowing command injection attacks (CVE-2025-10035), active exploitation of Ivanti EPMM vulnerabilities with sophisticated malware deployment (CVE-2025-4427 and CVE-2025-4428), and a novel zero-click attack against OpenAI's ChatGPT Deep Research agent enabling Gmail data exfiltration. Nation-state actors from North Korea, Iran, and Russia are conducting sophisticated campaigns using advanced social engineering, AI-powered malware, and collaborative operations to target telecommunications, cryptocurrency, and enterprise infrastructure.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: Critical command injection flaw in GoAnywhere Managed File Transfer software's License Servlet component with maximum CVSS 10.0 severity rating
- **Impact**: Complete system compromise through arbitrary command execution, potentially affecting file transfer operations and sensitive data
- **Status**: Critical patch released by Fortra, exploitation highly dependent on internet exposure
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Mobile Management Vulnerabilities
- **Description**: Multiple vulnerabilities in Ivanti Endpoint Manager Mobile platform being actively exploited with custom malware kits
- **Impact**: Complete device compromise, data theft, and persistent access to enterprise mobile infrastructure
- **Status**: Active exploitation detected by CISA with sophisticated malware deployment
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak ChatGPT Zero-Click Attack
- **Description**: Zero-click vulnerability in OpenAI ChatGPT's Deep Research agent allowing Gmail data exfiltration through crafted emails
- **Impact**: Invisible data theft from Gmail accounts without user interaction, complete email content access
- **Status**: Active proof-of-concept demonstrated, enables data exfiltration via OpenAI infrastructure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component in managed file transfer software
- **Ivanti EPMM**: Enterprise mobile device management platforms across multiple organizations
- **OpenAI ChatGPT**: Deep Research agent functionality integrated with Gmail
- **Apple macOS**: Targeted by Atomic Infostealer through fake GitHub repositories
- **European Telecommunications**: 34 devices across 11 telecom firms compromised by UNC1549
- **Cryptocurrency Exchanges**: TradeOgre platform dismantled with $40 million seized
- **Microsoft Azure Entra ID**: Identity and access management service with critical flaws

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: DPRK actors using fake error prompts to deliver BeaverTail malware in crypto job scams
- **Fake GitHub Repositories**: LastPass warns of malicious repositories distributing Atomic Infostealer on macOS
- **LinkedIn Job Lures**: Iranian UNC1549 group targeting telecom employees with MINIBIKE malware
- **AI-Powered Malware**: MalTerminal malware incorporating GPT-4 capabilities for dynamic ransomware and reverse shell generation
- **Email-Based Zero-Click**: ShadowLeak technique requiring only receipt of crafted email to compromise Gmail data
- **Phishing-as-a-Service**: Lighthouse and Lucid platforms supporting 17,500+ phishing domains targeting 316 brands globally

## Threat Actor Activities

- **DPRK Hackers**: Sophisticated cryptocurrency-focused campaigns using ClickFix techniques and BeaverTail malware delivery
- **UNC1549 (Iranian APT)**: Precision targeting of European telecommunications with 34 device compromises across 11 organizations using MINIBIKE malware
- **Gamaredon & Turla**: Russian state groups collaborating to deploy Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Two teenage members arrested in UK for August 2024 Transport for London cyber attack
- **SystemBC Operators**: Managing REM Proxy network with 1,500 daily VPS victims across 80 command-and-control servers
- **PhaaS Groups**: Lighthouse and Lucid services enabling massive phishing campaigns across 74 countries