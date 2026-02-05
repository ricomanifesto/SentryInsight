# Exploitation Report

Critical vulnerabilities across multiple platforms are experiencing active exploitation, ranging from zero-day attacks to widespread campaigns targeting infrastructure components. The most significant activity includes CVE-2026-25049 in n8n workflow automation platform enabling system command execution, CVE-2025-8088 WinRAR vulnerability being exploited by Chinese state-sponsored groups, and active ransomware campaigns exploiting VMware ESXi flaws. Additional concerning activity involves large-scale NGINX server compromises for traffic hijacking, exploitation of a five-year-old GitLab vulnerability, and SolarWinds Web Help Desk remote code execution flaws being added to CISA's Known Exploited Vulnerabilities catalog.

## Active Exploitation Details

### n8n Workflow Automation Platform Critical Flaw
- **Description**: Critical security vulnerability in the n8n open-source workflow automation platform that allows escaping environment confines and taking complete control of host servers
- **Impact**: Execution of arbitrary system commands and complete server compromise
- **Status**: Critical vulnerabilities disclosed with public exploits available
- **CVE ID**: CVE-2026-25049

### WinRAR Vulnerability
- **Description**: Security flaw in WinRAR being exploited by Chinese state-sponsored threat actors in espionage campaigns
- **Impact**: Used in cyber espionage operations targeting government and law enforcement agencies across Southeast Asia
- **Status**: Actively exploited by Amaranth Dragon APT group throughout 2025
- **CVE ID**: CVE-2025-8088

### VMware ESXi Sandbox Escape
- **Description**: High-severity VMware ESXi sandbox escape vulnerability previously used in zero-day attacks
- **Impact**: Ransomware gangs using this flaw to compromise virtualization infrastructure
- **Status**: CISA confirmed active exploitation in ransomware attacks

### GitLab Five-Year-Old Vulnerability
- **Description**: Legacy GitLab vulnerability that has remained unpatched for five years
- **Impact**: Active exploitation in attacks targeting government systems
- **Status**: CISA ordered government agencies to patch immediately due to active exploitation

### SolarWinds Web Help Desk RCE
- **Description**: Critical security flaw in SolarWinds Web Help Desk enabling remote code execution
- **Impact**: Complete system compromise through remote code execution
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

## Affected Systems and Products

- **n8n Workflow Automation Platform**: Open-source workflow automation systems vulnerable to command execution
- **WinRAR**: Archive utility being exploited in targeted espionage campaigns
- **VMware ESXi**: Virtualization infrastructure targeted by ransomware operators
- **NGINX Servers**: Web servers and management panels like Baota (BT) being compromised for traffic hijacking
- **GitLab**: Source code management platforms with legacy vulnerabilities
- **SolarWinds Web Help Desk**: IT service management platforms vulnerable to RCE
- **Microsoft Office**: RTF documents being weaponized for malware delivery
- **Google Looker**: Business intelligence platform with cross-tenant vulnerabilities
- **macOS Systems**: Apple systems increasingly targeted by Python-based infostealers

## Attack Vectors and Techniques

- **Malicious Workflows**: Attackers using crafted n8n workflows to execute system commands
- **Spear-Phishing**: Iranian threat actors using targeted phishing for credential theft
- **Social Engineering**: Sophisticated social engineering campaigns targeting Middle Eastern populations
- **Traffic Hijacking**: NGINX server compromises routing traffic through attacker infrastructure
- **Screensaver Malware**: Novel use of .scr files to deploy malware and RMM tools while evading detection
- **RTF Document Exploitation**: Microsoft Office RTF files weaponized for multistage infection chains
- **IPFS-Hosted VHD Files**: DEAD#VAX campaign using InterPlanetary File System to host malicious VHD phishing files
- **Fake Advertisements**: Python infostealers distributed through fake ads and installers targeting macOS
- **EDR Evasion**: Signed kernel drivers from forensic software being abused to disable security tools

## Threat Actor Activities

- **APT28**: Russian state-sponsored group weaponizing Microsoft Office bugs within 3 days of disclosure
- **Amaranth Dragon**: Chinese APT group linked to APT41, exploiting WinRAR vulnerabilities in Southeast Asian espionage campaigns
- **Iranian Threat Actors**: Conducting credential theft operations targeting expats, Syrians, and Israelis through spear-phishing
- **DragonForce Ransomware**: Operating cartel model emphasizing cooperation among ransomware gangs since 2023
- **DEAD#VAX Campaign**: Sophisticated malware operation deploying AsyncRAT via IPFS-hosted VHD phishing files
- **GlassWorm Operators**: Self-replicating malware campaign poisoning Open VSX software components with infostealer infections
- **NGINX Traffic Hijackers**: Threat actors compromising web servers to redirect user traffic through malicious infrastructure