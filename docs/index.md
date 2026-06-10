# Exploitation Report

Multiple critical zero-day vulnerabilities are currently being exploited in active attack campaigns, including CVE-2026-11645 in Chrome's V8 engine, CVE-2026-42271 in BerriAI LiteLLM, and CVE-2025-8088 in WinRAR. Microsoft has addressed three zero-day vulnerabilities and nearly 200 total flaws in their June 2026 Patch Tuesday release, marking a record-breaking security update cycle. Threat actors are actively targeting enterprise infrastructure through Check Point VPN systems, Veeam backup servers, and SAP enterprise applications, while supply chain attacks continue to compromise software repositories and package registries.

## Active Exploitation Details

### Chrome V8 Engine Zero-Day
- **Description**: High-severity vulnerability in Google Chrome's V8 JavaScript engine that allows arbitrary code execution
- **Impact**: Attackers can execute malicious code within the browser context, potentially leading to system compromise
- **Status**: Actively exploited in the wild, patches released by Google
- **CVE ID**: CVE-2026-11645

### BerriAI LiteLLM Authentication Bypass
- **Description**: High-severity flaw in BerriAI LiteLLM that can be chained with other vulnerabilities for unauthenticated remote code execution
- **Impact**: Complete system compromise through unauthenticated access and code execution
- **Status**: Actively exploited and added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-42271

### WinRAR Archive Processing Vulnerability
- **Description**: Security flaw in WinRAR archive processing that allows malicious code execution
- **Impact**: Deployment of credential stealers and data theft malware
- **Status**: Actively exploited by Russia-aligned threat actors despite patches being available since July 2025
- **CVE ID**: CVE-2025-8088

### Check Point VPN Zero-Day
- **Description**: Critical vulnerability in Check Point Remote Access VPN and Mobile Access systems
- **Impact**: Ransomware deployment and network infiltration
- **Status**: Exploited as zero-day by Qilin ransomware operators, CISA has mandated federal agencies patch within 3 days

### Veeam Backup & Replication RCE
- **Description**: Critical remote code execution vulnerability in Veeam Backup & Replication software affecting domain-joined systems
- **Impact**: Domain users can execute remote code on backup servers
- **Status**: Recently patched, high risk for enterprise environments
- **CVE ID**: CVE-2026-44963

### Microsoft Defender RoguePlanet Zero-Day
- **Description**: Zero-day vulnerability in Microsoft Defender that allows privilege escalation
- **Impact**: Attackers can gain SYSTEM-level privileges on compromised systems
- **Status**: Recently disclosed zero-day vulnerability

## Affected Systems and Products

- **Google Chrome**: All versions prior to latest security update containing V8 engine fix
- **BerriAI LiteLLM**: AI/ML infrastructure platforms using vulnerable versions
- **WinRAR**: Archive processing software used in Ukrainian government and military organizations
- **Check Point VPN**: Remote Access VPN and Mobile Access deployments in federal agencies
- **Veeam Backup & Replication**: Domain-joined backup server infrastructure
- **Microsoft Defender**: Windows endpoint protection systems
- **Microsoft Windows**: Nearly 200 vulnerabilities across Windows operating systems and supported software
- **SAP NetWeaver and Commerce Cloud**: Enterprise application platforms with 4 critical-severity flaws
- **ServiceNow**: Customer instances exposed through vulnerable API endpoints
- **Microsoft Exchange**: Email spoofing vulnerability in hybrid configurations

## Attack Vectors and Techniques

- **Browser-based Exploitation**: Malicious websites leveraging Chrome V8 zero-day for code execution
- **Supply Chain Poisoning**: Miasma and Hades campaigns targeting GitHub repositories and PyPI packages
- **Email Spoofing**: Ghost-Sender technique using Microsoft Exchange vulnerabilities
- **VPN Infiltration**: Zero-day exploitation of Check Point VPN systems for ransomware deployment
- **Archive-based Delivery**: Malicious WinRAR archives distributing credential stealers
- **API Exploitation**: Unauthenticated access through vulnerable ServiceNow API endpoints
- **SSD Timing Attacks**: FROST attack technique using JavaScript to track user activity via SSD timing
- **AI Agent Manipulation**: Phishing attacks successfully targeting AI agents like OpenClaw

## Threat Actor Activities

- **Russia-aligned Groups**: Conducting sustained campaigns against Ukrainian government and military targets using WinRAR exploits for data theft and cyberespionage
- **Qilin Ransomware**: Exploiting Check Point VPN zero-day vulnerabilities to deploy ransomware in enterprise networks
- **Miasma Campaign Actors**: Compromising Microsoft GitHub repositories and expanding into PyPI package poisoning through the Hades campaign
- **Supply Chain Attackers**: Targeting 73 Microsoft repositories and 19 PyPI packages with credential-stealing malware
- **Unknown Threat Actors**: Actively exploiting Chrome and LiteLLM zero-days in ongoing attack campaigns