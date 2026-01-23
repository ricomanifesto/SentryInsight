# Exploitation Report

Several critical vulnerabilities are experiencing active exploitation across enterprise infrastructure, with threat actors targeting enterprise communication systems, firewall devices, and email servers. The most severe activity involves a Cisco Unified Communications zero-day vulnerability (CVE-2026-20045) that enables remote code execution and has been actively exploited in attacks. Additional exploitation includes automated attacks against Fortinet FortiGate devices through FortiCloud SSO abuse, authentication bypass vulnerabilities in SmarterMail email servers, and a critical GNU InetUtils telnet daemon flaw (CVE-2026-24061) that allows attackers to bypass login and gain root access. Threat actors are also leveraging trusted Microsoft infrastructure through VS Code tunnels in spear-phishing campaigns and exploiting 29 zero-day vulnerabilities during the Pwn2Own Automotive competition.

## Active Exploitation Details

### Cisco Unified Communications Zero-Day
- **Description**: Critical remote code execution vulnerability in Cisco Unified Communications Manager (CM) and Webex Calling Dedicated Instance products
- **Impact**: Allows attackers to execute arbitrary code remotely on vulnerable systems
- **Status**: Actively exploited as zero-day; patches now available from Cisco
- **CVE ID**: CVE-2026-20045

### GNU InetUtils Telnet Daemon Vulnerability
- **Description**: Critical security flaw in GNU InetUtils telnet daemon that went undetected for nearly 11 years, allowing attackers to bypass authentication
- **Impact**: Complete system compromise with root access privileges
- **Status**: Recently disclosed with patches available; rated 9.8 out of 10.0 severity
- **CVE ID**: CVE-2026-24061

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools' SmarterMail email server allowing unauthorized access to admin accounts
- **Impact**: Complete compromise of email infrastructure with ability to reset admin passwords
- **Status**: Actively exploited within two days of patch release

### FortiGate Automated Configuration Attacks
- **Description**: Automated attacks targeting Fortinet FortiGate devices through FortiCloud SSO functionality to make unauthorized configuration changes
- **Impact**: Theft of firewall configuration files, creation of rogue accounts, and potential network compromise
- **Status**: Ongoing automated campaign targeting potentially fully patched devices

### Pwn2Own Automotive Zero-Days
- **Description**: Multiple zero-day vulnerabilities targeting automotive systems and related technologies
- **Impact**: Complete system compromise in controlled demonstration environment
- **Status**: 29 zero-day vulnerabilities successfully exploited on second day of competition, earning researchers $439,250

## Affected Systems and Products

- **Cisco Unified Communications Manager**: Multiple versions affected by RCE zero-day
- **Cisco Webex Calling Dedicated Instance**: Vulnerable to same RCE exploit
- **Fortinet FortiGate Devices**: Targeted in automated configuration theft attacks
- **SmarterTools SmarterMail**: Email server vulnerable to authentication bypass
- **GNU InetUtils Telnet Daemon**: Legacy systems running vulnerable telnet services
- **Automotive Systems**: Various automotive technologies demonstrated at Pwn2Own
- **Android Devices**: Targeted by AI-powered click-fraud trojans
- **PyPI Repository**: Hosting malicious packages impersonating legitimate libraries

## Attack Vectors and Techniques

- **FortiCloud SSO Abuse**: Leveraging legitimate SSO functionality to gain unauthorized access to FortiGate devices
- **VS Code Tunnel Exploitation**: North Korean actors using Microsoft VS Code tunnels for remote access and command execution
- **Vishing with Custom Phishing Kits**: Voice-based social engineering targeting Okta SSO accounts
- **Bring Your Own Vulnerable Driver (BYOVD)**: Osiris ransomware using POORTRY driver for privilege escalation
- **Supply Chain Attacks**: Malicious PyPI packages impersonating popular libraries like SymPy
- **AI-Powered Click Fraud**: Android malware using TensorFlow models for automated ad interaction
- **Contagious Interview Campaigns**: Social engineering through malicious coding repositories

## Threat Actor Activities

- **North Korean APT Groups**: Conducting spear-phishing campaigns using VS Code tunnels and "Contagious Interview" techniques targeting software developers
- **Osiris Ransomware Group**: Deploying new ransomware strain with BYOVD techniques against Southeast Asian food service companies
- **INC Ransomware Gang**: Suffered operational security failure allowing data recovery for 12 US organizations
- **Automated Attack Clusters**: Coordinated campaigns targeting FortiGate devices globally for configuration theft
- **AI-Powered Mobile Threats**: Sophisticated Android malware groups leveraging machine learning for fraud operations