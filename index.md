# Exploitation Report

The cybersecurity landscape is experiencing intense exploitation activity across multiple critical vulnerabilities and attack vectors. Most concerning is the active exploitation of CVE-2026-20045, a critical zero-day vulnerability in Cisco Unified Communications and Webex products that allows remote code execution. Additionally, automated attacks are targeting Fortinet FortiGate devices to steal firewall configurations, while SmarterMail authentication bypass vulnerabilities are being exploited just two days after patch release. The security community is also witnessing significant zero-day activity at Pwn2Own Automotive 2026, where researchers exploited 29 zero-day vulnerabilities in automotive systems. A critical GNU InetUtils telnet daemon flaw (CVE-2026-24061) has been disclosed after remaining unnoticed for nearly 11 years, presenting severe authentication bypass risks.

## Active Exploitation Details

### Cisco Unified Communications Zero-Day
- **Description**: Critical remote code execution vulnerability in Cisco Unified Communications Manager (CM) products and Webex Calling Dedicated Instance
- **Impact**: Attackers can execute arbitrary code remotely on affected systems
- **Status**: Actively exploited as zero-day, patches have been released by Cisco
- **CVE ID**: CVE-2026-20045

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools SmarterMail email server and collaboration tool that allows attackers to reset administrator passwords
- **Impact**: Complete administrative account takeover, allowing full control of email systems
- **Status**: Actively exploited in the wild just two days after patch release
- **Status**: Patch available but exploitation continues

### GNU InetUtils Telnet Daemon Critical Flaw
- **Description**: Critical security vulnerability in GNU InetUtils telnet daemon (telnetd) that went unnoticed for nearly 11 years, allowing login bypass
- **Impact**: Attackers can bypass authentication and gain root access to affected systems
- **Status**: Recently disclosed, rated 9.8/10.0 severity
- **CVE ID**: CVE-2026-24061

### Fortinet FortiGate Configuration Theft
- **Description**: Automated attacks targeting Fortinet FortiGate devices through FortiCloud SSO exploitation
- **Impact**: Creation of rogue accounts and theft of sensitive firewall configuration data
- **Status**: Ongoing automated attacks against potentially fully patched devices

### Pwn2Own Automotive Zero-Days
- **Description**: Multiple zero-day vulnerabilities discovered and exploited in automotive systems during security research competition
- **Impact**: Various security bypasses in automotive platforms and components
- **Status**: 29 zero-day vulnerabilities exploited on single day of competition, earning researchers $439,250

## Affected Systems and Products

- **Cisco Unified Communications Manager**: All versions affected by CVE-2026-20045
- **Webex Calling Dedicated Instance**: Remote code execution vulnerability
- **SmarterTools SmarterMail**: Email server and collaboration platform
- **GNU InetUtils telnetd**: Telnet daemon service across multiple Unix-like systems
- **Fortinet FortiGate**: Firewall devices targeted via FortiCloud SSO
- **Automotive Systems**: Multiple manufacturers' systems targeted at Pwn2Own event
- **Chinese Electric Buses**: Deployed across Australia and Europe with embedded vulnerabilities

## Attack Vectors and Techniques

- **Remote Code Execution**: Exploitation of CVE-2026-20045 for arbitrary code execution
- **Authentication Bypass**: SmarterMail and telnet daemon vulnerabilities allowing login circumvention
- **Automated Configuration Theft**: Systematic targeting of FortiGate devices for configuration data extraction
- **FortiCloud SSO Abuse**: Leveraging single sign-on mechanisms for unauthorized access
- **Voice-based Social Engineering (Vishing)**: Custom phishing kits targeting Okta SSO accounts
- **VS Code Tunnel Abuse**: DPRK actors using Microsoft VS Code tunnels for remote access
- **Bring Your Own Vulnerable Driver (BYOVD)**: Osiris ransomware using POORTRY driver for privilege escalation

## Threat Actor Activities

- **DPRK State Actors**: Conducting spear-phishing campaigns using VS Code tunnels and trusted Microsoft infrastructure to avoid detection, including "Contagious Interview" attacks
- **INC Ransomware Group**: Operational security failure allowed data recovery for 12 U.S. organizations
- **Osiris Ransomware Operators**: New ransomware family targeting major food service franchisee in Southeast Asia using BYOVD techniques
- **Automated Attack Clusters**: Systematic targeting of FortiGate devices for configuration theft
- **Vishing Attackers**: Specialized phishing kit development for voice-based Okta account compromises
- **Supply Chain Attackers**: Malicious PyPI packages impersonating SymPy library to deploy XMRig cryptocurrency miners