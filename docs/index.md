# Exploitation Report

The current threat landscape reveals critical exploitation activities across multiple vectors, with significant concerns around AI infrastructure vulnerabilities, enterprise security solutions, and blockchain-based command and control operations. The ClawJacked vulnerability represents a high-severity flaw in AI agent systems that allowed malicious websites to hijack local OpenClaw instances through WebSocket connections. Cisco SD-WAN infrastructure has been under zero-day exploitation for three years by sophisticated threat actors. Additionally, over 900 Sangoma FreePBX instances remain compromised through ongoing web shell attacks exploiting command injection vulnerabilities. Enterprise security is further threatened by critical remote code execution flaws in Trend Micro Apex One and active exploitation of Ivanti Connect Secure devices using the RESURGE malware implant.

## Active Exploitation Details

### ClawJacked OpenClaw Vulnerability
- **Description**: A high-severity vulnerability in the OpenClaw AI agent that allows malicious websites to establish unauthorized WebSocket connections to locally running instances
- **Impact**: Attackers can silently brute-force access to local AI agents, hijack their functionality, and potentially steal sensitive data from the compromised systems
- **Status**: Patched by OpenClaw developers following security researcher disclosure

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN infrastructure that has been actively exploited by sophisticated threat actors
- **Impact**: Unknown threat actors gained unauthorized access to network infrastructure with minimal forensic evidence left behind
- **Status**: Under active exploitation for approximately three years before discovery
- **CVE ID**: CVE-2026-20127

### Sangoma FreePBX Command Injection Vulnerability
- **Description**: A command injection vulnerability in Sangoma FreePBX systems that allows attackers to deploy web shells
- **Impact**: Over 900 instances remain compromised, providing persistent backdoor access to VoIP infrastructure
- **Status**: Ongoing exploitation since December with many systems still infected despite patches being available

### Ivanti Connect Secure RESURGE Malware
- **Description**: Zero-day attacks targeting Ivanti Connect Secure devices using the RESURGE malicious implant
- **Impact**: Attackers can establish persistent access to enterprise VPN infrastructure and remain dormant on compromised devices
- **Status**: Active exploitation with CISA warnings about dormant malware presence
- **CVE ID**: CVE-2025-0282

### Trend Micro Apex One Critical Vulnerabilities
- **Description**: Two critical vulnerabilities in Trend Micro Apex One security software allowing remote code execution
- **Impact**: Attackers can gain remote code execution capabilities on vulnerable Windows systems running enterprise security solutions
- **Status**: Recently patched by Trend Micro

## Affected Systems and Products

- **OpenClaw AI Agents**: Local instances vulnerable to WebSocket hijacking attacks
- **Cisco SD-WAN Infrastructure**: Network devices running vulnerable SD-WAN software
- **Sangoma FreePBX Systems**: VoIP communication platforms with command injection vulnerabilities
- **Ivanti Connect Secure**: Enterprise VPN solutions targeted by zero-day exploits
- **Trend Micro Apex One**: Windows-based enterprise security solutions with RCE vulnerabilities
- **Google Cloud API Infrastructure**: API keys potentially exposing Gemini AI data access
- **Chrome Browser Extensions**: QuickLens extension compromised to steal cryptocurrency
- **Korean Tax Service Systems**: Cryptocurrency wallet infrastructure exposed through operational security failures

## Attack Vectors and Techniques

- **WebSocket Hijacking**: Malicious websites exploiting OpenClaw's local WebSocket interfaces to gain unauthorized access
- **Command Injection**: Exploitation of input validation flaws in FreePBX to deploy persistent web shells
- **Zero-Day Exploitation**: Sophisticated attacks against Cisco and Ivanti infrastructure using previously unknown vulnerabilities
- **Supply Chain Compromise**: Trojanized gaming tools and browser extensions used to distribute RATs and cryptocurrency theft malware
- **Air-Gapped Network Infiltration**: APT37 and ScarCruft using USB-based malware and cloud storage services for command and control
- **Blockchain C2 Infrastructure**: Aeternum botnet using Polygon blockchain for resilient command and control operations
- **ClickFix Social Engineering**: Malicious extensions using fake error messages to trick users into executing malicious code

## Threat Actor Activities

- **APT37 (North Korean Group)**: Deploying new malware tools to breach air-gapped networks using removable drives for data exfiltration and covert surveillance operations
- **ScarCruft (North Korean Group)**: Utilizing Zoho WorkDrive for command and control communications and developing USB-based malware for air-gapped network infiltration
- **Unknown Sophisticated Actor**: Conducting three-year exploitation campaign against Cisco SD-WAN infrastructure with advanced operational security practices
- **Kimwolf Botnet Operators**: Operating the world's largest and most disruptive botnet following disclosure of underlying vulnerabilities
- **Aeternum C2 Operators**: Developing blockchain-based botnet infrastructure using Polygon network for takedown-resistant command and control
- **The Com Cybercrime Collective**: Online criminal organization targeting children and teenagers, with 30 arrests made in Europol-coordinated operation