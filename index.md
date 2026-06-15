# Exploitation Report

The cybersecurity landscape is experiencing significant exploitation activity across multiple attack vectors, with particular emphasis on zero-day vulnerabilities and supply chain attacks. ShinyHunters has successfully exploited a zero-day vulnerability in Oracle PeopleSoft systems to breach multiple universities, while attackers have compromised over 400 Arch Linux packages to distribute rootkits and infostealers. Additionally, critical vulnerabilities in Splunk Enterprise and phpBB forum software are being actively targeted, alongside sophisticated AI-powered phishing campaigns and long-term persistence attacks against authentication systems.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: An unpatched zero-day vulnerability in Oracle PeopleSoft enterprise systems allowing unauthorized access and data theft
- **Impact**: Enables attackers to break into enterprise systems, steal sensitive data, and conduct extortion campaigns
- **Status**: Currently unpatched, actively exploited by ShinyHunters group
- **CVE ID**: CVE-2026-35273

### Splunk Enterprise Critical Vulnerability
- **Description**: A critical security flaw in Splunk Enterprise allowing unauthenticated file operations and remote code execution
- **Impact**: Attackers can execute code without authentication and perform unauthorized file operations
- **Status**: Security updates have been released by Splunk

### phpBB Authentication Bypass Vulnerability
- **Description**: A 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators
- **Status**: Recently patched after being present for a decade

### Ivanti Sentry Vulnerability
- **Description**: An actively exploited vulnerability in Ivanti Sentry systems
- **Impact**: Allows unauthorized access to federal systems
- **Status**: Actively exploited, CISA has ordered federal agencies to patch within three days

### LangGraph Vulnerability Chain
- **Description**: Three security flaws in LangGraph affecting self-hosted AI agents
- **Impact**: Critical vulnerability chain could result in remote code execution
- **Status**: Now patched

## Affected Systems and Products

- **Oracle PeopleSoft**: Enterprise resource planning systems, particularly affecting American universities
- **Splunk Enterprise**: Data analytics and monitoring platform vulnerable to unauthenticated attacks
- **phpBB Forum Software**: Community forum platform with decade-old authentication bypass
- **Arch Linux AUR**: Over 400 packages in Arch User Repository compromised with malicious build scripts
- **Ivanti Sentry**: Enterprise security management systems in federal environments
- **LangGraph**: AI agent development framework for self-hosted implementations
- **Linux Authentication Systems**: Login software backdoored for nearly a decade
- **Tchap Messenger**: French government encrypted messaging platform affecting 73,000+ employees

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise software
- **Supply Chain Poisoning**: Hijacking of legitimate software repositories to distribute malware
- **Authentication Flow Hijacking**: Long-term compromise of authentication systems for persistent access
- **AI-Powered Phishing**: Use of artificial intelligence to enhance phishing campaign effectiveness
- **Package Repository Compromise**: Modification of build scripts in software repositories to install malware
- **Agentjacking**: New attack class targeting AI coding agents to execute malicious code on developer systems
- **Backdoor Installation**: Long-term persistence mechanisms in critical system components

## Threat Actor Activities

- **ShinyHunters**: Actively exploiting Oracle PeopleSoft zero-day to breach universities and conduct data extortion campaigns
- **Chinese Threat Groups**: Maintaining decade-long persistence in authentication systems and isolated networks through backdoored login software
- **Outsider Enterprise**: Chinese phishing-as-a-service operation using AI and managing over a million phishing URLs before FBI disruption
- **Sniper Dz Operators**: Decade-long phishing-as-a-service platform disrupted by INTERPOL Operation Ramz
- **AudiA6 Service**: Cryptocurrency laundering service used by ransomware gangs, disrupted by European authorities
- **Conti Ransomware Affiliates**: Ukrainian national pleading guilty to conspiracy charges related to ransomware operations
- **Arch Linux Package Hijackers**: Attackers compromising over 400 AUR packages to deploy eBPF rootkits and credential stealers