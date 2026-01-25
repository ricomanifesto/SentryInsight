# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure across multiple vectors, with several zero-day vulnerabilities and recently patched flaws being actively exploited in the wild. The most significant threats include a zero-day authentication bypass in Cisco Unified Communications systems affecting potentially millions of devices, ongoing exploitation of a critical VMware vCenter vulnerability, and active attacks against Fortinet firewalls through an incompletely patched authentication bypass. Additional concerning activity includes coordinated campaigns targeting telnet services, enterprise software vulnerabilities, and sophisticated phishing operations targeting single sign-on accounts across major platforms.

## Active Exploitation Details

### Cisco Unified Communications Zero-Day
- **Description**: A critical zero-day vulnerability in Cisco Unified Communications systems that enables complete system takeover
- **Impact**: Successful exploitation leads to full system compromise and potential lateral movement across enterprise networks
- **Status**: Currently being exploited with mass scanning campaigns underway to identify vulnerable systems
- **CVE ID**: CVE-2026-20045

### VMware vCenter Server Authentication Bypass
- **Description**: A critical security flaw in Broadcom VMware vCenter Server that allows authentication bypass
- **Impact**: Unauthorized access to virtualization infrastructure with potential for complete environment compromise
- **Status**: Actively exploited in the wild, patch available since June 2024
- **CVE ID**: CVE-2024-37079

### Fortinet FortiCloud SSO Authentication Bypass
- **Description**: Critical authentication bypass vulnerability affecting FortiGate firewalls' FortiCloud SSO functionality
- **Impact**: Threat actors can bypass authentication and make malicious configuration changes to steal firewall configurations
- **Status**: Active exploitation confirmed on fully patched systems, indicating incomplete patch coverage

### GNU InetUtils Telnetd Authentication Bypass
- **Description**: Critical vulnerability in GNU InetUtils telnetd server that has been present for 11 years, allowing authentication bypass
- **Impact**: Attackers can gain root access to affected systems through coordinated exploitation campaigns
- **Status**: Currently being exploited in coordinated campaigns targeting vulnerable telnet services

### Enterprise Software Vulnerabilities
- **Description**: Four vulnerabilities affecting Versa Networks, Zimbra email servers, and Vite frontend development tool
- **Impact**: Various impacts including unauthorized access, data exfiltration, and system compromise
- **Status**: Active exploitation confirmed by CISA, added to Known Exploited Vulnerabilities catalog

## Affected Systems and Products

- **VMware vCenter Server**: Broadcom VMware vCenter Server installations, particularly those not updated since June 2024
- **Cisco Unified Communications**: Millions of Cisco UC systems potentially affected by zero-day exploitation
- **FortiGate Firewalls**: Fortinet FortiGate devices with FortiCloud SSO functionality, including fully patched systems
- **GNU InetUtils**: Systems running telnetd server from GNU InetUtils package, vulnerability present for 11 years
- **Enterprise Software**: Versa Networks products, Zimbra email servers, and Vite development environments
- **Vehicle Systems**: 76 zero-day vulnerabilities discovered in automotive infotainment systems and EV chargers
- **Microsoft Outlook**: Windows 10, 11, and Windows Server systems experiencing PST-related issues
- **VSCode Marketplace**: Malicious AI extensions affecting Visual Studio Code developers

## Attack Vectors and Techniques

- **Mass Scanning Campaigns**: Automated scanning for vulnerable Cisco UC systems and other enterprise targets
- **Authentication Bypass**: Exploitation of SSO and authentication mechanisms in enterprise systems
- **Configuration Manipulation**: Malicious changes to firewall configurations for persistent access
- **Voice Phishing (Vishing)**: Custom phishing kits targeting SSO accounts through social engineering
- **AI-Generated Malware**: North Korean actors using AI to create PowerShell malware targeting blockchain developers
- **Multi-Stage Phishing**: Complex campaigns delivering ransomware and remote access trojans
- **Supply Chain Attacks**: Malicious extensions in trusted software repositories
- **Wiper Malware**: Destructive attacks targeting critical infrastructure with data-wiping capabilities

## Threat Actor Activities

- **Sandworm (Russian State-Sponsored)**: Attempted deployment of DynoWiper malware against Poland's power grid in December 2025, representing the largest cyber attack on Polish power systems
- **Konni/Opal Sleet (North Korean)**: Targeting blockchain engineers with AI-generated PowerShell malware in sophisticated social engineering campaigns
- **ShinyHunters**: Claiming responsibility for ongoing vishing attacks targeting Okta, Microsoft, and Google SSO accounts for data theft operations
- **Multiple Threat Groups**: Coordinated exploitation of telnetd vulnerabilities and enterprise software flaws across various attack campaigns
- **Unknown Actors**: Exploiting Fortinet firewall vulnerabilities and conducting phishing campaigns with legitimate RMM tools for persistent access