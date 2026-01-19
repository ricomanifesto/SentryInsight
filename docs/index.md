# Exploitation Report

The current threat landscape reveals a concerning surge in active exploitation across multiple platforms and products. Critical vulnerabilities are being exploited in enterprise infrastructure, with several zero-day attacks targeting Fortinet's FortiSIEM platform (CVE-2025-64155), Cisco secure email gateways (CVE-2025-20029), WordPress plugins (CVE-2026-23550), and Sitecore content management systems. China-linked threat actors have demonstrated sophisticated capabilities by exploiting both known and zero-day vulnerabilities to target North American critical infrastructure. Additionally, widespread malicious browser extension campaigns are compromising enterprise HR and ERP platforms, while ransomware operations continue to evolve their tactics for maximum impact.

## Active Exploitation Details

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: A critical command injection vulnerability in Fortinet's FortiSIEM platform that allows attackers to execute arbitrary commands on affected systems
- **Impact**: Complete system compromise and potential lateral movement within enterprise security infrastructure
- **Status**: Disclosed earlier this week and quickly came under attack from multiple IP addresses
- **CVE ID**: CVE-2025-64155

### Cisco Secure Email Gateway Zero-Day RCE
- **Description**: A maximum-severity remote code execution vulnerability in Cisco AsyncOS Software for Cisco Secure Email Gateway and Cisco Secure Email and Web Manager
- **Impact**: Complete system takeover and potential compromise of email security infrastructure
- **Status**: Actively exploited by China-linked APT groups; patches released by Cisco
- **CVE ID**: CVE-2025-20029

### WordPress Modular DS Plugin Authentication Bypass
- **Description**: A maximum-severity security flaw in the WordPress Modular DS plugin that allows unauthorized administrative access
- **Impact**: Complete WordPress site takeover and administrative privilege escalation
- **Status**: Under active exploitation in the wild according to Patchstack
- **CVE ID**: CVE-2026-23550

### Sitecore Zero-Day Vulnerability
- **Description**: An undisclosed zero-day vulnerability in Sitecore content management system exploited for initial access
- **Impact**: Initial foothold in critical infrastructure systems for further lateral movement
- **Status**: Actively exploited by China-linked threat actors targeting North American critical infrastructure

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security information and event management platforms used in enterprise environments
- **Cisco Secure Email Gateway**: Email security appliances and web management systems running AsyncOS Software
- **WordPress Sites**: Websites using the Modular DS plugin for content management
- **Sitecore CMS**: Content management systems used by enterprise organizations
- **Google Chrome**: Browser extensions targeting enterprise HR and ERP platforms including Workday and NetSuite
- **StealC Malware**: Information-stealing malware control panels with cross-site scripting vulnerabilities

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of FortiSIEM systems through command injection flaws allowing arbitrary code execution
- **Remote Code Execution**: Zero-day attacks against Cisco email security infrastructure for system compromise
- **Authentication Bypass**: WordPress plugin exploitation to gain unauthorized administrative access
- **Malicious Browser Extensions**: Fake productivity and security tools distributed through official Chrome Web Store
- **Spear Phishing**: Venezuela-themed lures delivering LOTUSLITE backdoor to U.S. policy entities
- **Concatenated ZIP Archives**: GootLoader malware using 500-1,000 concatenated ZIP files to evade detection
- **Cross-Site Scripting**: Exploitation of XSS vulnerabilities in StealC malware control panels

## Threat Actor Activities

- **UAT-8837 (China-linked APT)**: Targeting North American critical infrastructure using both known and zero-day vulnerabilities including Sitecore CMS exploitation
- **China-linked APT Groups**: Exploiting Cisco email gateway zero-days for persistent access to secure communications infrastructure
- **Black Basta Ransomware**: Leadership identified by Ukrainian and German law enforcement, with leader added to Europol and Interpol wanted lists
- **GhostPoster Campaign**: Distributing 17 malicious browser extensions across Chrome, Firefox, and Edge stores with 840,000 total installations
- **StealC Operators**: Information-stealing malware campaigns compromised by researchers exploiting XSS vulnerabilities in their control panels
- **LOTUSLITE Campaign**: Targeting U.S. government and policy entities with Venezuela-themed spear phishing attacks