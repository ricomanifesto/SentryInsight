# Exploitation Report

Multiple critical exploitation activities are currently threatening organizations across various sectors. The most significant threats include a state-sponsored zero-day attack by APT28 targeting MSHTML components, widespread compromise of Sangoma FreePBX instances through command injection vulnerabilities, active exploitation of Ivanti devices with dormant RESURGE malware, and a three-year-long exploitation campaign against Cisco SD-WAN infrastructure. North Korean threat actors continue their aggressive campaigns with sophisticated supply chain attacks through npm packages, air-gapped network breaches, and compromised browser extensions targeting cryptocurrency assets.

## Active Exploitation Details

### MSHTML Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Microsoft's MSHTML component that was exploited before the February 2026 Patch Tuesday
- **Impact**: Allows remote code execution and system compromise
- **Status**: Patched by Microsoft in February 2026, but was actively exploited before patch release
- **CVE ID**: CVE-2026-21513

### Sangoma FreePBX Command Injection Vulnerability
- **Description**: Command injection vulnerability in Sangoma FreePBX systems allowing remote code execution
- **Impact**: Installation of web shells for persistent access and system control
- **Status**: Over 900 instances remain compromised despite patches being available

### Ivanti Connect Zero-Day
- **Description**: Zero-day vulnerability in Ivanti Connect Secure devices exploited to deploy RESURGE malware
- **Impact**: Installation of dormant malware implants for persistent access
- **Status**: Actively exploited with RESURGE malware remaining dormant on compromised devices
- **CVE ID**: CVE-2025-0282

### Cisco SD-WAN Critical Vulnerability
- **Description**: Maximum-severity vulnerability in Cisco SD-WAN infrastructure exploited for three years
- **Impact**: Complete system compromise and network infiltration
- **Status**: Active exploitation by sophisticated threat actors with minimal forensic evidence
- **CVE ID**: CVE-2026-20127

### ClawJacked OpenClaw Vulnerability
- **Description**: High-severity vulnerability in OpenClaw AI agent allowing malicious websites to hijack local instances
- **Impact**: Remote takeover of AI agents and data theft through WebSocket connections
- **Status**: Fixed by OpenClaw but previously exploited for data exfiltration

## Affected Systems and Products

- **Microsoft MSHTML**: Legacy web browser engine components in Windows systems
- **Sangoma FreePBX**: Over 900 VoIP phone system instances remain compromised with web shells
- **Ivanti Connect Secure**: VPN appliances with dormant RESURGE malware implants
- **Cisco SD-WAN**: Network infrastructure devices compromised for three years
- **OpenClaw AI Agent**: Local AI assistants vulnerable to remote hijacking via malicious websites
- **Google Cloud API**: Thousands of API keys with unintended Gemini AI access permissions
- **Chrome Browser Extensions**: QuickLens extension compromised to steal cryptocurrency
- **npm Package Registry**: 26 malicious packages published for cross-platform RAT distribution

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: APT28 leveraging unpatched MSHTML vulnerabilities for targeted attacks
- **Command Injection**: Direct exploitation of FreePBX systems to deploy persistent web shells
- **Supply Chain Compromise**: North Korean actors publishing malicious npm packages with hidden C2 communications
- **WebSocket Hijacking**: Malicious websites connecting to local AI agents through unprotected WebSocket interfaces
- **Browser Extension Compromise**: Legitimate extensions modified to include cryptocurrency theft capabilities
- **Air-Gapped Network Breach**: USB-based malware and removable drive propagation techniques
- **API Key Abuse**: Exploitation of exposed Google Cloud API keys for unauthorized Gemini AI access
- **Social Engineering**: Trojanized gaming tools distributed via browsers and chat platforms

## Threat Actor Activities

- **APT28 (Fancy Bear)**: Russian state-sponsored group exploiting MSHTML zero-day vulnerabilities in targeted campaigns
- **North Korean APT Groups**: Multiple campaigns including Contagious Interview with npm package poisoning and APT37/ScarCruft air-gapped network infiltration
- **Kimwolf Botnet Operators**: Large-scale botnet operations with operators identified but still active
- **The Com Cybercrime Collective**: Online group targeting children and teenagers, with 30 arrests following Europol operation
- **Unknown Sophisticated Actor**: Three-year exploitation campaign against Cisco SD-WAN infrastructure with advanced evasion techniques