# Exploitation Report

CISA has identified a critical zero-day vulnerability in Oracle Identity Manager (CVE-2025-61757) that is being actively exploited in the wild, allowing attackers to achieve remote code execution. Meanwhile, threat actors continue to leverage sophisticated attack vectors including browser notification hijacking through the Matrix Push C2 platform, unauthorized OAuth activity targeting Salesforce customers via Gainsight applications, and advanced persistent threat campaigns by Chinese-linked APT24 using the BADAUDIO malware. Additional critical vulnerabilities include a maximum severity SCIM flaw in Grafana Enterprise (CVE-2025-41115) enabling privilege escalation and admin impersonation, as well as security issues in LINE messaging that expose Asian users to potential cyber espionage.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: A critical remote code execution vulnerability in Oracle Identity Manager that allows attackers to execute arbitrary code on affected systems
- **Impact**: Complete system compromise, unauthorized access to identity management systems, potential lateral movement within enterprise networks
- **Status**: Currently being exploited in the wild; CISA has added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-61757

### Matrix Push C2 Browser Notification Hijacking
- **Description**: A fileless, cross-platform command-and-control platform that leverages browser push notifications to distribute malicious links and conduct phishing attacks
- **Impact**: Cross-platform phishing attacks, credential theft, initial access to victim systems without traditional malware deployment
- **Status**: Active threat being used by malicious actors for ongoing phishing campaigns

### Gainsight-Linked Salesforce Data Access
- **Description**: Unauthorized access to Salesforce customer data through compromised OAuth applications published by Gainsight, similar to previous summer attacks
- **Impact**: Exposure of sensitive customer data, potential data theft by ShinyHunters extortion group affiliates
- **Status**: Active incident with confirmed unauthorized data access detected by Salesforce

## Affected Systems and Products

- **Oracle Identity Manager**: All versions affected by the zero-day vulnerability requiring immediate patching
- **Grafana Enterprise**: Versions affected by SCIM vulnerability allowing admin spoofing and privilege escalation
- **Salesforce Platform**: Organizations using Gainsight-published OAuth applications experiencing unauthorized data access
- **LINE Messaging Application**: Asian users vulnerable to message replay attacks and sensitive information exposure
- **Web Browsers**: All major browsers susceptible to Matrix Push C2 notification hijacking attacks
- **Network Infrastructure**: Routers targeted by Chinese PlushDaemon APT for software update hijacking
- **Enterprise Networks**: Over 1,000+ domains affected by APT24 BADAUDIO malware campaigns

## Attack Vectors and Techniques

- **Browser Notification Abuse**: Hijacking push notification systems for fileless phishing attacks across multiple platforms
- **OAuth Application Compromise**: Exploiting third-party application integrations to gain unauthorized access to cloud platforms
- **Zero-Day Exploitation**: Remote code execution through unpatched Oracle Identity Manager vulnerabilities
- **SCIM Protocol Abuse**: Leveraging System for Cross-domain Identity Management flaws for privilege escalation
- **Router Compromise**: Infecting network devices to hijack legitimate software updates with malicious payloads
- **Message Protocol Manipulation**: Exploiting custom messaging protocols for replay attacks and impersonation
- **Persistent Malware Deployment**: Using BADAUDIO malware for long-term network access and espionage

## Threat Actor Activities

- **APT24 (Chinese-linked)**: Conducting three-year espionage campaign using BADAUDIO malware, targeting Taiwan and over 1,000 domains with sophisticated attack methods
- **PlushDaemon (Chinese APT)**: Targeting routers to hijack software updates, primarily focusing on Chinese organizations while evading detection
- **ShinyHunters Affiliates**: Exploiting Gainsight OAuth applications to steal Salesforce customer data in repeat attacks similar to previous summer incidents
- **Matrix Push Operators**: Deploying cross-platform C2 infrastructure leveraging browser notifications for widespread phishing operations
- **Scattered Spider**: British teenagers involved in Transport for London breach causing millions in damages and customer data exposure
- **Unknown Threat Actors**: Actively exploiting Oracle Identity Manager zero-day vulnerability prompting CISA emergency response