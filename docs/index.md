# Exploitation Report

The cybersecurity landscape is experiencing significant exploitation activity across multiple platforms and products. Critical vulnerabilities are being actively exploited in Oracle PeopleSoft systems, Ivanti Sentry solutions, and Splunk Enterprise platforms, with threat actors moving rapidly to capitalize on newly disclosed flaws. Notable campaigns include ShinyHunters leveraging a zero-day vulnerability to target educational institutions, Chinese-linked threat actors maintaining decade-long persistence in authentication systems, and widespread compromise of Linux package repositories. The rapid exploitation of vulnerabilities within 24 hours of disclosure demonstrates attackers' sophisticated preparation and monitoring capabilities.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Attackers can break into enterprise systems, steal data, and demand payment to keep information private
- **Status**: Actively exploited by ShinyHunters extortion crew; Oracle has implemented mitigations
- **CVE ID**: CVE-2026-35273

### Ivanti Sentry Maximum Severity Flaw
- **Description**: Critical vulnerability in Ivanti Sentry solutions with maximum severity rating
- **Impact**: Allows attackers to compromise systems and gain unauthorized access
- **Status**: Actively exploited within 24 hours of disclosure; CISA has mandated federal agencies patch within three days
- **CVE ID**: Not specified in the articles

### Splunk Enterprise Critical Flaw
- **Description**: Critical security vulnerability in Splunk Enterprise enabling unauthenticated file operations
- **Impact**: Allows remote code execution without authentication requirements
- **Status**: Security updates released by Splunk to address the vulnerability
- **CVE ID**: Not specified in the articles

### phpBB Authentication Bypass
- **Description**: 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators
- **Status**: Fixed in recent phpBB security update
- **CVE ID**: Not specified in the articles

### LangGraph Security Flaws
- **Description**: Chain of three security vulnerabilities in LangGraph affecting self-hosted AI agents
- **Impact**: Could result in remote code execution on systems running AI agents
- **Status**: All vulnerabilities have been patched
- **CVE ID**: Not specified in the articles

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning software, particularly affecting American universities
- **Ivanti Sentry**: Security solutions used by federal agencies and enterprises
- **Splunk Enterprise**: Data analytics and monitoring platform
- **phpBB Forum Software**: Open-source forum platform with decade-old vulnerability
- **Arch User Repository (AUR)**: Over 400 packages compromised to distribute malware
- **LangGraph**: AI agent framework for self-hosted deployments
- **Linux Authentication Systems**: PAM modules targeted for long-term persistence

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Rapid exploitation of previously unknown vulnerabilities in Oracle PeopleSoft
- **Authentication Hijacking**: Chinese threat actors compromising authentication stacks for persistent access
- **Supply Chain Attacks**: Compromise of AUR packages to distribute rootkits and infostealers
- **Package Repository Hijacking**: Rewriting build scripts in legitimate software packages
- **AI Agent Manipulation**: Agentjacking attacks tricking AI coding agents into running malicious code
- **Phishing-as-a-Service**: Use of platforms like Sniper Dz for coordinated phishing campaigns

## Threat Actor Activities

- **ShinyHunters**: Actively exploiting Oracle PeopleSoft zero-day to target universities and steal data for extortion
- **Chinese-Linked Groups**: Maintaining decade-long persistence in authentication systems and Linux login software
- **Conti Ransomware Operation**: Ukrainian national pleading guilty to conspiracy charges related to ransomware activities
- **Chinese Smishing Network**: Using Google's Gemini AI to enhance phishing text message campaigns
- **AudiA6 Operators**: Running cryptocurrency laundering service for ransomware gangs before Europol disruption
- **Sniper Dz Administrators**: Operating decade-long phishing-as-a-service platform before INTERPOL takedown