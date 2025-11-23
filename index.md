# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited in the wild, with the most severe being an Oracle Identity Manager remote code execution flaw (CVE-2025-61757) that CISA has added to its Known Exploited Vulnerabilities catalog. Additional significant exploitation activity includes a zero-day Oracle E-Business Suite vulnerability that enabled a data breach at Cox Enterprises, and a maximum severity SCIM flaw in Grafana Enterprise (CVE-2025-41115) that allows privilege escalation and user impersonation. Threat actors continue leveraging various attack vectors including API abuse for large-scale data harvesting, browser notifications for phishing campaigns, and OAuth applications for unauthorized Salesforce data access.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: Critical security flaw in Oracle Identity Manager that allows remote code execution
- **Impact**: Attackers can achieve remote code execution on vulnerable systems, potentially leading to complete system compromise
- **Status**: Currently being actively exploited in the wild; CISA has added to KEV catalog requiring federal agencies to patch
- **CVE ID**: CVE-2025-61757

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: Zero-day vulnerability in Oracle E-Business Suite that was exploited to breach Cox Enterprises
- **Impact**: Enabled unauthorized access to personal data and network infiltration
- **Status**: Zero-day exploitation confirmed in Cox Enterprises breach; patch status unclear

### Grafana Enterprise SCIM Vulnerability
- **Description**: Maximum severity vulnerability in Grafana Enterprise's SCIM (System for Cross-domain Identity Management) implementation
- **Impact**: Allows attackers to perform privilege escalation or user impersonation, potentially treating new users as administrators
- **Status**: Patches have been released by Grafana Labs
- **CVE ID**: CVE-2025-41115

### WhatsApp Contact Discovery API Vulnerability
- **Description**: Rate limiting flaw in WhatsApp's contact-discovery API that allowed mass data harvesting
- **Impact**: Researchers compiled 3.5 billion WhatsApp mobile phone numbers and associated personal information
- **Status**: Vulnerability has been exploited for large-scale data collection

## Affected Systems and Products

- **Oracle Identity Manager**: All versions vulnerable to the critical RCE flaw
- **Oracle E-Business Suite**: Zero-day exploitation confirmed affecting Cox Enterprises systems
- **Grafana Enterprise**: SCIM implementation vulnerable to maximum severity privilege escalation
- **WhatsApp API**: Contact-discovery endpoint lacking proper rate limiting controls
- **Salesforce Platform**: Unauthorized data access via compromised Gainsight OAuth applications
- **LINE Messaging App**: Custom protocol vulnerabilities enabling message replay and impersonation attacks
- **Windows 11 Systems**: Gaming performance issues caused by October security updates on 24H2 and 25H2 versions

## Attack Vectors and Techniques

- **Remote Code Execution**: Oracle Identity Manager exploitation enabling complete system compromise
- **API Abuse**: Mass data harvesting through rate limiting bypass in WhatsApp contact discovery
- **OAuth Application Compromise**: Unauthorized Salesforce data access through Gainsight-linked applications
- **Browser Notification Abuse**: Matrix Push C2 platform leveraging browser notifications for cross-platform phishing
- **Protocol Vulnerabilities**: LINE messaging app exploitation through leaky custom protocol implementation
- **Zero-Day Exploitation**: Oracle E-Business Suite compromise at Cox Enterprises
- **SCIM Implementation Flaws**: Privilege escalation and admin impersonation in Grafana Enterprise

## Threat Actor Activities

- **APT31 (China-linked)**: Conducting stealthy cyberattacks against Russian IT sector using cloud services infrastructure between 2024-2025
- **APT24 (China-nexus)**: Multi-year espionage campaign targeting Taiwan and over 1,000 domains using BADAUDIO malware for persistent access
- **ShinyHunters Group**: Exploiting third-party applications to steal Salesforce customer data via Gainsight compromise
- **Qilin Ransomware Operators**: Sophisticated attack chains involving rogue ScreenConnect access and failed infostealer deployment
- **Scattered Spider (Lapsus$ Hunters)**: Ongoing insider threats and data leaks, including CrowdStrike internal information sharing
- **Matrix Push C2 Operators**: Leveraging browser notifications for fileless, cross-platform phishing campaigns