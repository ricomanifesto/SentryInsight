# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited across enterprise systems, with CVE-2026-35273 in Oracle PeopleSoft being leveraged by ShinyHunters to breach university networks and steal sensitive data. A maximum severity Ivanti Sentry flaw was exploited within 24 hours of disclosure, prompting CISA emergency directives. Additionally, authentication bypass vulnerabilities in enterprise software, Linux package repository compromises affecting 400+ Arch Linux AUR packages, and sophisticated long-term persistence attacks by Chinese threat actors highlight the evolving threat landscape across multiple platforms and industries.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day
- **Description**: Critical zero-day vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Complete system compromise, data theft, and enterprise network breaches
- **Status**: Oracle has issued mitigation guidance; actively exploited by ShinyHunters
- **CVE ID**: CVE-2026-35273

### Ivanti Sentry Maximum Severity Flaw
- **Description**: Maximum severity vulnerability in Ivanti Sentry with rapid exploitation timeline
- **Impact**: System compromise and unauthorized access to enterprise environments
- **Status**: Exploited within 24 hours of disclosure; CISA mandates federal patching by Sunday
- **CVE ID**: Not specified in source articles

### Splunk Enterprise Critical Vulnerability
- **Description**: Critical security flaw enabling unauthenticated file operations and remote code execution
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Security updates released by Splunk

### phpBB Authentication Bypass
- **Description**: 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Attackers can log in as any user, including administrators
- **Status**: Recently patched after decade-long exposure

### LangGraph Self-Hosted AI Agent Vulnerabilities
- **Description**: Critical vulnerability chain in LangGraph affecting self-hosted AI agents
- **Impact**: Remote code execution on AI agent systems
- **Status**: Three security flaws now patched

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning software, particularly affecting American universities
- **Ivanti Sentry**: Enterprise security solutions with federal government deployments
- **Splunk Enterprise**: Data analytics and monitoring platforms
- **phpBB Forum Software**: Web-based bulletin board systems across various organizations
- **Arch Linux AUR**: Over 400 packages in the Arch User Repository compromised
- **LangGraph**: Self-hosted artificial intelligence coding agents
- **Linux Login Systems**: Authentication mechanisms backdoored for nearly a decade

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Immediate weaponization of undisclosed vulnerabilities within hours of discovery
- **Supply Chain Attacks**: Compromise of software repositories and package managers to distribute malware
- **Authentication Stack Hijacking**: Long-term persistence through compromised authentication systems
- **Package Repository Poisoning**: Malicious modification of legitimate software packages to include rootkits and infostealers
- **AI Agent Manipulation**: Agentjacking attacks that trick AI coding agents into executing malicious code
- **eBPF Rootkit Deployment**: Advanced Linux rootkits using extended Berkeley Packet Filter technology

## Threat Actor Activities

- **ShinyHunters**: Actively exploiting Oracle PeopleSoft zero-day to target higher education institutions for data theft and extortion
- **Chinese APT Groups**: Maintaining decade-long persistence in isolated networks through authentication system compromises and Linux backdoors
- **Ransomware Operations**: Continued activities including Conti ransomware operations with Ukrainian national prosecution
- **Cryptocurrency Laundering Networks**: AudiA6 service disrupted by Europol after facilitating ransomware gang money laundering
- **Phishing-as-a-Service Operators**: Sniper Dz platform disrupted after decade of operation, with administrator arrested
- **Chinese Smishing Networks**: Using Google's Gemini AI for enhanced phishing campaigns targeting American users