# Exploitation Report

Multiple critical vulnerabilities are currently being exploited in the wild, with threat actors targeting enterprise infrastructure, AI platforms, and consumer applications. The most severe activity includes a three-year exploitation of a maximum-severity Cisco SD-WAN zero-day vulnerability, ongoing attacks against Sangoma FreePBX systems using web shells, and zero-day attacks on Ivanti Connect devices. Additionally, sophisticated threat actors are compromising browser extensions, deploying blockchain-based botnets, and targeting air-gapped networks through novel attack vectors.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN infrastructure that has been actively exploited for three years
- **Impact**: Full compromise of network infrastructure by sophisticated threat actors
- **Status**: Under active exploitation by unknown but sophisticated threat actors who left minimal evidence
- **CVE ID**: CVE-2026-20127

### Ivanti Connect Zero-Day Attacks
- **Description**: Zero-day vulnerability in Ivanti Connect Secure devices exploited to deploy RESURGE malware implants
- **Impact**: Persistent access to enterprise networks with dormant malware capabilities
- **Status**: CISA has issued warnings about RESURGE malware remaining dormant on compromised devices
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection Vulnerability
- **Description**: Command injection vulnerability in Sangoma FreePBX systems exploited to deploy web shells
- **Impact**: Remote code execution and persistent access to VoIP infrastructure
- **Status**: Over 900 instances remain compromised with web shells despite patches being available

### ClawJacked OpenClaw AI Agent Vulnerability
- **Description**: High-severity WebSocket vulnerability allowing malicious websites to hijack locally running AI agents
- **Impact**: Complete takeover of local AI agent functionality and potential data exfiltration
- **Status**: Fixed by OpenClaw after disclosure

### Trend Micro Apex One Critical Vulnerabilities
- **Description**: Two critical vulnerabilities in Trend Micro Apex One security platform
- **Impact**: Remote code execution on vulnerable Windows systems running enterprise security software
- **Status**: Patches released by Trend Micro

### Juniper Networks PTX Router Critical Flaw
- **Description**: Critical vulnerability in Junos OS Evolved running on PTX Series routers
- **Impact**: Full router takeover and remote code execution with root privileges by unauthenticated attackers
- **Status**: Requires immediate patching of affected router infrastructure

## Affected Systems and Products

- **Cisco SD-WAN Infrastructure**: Network routing and management systems affected by long-term zero-day exploitation
- **Ivanti Connect Secure**: Enterprise VPN and secure access solutions compromised by zero-day attacks
- **Sangoma FreePBX**: Over 900 VoIP systems remain compromised with persistent web shells
- **Chrome Browser Extensions**: QuickLens extension compromised to steal cryptocurrency and deploy ClickFix attacks
- **OpenClaw AI Agents**: Local AI agent platforms vulnerable to WebSocket hijacking
- **Trend Micro Apex One**: Enterprise endpoint security platform on Windows systems
- **Juniper PTX Series Routers**: Network infrastructure routers running Junos OS Evolved
- **Google Cloud API Keys**: Thousands of exposed keys providing unauthorized access to Gemini AI endpoints

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Advanced persistent threats using unknown vulnerabilities for long-term access
- **Web Shell Deployment**: Command injection attacks installing persistent backdoors on compromised systems
- **Browser Extension Compromise**: Supply chain attacks targeting popular Chrome extensions for cryptocurrency theft
- **WebSocket Hijacking**: Cross-origin attacks against locally running AI services
- **ClickFix Social Engineering**: Fake error messages tricking users into executing malicious code
- **Blockchain C2 Infrastructure**: Aeternum botnet using Polygon blockchain for resilient command and control
- **USB-Based Air-Gap Bridging**: Advanced malware spreading between isolated and connected networks
- **Trojanized Gaming Tools**: Java-based RATs distributed through compromised gaming utilities
- **Supply Chain Attacks**: Malicious Go modules targeting cryptocurrency operations and Linux systems

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new malware tools to breach air-gapped networks using removable drives for covert surveillance
- **ScarCruft (North Korean)**: Using Zoho WorkDrive for C2 communications and USB malware to target air-gapped systems
- **Sophisticated Unknown Actor**: Three-year exploitation campaign against Cisco SD-WAN infrastructure with advanced evasion techniques
- **Kimwolf Botnet Operators**: Operating the world's largest botnet through disclosed vulnerability exploitation
- **The Com Cybercrime Collective**: Targeting children and teenagers in online schemes, resulting in 30 arrests through Europol coordination
- **Aeternum C2 Operators**: Developing blockchain-resistant botnet infrastructure using encrypted commands on Polygon network
- **QuickLens Compromisers**: Hijacking legitimate Chrome extensions for cryptocurrency theft and malware distribution