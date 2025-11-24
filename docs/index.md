# Exploitation Report

Current threat intelligence indicates several critical exploitation campaigns actively targeting enterprise infrastructure. Most notably, CISA has added an Oracle Identity Manager zero-day vulnerability (CVE-2025-61757) to its Known Exploited Vulnerabilities catalog, confirming active exploitation in the wild. Additionally, major data breaches have occurred through vendor compromises, including Cox Enterprises suffering a breach via an Oracle E-Business Suite zero-day flaw. Chinese APT groups continue sophisticated espionage operations, with APT31 targeting Russian IT infrastructure and APT24 conducting long-term surveillance campaigns against Taiwan using previously unknown malware. Multiple maximum severity vulnerabilities are also being disclosed, including a CVSS 10.0 flaw in Grafana Enterprise that enables privilege escalation and administrative impersonation.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: Critical remote code execution vulnerability in Oracle Identity Manager that allows attackers to execute arbitrary commands on affected systems
- **Impact**: Complete system compromise, unauthorized access to identity management infrastructure, potential lateral movement across enterprise networks
- **Status**: Actively exploited in the wild, added to CISA KEV catalog requiring immediate patching for federal agencies
- **CVE ID**: CVE-2025-61757

### Oracle E-Business Suite Zero-Day Flaw
- **Description**: Zero-day vulnerability in Oracle E-Business Suite that enabled unauthorized access to corporate networks
- **Impact**: Data breach exposing personal information of employees and customers, network compromise at major enterprises
- **Status**: Exploited against Cox Enterprises, patch status unknown from provided information

### Grafana Enterprise SCIM Vulnerability
- **Description**: Maximum severity flaw in Grafana Enterprise's SCIM (System for Cross-domain Identity Management) implementation
- **Impact**: Privilege escalation to administrative access, user impersonation attacks, complete compromise of monitoring infrastructure
- **Status**: Patches released by Grafana Labs
- **CVE ID**: CVE-2025-41115

## Affected Systems and Products

- **Oracle Identity Manager**: Federal agencies and enterprises using identity management solutions
- **Oracle E-Business Suite**: Enterprise resource planning systems at major corporations like Cox Enterprises
- **Grafana Enterprise**: Organizations using Grafana's commercial monitoring and visualization platform
- **WhatsApp API**: Contact discovery functionality affecting 3.5 billion potential user accounts
- **Russian IT Infrastructure**: Multiple organizations targeted by Chinese APT31 operations
- **Taiwan Government and Private Sector**: Over 1,000 domains compromised in APT24 espionage campaign
- **Salesforce Customers**: Organizations using Gainsight third-party application integration
- **LINE Messaging Platform**: Asian users vulnerable to message replay and impersonation attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging unpatched vulnerabilities in Oracle products for initial access
- **Third-Party Application Abuse**: Threat actors using legitimate tools like ScreenConnect and Gainsight to maintain persistence
- **API Rate Limiting Bypass**: WhatsApp contact discovery API exploited to scrape billions of phone numbers
- **Browser Notification Hijacking**: Matrix Push C2 platform using browser notifications for cross-platform phishing
- **Cloud Service Abuse**: APT31 utilizing legitimate cloud services to mask malicious activities
- **SCIM Protocol Exploitation**: Grafana vulnerability allowing authentication bypass and privilege escalation
- **Custom Protocol Weaknesses**: LINE messaging app's proprietary protocol enabling message replay attacks

## Threat Actor Activities

- **APT31 (Chinese State-Sponsored)**: Conducting stealthy cyberattacks against Russian IT sector using cloud services for command and control infrastructure
- **APT24 (Chinese State-Sponsored)**: Multi-year espionage campaign targeting Taiwan with BADAUDIO malware, compromising over 1,000 domains for intelligence collection
- **ShinyHunters Extortion Group**: Targeting Salesforce customers through third-party application compromise at Gainsight
- **Scattered Spider**: Teenage members involved in Transport for London breach, with insider threats feeding information to the group
- **Qilin Ransomware Operators**: Using rogue ScreenConnect access and failed infostealer attempts before deploying encryption payloads
- **Matrix Push C2 Operators**: Developing new command-and-control platform leveraging browser notifications for fileless attacks across multiple platforms