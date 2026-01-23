# Exploitation Report

Critical exploitation activities are currently targeting multiple high-value systems, with Fortinet FortiGate firewalls experiencing the most severe impact through automated attacks exploiting FortiCloud SSO authentication bypass vulnerabilities. Attackers are successfully creating rogue administrative accounts and stealing firewall configurations even on fully patched devices, indicating incomplete remediation. Additional active exploitation includes SmarterMail authentication bypass attacks enabling admin account takeover, and Cisco zero-day exploitation in Unified Communications products. The Pwn2Own Automotive 2026 event highlighted significant automotive security gaps with researchers discovering 76 zero-day vulnerabilities across various automotive systems.

## Active Exploitation Details

### FortiCloud SSO Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Fortinet's FortiCloud Single Sign-On system affecting FortiGate firewalls
- **Impact**: Attackers can create unauthorized administrative accounts, steal firewall configuration files, and modify security settings remotely
- **Status**: Actively exploited in automated attacks; Fortinet confirms patches are incomplete and vulnerability not fully addressed

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools SmarterMail email server and collaboration platform
- **Impact**: Complete administrative account takeover through password reset manipulation
- **Status**: Actively exploited within two days of patch release; widespread exploitation reported

### Cisco Unified Communications Zero-Day
- **Description**: Critical zero-day vulnerability in Cisco Unified Communications Manager and Webex Calling Dedicated Instance
- **Impact**: Unauthorized system access and potential service disruption
- **Status**: Actively exploited in the wild; patches released by Cisco
- **CVE ID**: CVE-2026-20045

### GNU InetUtils Telnet Daemon Vulnerability
- **Description**: Critical security flaw in GNU InetUtils telnet daemon that remained undetected for 11 years
- **Impact**: Complete login bypass and root access acquisition on affected systems
- **Status**: Recently disclosed with high severity rating
- **CVE ID**: CVE-2026-24061

## Affected Systems and Products

- **Fortinet FortiGate Firewalls**: All versions affected by FortiCloud SSO integration, including fully patched systems
- **SmarterTools SmarterMail**: Email server and collaboration platforms with authentication systems
- **Cisco Unified Communications Manager**: Multiple UC products and Webex Calling Dedicated Instance
- **GNU InetUtils**: Telnet daemon implementations across Unix-like systems
- **Automotive Systems**: 76 different zero-day vulnerabilities discovered across various automotive manufacturers and components
- **Zendesk Support Systems**: Unsecured instances being exploited for massive spam campaigns

## Attack Vectors and Techniques

- **Automated Configuration Exploitation**: Mass scanning and exploitation of FortiGate devices to create rogue accounts and extract configuration data
- **Authentication Bypass**: Direct circumvention of login mechanisms in SmarterMail and FortiCloud systems
- **Password Reset Manipulation**: Exploitation of authentication flaws to reset administrative passwords
- **Zero-Day Exploitation**: Active use of previously unknown vulnerabilities in Cisco UC products
- **Bring Your Own Vulnerable Driver (BYOVD)**: Osiris ransomware using POORTRY driver for kernel-level access
- **Voice Phishing (Vishing)**: Custom phishing kits targeting Okta SSO accounts through voice-based social engineering
- **Adversary-in-the-Middle (AitM)**: Multi-stage phishing campaigns targeting energy sector organizations
- **Remote Monitoring and Management (RMM) Abuse**: LogMeIn RMM deployment through stolen credentials for persistent access

## Threat Actor Activities

- **Automated Attack Groups**: Conducting mass exploitation of FortiGate devices with systematic configuration theft
- **Ransomware Operators**: Osiris ransomware group targeting Southeast Asian food service companies using advanced BYOVD techniques
- **DPRK-Linked Actors**: Using Visual Studio Code tunnels and Microsoft infrastructure for spear-phishing campaigns to avoid detection
- **Energy Sector Targeting**: Sophisticated multi-stage AitM and BEC campaigns specifically focused on energy companies
- **INC Ransomware Gang**: Operational security failures allowed data recovery for 12 US organizations, indicating ongoing large-scale operations
- **Phishing Kit Developers**: Creating specialized vishing tools targeting Okta SSO authentication systems