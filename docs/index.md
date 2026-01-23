# Exploitation Report

Critical security vulnerabilities are currently under active exploitation across multiple platforms and systems. The most severe activity involves a critical authentication bypass vulnerability in GNU InetUtils telnetd servers that has been present for 11 years and allows attackers to gain root access. Additionally, Fortinet FortiGate firewalls are experiencing widespread automated attacks targeting both a FortiCloud SSO bypass vulnerability and general configuration theft. Other significant exploitation includes SmarterMail authentication bypass attacks, ATM jackpotting schemes using malware, and sophisticated phishing campaigns leveraging legitimate remote management tools. The security landscape is further complicated by 76 zero-day vulnerabilities demonstrated at Pwn2Own Automotive 2026, highlighting the extensive attack surface in automotive systems.

## Active Exploitation Details

### GNU InetUtils telnetd Authentication Bypass
- **Description**: A critical security flaw in the GNU InetUtils telnet daemon (telnetd) that went undetected for nearly 11 years, allowing attackers to completely bypass login authentication mechanisms
- **Impact**: Attackers can gain root access to affected systems without valid credentials, providing complete system control
- **Status**: Currently under coordinated exploitation campaign targeting the recently disclosed vulnerability
- **CVE ID**: CVE-2026-24061

### Fortinet FortiCloud SSO Authentication Bypass
- **Description**: A critical vulnerability in Fortinet's FortiCloud Single Sign-On system that allows attackers to bypass authentication even on fully patched FortiGate firewalls
- **Impact**: Unauthorized access to firewall management interfaces and network infrastructure control
- **Status**: Active exploitation confirmed on fully patched systems; Fortinet working on complete remediation

### SmarterMail Authentication Bypass
- **Description**: An authentication bypass vulnerability in SmarterTools' SmarterMail email server and collaboration platform
- **Impact**: Attackers can reset administrator passwords and hijack admin accounts, gaining full control over email systems
- **Status**: Currently being exploited in active attacks against SmarterMail deployments

### ATM Jackpotting Malware
- **Description**: Sophisticated malware used to compromise bank ATM systems and force cash dispensing
- **Impact**: Direct financial theft through unauthorized cash withdrawal from ATMs
- **Status**: Active deployment by criminal organizations, resulting in convictions and deportations

## Affected Systems and Products

- **GNU InetUtils telnetd**: Telnet daemon servers with 11-year-old vulnerability affecting login authentication
- **Fortinet FortiGate Firewalls**: Network security appliances affected by FortiCloud SSO bypass, including fully patched systems
- **SmarterMail Email Servers**: Email and collaboration platforms vulnerable to administrative account takeover
- **Bank ATM Systems**: Automated teller machines across U.S. banking infrastructure targeted by jackpotting malware
- **Automotive Systems**: 76 zero-day vulnerabilities identified across various automotive platforms and components
- **Okta SSO Platforms**: Single sign-on systems targeted through sophisticated voice-based social engineering attacks

## Attack Vectors and Techniques

- **Direct Authentication Bypass**: Exploitation of telnetd vulnerability to gain immediate root access without credentials
- **Automated Configuration Theft**: Systematic attacks against FortiGate devices to extract firewall configuration files and create rogue administrative accounts
- **Administrative Password Reset**: Abuse of authentication bypass flaws to reset and hijack administrator credentials
- **Voice-based Social Engineering (Vishing)**: Custom phishing kits designed specifically for telephone-based credential theft targeting Okta accounts
- **Adversary-in-the-Middle (AitM) Phishing**: Multi-stage campaigns combining credential theft with legitimate remote management tool deployment
- **Physical ATM Compromise**: Deployment of specialized malware to force cash dispensing from banking systems
- **Bring Your Own Vulnerable Driver (BYOVD)**: Ransomware attacks leveraging legitimate but vulnerable drivers for system compromise

## Threat Actor Activities

- **Venezuelan Criminal Groups**: Convicted ATM jackpotting operations targeting U.S. banking infrastructure with specialized malware deployment
- **DPRK-linked Actors**: Spear-phishing campaigns using Microsoft VS Code tunnels and trusted infrastructure to avoid detection while targeting remote systems
- **Energy Sector Attackers**: Multi-stage campaigns targeting energy companies with adversary-in-the-middle phishing and business email compromise techniques
- **Coordinated Telnet Exploiters**: Organized campaign systematically targeting GNU InetUtils telnetd vulnerability across multiple systems
- **Osiris Ransomware Group**: New ransomware family conducting BYOVD attacks against major food service operators in Southeast Asia
- **INC Ransomware Gang**: Operational security failures exposed data theft operations affecting 12 U.S. organizations, allowing data recovery
- **Fortinet Infrastructure Attackers**: Automated exploitation campaigns targeting FortiGate devices for configuration theft and persistent access