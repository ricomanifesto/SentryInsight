# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise systems, with several zero-day vulnerabilities and authentication bypass flaws being actively exploited in the wild. The most concerning threats include ongoing attacks against Fortinet FortiGate firewalls through a FortiCloud SSO bypass vulnerability that remains incompletely patched, active exploitation of authentication bypass flaws in SmarterMail email servers, and a newly discovered critical GNU InetUtils telnet daemon vulnerability. Additionally, Cisco has confirmed active exploitation of a zero-day vulnerability (CVE-2026-20045) affecting Unified Communications products and Webex systems, while the Pwn2Own Automotive 2026 event has revealed 76 zero-day vulnerabilities across automotive systems.

## Active Exploitation Details

### FortiCloud SSO Authentication Bypass
- **Description**: A critical authentication bypass vulnerability in Fortinet's FortiCloud Single Sign-On service that allows unauthorized access to FortiGate firewalls
- **Impact**: Attackers can gain administrative access to firewall systems, create rogue accounts, steal configuration files, and modify security policies
- **Status**: Actively exploited in the wild on fully patched systems; Fortinet confirms the vulnerability is not fully addressed despite available patches

### SmarterMail Authentication Bypass
- **Description**: An authentication bypass vulnerability in SmarterTools' SmarterMail email server and collaboration tool
- **Impact**: Allows attackers to reset administrator passwords and hijack admin accounts, providing full control over email systems
- **Status**: Actively exploited in the wild starting just two days after patch release

### Cisco Unified CM and Webex Zero-Day
- **Description**: A critical security vulnerability affecting multiple Unified Communications products and Webex Calling Dedicated Instance
- **Impact**: Enables unauthorized access and potential system compromise of enterprise communication platforms
- **Status**: Actively exploited in the wild; patches have been released
- **CVE ID**: CVE-2026-20045

### GNU InetUtils Telnet Daemon Critical Flaw
- **Description**: A critical security flaw in the GNU InetUtils telnet daemon that went undetected for nearly 11 years
- **Impact**: Allows attackers to bypass login authentication and gain root access to affected systems
- **Status**: Recently disclosed with patches available
- **CVE ID**: CVE-2026-24061

### Automotive Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities across various automotive systems and components discovered during Pwn2Own Automotive 2026
- **Impact**: Range of security compromises across automotive platforms including infotainment systems, ECUs, and connected vehicle components
- **Status**: 76 total zero-days discovered with researchers earning $1,047,000 in bounties

## Affected Systems and Products

- **Fortinet FortiGate Firewalls**: All versions affected by FortiCloud SSO bypass, including fully patched systems
- **SmarterTools SmarterMail**: Email server and collaboration platforms vulnerable to authentication bypass
- **Cisco Unified Communications**: Multiple UC products and Webex Calling Dedicated Instance affected by zero-day
- **GNU InetUtils**: Telnet daemon (telnetd) affected by 11-year-old critical vulnerability
- **Automotive Systems**: Wide range of automotive platforms, infotainment systems, and electronic control units
- **LogMeIn RMM**: Being weaponized by attackers for persistent access via phishing campaigns
- **Okta SSO**: Targeted in sophisticated vishing-based data theft attacks
- **Zendesk Support Systems**: Hijacked globally for massive spam campaigns

## Attack Vectors and Techniques

- **Automated Configuration Changes**: Mass automated attacks against FortiGate devices to alter firewall configurations and steal sensitive data
- **Authentication Bypass Exploitation**: Direct exploitation of SSO and authentication flaws to gain administrative access
- **Phishing with RMM Deployment**: Dual-vector campaigns using stolen credentials to install legitimate remote management tools for persistence
- **Vishing Attacks**: Custom phishing kits designed specifically for voice-based social engineering targeting SSO accounts
- **Zero-Day Chain Exploitation**: Sequential exploitation of multiple zero-day vulnerabilities in automotive systems
- **BYOVD (Bring Your Own Vulnerable Driver)**: Osiris ransomware using POORTRY driver in attacks
- **Adversary-in-the-Middle (AitM)**: Multi-stage phishing and business email compromise campaigns targeting energy sector
- **Spam Infrastructure Abuse**: Hijacking of legitimate support ticket systems for global spam distribution

## Threat Actor Activities

- **DPRK-Linked Actors**: Deploying Visual Studio Code tunnels for remote access in spear-phishing campaigns using trusted Microsoft infrastructure
- **Osiris Ransomware Group**: New ransomware family targeting major food service operators in Southeast Asia using vulnerable driver techniques
- **INC Ransomware Gang**: Operational security failures exposed attack infrastructure, allowing data recovery for 12 U.S. organizations
- **Energy Sector Targeting**: Sophisticated multi-stage campaigns specifically targeting energy organizations with AitM phishing and BEC attacks
- **Automated Attack Infrastructure**: Large-scale automated campaigns targeting FortiGate devices globally for configuration theft and manipulation
- **Supply Chain Attackers**: Malicious PyPI packages impersonating legitimate libraries to deploy cryptocurrency miners on Linux systems