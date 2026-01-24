# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure through multiple attack vectors. The most severe threats include a zero-day vulnerability in Cisco UC systems that could affect millions of users and is undergoing mass scanning campaigns. Additionally, CISA has confirmed active exploitation of four enterprise software vulnerabilities affecting Versa, Zimbra, and Vite frontend tools. Authentication bypass vulnerabilities are particularly concerning, with a critical 11-year-old flaw in GNU InetUtils telnetd enabling root access, and an unpatched FortiCloud SSO bypass affecting fully patched FortiGate firewalls. Coordinated phishing campaigns are targeting SSO accounts across major platforms, while researchers have discovered 76 zero-day vulnerabilities in automotive systems and EV infrastructure.

## Active Exploitation Details

### Cisco UC Zero-Day Vulnerability
- **Description**: Critical zero-day flaw in Cisco Unified Communications systems currently under active exploitation with mass scanning campaigns underway
- **Impact**: Complete system takeover and compromise of potentially millions of affected systems
- **Status**: Actively exploited zero-day vulnerability
- **CVE ID**: CVE-2026-20045

### GNU InetUtils Telnetd Authentication Bypass
- **Description**: Critical authentication bypass vulnerability present in GNU InetUtils telnet daemon for 11 years that allows attackers to bypass login mechanisms
- **Impact**: Direct root access to affected systems without authentication
- **Status**: Active coordinated exploitation campaign targeting this recently disclosed flaw
- **CVE ID**: CVE-2026-24061

### FortiCloud SSO Authentication Bypass
- **Description**: Critical FortiCloud Single Sign-On authentication bypass vulnerability affecting FortiGate firewalls
- **Impact**: Administrative access bypass even on fully patched systems, allowing malicious configuration changes and data theft
- **Status**: Confirmed active exploitation on fully patched firewalls, incomplete fix implementation

### CISA KEV Enterprise Software Vulnerabilities
- **Description**: Four enterprise software vulnerabilities affecting Versa, Zimbra, and Vite frontend tools added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: Various impacts depending on specific vulnerability, affecting enterprise software infrastructure
- **Status**: Confirmed active exploitation prompting CISA advisory

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools' SmarterMail email server and collaboration platform
- **Impact**: Administrative account takeover through password reset mechanism exploitation
- **Status**: Currently being exploited to hijack admin accounts

## Affected Systems and Products

- **Cisco Unified Communications**: Mass scanning targeting millions of potentially affected UC systems
- **GNU InetUtils telnetd**: Systems running telnet daemon services, vulnerability present for 11 years
- **FortiGate Firewalls**: Fully patched FortiGate devices with FortiCloud SSO integration
- **Versa Enterprise Software**: Specific enterprise networking and security solutions
- **Zimbra Collaboration Suite**: Email and collaboration platform deployments
- **Vite Frontend Tools**: Development environment and build tools
- **SmarterMail Servers**: Email server and collaboration platform installations
- **Automotive Infotainment Systems**: Vehicle entertainment and connectivity systems with 76 identified zero-days
- **EV Charging Infrastructure**: Electric vehicle charging stations and management systems
- **VSCode Marketplace Extensions**: Malicious AI extensions with 1.5 million collective installations

## Attack Vectors and Techniques

- **Mass Scanning Campaigns**: Automated scanning for vulnerable Cisco UC systems to identify exploitation targets
- **Authentication Bypass**: Direct bypass of login mechanisms in telnetd and FortiCloud SSO systems
- **Configuration Manipulation**: Malicious changes to firewall configurations for persistent access
- **Voice Phishing (Vishing)**: Custom phishing kits targeting SSO accounts through voice-based social engineering
- **Supply Chain Attacks**: Malicious extensions in legitimate software marketplaces
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver techniques used by Osiris ransomware
- **Multi-Stage AitM Phishing**: Adversary-in-the-middle attacks combined with business email compromise
- **Credential Harvesting**: Theft of SSO credentials through specialized phishing infrastructure

## Threat Actor Activities

- **ShinyHunters Extortion Gang**: Claiming responsibility for wave of voice phishing attacks targeting SSO accounts at Okta, Microsoft, and Google platforms
- **Coordinated Campaign Actors**: Organized exploitation of GNU InetUtils telnetd vulnerability with systematic targeting approach
- **FortiGate Attackers**: Automated infections of FortiGate devices for configuration file theft and persistent access
- **Automotive Research Community**: Security researchers discovered 76 zero-day vulnerabilities during Pwn2Own Automotive 2026 contest
- **Osiris Ransomware Operators**: New ransomware family targeting major food service companies in Southeast Asia using advanced driver exploitation techniques
- **Chinese-Based Data Exfiltration**: Malicious VSCode extensions exfiltrating developer data to China-based command and control servers
- **Energy Sector Targeting**: Multi-stage phishing and BEC campaigns specifically focused on energy industry organizations