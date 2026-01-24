# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise systems across various sectors. CISA has confirmed active exploitation of CVE-2024-37079 affecting VMware vCenter Server, along with four additional vulnerabilities in Versa, Zimbra, and Vite frontend tools. A zero-day vulnerability in Cisco UC systems (CVE-2026-20045) is being actively exploited with mass scanning underway. Fortinet FortiGate firewalls are experiencing ongoing attacks through a FortiCloud SSO authentication bypass that remains incompletely patched. Additionally, attackers are exploiting a critical authentication bypass vulnerability in GNU InetUtils telnetd server and targeting SmarterMail systems with authentication bypass flaws for admin account hijacking.

## Active Exploitation Details

### VMware vCenter Server Authentication Bypass
- **Description**: Critical security flaw in Broadcom VMware vCenter Server that was patched in June 2024
- **Impact**: Complete system compromise and unauthorized access to virtualized infrastructure
- **Status**: Actively exploited in the wild, patch available since June 2024
- **CVE ID**: CVE-2024-37079

### Cisco UC Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in Cisco Unified Communications systems
- **Impact**: Complete system takeover affecting potentially millions of systems
- **Status**: Actively exploited with mass scanning campaigns underway
- **CVE ID**: CVE-2026-20045

### Fortinet FortiCloud SSO Authentication Bypass
- **Description**: Authentication bypass vulnerability in FortiCloud Single Sign-On affecting FortiGate firewalls
- **Impact**: Unauthorized access to firewall configurations and potential network compromise
- **Status**: Actively exploited on fully patched systems, incomplete fix confirmed by vendor

### GNU InetUtils Telnetd Authentication Bypass
- **Description**: Critical authentication bypass vulnerability present in GNU InetUtils telnetd server for 11 years
- **Impact**: Root access compromise through coordinated exploitation campaigns
- **Status**: Actively exploited in coordinated attacks, recently disclosed

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools' SmarterMail email server
- **Impact**: Administrative account hijacking and complete email system compromise
- **Status**: Actively exploited for admin password resets

## Affected Systems and Products

- **VMware vCenter Server**: Broadcom VMware vCenter Server installations
- **Cisco Unified Communications**: Cisco UC systems with potential millions affected
- **Fortinet FortiGate Firewalls**: Even fully patched systems remain vulnerable to FortiCloud SSO bypass
- **GNU InetUtils**: Systems running telnetd server component for over 11 years
- **SmarterMail**: SmarterTools email server and collaboration platform
- **Versa Systems**: Enterprise software with confirmed active exploitation
- **Zimbra**: Email and collaboration platform vulnerabilities
- **Vite Frontend Tools**: Development tools with exploited vulnerabilities
- **Visual Studio Code**: Marketplace extensions compromising developer environments
- **Vehicle Infotainment Systems**: 76 zero-day vulnerabilities discovered across automotive platforms
- **EV Charging Systems**: Multiple vulnerabilities in electric vehicle charging infrastructure

## Attack Vectors and Techniques

- **Authentication Bypass**: Direct bypass of authentication mechanisms in multiple enterprise platforms
- **Social Engineering**: Voice phishing (vishing) attacks targeting SSO accounts at Okta, Microsoft, and Google
- **Supply Chain Attacks**: Malicious AI extensions in VSCode Marketplace with 1.5 million collective installations
- **Phishing Campaigns**: Multi-stage campaigns deploying Amnesia RAT and ransomware
- **Configuration Manipulation**: Automated infections modifying FortiGate firewall configurations
- **AI-Generated Malware**: PowerShell malware created using artificial intelligence tools
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver attacks using POORTRY driver
- **Remote Access Tool Deployment**: LogMeIn RMM installation for persistent access
- **Mass Scanning**: Coordinated scanning for vulnerable Cisco UC systems

## Threat Actor Activities

- **Konni Group (Opal Sleet, TA406)**: North Korean actors using AI-generated PowerShell malware to target blockchain developers and engineers
- **Sandworm**: Russian nation-state group deploying DynoWiper malware in attacks against Polish power infrastructure
- **ShinyHunters**: Extortion gang conducting voice phishing attacks against SSO providers
- **Multi-Stage Campaign Actors**: Targeting Russian users with Amnesia RAT and ransomware through phishing
- **Energy Sector Attackers**: Multi-stage adversary-in-the-middle phishing and BEC campaigns targeting energy organizations
- **Osiris Ransomware Group**: New ransomware family targeting food service operators in Southeast Asia using BYOVD techniques
- **Venezuelan ATM Jackpotting Group**: Convicted actors who used malware to empty bank ATMs before deportation
- **Automotive Research Teams**: Security researchers discovering 76 zero-day vulnerabilities in vehicle systems during Pwn2Own contest