# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise systems with several actively exploited vulnerabilities posing immediate risks to organizations. The most severe threats include a zero-day vulnerability in Cisco UC systems affecting millions of users, active exploitation of a critical telnetd authentication bypass flaw that has existed undetected for 11 years, and ongoing attacks against FortiGate firewalls through an SSO authentication bypass. Additionally, CISA has confirmed active exploitation of four enterprise software vulnerabilities affecting Versa, Zimbra, and the Vite frontend tool, while threat actors are conducting sophisticated voice phishing campaigns targeting SSO accounts across major platforms.

## Active Exploitation Details

### Cisco UC Zero-Day Vulnerability
- **Description**: Critical zero-day flaw in Cisco Unified Communications systems that enables complete system takeover
- **Impact**: Successful exploitation could lead to complete system compromise affecting millions of users
- **Status**: Actively exploited with mass scanning campaigns underway
- **CVE ID**: CVE-2026-20045

### GNU InetUtils telnetd Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in GNU InetUtils telnet daemon that went unnoticed for 11 years
- **Impact**: Allows attackers to bypass login mechanisms and gain root access to affected systems
- **Status**: Under active coordinated exploitation campaign
- **CVE ID**: CVE-2026-24061

### FortiGate FortiCloud SSO Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in FortiCloud SSO affecting FortiGate firewalls
- **Impact**: Enables unauthorized access to firewall configurations and potential network compromise
- **Status**: Actively exploited against fully patched devices; fix incomplete according to Fortinet

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools' SmarterMail email server and collaboration platform
- **Impact**: Allows attackers to reset admin passwords and hijack administrative accounts
- **Status**: Currently being exploited to compromise admin accounts

### Enterprise Software Vulnerabilities
- **Description**: Four vulnerabilities affecting Versa networks, Zimbra email systems, and Vite frontend development tool
- **Impact**: Various impacts ranging from unauthorized access to system compromise
- **Status**: CISA confirmed active exploitation and added to Known Exploited Vulnerabilities catalog

## Affected Systems and Products

- **Cisco Unified Communications**: Systems potentially affecting millions of users worldwide
- **GNU InetUtils telnetd**: Telnet daemon servers that have been vulnerable for 11 years
- **FortiGate Firewalls**: FortiCloud SSO-enabled devices including fully patched systems
- **SmarterMail**: Email server and collaboration platform administrative interfaces
- **Versa Networks**: Enterprise networking solutions
- **Zimbra**: Email and collaboration platforms
- **Vite**: Frontend development tool and build systems
- **Vehicle Infotainment Systems**: 76 zero-day vulnerabilities discovered in automotive systems
- **EV Charging Infrastructure**: Multiple vulnerabilities in electric vehicle charging systems

## Attack Vectors and Techniques

- **Voice Phishing (Vishing)**: Custom phishing kits targeting Okta, Microsoft, and Google SSO accounts through social engineering calls
- **Mass Scanning**: Automated scanning campaigns targeting Cisco UC systems for zero-day exploitation
- **Authentication Bypass**: Direct exploitation of authentication mechanisms in telnetd and FortiCloud systems
- **Malicious Extensions**: Supply chain attacks through VSCode Marketplace extensions exfiltrating developer data
- **Configuration Manipulation**: Unauthorized changes to FortiGate firewall configurations
- **Remote Monitoring Tools**: Deployment of legitimate RMM software like LogMeIn for persistent access
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver technique using POORTRY driver in ransomware operations

## Threat Actor Activities

- **ShinyHunters**: Extortion gang conducting voice phishing campaigns targeting SSO accounts across major cloud platforms
- **Coordinated Campaigns**: Organized exploitation of the 11-year-old telnetd vulnerability across multiple targets
- **Automotive Researchers**: Security researchers discovered 76 zero-day vulnerabilities during Pwn2Own Automotive 2026, earning over $1 million
- **Osiris Ransomware**: New ransomware family targeting food service operators in Southeast Asia using advanced BYOVD techniques
- **Multi-Stage AitM Operations**: Sophisticated adversary-in-the-middle phishing and business email compromise campaigns targeting energy sector organizations
- **INC Ransomware**: Operational security failures exposed data from 12 U.S. organizations, allowing data recovery
- **Venezuelan ATM Fraud**: Coordinated malware-based ATM jackpotting scheme targeting U.S. banking infrastructure