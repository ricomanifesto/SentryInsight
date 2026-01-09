# Exploitation Report

Critical exploitation activity is currently dominated by sophisticated state-sponsored campaigns and high-impact vulnerabilities across enterprise infrastructure. Chinese-linked threat actors are actively exploiting edge devices to breach telecommunications providers, while North Korean groups are leveraging innovative QR code phishing techniques. A maximum severity vulnerability in HPE OneView is being exploited in the wild, alongside active exploitation of previously undisclosed VMware ESXi zero-day vulnerabilities that may have been compromised for over a year before public disclosure. Trend Micro's Apex Central platform faces critical remote code execution vulnerabilities, while multiple botnet operations and malware distribution campaigns continue to target millions of devices globally.

## Active Exploitation Details

### VMware ESXi Zero-Day Vulnerabilities
- **Description**: Previously undisclosed zero-day vulnerabilities in VMware ESXi that were exploited using a sophisticated toolkit
- **Impact**: Chinese-speaking threat actors gained unauthorized access to ESXi infrastructure through compromised SonicWall VPN appliances
- **Status**: Vulnerabilities were exploited approximately one year before public disclosure; patches now available

### HPE OneView Critical Vulnerability
- **Description**: Maximum severity vulnerability in HPE's IT infrastructure management platform
- **Impact**: Remote code execution capabilities that can lead to devastating consequences for enterprise infrastructure
- **Status**: Currently being exploited in the wild
- **CVE ID**: CVE-2025-37164

### Trend Micro Apex Central Remote Code Execution
- **Description**: Critical security flaw in Trend Micro Apex Central (on-premise) that scores 9.8 on the CVSS scale
- **Impact**: Allows attackers to execute arbitrary code with SYSTEM privileges on Windows-based installations
- **Status**: Patches have been released by Trend Micro

### Cisco Identity Services Engine Vulnerability
- **Description**: Medium-severity security flaw in Cisco Identity Services Engine (ISE) and ISE Passive Identity Connector
- **Impact**: Potential security bypass and unauthorized access
- **Status**: Public proof-of-concept exploit available; Cisco has released security updates

### Coolify Platform Critical Flaws
- **Description**: Eleven critical-severity security vulnerabilities affecting the open-source self-hosting platform
- **Impact**: Authentication bypass and remote code execution leading to full server compromise
- **Status**: Disclosed vulnerabilities affecting self-hosted instances

## Affected Systems and Products

- **Trend Micro Apex Central**: On-premise Windows versions vulnerable to critical RCE
- **VMware ESXi**: Infrastructure platforms targeted by Chinese threat actors with zero-day exploits
- **HPE OneView**: IT infrastructure management platform facing active exploitation
- **Cisco ISE/ISE-PIC**: Identity Services Engine products with publicly available exploits
- **SonicWall VPN Appliances**: Used as initial access vectors for ESXi exploitation
- **Telecommunications Infrastructure**: Edge devices targeted by China-linked campaigns
- **Android TV Devices**: Over 2 million devices infected by Kimwolf botnet
- **Chrome Browser Extensions**: Fake AI extensions compromising 900,000 users
- **Coolify Self-Hosted Instances**: Open-source platform installations vulnerable to complete compromise

## Attack Vectors and Techniques

- **QR Code Phishing**: North Korean Kimsuky group using malicious QR codes in spear-phishing campaigns targeting U.S. organizations
- **Edge Device Exploitation**: China-linked UAT-7290 targeting telecommunications providers through edge device vulnerabilities
- **WhatsApp Worm Distribution**: Astaroth banking trojan spreading through contact auto-messaging in Brazil
- **npm Package Poisoning**: NodeCordRAT malware distributed through malicious Bitcoin-themed npm packages
- **Chrome Extension Mimicry**: Fake AI-powered extensions harvesting ChatGPT and DeepSeek data
- **VPN Appliance Compromise**: Initial access through compromised SonicWall devices for ESXi exploitation
- **Linux Malware Deployment**: Sophisticated Linux-based malware targeting telecommunications infrastructure

## Threat Actor Activities

- **China-linked UAT-7290**: Espionage-focused intrusions against entities in South Asia and Southeastern Europe using Linux malware and ORB nodes
- **Russian Fancy Bear (APT28)**: Continuing global secrets theft operations using basic but highly effective techniques
- **North Korean Kimsuky**: Implementing QR code-based phishing campaigns targeting U.S. organizations and government entities
- **Chinese-speaking Groups**: Operating VMware ESXi exploitation toolkit for over a year before vulnerability disclosure
- **Brazilian Cybercriminals**: Distributing Astaroth banking trojan through WhatsApp worm campaigns
- **Kimwolf Botnet Operators**: Successfully compromising over 2 million Android TV devices through mass exploitation
- **npm Package Attackers**: Deploying NodeCordRAT through malicious cryptocurrency-themed packages