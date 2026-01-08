# Exploitation Report

Critical vulnerabilities are currently being actively exploited across multiple platforms and systems. The most severe incidents involve maximum-severity vulnerabilities in HPE OneView and Microsoft Office being exploited in the wild, as flagged by CISA. Additionally, a newly discovered zero-day vulnerability (CVE-2026-0625) in legacy D-Link DSL routers is under active exploitation, while threat actors are targeting the n8n workflow automation platform through a maximum-severity vulnerability. The landscape also shows significant malware campaigns including GoBruteforcer botnet attacks on cryptocurrency platforms and malicious Chrome extensions stealing user conversations from AI services.

## Active Exploitation Details

### HPE OneView Maximum-Severity Vulnerability
- **Description**: A critical vulnerability in HPE OneView infrastructure management software that has reached maximum CVSS severity rating
- **Impact**: Allows attackers to gain unauthorized access to infrastructure management systems
- **Status**: Actively exploited in attacks and flagged by CISA for immediate attention

### Microsoft Office Security Flaw
- **Description**: A security vulnerability affecting Microsoft Office applications
- **Impact**: Enables unauthorized access and potential system compromise
- **Status**: Actively exploited and added to CISA's Known Exploited Vulnerabilities catalog

### D-Link DSL Router Zero-Day
- **Description**: A newly discovered critical remote code execution vulnerability in legacy D-Link DSL gateway routers
- **Impact**: Allows remote attackers to execute arbitrary commands and take control of affected routers
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-0625

### n8n Workflow Automation Platform Vulnerability
- **Description**: A maximum-severity vulnerability dubbed "Ni8mare" affecting the N8N workflow automation platform
- **Impact**: Allows remote, unauthenticated attackers to take complete control over locally deployed instances
- **Status**: Critical vulnerability with CVSS 10.0 score affecting both self-hosted and cloud versions

### jsPDF Library Critical Flaw
- **Description**: A critical vulnerability in the jsPDF library for generating PDF documents in JavaScript applications
- **Impact**: Allows attackers to steal sensitive data from the local filesystem by including malicious content in generated PDFs
- **Status**: Recently disclosed with potential for widespread impact

## Affected Systems and Products

- **HPE OneView**: Infrastructure management software with maximum-severity vulnerability
- **Microsoft Office**: Various Office applications affected by actively exploited security flaw
- **D-Link DSL Routers**: Legacy DSL gateway routers (end-of-life products) vulnerable to zero-day exploitation
- **n8n Platform**: Workflow automation platform (both self-hosted and cloud versions)
- **jsPDF Library**: JavaScript PDF generation library used in web applications
- **Veeam Backup & Replication**: Backup software with multiple security flaws including critical RCE vulnerability
- **Chrome Browser**: Extensions marketplace compromised by malicious extensions targeting 900,000 users
- **ownCloud Platform**: File-sharing platform experiencing credential theft incidents

## Attack Vectors and Techniques

- **Remote Code Execution**: Critical vulnerabilities in D-Link routers, Veeam backup systems, and n8n platform enabling arbitrary command execution
- **Credential Theft**: Large-scale compromise affecting cloud platforms and file-sharing services, with lack of MFA being a common vulnerability
- **Malware Distribution**: GoBruteforcer botnet targeting cryptocurrency and blockchain project databases
- **Browser Extension Abuse**: Malicious Chrome extensions stealing ChatGPT and DeepSeek conversations from users
- **SEO Poisoning**: Black Cat cybercrime gang using fraudulent sites to distribute malware through popular software searches
- **Email Spoofing**: Exploitation of misconfigured email routing and weak anti-spoofing protections in Office 365
- **PDF-based Attacks**: File inclusion vulnerabilities in PDF generation libraries enabling local file system access

## Threat Actor Activities

- **CISA-Tracked Attackers**: Actively exploiting HPE OneView and Microsoft Office vulnerabilities in ongoing campaigns
- **D-Link Router Exploiters**: Unknown threat actors leveraging zero-day vulnerability in legacy router infrastructure
- **Black Cat Cybercrime Gang**: Conducting SEO poisoning campaigns targeting users searching for popular software
- **GoBruteforcer Operators**: Targeting cryptocurrency and blockchain project databases using AI-generated configuration examples
- **Zestix Threat Actor**: Emerging group using various infostealers to breach file-sharing instances of approximately 50 enterprises
- **NoName057(16)**: Pro-Russian hacktivist group using DDoSia tool to mobilize volunteers for denial-of-service attacks
- **Chrome Extension Threat Actors**: Operators of malicious browser extensions targeting AI service users for conversation theft