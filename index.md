# Exploitation Report

Critical exploitation activity continues to escalate with threat actors targeting multiple high-value systems across various sectors. A maximum-severity HPE OneView vulnerability (CVE-2025-37164) has been actively exploited in the wild, enabling remote code execution on IT infrastructure management platforms. Chinese-speaking threat actors are leveraging compromised SonicWall VPN appliances to deploy VMware ESXi exploit toolkits, with evidence suggesting these zero-day exploits were developed and used up to a year before their public disclosure. Additionally, attackers are exploiting a critical zero-day flaw in end-of-life D-Link DSL routers, while the UAT-7290 Chinese threat group continues sophisticated espionage campaigns targeting telecommunications providers across South Asia and Southeastern Europe using Linux malware and edge device exploits.

## Active Exploitation Details

### HPE OneView Maximum Severity Flaw
- **Description**: Critical vulnerability in HPE's IT infrastructure management platform that enables remote code execution
- **Impact**: Attackers can achieve complete system compromise, leading to devastating consequences for enterprise infrastructure management
- **Status**: Actively exploited in the wild, flagged by CISA as exploited
- **CVE ID**: CVE-2025-37164

### VMware ESXi Zero-Day Exploits
- **Description**: Previously unknown vulnerabilities in VMware ESXi hypervisors that were exploited by sophisticated threat actors
- **Impact**: Complete virtualization infrastructure compromise, allowing attackers to control host systems and all virtual machines
- **Status**: Exploited for approximately one year before disclosure, delivered via compromised SonicWall VPN appliances

### D-Link DSL Router Zero-Day
- **Description**: Critical zero-day vulnerability affecting end-of-life D-Link DSL routers
- **Impact**: Allows attackers to execute arbitrary commands on vulnerable devices
- **Status**: Currently being exploited in active campaigns targeting unsupported router models

### Microsoft Office Vulnerability
- **Description**: Security flaw in Microsoft Office applications being exploited by threat actors
- **Impact**: Enables unauthorized access and potential system compromise through document-based attacks
- **Status**: Flagged by CISA as actively exploited

## Affected Systems and Products

- **HPE OneView**: IT infrastructure management platform with maximum severity vulnerability
- **VMware ESXi**: Hypervisor platform targeted by Chinese threat actors using zero-day exploits
- **D-Link DSL Routers**: End-of-life router models vulnerable to zero-day exploitation
- **Microsoft Office**: Office applications with actively exploited security flaws
- **SonicWall VPN Appliances**: Used as compromise vectors for ESXi exploit delivery
- **Telecommunications Infrastructure**: Edge devices and network equipment targeted by UAT-7290
- **Android TV Devices**: Over two million devices infected by Kimwolf botnet through unofficial streaming apps

## Attack Vectors and Techniques

- **VPN Appliance Compromise**: Chinese actors using compromised SonicWall VPN devices to deliver ESXi exploit toolkits
- **Edge Device Exploitation**: Telecommunications providers targeted through vulnerable edge network equipment
- **Zero-Day Exploitation**: Long-term use of undisclosed vulnerabilities before public awareness
- **Botnet Distribution**: Mass compromise of Android TV devices through malicious streaming applications
- **QR Code Phishing**: North Korean Kimsuky group using malicious QR codes in spearphishing campaigns
- **WhatsApp Worm Distribution**: Banking trojans spread through contact auto-messaging on WhatsApp platform
- **Chrome Extension Impersonation**: Fake AI-powered extensions stealing user data from 900,000 users

## Threat Actor Activities

- **Chinese Threat Groups**: Sophisticated espionage operations targeting telecommunications and virtualization infrastructure using advanced zero-day exploits and compromised VPN appliances
- **UAT-7290**: China-nexus threat actor conducting espionage-focused intrusions against entities in South Asia and Southeastern Europe using Linux malware and ORB nodes
- **Kimsuky (North Korean APT)**: State-sponsored group deploying QR code-based phishing campaigns targeting U.S. organizations
- **Banking Trojan Operators**: Cybercriminals using WhatsApp worm distribution to spread Astaroth banking malware across Brazil
- **Botnet Operators**: Criminal groups behind Aisuru and Kimwolf botnets targeting Android TV streaming devices for mass compromise