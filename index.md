# Exploitation Report

Critical security incidents continue to plague organizations worldwide, with threat actors exploiting multiple high-severity vulnerabilities across various platforms. Ransomware operators are particularly active, exploiting VMware ESXi flaws and leveraging cloud infrastructure for payload delivery. Notable incidents include the weaponization of legitimate forensic tools for EDR evasion, the exploitation of workflow automation platforms for system command execution, and sophisticated traffic hijacking campaigns targeting NGINX servers. Government agencies and educational institutions remain prime targets, with Spain's Ministry of Science and Rome's La Sapienza University suffering significant disruptions from cyberattacks.

## Active Exploitation Details

### VMware ESXi Sandbox Escape Vulnerability
- **Description**: A high-severity vulnerability in VMware ESXi that allows attackers to escape sandbox restrictions and gain unauthorized access to the hypervisor
- **Impact**: Ransomware gangs can compromise virtualized environments and deploy encryption payloads across multiple virtual machines
- **Status**: Currently being exploited by ransomware groups since at least February 2024, now added to CISA's KEV catalog

### n8n Workflow Automation Platform Vulnerability
- **Description**: Critical security flaw in the n8n workflow automation platform that enables arbitrary system command execution through malicious workflows
- **Impact**: Attackers can escape environment confines and gain complete control of the host server
- **Status**: Critical vulnerability with public exploits available
- **CVE ID**: CVE-2026-25049

### GitLab Five-Year-Old Vulnerability
- **Description**: A legacy vulnerability in GitLab that has remained unpatched in many systems for approximately five years
- **Impact**: Enables unauthorized access to GitLab instances and potential code repository compromise
- **Status**: Actively exploited in attacks, prompting CISA warning to government agencies

### EnCase Forensic Driver Vulnerability
- **Description**: Legitimate but revoked kernel driver from EnCase forensic software being weaponized for malicious purposes
- **Impact**: Allows detection and deactivation of 59 different security tools, effectively blinding EDR systems
- **Status**: Being actively used in EDR killer tools despite expired digital certificate

## Affected Systems and Products

- **VMware ESXi**: Hypervisor platforms vulnerable to sandbox escape attacks
- **n8n Platform**: Open-source workflow automation systems running vulnerable versions
- **GitLab Instances**: Legacy installations with unpatched five-year-old vulnerabilities
- **NGINX Servers**: Web servers and management panels including Baota (BT) systems
- **Windows Systems**: Platforms targeted through malicious screensaver files (.scr)
- **ISPsystem VMs**: Virtual machines being abused for ransomware payload delivery
- **Exchange Online**: Microsoft's cloud email service facing upcoming API deprecation
- **Educational Institutions**: Universities and academic networks under active attack

## Attack Vectors and Techniques

- **EDR Evasion**: Weaponization of legitimate signed drivers to bypass endpoint detection systems
- **Traffic Hijacking**: Malicious NGINX configuration modifications to redirect user traffic through attacker infrastructure
- **VM Abuse**: Leveraging legitimate virtual infrastructure providers for ransomware payload hosting and delivery
- **Phishing with VHD Files**: Using IPFS-hosted Virtual Hard Disk files to deploy AsyncRAT malware
- **Screensaver Exploitation**: Utilizing Windows .scr files as execution vectors for malware and RMM tools
- **Workflow Injection**: Exploiting automation platforms to execute arbitrary system commands
- **Social Engineering**: Iranian threat actors using spear-phishing against Middle Eastern targets

## Threat Actor Activities

- **Ransomware Groups**: Multiple gangs exploiting VMware ESXi vulnerabilities and using ISPsystem VMs for payload delivery
- **AISURU/Kimwolf Botnet**: Launched record-setting 31.4 Tbps DDoS attack lasting 35 seconds
- **Infy/Prince of Persia**: Iranian threat group resuming operations with new C2 infrastructure after internet blackout
- **DEAD#VAX Campaign**: Sophisticated malware operation using IPFS-hosted VHD files for AsyncRAT deployment
- **DragonForce**: Ransomware gang adopting organized crime tactics and forming cooperative cartels
- **Iranian Threat Actors**: Conducting espionage campaigns targeting expats, Syrians, and Israelis through credential theft
- **Traffic Hijacking Groups**: Compromising NGINX servers for large-scale web traffic redirection campaigns