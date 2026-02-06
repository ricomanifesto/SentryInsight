# Exploitation Report

Current threat activity reveals a concerning landscape of active exploitation targeting critical infrastructure and enterprise systems. Ransomware operators are increasingly sophisticated, with VMware ESXi vulnerabilities being weaponized in attacks and threat actors abusing legitimate infrastructure for payload delivery. Security researchers have identified multiple critical vulnerabilities in widely-used platforms like n8n workflow automation that enable arbitrary system command execution. Additionally, attackers are employing advanced EDR evasion techniques using legitimate but revoked forensic drivers, while leveraging novel attack vectors including NGINX server compromises and IPFS-hosted malware campaigns.

## Active Exploitation Details

### VMware ESXi Sandbox Escape Vulnerability
- **Description**: A high-severity VMware ESXi sandbox escape vulnerability that has been exploited in zero-day attacks since at least February 2024
- **Impact**: Allows attackers to escape virtualization boundaries and compromise ESXi hypervisors, leading to ransomware deployment
- **Status**: Now actively exploited by ransomware gangs, CISA has confirmed ongoing exploitation
- **CVE ID**: CVE-2026-25049

### n8n Workflow Automation Platform Vulnerability
- **Description**: Critical security vulnerability in the n8n workflow automation platform that enables arbitrary system command execution through malicious workflows
- **Impact**: Complete compromise of the host server by escaping environment confines
- **Status**: Public exploits available, critical severity rating assigned

### Five-Year-Old GitLab Vulnerability
- **Description**: A legacy GitLab vulnerability that has remained unpatched in many systems for five years
- **Impact**: Active exploitation enabling unauthorized access to GitLab instances
- **Status**: CISA has ordered government agencies to patch immediately due to active attacks

## Affected Systems and Products

- **VMware ESXi**: Hypervisor platforms vulnerable to sandbox escape leading to ransomware deployment
- **n8n Workflow Automation**: Open-source workflow platform with critical command execution vulnerabilities
- **GitLab**: DevOps platform with five-year-old vulnerability under active exploitation
- **NGINX Servers**: Web servers being compromised for traffic hijacking campaigns
- **Windows Systems**: Targeted by screensaver-based malware delivery and EDR killer tools
- **EnCase Forensic Software**: Legitimate driver being weaponized for EDR evasion
- **ISPsystem VMs**: Virtual machines being abused for ransomware payload hosting

## Attack Vectors and Techniques

- **EDR Killer Tools**: Abusing legitimate but revoked EnCase kernel drivers to detect and disable 59 different security tools
- **BYOVD (Bring Your Own Vulnerable Driver)**: Using signed but expired certificates to load malicious drivers on Windows systems
- **NGINX Configuration Manipulation**: Compromising web servers to redirect user traffic through attacker-controlled infrastructure
- **Screensaver File Abuse**: Leveraging .scr file types to drop malware and remote monitoring tools while evading executable-level controls
- **IPFS-Hosted VHD Files**: Using InterPlanetary File System to host Virtual Hard Disk files containing AsyncRAT malware
- **VM Infrastructure Abuse**: Exploiting legitimate ISPsystem virtual machines for stealthy ransomware payload delivery
- **Workflow Exploitation**: Crafting malicious n8n workflows to execute arbitrary system commands

## Threat Actor Activities

- **Ransomware Gangs**: Actively exploiting VMware ESXi vulnerabilities and using ISPsystem VMs for payload delivery, with DragonForce emphasizing cartel-like cooperation
- **AISURU/Kimwolf Botnet**: Responsible for record-setting 31.4 Tbps DDoS attack lasting 35 seconds
- **DEAD#VAX Campaign**: Deploying AsyncRAT malware through IPFS-hosted VHD phishing files with disciplined tradecraft
- **Infy/Prince of Persia**: Iranian threat group resuming operations with new C2 infrastructure after internet blackouts, targeting expats and regional interests
- **NGINX Traffic Hijackers**: Unknown threat actors compromising web servers to route traffic through malicious backend infrastructure
- **Qilin Ransomware**: Suspected involvement in attacks against Romanian oil pipeline operator Conpet