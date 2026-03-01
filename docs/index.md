# Exploitation Report

The cybersecurity landscape continues to face significant exploitation activity across multiple attack vectors, with threat actors targeting everything from browser extensions and AI systems to critical network infrastructure. Most concerning is the active exploitation of a maximum-severity zero-day vulnerability in Cisco SD-WAN systems that has been under attack for three years, alongside the compromise of over 900 Sangoma FreePBX instances through web shell attacks. North Korean APT groups APT37 and ScarCruft have deployed sophisticated new malware tools to breach air-gapped networks, while a compromised Chrome extension has been weaponized to steal cryptocurrency from thousands of users. Additionally, critical vulnerabilities in Trend Micro Apex One and Juniper Networks PTX routers pose immediate risks of remote code execution and full system compromise.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability that has been actively exploited by sophisticated threat actors
- **Impact**: Allows attackers to compromise SD-WAN infrastructure with significant network access
- **Status**: Under active exploitation for approximately 3 years by unknown sophisticated threat actors
- **CVE ID**: CVE-2026-20127

### Ivanti Connect Secure Zero-Day
- **Description**: Zero-day vulnerability exploited to deploy RESURGE malware implants on Ivanti devices
- **Impact**: Allows persistent access and malware deployment that can remain dormant on affected systems
- **Status**: Actively exploited with CISA warning about dormant malware persistence
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection
- **Description**: Command injection vulnerability in Sangoma FreePBX systems allowing web shell deployment
- **Impact**: Remote code execution and persistent system access through web shells
- **Status**: Over 900 instances currently compromised with ongoing attacks since December

### QuickLens Chrome Extension Compromise
- **Description**: Legitimate Chrome extension "QuickLens - Search Screen with Google Lens" compromised to deliver malware
- **Impact**: Cryptocurrency theft and malware distribution to thousands of users
- **Status**: Extension removed from Chrome Web Store after compromise detection

### ClawJacked WebSocket Vulnerability
- **Description**: High-severity flaw in OpenClaw AI agents allowing malicious websites to hijack local AI agents via WebSocket connections
- **Impact**: Unauthorized access and control of locally running AI agents
- **Status**: Patched by OpenClaw after security disclosure

## Affected Systems and Products

- **Cisco SD-WAN Systems**: All SD-WAN infrastructure vulnerable to CVE-2026-20127 exploitation
- **Ivanti Connect Secure**: Devices vulnerable to CVE-2025-0282 with potential dormant RESURGE malware
- **Sangoma FreePBX**: Over 900 instances compromised with web shells, ongoing exploitation
- **Chrome Browser Extensions**: QuickLens extension users affected by malicious compromise
- **OpenClaw AI Agents**: Local AI agent installations vulnerable to WebSocket hijacking
- **Trend Micro Apex One**: Windows systems running vulnerable versions at risk of RCE
- **Juniper Networks PTX Routers**: PTX Series routers running Junos OS Evolved vulnerable to takeover
- **Google Cloud API**: Thousands of API keys exposed with unauthorized Gemini AI access

## Attack Vectors and Techniques

- **Browser Extension Compromise**: Legitimate extensions weaponized for malware delivery and cryptocurrency theft
- **ClickFix Attack Technique**: Social engineering method demonstrated in QuickLens extension compromise
- **Web Shell Deployment**: Command injection exploits leading to persistent web shell access
- **WebSocket Hijacking**: Malicious websites exploiting local AI agent connections
- **Air-Gapped Network Infiltration**: USB-based malware and removable drive propagation
- **Blockchain C2 Infrastructure**: Encrypted command storage on Polygon blockchain for takedown resilience
- **Supply Chain Attacks**: Third-party service provider compromises affecting downstream customers
- **Zero-Day Exploitation**: Long-term exploitation of unpatched critical vulnerabilities

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new malware tools for air-gapped network breaches and covert surveillance via removable drives
- **ScarCruft (North Korean)**: Using Zoho WorkDrive for C2 communications and USB malware to breach air-gapped networks
- **Kimwolf Botmaster "Dort"**: Operating the world's largest and most disruptive botnet through disclosed vulnerability exploitation
- **The Com Cybercrime Collective**: Targeting children and teenagers, leading to 30 arrests in Europol-coordinated operation
- **Unknown Sophisticated Actor**: Exploiting Cisco SD-WAN zero-day for three years with minimal forensic evidence
- **Cryptocurrency Scammers**: Operating pig butchering schemes with $61 million in seized Tether assets
- **Gaming Tool Attackers**: Distributing Java-based RATs through trojanized gaming utilities via browsers and chat platforms