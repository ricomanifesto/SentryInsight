# Exploitation Report

Critical vulnerabilities across multiple platforms are under active exploitation, with threat actors targeting everything from workflow automation platforms to enterprise virtualization infrastructure. The most severe activity includes exploitation of n8n workflow automation vulnerabilities enabling system command execution, VMware ESXi sandbox escape vulnerabilities being leveraged in ransomware campaigns, and China-linked espionage groups exploiting WinRAR flaws for targeted attacks. Additional concerning activity includes large-scale web traffic hijacking through compromised NGINX servers, abuse of legitimate kernel drivers for EDR evasion, and coordinated reconnaissance campaigns against Citrix NetScaler infrastructure using residential proxy networks.

## Active Exploitation Details

### n8n Workflow Automation Platform Critical Vulnerability
- **Description**: Critical security vulnerability in the n8n workflow automation platform enabling arbitrary system command execution through malicious workflows
- **Impact**: Complete system compromise and arbitrary command execution on host servers
- **Status**: Multiple critical vulnerabilities disclosed with public exploits available
- **CVE ID**: CVE-2026-25049

### VMware ESXi Sandbox Escape Vulnerability
- **Description**: High-severity VMware ESXi sandbox escape vulnerability previously exploited as a zero-day
- **Impact**: Escape from virtualized environment constraints, enabling broader system compromise
- **Status**: Now being actively exploited by ransomware gangs in ongoing attacks
- **CVE ID**: Not specified in articles

### WinRAR Vulnerability
- **Description**: Security flaw in WinRAR compression software being exploited in targeted espionage campaigns
- **Impact**: Used as initial attack vector for deploying espionage malware and maintaining persistent access
- **Status**: Actively exploited by China-linked Amaranth Dragon threat group
- **CVE ID**: CVE-2025-8088

### GitLab Five-Year-Old Vulnerability
- **Description**: Legacy GitLab vulnerability that has remained unpatched in many environments
- **Impact**: Enables unauthorized access to GitLab instances and potentially sensitive source code repositories
- **Status**: Actively exploited in attacks, prompting CISA warning to federal agencies

### SolarWinds Web Help Desk RCE
- **Description**: Critical remote code execution vulnerability in SolarWinds Web Help Desk application
- **Impact**: Allows attackers to execute arbitrary code remotely on affected systems
- **Status**: Actively exploited and added to CISA's Known Exploited Vulnerabilities catalog

## Affected Systems and Products

- **n8n Workflow Automation Platform**: Open-source automation platform with critical command execution vulnerabilities
- **VMware ESXi**: Enterprise virtualization platform targeted by ransomware operators
- **WinRAR**: Popular compression software exploited in espionage campaigns
- **NGINX Servers**: Web servers compromised for traffic hijacking and redirection attacks
- **GitLab Instances**: Source code management platforms with legacy unpatched vulnerabilities
- **SolarWinds Web Help Desk**: IT service management application with RCE vulnerabilities
- **Citrix NetScaler**: Application delivery controllers targeted in reconnaissance campaigns
- **Windows Systems**: Targeted through screensaver-based malware delivery and EDR evasion techniques
- **macOS Environments**: Increasingly targeted by Python-based information stealers

## Attack Vectors and Techniques

- **Malicious Workflow Execution**: Exploitation of n8n platform to execute system commands through crafted workflows
- **Web Traffic Hijacking**: Compromise of NGINX servers and management panels to redirect user traffic through attacker infrastructure
- **Sandbox Escape Exploitation**: Breaking out of VMware ESXi virtualized environments for broader system access
- **Screensaver-Based Malware**: Using Windows .scr files to deploy malware and remote monitoring tools while evading detection
- **EDR Killer Tools**: Abusing legitimate but revoked EnCase kernel drivers to detect and disable 59 different security tools
- **IPFS-Hosted Phishing**: DEAD#VAX campaign using IPFS-hosted VHD files to deploy AsyncRAT malware
- **Residential Proxy Networks**: Large-scale reconnaissance using thousands of residential proxies to discover login panels
- **Cross-Platform InfoStealers**: Python-based malware targeting both Windows and macOS through fake advertisements and installers

## Threat Actor Activities

- **Amaranth Dragon**: China-linked APT group associated with APT41 conducting espionage against government and law enforcement agencies in Southeast Asia using WinRAR exploits
- **DragonForce Ransomware**: Operating cartel model emphasizing cooperation among ransomware groups since 2023 launch
- **APT28 (Russian)**: Rapidly weaponizing Microsoft Office bugs within 3 days of disclosure, using crafted RTF documents for multistage infections
- **DEAD#VAX Campaign**: Sophisticated malware operation using disciplined tradecraft and legitimate system feature abuse to deploy AsyncRAT
- **NGINX Traffic Hijackers**: Threat actors compromising NGINX installations and Baota management panels for traffic redirection schemes
- **GlassWorm Operators**: Self-replicating malware campaign targeting developer ecosystems through poisoned Open VSX software components
- **Ransomware Groups**: Multiple gangs now exploiting VMware ESXi vulnerabilities as part of their attack playbooks targeting network edge devices