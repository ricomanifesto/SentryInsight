# Exploitation Report

Critical exploitation activity is currently targeting high-value enterprise infrastructure across multiple attack vectors. Chinese-linked threat actors are actively exploiting edge devices and telecommunications infrastructure using sophisticated Linux malware, while a maximum-severity HPE OneView vulnerability (CVE-2025-37164) is being exploited to enable remote code execution on IT management platforms. Additionally, threat actors are leveraging zero-day vulnerabilities in VMware ESXi systems that were exploited for over a year before disclosure, and attacking end-of-life D-Link routers through zero-day flaws. North Korean groups continue their campaigns using novel QR code phishing techniques, while malicious botnets like Kimwolf have infected over two million Android TV devices. The exploitation landscape also includes fake AI Chrome extensions stealing data from 900,000 users and sophisticated social engineering campaigns targeting Office 365 users.

## Active Exploitation Details

### HPE OneView Critical Vulnerability
- **Description**: A maximum-severity vulnerability in HPE's IT infrastructure management platform that enables remote code execution
- **Impact**: Attackers can achieve complete system compromise and gain control over critical IT infrastructure management systems
- **Status**: Actively exploited in the wild and flagged by CISA as a known exploited vulnerability
- **CVE ID**: CVE-2025-37164

### VMware ESXi Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in VMware ESXi hypervisor systems that were developed and exploited long before public disclosure
- **Impact**: Complete compromise of virtualization infrastructure, potentially affecting multiple virtual machines and critical services
- **Status**: Chinese-speaking threat actors used compromised SonicWall VPN appliances to deliver exploit toolkits targeting these vulnerabilities over a year before disclosure

### D-Link Router Zero-Day
- **Description**: Critical zero-day vulnerability affecting end-of-life D-Link DSL routers
- **Impact**: Allows attackers to run arbitrary commands on compromised router devices
- **Status**: Currently being exploited in active attacks against unsupported D-Link devices

### Microsoft Office Vulnerability
- **Description**: Security flaw impacting Microsoft Office products
- **Impact**: Enables various attack vectors against Office users and environments
- **Status**: Flagged by CISA as actively exploited

### Cisco Identity Services Engine Vulnerability
- **Description**: Medium-severity security flaw in Cisco ISE and ISE Passive Identity Connector
- **Impact**: Authentication bypass and potential system compromise for attackers with administrative privileges
- **Status**: Public proof-of-concept exploit code available, patches released by Cisco

## Affected Systems and Products

- **HPE OneView**: IT infrastructure management platform experiencing maximum-severity exploitation
- **VMware ESXi**: Hypervisor systems targeted by Chinese threat actors using year-old exploit toolkits
- **D-Link DSL Routers**: End-of-life router models under active zero-day attack
- **Microsoft Office**: Office products targeted through known exploited vulnerabilities
- **Cisco ISE/ISE-PIC**: Identity Services Engine platforms with public exploit code available
- **Android TV Devices**: Over two million devices infected by Kimwolf botnet
- **Chrome Browser Extensions**: Fake AI extensions compromising 900,000 users
- **SonicWall VPN Appliances**: Used as initial access vectors for ESXi attacks
- **Telecommunications Infrastructure**: Targeted by China-linked groups using Linux malware

## Attack Vectors and Techniques

- **Edge Device Exploitation**: Chinese-linked actors targeting telecommunications providers through compromised edge infrastructure
- **QR Code Phishing**: North Korean Kimsuky group using malicious QR codes in spearphishing campaigns against U.S. organizations
- **VPN Appliance Compromise**: Threat actors using compromised SonicWall devices as entry points for broader infrastructure attacks
- **Malicious Browser Extensions**: Fake AI-powered Chrome extensions harvesting ChatGPT and DeepSeek data before sending to command and control servers
- **Social Engineering**: Office 365 phishing campaigns targeting users with weak security configurations
- **Botnet Propagation**: Mass compromise of Android TV streaming devices through unofficial applications
- **Supply Chain Attacks**: Malicious npm packages delivering NodeCordRAT through Bitcoin-themed package names
- **WhatsApp Worm Distribution**: Banking trojans spread through WhatsApp auto-messaging across Brazil

## Threat Actor Activities

- **China-Linked UAT-7290**: Conducting espionage-focused intrusions against entities in South Asia and Southeastern Europe using Linux malware and ORB nodes for telecommunications targeting
- **Chinese-Speaking Groups**: Deploying VMware ESXi exploit toolkits through compromised VPN appliances, demonstrating advanced persistent threat capabilities
- **North Korean Kimsuky**: Using QR code-based spearphishing campaigns to target U.S. organizations with novel social engineering techniques
- **Brazilian Cybercriminals**: Distributing Astaroth banking trojan through WhatsApp worm campaigns targeting financial institutions
- **Chrome Extension Attackers**: Operating fake AI extension campaigns that have successfully compromised data from 900,000 users
- **Botnet Operators**: Managing Kimwolf botnet with over two million infected Android TV devices for potential large-scale attacks