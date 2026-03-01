# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms, with the most concerning being a zero-day vulnerability in Ivanti Connect systems (CVE-2025-0282) that has allowed attackers to deploy persistent RESURGE malware implants. Simultaneously, over 900 Sangoma FreePBX instances remain compromised through web shell attacks exploiting command injection vulnerabilities, while a maximum-severity Cisco SD-WAN zero-day (CVE-2026-20127) has been under active exploitation for three years by sophisticated threat actors. Additional exploitation includes the compromise of Chrome extensions for cryptocurrency theft and attacks against air-gapped networks by North Korean APT groups.

## Active Exploitation Details

### Ivanti Connect Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Ivanti Connect systems that allows attackers to deploy persistent malware implants
- **Impact**: Enables deployment of RESURGE malware that can remain dormant on devices and provide persistent access to compromised systems
- **Status**: Actively exploited in the wild, CISA has issued warnings about dormant malware on affected devices
- **CVE ID**: CVE-2025-0282

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: Maximum-severity vulnerability in Cisco SD-WAN systems that has been exploited by sophisticated threat actors
- **Impact**: Complete system compromise with very little evidence left behind by attackers
- **Status**: Under active exploitation for three years by unknown sophisticated threat actors
- **CVE ID**: CVE-2026-20127

### Sangoma FreePBX Command Injection
- **Description**: Command injection vulnerability in Sangoma FreePBX systems allowing web shell deployment
- **Impact**: Enables persistent access and control over FreePBX instances for ongoing malicious activities
- **Status**: Over 900 instances remain compromised with web shells, attacks began in December

### ClawJacked WebSocket Vulnerability
- **Description**: High-severity flaw in OpenClaw AI agents allowing malicious websites to hijack local AI agents
- **Impact**: Malicious websites can connect to and take control of locally running AI agents via WebSocket connections
- **Status**: Vulnerability has been patched by OpenClaw

### QuickLens Chrome Extension Compromise
- **Description**: Chrome extension "QuickLens - Search Screen with Google Lens" was compromised to push malware
- **Impact**: Cryptocurrency theft and ClickFix attack deployment affecting thousands of users
- **Status**: Extension removed from Chrome Web Store after compromise detection

## Affected Systems and Products

- **Ivanti Connect Systems**: Zero-day exploitation affecting enterprise VPN and remote access systems
- **Cisco SD-WAN Infrastructure**: Critical vulnerability in network infrastructure with three-year exploitation history
- **Sangoma FreePBX Instances**: Over 900 compromised VoIP systems with persistent web shell infections
- **OpenClaw AI Agents**: Local AI agent systems vulnerable to WebSocket-based hijacking
- **Chrome Extensions**: QuickLens extension and potentially other browser extensions in supply chain attacks
- **Trend Micro Apex One**: Critical remote code execution vulnerabilities in Windows security systems
- **Juniper Networks PTX Routers**: Critical vulnerability allowing full router takeover in Junos OS Evolved
- **Google Cloud API Keys**: Exposed API keys providing unauthorized access to Gemini AI endpoints

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise systems
- **Web Shell Deployment**: Command injection leading to persistent web shell installation on FreePBX systems
- **Supply Chain Compromise**: Compromising legitimate browser extensions to deliver malware
- **WebSocket Hijacking**: Malicious websites exploiting local AI agent connections
- **ClickFix Social Engineering**: Fake error messages tricking users into executing malicious code
- **Air-Gapped Network Infiltration**: USB-based malware spreading between isolated and connected systems
- **Blockchain-Based C2**: Using Polygon blockchain to store encrypted botnet commands for resilience
- **API Key Abuse**: Exploiting exposed Google API keys to access private AI data and services

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new malware tools to breach air-gapped networks and conduct covert surveillance using removable drives
- **ScarCruft (North Korean)**: Using Zoho WorkDrive for C2 communications and USB malware to target air-gapped systems
- **Unknown Sophisticated Actor**: Exploiting Cisco SD-WAN zero-day for three years while leaving minimal forensic evidence
- **Kimwolf Botnet Operator "Dort"**: Operating the world's largest botnet through disclosed vulnerability exploitation
- **Aeternum C2 Operators**: Using blockchain-based infrastructure to evade takedown efforts and maintain persistent botnet operations
- **The Com Cybercrime Collective**: Online group targeting children and teenagers, resulting in 30 arrests through Europol operation
- **Cryptocurrency Scammers**: Operating pig butchering schemes with $61 million in seized Tether assets
- **Gaming Platform Attackers**: Distributing Java-based RATs through trojanized gaming utilities via browsers and chat platforms