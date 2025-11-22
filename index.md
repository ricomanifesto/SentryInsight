# Exploitation Report

Critical active exploitation is currently targeting Oracle Identity Manager systems through a zero-day remote code execution vulnerability, prompting CISA to add it to the Known Exploited Vulnerabilities catalog. Concurrently, threat actors are leveraging innovative attack vectors including browser notification hijacking through the Matrix Push C2 platform and exploiting OAuth applications to gain unauthorized access to Salesforce customer data. Advanced persistent threats, particularly APT24, continue long-term espionage campaigns using sophisticated malware like BADAUDIO, while maximum severity vulnerabilities in enterprise software platforms like Grafana pose significant privilege escalation risks.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: A critical remote code execution vulnerability affecting Oracle Identity Manager that allows attackers to execute arbitrary code on vulnerable systems
- **Impact**: Complete system compromise and unauthorized access to identity management infrastructure
- **Status**: Actively exploited in the wild; CISA has added this to the Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-61757

### Grafana Enterprise SCIM Vulnerability
- **Description**: A maximum severity vulnerability in Grafana Enterprise's SCIM (System for Cross-domain Identity Management) implementation that enables user impersonation and privilege escalation
- **Impact**: Attackers can impersonate administrators or escalate privileges within Grafana environments
- **Status**: Recently patched by Grafana Labs
- **CVE ID**: CVE-2025-41115

### Matrix Push C2 Browser Notification Exploitation
- **Description**: A novel command-and-control platform that hijacks browser notifications to conduct fileless, cross-platform phishing attacks
- **Impact**: Distribution of malicious links through trusted browser notification mechanisms, bypassing traditional security controls
- **Status**: Active exploitation observed across multiple platforms

### Gainsight OAuth Application Compromise
- **Description**: Unauthorized access to Salesforce customer data through compromised OAuth applications published by Gainsight
- **Impact**: Data theft from Salesforce organizations, similar to previous ShinyHunters group attacks during summer 2024
- **Status**: Active investigation by Salesforce; unusual activity detected in Gainsight-linked applications

## Affected Systems and Products

- **Oracle Identity Manager**: All versions vulnerable to the zero-day RCE exploit
- **Grafana Enterprise**: Versions with SCIM configuration enabled
- **Salesforce Platform**: Organizations using Gainsight-published OAuth applications
- **Browser Platforms**: Cross-platform impact affecting Chrome, Firefox, Safari, and other major browsers
- **LINE Messaging App**: Asian users exposed through custom protocol vulnerabilities enabling message replays and impersonation
- **Router Infrastructure**: Chinese organizations targeted by PlushDaemon APT through compromised router firmware

## Attack Vectors and Techniques

- **Browser Notification Hijacking**: Malicious actors leverage trusted browser notification systems to deliver phishing content without traditional malware installation
- **OAuth Application Abuse**: Exploitation of third-party OAuth applications to gain unauthorized access to cloud platforms like Salesforce
- **Zero-Day Exploitation**: Direct targeting of unpatched Oracle Identity Manager systems for remote code execution
- **Router Firmware Compromise**: PlushDaemon APT infects router firmware to hijack software update processes
- **SCIM Protocol Abuse**: Manipulation of identity management protocols in Grafana Enterprise for privilege escalation
- **Custom Protocol Exploitation**: LINE messaging app vulnerabilities allow message replay attacks and sensitive information exposure

## Threat Actor Activities

- **APT24 (China-linked)**: Conducting three-year espionage campaign using BADAUDIO malware, targeting Taiwan and over 1,000 domains with sophisticated persistence mechanisms
- **ShinyHunters Group**: Continuing attacks against Salesforce customers through third-party application compromises, repeating tactics from summer 2024 campaigns
- **PlushDaemon APT (China-sponsored)**: Targeting primarily Chinese organizations through router compromise and software update hijacking techniques
- **Matrix Push C2 Operators**: Developing and deploying innovative browser notification-based phishing infrastructure for cross-platform attacks
- **CrowdStrike Insider Threat**: Internal employee confirmed to be feeding sensitive information to external hackers, with evidence shared on Telegram through Scattered Lapsus$ Hunters
- **Scattered Spider Group**: British teenagers involved in Transport for London breach causing millions in damages and customer data exposure