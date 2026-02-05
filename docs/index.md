# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms and systems, with ransomware groups and state-sponsored actors leading sophisticated campaigns. The most concerning activities include ransomware gangs exploiting a VMware ESXi sandbox escape vulnerability, Chinese APT groups leveraging WinRAR flaws in espionage campaigns, and widespread targeting of network infrastructure including NGINX servers, Citrix NetScaler appliances, and various enterprise platforms. Several zero-day and recently patched vulnerabilities are seeing immediate weaponization, with threat actors demonstrating rapid exploit development capabilities and coordination between different criminal groups.

## Active Exploitation Details

### VMware ESXi Sandbox Escape Vulnerability
- **Description**: High-severity sandbox escape vulnerability in VMware ESXi that allows attackers to break out of virtualized environments
- **Impact**: Ransomware gangs can escape virtual machine confines and compromise the underlying hypervisor infrastructure
- **Status**: Previously exploited as zero-day, now confirmed to be actively exploited by ransomware groups in ongoing campaigns

### Five-Year-Old GitLab Vulnerability
- **Description**: Legacy vulnerability in GitLab platform that has remained unpatched in many environments for five years
- **Impact**: Allows attackers to gain unauthorized access to GitLab instances and potentially extract sensitive source code and credentials
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog

### SolarWinds Web Help Desk Remote Code Execution
- **Description**: Critical remote code execution vulnerability in SolarWinds Web Help Desk platform
- **Impact**: Attackers can execute arbitrary commands on vulnerable systems, leading to complete system compromise
- **Status**: Actively exploited in attacks, added to CISA KEV catalog with mandatory patching deadline for federal agencies

### WinRAR Archive Processing Vulnerability
- **Description**: Vulnerability in WinRAR's archive file processing that allows malicious code execution
- **Impact**: Enables state-sponsored actors to deliver malware and establish persistent access to targeted systems
- **Status**: Actively exploited by Amaranth Dragon APT group in espionage campaigns against Southeast Asian governments
- **CVE ID**: CVE-2025-8088

### Microsoft Office RTF Processing Flaw
- **Description**: Vulnerability in Microsoft Office's Rich Text Format document processing
- **Impact**: Allows attackers to execute malicious payloads through specially crafted RTF documents
- **Status**: Weaponized by Russian APT groups within three days of disclosure

### Multiple Critical n8n Workflow Platform Vulnerabilities
- **Description**: Multiple critical vulnerabilities in n8n open-source workflow automation platform
- **Impact**: Allow attackers to escape environment confines and achieve complete host server control
- **Status**: Public exploits available, high risk of active exploitation

## Affected Systems and Products

- **VMware ESXi**: Hypervisor infrastructure vulnerable to sandbox escape attacks
- **GitLab**: Source code management platforms with legacy unpatched vulnerabilities
- **SolarWinds Web Help Desk**: IT service management platforms at critical risk
- **WinRAR**: Archive processing software targeted in espionage campaigns
- **Microsoft Office**: RTF document processing functionality exploited by APT groups
- **NGINX Servers**: Web servers being compromised for traffic redirection campaigns
- **Citrix NetScaler**: Network appliances under coordinated reconnaissance scanning
- **n8n Workflow Platform**: Open-source automation tools with critical security flaws
- **Google Looker**: Business intelligence platform with cross-tenant vulnerabilities

## Attack Vectors and Techniques

- **Traffic Redirection**: Compromising NGINX servers to hijack and reroute user traffic through attacker infrastructure
- **RTF Document Exploits**: Using malicious Rich Text Format files to deliver multistage infection chains
- **Residential Proxy Networks**: Employing thousands of residential proxies for coordinated infrastructure reconnaissance
- **Screensaver File Abuse**: Utilizing Windows .scr files to deploy malware and remote management tools while bypassing security controls
- **VHD File Phishing**: Deploying AsyncRAT malware through IPFS-hosted Virtual Hard Disk files in DEAD#VAX campaign
- **EDR Evasion**: Using legitimate but revoked EnCase kernel drivers to detect and disable 59 different security tools
- **Sandbox Escape**: Breaking out of virtualized environments to compromise underlying hypervisor systems

## Threat Actor Activities

- **Amaranth Dragon (China-linked)**: Conducting espionage campaigns against Southeast Asian government and law enforcement agencies using WinRAR exploits
- **APT28 (Russian)**: Rapidly weaponizing Microsoft Office vulnerabilities within days of disclosure for targeted attacks
- **DragonForce Ransomware**: Operating cartel-style coordination model since 2023, emphasizing cooperation between ransomware groups
- **Unknown NGINX Attackers**: Systematically compromising web servers for traffic hijacking operations
- **GlassWorm Operators**: Returning with self-replicating malware targeting developer ecosystems through poisoned Open VSX components
- **DEAD#VAX Campaign**: Deploying AsyncRAT through sophisticated phishing techniques using IPFS infrastructure