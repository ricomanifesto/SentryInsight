# Exploitation Report

Critical exploitation activity is currently impacting multiple enterprise systems, with threat actors actively targeting authentication bypass vulnerabilities and zero-day flaws. The most severe ongoing attacks involve Fortinet FortiGate firewalls where attackers are exploiting a FortiCloud SSO authentication bypass vulnerability even on fully patched systems, allowing unauthorized access and configuration theft. Additionally, SmarterMail email servers are being compromised through an authentication bypass flaw that enables admin account takeovers just two days after patch release. The security landscape is further complicated by the discovery of 76 zero-day vulnerabilities demonstrated at Pwn2Own Automotive 2026 and a critical 11-year-old GNU InetUtils telnetd vulnerability that permits complete authentication bypass and root access.

## Active Exploitation Details

### FortiCloud SSO Authentication Bypass
- **Description**: A critical authentication bypass vulnerability in FortiCloud SSO that affects FortiGate firewalls, allowing attackers to bypass authentication mechanisms
- **Impact**: Unauthorized access to firewall systems, theft of configuration files, creation of rogue accounts, and potential network compromise
- **Status**: Actively exploited in the wild on fully patched devices; Fortinet working to completely resolve the issue

### SmarterMail Authentication Bypass
- **Description**: An authentication bypass vulnerability in SmarterTools SmarterMail email server that allows password reset manipulation
- **Impact**: Complete takeover of administrator accounts, unauthorized access to email systems and sensitive communications
- **Status**: Active exploitation observed within two days of patch release

### GNU InetUtils Telnetd Critical Flaw
- **Description**: A critical vulnerability in GNU InetUtils telnet daemon that went undetected for nearly 11 years
- **Impact**: Complete authentication bypass and root access to affected systems
- **Status**: Recently disclosed, patch available
- **CVE ID**: CVE-2026-24061

### Automotive Zero-Day Vulnerabilities
- **Description**: Collection of 76 zero-day vulnerabilities discovered across automotive systems during security research
- **Impact**: Various impacts including remote code execution, privilege escalation, and system compromise
- **Status**: Demonstrated at Pwn2Own Automotive 2026 competition

## Affected Systems and Products

- **Fortinet FortiGate Firewalls**: All versions affected by FortiCloud SSO bypass, including fully patched systems
- **SmarterTools SmarterMail**: Email server and collaboration platform vulnerable to authentication bypass
- **GNU InetUtils**: Telnet daemon component affected by critical authentication bypass
- **Automotive Systems**: Multiple manufacturers and models with 76 different zero-day vulnerabilities
- **CISA KEV Catalog**: Four additional software vulnerabilities added due to active exploitation evidence

## Attack Vectors and Techniques

- **Authentication Bypass**: Direct circumvention of login mechanisms in FortiGate and SmarterMail systems
- **Configuration Theft**: Automated attacks stealing firewall configuration data from compromised FortiGate devices
- **Account Creation**: Unauthorized creation of rogue administrative accounts on compromised systems
- **Password Reset Manipulation**: Exploitation of password reset functionality in SmarterMail to gain admin access
- **Remote Access**: Use of legitimate tools like LogMeIn RMM for persistent access after initial compromise
- **Adversary-in-the-Middle**: Multi-stage phishing campaigns targeting energy sector organizations
- **Voice-based Social Engineering**: Custom phishing kits designed for vishing attacks against Okta SSO accounts

## Threat Actor Activities

- **Automated Attack Campaigns**: Systematic targeting of Fortinet FortiGate devices with automated exploitation tools
- **Energy Sector Targeting**: Multi-stage AitM phishing and business email compromise campaigns specifically targeting energy organizations
- **Credential-based Attacks**: Dual-vector campaigns leveraging stolen credentials to deploy legitimate RMM software
- **Ransomware Operations**: INC ransomware group operational security failures leading to data recovery for 12 US organizations
- **DPRK-linked Activities**: North Korean actors deploying VS Code tunnels for remote hacking through spear-phishing campaigns
- **Supply Chain Attacks**: Malicious PyPI packages impersonating legitimate libraries to deploy cryptocurrency miners