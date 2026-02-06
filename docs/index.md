# Exploitation Report

The current threat landscape reveals significant exploitation activity across multiple attack vectors, with particularly concerning developments in endpoint security evasion, critical infrastructure targeting, and vulnerable workflow automation platforms. Most notably, ransomware operators are actively exploiting VMware ESXi vulnerabilities for hypervisor compromise, while threat actors are weaponizing legitimate forensic tools to disable security controls. The emergence of CVE-2026-25049 in n8n workflow automation platforms presents a critical system command execution risk, and ongoing NGINX server compromises are enabling large-scale traffic hijacking operations.

## Active Exploitation Details

### VMware ESXi Sandbox Escape Vulnerability
- **Description**: A high-severity sandbox escape vulnerability in VMware ESXi hypervisors that has been exploited in zero-day attacks since February 2024
- **Impact**: Allows ransomware gangs to compromise virtualized environments and escape hypervisor security boundaries
- **Status**: Now confirmed by CISA as actively exploited by ransomware operators

### n8n Workflow Automation Platform Vulnerability
- **Description**: Critical security vulnerability in the n8n workflow automation platform allowing arbitrary system command execution through malicious workflows
- **Impact**: Complete host server takeover and escape from environment confines
- **Status**: Public exploits available, actively being disclosed
- **CVE ID**: CVE-2026-25049

### GitLab Five-Year-Old Vulnerability
- **Description**: A five-year-old GitLab vulnerability that remains unpatched in many systems
- **Impact**: Active exploitation enabling unauthorized access to development environments
- **Status**: CISA has ordered government agencies to patch due to active exploitation

### EnCase Driver Exploitation
- **Description**: Legitimate but revoked EnCase forensic kernel driver being weaponized by attackers
- **Impact**: Detection and deactivation of 59 different security tools including EDR solutions
- **Status**: Active use in EDR killer tools despite expired digital certificates

## Affected Systems and Products

- **VMware ESXi**: Hypervisor environments vulnerable to sandbox escape and ransomware deployment
- **n8n Platform**: Open-source workflow automation systems allowing command execution
- **GitLab**: Development platforms with five-year-old unpatched vulnerabilities
- **NGINX Servers**: Web servers and management panels including Baota (BT) systems
- **EnCase Software**: Forensic tool drivers being abused for security evasion
- **ISPsystem VMs**: Virtual machine infrastructure used for malicious payload delivery
- **Educational Institutions**: La Sapienza University and other academic networks under attack
- **Critical Infrastructure**: Romanian oil pipeline operator Conpet and Spain's Ministry of Science systems

## Attack Vectors and Techniques

- **EDR Evasion**: Using signed but revoked kernel drivers to bypass endpoint detection and response systems
- **Traffic Hijacking**: Compromising NGINX configurations to redirect user traffic through attacker infrastructure
- **Ransomware-as-a-Service**: ISPsystem VM abuse for stealthy payload delivery at scale
- **Workflow Exploitation**: Malicious n8n workflows enabling system command execution
- **Hypervisor Escape**: VMware ESXi sandbox vulnerabilities allowing ransomware deployment
- **Screensaver Malware**: Windows .scr files used to drop malware and remote management tools
- **VHD File Phishing**: IPFS-hosted virtual hard disk files delivering AsyncRAT malware
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver techniques for security bypass

## Threat Actor Activities

- **Ransomware Operators**: Actively exploiting VMware ESXi vulnerabilities and using ISPsystem VMs for payload delivery
- **DragonForce**: Establishing cartel-like cooperation structures among ransomware gangs
- **AISURU/Kimwolf Botnet**: Launching record-setting 31.4 Tbps DDoS attacks
- **Infy/Prince of Persia**: Iranian threat group resuming operations with new C2 infrastructure after internet blackout
- **DEAD#VAX Campaign**: Deploying AsyncRAT malware through sophisticated IPFS-hosted phishing campaigns
- **Iranian APT Groups**: Conducting credential theft operations against expatriates, Syrians, and Israelis through spear-phishing and social engineering
- **NGINX Traffic Hijackers**: Large-scale web traffic redirection through compromised server configurations