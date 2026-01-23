# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise infrastructure components, with threat actors focusing on network security devices, communication platforms, and email systems. The most concerning developments include active zero-day exploitation of Cisco Unified Communications products enabling remote code execution, automated attacks against Fortinet FortiGate firewalls that bypass authentication to steal configuration data, and immediate exploitation of authentication bypass vulnerabilities in SmarterMail servers within days of patches being released. Additional significant threats include the emergence of new ransomware families using sophisticated BYOVD techniques and North Korean actors leveraging trusted Microsoft infrastructure for persistent access.

## Active Exploitation Details

### Cisco Unified Communications Remote Code Execution Zero-Day
- **Description**: Critical vulnerability in Cisco Unified Communications (CM) products and Webex Calling Dedicated Instance allowing remote code execution
- **Impact**: Attackers can execute arbitrary code remotely on affected systems
- **Status**: Actively exploited as zero-day, patches now available
- **CVE ID**: CVE-2026-20045

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools SmarterMail email server and collaboration tool that allows resetting admin passwords
- **Impact**: Attackers can hijack administrator accounts and gain full control of email systems
- **Status**: Exploited in the wild within two days after patch release, currently does not have a CVE assigned

### GNU InetUtils Telnet Daemon Critical Flaw
- **Description**: Critical security flaw in GNU InetUtils telnet daemon (telnetd) that went unnoticed for nearly 11 years, allowing attackers to bypass login
- **Impact**: Attackers can bypass authentication and gain root access to affected systems
- **Status**: Newly disclosed, rated 9.8/10.0 severity
- **CVE ID**: CVE-2026-24061

### Fortinet FortiGate Configuration Theft
- **Description**: Automated attacks targeting Fortinet FortiGate devices through FortiCloud SSO to create rogue accounts and modify firewall configurations
- **Impact**: Unauthorized firewall configuration changes and theft of sensitive network configuration data
- **Status**: Active automated campaign affecting potentially fully patched devices

## Affected Systems and Products

- **Cisco Unified Communications Manager**: Multiple versions affected by RCE vulnerability
- **Webex Calling Dedicated Instance**: Impacted by the same critical RCE flaw
- **SmarterTools SmarterMail**: Email server and collaboration platform vulnerable to auth bypass
- **GNU InetUtils telnetd**: Telnet daemon with 11-year-old critical vulnerability
- **Fortinet FortiGate**: Network security devices targeted through FortiCloud SSO
- **Chainlit AI Framework**: Open-source conversational AI platform with file read vulnerabilities
- **Android Devices**: Targeted by new AI-powered click-fraud malware using TensorFlow models
- **Visual Studio Code**: Exploited by DPRK actors for remote access tunneling

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Cisco vulnerability exploited before patches were available
- **Automated Configuration Tampering**: Systematic attacks on FortiGate devices to steal firewall configs
- **Authentication Bypass**: Direct bypass of login mechanisms in email systems
- **BYOVD (Bring Your Own Vulnerable Driver)**: Osiris ransomware using POORTRY driver for privilege escalation
- **Social Engineering**: Voice-based phishing (vishing) attacks targeting Okta SSO accounts
- **Supply Chain Attacks**: Malicious PyPI packages impersonating legitimate libraries
- **Trusted Infrastructure Abuse**: VS Code tunnels used by DPRK actors for persistence
- **AI-Enhanced Malware**: Android trojans using machine learning for ad click fraud

## Threat Actor Activities

- **DPRK State Actors**: Deploying VS Code tunnels in spear-phishing campaigns using trusted Microsoft infrastructure to avoid detection
- **Osiris Ransomware Group**: New ransomware family targeting Southeast Asian food service companies using advanced BYOVD techniques with POORTRY driver
- **INC Ransomware Gang**: Operational security failure exposed stolen data from 12 U.S. organizations, allowing data recovery
- **Automated Attack Operators**: Systematic campaigns against FortiGate devices and SmarterMail servers showing rapid exploitation capabilities
- **Chinese Electric Bus Manufacturers**: Vehicles deployed across Australia and Europe contain cybersecurity vulnerabilities and potential state-controlled kill switches
- **Supply Chain Attackers**: Malicious actors targeting PyPI repository with fake packages impersonating SymPy library to deploy XMRig cryptocurrency miners