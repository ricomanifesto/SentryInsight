# Exploitation Report

The current threat landscape reveals several critical vulnerabilities under active exploitation, with Oracle Identity Manager facing zero-day exploitation and Grafana Enterprise experiencing a maximum severity authentication bypass flaw. Threat actors are leveraging innovative attack vectors including browser notifications for command and control operations, while established APT groups continue multi-year espionage campaigns using sophisticated malware. The cybersecurity community is also witnessing insider threats at major security firms and ongoing attacks against third-party integrations affecting cloud platforms.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: Critical security flaw in Oracle Identity Manager that enables remote code execution
- **Impact**: Attackers can achieve complete system compromise and establish persistent access to enterprise identity management systems
- **Status**: Currently being actively exploited in the wild; CISA has added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-61757

### Grafana Enterprise SCIM Authentication Bypass
- **Description**: Maximum severity vulnerability in Grafana Enterprise's SCIM (System for Cross-domain Identity Management) implementation that allows authentication bypass
- **Impact**: Enables privilege escalation and user impersonation, potentially granting administrative access to unauthorized users
- **Status**: Patches have been released; vulnerability carries maximum CVSS 10.0 severity score
- **CVE ID**: CVE-2025-41115

### Browser Notification Command and Control
- **Description**: Novel attack vector using browser push notifications to establish command and control communications through a platform called Matrix Push C2
- **Impact**: Enables fileless, cross-platform phishing attacks and malware distribution through legitimate browser notification systems
- **Status**: Active exploitation observed; represents emerging threat vector

## Affected Systems and Products

- **Oracle Identity Manager**: Enterprise identity management systems vulnerable to remote code execution
- **Grafana Enterprise**: Business intelligence and monitoring platforms with SCIM configurations affected
- **Web Browsers**: Cross-platform browser notification systems being hijacked for malicious communications
- **Salesforce Platforms**: Customer data exposed through compromised Gainsight OAuth applications
- **LINE Messaging Application**: Asian users facing exposure through custom protocol vulnerabilities
- **Network Routers**: Chinese-manufactured and other routers targeted by PlushDaemon malware for software update hijacking

## Attack Vectors and Techniques

- **Browser Notification Hijacking**: Malicious actors abuse legitimate browser push notification systems to deliver phishing content and establish C2 channels
- **OAuth Application Compromise**: Third-party applications with OAuth permissions being exploited to access cloud platform data
- **Software Update Hijacking**: Router infections used to intercept and modify legitimate software updates
- **SCIM Protocol Exploitation**: Authentication bypass through manipulation of identity management protocols
- **Custom Protocol Vulnerabilities**: Encrypted messaging applications with leaky protocols enabling message replay and impersonation attacks

## Threat Actor Activities

- **APT24 (China-linked)**: Conducting three-year espionage campaign using BADAUDIO malware, targeting over 1,000 domains with focus on Taiwan and sophisticated persistence mechanisms
- **PlushDaemon Group**: Chinese state-sponsored APT targeting routers to hijack software updates, primarily focusing on Chinese organizations to maintain stealth
- **ShinyHunters Extortion Group**: Exploiting third-party applications to steal Salesforce customer data in repeated attacks against cloud platform users
- **Scattered Spider**: British teenagers associated with the group facing charges related to Transport for London breach causing millions in damages
- **CrowdStrike Insider**: Internal employee confirmed to have shared sensitive screenshots with external hackers, subsequently leaked on Telegram by Scattered Lapsus$ Hunters