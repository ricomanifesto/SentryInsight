# Exploitation Report

Critical vulnerability exploitation activity is currently dominated by several high-severity zero-day vulnerabilities being actively exploited in the wild. The most concerning activity includes China-linked threat actors exploiting zero-day vulnerabilities in Fortinet FortiSIEM systems (CVE-2025-64155), Sitecore platforms, and Cisco AsyncOS software. Additionally, a maximum-severity WordPress plugin vulnerability (CVE-2026-23550) is under active exploitation, allowing attackers to gain administrative access to websites. These exploitations represent immediate threats to enterprise infrastructure, with attackers targeting critical systems and successfully establishing persistent access.

## Active Exploitation Details

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: A critical command injection vulnerability in Fortinet FortiSIEM that enables attackers to execute arbitrary commands on affected systems
- **Impact**: Complete system compromise allowing attackers to execute commands with elevated privileges
- **Status**: Actively exploited in the wild with publicly available proof-of-concept exploit code
- **CVE ID**: CVE-2025-64155

### Sitecore Zero-Day Vulnerability
- **Description**: An undisclosed zero-day vulnerability in Sitecore platforms being exploited by China-linked threat actors
- **Impact**: Provides initial access to critical infrastructure systems, enabling lateral movement and persistent access
- **Status**: Actively exploited since at least 2024, targeting North American critical infrastructure

### Cisco AsyncOS Zero-Day RCE
- **Description**: A maximum-severity remote code execution vulnerability in Cisco AsyncOS software affecting Secure Email Gateway and Secure Email and Web Manager
- **Impact**: Complete remote system compromise with maximum privileges
- **Status**: Actively exploited since November 2025, recently patched by Cisco

### WordPress Modular DS Plugin Vulnerability
- **Description**: A maximum-severity security flaw in the WordPress Modular DS plugin that allows unauthorized administrative access
- **Impact**: Complete WordPress site takeover with administrative privileges
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-23550

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security Information and Event Management systems vulnerable to command injection attacks
- **Sitecore Platforms**: Content management systems in critical infrastructure environments
- **Cisco Secure Email Gateway**: Email security appliances running vulnerable AsyncOS software
- **Cisco Secure Email and Web Manager**: Management systems for email security infrastructure
- **WordPress Websites**: Sites using the vulnerable Modular DS plugin

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of input validation flaws in FortiSIEM to execute arbitrary system commands
- **Zero-Day Exploitation**: Advanced persistent threat groups leveraging unknown vulnerabilities for initial access
- **Spear Phishing**: Venezuela-themed campaigns targeting U.S. policy entities with LOTUSLITE backdoor
- **Malware Evasion**: GootLoader using concatenated ZIP archives (500-1,000 parts) to bypass detection systems
- **Browser Extension Abuse**: Malicious Chrome extensions impersonating Workday and NetSuite to hijack user accounts
- **Cross-Site Scripting**: XSS vulnerabilities in StealC malware control panels being exploited by researchers

## Threat Actor Activities

- **UAT-8837 (China-linked)**: Advanced persistent threat group targeting North American critical infrastructure using both known and zero-day vulnerabilities, particularly focusing on Sitecore platforms
- **China-linked APT**: Exploiting Cisco AsyncOS zero-day vulnerabilities in Secure Email Gateway appliances since November, demonstrating sophisticated targeting of email security infrastructure
- **Black Basta Ransomware**: Leader identified and added to Interpol's Red Notice list following collaborative law enforcement efforts
- **GootLoader Operators**: Enhancing evasion techniques with malformed ZIP archive concatenation to avoid security detection
- **LOTUSLITE Campaign**: Targeting U.S. government and policy entities with Venezuela-themed spear phishing attacks
- **StealC Malware Operators**: Information-stealing malware campaigns disrupted by researchers exploiting XSS vulnerabilities in control panels