# Exploitation Report

Critical vulnerabilities across enterprise infrastructure are experiencing active exploitation, with ransomware operators increasingly targeting virtualization platforms and network edge devices. The most severe incidents involve VMware ESXi sandbox escape vulnerabilities being leveraged by ransomware gangs, while China-linked APT groups exploit WinRAR flaws in espionage campaigns. Additionally, CISA has confirmed active exploitation of a critical SolarWinds Web Help Desk remote code execution vulnerability and a five-year-old GitLab flaw, indicating persistent threats against enterprise management systems. Russian threat actors have also demonstrated rapid weaponization capabilities, exploiting Microsoft Office vulnerabilities within just three days of disclosure.

## Active Exploitation Details

### VMware ESXi Sandbox Escape Vulnerability
- **Description**: High-severity sandbox escape vulnerability in VMware ESXi that was previously exploited as a zero-day
- **Impact**: Allows attackers to escape virtualization constraints and gain control over the hypervisor
- **Status**: Now being actively exploited by ransomware gangs following initial zero-day attacks

### SolarWinds Web Help Desk Remote Code Execution
- **Description**: Critical remote code execution vulnerability in SolarWinds Web Help Desk (WHD)
- **Impact**: Enables attackers to execute arbitrary code remotely on affected systems
- **Status**: Actively exploited in attacks, added to CISA KEV catalog with mandatory patching requirements

### GitLab Vulnerability
- **Description**: Five-year-old vulnerability in GitLab systems
- **Impact**: Allows unauthorized access and potential code repository compromise
- **Status**: Currently being exploited in active attacks despite its age

### WinRAR Vulnerability
- **Description**: Vulnerability in WinRAR compression software exploited by Chinese threat actors
- **Impact**: Used as initial access vector for espionage campaigns
- **Status**: Actively exploited by Amaranth Dragon APT group
- **CVE ID**: CVE-2025-8088

### Microsoft Office RTF Vulnerability
- **Description**: Vulnerability in Microsoft Rich Text Format (RTF) document processing
- **Impact**: Enables multistage infection chains through specially crafted RTF documents
- **Status**: Weaponized by Russian APT28 within three days of disclosure

## Affected Systems and Products

- **VMware ESXi**: Hypervisor platform vulnerable to sandbox escape attacks
- **SolarWinds Web Help Desk**: IT service management platform with critical RCE vulnerability
- **GitLab**: Source code management platform with long-standing security flaw
- **WinRAR**: File compression software targeted in espionage campaigns
- **Microsoft Office**: RTF document processing component exploited by Russian APT groups
- **NGINX Servers**: Web servers compromised for traffic redirection attacks
- **n8n Workflow Platform**: Open-source automation platform with critical vulnerabilities
- **Citrix NetScaler**: Network infrastructure targeted in reconnaissance campaigns
- **Google Looker**: Business intelligence platform with cross-tenant vulnerabilities

## Attack Vectors and Techniques

- **Traffic Redirection**: Compromising NGINX servers to hijack user traffic through attacker infrastructure
- **Phishing with VHD Files**: DEAD#VAX campaign using IPFS-hosted VHD files to deploy AsyncRAT malware
- **EDR Evasion**: Using legitimate but revoked EnCase kernel drivers to disable 59 security tools
- **Screensaver Exploitation**: Leveraging Windows .scr files to bypass executable-level security controls
- **Residential Proxy Networks**: Using thousands of residential proxies for Citrix NetScaler reconnaissance
- **Supply Chain Attacks**: GlassWorm malware targeting Open VSX software components in developer ecosystems
- **RTF Document Weaponization**: Crafted Microsoft RTF documents delivering malicious payloads

## Threat Actor Activities

- **Amaranth Dragon (APT41-linked)**: Chinese espionage group targeting Southeast Asian government and law enforcement agencies using WinRAR exploits
- **APT28 (Russian)**: Rapidly weaponizing Microsoft Office vulnerabilities within three days for document-based attacks
- **DragonForce Ransomware**: Operating cartel model emphasizing cooperation among ransomware gangs since 2023
- **DEAD#VAX Campaign**: Sophisticated malware operation using disciplined tradecraft and legitimate system feature abuse
- **Various Ransomware Groups**: Exploiting VMware ESXi vulnerabilities and building playbooks around network perimeter devices