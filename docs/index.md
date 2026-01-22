# Exploitation Report

Critical vulnerabilities are under active exploitation across multiple enterprise platforms, with threat actors rapidly capitalizing on newly disclosed flaws. The most concerning activity involves a zero-day vulnerability CVE-2026-20045 affecting Cisco Unified Communications and Webex systems that is being actively exploited, alongside CVE-2026-24061, a critical GNU InetUtils telnetd flaw that enables attackers to bypass login mechanisms and gain root access. Additionally, Fortinet FortiGate devices are experiencing widespread automated attacks exploiting FortiCloud SSO mechanisms, while threat actors are leveraging patch bypass techniques for previously fixed vulnerabilities like CVE-2025-59718. North Korean threat groups continue their sophisticated "Contagious Interview" campaigns, now utilizing Microsoft VS Code tunnels to establish persistent access, while malicious actors are exploiting 29 zero-day vulnerabilities in automotive systems during security competitions.

## Active Exploitation Details

### Cisco Unified Communications Zero-Day Vulnerability
- **Description**: Critical remote code execution vulnerability affecting Cisco Unified Communications (CM) products and Webex Calling Dedicated Instance
- **Impact**: Attackers can execute arbitrary code remotely on affected systems
- **Status**: Actively exploited as zero-day, patches now available
- **CVE ID**: CVE-2026-20045

### GNU InetUtils Telnetd Authentication Bypass
- **Description**: Critical vulnerability in GNU InetUtils telnet daemon that went unnoticed for nearly 11 years, allowing complete authentication bypass
- **Impact**: Attackers can bypass login mechanisms and gain root access to affected systems
- **Status**: Recently disclosed vulnerability with patches available
- **CVE ID**: CVE-2026-24061

### SmarterMail Authentication Bypass
- **Description**: Security flaw in SmarterTools SmarterMail email software allowing authentication bypass
- **Impact**: Unauthorized access to email systems and potential data compromise
- **Status**: Under active exploitation two days after patch release

### FortiGate Authentication Vulnerability Patch Bypass
- **Description**: Attackers exploiting patch bypass techniques for previously fixed critical FortiGate authentication vulnerability
- **Impact**: Unauthorized access to firewall configurations and network infrastructure
- **Status**: Actively exploited despite patches being available
- **CVE ID**: CVE-2025-59718

### Pwn2Own Automotive Zero-Days
- **Description**: Multiple zero-day vulnerabilities discovered and exploited in automotive systems during security competition
- **Impact**: Various impacts on automotive systems and components
- **Status**: 29 zero-day vulnerabilities exploited on single day during competition

## Affected Systems and Products

- **Cisco Unified Communications Manager**: All versions affected by the zero-day RCE vulnerability
- **Cisco Webex Calling Dedicated Instance**: Critical vulnerability enabling remote code execution
- **GNU InetUtils telnetd**: Authentication bypass affecting systems running the telnet daemon
- **SmarterTools SmarterMail**: Email software vulnerable to authentication bypass
- **Fortinet FortiGate Firewalls**: Devices targeted through FortiCloud SSO exploitation and patch bypass techniques
- **Automotive Systems**: Various automotive platforms and components affected by multiple zero-days
- **Zendesk Support Systems**: Unsecured ticket systems being exploited for massive spam campaigns
- **Chainlit AI Framework**: Open-source conversational AI framework with file disclosure vulnerabilities

## Attack Vectors and Techniques

- **FortiCloud SSO Exploitation**: Automated attacks targeting Fortinet devices through single sign-on mechanisms to alter firewall configurations
- **VS Code Tunnel Abuse**: North Korean threat actors deploying Microsoft VS Code tunnels for remote access and persistence
- **Fake Job Interview Campaigns**: "Contagious Interview" attacks using fraudulent recruitment processes to deliver backdoors
- **PyPI Package Impersonation**: Malicious packages mimicking legitimate libraries like SymPy to deploy cryptocurrency miners
- **Zendesk System Abuse**: Hijacking unsecured Zendesk support systems for global spam distribution
- **AI-Enhanced Malware Development**: VoidLink Linux malware framework created almost entirely using AI agents
- **Phishing Campaigns**: Sophisticated LastPass-targeted phishing using AI-generated content with credible messaging

## Threat Actor Activities

- **North Korean PurpleBravo Campaign**: Targeted 3,136 IP addresses across 20 organizations using fake job interviews to deploy backdoors via VS Code tunnels
- **INC Ransomware Group**: Operational security failures allowed data recovery for 12 U.S. organizations
- **Automated Attack Infrastructure**: Coordinated campaigns targeting FortiGate devices with automated configuration changes
- **AI-Powered Threat Development**: Advanced threat actors utilizing artificial intelligence to create sophisticated malware frameworks like VoidLink
- **Supply Chain Attackers**: Threat actors targeting software repositories and package managers to distribute malicious code