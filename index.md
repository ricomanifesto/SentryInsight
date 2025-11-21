# Exploitation Report

Current cybersecurity threat landscape reveals several critical vulnerabilities under active exploitation, with maximum severity flaws in enterprise systems presenting immediate risks. The most concerning activity includes a CVSS 10.0 vulnerability in Grafana Enterprise enabling administrative privilege escalation, ongoing exploitation of Ray AI framework vulnerabilities for cryptocurrency mining operations, and sophisticated espionage campaigns by state-sponsored actors. Multiple threat groups are leveraging unpatched systems, insider threats, and novel attack vectors including browser notification hijacking and Ethereum-based command and control infrastructure.

## Active Exploitation Details

### Grafana Enterprise SCIM Vulnerability
- **Description**: Maximum severity vulnerability in Grafana Enterprise's System for Cross-domain Identity Management (SCIM) functionality that allows attackers to treat new users as administrators or escalate privileges
- **Impact**: Complete administrative access to Grafana systems, potential for full system compromise and data exfiltration
- **Status**: Patches available, actively exploitable in unpatched systems
- **CVE ID**: CVE-2025-41115

### Ray AI Framework Security Flaw
- **Description**: Two-year-old unpatched vulnerability in the Ray open-source artificial intelligence framework being exploited to build self-spreading GPU cryptocurrency mining botnets
- **Impact**: Unauthorized cryptocurrency mining, resource consumption, potential lateral movement across AI clusters
- **Status**: Actively exploited in ShadowRay 2.0 campaigns targeting NVIDIA GPU clusters

### Palo Alto Networks GlobalProtect Portal Scanning
- **Description**: Massive reconnaissance campaign targeting GlobalProtect VPN portals with over 2.3 million scan sessions detected starting November 14, 2025
- **Impact**: Network reconnaissance, potential identification of vulnerable endpoints for future exploitation
- **Status**: Ongoing active scanning activity, no specific vulnerability exploitation confirmed

## Affected Systems and Products

- **Grafana Enterprise**: SCIM-enabled configurations vulnerable to administrative privilege escalation
- **Ray AI Framework**: Open-source AI clusters with NVIDIA GPUs targeted for cryptocurrency mining
- **Palo Alto Networks GlobalProtect**: VPN portals under intensive reconnaissance scanning
- **SonicWall SonicOS SSLVPN**: Firewalls vulnerable to denial-of-service attacks via high-severity flaw
- **Salesforce Platform**: Customer data exposed through Gainsight-linked OAuth application compromise
- **Windows Systems**: Targeted by Tsundere botnet using game-themed social engineering lures
- **FS Italiane Group**: Italian national railway data compromised via IT services provider breach

## Attack Vectors and Techniques

- **SCIM Protocol Exploitation**: Attackers manipulating cross-domain identity management to gain administrative privileges
- **AI Framework Compromise**: Self-spreading malware targeting distributed AI computing environments
- **OAuth Token Abuse**: Unauthorized access to cloud platforms through compromised third-party application tokens
- **Browser Notification Hijacking**: Matrix Push command-and-control tool leveraging browser notifications for phishing
- **Ethereum-Based C2**: Blockchain infrastructure used for botnet command and control communications
- **Social Engineering**: Game-themed lures used to distribute Windows-targeting malware
- **Supply Chain Attacks**: Compromising IT service providers to access downstream clients

## Threat Actor Activities

- **APT24**: China-linked group conducting three-year espionage campaign using BADAUDIO malware against Taiwan and over 1,000 domains
- **Scattered Spider**: British teenagers involved in Transport for London breach causing millions in damage and customer data exposure
- **PlushDaemon**: Chinese state-sponsored APT group infecting routers to hijack software updates, primarily targeting Chinese organizations
- **ShadowRay Operators**: Cybercriminals building GPU-based cryptocurrency mining botnets through Ray framework exploitation
- **CrowdStrike Insider Threat**: Internal actor sharing sensitive screenshots with external hackers via Telegram channels
- **Tsundere Botnet Operators**: Active since mid-2025, expanding Windows-targeting botnet using JavaScript execution capabilities