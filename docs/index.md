# Exploitation Report

The current threat landscape reveals several critical exploitation activities spanning from zero-day vulnerabilities to sophisticated botnet operations. Most notably, HPE OneView faces active exploitation of CVE-2025-37164, a maximum severity flaw enabling remote code execution. Meanwhile, VMware ESXi zero-day vulnerabilities have been exploited by Chinese-speaking threat actors for over a year before disclosure. State-sponsored groups are intensifying their campaigns, with North Korean Kimsuky actors deploying malicious QR codes in spear-phishing operations, while Chinese-linked UAT-7290 targets telecommunications providers using Linux malware. The destructive Kimwolf botnet has rapidly infected over two million Android TV devices, and cybercriminals are leveraging fake AI Chrome extensions to harvest data from 900,000 users.

## Active Exploitation Details

### HPE OneView Remote Code Execution Flaw
- **Description**: A maximum severity vulnerability affecting HPE's IT infrastructure management platform that enables remote code execution
- **Impact**: Attackers can achieve devastating consequences through remote code execution on critical infrastructure management systems
- **Status**: Currently being exploited in the wild
- **CVE ID**: CVE-2025-37164

### VMware ESXi Zero-Day Vulnerabilities
- **Description**: Previously unknown vulnerabilities in VMware ESXi that were exploited using a sophisticated toolkit delivered through compromised SonicWall VPN appliances
- **Impact**: Complete compromise of virtualized infrastructure environments
- **Status**: Exploited in the wild approximately one year before official disclosure, with exploit toolkit appearing to predate vulnerability disclosure significantly
- **CVE ID**: Not specified in the articles

### Trend Micro Apex Central RCE Vulnerability
- **Description**: Critical security flaw in on-premise versions of Apex Central for Windows that allows arbitrary code execution with SYSTEM privileges
- **Impact**: Attackers can gain complete system control with highest privilege levels
- **Status**: Recently patched by Trend Micro with CVSS score of 9.8
- **CVE ID**: Not specified in the articles

## Affected Systems and Products

- **HPE OneView**: IT infrastructure management platform experiencing active exploitation
- **VMware ESXi**: Virtualization platform targeted with zero-day exploits via compromised SonicWall VPN appliances
- **Trend Micro Apex Central**: On-premise Windows versions vulnerable to remote code execution
- **Android TV Streaming Devices**: Over 2 million devices infected by Kimwolf botnet through unofficial streaming applications
- **Chrome Browser Extensions**: Fake AI-powered extensions affecting approximately 900,000 users
- **Cisco Identity Services Engine (ISE)**: Network access control platform with public proof-of-concept exploit available
- **Coolify Platform**: Self-hosted deployment platform affected by 11 critical vulnerabilities
- **npm Package Repository**: Bitcoin-themed packages containing NodeCordRAT malware

## Attack Vectors and Techniques

- **QR Code Phishing**: North Korean Kimsuky group using malicious QR codes in targeted spear-phishing campaigns against U.S. organizations
- **VPN Appliance Compromise**: Chinese actors leveraging compromised SonicWall VPN devices to deliver VMware exploit toolkits
- **Botnet Distribution**: Mass compromise of unofficial Android TV streaming applications to deploy Kimwolf botnet
- **Supply Chain Attacks**: Malicious npm packages disguised as Bitcoin-related tools delivering NodeCordRAT
- **Browser Extension Impersonation**: Fake AI Chrome extensions mimicking legitimate tools to harvest ChatGPT and DeepSeek data
- **WhatsApp Auto-Messaging**: Worm propagation spreading Astaroth banking trojan across Brazil through automated contact messaging
- **Edge Device Exploitation**: China-linked actors targeting telecommunications providers through network edge device vulnerabilities

## Threat Actor Activities

- **Kimsuky (North Korean APT)**: Conducting spear-phishing campaigns using malicious QR codes targeting U.S. organizations, representing evolution in social engineering tactics
- **Chinese-Speaking Threat Actors**: Operating sophisticated VMware ESXi exploitation campaigns using zero-day vulnerabilities and compromised VPN infrastructure
- **UAT-7290 (China-Linked)**: Espionage-focused intrusions against South Asian and Southeastern European telecommunications entities using Linux malware and ORB nodes
- **Brazilian Cybercriminals**: WhatsApp-based distribution campaign spreading Astaroth banking trojan through automated messaging worm
- **Supply Chain Attackers**: Targeting npm ecosystem with NodeCordRAT hidden in Bitcoin-themed packages to compromise developer environments