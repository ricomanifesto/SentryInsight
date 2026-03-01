# Exploitation Report

Critical exploitation activity continues across multiple attack vectors, with significant focus on zero-day vulnerabilities, supply chain compromises, and sophisticated threat actor operations. The most concerning developments include a three-year exploitation campaign targeting Cisco SD-WAN infrastructure through CVE-2026-20127, active zero-day attacks against Ivanti Connect Secure devices using CVE-2025-0282, and widespread compromise of over 900 Sangoma FreePBX instances through command injection vulnerabilities. North Korean threat actors APT37 and ScarCruft are deploying advanced malware tools to breach air-gapped networks, while ransomware attacks continue to impact critical healthcare infrastructure.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN infrastructure that has been actively exploited for three years
- **Impact**: Allows sophisticated threat actors to compromise SD-WAN deployments with minimal detection
- **Status**: Under active exploitation by unknown sophisticated threat actors who leave very little evidence
- **CVE ID**: CVE-2026-20127

### Ivanti Connect Secure Zero-Day
- **Description**: Zero-day vulnerability being exploited to deploy RESURGE malware implants on Ivanti Connect Secure devices
- **Impact**: Allows attackers to establish persistent access and potentially remain dormant on compromised devices
- **Status**: Active exploitation confirmed with RESURGE malware deployment
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection
- **Description**: Command injection vulnerability in Sangoma FreePBX systems allowing web shell deployment
- **Impact**: Remote code execution and persistent access through web shell implants
- **Status**: Over 900 instances remain compromised with web shells from attacks starting in December

### QuickLens Chrome Extension Compromise
- **Description**: Legitimate Chrome extension compromised to push malware and steal cryptocurrency
- **Impact**: Cryptocurrency theft and malware distribution to thousands of users through ClickFix attack techniques
- **Status**: Extension removed from Chrome Web Store after compromise detection

### ClawJacked WebSocket Vulnerability
- **Description**: High-severity security flaw in OpenClaw AI agents allowing malicious websites to hijack local AI agents via WebSocket connections
- **Impact**: Complete takeover of locally running AI agents by malicious websites
- **Status**: Fixed by OpenClaw after security disclosure

## Affected Systems and Products

- **Cisco SD-WAN Infrastructure**: All SD-WAN deployments potentially affected by three-year exploitation campaign
- **Ivanti Connect Secure**: Zero-day exploitation targeting these devices with RESURGE malware
- **Sangoma FreePBX**: Over 900 instances compromised with persistent web shells
- **Chrome Extensions**: QuickLens extension compromised affecting thousands of users
- **OpenClaw AI Agents**: Local AI agents vulnerable to WebSocket-based hijacking
- **Trend Micro Apex One**: Critical RCE vulnerabilities in Windows systems recently patched
- **Juniper Networks PTX Series**: Critical vulnerability allowing full router takeover in Junos OS Evolved
- **Google Cloud API Keys**: Previously harmless API keys now provide access to Gemini AI data
- **Healthcare Systems**: Multiple hospitals affected by ransomware attacks impacting patient care

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term campaigns exploiting unpatched vulnerabilities in critical infrastructure
- **Supply Chain Compromise**: Legitimate software and extensions compromised to deliver malware
- **Web Shell Deployment**: Command injection vulnerabilities used to establish persistent access
- **ClickFix Attacks**: Social engineering technique used in Chrome extension compromise
- **WebSocket Hijacking**: Malicious websites exploiting local AI agent communications
- **USB-Based Air-Gap Bridging**: Specialized malware designed to move between isolated and connected networks
- **Blockchain C2 Infrastructure**: Aeternum botnet using Polygon blockchain for resilient command and control
- **Trojanized Gaming Tools**: Java-based RATs distributed through gaming utilities on browsers and chat platforms
- **Cloud API Exploitation**: Exposed Google API keys providing unauthorized access to AI services

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new malware tools to breach air-gapped networks using removable drives for covert surveillance
- **ScarCruft (North Korean)**: Using Zoho WorkDrive for C2 communications and USB malware to breach air-gapped networks with specialized backdoors
- **Unknown Sophisticated Actor**: Three-year exploitation campaign against Cisco SD-WAN infrastructure with minimal forensic evidence
- **Kimwolf Botmaster "Dort"**: Operating the world's largest and most disruptive botnet through disclosed vulnerability exploitation
- **The Com Cybercrime Collective**: Targeted children and teenagers before 30 arrests in Europol-coordinated operation
- **Cryptocurrency Scammers**: $61 million in Tether seized related to pig butchering schemes
- **Ransomware Groups**: Continuing attacks on healthcare infrastructure with real-world patient care impacts
- **Various Threat Actors**: Exploiting exposed Google API keys for unauthorized Gemini AI access and data theft