# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure across multiple sectors. The most significant threats include zero-day exploitation of Sitecore systems by China-linked threat actors targeting North American critical infrastructure, active exploitation of a critical Fortinet FortiSIEM command injection vulnerability, and a maximum-severity Cisco AsyncOS zero-day that has been exploited since November 2024. Additionally, attackers are leveraging a critical WordPress plugin vulnerability to gain administrative access to websites. These exploitations demonstrate sophisticated threat actors' focus on high-value enterprise targets and critical infrastructure systems.

## Active Exploitation Details

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: A command injection vulnerability in Fortinet FortiSIEM security information and event management platform
- **Impact**: Attackers can execute arbitrary commands on affected systems
- **Status**: Actively exploited with publicly available proof-of-concept exploit code
- **CVE ID**: CVE-2025-64155

### Cisco AsyncOS Zero-Day Remote Code Execution
- **Description**: A maximum-severity remote code execution vulnerability in Cisco AsyncOS Software for Secure Email Gateway and Secure Email and Web Manager
- **Impact**: Complete system compromise and potential email security bypass
- **Status**: Exploited in the wild since November 2024, recently patched by Cisco
- **CVE ID**: Not specified in articles

### Sitecore Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Sitecore content management systems
- **Impact**: Initial access for advanced persistent threat actors targeting critical infrastructure
- **Status**: Actively exploited by China-linked threat actors
- **CVE ID**: Not specified in articles

### WordPress Modular DS Plugin Critical Flaw
- **Description**: A maximum-severity vulnerability in the WordPress Modular DS plugin
- **Impact**: Allows attackers to gain administrative access to WordPress websites
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2026-23550

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security information and event management platforms actively under attack
- **Cisco Secure Email Gateway**: Email security appliances affected by AsyncOS zero-day
- **Cisco Secure Email and Web Manager**: Management systems vulnerable to remote code execution
- **Sitecore CMS**: Content management systems targeted by APT groups
- **WordPress Sites**: Websites using the Modular DS plugin vulnerable to admin takeover
- **Critical Infrastructure**: North American systems targeted through zero-day exploits

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of FortiSIEM systems through malicious command execution
- **Zero-Day Exploitation**: Use of previously unknown vulnerabilities in Sitecore and Cisco products
- **Spear Phishing**: Venezuela-themed campaigns delivering LOTUSLITE backdoor to U.S. policy entities
- **Malware Evasion**: GootLoader using concatenated ZIP archives (500-1,000 files) to bypass detection
- **Browser Extensions**: Five malicious Chrome extensions impersonating Workday and NetSuite platforms
- **Web Panel Exploitation**: Cross-site scripting vulnerabilities in StealC malware control panels

## Threat Actor Activities

- **UAT-8837 (China-linked APT)**: Targeting North American critical infrastructure using Sitecore zero-day exploits for initial access
- **China-linked APT Groups**: Exploiting Cisco AsyncOS zero-day in Secure Email Gateway attacks since November 2024
- **LOTUSLITE Campaign Operators**: Targeting U.S. government and policy entities with politically-themed spear phishing campaigns
- **GootLoader Operators**: Implementing advanced evasion techniques using malformed ZIP archives for malware delivery
- **StealC Malware Operators**: Operating compromised control panels with exploitable XSS vulnerabilities
- **Black Basta Ransomware Group**: Leadership identified and added to Interpol's Red Notice list
- **Chrome Extension Threat Actors**: Deploying malicious browser extensions targeting enterprise HR and ERP platforms