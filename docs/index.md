# Exploitation Report

Critical zero-day vulnerabilities are currently being exploited in the wild, posing significant risks to enterprise infrastructure. Notable active exploitation includes VMware ESXi zero-day vulnerabilities being leveraged by Chinese threat actors for virtual machine escape attacks, and a critical HPE OneView flaw (CVE-2025-37164) achieving maximum severity CVSS scoring. Additionally, sophisticated threat actor campaigns are targeting organizations through spear-phishing operations, with Russian APT28 conducting credential harvesting attacks and North Korean actors employing malicious QR codes in targeted campaigns.

## Active Exploitation Details

### VMware ESXi Zero-Day Vulnerabilities
- **Description**: Previously unknown vulnerabilities in VMware ESXi hypervisor allowing virtual machine escape
- **Impact**: Attackers can break out of virtual machine containment and gain access to the underlying hypervisor infrastructure
- **Status**: Actively exploited by Chinese-speaking threat actors, may have been developed years ago

### HPE OneView Critical Flaw
- **Description**: Maximum severity vulnerability in HPE's IT infrastructure management platform
- **Impact**: Remote code execution capabilities leading to complete system compromise
- **Status**: Actively exploited in the wild with devastating potential consequences
- **CVE ID**: CVE-2025-37164

### Trend Micro Apex Central RCE Vulnerability
- **Description**: Critical remote code execution vulnerability in on-premise Windows versions of Apex Central
- **Impact**: Arbitrary code execution on affected security management systems
- **Status**: Patches available, CVSS score of 9.8

## Affected Systems and Products

- **VMware ESXi**: Hypervisor infrastructure in enterprise environments
- **HPE OneView**: IT infrastructure management platforms across organizations
- **Trend Micro Apex Central**: On-premise Windows versions of the security management platform
- **SonicWall VPN Appliances**: Used as initial access vector in ESXi attacks
- **Misconfigured Proxy Servers**: Providing unauthorized access to commercial LLM services
- **Android TV Streaming Devices**: Over 2 million devices infected by Kimwolf botnet
- **Chrome Browser Extensions**: 900,000 users affected by fake AI extensions

## Attack Vectors and Techniques

- **Spear-Phishing Campaigns**: Targeted email attacks delivering malicious payloads and credential harvesting
- **Malicious QR Codes**: North Korean actors embedding malicious links in QR codes for mobile targeting
- **WhatsApp Worm Distribution**: Auto-messaging functionality spreading Astaroth banking trojan in Brazil
- **Proxy Server Exploitation**: Systematic hunting for misconfigured proxies to access paid services
- **Virtual Machine Escape**: Exploiting hypervisor vulnerabilities to break containment
- **Password Reset Abuse**: Mass-requesting password reset emails for account takeover attempts
- **Prompt Injection Attacks**: ZombieAgent exploit targeting ChatGPT's memory feature

## Threat Actor Activities

- **Chinese-Speaking Actors**: Leveraging compromised SonicWall VPN appliances to deploy VMware ESXi exploits for virtual machine escape attacks
- **Russian APT28 (Fancy Bear)**: Conducting credential harvesting campaigns targeting Turkish energy and nuclear research agencies, as well as strategic organizations
- **Iranian MuddyWater**: Launching RustyWater RAT via spear-phishing across Middle East diplomatic, maritime, financial, and telecom sectors
- **North Korean State-Sponsored Groups**: Using malicious QR codes in spear-phishing campaigns targeting specific organizations and individuals
- **Black Axe Criminal Network**: 34 members arrested in Spain for €5.9M fraud operations and organized cybercrime activities
- **Banking Trojan Operators**: Distributing Astaroth malware through WhatsApp worm campaigns targeting Brazilian users