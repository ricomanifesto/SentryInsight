# Exploitation Report

The current threat landscape reveals multiple active exploitation campaigns targeting critical infrastructure and widely-used technologies. The most significant activity includes active exploitation of a maximum-severity zero-day vulnerability in Cisco SD-WAN systems that has been under attack for three years, ongoing web shell deployments against over 900 Sangoma FreePBX instances, and sophisticated malware campaigns by North Korean threat actors targeting air-gapped networks. Additionally, the ClawJacked vulnerability in OpenClaw AI agents and exposed Google Cloud API keys with Gemini access represent emerging attack vectors in AI systems. Critical vulnerabilities in Trend Micro Apex One and an Ivanti Connect Secure zero-day with associated RESURGE malware implants highlight the persistent targeting of enterprise security and infrastructure solutions.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN systems that has been actively exploited by sophisticated threat actors for approximately three years
- **Impact**: Allows attackers to compromise SD-WAN infrastructure with minimal evidence left behind
- **Status**: Currently under active exploitation by unknown but sophisticated threat actors
- **CVE ID**: CVE-2026-20127

### Sangoma FreePBX Command Injection Vulnerability
- **Description**: A command injection vulnerability in Sangoma FreePBX systems enabling web shell deployment
- **Impact**: Allows attackers to install persistent web shells for remote access and control
- **Status**: Over 900 instances remain compromised with web shells since attacks began in December
- **CVE ID**: Not specified in the articles

### Ivanti Connect Secure Zero-Day
- **Description**: A zero-day vulnerability in Ivanti Connect Secure systems exploited to deploy RESURGE malware implants
- **Impact**: Enables attackers to establish persistent access and deploy dormant malware that can remain undetected
- **Status**: Actively exploited in the wild with RESURGE malware deployments
- **CVE ID**: CVE-2025-0282

### ClawJacked OpenClaw AI Agent Vulnerability
- **Description**: A high-severity vulnerability in OpenClaw AI agent that allows malicious websites to hijack local AI agents via WebSocket connections
- **Impact**: Enables attackers to silently brute-force access to locally running AI agents and take control
- **Status**: Fixed by OpenClaw developers
- **CVE ID**: Not specified in the articles

### Trend Micro Apex One Critical Vulnerabilities
- **Description**: Two critical vulnerabilities in Trend Micro Apex One allowing remote code execution
- **Impact**: Attackers can gain remote code execution on vulnerable Windows systems
- **Status**: Patched by Trend Micro
- **CVE ID**: Not specified in the articles

## Affected Systems and Products

- **Cisco SD-WAN Systems**: Infrastructure components affected by three-year exploitation campaign
- **Sangoma FreePBX Instances**: Over 900 compromised instances with persistent web shell infections
- **Ivanti Connect Secure**: Systems vulnerable to zero-day exploitation and RESURGE malware deployment
- **OpenClaw AI Agents**: Local AI agent installations susceptible to WebSocket hijacking
- **Trend Micro Apex One**: Windows-based endpoint security systems with RCE vulnerabilities
- **Google Cloud API Keys**: Previously harmless API keys now providing unauthorized Gemini AI access
- **Chrome Extensions**: QuickLens extension compromised to steal cryptocurrency
- **Linux Systems**: Targeted by malicious Go modules deploying Rekoobe backdoor

## Attack Vectors and Techniques

- **WebSocket Exploitation**: Malicious websites hijacking local AI agents through WebSocket connections
- **Web Shell Deployment**: Persistent compromise of FreePBX systems through command injection
- **USB-based Air-Gap Bridging**: North Korean actors using removable drives to breach isolated networks
- **Blockchain C2 Infrastructure**: Aeternum C2 botnet using Polygon blockchain for command storage
- **Supply Chain Compromise**: Trojanized gaming tools distributing Java-based RATs
- **API Key Abuse**: Exploitation of exposed Google Cloud API keys for unauthorized Gemini access
- **Browser Extension Compromise**: Hijacking legitimate Chrome extensions for cryptocurrency theft
- **Malicious Package Distribution**: Go crypto modules containing password stealers and backdoors

## Threat Actor Activities

- **APT37/ScarCruft**: North Korean group deploying new malware tools for air-gapped network infiltration using Zoho WorkDrive for C2 communications and USB-based propagation
- **Kimwolf Botnet Operators**: Large-scale botnet operation with focus on the operator "Dort" and vulnerability exploitation for botnet assembly
- **The Com Cybercrime Collective**: Online criminal group targeting children and teenagers, with 30 arrests following Europol's Project Compass operation
- **Unknown Sophisticated Actors**: Three-year exploitation campaign against Cisco SD-WAN systems with minimal attribution evidence
- **Cryptocurrency Scammers**: Pig butchering operations resulting in $61 million seizure by U.S. Department of Justice