# Exploitation Report

The current threat landscape is dominated by several critical exploitation activities, most notably the ShinyHunters group's exploitation of an Oracle PeopleSoft zero-day vulnerability (CVE-2026-35273) targeting universities, and a massive compromise of over 400 Arch Linux AUR packages deploying rootkits and infostealers. Additionally, Chinese-linked threat actors have demonstrated sophisticated persistence techniques, maintaining access to isolated networks for nearly a decade through compromised authentication systems and Linux login software. Critical vulnerabilities in Splunk Enterprise allowing unauthenticated remote code execution and a decade-old authentication bypass in phpBB forum software further highlight the severity of current exploitation trends.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: An unpatched zero-day vulnerability in Oracle's PeopleSoft ERP software that allows unauthorized access to enterprise systems
- **Impact**: Attackers can break into enterprise systems, steal sensitive data, and conduct extortion campaigns
- **Status**: Actively exploited by ShinyHunters group, disproportionately affecting American universities
- **CVE ID**: CVE-2026-35273

### Splunk Enterprise Critical Authentication Bypass
- **Description**: A critical security flaw in Splunk Enterprise that allows attackers to conduct file operations and execute code without authentication
- **Impact**: Unauthenticated remote code execution and unauthorized file operations
- **Status**: Security updates released by Splunk to address the vulnerability

### phpBB Authentication Bypass Vulnerability
- **Description**: A 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators
- **Status**: Recently patched after lurking undetected for a decade

### Ivanti Sentry Actively Exploited Flaw
- **Description**: A vulnerability in Ivanti Sentry systems currently being exploited in active attacks
- **Impact**: Allows unauthorized access to affected systems
- **Status**: CISA has ordered federal agencies to patch within three days due to active exploitation

## Affected Systems and Products

- **Oracle PeopleSoft**: ERP software systems, particularly affecting university environments
- **Splunk Enterprise**: Data analytics and monitoring platforms vulnerable to unauthenticated attacks
- **phpBB Forum Software**: Web-based forum platforms with decade-old authentication vulnerabilities
- **Arch Linux AUR**: Over 400 packages in the Arch User Repository compromised with malicious build scripts
- **Ivanti Sentry**: Network security appliances under active attack
- **Linux Systems**: Authentication systems and login software targeted by long-term Chinese campaigns
- **French Government Tchap**: Encrypted messaging platform affecting over 73,000 public sector employees

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: ShinyHunters leveraging unpatched Oracle vulnerabilities for data theft and extortion
- **Supply Chain Compromise**: Mass hijacking of Arch Linux AUR packages to deploy rootkits and credential stealers
- **Authentication Bypass**: Exploiting long-standing vulnerabilities in phpBB and Splunk systems
- **Persistence Techniques**: Chinese actors maintaining decade-long access through compromised authentication flows
- **AI-Enhanced Phishing**: Use of AI tools like Gemini to create more sophisticated phishing campaigns
- **Package Repository Hijacking**: Rewriting build scripts in legitimate software packages to deliver malware
- **Agentjacking Attacks**: New attack class targeting AI coding agents to execute malicious code on developer systems

## Threat Actor Activities

- **ShinyHunters**: Actively exploiting Oracle PeopleSoft zero-day (CVE-2026-35273) in campaign targeting universities for data theft and extortion
- **Chinese-Linked Groups**: Demonstrated advanced persistence by maintaining access to isolated networks for nearly a decade through compromised authentication systems and Linux login software backdoors
- **AUR Package Attackers**: Compromised over 400 Arch Linux packages to distribute Linux rootkits and credential-stealing malware targeting access tokens
- **Chinese Cybercrime Networks**: Operating massive AI-powered phishing services using over one million URLs, disrupted by FBI in coordination with Google and Black Lotus Labs
- **Outsider Enterprise**: Chinese phishing-as-a-service operation dismantled by FBI with thousands of phishing websites
- **Conti Ransomware Operators**: Ukrainian national pleaded guilty to conspiracy charges related to ransomware operations
- **Sniper Dz Operators**: Decade-long phishing-as-a-service platform disrupted by INTERPOL Operation Ramz with administrator arrested