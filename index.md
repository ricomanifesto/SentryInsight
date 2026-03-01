# Exploitation Report

Current cybersecurity intelligence reveals a diverse landscape of active exploitation targeting critical infrastructure, enterprise systems, and consumer applications. The most severe incidents include a three-year exploitation campaign against Cisco SD-WAN systems using CVE-2026-20127, ongoing attacks against over 900 Sangoma FreePBX instances through command injection vulnerabilities, and zero-day exploitation of Ivanti Connect Secure devices with the RESURGE malware implant. Additionally, sophisticated threat actors are leveraging compromised browser extensions, manipulating Google Cloud API keys for unauthorized AI access, and deploying advanced tools to breach air-gapped networks through USB-based malware propagation.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: Maximum-severity vulnerability in Cisco SD-WAN systems that has been under active exploitation for three years
- **Impact**: Allows sophisticated threat actors to compromise SD-WAN infrastructure with minimal forensic evidence
- **Status**: Currently being exploited by unknown but sophisticated threat actors
- **CVE ID**: CVE-2026-20127

### Sangoma FreePBX Command Injection Vulnerability
- **Description**: Command injection vulnerability in Sangoma FreePBX instances allowing web shell deployment
- **Impact**: Enables attackers to maintain persistent access and execute arbitrary commands on compromised systems
- **Status**: Over 900 instances remain infected with web shells from attacks beginning in December

### Ivanti Connect Secure Zero-Day
- **Description**: Zero-day vulnerability allowing deployment of RESURGE malware implant on Ivanti devices
- **Impact**: Provides attackers with persistent access and potential for dormant malware activation
- **Status**: Actively exploited with RESURGE malware capable of remaining dormant on devices
- **CVE ID**: CVE-2025-0282

### QuickLens Chrome Extension Compromise
- **Description**: Legitimate Chrome extension compromised to distribute malware and steal cryptocurrency
- **Impact**: Targets thousands of users for crypto theft using ClickFix attack techniques
- **Status**: Extension removed from Chrome Web Store after compromise detection

### ClawJacked WebSocket Vulnerability
- **Description**: High-severity flaw in OpenClaw AI agents allowing malicious website connections via WebSocket
- **Impact**: Enables malicious sites to hijack local AI agents and take control of systems
- **Status**: Fixed by OpenClaw after discovery

### Trend Micro Apex One Critical Flaws
- **Description**: Two critical vulnerabilities in Trend Micro Apex One security software
- **Impact**: Allow attackers to achieve remote code execution on vulnerable Windows systems
- **Status**: Patched by Trend Micro

### Juniper Networks PTX Router Vulnerability
- **Description**: Critical flaw in Junos OS Evolved running on PTX Series routers
- **Impact**: Allows unauthenticated remote code execution with root privileges for complete router takeover
- **Status**: Critical vulnerability requiring immediate patching

## Affected Systems and Products

- **Cisco SD-WAN Systems**: Infrastructure devices vulnerable to CVE-2026-20127 exploitation
- **Sangoma FreePBX**: Over 900 instances compromised with persistent web shell infections
- **Ivanti Connect Secure**: Devices targeted by zero-day attacks deploying RESURGE malware
- **Chrome Extensions**: QuickLens extension with thousands of users affected by compromise
- **OpenClaw AI Agents**: Local AI systems vulnerable to WebSocket-based hijacking
- **Google Cloud API Keys**: Thousands of exposed keys providing unauthorized Gemini AI access
- **Trend Micro Apex One**: Windows security software with critical RCE vulnerabilities
- **Juniper PTX Series Routers**: Network infrastructure devices with critical remote code execution flaws

## Attack Vectors and Techniques

- **Browser Extension Compromise**: Legitimate extensions hijacked to distribute malware and steal cryptocurrency
- **ClickFix Attacks**: Social engineering technique used in conjunction with compromised extensions
- **WebSocket Exploitation**: Malicious websites connecting to local AI agents via WebSocket vulnerabilities
- **Web Shell Deployment**: Command injection attacks resulting in persistent web shell access
- **Zero-Day Exploitation**: Advanced persistent threats using previously unknown vulnerabilities
- **USB-Based Malware**: Air-gapped network breaches using removable drive propagation
- **API Key Abuse**: Exploitation of exposed Google Cloud keys for unauthorized AI service access
- **Blockchain C2 Infrastructure**: Aeternum botnet using Polygon blockchain for command storage
- **Social Engineering**: Trojanized gaming tools distributed via browsers and chat platforms

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new malware tools to breach air-gapped networks using removable drives and conducting covert surveillance operations
- **ScarCruft (North Korean)**: Using Zoho WorkDrive for command-and-control communications and USB malware to target air-gapped systems
- **Sophisticated Unknown Actor**: Conducting three-year exploitation campaign against Cisco SD-WAN systems with minimal forensic traces
- **Cybercrime Collective "The Com"**: Online group targeting children and teenagers, resulting in 30 arrests through Europol's Project Compass
- **Kimwolf Botmaster "Dort"**: Operating the world's largest and most disruptive botnet through disclosed vulnerability exploitation
- **Cryptocurrency Scammers**: Conducting pig butchering schemes resulting in $61 million DoJ seizure
- **Gaming Tool Attackers**: Distributing Java-based RATs through trojanized gaming utilities via browsers and chat platforms