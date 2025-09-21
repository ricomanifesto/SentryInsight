# Exploitation Report

The current threat landscape reveals several critical exploitation activities, with maximum-severity vulnerabilities actively being exploited across enterprise systems. The most concerning developments include a CVSS 10.0 command injection flaw in Fortra GoAnywhere MFT systems, active exploitation of Ivanti EPMM vulnerabilities by multiple malware strains, and a sophisticated zero-click attack vector targeting OpenAI ChatGPT's Deep Research agent. Advanced persistent threat groups continue to demonstrate enhanced capabilities, with Iranian-nexus actors conducting highly targeted campaigns against telecommunications infrastructure while ransomware operations maintain their effectiveness despite defensive improvements.

## Active Exploitation Details

### GoAnywhere MFT License Servlet Command Injection
- **Description**: A maximum severity vulnerability in Fortra GoAnywhere MFT's License Servlet component allowing remote command injection attacks
- **Impact**: Attackers can execute arbitrary commands on affected systems, potentially leading to complete system compromise
- **Status**: Critical security updates released by Fortra, immediate patching required
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Multiple Vulnerabilities
- **Description**: Multiple vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) being actively exploited by threat actors to deploy custom malware
- **Impact**: Successful exploitation enables malware deployment and persistent access to enterprise mobile management systems
- **Status**: Active exploitation confirmed with CISA analysis of deployed malware strains
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak Zero-Click Attack
- **Description**: A zero-click vulnerability in OpenAI ChatGPT's Deep Research agent that allows attackers to exfiltrate sensitive Gmail data through crafted emails
- **Impact**: Enables invisible data exfiltration through OpenAI's infrastructure without leaving traces on target systems
- **Status**: Newly disclosed vulnerability affecting ChatGPT Deep Research functionality

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection, particularly systems exposed to the Internet
- **Ivanti EPMM**: Endpoint Manager Mobile systems targeted by custom malware deployment campaigns
- **OpenAI ChatGPT**: Deep Research agent vulnerable to data exfiltration attacks
- **macOS Systems**: Targeted by Atomic Infostealer through fake GitHub repositories and malicious applications
- **Telecommunications Infrastructure**: European telecom companies compromised through targeted phishing campaigns
- **Windows Systems**: Affected by MalTerminal malware utilizing GPT-4 capabilities for dynamic attack generation

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of GoAnywhere MFT License Servlet for arbitrary command execution
- **Zero-Click Email Attacks**: ShadowLeak technique targeting ChatGPT users through specially crafted emails
- **Social Engineering**: LinkedIn job lures used by UNC1549 to target telecommunications professionals
- **Malicious Repositories**: Fake GitHub repositories distributing Atomic Infostealer to macOS users
- **AI-Powered Malware**: MalTerminal leveraging GPT-4 capabilities to generate dynamic ransomware and reverse shells
- **Proxy Network Operations**: SystemBC malware powering REM Proxy network with over 1,500 daily VPS victims

## Threat Actor Activities

- **UNC1549**: Iran-nexus group successfully infiltrating 34 devices across 11 European telecommunications companies using LinkedIn job lures and MINIBIKE malware
- **Gamaredon and Turla**: Russian hacking groups collaborating to deploy Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Teen members arrested in connection with August 2024 Transport for London cyber attack
- **PhaaS Operators**: Lighthouse and Lucid phishing-as-a-service platforms targeting 316 brands across 74 countries with over 17,500 domains
- **REM Proxy Network**: Operating approximately 80 command and control servers managing botnet infrastructure
- **Atomic Infostealer Operators**: Conducting widespread campaigns against macOS users through fake software repositories