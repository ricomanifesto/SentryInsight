# Exploitation Report

Critical exploitation activity continues to target enterprise infrastructure and cloud environments, with threat actors leveraging advanced malware frameworks, exploiting zero-day vulnerabilities, and conducting sophisticated social engineering campaigns. Microsoft's January 2026 Patch Tuesday addressed 114 vulnerabilities including three zero-day flaws, with one being actively exploited in the wild. Notable campaigns include Chinese-linked actors exploiting VMware ESXi zero-days to escape virtual machines, the deployment of advanced Linux malware targeting cloud servers, and state-sponsored groups conducting credential harvesting operations against energy and policy organizations.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Three zero-day vulnerabilities addressed in Microsoft's January 2026 Patch Tuesday, including one actively exploited vulnerability and two publicly disclosed zero-days
- **Impact**: Active exploitation allowing unauthorized access and potential system compromise
- **Status**: Patches available through KB5073724 extended security update for Windows 10 and cumulative updates KB5074109 and KB5073455 for Windows 11

### VMware ESXi Zero-Day Exploits
- **Description**: Chinese-speaking threat actors exploited VMware ESXi zero-day vulnerabilities to escape virtual machines, potentially developed years ago
- **Impact**: Virtual machine escape allowing attackers to gain access to hypervisor level and compromise entire virtualized infrastructure
- **Status**: Active exploitation detected, accessed through compromised SonicWall VPN appliances as initial attack vector

### Gogs Code Execution Vulnerability
- **Description**: High-severity security flaw in Gogs git service enabling remote code execution
- **Impact**: Unauthorized code execution on affected systems
- **Status**: Active exploitation confirmed by CISA, added to Known Exploited Vulnerabilities catalog

### ServiceNow AI Platform Critical Flaw
- **Description**: Critical security vulnerability in ServiceNow's AI Platform allowing unauthenticated user impersonation
- **Impact**: Complete user impersonation capabilities without authentication requirements
- **Status**: Patched by ServiceNow

## Affected Systems and Products

- **Microsoft Windows Systems**: Windows 10 and Windows 11 (versions 23H2, 24H2, 25H2) affected by zero-day vulnerabilities
- **VMware ESXi Infrastructure**: Virtual machine hypervisors targeted for escape attacks
- **SonicWall VPN Appliances**: Used as initial access vector for VMware attacks
- **Linux Cloud Servers**: Targeted by VoidLink malware framework
- **Gogs Git Services**: Code execution vulnerability actively exploited
- **ServiceNow AI Platform**: User impersonation vulnerability in AI services
- **Healthcare Systems**: Central Maine Healthcare and AZ Monica hospital affected by cyberattacks
- **Cryptocurrency Exchanges**: MEXC API keys targeted through malicious Chrome extensions
- **npm Registry**: Eight malicious packages targeting n8n workflow automation platform

## Attack Vectors and Techniques

- **Charity-Themed Social Engineering**: Ukrainian Defense Forces targeted with PluggyApe backdoor malware through charity-themed campaigns
- **Web Skimming Operations**: Long-running campaign since January 2022 targeting payment networks including American Express, Diners Club, and Discover
- **Malicious Browser Extensions**: Chrome extensions stealing MEXC cryptocurrency exchange API keys
- **LinkedIn Phishing**: Fake comment-reply tactics impersonating LinkedIn platform warnings
- **Multi-Stage Malware Deployment**: SHADOW#REACTOR campaign delivering Remcos RAT through evasive attack chains
- **Supply Chain Attacks**: Malicious npm packages masquerading as n8n workflow integrations
- **Credential Brute-Forcing**: GoBruteforcer botnet targeting cryptocurrency project databases
- **Spear-Phishing Campaigns**: Advanced persistent threat groups targeting diplomatic and energy sectors

## Threat Actor Activities

- **Chinese-Linked APT Groups**: Exploiting VMware ESXi zero-days and conducting virtual machine escape attacks through compromised VPN infrastructure
- **Russian APT28**: Running credential-stealing campaigns targeting Turkish energy, nuclear research agencies, and European policy organizations
- **Iranian MuddyWater**: Deploying RustyWater RAT via spear-phishing across Middle East diplomatic, maritime, financial, and telecom sectors
- **Black Axe Criminal Organization**: 34 members arrested in Spain for €5.9M fraud operations and organized cybercrime activities
- **Ukrainian-Focused Threat Actors**: Targeting Defense Forces with charity-themed malware campaigns using PluggyApe backdoors
- **Financially Motivated Cybercriminals**: Operating long-term web skimming campaigns and pig butchering-as-a-service operations