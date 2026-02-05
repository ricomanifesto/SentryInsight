# Exploitation Report

Current threat intelligence reveals a concerning landscape of active exploitation targeting critical infrastructure and enterprise systems. Ransomware groups are actively exploiting virtualization platforms, with VMware ESXi environments being targeted through sandbox escape vulnerabilities that have been leveraged in zero-day attacks since February 2024. Workflow automation platforms face severe risks with newly disclosed critical vulnerabilities enabling complete system compromise through malicious workflows. Additionally, Chinese state-sponsored groups are conducting widespread espionage campaigns targeting Southeast Asian governments through WinRAR vulnerabilities, while Iranian threat actors maintain persistent surveillance operations against dissidents and regional targets despite domestic infrastructure disruptions.

## Active Exploitation Details

### VMware ESXi Sandbox Escape Vulnerability
- **Description**: A high-severity sandbox escape vulnerability in VMware ESXi hypervisor platforms that allows attackers to break out of virtualized environments
- **Impact**: Complete compromise of virtualization infrastructure, enabling ransomware deployment across multiple virtual machines and potential lateral movement throughout enterprise networks
- **Status**: Currently being exploited by ransomware gangs, with zero-day attacks observed since February 2024

### n8n Workflow Automation Critical Vulnerabilities
- **Description**: Multiple critical security flaws in the n8n open-source workflow automation platform that allow attackers to escape environment confines
- **Impact**: Complete control of host servers through malicious workflow execution, enabling arbitrary system command execution
- **Status**: Public exploits available, patches released but exploitation risk remains high
- **CVE ID**: CVE-2026-25049

### GitLab Legacy Vulnerability
- **Description**: A five-year-old vulnerability in GitLab platforms that continues to be actively exploited despite its age
- **Impact**: Unauthorized access to source code repositories and development infrastructure
- **Status**: Active exploitation confirmed by CISA, requiring immediate patching of government systems

### WinRAR Archive Processing Flaw
- **Description**: A vulnerability in WinRAR file processing that enables code execution through malicious archive files
- **Impact**: Initial access vector for espionage campaigns, allowing deployment of surveillance tools and data exfiltration capabilities
- **Status**: Actively exploited by Chinese APT groups in targeted campaigns
- **CVE ID**: CVE-2025-8088

## Affected Systems and Products

- **VMware ESXi**: Hypervisor platforms across enterprise virtualization environments
- **n8n Workflow Platform**: Open-source automation systems used in enterprise environments
- **GitLab Repositories**: Source code management platforms, particularly in government sectors
- **WinRAR Applications**: Archive processing software in government and law enforcement systems
- **NGINX Web Servers**: Web infrastructure and management panels including Baota (BT) systems
- **Windows Systems**: Enterprise environments vulnerable to screensaver-based malware delivery

## Attack Vectors and Techniques

- **Malicious Workflow Injection**: Exploitation of automation platforms through crafted workflows that execute system commands
- **Archive-Based Payload Delivery**: Using compromised WinRAR files to deliver espionage tools and remote access capabilities
- **Traffic Hijacking**: Compromising NGINX configurations to redirect legitimate user traffic through attacker-controlled infrastructure
- **Screensaver Exploitation**: Leveraging Windows .scr files to deploy malware and remote monitoring tools while evading traditional executable controls
- **BYOVD (Bring Your Own Vulnerable Driver)**: Abusing legitimate but revoked kernel drivers from forensic software to disable EDR systems
- **IPFS-Hosted Phishing**: Using decentralized file systems to host VHD phishing files for AsyncRAT deployment

## Threat Actor Activities

- **Amaranth Dragon**: China-linked APT group conducting espionage campaigns against Southeast Asian government and law enforcement agencies using WinRAR exploits
- **Qilin Ransomware**: Targeting critical infrastructure including Romanian oil pipeline operators through system compromises
- **Infy (Prince of Persia)**: Iranian threat group resuming operations with new C2 infrastructure following internet blackouts, targeting Iranian expats, Syrian dissidents, and Israeli entities
- **DEAD#VAX Campaign**: Sophisticated malware operation deploying AsyncRAT through IPFS-hosted VHD files with disciplined tradecraft
- **DragonForce Ransomware**: Operating a cartel model emphasizing cooperation among ransomware groups since 2023
- **NGINX Traffic Hijacking Group**: Large-scale campaign compromising web servers to redirect traffic through attacker backend infrastructure