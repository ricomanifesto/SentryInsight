# Exploitation Report

Critical exploitation activity continues across multiple attack surfaces, with several zero-day vulnerabilities being actively exploited in the wild. Most concerning are the three-year exploitation of a maximum-severity Cisco SD-WAN vulnerability (CVE-2026-20127), ongoing web shell attacks against over 900 Sangoma FreePBX instances exploiting a command injection vulnerability, and active exploitation of an Ivanti Connect vulnerability (CVE-2025-0282) using the RESURGE malware implant. Additional threats include compromised Chrome extensions conducting ClickFix attacks for cryptocurrency theft, ClawJacked attacks hijacking OpenClaw AI agents, and sophisticated North Korean APT groups deploying new malware for air-gapped network breaches and covert surveillance operations.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN systems that has been under active exploitation by an unknown but sophisticated threat actor
- **Impact**: Complete system compromise with threat actors leaving minimal evidence of their activities
- **Status**: Actively exploited for 3 years before discovery and disclosure
- **CVE ID**: CVE-2026-20127

### Ivanti Connect Zero-Day Exploitation
- **Description**: Zero-day attacks exploiting a vulnerability in Ivanti Connect systems using RESURGE malware implant
- **Impact**: System compromise with persistent malicious implant that can remain dormant on devices
- **Status**: Active exploitation with CISA warning about dormant malware persistence
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection Attacks
- **Description**: Command injection vulnerability in Sangoma FreePBX systems being exploited to deploy web shells
- **Impact**: Over 900 instances compromised with persistent web shell access for attackers
- **Status**: Ongoing attacks with hundreds of systems remaining infected since December

### QuickLens Chrome Extension Compromise
- **Description**: Compromised Chrome extension "QuickLens - Search Screen with Google Lens" used to push malware and steal cryptocurrency
- **Impact**: Malware deployment and cryptocurrency theft targeting thousands of users
- **Status**: Extension removed from Chrome Web Store after compromise detection

### ClawJacked Flaw in OpenClaw AI
- **Description**: High-severity security issue allowing malicious websites to connect to locally running AI agents via WebSocket hijacking
- **Impact**: Complete takeover of local OpenClaw AI agents by malicious websites
- **Status**: Fixed by OpenClaw after disclosure

## Affected Systems and Products

- **Cisco SD-WAN Systems**: Maximum-severity vulnerability affecting network infrastructure
- **Sangoma FreePBX Instances**: Over 900 systems compromised with web shells deployed
- **Ivanti Connect Systems**: Zero-day exploitation with RESURGE malware persistence
- **Chrome Extensions**: QuickLens extension compromised affecting thousands of users
- **OpenClaw AI Agents**: Local AI agents vulnerable to WebSocket hijacking attacks
- **Trend Micro Apex One**: Critical RCE vulnerabilities in Windows systems
- **Juniper Networks PTX Series**: Critical vulnerability allowing full router takeover in Junos OS Evolved
- **Google Cloud API Keys**: Thousands exposed with unauthorized Gemini access capabilities

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term exploitation of unpatched vulnerabilities in critical infrastructure
- **Web Shell Deployment**: Command injection attacks leading to persistent backdoor access
- **Browser Extension Compromise**: Malicious takeover of legitimate extensions for malware distribution
- **ClickFix Attacks**: Social engineering technique used in cryptocurrency theft campaigns
- **WebSocket Hijacking**: Malicious websites exploiting local AI agent connections
- **Air-Gapped Network Infiltration**: USB-based malware for breaching isolated systems
- **Blockchain-Based C2**: Aeternum C2 botnet using Polygon blockchain for command storage
- **API Key Abuse**: Exploitation of exposed Google Cloud keys for unauthorized AI access

## Threat Actor Activities

- **APT37 (North Korean Group)**: Deploying new malware tools for air-gapped network breaches and covert surveillance operations using removable drives
- **ScarCruft (North Korean Group)**: Using Zoho WorkDrive for C2 communications and USB malware to breach air-gapped networks
- **Unknown Sophisticated Actor**: Three-year exploitation campaign against Cisco SD-WAN systems with minimal evidence trails
- **The Com Cybercrime Collective**: Online group targeting children and teenagers, with 30 arrests made in Europol operation
- **Kimwolf Botmaster "Dort"**: Operating world's largest and most disruptive botnet through vulnerability exploitation
- **Multiple Threat Actors**: Conducting pig butchering cryptocurrency scams resulting in $61 million seized by DoJ
- **Ransomware Groups**: Actively targeting healthcare systems and hospitals with encryption attacks