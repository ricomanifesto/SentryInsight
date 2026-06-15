# Exploitation Report

Current exploitation activity shows a concerning mix of zero-day attacks, supply chain compromises, and long-term persistent threats. The ShinyHunters group has actively exploited a critical Oracle PeopleSoft zero-day vulnerability (CVE-2026-35273) to breach numerous universities, while Chinese-linked threat actors have maintained decade-long persistence through backdoored Linux authentication systems. Additionally, over 400 Arch Linux packages have been compromised to distribute rootkits and infostealers, and critical vulnerabilities in Splunk Enterprise and phpBB forum software pose significant risks to organizational security. CISA has issued urgent patching directives for an actively exploited Ivanti Sentry vulnerability, highlighting the immediate threat landscape facing federal agencies.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical unpatched flaw in Oracle's PeopleSoft ERP software that allows unauthorized access to enterprise systems
- **Impact**: Attackers can break into systems, steal sensitive data, and conduct extortion campaigns
- **Status**: Actively exploited by ShinyHunters group, primarily targeting American universities
- **CVE ID**: CVE-2026-35273

### Ivanti Sentry Vulnerability
- **Description**: Critical security flaw in Ivanti Sentry platform being actively exploited in the wild
- **Impact**: Allows attackers to compromise federal government systems
- **Status**: Under active exploitation with CISA mandating emergency patching within three days

### Splunk Enterprise Critical Flaw
- **Description**: Critical security vulnerability enabling unauthenticated file operations and remote code execution
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Security updates released by Splunk to address the vulnerability

### phpBB Authentication Bypass
- **Description**: 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators
- **Status**: Recently patched after lurking undetected for a decade

### LangGraph Vulnerability Chain
- **Description**: Three security flaws in LangGraph affecting self-hosted AI agents
- **Impact**: Remote code execution on systems running AI coding agents
- **Status**: Now patched but previously exposed AI development environments

## Affected Systems and Products

- **Oracle PeopleSoft ERP**: Critical zero-day affecting enterprise resource planning systems, disproportionately impacting American universities
- **Ivanti Sentry**: Federal government systems under active attack requiring emergency patching
- **Splunk Enterprise**: Enterprise logging and analytics platform vulnerable to unauthenticated attacks
- **phpBB Forum Software**: Decade-old authentication bypass affecting forum administrators
- **Arch Linux AUR Packages**: Over 400 packages compromised in the Arch User Repository
- **LangGraph AI Framework**: Self-hosted AI agent platforms vulnerable to remote code execution
- **Linux Authentication Systems**: Long-term backdoors in login software affecting enterprise environments

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: ShinyHunters leveraging unpatched Oracle vulnerability for data theft and extortion
- **Supply Chain Poisoning**: Mass compromise of Arch Linux packages to distribute rootkits and credential stealers
- **Authentication Hijacking**: Chinese hackers maintaining decade-long persistence through backdoored Linux login systems
- **eBPF Rootkit Deployment**: Advanced Linux rootkit technology deployed through compromised AUR packages
- **AI Agent Manipulation**: Agentjacking attacks tricking AI coding agents into executing malicious code
- **Phishing-as-a-Service**: FBI disruption of massive AI-powered phishing operations using over one million URLs

## Threat Actor Activities

- **ShinyHunters**: Actively exploiting Oracle PeopleSoft zero-day (CVE-2026-35273) to breach universities and conduct data extortion campaigns
- **Chinese APT Groups**: Maintaining nearly decade-long persistence through backdoored Linux authentication systems with full administrative visibility
- **Chinese Phishing Networks**: Operating massive AI-powered phishing services and using Gemini AI for SMS phishing campaigns targeting Americans
- **Arch Linux Package Hijackers**: Compromised over 400 AUR packages to deploy sophisticated rootkits and infostealers targeting credentials and access tokens
- **Conti Ransomware Operation**: Ukrainian national pleaded guilty to conspiracy charges in connection with the notorious ransomware group
- **Sniper Dz PhaaS**: Decade-long phishing-as-a-service platform disrupted by INTERPOL Operation Ramz with administrator arrested