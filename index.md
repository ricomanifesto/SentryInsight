# Exploitation Report

Current threat intelligence reveals a concerning surge in exploitation activity across multiple platforms and sectors. Critical vulnerabilities in n8n workflow automation platform, VMware ESXi, and SolarWinds Web Help Desk are being actively exploited, with ransomware groups increasingly targeting these systems. Chinese-linked threat actors are leveraging WinRAR vulnerabilities for espionage campaigns, while a sophisticated web traffic hijacking operation is compromising NGINX servers worldwide. The resurgence of the Iranian Infy group with new command-and-control infrastructure, combined with ongoing exploitation of five-year-old GitLab vulnerabilities, demonstrates the persistent and evolving nature of current cyber threats.

## Active Exploitation Details

### n8n Workflow Automation Platform Vulnerability
- **Description**: Critical security vulnerability in the n8n workflow automation platform that allows escaping the confines of the environment and taking complete control of the host server
- **Impact**: Arbitrary system command execution through malicious workflows, complete server compromise
- **Status**: Critical vulnerability with public exploits disclosed
- **CVE ID**: CVE-2026-25049

### VMware ESXi Sandbox Escape Vulnerability
- **Description**: High-severity VMware ESXi sandbox escape vulnerability that has been exploited in zero-day attacks since at least February 2024
- **Impact**: Ransomware gangs can escape virtualized environments and compromise host systems
- **Status**: Now actively exploited by ransomware groups, confirmed by CISA
- **CVE ID**: Not specified in the articles

### SolarWinds Web Help Desk Remote Code Execution
- **Description**: Critical security flaw in SolarWinds Web Help Desk (WHD) allowing remote code execution
- **Impact**: Complete system compromise and potential lateral movement within enterprise networks
- **Status**: Actively exploited and added to CISA's KEV catalog
- **CVE ID**: Not specified in the articles

### GitLab Five-Year-Old Vulnerability
- **Description**: A five-year-old GitLab vulnerability that is actively being exploited in attacks against government systems
- **Impact**: Unauthorized access to code repositories and development environments
- **Status**: Active exploitation confirmed by CISA, government agencies ordered to patch
- **CVE ID**: Not specified in the articles

### WinRAR Exploitation Vulnerability
- **Description**: Vulnerability in WinRAR being exploited by Chinese threat actors for espionage campaigns
- **Impact**: Used in targeted attacks against government and law enforcement agencies across Southeast Asia
- **Status**: Actively exploited by Amaranth Dragon group linked to APT41
- **CVE ID**: CVE-2025-8088

## Affected Systems and Products

- **n8n Platform**: Open-source workflow automation platform with critical command execution vulnerabilities
- **VMware ESXi**: Virtualization platform targeted by ransomware groups through sandbox escape flaws
- **SolarWinds Web Help Desk**: Enterprise help desk solution with remote code execution vulnerability
- **GitLab**: Development platform with persistent exploitation of legacy vulnerabilities
- **WinRAR**: Archive utility exploited in Chinese espionage campaigns
- **NGINX Servers**: Web servers compromised for traffic hijacking campaigns
- **Baota (BT) Management Panels**: Server management interfaces targeted alongside NGINX installations
- **Betterment Platform**: Fintech automated investment platform suffering data breach affecting 1.4 million accounts
- **Zendesk Systems**: Support platforms exploited for spam campaigns through unsecured configurations

## Attack Vectors and Techniques

- **Malicious Workflow Injection**: Attackers inject malicious workflows into n8n platforms to execute arbitrary system commands
- **Sandbox Escape Exploitation**: VMware ESXi vulnerabilities exploited to break out of virtualized environments
- **Web Traffic Hijacking**: NGINX servers compromised to redirect user traffic through attacker-controlled infrastructure
- **Screensaver Malware Delivery**: Windows screensaver (.scr) files used to drop malware and remote monitoring tools
- **IPFS-Hosted Phishing**: DEAD#VAX campaign uses InterPlanetary File System to host VHD phishing files deploying AsyncRAT
- **Kernel Driver Abuse**: EDR killer tools using signed but revoked EnCase kernel drivers to bypass security solutions
- **Social Engineering Campaigns**: Iranian actors using spear-phishing and social engineering against Middle Eastern targets
- **Supply Chain Targeting**: Exploitation of legitimate software components and trusted system features for evasion

## Threat Actor Activities

- **Amaranth Dragon**: Chinese-linked group associated with APT41, targeting government and law enforcement in Southeast Asia using WinRAR exploits
- **Infy (Prince of Persia)**: Iranian threat group resuming operations with new C2 infrastructure after internet blackout, targeting expats, Syrians, and Israelis
- **DragonForce Ransomware**: Operating cartel model since 2023, emphasizing cooperation among ransomware gangs
- **DEAD#VAX Campaign**: Sophisticated malware operation using disciplined tradecraft and legitimate system feature abuse
- **NGINX Traffic Hijackers**: Organized campaign compromising web servers and management panels for large-scale traffic redirection
- **EDR Killer Operators**: Attackers using forensic software drivers to detect and disable 59 different security tools