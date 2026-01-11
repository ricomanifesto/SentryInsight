# Exploitation Report

Current cybersecurity landscape shows significant active exploitation across multiple vectors, with critical vulnerabilities being exploited in VMware ESXi infrastructure and HPE OneView platforms. Chinese-speaking threat actors are leveraging zero-day VMware ESXi vulnerabilities for virtual machine escape attacks, while HPE OneView faces maximum severity exploitation enabling remote code execution. State-sponsored groups including Russian APT28, Iranian MuddyWater, and North Korean actors are conducting sophisticated campaigns targeting energy organizations, diplomatic entities, and global infrastructure through credential harvesting, spear-phishing, and malicious QR codes.

## Active Exploitation Details

### VMware ESXi Zero-Day Vulnerabilities
- **Description**: Zero-day vulnerabilities in VMware ESXi allowing virtual machine escape attacks
- **Impact**: Attackers can escape virtual machine isolation and gain access to the underlying hypervisor infrastructure
- **Status**: Actively exploited by Chinese-speaking threat actors, patch status unclear

### HPE OneView Remote Code Execution Vulnerability
- **Description**: Maximum severity vulnerability in HPE's IT infrastructure management platform
- **Impact**: Enables remote code execution with devastating consequences for infrastructure management
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2025-37164

### Trend Micro Apex Central Remote Code Execution Vulnerability
- **Description**: Critical security flaw in Trend Micro Apex Central on-premise Windows versions
- **Impact**: Allows attackers to execute arbitrary code with SYSTEM privileges
- **Status**: Recently patched, scored 9.8 CVSS

## Affected Systems and Products

- **VMware ESXi**: Hypervisor infrastructure targeted by zero-day exploits for virtual machine escape
- **HPE OneView**: IT infrastructure management platform with maximum severity RCE vulnerability
- **Trend Micro Apex Central**: On-premise Windows versions affected by critical RCE flaw
- **SonicWall VPN Appliances**: Used as initial access vector in VMware ESXi compromise campaigns
- **Misconfigured Proxy Servers**: Systematically targeted for unauthorized access to commercial LLM services
- **WhatsApp Platform**: Used as distribution vector for banking trojans in Brazil
- **Chrome Browser Extensions**: Fake AI extensions harvesting data from 900,000 users
- **ChatGPT Platform**: Memory feature exploited through "ZombieAgent" prompt injection attacks

## Attack Vectors and Techniques

- **Virtual Machine Escape**: Exploitation of VMware ESXi zero-days to break out of virtualized environments
- **Initial Access via VPN Compromise**: Using compromised SonicWall VPN appliances as entry points
- **Spear-Phishing Campaigns**: Targeted email attacks by MuddyWater and APT28 groups
- **Malicious QR Codes**: North Korean threat actors embedding malicious codes in phishing campaigns
- **Proxy Server Exploitation**: Systematic hunting for misconfigured proxies to access paid LLM services
- **WhatsApp Worm Distribution**: Auto-messaging contacts to spread banking trojans
- **Fake Browser Extensions**: Malicious Chrome extensions masquerading as AI tools
- **Prompt Injection Attacks**: Exploiting ChatGPT's memory feature through "ZombieAgent" techniques
- **Credential Harvesting**: Russian APT28 targeting energy and policy organizations

## Threat Actor Activities

- **Chinese-Speaking Threat Actors**: Exploiting VMware ESXi zero-days for infrastructure compromise, suspected development dating back years
- **MuddyWater (Iranian APT)**: Launching RustyWater RAT via spear-phishing targeting diplomatic, maritime, financial, and telecom entities across Middle East
- **APT28 (Russian Fancy Bear)**: Running credential-stealing campaigns against Turkish energy and nuclear research agencies, plus strategic targets globally
- **North Korean State Actors**: Deploying malicious QR codes in sophisticated spear-phishing operations
- **Black Axe Criminal Network**: 34 members arrested in Spain for €5.9M fraud and organized cybercrime activities
- **Brazilian Cybercriminals**: Distributing Astaroth banking trojan through WhatsApp worm campaigns
- **Chrome Extension Threat Actors**: Creating fake AI extensions to harvest ChatGPT and DeepSeek user data from 900,000 victims