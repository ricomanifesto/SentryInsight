# Exploitation Report

Critical exploitation activity continues to emerge across multiple attack surfaces, with several high-severity vulnerabilities being actively exploited in the wild. The most concerning developments include a maximum severity command injection flaw in Fortra's GoAnywhere MFT platform (CVE-2025-10035), active exploitation of Ivanti Endpoint Manager Mobile vulnerabilities (CVE-2025-4427 and CVE-2025-4428), and sophisticated state-sponsored campaigns targeting telecommunications infrastructure. Additionally, novel attack techniques such as the ShadowLeak method against ChatGPT systems and large-scale proxy botnets are demonstrating the evolving threat landscape.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in GoAnywhere MFT's License Servlet that allows remote command injection attacks with a CVSS score of 10.0
- **Impact**: Attackers can execute arbitrary commands on vulnerable systems, potentially leading to complete system compromise
- **Status**: Patch available from Fortra; exploitation highly dependent on Internet exposure of affected systems
- **CVE ID**: CVE-2025-10035

### Ivanti Endpoint Manager Mobile Vulnerabilities
- **Description**: Two vulnerabilities in Ivanti EPMM being actively exploited with custom malware strains deployed post-compromise
- **Impact**: Full system compromise with persistent malware installation and potential lateral movement
- **Status**: Active exploitation detected with specialized malware kits identified by CISA
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak ChatGPT Attack Method
- **Description**: A novel attack technique that exploits ChatGPT's infrastructure to exfiltrate company data invisibly
- **Impact**: Data exfiltration through OpenAI's infrastructure, leaving no traces on enterprise systems
- **Status**: Proof-of-concept demonstrated, allowing attackers to steal emails and sensitive information

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection
- **Ivanti Endpoint Manager Mobile (EPMM)**: Multiple versions affected by actively exploited vulnerabilities
- **ChatGPT/OpenAI Infrastructure**: Vulnerable to ShadowLeak data exfiltration technique
- **SonicWall MySonicWall Service**: Cloud backup service breached, affecting under 5% of customer base
- **Commercial Virtual Private Servers**: Targeted by SystemBC malware for proxy botnet operations
- **European Telecommunications Companies**: 34 devices across 11 organizations compromised by UNC1549

## Attack Vectors and Techniques

- **Command Injection**: Remote exploitation of GoAnywhere MFT License Servlet for arbitrary command execution
- **Social Engineering**: LinkedIn job lures used by UNC1549 to target telecommunications personnel
- **Malware-as-a-Service**: SystemBC powering REM Proxy network with approximately 1,500 daily VPS victims
- **AI Infrastructure Abuse**: ShadowLeak technique leveraging ChatGPT for covert data exfiltration
- **Phishing-as-a-Service**: Lighthouse and Lucid PhaaS platforms operating 17,500 phishing domains targeting 316 brands
- **Configuration File Exposure**: SonicWall breach exposing firewall backup configurations

## Threat Actor Activities

- **UNC1549 (Iran-nexus)**: Sophisticated espionage campaign targeting European telecommunications companies using MINIBIKE malware and LinkedIn social engineering
- **Scattered Spider**: Two teenage members arrested in UK for August 2024 Transport for London cyberattack
- **Gamaredon and Turla**: Russian hacking groups collaborating to deploy Kazuar backdoor against Ukrainian entities
- **SystemBC Operators**: Maintaining large-scale proxy botnet infrastructure across 80 C2 servers
- **Phishing-as-a-Service Groups**: Operating Lighthouse and Lucid platforms targeting global brands across 74 countries