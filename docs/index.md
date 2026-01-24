# Exploitation Report

Critical exploitation activity continues to surge across enterprise environments, with CISA confirming active exploitation of four vulnerabilities in widely-used enterprise software including Versa, Zimbra, and the Vite frontend tool. A critical zero-day vulnerability (CVE-2026-20045) in Cisco UC systems is under mass scanning with potential to affect millions of users through complete system takeover. Additionally, threat actors are actively exploiting a critical authentication bypass flaw in GNU InetUtils telnetd (CVE-2026-24061) that remained unpatched for 11 years, enabling root access. Fortinet has confirmed ongoing exploitation of a FortiCloud SSO authentication bypass vulnerability that affects even fully patched FortiGate firewalls, while attackers are also targeting SmarterMail servers through authentication bypass flaws to hijack administrative accounts.

## Active Exploitation Details

### Cisco UC Zero-Day Vulnerability
- **Description**: Critical zero-day flaw in Cisco Unified Communications systems enabling complete system compromise
- **Impact**: Mass scanning campaigns underway; successful exploitation leads to complete system takeover affecting potentially millions of users
- **Status**: Currently being exploited in the wild with active mass scanning
- **CVE ID**: CVE-2026-20045

### GNU InetUtils telnetd Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in GNU InetUtils telnet daemon that existed unpatched for 11 years
- **Impact**: Allows attackers to bypass login mechanisms and gain root access to affected systems
- **Status**: Active coordinated exploitation campaigns observed
- **CVE ID**: CVE-2026-24061

### FortiCloud SSO Authentication Bypass
- **Description**: Critical authentication bypass vulnerability affecting FortiCloud SSO on FortiGate firewalls
- **Impact**: Enables unauthorized access to firewall configurations and systems even on fully patched devices
- **Status**: Active exploitation confirmed by Fortinet; patch not fully effective

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools' SmarterMail email server and collaboration platform
- **Impact**: Allows attackers to reset administrator passwords and hijack admin accounts
- **Status**: Currently being exploited to compromise administrative accounts

### Four Enterprise Software Vulnerabilities (CISA KEV)
- **Description**: Four vulnerabilities in enterprise software from Versa, Zimbra, and Vite frontend tool
- **Impact**: Various impacts depending on specific vulnerability and affected system
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to confirmed active exploitation

## Affected Systems and Products

- **Cisco Unified Communications**: Systems vulnerable to zero-day exploitation with millions potentially affected
- **GNU InetUtils telnetd**: Telnet daemon servers running vulnerable versions for the past 11 years
- **Fortinet FortiGate**: Firewalls using FortiCloud SSO, including fully patched systems
- **SmarterTools SmarterMail**: Email servers and collaboration platforms
- **Versa Software**: Enterprise networking solutions
- **Zimbra**: Email and collaboration platforms
- **Vite Frontend Tool**: Development and build tools
- **Vehicle Infotainment Systems**: 76 zero-day vulnerabilities discovered across various automotive systems
- **EV Charging Systems**: Multiple vulnerabilities found in electric vehicle charging infrastructure
- **Microsoft VSCode**: Malicious AI extensions affecting 1.5 million installations

## Attack Vectors and Techniques

- **Mass Scanning Campaigns**: Automated scanning for Cisco UC zero-day vulnerability across internet-facing systems
- **Authentication Bypass**: Direct bypass of login mechanisms in telnetd, FortiCloud SSO, and SmarterMail systems
- **Voice Phishing (Vishing)**: Custom phishing kits targeting SSO accounts at Okta, Microsoft, and Google through voice-based social engineering
- **Supply Chain Attacks**: Malicious VSCode extensions exfiltrating developer data to China-based servers
- **Configuration Manipulation**: Automated infections modifying FortiGate firewall configurations to steal sensitive data
- **BYOVD (Bring Your Own Vulnerable Driver)**: Osiris ransomware using POORTRY driver for system compromise
- **Adversary-in-the-Middle (AitM)**: Multi-stage phishing campaigns targeting energy sector organizations

## Threat Actor Activities

- **ShinyHunters**: Claims responsibility for ongoing vishing attacks targeting SSO accounts across major platforms including Okta, Microsoft, and Google
- **Coordinated Campaign Groups**: Organized exploitation of the GNU InetUtils telnetd vulnerability through systematic targeting
- **Osiris Ransomware Operators**: New ransomware strain targeting food service franchises in Southeast Asia using advanced driver-based attack techniques
- **Automotive Security Researchers**: Demonstrated 76 zero-day exploits at Pwn2Own Automotive 2026, earning over $1 million in rewards
- **INC Ransomware Gang**: Operational security failure exposed data theft operations affecting 12 U.S. organizations
- **Energy Sector Attackers**: Multi-stage campaigns using AitM phishing and BEC attacks specifically targeting energy companies