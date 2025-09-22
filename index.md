# Exploitation Report

Critical vulnerabilities are currently being actively exploited across multiple platforms and services. The most severe incidents include a maximum severity command injection flaw in Fortra's GoAnywhere MFT platform (CVE-2025-10035), ongoing exploitation of Ivanti EPMM vulnerabilities (CVE-2025-4427 and CVE-2025-4428), and a recently patched critical Microsoft Entra ID authentication bypass flaw that could have enabled global admin impersonation across any tenant. Additionally, a zero-click vulnerability in OpenAI's ChatGPT Deep Research agent allows attackers to exfiltrate Gmail data through carefully crafted emails. Threat actors are leveraging sophisticated social engineering campaigns, including North Korean groups using ClickFix techniques and Iranian APT groups targeting telecommunications companies through LinkedIn job lures.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in GoAnywhere MFT's License Servlet that enables command injection attacks
- **Impact**: Attackers can execute arbitrary commands on vulnerable systems
- **Status**: Critical patch available; exploitation highly dependent on internet exposure
- **CVE ID**: CVE-2025-10035

### Microsoft Entra ID Authentication Bypass
- **Description**: Critical token validation failure in Microsoft Entra ID allowing impersonation of any user including Global Administrators across any tenant
- **Impact**: Complete tenant takeover capabilities across any organization using Microsoft Entra ID
- **Status**: Patched by Microsoft; was a zero-day vulnerability before disclosure

### Ivanti EPMM Vulnerabilities
- **Description**: Multiple vulnerabilities in Ivanti Endpoint Manager Mobile being actively exploited by threat actors
- **Impact**: Deployment of custom malware kits and persistent access to enterprise networks
- **Status**: Active exploitation ongoing with CISA-documented malware campaigns
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ChatGPT Deep Research Agent Zero-Click Flaw (ShadowLeak)
- **Description**: Zero-click vulnerability in OpenAI's ChatGPT Deep Research agent that allows data exfiltration through crafted emails
- **Impact**: Sensitive Gmail inbox data can be leaked without user interaction via OpenAI's infrastructure
- **Status**: Disclosed vulnerability with proof-of-concept demonstration

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection
- **Microsoft Entra ID**: All tenants were potentially vulnerable before patching
- **Ivanti EPMM**: Endpoint Manager Mobile platforms across multiple organizations
- **OpenAI ChatGPT**: Deep Research agent functionality
- **Apple macOS**: Targeted by Atomic Infostealer through fake GitHub repositories
- **Gmail Users**: Data exfiltration possible through ChatGPT integration
- **Telecommunications Companies**: 11 European telecom firms compromised with 34 devices affected
- **Cryptocurrency Platforms**: TradeOgre exchange dismantled with $40M seized

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: North Korean actors using fake error messages to deliver BeaverTail malware in cryptocurrency job scams
- **LinkedIn Job Lures**: Iranian UNC1549 group targeting telecom employees with MINIBIKE malware
- **Fake GitHub Repositories**: Distribution of Atomic Infostealer targeting macOS users through legitimate-looking software packages
- **Command Injection**: Direct exploitation of GoAnywhere MFT License Servlet for system compromise
- **Token Validation Bypass**: Exploitation of authentication flaws in Microsoft Entra ID for admin impersonation
- **Zero-Click Email Attacks**: ShadowLeak technique using crafted emails to trigger automatic data exfiltration
- **Phishing-as-a-Service**: Lighthouse and Lucid platforms operating 17,500 phishing domains targeting 316 brands across 74 countries

## Threat Actor Activities

- **DPRK/North Korean Groups**: Conducting cryptocurrency-focused job scam campaigns using ClickFix techniques to deliver BeaverTail malware and information stealers
- **UNC1549 (Iran-nexus)**: Successfully compromised 34 devices across 11 European telecommunications companies using LinkedIn job lures and MINIBIKE malware deployment
- **Gamaredon and Turla**: Russian hacking groups collaborating to deploy Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Teen members arrested in connection with August 2024 Transport for London cyber attack
- **SystemBC Operators**: Running REM Proxy network with 1,500 daily VPS victims across 80 command and control servers
- **Cybercriminal Groups**: Impersonating FBI Internet Crime Complaint Center through fake crime reporting portals for malicious activities