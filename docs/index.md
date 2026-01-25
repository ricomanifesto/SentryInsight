# Exploitation Report

Critical exploitation activity is currently impacting enterprise infrastructure with multiple zero-day vulnerabilities and authentication bypass flaws being actively exploited in the wild. CISA has added several vulnerabilities to its Known Exploited Vulnerabilities catalog, including CVE-2024-37079 affecting VMware vCenter Server and CVE-2026-20045 targeting Cisco UC systems. Nation-state actors including Sandworm and Konni are conducting sophisticated campaigns, while threat groups like ShinyHunters are targeting SSO accounts across major platforms. Additionally, authentication bypass vulnerabilities in Fortinet FortiCloud and SmarterMail systems are being exploited even on fully patched systems, indicating incomplete remediation efforts.

## Active Exploitation Details

### VMware vCenter Server Authentication Bypass
- **Description**: Critical security flaw affecting Broadcom VMware vCenter Server that was patched in June 2024 but continues to be exploited
- **Impact**: Successful exploitation could lead to unauthorized access to vCenter management interfaces
- **Status**: Actively exploited in the wild, patch available since June 2024
- **CVE ID**: CVE-2024-37079

### Cisco UC Zero-Day Vulnerability
- **Description**: Critical zero-day flaw in Cisco UC systems currently under mass scanning campaigns
- **Impact**: Complete system takeover possible upon successful exploitation
- **Status**: Actively exploited, mass scanning underway
- **CVE ID**: CVE-2026-20045

### Fortinet FortiCloud SSO Authentication Bypass
- **Description**: Authentication bypass vulnerability in FortiCloud SSO affecting FortiGate firewalls, with reports of exploitation on fully patched systems
- **Impact**: Unauthorized access to firewall configurations and administrative functions
- **Status**: Actively exploited, incomplete patch remediation confirmed by vendor

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools' SmarterMail email server allowing password reset for admin accounts
- **Impact**: Complete compromise of email server administration and user data access
- **Status**: Actively exploited for admin account hijacking

### GNU InetUtils Telnetd Authentication Bypass
- **Description**: Critical authentication bypass vulnerability present in GNU InetUtils telnetd server for 11 years, recently disclosed
- **Impact**: Root-level system access through authentication bypass
- **Status**: Coordinated exploitation campaign observed targeting this vulnerability

## Affected Systems and Products

- **VMware vCenter Server**: Broadcom VMware vCenter Server installations
- **Cisco UC Systems**: Cisco Unified Communications infrastructure potentially affecting millions of users
- **Fortinet FortiGate**: FortiGate firewalls using FortiCloud SSO authentication
- **SmarterMail**: SmarterTools email server and collaboration platforms
- **GNU InetUtils**: Systems running GNU InetUtils telnetd server
- **Versa Networks**: Enterprise software solutions
- **Zimbra**: Collaboration and email platforms
- **Vite**: Frontend development tool
- **VSCode Marketplace**: Two malicious AI extensions affecting 1.5 million installations
- **Automotive Systems**: 76 zero-day vulnerabilities discovered in vehicle infotainment systems and EV chargers

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of authentication mechanisms in enterprise software to gain unauthorized access
- **Mass Scanning**: Automated scanning campaigns targeting newly disclosed vulnerabilities
- **Social Engineering**: Voice phishing (vishing) attacks targeting SSO accounts
- **AI-Generated Malware**: Use of artificial intelligence to create PowerShell-based malware for blockchain sector targeting
- **Supply Chain Attacks**: Malicious extensions in legitimate software marketplaces
- **Multi-Stage Phishing**: Complex phishing campaigns combining multiple attack vectors
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver attacks using POORTRY driver
- **Remote Access Trojan Deployment**: Installation of Amnesia RAT through phishing campaigns

## Threat Actor Activities

- **Sandworm**: Russian nation-state group conducted "largest cyber attack" targeting Poland's power system using new DynoWiper malware in December 2025
- **Konni (Opal Sleet, TA406)**: North Korean group using AI-generated PowerShell malware to target blockchain developers and engineers
- **ShinyHunters**: Extortion gang claiming responsibility for wave of vishing attacks targeting Okta, Microsoft, and Google SSO accounts
- **Energy Sector Attackers**: Multi-stage adversary-in-the-middle phishing and business email compromise campaigns targeting energy organizations
- **Automotive Researchers**: Security researchers exploited 76 zero-day vulnerabilities during Pwn2Own Automotive 2026, earning over $1 million in rewards
- **Ransomware Operators**: Deployment of Osiris ransomware targeting Southeast Asian food service companies using BYOVD techniques