# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value systems across enterprise infrastructure. Chinese-linked threat actors are actively exploiting zero-day vulnerabilities in Sitecore systems and Cisco AsyncOS platforms to gain access to critical infrastructure in North America. Simultaneously, the Fortinet FortiSIEM platform is under active attack following the disclosure of CVE-2025-64155, with proof-of-concept exploit code now publicly available. Additional threats include sophisticated malware campaigns using advanced evasion techniques, malicious browser extensions targeting enterprise platforms, and ongoing ransomware operations by established criminal groups.

## Active Exploitation Details

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: A critical command injection vulnerability in Fortinet FortiSIEM platforms that allows remote code execution
- **Impact**: Attackers can execute arbitrary commands and gain unauthorized access to security information and event management systems
- **Status**: Under active exploitation with publicly available proof-of-concept exploit code
- **CVE ID**: CVE-2025-64155

### Sitecore Zero-Day Vulnerability
- **Description**: An undisclosed zero-day vulnerability in Sitecore content management systems being exploited for initial access
- **Impact**: Provides threat actors with entry points into critical infrastructure networks
- **Status**: Actively exploited by Chinese-linked APT groups since at least November 2024

### Cisco AsyncOS Zero-Day Vulnerability
- **Description**: A maximum-severity zero-day vulnerability in Cisco AsyncOS Software affecting Secure Email Gateway and Secure Email and Web Manager
- **Impact**: Enables remote code execution and complete system compromise
- **Status**: Exploited since November 2024, recently patched by Cisco

### WordPress Modular DS Plugin Vulnerability
- **Description**: A maximum-severity authentication bypass vulnerability in the WordPress Modular DS plugin
- **Impact**: Allows attackers to gain administrator access to WordPress websites
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-23550

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security information and event management platforms vulnerable to command injection attacks
- **Sitecore CMS**: Content management systems targeted by Chinese APT groups for critical infrastructure access
- **Cisco Secure Email Gateway**: AsyncOS-based email security appliances affected by zero-day exploitation
- **Cisco Secure Email and Web Manager**: Management platforms running vulnerable AsyncOS software
- **WordPress Sites**: Websites using the Modular DS plugin susceptible to authentication bypass
- **Chrome Browser**: Users targeted by malicious extensions impersonating Workday and NetSuite platforms

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of FortiSIEM systems through command injection vulnerabilities with publicly available exploits
- **Zero-Day Exploitation**: Advanced persistent threat groups leveraging undisclosed vulnerabilities in enterprise platforms
- **Spear Phishing**: Venezuela-themed campaigns delivering LOTUSLITE backdoors to U.S. government and policy entities
- **Malicious Browser Extensions**: Five Chrome extensions masquerading as legitimate HR and ERP platforms to hijack user accounts
- **Archive Evasion**: GootLoader malware using concatenated ZIP archives (500-1,000 files) to bypass security detection
- **Cross-Site Scripting**: Exploitation of XSS vulnerabilities in StealC malware control panels for intelligence gathering

## Threat Actor Activities

- **UAT-8837 (China-linked)**: Targeting critical infrastructure in North America using both known and zero-day vulnerabilities for long-term access
- **Chinese APT Groups**: Exploiting Cisco AsyncOS and Sitecore platforms since November 2024 for strategic intelligence gathering
- **Black Basta Ransomware**: Continued operations with leadership now identified and added to INTERPOL Red Notice and EU Most Wanted lists
- **GootLoader Operators**: Implementing advanced evasion techniques using malformed ZIP archives to maintain stealth in initial access operations
- **LOTUSLITE Campaign**: Sophisticated actors targeting U.S. government entities with politically-themed lures and custom backdoors