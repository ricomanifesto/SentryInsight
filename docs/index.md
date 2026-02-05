# Exploitation Report

The current threat landscape reveals several critical exploitation campaigns actively targeting enterprise infrastructure and cloud environments. Ransomware operators have intensified their focus on network edge devices, particularly targeting VMware ESXi environments and legacy vulnerabilities in enterprise platforms. Notable threat actors including Chinese state-sponsored groups and Iranian cyber espionage teams are leveraging both recently disclosed vulnerabilities and older unpatched flaws to compromise high-value targets. Critical vulnerabilities in workflow automation platforms and web traffic hijacking campaigns demonstrate the evolving sophistication of attack methodologies against modern enterprise infrastructure.

## Active Exploitation Details

### n8n Workflow Automation Platform Vulnerability
- **Description**: Critical security vulnerability in the n8n workflow automation platform enabling arbitrary system command execution
- **Impact**: Complete control of host server and escape from environment confines
- **Status**: Critical vulnerability with public exploits disclosed
- **CVE ID**: CVE-2026-25049

### VMware ESXi Sandbox Escape Vulnerability
- **Description**: High-severity VMware ESXi vulnerability allowing escape from sandbox environment
- **Impact**: Used in zero-day attacks since February 2024, now exploited by ransomware gangs
- **Status**: Actively exploited in ransomware attacks, confirmed by CISA

### GitLab Authentication Bypass
- **Description**: Five-year-old GitLab vulnerability allowing authentication bypass
- **Impact**: Unauthorized access to GitLab repositories and systems
- **Status**: Actively exploited in attacks, added to CISA KEV catalog

### SolarWinds Web Help Desk Remote Code Execution
- **Description**: Critical security flaw in SolarWinds Web Help Desk platform
- **Impact**: Remote code execution capabilities on affected systems
- **Status**: Actively exploited, added to CISA KEV catalog

### WinRAR Vulnerability Exploitation
- **Description**: Vulnerability in WinRAR archiving software exploited in targeted campaigns
- **Impact**: Initial access vector for espionage operations
- **Status**: Actively exploited by Chinese APT groups
- **CVE ID**: CVE-2025-8088

## Affected Systems and Products

- **n8n Workflow Automation Platform**: Open-source automation platform vulnerable to system command execution
- **VMware ESXi**: Enterprise virtualization platform targeted in ransomware campaigns
- **GitLab**: Source code management platform with authentication bypass vulnerability
- **SolarWinds Web Help Desk**: IT service management platform with RCE vulnerability
- **WinRAR**: File archiving software exploited in espionage campaigns
- **NGINX Servers**: Web servers compromised for traffic hijacking campaigns
- **Betterment Platform**: Financial technology platform with data breach affecting 1.4 million accounts
- **Zendesk Support Systems**: Customer support platforms exploited for spam campaigns
- **Google Looker**: Business intelligence platform with cross-tenant vulnerabilities

## Attack Vectors and Techniques

- **Web Traffic Hijacking**: Malicious NGINX configurations used to redirect and hijack user traffic through attacker infrastructure
- **Malicious Workflows**: Exploitation of n8n platform through crafted workflows containing system commands
- **Spear-phishing Campaigns**: Targeted email attacks using legitimate file formats like VHD files hosted on IPFS
- **Screensaver Malware**: Unusual use of .scr file types to drop malware and remote management tools
- **EDR Evasion**: Use of legitimate but revoked kernel drivers to detect and disable security tools
- **Cross-platform Infostealers**: Python-based malware targeting macOS through fake advertisements and installers
- **Ransomware Infrastructure**: Cartel-based cooperation models among ransomware groups for coordinated attacks

## Threat Actor Activities

- **Infy (Prince of Persia)**: Iranian threat group resuming operations with new command-and-control infrastructure after internet blackout
- **Amaranth Dragon**: Chinese state-sponsored group linked to APT41, conducting espionage campaigns against Southeast Asian government and law enforcement agencies
- **DragonForce Ransomware**: Organized cartel emphasizing cooperation among ransomware gangs since 2023
- **DEAD#VAX Campaign**: Sophisticated malware operation deploying AsyncRAT through IPFS-hosted VHD phishing files
- **Iranian Cyber Operations**: Continued espionage targeting expats, Syrians, and Israelis using credential theft and social engineering
- **React2Shell Operators**: Threat actors conducting large-scale web traffic hijacking through compromised NGINX servers