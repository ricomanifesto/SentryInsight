# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value systems across enterprise environments. The most severe threat involves a maximum severity command injection vulnerability in Fortra GoAnywhere MFT's License Servlet, assigned a CVSS 10.0 rating and tracked as CVE-2025-10035. Concurrently, attackers are actively exploiting two Ivanti Endpoint Manager Mobile vulnerabilities (CVE-2025-4427 and CVE-2025-4428) with sophisticated malware deployments. Additionally, a zero-click vulnerability dubbed "ShadowLeak" in OpenAI ChatGPT's Deep Research agent enables silent data exfiltration from Gmail accounts. The threat landscape is further complicated by AI-powered malware, information stealers targeting macOS users, and coordinated nation-state campaigns by Iranian and Russian threat actors.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity command injection flaw in GoAnywhere MFT's License Servlet that allows remote code execution
- **Impact**: Enables attackers to execute arbitrary commands on affected systems, potentially leading to complete system compromise
- **Status**: Critical patch released by Fortra; exploitation highly dependent on internet exposure
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Authentication Bypass and Command Injection
- **Description**: Two vulnerabilities in Ivanti Endpoint Manager Mobile that enable authentication bypass and command injection attacks
- **Impact**: Allows attackers to deploy sophisticated malware kits for persistent access and data exfiltration
- **Status**: Actively exploited in the wild with CISA-documented malware deployments
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak Zero-Click ChatGPT Vulnerability
- **Description**: A zero-click flaw in OpenAI ChatGPT's Deep Research agent that enables data exfiltration through crafted emails
- **Impact**: Allows attackers to leak sensitive Gmail inbox data without user interaction, using OpenAI's infrastructure to hide malicious activity
- **Status**: Actively exploitable vulnerability affecting ChatGPT users

### Atomic Infostealer macOS Campaign
- **Description**: Widespread information stealer campaign targeting macOS users through fake GitHub repositories
- **Impact**: Steals credentials, browser data, and system information from infected macOS systems
- **Status**: Ongoing campaign with active distribution through legitimate-appearing repositories

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection attacks
- **Ivanti Endpoint Manager Mobile**: Authentication and command injection vulnerabilities enabling malware deployment
- **OpenAI ChatGPT**: Deep Research agent susceptible to zero-click data exfiltration
- **macOS Systems**: Targeted by Atomic Infostealer through fake GitHub repositories
- **European Telecommunications**: 34 devices across 11 organizations compromised by UNC1549
- **Gmail Users**: Vulnerable to ShadowLeak attacks through ChatGPT integration
- **SonicWall MySonicWall Service**: Breached with firewall backup data exposed

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of GoAnywhere MFT License Servlet for arbitrary code execution
- **Zero-Click Exploitation**: ShadowLeak attacks requiring no user interaction beyond receiving an email
- **Social Engineering**: Fake GitHub repositories and LinkedIn job lures for initial access
- **Malware-as-a-Service**: AI-powered MalTerminal creating custom ransomware and reverse shells
- **Supply Chain Attacks**: Compromised repositories distributing legitimate-appearing malicious software
- **Email-Based Attacks**: Crafted emails triggering automated data exfiltration through AI agents
- **Phishing-as-a-Service**: Over 17,500 domains targeting 316 brands across 74 countries

## Threat Actor Activities

- **UNC1549 (Iran-nexus)**: Targeted European telecommunications companies using LinkedIn job lures and MINIBIKE malware, successfully compromising 34 devices across 11 organizations
- **Gamaredon and Turla (Russian)**: Collaborative operations deploying Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Two teenage members arrested in connection with August 2024 Transport for London cyber attack
- **LastPass Campaign Actors**: Operating widespread macOS-targeting campaign using fake repositories to distribute Atomic Infostealer
- **SystemBC Operators**: Managing REM Proxy network with 1,500 daily VPS victims across 80 command-and-control servers
- **Lighthouse/Lucid PhaaS**: Operating massive phishing infrastructure targeting global brands and organizations