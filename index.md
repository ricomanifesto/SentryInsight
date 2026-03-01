# Exploitation Report

The current threat landscape is dominated by several critical zero-day exploitations and sophisticated attack campaigns. Most concerning is the active exploitation of CVE-2026-20127, a maximum-severity Cisco SD-WAN vulnerability that has been exploited by sophisticated threat actors for three years, and CVE-2025-0282, an Ivanti Connect zero-day enabling deployment of RESURGE malware. Additional significant threats include compromised Chrome extensions facilitating cryptocurrency theft, over 900 infected Sangoma FreePBX instances through command injection attacks, and North Korean APT groups deploying advanced tools to breach air-gapped networks. These incidents demonstrate the evolving sophistication of threat actors targeting enterprise infrastructure, browser extensions, and isolated systems.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN systems that has been actively exploited by sophisticated threat actors
- **Impact**: Complete system compromise allowing attackers to gain unauthorized access to network infrastructure
- **Status**: Under active exploitation for approximately three years by unknown threat actors who left minimal forensic evidence
- **CVE ID**: CVE-2026-20127

### Ivanti Connect Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Ivanti Connect Secure devices being exploited to deploy RESURGE malware
- **Impact**: Installation of persistent malicious implants that can remain dormant on compromised devices
- **Status**: Actively exploited in the wild with RESURGE malware deployments confirmed
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection
- **Description**: A command injection vulnerability in Sangoma FreePBX systems allowing remote code execution
- **Impact**: Web shell deployment enabling persistent access and control over telephony infrastructure
- **Status**: Over 900 instances confirmed compromised since December with ongoing exploitation

### Trend Micro Apex One Code Execution Vulnerabilities
- **Description**: Critical remote code execution vulnerabilities in Trend Micro Apex One security software
- **Impact**: Complete system compromise on vulnerable Windows systems running the security solution
- **Status**: Recently patched by vendor, exploitation status in the wild unclear

### Juniper Networks PTX Router Vulnerability
- **Description**: Critical vulnerability in Junos OS Evolved affecting PTX Series routers
- **Impact**: Complete router takeover allowing unauthenticated attackers to execute code with root privileges
- **Status**: Recently disclosed, patch availability and exploitation status unclear

## Affected Systems and Products

- **Chrome Browser Extensions**: QuickLens extension compromised to steal cryptocurrency and deploy malware via ClickFix attacks
- **Sangoma FreePBX Systems**: Over 900 instances worldwide infected with web shells through command injection
- **Cisco SD-WAN Infrastructure**: Enterprise networking equipment vulnerable to zero-day exploitation
- **Ivanti Connect Secure**: VPN and secure access solutions targeted by RESURGE malware campaigns
- **OpenClaw AI Agents**: Local AI systems vulnerable to WebSocket hijacking via ClawJacked flaw
- **Trend Micro Apex One**: Windows-based endpoint security solutions with critical RCE vulnerabilities
- **Juniper PTX Routers**: Enterprise routing infrastructure running Junos OS Evolved
- **Google Cloud API Keys**: Thousands of exposed keys providing unauthorized Gemini AI access
- **Korean Government Systems**: National Tax Service cryptocurrency wallets compromised

## Attack Vectors and Techniques

- **Browser Extension Compromise**: Hijacking legitimate Chrome extensions to deploy ClickFix attacks and cryptocurrency theft mechanisms
- **WebSocket Hijacking**: ClawJacked attacks targeting local AI agents through malicious websites
- **Command Injection**: Exploiting input validation flaws in FreePBX systems to deploy web shells
- **Zero-Day Exploitation**: Long-term exploitation of unpatched Cisco SD-WAN vulnerabilities
- **Air-Gapped Network Infiltration**: USB-based malware and removable drive attacks to breach isolated systems
- **Supply Chain Attacks**: Compromising legitimate software tools and extensions for malware distribution
- **Blockchain C2 Infrastructure**: Using Polygon blockchain to store encrypted botnet commands for takedown resistance
- **Social Engineering**: ClickFix attacks and fake gaming utility distribution via chat platforms
- **API Key Abuse**: Exploiting exposed Google Cloud keys for unauthorized AI service access

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new malware tools for air-gapped network infiltration and covert surveillance operations
- **ScarCruft (North Korean)**: Using Zoho WorkDrive for C2 communications and USB malware for air-gapped network breaches
- **Sophisticated Unknown Actor**: Conducting three-year exploitation campaign against Cisco SD-WAN infrastructure with minimal forensic footprint
- **Kimwolf Botnet Operators**: Operating world's largest botnet through disclosed vulnerability exploitation
- **The Com Cybercrime Collective**: Targeting children and teenagers through online platforms, resulting in 30 arrests
- **Aeternum C2 Operators**: Developing blockchain-based botnet infrastructure for takedown resistance
- **Cryptocurrency Thieves**: Exploiting browser extensions and government data exposure for digital asset theft
- **Gaming Community Attackers**: Distributing Java-based RATs through trojanized gaming utilities via browsers and chat platforms