# Exploitation Report

Multiple critical vulnerabilities are currently being actively exploited in the wild, with several zero-day flaws and newly disclosed vulnerabilities posing significant threats to organizations. The most severe activity includes active exploitation of Ivanti EPMM vulnerabilities CVE-2025-4427 and CVE-2025-4428 with custom malware deployment, a maximum severity command injection flaw in Fortra GoAnywhere MFT (CVE-2025-10035), and a sophisticated zero-click vulnerability in OpenAI's ChatGPT Deep Research agent dubbed "ShadowLeak." Additionally, Iranian state-sponsored threat actors are conducting highly targeted campaigns against telecommunications companies, while widespread malware campaigns are targeting macOS users and leveraging AI-powered capabilities for enhanced attack effectiveness.

## Active Exploitation Details

### ShadowLeak Zero-Click Flaw in OpenAI ChatGPT Deep Research Agent
- **Description**: A zero-click vulnerability in OpenAI's ChatGPT Deep Research agent that allows attackers to leak sensitive Gmail inbox data through a single crafted email without user interaction
- **Impact**: Enables data exfiltration of company information via OpenAI's infrastructure, leaving no trace on enterprise systems
- **Status**: Actively exploitable, allows invisible email theft

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in GoAnywhere MFT's License Servlet that enables command injection attacks
- **Impact**: Allows execution of arbitrary commands on affected systems
- **Status**: Critical patch available, highly dependent on Internet exposure
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities with Active Malware Deployment
- **Description**: Two vulnerabilities in Ivanti Endpoint Manager Mobile being exploited with custom malware deployment
- **Impact**: Complete system compromise with persistent malware installation
- **Status**: Active exploitation with CISA-documented malware kits
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection
- **Ivanti Endpoint Manager Mobile (EPMM)**: Multiple vulnerabilities with active malware campaigns
- **OpenAI ChatGPT**: Deep Research agent vulnerable to zero-click data exfiltration
- **Apple macOS**: Targeted by Atomic Infostealer through fake GitHub repositories
- **European Telecommunications Infrastructure**: 34 devices across 11 organizations compromised
- **Gmail Services**: Data accessible through ChatGPT vulnerability exploitation
- **Steam Platform**: 32-bit Windows support ending January 2026 (security consideration)

## Attack Vectors and Techniques

- **Social Engineering via LinkedIn**: UNC1549 using fake job offers to target telecommunications employees
- **Fake GitHub Repositories**: Malware distribution disguised as legitimate software for macOS users
- **Zero-Click Email Exploitation**: ShadowLeak attack requiring only crafted email delivery
- **AI-Powered Malware**: MalTerminal leveraging GPT-4 capabilities for ransomware and reverse shell creation
- **Phishing-as-a-Service (PhaaS)**: Lighthouse and Lucid platforms hosting 17,500 phishing domains
- **SystemBC Proxy Network**: REM Proxy botnet with 1,500 daily VPS victims across 80 C2 servers
- **Command Injection**: Direct exploitation of web application vulnerabilities for system access

## Threat Actor Activities

- **UNC1549 (Iran-nexus)**: Successfully infiltrated 34 devices across 11 European telecommunications companies using LinkedIn job lures and MINIBIKE malware
- **Gamaredon and Turla Collaboration**: Russian hacking groups working together to deploy Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Two teen members arrested in connection with August 2024 Transport for London cyber attack
- **Unknown Threat Actors**: Deploying Atomic Infostealer via fake LastPass-themed repositories targeting macOS users
- **Cybercriminal Groups**: Operating fake FBI Internet Crime Complaint Center websites for malicious activities
- **PhaaS Operators**: Managing Lighthouse and Lucid services targeting 316 brands across 74 countries