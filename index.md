# Exploitation Report

The cybersecurity landscape shows significant active exploitation across multiple vectors, with particularly concerning activity involving zero-day vulnerabilities, supply chain compromises, and sophisticated botnet operations. Critical zero-day exploitation has been identified in Cisco SD-WAN infrastructure that remained undetected for three years, while the Ivanti Connect Secure platform faces active attacks using RESURGE malware. Additionally, over 900 Sangoma FreePBX instances remain compromised through ongoing web shell attacks, and North Korean APT groups are deploying advanced tools to breach air-gapped networks using USB-based malware and cloud services for command-and-control operations.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN infrastructure that has been exploited by sophisticated threat actors
- **Impact**: Full system compromise allowing attackers complete control over SD-WAN infrastructure
- **Status**: Under active exploitation for approximately three years before discovery
- **CVE ID**: CVE-2026-20127

### Ivanti Connect Secure RESURGE Malware
- **Description**: Zero-day exploitation targeting Ivanti Connect Secure devices using malicious implants that can remain dormant
- **Impact**: Persistent access to enterprise networks with stealth capabilities
- **Status**: Active exploitation with CISA warnings issued about dormant infections
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection
- **Description**: Command injection vulnerability in FreePBX instances allowing web shell deployment
- **Impact**: Remote code execution and persistent system access
- **Status**: Over 900 instances remain compromised with ongoing exploitation since December

### ClawJacked OpenClaw AI Vulnerability
- **Description**: High-severity WebSocket vulnerability allowing malicious websites to hijack local AI agents
- **Impact**: Remote takeover of AI agents and unauthorized access to local systems
- **Status**: Fixed by OpenClaw but previously exploitable

### Trend Micro Apex One Critical Flaws
- **Description**: Two critical vulnerabilities in Apex One security software allowing remote code execution
- **Impact**: Full system compromise on Windows systems running the security solution
- **Status**: Recently patched by Trend Micro

### Juniper Networks PTX Router Vulnerability
- **Description**: Critical vulnerability in Junos OS Evolved affecting PTX Series routers
- **Impact**: Complete router takeover with root-level access for unauthenticated attackers
- **Status**: Allows full remote code execution

## Affected Systems and Products

- **Cisco SD-WAN Infrastructure**: Network devices and management systems affected by three-year exploitation campaign
- **Ivanti Connect Secure**: Enterprise VPN and secure access solutions with dormant malware implants
- **Sangoma FreePBX**: Over 900 VoIP systems compromised with web shells
- **OpenClaw AI Agents**: Local AI systems vulnerable to WebSocket-based hijacking
- **Trend Micro Apex One**: Windows endpoint security solutions with RCE vulnerabilities
- **Juniper PTX Series Routers**: Enterprise network infrastructure devices running Junos OS Evolved
- **Chrome Extensions**: Browser extensions compromised to deliver malware and steal cryptocurrency
- **Google Cloud API Keys**: Thousands of exposed keys providing unauthorized Gemini AI access

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term undetected exploitation of Cisco infrastructure and Ivanti devices
- **Web Shell Deployment**: Command injection attacks leading to persistent backdoor access
- **Supply Chain Compromise**: Malicious Chrome extensions and trojanized software distribution
- **WebSocket Hijacking**: Browser-based attacks targeting local AI agent services
- **USB-Based Air-Gap Bridging**: Physical malware propagation using removable drives
- **Cloud Service Abuse**: Legitimate services like Zoho WorkDrive used for C2 communications
- **Blockchain C2 Infrastructure**: Polygon blockchain used to store encrypted botnet commands
- **ClickFix Social Engineering**: Fake error messages tricking users into malware execution
- **Cryptocurrency Theft**: Direct wallet compromise through exposed mnemonic phrases

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new malware tools for air-gapped network infiltration and covert surveillance
- **ScarCruft (North Korean)**: Using Zoho WorkDrive and USB malware to breach isolated systems
- **Sophisticated Unknown Actor**: Conducting three-year Cisco SD-WAN exploitation campaign with minimal forensic evidence
- **Kimwolf Botmaster "Dort"**: Operating the world's largest botnet through vulnerability exploitation
- **Aeternum C2 Operators**: Using blockchain-based command infrastructure for botnet resilience
- **The Com Cybercrime Collective**: Online group targeting children and teenagers, resulting in 30 arrests
- **Chrome Extension Attackers**: Compromising legitimate browser extensions for cryptocurrency theft
- **Gaming Tool Trojans**: Distributing Java-based RATs through trojanized gaming utilities