# Exploitation Report

The current threat landscape is dominated by sophisticated zero-day exploitation campaigns, with APT28 actively exploiting CVE-2026-21513, a critical MSHTML vulnerability that was weaponized before Microsoft's February 2026 Patch Tuesday. State-sponsored threat actors are increasingly targeting air-gapped networks and cloud infrastructure, while cybercriminals continue exploiting supply chain vulnerabilities through compromised browser extensions and malicious npm packages. Notable incidents include the exploitation of Ivanti devices through CVE-2025-0282, ongoing attacks against Sangoma FreePBX systems, and the ClawJacked vulnerability affecting OpenClaw AI agents. The exploitation landscape also features novel attack vectors targeting identity verification systems through deepfakes and AI-powered deception techniques.

## Active Exploitation Details

### MSHTML Zero-Day Vulnerability
- **Description**: A critical security flaw in Microsoft's MSHTML component that was actively exploited by state-sponsored threat actors before being patched
- **Impact**: Allows attackers to execute arbitrary code and compromise target systems through web-based attacks
- **Status**: Patched by Microsoft in February 2026 Patch Tuesday, but was exploited in the wild before disclosure
- **CVE ID**: CVE-2026-21513

### Ivanti Connect Secure Zero-Day
- **Description**: A vulnerability in Ivanti Connect Secure devices that allows for malware implantation and persistent access
- **Impact**: Enables attackers to deploy the RESURGE malware implant, which can remain dormant on compromised devices
- **Status**: Actively exploited with CISA warning about dormant malware remaining on affected systems
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection
- **Description**: A command injection vulnerability in Sangoma FreePBX systems that allows for web shell deployment
- **Impact**: Enables attackers to gain persistent access to telecommunications infrastructure and deploy malicious web shells
- **Status**: Over 900 instances remain compromised with active web shell infections since December attacks

### ClawJacked OpenClaw Vulnerability
- **Description**: A high-severity vulnerability in the OpenClaw AI agent that allows malicious websites to hijack local instances via WebSocket connections
- **Impact**: Permits unauthorized control of AI agents, data theft, and system compromise through web-based attacks
- **Status**: Fixed by OpenClaw developers after security researcher disclosure

### QuickLens Chrome Extension Compromise
- **Description**: A legitimate Chrome extension that was compromised to deliver malware and cryptocurrency theft capabilities
- **Impact**: Targets cryptocurrency users with ClickFix attack techniques and credential harvesting
- **Status**: Extension removed from Chrome Web Store after compromise detection

## Affected Systems and Products

- **Microsoft MSHTML Component**: Legacy web rendering component used across Windows systems
- **Ivanti Connect Secure**: VPN and secure access devices widely deployed in enterprise environments
- **Sangoma FreePBX**: Open-source PBX telephony systems used by businesses globally
- **OpenClaw AI Agents**: Local AI automation tools running on user systems
- **Google Chrome Extensions**: Browser extension ecosystem, specifically the QuickLens extension
- **npm Package Registry**: JavaScript package repository targeted by North Korean threat actors
- **Google Cloud API**: Cloud platform services with exposed API keys providing Gemini access
- **Zoho WorkDrive**: Cloud storage service used as command-and-control infrastructure

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: State-sponsored actors leveraging undisclosed vulnerabilities before patches are available
- **Web Shell Deployment**: Persistent access through malicious web shells on compromised FreePBX systems
- **Supply Chain Compromise**: Infiltration of legitimate software distribution channels including npm packages and browser extensions
- **WebSocket Hijacking**: Exploitation of local AI agents through malicious website interactions
- **USB-Based Air-Gap Bridging**: Malware designed to transfer data between isolated and internet-connected networks
- **Cloud API Abuse**: Exploitation of exposed Google Cloud API keys for unauthorized Gemini access
- **ClickFix Social Engineering**: Deceptive techniques used in browser extension compromise campaigns
- **Deepfake Identity Bypass**: AI-generated content used to circumvent identity verification systems

## Threat Actor Activities

- **APT28 (Russian State-Sponsored)**: Actively exploiting CVE-2026-21513 MSHTML vulnerability in targeted campaigns before patch availability
- **APT37/ScarCruft (North Korean)**: Deploying sophisticated malware toolsets including USB-based air-gap bridging capabilities and Zoho WorkDrive C2 infrastructure
- **North Korean Contagious Interview Campaign**: Publishing 26 malicious npm packages with Pastebin command-and-control for cross-platform RAT deployment
- **Kimwolf Botnet Operators**: Managing the world's largest and most disruptive botnet through exploited vulnerabilities
- **The Com Cybercrime Collective**: Online criminal group targeting children and teenagers, subject to Europol operation resulting in 30 arrests
- **Unknown Threat Actors**: Conducting ongoing web shell attacks against FreePBX systems and exploiting Ivanti devices with RESURGE malware