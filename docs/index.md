# Exploitation Report

Critical exploitation activity is dominating the cybersecurity landscape with multiple high-severity vulnerabilities being actively exploited across enterprise infrastructure. Trend Micro's Apex Central faces a critical remote code execution flaw with a 9.8 CVSS score that allows attackers to execute arbitrary code with SYSTEM privileges. HPE OneView is experiencing active exploitation of CVE-2025-37164, enabling remote code execution on IT infrastructure management platforms. Chinese-speaking threat actors are leveraging previously unknown VMware ESXi zero-day vulnerabilities that were likely exploited for over a year before disclosure, while sophisticated campaigns target telecommunications providers through edge device exploits and Linux-based malware.

## Active Exploitation Details

### Trend Micro Apex Central RCE Vulnerability
- **Description**: A critical security flaw in Trend Micro Apex Central (on-premise) Windows versions that allows remote code execution
- **Impact**: Attackers can execute arbitrary code with SYSTEM privileges, leading to complete system compromise
- **Status**: Recently patched by Trend Micro; affects on-premise Windows versions

### HPE OneView Maximum Severity Flaw
- **Description**: A maximum severity vulnerability in HPE's IT infrastructure management platform
- **Impact**: Enables remote code execution with devastating consequences for infrastructure management
- **Status**: Currently being exploited in the wild
- **CVE ID**: CVE-2025-37164

### VMware ESXi Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in VMware ESXi that were exploited using a specialized toolkit
- **Impact**: Complete hypervisor compromise allowing attackers to control virtual infrastructure
- **Status**: Exploited for approximately one year before public disclosure; delivered via compromised SonicWall VPN appliances

### Coolify Critical Vulnerabilities
- **Description**: Eleven critical-severity security flaws affecting the open-source, self-hosting platform
- **Impact**: Authentication bypass and remote code execution leading to full server compromise
- **Status**: Recently disclosed; affects self-hosted instances

### Cisco Identity Services Engine Vulnerability
- **Description**: Medium-severity security flaw in Cisco ISE and ISE Passive Identity Connector
- **Impact**: Exploitable by attackers with admin privileges
- **Status**: Recently patched after public proof-of-concept exploit release

## Affected Systems and Products

- **Trend Micro Apex Central**: On-premise Windows versions affected by critical RCE vulnerability
- **HPE OneView**: IT infrastructure management platform experiencing active exploitation
- **VMware ESXi**: Hypervisor infrastructure compromised through zero-day exploits
- **SonicWall VPN Appliances**: Used as initial compromise vector for ESXi attacks
- **Coolify Platform**: Self-hosted instances vulnerable to complete server compromise
- **Cisco ISE/ISE-PIC**: Identity Services Engine and Passive Identity Connector affected
- **Telecommunications Infrastructure**: Edge devices and Linux-based systems targeted by sophisticated actors
- **Chrome Extensions**: Fake AI extensions affecting approximately 900,000 users
- **Android TV Devices**: Over 2 million devices infected by Kimwolf botnet through unofficial streaming boxes

## Attack Vectors and Techniques

- **Edge Device Exploitation**: Targeting telecommunications providers through compromised edge infrastructure
- **VPN Appliance Compromise**: Using compromised SonicWall devices to deliver ESXi exploit toolkits
- **Linux Malware Deployment**: Sophisticated actors using custom Linux-based malware against telecoms
- **QR Code Phishing**: North Korean Kimsuky group leveraging malicious QR codes in spear-phishing campaigns
- **Social Engineering**: Enhanced QR code attacks targeting U.S. organizations
- **Supply Chain Attacks**: Malicious npm packages delivering NodeCordRAT malware through Bitcoin-themed packages
- **Extension Impersonation**: Fake AI Chrome extensions mimicking legitimate tools to harvest user data
- **WhatsApp Distribution**: Astaroth banking trojan spreading via WhatsApp auto-messaging worm in Brazil
- **Botnet Mass Compromise**: Kimwolf botnet rapidly infecting millions of Android TV streaming devices

## Threat Actor Activities

- **Chinese-Speaking Threat Actors**: Deploying VMware ESXi exploit toolkits and targeting telecommunications infrastructure with advanced Linux malware
- **UAT-7290**: China-linked group conducting espionage operations against South Asia and Southeastern Europe telecoms using ORB nodes
- **North Korean Kimsuky Group**: Implementing QR code-based spear-phishing campaigns targeting U.S. organizations with sophisticated social engineering
- **Cybercriminal Groups**: Operating Aisuru and Kimwolf botnets affecting millions of devices globally
- **Banking Trojan Operators**: Distributing Astaroth malware through WhatsApp worm campaigns in Brazil
- **Supply Chain Attackers**: Embedding NodeCordRAT in npm packages targeting cryptocurrency enthusiasts and developers