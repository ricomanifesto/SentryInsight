# Exploitation Report

Critical vulnerability exploitation activity is currently targeting enterprise infrastructure, with several zero-day and recently patched vulnerabilities being actively exploited in the wild. The most severe concerns include a critical Cisco UC zero-day (CVE-2026-20045) under mass scanning attacks, ongoing exploitation of a VMware vCenter Server flaw (CVE-2024-37079) now added to CISA's KEV catalog, and active attacks against a critical GNU InetUtils telnetd vulnerability (CVE-2026-24061) that went undetected for 11 years. Additionally, Fortinet FortiGate firewalls are experiencing ongoing exploitation through a FortiCloud SSO authentication bypass that remains incompletely patched, while CISA has confirmed active exploitation of four enterprise software vulnerabilities affecting Versa, Zimbra, and Vite frontend tools.

## Active Exploitation Details

### Cisco UC Zero-Day Vulnerability
- **Description**: Critical security flaw in Cisco Unified Communications systems currently being mass-scanned by attackers
- **Impact**: Successful exploitation could lead to complete system takeover, potentially affecting millions of systems
- **Status**: Active exploitation with mass scanning campaigns underway
- **CVE ID**: CVE-2026-20045

### VMware vCenter Server Authentication Bypass
- **Description**: Critical security flaw affecting Broadcom VMware vCenter Server that was patched in June 2024
- **Impact**: Authentication bypass allowing unauthorized access to vCenter management infrastructure
- **Status**: Added to CISA KEV catalog due to confirmed active exploitation
- **CVE ID**: CVE-2024-37079

### GNU InetUtils Telnetd Authentication Bypass
- **Description**: Critical vulnerability in GNU InetUtils telnet daemon that remained undetected for 11 years, allowing attackers to bypass login mechanisms
- **Impact**: Complete authentication bypass leading to root access on affected systems
- **Status**: Under active coordinated exploitation campaigns
- **CVE ID**: CVE-2026-24061

### FortiCloud SSO Authentication Bypass
- **Description**: Authentication bypass vulnerability affecting FortiGate firewalls through FortiCloud SSO, with reports of exploitation on fully patched systems
- **Impact**: Unauthorized access to firewall configurations and potential network compromise
- **Status**: Active exploitation confirmed on patched systems; Fortinet working on complete remediation

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools' SmarterMail email server allowing password reset attacks
- **Impact**: Administrative account takeover and email system compromise
- **Status**: Active exploitation targeting admin accounts

## Affected Systems and Products

- **VMware vCenter Server**: Broadcom VMware vCenter Server systems patched in June 2024
- **Cisco Unified Communications**: Cisco UC systems potentially affecting millions of deployments
- **GNU InetUtils**: Systems running GNU InetUtils telnetd daemon (11-year-old vulnerability)
- **FortiGate Firewalls**: Fortinet FortiGate devices with FortiCloud SSO integration, including fully patched systems
- **Enterprise Software**: Versa, Zimbra, and Vite frontend tools confirmed by CISA
- **SmarterMail Servers**: SmarterTools email server and collaboration platforms
- **Vehicle Systems**: 76 zero-day vulnerabilities discovered in automotive infotainment systems and EV chargers at Pwn2Own
- **VSCode Extensions**: Malicious AI extensions in Microsoft Visual Studio Code Marketplace

## Attack Vectors and Techniques

- **Mass Scanning Campaigns**: Large-scale automated scanning targeting Cisco UC systems for CVE-2026-20045
- **Authentication Bypass Attacks**: Direct exploitation of login mechanisms in telnetd, FortiCloud SSO, and SmarterMail
- **Multi-Stage Phishing**: Sophisticated campaigns using Amnesia RAT and ransomware targeting Russian users
- **Voice Phishing (Vishing)**: Custom phishing kits targeting Okta, Microsoft, and Google SSO accounts
- **Supply Chain Attacks**: Malicious VSCode extensions exfiltrating developer data to China-based servers
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver techniques used by Osiris ransomware with POORTRY driver
- **Configuration Tampering**: Automated infections modifying FortiGate firewall configurations to steal config files

## Threat Actor Activities

- **Sandworm Group**: Russian nation-state actors deployed DynoWiper malware in attempted attack on Polish power sector infrastructure
- **ShinyHunters**: Extortion gang claiming responsibility for wave of vishing attacks targeting SSO accounts at major providers
- **Ransomware Operators**: Multiple groups including Osiris ransomware targeting Southeast Asian food service companies
- **Unknown Actors**: Coordinated campaigns exploiting GNU InetUtils telnetd vulnerability and targeting enterprise software vulnerabilities
- **ATM Jackpotting Crews**: Venezuelan nationals convicted of stealing hundreds of thousands from US banks using malware-based ATM attacks