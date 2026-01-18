# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise systems, with attackers actively exploiting zero-day vulnerabilities in Cisco email security appliances and Sitecore content management systems. China-linked threat actors are leveraging these vulnerabilities to compromise critical infrastructure in North America, while other campaigns target WordPress sites and enterprise security tools. The exploitation landscape includes command injection flaws in Fortinet FortiSIEM, authentication bypass vulnerabilities in WordPress plugins, and sophisticated malware delivery techniques using malformed ZIP archives to evade detection.

## Active Exploitation Details

### Cisco AsyncOS Zero-Day Remote Code Execution
- **Description**: A maximum-severity remote code execution vulnerability in Cisco AsyncOS Software affecting Cisco Secure Email Gateway and Cisco Secure Email and Web Manager appliances
- **Impact**: Complete system compromise and potential lateral movement within enterprise networks
- **Status**: Actively exploited by China-linked APT groups since November 2024, patch released by Cisco in January 2025

### Sitecore Zero-Day Vulnerability
- **Description**: An undisclosed zero-day vulnerability in Sitecore content management system exploited for initial access to critical infrastructure
- **Impact**: Initial access vector enabling deeper network penetration and data exfiltration
- **Status**: Actively exploited by UAT-8837 threat group targeting North American critical infrastructure

### Fortinet FortiSIEM Command Injection Flaw
- **Description**: Command injection vulnerability in Fortinet FortiSIEM security information and event management platform
- **Impact**: Remote code execution and potential compromise of security monitoring infrastructure
- **Status**: Under active exploitation with publicly available proof-of-concept exploit code
- **CVE ID**: CVE-2025-64155

### WordPress Modular DS Plugin Authentication Bypass
- **Description**: Maximum-severity authentication bypass vulnerability in the Modular DS WordPress plugin
- **Impact**: Administrative access to WordPress sites, enabling complete site takeover
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-23550

## Affected Systems and Products

- **Cisco AsyncOS Software**: Cisco Secure Email Gateway and Cisco Secure Email and Web Manager appliances
- **Sitecore CMS**: Various versions of Sitecore content management system
- **Fortinet FortiSIEM**: Security information and event management platforms
- **WordPress Modular DS Plugin**: WordPress sites using the vulnerable plugin
- **Google Chrome**: Extensions impersonating Workday and NetSuite platforms
- **StealC Malware**: Web-based control panels with cross-site scripting vulnerabilities

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: China-linked actors exploiting previously unknown vulnerabilities in enterprise systems
- **Command Injection**: Leveraging input validation flaws to execute arbitrary commands on target systems
- **Authentication Bypass**: Circumventing login mechanisms to gain unauthorized administrative access
- **Malicious Browser Extensions**: Chrome extensions impersonating legitimate HR and ERP platforms
- **Malformed ZIP Archives**: GootLoader malware using concatenated ZIP files (500-1,000 archives) to evade security detection
- **Spear Phishing**: Venezuela-themed campaigns targeting U.S. policy entities with LOTUSLITE backdoor

## Threat Actor Activities

- **UAT-8837 (China-linked)**: Targeting North American critical infrastructure using Sitecore zero-day and other vulnerabilities for initial access and lateral movement
- **China-linked APT Groups**: Exploiting Cisco AsyncOS zero-day since November 2024 to compromise email security infrastructure
- **Black Basta Ransomware**: Leadership identified by Ukrainian and German law enforcement, with key figures added to EU Most Wanted and INTERPOL Red Notice lists
- **GootLoader Operators**: Evolving malware delivery techniques using sophisticated ZIP archive concatenation for detection evasion
- **LOTUSLITE Campaign**: Targeting U.S. government and policy entities with politically-themed spear phishing attacks focused on Venezuela
- **StealC Operators**: Info-stealing malware campaigns with compromised web control panels due to XSS vulnerabilities