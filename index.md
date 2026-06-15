# Exploitation Report

Critical exploitation activity continues to surge across multiple platforms and systems, with threat actors actively targeting zero-day vulnerabilities and recently disclosed flaws. Most concerning is the ShinyHunters group's exploitation of an Oracle PeopleSoft zero-day vulnerability affecting numerous universities, alongside active exploitation of Splunk Enterprise and Ivanti Sentry vulnerabilities. Chinese threat actors have demonstrated sophisticated persistence techniques, maintaining access to systems for nearly a decade through backdoored authentication flows and Linux login systems. The compromise of over 400 Arch Linux packages and ongoing phishing-as-a-service operations highlight the expanding attack surface that organizations must defend against.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Oracle PeopleSoft enterprise systems that allows attackers to breach systems and access sensitive data
- **Impact**: Complete system compromise, data theft, and extortion demands against organizations
- **Status**: Actively exploited by ShinyHunters group, particularly targeting universities
- **CVE ID**: CVE-2026-35273

### Splunk Enterprise Critical Flaw
- **Description**: A critical security flaw in Splunk Enterprise that allows unauthenticated file operations and remote code execution
- **Impact**: Complete system compromise without requiring authentication credentials
- **Status**: Security updates released by Splunk to address the vulnerability

### Ivanti Sentry Vulnerability
- **Description**: An actively exploited vulnerability in Ivanti Sentry systems
- **Impact**: System compromise and potential lateral movement within enterprise environments
- **Status**: Under active exploitation; CISA has mandated federal agencies patch within three days

### phpBB Authentication Bypass
- **Description**: A 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators
- **Status**: Recently patched after being present for a decade

### LangGraph Security Flaws
- **Description**: Three security flaws in LangGraph including a critical vulnerability chain
- **Impact**: Remote code execution on self-hosted AI agents
- **Status**: Vulnerabilities have been patched

## Affected Systems and Products

- **Oracle PeopleSoft**: Enterprise resource planning systems, particularly affecting American universities
- **Splunk Enterprise**: Data analytics and monitoring platforms across enterprise environments
- **Ivanti Sentry**: Enterprise security and management systems in federal agencies
- **Arch Linux AUR**: Over 400 packages in the Arch User Repository compromised with malware
- **phpBB Forums**: Forum software installations running vulnerable versions
- **Linux Systems**: Authentication systems backdoored by Chinese threat actors
- **LangGraph Platforms**: Self-hosted AI agent systems
- **French Government Systems**: Tchap encrypted messaging platform affecting over 73,000 accounts

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise systems
- **Supply Chain Attacks**: Compromise of software repositories and package distribution systems
- **Authentication Bypass**: Circumventing login mechanisms to gain unauthorized access
- **Backdoor Installation**: Long-term persistence through compromised authentication flows
- **AI-Powered Phishing**: Use of artificial intelligence to enhance phishing campaign effectiveness
- **Package Hijacking**: Takeover of legitimate software packages to distribute malware
- **Remote Code Execution**: Execution of malicious code on target systems without authentication
- **eBPF Rootkit Deployment**: Advanced rootkit techniques for maintaining persistence on Linux systems

## Threat Actor Activities

- **ShinyHunters Group**: Actively exploiting Oracle PeopleSoft zero-day to breach universities and conduct data extortion operations
- **Chinese Threat Actors**: Maintaining decade-long persistence in target networks through backdoored Linux authentication systems and hijacked authentication flows
- **Vervain Team**: China-nexus group tracked by Sygnia, hidden inside Linux login systems for nearly a decade
- **Arch Linux Attackers**: Compromised over 400 AUR packages to deploy credential stealers and eBPF rootkits
- **Phishing-as-a-Service Operators**: Multiple groups operating large-scale phishing platforms, including Outsider Enterprise and Sniper Dz
- **Conti Ransomware Operation**: Continued legal actions against operators of the dismantled ransomware group
- **AI-Enhanced Phishing Groups**: Chinese cybercrime networks using Gemini AI for sophisticated phishing campaigns