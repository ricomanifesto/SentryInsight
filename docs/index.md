# Exploitation Report

The current threat landscape reveals several critical exploitation activities, with zero-day vulnerabilities in enterprise systems being actively targeted by threat actors. CISA has identified active exploitation of a critical Oracle Identity Manager vulnerability (CVE-2025-61757) that enables remote code execution, while Grafana has addressed a maximum severity SCIM vulnerability (CVE-2025-41115) with a perfect CVSS score of 10.0. Meanwhile, sophisticated APT groups continue their espionage campaigns, with APT31 targeting Russian IT infrastructure and APT24 conducting multi-year operations against Taiwanese organizations using custom malware. Additionally, enterprise organizations face ongoing challenges with data breaches stemming from third-party vendor compromises and API vulnerabilities.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: A critical security flaw in Oracle Identity Manager that allows remote code execution
- **Impact**: Attackers can potentially gain full system control and execute arbitrary code remotely
- **Status**: Actively exploited in the wild; CISA has added it to the Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-61757

### Oracle E-Business Suite Zero-Day Exploit
- **Description**: A zero-day vulnerability in Oracle E-Business Suite that was exploited to breach Cox Enterprises
- **Impact**: Unauthorized access to corporate networks and exposure of personal data
- **Status**: Exploited in successful breach; patch status unclear

### Grafana SCIM Maximum Severity Vulnerability
- **Description**: A critical flaw in Grafana's SCIM (System for Cross-domain Identity Management) implementation
- **Impact**: Enables privilege escalation and user impersonation, allowing attackers to treat new users as administrators
- **Status**: Patches released; CVSS score of 10.0 indicates maximum severity
- **CVE ID**: CVE-2025-41115

### WhatsApp API Rate Limiting Vulnerability
- **Description**: A contact-discovery API flaw lacking proper rate limiting controls
- **Impact**: Researchers were able to compile a list of 3.5 billion WhatsApp phone numbers and associated personal information
- **Status**: Vulnerability disclosed; demonstrates massive data exposure potential

## Affected Systems and Products

- **Oracle Identity Manager**: Critical vulnerability enabling remote code execution
- **Oracle E-Business Suite**: Zero-day flaw exploited in enterprise breaches
- **Grafana Enterprise**: Maximum severity SCIM vulnerability affecting user privilege management
- **WhatsApp API**: Contact discovery service lacking rate limiting protections
- **Windows 11 Systems**: Gaming performance issues caused by October security updates affecting 24H2 and 25H2 versions
- **ScreenConnect**: Used as attack vector in Qilin ransomware operations
- **Salesforce via Gainsight**: Third-party application vulnerabilities exposing customer data

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers targeting unpatched vulnerabilities in enterprise identity management systems
- **Third-Party Vendor Compromise**: Supply chain attacks through compromised vendor systems affecting organizations like Iberia and Salesforce customers
- **API Abuse**: Exploitation of rate limiting weaknesses to conduct massive data harvesting operations
- **Browser Notification Phishing**: Matrix Push C2 platform leveraging browser notifications for fileless, cross-platform attacks
- **Ransomware via Remote Access**: Qilin ransomware operations using rogue ScreenConnect access for initial compromise
- **Cloud Service Abuse**: APT31 using legitimate cloud services to mask malicious activities in targeted attacks

## Threat Actor Activities

- **APT31**: China-linked group conducting stealthy cyberattacks against Russian IT sector using cloud services to mask activities between 2024-2025
- **APT24**: China-nexus threat actor deploying BADAUDIO malware in years-long espionage campaign targeting Taiwan and over 1,000 domains
- **ShinyHunters**: Extortion group exploiting third-party applications to steal Salesforce customer data via Gainsight platform
- **Qilin Ransomware Group**: Sophisticated operations using ScreenConnect for initial access, followed by infostealer attempts and ransomware deployment
- **Scattered Lapsus$ Hunters**: Insider threat operations with confirmed CrowdStrike employee providing internal screenshots to external hackers
- **Scattered Spider**: British teenagers involved in Transport for London breach causing millions in damages and customer data exposure