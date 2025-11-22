# Exploitation Report

Critical security vulnerabilities are being actively exploited across multiple enterprise platforms, with CISA highlighting a zero-day Oracle Identity Manager vulnerability (CVE-2025-61757) that poses immediate threats to government agencies. Simultaneously, threat actors are leveraging sophisticated techniques including browser notification hijacking, OAuth token abuse through third-party applications, and advanced persistent threat campaigns targeting Asian infrastructure. The security landscape shows increased activity from state-sponsored groups, particularly Chinese APT organizations conducting multi-year espionage operations, while cybercriminals exploit enterprise software vulnerabilities for privilege escalation and data theft.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: A critical remote code execution vulnerability in Oracle Identity Manager that has been added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: Attackers can achieve remote code execution on vulnerable Oracle Identity Manager systems, potentially leading to complete system compromise
- **Status**: Actively exploited in the wild, with CISA warning government agencies to patch immediately
- **CVE ID**: CVE-2025-61757

### Grafana Enterprise SCIM Vulnerability
- **Description**: A maximum severity vulnerability in Grafana Enterprise's SCIM (System for Cross-domain Identity Management) implementation that enables user impersonation and privilege escalation
- **Impact**: Attackers can treat new users as administrators or escalate privileges within Grafana Enterprise environments
- **Status**: Recently patched, but represents a critical security flaw with maximum CVSS score
- **CVE ID**: CVE-2025-41115

### Matrix Push C2 Browser Notification Exploitation
- **Description**: A new command-and-control platform that leverages browser notifications as a vector for phishing attacks and malicious link distribution
- **Impact**: Enables fileless, cross-platform attacks that bypass traditional detection methods through legitimate browser notification mechanisms
- **Status**: Active exploitation observed with new C2 infrastructure

## Affected Systems and Products

- **Oracle Identity Manager**: Critical RCE vulnerability affecting enterprise identity management systems
- **Grafana Enterprise**: SCIM implementation vulnerability in enterprise monitoring and observability platforms
- **Salesforce Platform**: Unauthorized data access through compromised Gainsight OAuth applications
- **Browser Applications**: Cross-platform exploitation through notification mechanisms (Chrome, Firefox, Safari, Edge)
- **LINE Messaging App**: Custom protocol vulnerabilities affecting Asian users with message replay and impersonation risks
- **Network Infrastructure**: Router compromises by Chinese APT groups for software update hijacking
- **Windows 11 Systems**: Gaming performance issues linked to October security updates

## Attack Vectors and Techniques

- **Browser Notification Hijacking**: Exploitation of legitimate browser notification systems to deliver phishing content and malicious links
- **OAuth Token Abuse**: Unauthorized access to Salesforce data through compromised third-party application tokens (Gainsight)
- **Software Update Hijacking**: Chinese APT groups compromising routers to intercept and modify software updates
- **SCIM Protocol Exploitation**: Abuse of identity management protocols to achieve privilege escalation
- **Message Protocol Manipulation**: Exploitation of custom messaging protocols for replay attacks and user impersonation
- **Zero-Day Exploitation**: Active exploitation of unpatched Oracle Identity Manager vulnerabilities

## Threat Actor Activities

- **APT24 (Chinese State-Sponsored)**: Conducting multi-year espionage campaigns using BADAUDIO malware, targeting Taiwan and over 1,000 domains with persistent remote access capabilities
- **ShinyHunters Extortion Group**: Targeting Salesforce customers through third-party application compromises, similar to previous summer attacks
- **PlushDaemon (Chinese APT)**: Infecting routers to hijack software updates, primarily targeting Chinese organizations while evading detection
- **Scattered Spider**: British teenagers involved in Transport for London breach causing millions in damages and customer data exposure
- **Matrix Push Operators**: Cybercriminals deploying new C2 infrastructure for cross-platform phishing campaigns through browser notifications
- **CrowdStrike Insider Threat**: Internal employee sharing screenshots with hackers, later leaked on Telegram by Scattered Lapsus$ Hunters