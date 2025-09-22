# Exploitation Report

Multiple critical vulnerabilities and active exploitation campaigns have emerged across cloud platforms, enterprise software, and mobile malware distribution networks. The most severe issues include a maximum severity command injection flaw in Fortra GoAnywhere MFT (CVE-2025-10035), active exploitation of Ivanti EPMM vulnerabilities (CVE-2025-4427 and CVE-2025-4428), and a zero-click vulnerability in OpenAI ChatGPT's Deep Research agent that can leak Gmail data. State-sponsored threat actors from North Korea and Iran continue sophisticated campaigns targeting cryptocurrency professionals and telecommunications infrastructure, while multiple malware distribution networks leverage AI-powered tools and social engineering tactics.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in GoAnywhere MFT's License Servlet that allows command injection attacks
- **Impact**: Attackers can execute arbitrary commands on affected systems
- **Status**: Critical patch released by Fortra, immediate patching required
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities
- **Description**: Two vulnerabilities in Ivanti Endpoint Manager Mobile being actively exploited with custom malware kits
- **Impact**: Threat actors can deploy specialized malware strains for persistent access and data exfiltration
- **Status**: CISA has published detailed analysis of malware deployed in attacks
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### OpenAI ChatGPT Deep Research Agent Zero-Click Flaw
- **Description**: A zero-click vulnerability dubbed "ShadowLeak" that allows data exfiltration from Gmail through a single crafted email
- **Impact**: Attackers can invisibly steal sensitive Gmail inbox data without user interaction
- **Status**: Actively exploitable vulnerability disclosed by researchers

### Microsoft Entra ID Tenant Hijacking Vulnerability
- **Description**: Critical flaw involving legacy components that could allow complete access to any company's Microsoft Entra ID tenant
- **Impact**: Total compromise of organizational identity and access management systems
- **Status**: Fixed by Microsoft prior to disclosure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection
- **Ivanti Endpoint Manager Mobile**: Multiple vulnerabilities being exploited with custom malware
- **Microsoft Entra ID**: Legacy component combination allowed tenant hijacking
- **OpenAI ChatGPT**: Deep Research agent vulnerable to zero-click data exfiltration
- **macOS Systems**: Targeted by Atomic Infostealer through fake GitHub repositories
- **Android Devices**: BeaverTail malware distribution via ClickFix-style attacks
- **European Telecommunications**: 34 devices across 11 organizations compromised by UNC1549
- **Windows Systems**: MalTerminal malware with GPT-4 integration creating ransomware

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: DPRK actors using fake error messages to deliver BeaverTail malware in cryptocurrency job scams
- **Fake GitHub Repositories**: Malicious repositories distributing Atomic Infostealer disguised as legitimate software
- **LinkedIn Job Lures**: UNC1549 using professional networking for initial access to telecommunications targets
- **Email-Based Zero-Click**: ShadowLeak attack requiring only a single crafted email to exfiltrate Gmail data
- **Proxy Network Infrastructure**: SystemBC malware powering REM Proxy with 1,500 daily victims across 80 C2 servers
- **AI-Powered Malware**: MalTerminal using GPT-4 capabilities to create ransomware and reverse shells
- **Phishing-as-a-Service**: Lighthouse and Lucid PhaaS platforms targeting 316 brands across 74 countries

## Threat Actor Activities

- **DPRK Threat Actors**: Conducting cryptocurrency-focused campaigns using ClickFix techniques and BeaverTail malware
- **UNC1549 (Iran-nexus)**: Successfully infiltrated 34 devices across 11 European telecommunications companies using MINIBIKE malware
- **Gamaredon and Turla**: Russian groups collaborating to deploy Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Two teen members arrested in connection with August 2024 Transport for London cyber attack
- **Charming Kitten Subgroup**: Iranian APT conducting highly targeted attacks against telecommunications and satellite companies