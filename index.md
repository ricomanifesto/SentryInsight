# Exploitation Report

Current cybersecurity intelligence reveals a concerning landscape of active exploitation targeting critical infrastructure and enterprise systems. Ransomware operators are leveraging sophisticated techniques including ISPsystem virtual machines for payload delivery and exploiting newly disclosed vulnerabilities in widely-used platforms. The most significant threats include active exploitation of VMware ESXi sandbox escape vulnerabilities being used in ransomware campaigns, critical flaws in the n8n workflow automation platform enabling system command execution, and a five-year-old GitLab vulnerability that continues to be exploited. Chinese-linked threat actors are actively exploiting WinRAR vulnerabilities in targeted espionage campaigns against government entities, while massive DDoS attacks reaching record-breaking 31.4 Tbps are being launched by sophisticated botnets.

## Active Exploitation Details

### VMware ESXi Sandbox Escape Vulnerability
- **Description**: A high-severity sandbox escape vulnerability in VMware ESXi hypervisors that has been exploited since February 2024
- **Impact**: Enables ransomware operators to escape virtualized environments and compromise host systems
- **Status**: Now confirmed as actively exploited by ransomware gangs in attacks

### n8n Workflow Automation Platform Vulnerabilities
- **Description**: Multiple critical security flaws in the n8n open-source workflow automation platform allowing environment escape
- **Impact**: Successful exploitation results in execution of arbitrary system commands and complete control of the host server
- **Status**: Critical vulnerabilities with public exploits available
- **CVE ID**: CVE-2026-25049

### GitLab Authentication Bypass Vulnerability
- **Description**: A five-year-old vulnerability in GitLab systems enabling authentication bypass
- **Impact**: Unauthorized access to GitLab repositories and associated development infrastructure
- **Status**: Actively exploited in attacks according to CISA warnings

### WinRAR Vulnerability
- **Description**: A security flaw in WinRAR archive software being exploited in targeted campaigns
- **Impact**: Enables threat actors to execute malicious code through crafted archive files
- **Status**: Actively exploited by Chinese-linked APT groups in espionage operations
- **CVE ID**: CVE-2025-8088

## Affected Systems and Products

- **VMware ESXi**: Hypervisor platforms vulnerable to sandbox escape attacks
- **n8n Platform**: Open-source workflow automation systems with critical command execution flaws
- **GitLab**: Development platforms with authentication bypass vulnerabilities
- **WinRAR Software**: Archive utility software vulnerable to exploitation in espionage campaigns
- **NGINX Servers**: Web servers being compromised for traffic hijacking campaigns
- **ISPsystem VMs**: Virtual machines being abused for ransomware payload delivery
- **Educational Institutions**: University systems including La Sapienza targeted by cyberattacks
- **Energy Infrastructure**: Romanian oil pipeline operator Conpet systems compromised
- **Financial Services**: Betterment platform with 1.4 million accounts exposed
- **Newsletter Platforms**: Substack user data compromised in breach incidents

## Attack Vectors and Techniques

- **Virtual Machine Abuse**: Ransomware operators leveraging ISPsystem VMs for stealthy payload delivery at scale
- **Traffic Hijacking**: NGINX server compromises enabling redirection of user traffic through attacker infrastructure
- **DDoS Amplification**: AISURU/Kimwolf botnet launching record-setting 31.4 Tbps distributed denial-of-service attacks
- **EDR Evasion**: Use of signed kernel drivers from forensic software to disable 59 different security tools
- **Phishing Campaigns**: DEAD#VAX malware deployment through IPFS-hosted VHD files containing AsyncRAT
- **Screensaver Exploitation**: Windows .scr files being weaponized to deploy malware and remote management tools
- **Zendesk Abuse**: Spam campaigns exploiting unsecured Zendesk support systems for email flooding attacks

## Threat Actor Activities

- **Chinese APT Groups**: Amaranth Dragon threat actor linked to APT41 conducting espionage campaigns against Southeast Asian government and law enforcement agencies using WinRAR exploits
- **Iranian Threat Actors**: Infy (Prince of Persia) group resuming operations with new C2 infrastructure following Iran internet blackout, targeting expats, Syrians, and Israelis through credential theft
- **Ransomware Operators**: Multiple gangs including Qilin targeting critical infrastructure and educational institutions with sophisticated delivery mechanisms
- **DragonForce Ransomware**: Implementing organized crime-style coordination strategies among ransomware groups for enhanced cooperation
- **AISURU/Kimwolf Botnet**: Launching massive DDoS attacks with unprecedented scale and brief duration for maximum impact