# Exploitation Report

Critical vulnerabilities across multiple enterprise platforms are experiencing active exploitation, with threat actors targeting cloud infrastructure, mobile device management systems, and file transfer solutions. The most severe incidents include a maximum severity command injection flaw in Fortra GoAnywhere MFT (CVE-2025-10035) and active exploitation of Ivanti Endpoint Manager Mobile vulnerabilities (CVE-2025-4427 and CVE-2025-4428). Additionally, sophisticated attack campaigns are leveraging zero-click vulnerabilities in OpenAI's ChatGPT Deep Research agent and targeting Microsoft Entra ID through legacy component combinations. Nation-state actors, particularly from North Korea, Iran, and Russia, are conducting advanced persistent threat operations using social engineering tactics and custom malware frameworks.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in GoAnywhere MFT's License Servlet that allows remote command injection attacks
- **Impact**: Attackers can execute arbitrary commands on affected systems, potentially leading to complete system compromise
- **Status**: Critical patch released by Fortra, exploitation depends on internet exposure of affected systems
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Authentication Bypass and SQL Injection
- **Description**: Multiple vulnerabilities affecting Ivanti Endpoint Manager Mobile allowing authentication bypass and SQL injection attacks
- **Impact**: Complete compromise of mobile device management infrastructure with deployment of custom malware toolkits
- **Status**: Actively exploited in the wild with CISA publishing detailed malware analysis
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak Zero-Click ChatGPT Vulnerability
- **Description**: Zero-click flaw in OpenAI ChatGPT's Deep Research agent that enables data exfiltration through crafted emails
- **Impact**: Attackers can steal sensitive Gmail inbox data without user interaction using OpenAI's infrastructure
- **Status**: Active exploitation possible with no user interaction required

### Microsoft Entra ID Legacy Component Exploitation
- **Description**: Critical combination of legacy components in Microsoft Entra ID that could allow tenant hijacking
- **Impact**: Complete access to any company's Microsoft Entra ID tenant globally
- **Status**: Vulnerability has been addressed by Microsoft prior to public disclosure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection attacks
- **Ivanti Endpoint Manager Mobile (EPMM)**: Authentication and SQL injection vulnerabilities actively exploited
- **Microsoft Entra ID**: Legacy component combinations affecting tenant security globally
- **OpenAI ChatGPT**: Deep Research agent vulnerable to zero-click data exfiltration
- **macOS Systems**: Targeted by Atomic Infostealer through fake GitHub repositories
- **Windows Systems**: MalTerminal malware with integrated GPT-4 capabilities creating ransomware and reverse shells
- **Telecommunications Infrastructure**: European telecom companies compromised through LinkedIn job lures and MINIBIKE malware

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: North Korean threat actors using fake error messages to deliver BeaverTail malware
- **LinkedIn Job Lures**: Iranian UNC1549 group targeting telecommunications employees with fake job opportunities
- **Fake GitHub Repositories**: Distribution of Atomic Infostealer through legitimate-looking macOS applications
- **Email-Based Zero-Click Attacks**: ShadowLeak technique requiring only a single crafted email to exfiltrate data
- **Command Injection**: Direct exploitation of web application vulnerabilities in file transfer solutions
- **Malware Kit Deployment**: Custom toolkits deployed following successful Ivanti EPMM exploitation
- **AI-Powered Malware**: GPT-4 integration in malware for dynamic payload generation and evasion

## Threat Actor Activities

- **North Korean APT Groups**: Conducting cryptocurrency-focused job scams using ClickFix techniques to deliver BeaverTail malware
- **UNC1549 (Iran-nexus)**: Successfully infiltrated 34 devices across 11 European telecommunications companies using MINIBIKE malware
- **Gamaredon and Turla (Russian)**: Collaborative operations deploying Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Teen members arrested in connection with August 2024 Transport for London cyber attack
- **PhaaS Operators**: Lighthouse and Lucid services operating over 17,500 phishing domains targeting 316 brands across 74 countries
- **SystemBC Botnet**: Powering REM Proxy network with approximately 1,500 daily VPS victims across 80 command and control servers