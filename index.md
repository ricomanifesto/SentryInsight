# Exploitation Report

Recent cybersecurity activity shows a concerning surge in active exploitation targeting critical infrastructure and enterprise systems. China-linked threat actors have been particularly active, exploiting zero-day vulnerabilities in Sitecore content management systems and Cisco email security appliances to target North American critical infrastructure. Meanwhile, the Fortinet ecosystem faces continued pressure with active exploitation of FortiSIEM command injection vulnerabilities. Additional threats include malicious Chrome extensions targeting enterprise HR platforms, credential-stealing campaigns, and WordPress plugin vulnerabilities being exploited for administrative access.

## Active Exploitation Details

### Cisco AsyncOS Zero-Day Remote Code Execution
- **Description**: Maximum-severity remote code execution vulnerability in Cisco AsyncOS Software for Cisco Secure Email Gateway and Cisco Secure Email and Web Manager
- **Impact**: Attackers can achieve complete system compromise and remote code execution on email security appliances
- **Status**: Actively exploited in the wild by China-linked APT groups since November 2024, patches released in January 2025

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: Critical command injection vulnerability in Fortinet FortiSIEM security information and event management platform
- **Impact**: Allows attackers to execute arbitrary commands and gain unauthorized access to security monitoring systems
- **Status**: Currently under active exploitation with publicly available proof-of-concept exploit code
- **CVE ID**: CVE-2025-64155

### Sitecore Zero-Day Vulnerability
- **Description**: Zero-day vulnerability in Sitecore content management system used for initial access by advanced persistent threat actors
- **Impact**: Enables initial compromise of web applications and potential lateral movement within enterprise networks
- **Status**: Actively exploited by China-linked threat actors targeting critical infrastructure

### WordPress Modular DS Plugin Critical Flaw
- **Description**: Maximum-severity authentication bypass vulnerability in WordPress Modular DS plugin allowing unauthorized administrative access
- **Impact**: Complete administrative takeover of affected WordPress websites and potential website defacement or data theft
- **Status**: Currently under active exploitation in the wild
- **CVE ID**: CVE-2026-23550

## Affected Systems and Products

- **Cisco Secure Email Gateway**: AsyncOS software vulnerable to remote code execution attacks
- **Cisco Secure Email and Web Manager**: Email security management platforms affected by zero-day exploitation
- **Fortinet FortiSIEM**: Security information and event management systems vulnerable to command injection
- **Sitecore CMS**: Content management systems used in critical infrastructure environments
- **WordPress Modular DS Plugin**: WordPress plugin installations vulnerable to authentication bypass
- **Google Chrome Extensions**: Malicious extensions targeting enterprise HR platforms like Workday and NetSuite
- **Enterprise HR/ERP Platforms**: Systems targeted through malicious browser extensions for credential theft

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Threat actors leveraging unknown vulnerabilities in Cisco and Sitecore systems for initial access
- **Malicious Browser Extensions**: Chrome extensions masquerading as productivity tools to steal enterprise credentials
- **Command Injection**: Direct exploitation of input validation flaws in FortiSIEM to execute arbitrary commands
- **Spear Phishing**: Venezuela-themed campaigns targeting U.S. policy entities with LOTUSLITE backdoor
- **Supply Chain Targeting**: Potential attacks against AWS CodeBuild misconfigurations exposing GitHub repositories
- **Archive Evasion**: GootLoader malware using 500-1,000 concatenated ZIP archives to bypass security detection
- **Cross-Site Scripting**: XSS vulnerabilities in StealC malware control panels exploited by researchers

## Threat Actor Activities

- **UAT-8837 (China-linked)**: Advanced persistent threat group targeting North American critical infrastructure using both known and zero-day vulnerabilities in Sitecore and Cisco systems
- **Black Basta Ransomware**: Leadership identified by Ukrainian and German law enforcement, with key figures added to Europol and Interpol wanted lists
- **GhostPoster Campaign**: Malicious browser extension operation with 840,000 total installations across Chrome, Firefox, and Edge stores
- **StealC Operators**: Information-stealing malware operators whose control panels were compromised by security researchers
- **LOTUSLITE Campaign**: Targeted attacks against U.S. government and policy entities using politically-themed Venezuelan lures