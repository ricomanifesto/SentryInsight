# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited in the wild, with CISA adding CVE-2025-61757 affecting Oracle Identity Manager to its Known Exploited Vulnerabilities catalog due to active exploitation. Cox Enterprises suffered a significant data breach through exploitation of a zero-day flaw in Oracle E-Business Suite, while threat actors continue to abuse third-party applications like Gainsight to compromise Salesforce customer data. Additional high-severity vulnerabilities include a maximum severity SCIM flaw in Grafana Enterprise (CVE-2025-41115) and a WhatsApp API vulnerability that enabled massive data scraping operations affecting 3.5 billion accounts.

## Active Exploitation Details

### Oracle Identity Manager Remote Code Execution Vulnerability
- **Description**: A critical security flaw in Oracle Identity Manager that allows remote code execution
- **Impact**: Attackers can potentially gain full control of affected systems and execute arbitrary code remotely
- **Status**: Actively exploited in the wild; CISA has added it to the KEV catalog requiring federal agencies to patch by a specified deadline
- **CVE ID**: CVE-2025-61757

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: An unpatched zero-day vulnerability in Oracle E-Business Suite that was exploited to breach Cox Enterprises
- **Impact**: Enabled unauthorized access to corporate networks and exposure of personal data belonging to impacted individuals
- **Status**: Zero-day vulnerability that was exploited before patches were available

### Grafana Enterprise SCIM Vulnerability
- **Description**: A maximum severity vulnerability in Grafana Enterprise's SCIM implementation that enables user impersonation and privilege escalation
- **Impact**: Attackers can treat new users as administrators or escalate privileges within the system
- **Status**: Patches have been released by Grafana Labs
- **CVE ID**: CVE-2025-41115

### WhatsApp API Contact Discovery Flaw
- **Description**: A vulnerability in WhatsApp's contact-discovery API that lacked proper rate limiting controls
- **Impact**: Enabled researchers to scrape 3.5 billion WhatsApp mobile phone numbers and associated personal information
- **Status**: Vulnerability was demonstrated by security researchers and has been disclosed

## Affected Systems and Products

- **Oracle Identity Manager**: All versions affected by the actively exploited RCE vulnerability
- **Oracle E-Business Suite**: Vulnerable to zero-day exploitation that resulted in the Cox Enterprises breach
- **Grafana Enterprise**: Affected by the maximum severity SCIM vulnerability enabling admin spoofing
- **WhatsApp Platform**: API vulnerability affecting contact discovery functionality across the global user base
- **Salesforce Platforms**: Customers affected through unauthorized access via compromised Gainsight OAuth applications
- **LINE Messaging Application**: Custom protocol vulnerabilities enabling message replays and impersonation attacks

## Attack Vectors and Techniques

- **Remote Code Execution**: Exploitation of Oracle Identity Manager vulnerability to gain system control
- **Zero-Day Exploitation**: Attackers leveraging unpatched Oracle E-Business Suite vulnerabilities
- **API Rate Limiting Abuse**: Mass data scraping through WhatsApp's inadequately protected contact discovery API
- **OAuth Application Compromise**: Unauthorized access to Salesforce data through compromised third-party Gainsight applications
- **Privilege Escalation**: Exploitation of Grafana SCIM vulnerability to gain administrative access
- **Browser Notification Abuse**: Matrix Push C2 platform using browser notifications for fileless, cross-platform phishing attacks
- **Custom Protocol Exploitation**: Abuse of LINE messaging app's leaky custom protocol for message replays and impersonation

## Threat Actor Activities

- **APT31 (China-linked)**: Conducting stealthy cyberattacks against Russian IT sector between 2024-2025 using cloud services for infrastructure
- **APT24 (China-nexus)**: Deploying BADAUDIO malware in years-long espionage campaign targeting Taiwan and over 1,000 domains for persistent remote access
- **ShinyHunters Extortion Group**: Affiliated threat actors exploiting third-party applications to steal Salesforce customer data in repeat attacks
- **Qilin Ransomware Operators**: Conducting sophisticated ransomware attacks using rogue ScreenConnect access and failed infostealer attempts
- **Scattered Spider Affiliates**: British teenagers charged in connection with Transport for London breach causing millions in damage and customer data exposure
- **Matrix Push C2 Operators**: Bad actors leveraging new command-and-control platform for browser notification-based phishing campaigns
- **CrowdStrike Insider Threat**: Internal employee confirmed to be feeding information and screenshots to external hackers via Telegram channels