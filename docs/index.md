# Exploitation Report

Critical exploitation activity is surging across multiple platforms, with threat actors targeting enterprise infrastructure, communication systems, and development tools. The most severe incidents include active exploitation of a Cisco Unified Communications zero-day vulnerability, automated attacks on Fortinet FortiGate firewalls that bypass authentication mechanisms, and sophisticated social engineering campaigns targeting Okta single sign-on accounts. Additionally, researchers discovered 29 zero-day vulnerabilities at Pwn2Own Automotive, while ransomware groups continue deploying advanced techniques including BYOVD attacks and AI-powered malware for click fraud operations.

## Active Exploitation Details

### Cisco Unified Communications Zero-Day
- **Description**: Critical remote code execution vulnerability in Cisco Unified Communications and Webex Calling Dedicated Instance products
- **Impact**: Complete system compromise allowing attackers to execute arbitrary code remotely
- **Status**: Actively exploited as zero-day, patches now available from Cisco
- **CVE ID**: CVE-2026-20045

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools SmarterMail email server allowing password reset manipulation
- **Impact**: Complete admin account takeover and unauthorized access to email systems
- **Status**: Exploited in the wild within two days of patch release, currently under active attack

### GNU InetUtils Telnet Daemon Critical Flaw
- **Description**: Critical vulnerability in GNU InetUtils telnet daemon that remained undetected for nearly 11 years
- **Impact**: Complete bypass of login authentication, direct root access to affected systems
- **Status**: Recently disclosed with patches available
- **CVE ID**: CVE-2026-24061

### Fortinet FortiGate Configuration Theft
- **Description**: Automated attacks exploiting FortiCloud SSO mechanisms to create unauthorized accounts and modify firewall configurations
- **Impact**: Theft of sensitive firewall configuration data and potential network compromise
- **Status**: Ongoing automated campaign targeting potentially fully patched devices

### Pwn2Own Automotive Zero-Days
- **Description**: 29 zero-day vulnerabilities demonstrated across various automotive systems and components
- **Impact**: Complete system compromise of automotive platforms and connected vehicle systems
- **Status**: Vulnerabilities disclosed through security research competition, patches pending

## Affected Systems and Products

- **Cisco Unified Communications**: Multiple CM products and Webex Calling Dedicated Instance affected by critical RCE
- **SmarterTools SmarterMail**: Email server and collaboration platform vulnerable to authentication bypass
- **GNU InetUtils**: Telnet daemon component with 11-year-old critical vulnerability
- **Fortinet FortiGate**: Enterprise firewalls targeted in automated configuration theft attacks
- **Automotive Systems**: 29 different automotive platforms and components with zero-day vulnerabilities
- **Okta SSO**: Single sign-on accounts targeted through custom phishing frameworks
- **Chainlit AI Framework**: Conversational AI applications vulnerable to file disclosure attacks
- **PyPI Repository**: Malicious packages impersonating legitimate libraries like SymPy
- **Chinese Electric Buses**: Connected vehicle systems deployed across Australia and Europe with potential state-controlled kill switches

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in critical enterprise systems
- **Voice-Based Social Engineering**: Custom vishing kits specifically targeting Okta SSO credentials
- **Automated Configuration Theft**: Systematic attacks on firewall systems using legitimate SSO mechanisms
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver techniques used by Osiris ransomware with POORTRY driver
- **AI-Powered Click Fraud**: Android malware using TensorFlow models for automated ad interaction
- **VS Code Tunnel Abuse**: North Korean actors leveraging Microsoft development infrastructure for persistence
- **Supply Chain Attacks**: Malicious packages in software repositories impersonating legitimate tools
- **Contagious Interview Campaigns**: Social engineering attacks using development environments as attack vectors

## Threat Actor Activities

- **DPRK/North Korean Actors**: Deploying VS Code tunnels and contagious interview campaigns for remote access and persistence
- **Osiris Ransomware Group**: New ransomware family using advanced BYOVD techniques targeting Southeast Asian food service operators
- **INC Ransomware Gang**: Operational security failures leading to data recovery for 12 U.S. organizations
- **Unknown Automated Groups**: Systematic campaigns targeting Fortinet infrastructure and SmarterMail installations
- **Android Malware Operators**: Deploying AI-enhanced click fraud trojans using machine learning models
- **Supply Chain Attackers**: Distributing malicious packages through PyPI repository impersonating popular libraries