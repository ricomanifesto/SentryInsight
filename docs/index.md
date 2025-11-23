# Exploitation Report

Current exploitation activity reveals several critical zero-day vulnerabilities actively being exploited in the wild, with Oracle systems bearing the brunt of recent attacks. The most severe incident involves CVE-2025-61757, a zero-day remote code execution flaw in Oracle Identity Manager that CISA has added to its Known Exploited Vulnerabilities catalog due to active exploitation. Additionally, Oracle E-Business Suite has been compromised through zero-day attacks, leading to significant data breaches at major enterprises. State-sponsored activities continue to escalate with Chinese APT groups conducting sophisticated campaigns against Russian IT infrastructure and deploying new persistent access malware against Taiwan and other regional targets.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day RCE
- **Description**: Critical remote code execution vulnerability in Oracle Identity Manager allowing attackers to execute arbitrary code remotely
- **Impact**: Complete system compromise, potential lateral movement, and unauthorized access to identity management systems
- **Status**: Actively exploited in the wild, CISA has added to KEV catalog requiring federal agencies to patch
- **CVE ID**: CVE-2025-61757

### Oracle E-Business Suite Zero-Day
- **Description**: Unpatched vulnerability in Oracle E-Business Suite exploited to breach enterprise networks
- **Impact**: Data breach exposing personal information of impacted individuals, unauthorized network access
- **Status**: Actively exploited, led to confirmed data breach at Cox Enterprises

### Grafana Enterprise SCIM Vulnerability
- **Description**: Maximum severity flaw in Grafana Enterprise's SCIM (System for Cross-domain Identity Management) implementation
- **Impact**: Privilege escalation allowing attackers to treat new users as administrators or escalate existing privileges
- **Status**: Patched by vendor, CVSS score of 10.0
- **CVE ID**: CVE-2025-41115

### WhatsApp Contact Discovery API Flaw
- **Description**: Rate limiting vulnerability in WhatsApp's contact discovery API allowing mass data scraping
- **Impact**: Exposed 3.5 billion WhatsApp accounts and associated personal information through automated scraping
- **Status**: Exploited by researchers, demonstrates large-scale data exposure potential

## Affected Systems and Products

- **Oracle Identity Manager**: All versions vulnerable to zero-day RCE attack
- **Oracle E-Business Suite**: Affected by separate zero-day vulnerability leading to data breaches
- **Grafana Enterprise**: SCIM implementation vulnerable to privilege escalation
- **WhatsApp Platform**: Contact discovery API lacks proper rate limiting controls
- **LINE Messaging App**: Multiple vulnerabilities enabling message replay attacks and impersonation
- **Gainsight Applications**: OAuth-linked applications enabling unauthorized Salesforce data access
- **ScreenConnect**: Used as attack vector in Qilin ransomware campaigns

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Targeting unpatched Oracle products for initial access and system compromise
- **API Abuse**: Exploiting rate limiting flaws in contact discovery systems for mass data collection
- **OAuth Token Abuse**: Leveraging third-party application tokens for unauthorized cloud platform access
- **Browser Push Notifications**: Using Matrix Push C2 platform for fileless, cross-platform phishing attacks
- **Remote Access Tool Abuse**: Exploiting legitimate tools like ScreenConnect for persistent access
- **Custom Protocol Exploitation**: Targeting proprietary messaging protocols for espionage activities

## Threat Actor Activities

- **APT31 (China-linked)**: Conducting stealthy cyberattacks against Russian IT sector using cloud services for command and control operations
- **APT24 (China-nexus)**: Deploying BADAUDIO malware for years-long espionage campaigns targeting Taiwan and over 1,000 domains
- **ShinyHunters Group**: Exploiting Salesforce customers through Gainsight third-party application compromise
- **Qilin Ransomware Operators**: Utilizing ScreenConnect for initial access and deploying ransomware payloads
- **Scattered Spider**: British teenagers involved in Transport for London breach causing millions in damages
- **Matrix Push C2 Users**: Leveraging browser notifications for cross-platform phishing distribution