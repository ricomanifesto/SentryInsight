# Exploitation Report

The current threat landscape reveals multiple critical exploitation activities targeting enterprise infrastructure and cloud services. A maximum severity vulnerability in Fortra GoAnywhere MFT's License Servlet poses immediate risks through command injection attacks, while threat actors are actively exploiting Ivanti EPMM vulnerabilities to deploy specialized malware kits. Additionally, a zero-click flaw in OpenAI's ChatGPT Deep Research agent enables Gmail data exfiltration, and North Korean actors continue leveraging social engineering campaigns to distribute BeaverTail malware through cryptocurrency job scams. Iranian state-sponsored groups have demonstrated sophisticated targeting of telecommunications companies across Europe, successfully compromising 34 devices across 11 organizations.

## Active Exploitation Details

### GoAnywhere MFT License Servlet Command Injection
- **Description**: A maximum severity vulnerability in Fortra GoAnywhere MFT's License Servlet that allows command injection attacks
- **Impact**: Enables arbitrary command execution on affected systems
- **Status**: Critical patch released by Fortra, immediate patching required
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities
- **Description**: Two vulnerabilities in Ivanti Endpoint Manager Mobile being actively exploited to deploy malware
- **Impact**: Allows threat actors to compromise enterprise mobile device management systems and deploy persistent malware
- **Status**: Actively exploited with CISA documenting deployed malware kits
- **CVE ID**: CVE-2025-4427 and CVE-2025-4428

### ShadowLeak Zero-Click Gmail Exploitation
- **Description**: A zero-click vulnerability in OpenAI ChatGPT's Deep Research agent that enables Gmail data exfiltration
- **Impact**: Allows attackers to steal sensitive Gmail inbox data through a single crafted email without user interaction
- **Status**: Disclosed vulnerability with potential for invisible data exfiltration

### Microsoft Entra ID Tenant Hijacking
- **Description**: A critical combination of legacy components in Microsoft Entra ID that could allow complete tenant access
- **Impact**: Complete hijacking of any company's Microsoft Entra ID tenant worldwide
- **Status**: Vulnerability was fixed prior to disclosure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection
- **Ivanti Endpoint Manager Mobile (EPMM)**: Mobile device management platform targeted by malware deployment
- **OpenAI ChatGPT**: Deep Research agent vulnerable to zero-click data exfiltration
- **Microsoft Entra ID**: Identity and access management service with tenant hijacking vulnerability
- **Apple macOS**: Targeted by Atomic Infostealer through fake GitHub repositories
- **European Telecommunications Companies**: 34 devices across 11 organizations compromised by Iranian actors
- **Gmail Accounts**: Vulnerable to data exfiltration through ChatGPT integration
- **Cryptocurrency Platforms**: Targeted by North Korean social engineering campaigns

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of GoAnywhere MFT License Servlet for arbitrary command execution
- **Zero-Click Exploitation**: Gmail data theft through crafted emails targeting ChatGPT integration
- **Social Engineering**: LinkedIn job lures used by Iranian UNC1549 group to target telecommunications
- **Fake Repository Distribution**: macOS users targeted through malicious GitHub repositories masquerading as legitimate software
- **ClickFix Lures**: DPRK actors using fake error messages to deliver BeaverTail malware
- **Tenant Takeover**: Legacy component exploitation for complete Entra ID tenant control
- **Cryptocurrency Job Scams**: North Korean campaigns targeting crypto industry professionals
- **Malware Kit Deployment**: Sophisticated malware installation following Ivanti EPMM compromise

## Threat Actor Activities

- **UNC1549 (Iranian APT)**: Successfully infiltrated 34 devices across 11 European telecommunications companies using LinkedIn job lures and MINIBIKE malware
- **DPRK Hackers**: Deploying BeaverTail malware through ClickFix-style lures in cryptocurrency job scams targeting industry professionals
- **Gamaredon and Turla**: Russian hacking groups collaborating to deploy Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Teen members arrested in connection with August 2024 Transport for London cyber attack
- **SystemBC Operators**: Powering REM Proxy network with approximately 1,500 daily VPS victims across 80 command and control servers
- **PhaaS Groups**: Lighthouse and Lucid phishing-as-a-service operations targeting 316 brands across 74 countries with over 17,500 phishing domains