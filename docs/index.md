# Exploitation Report

Critical vulnerabilities are currently being exploited in the wild, with the most severe being a zero-day flaw in Oracle Identity Manager that enables remote code execution and has been added to CISA's Known Exploited Vulnerabilities catalog. Additionally, a maximum severity vulnerability in Grafana Enterprise allows admin privilege escalation and user impersonation. Meanwhile, threat actors continue exploiting Oracle E-Business Suite zero-day flaws for data breaches, and sophisticated campaigns are leveraging browser notifications for fileless attacks across multiple platforms.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Remote Code Execution
- **Description**: A critical security flaw in Oracle Identity Manager that allows remote code execution
- **Impact**: Attackers can gain full system control and execute arbitrary code remotely
- **Status**: Actively exploited in the wild; CISA has added it to the Known Exploited Vulnerabilities catalog requiring government agencies to patch immediately
- **CVE ID**: CVE-2025-61757

### Oracle E-Business Suite Zero-Day
- **Description**: A zero-day vulnerability in Oracle E-Business Suite that enabled unauthorized access to corporate networks
- **Impact**: Data breach exposing personal information of affected individuals
- **Status**: Exploited by hackers in Cox Enterprises breach; patch status unknown

### Grafana Enterprise SCIM Vulnerability
- **Description**: A maximum severity flaw in Grafana's SCIM (System for Cross-domain Identity Management) implementation
- **Impact**: Allows privilege escalation to administrator level and user impersonation attacks
- **Status**: Recently patched by Grafana Labs with security updates
- **CVE ID**: CVE-2025-41115

### WhatsApp Contact Discovery API Flaw
- **Description**: A rate limiting vulnerability in WhatsApp's contact-discovery API
- **Impact**: Enabled scraping of 3.5 billion WhatsApp phone numbers and associated personal information
- **Status**: Exploited by researchers to demonstrate data exposure risks

## Affected Systems and Products

- **Oracle Identity Manager**: Critical vulnerability affecting identity management systems
- **Oracle E-Business Suite**: Zero-day exploited in Cox Enterprises data breach
- **Grafana Enterprise**: SCIM implementation vulnerability with CVSS 10.0 severity score
- **WhatsApp API**: Contact discovery system lacking proper rate limiting controls
- **Windows 11 Systems**: Gaming performance issues from October security updates affecting versions 24H2 and 25H2
- **Gainsight Applications**: Third-party Salesforce applications enabling unauthorized data access
- **LINE Messaging App**: Custom protocol vulnerabilities exposing Asian users to cyber espionage

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct targeting of unpatched vulnerabilities in Oracle products for initial access
- **API Abuse**: Exploiting rate limiting flaws to scrape massive datasets from messaging platforms
- **OAuth Token Manipulation**: Using third-party application access to steal Salesforce customer data
- **Browser Notification Hijacking**: Matrix Push C2 platform leveraging browser notifications for fileless, cross-platform phishing
- **SCIM Protocol Abuse**: Exploiting identity management flaws for privilege escalation and impersonation
- **Cloud Service Abuse**: APT31 using legitimate cloud services for stealthy operations against Russian IT infrastructure

## Threat Actor Activities

- **APT31 (China-linked)**: Conducting stealthy cyberattacks against Russian IT sector using cloud services between 2024-2025
- **APT24 (China-nexus)**: Deploying BADAUDIO malware in multi-year espionage campaign targeting Taiwan and over 1,000 domains
- **ShinyHunters Group**: Exploiting Gainsight OAuth applications to steal Salesforce customer data in repeat attack pattern
- **Qilin Ransomware Operators**: Using rogue ScreenConnect access and failed infostealer attempts before ransomware deployment
- **Scattered Spider**: British teenagers involved in Transport for London breach causing millions in damage
- **CrowdStrike Insider Threat**: Internal employee sharing sensitive screenshots with external hackers via Telegram