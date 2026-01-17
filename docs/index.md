# Exploitation Report

Critical zero-day vulnerabilities are under active exploitation across multiple enterprise platforms, with China-linked threat actors demonstrating sophisticated capabilities in targeting critical infrastructure. The most severe incidents include the exploitation of Cisco AsyncOS zero-day vulnerabilities in Secure Email Gateway appliances since November 2024, Sitecore zero-day attacks against North American critical infrastructure, and widespread exploitation of a critical Fortinet FortiSIEM command injection flaw. These attacks represent significant threats to enterprise security, with attackers gaining administrative access and establishing persistent footholds in targeted environments.

## Active Exploitation Details

### Cisco AsyncOS Zero-Day
- **Description**: Maximum-severity remote code execution vulnerability in Cisco AsyncOS Software affecting Cisco Secure Email Gateway and Cisco Secure Email and Web Manager
- **Impact**: Complete system compromise and remote code execution on email security appliances
- **Status**: Actively exploited since November 2024, patch released by Cisco in January 2026
- **CVE ID**: Not specified in source material

### Sitecore Zero-Day
- **Description**: Zero-day vulnerability in Sitecore content management system being exploited for initial access
- **Impact**: Initial access to critical infrastructure systems, enabling lateral movement and persistent access
- **Status**: Under active exploitation by China-linked APT groups targeting North American infrastructure
- **CVE ID**: Not specified in source material

### Fortinet FortiSIEM Command Injection
- **Description**: Critical command injection vulnerability in FortiSIEM allowing arbitrary command execution
- **Impact**: Remote code execution and system compromise of security information and event management systems
- **Status**: Under active exploitation from multiple IP addresses with publicly available exploit code
- **CVE ID**: CVE-2025-64155

### WordPress Modular DS Plugin Vulnerability
- **Description**: Maximum-severity security flaw in the Modular DS WordPress plugin
- **Impact**: Attackers can gain administrative access to WordPress websites
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-23550

## Affected Systems and Products

- **Cisco Secure Email Gateway**: AsyncOS software running on email security appliances
- **Cisco Secure Email and Web Manager**: Management systems for Cisco email security infrastructure
- **Sitecore Content Management System**: Web content management platforms used by enterprises
- **Fortinet FortiSIEM**: Security information and event management platforms
- **WordPress Websites**: Sites using the Modular DS plugin for content management

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging previously unknown vulnerabilities before patches are available
- **Command Injection**: Direct execution of system commands through vulnerable input fields in FortiSIEM
- **Spear Phishing**: LOTUSLITE backdoor campaigns using Venezuela-themed lures targeting U.S. policy entities
- **Malicious Browser Extensions**: Five Chrome extensions impersonating Workday and NetSuite to hijack enterprise accounts
- **Malformed Archive Evasion**: GootLoader malware using concatenated ZIP archives (500-1,000 parts) to bypass detection
- **Cross-Site Scripting**: XSS vulnerabilities in StealC malware control panels being exploited by researchers

## Threat Actor Activities

- **UAT-8837 (China-linked)**: Targeting North American critical infrastructure using Sitecore zero-day and other vulnerabilities for initial access
- **China-linked APT Groups**: Exploiting Cisco AsyncOS zero-day in Secure Email Gateway appliances since November 2024
- **GootLoader Operators**: Implementing advanced evasion techniques using malformed multi-part ZIP archives for malware delivery
- **StealC Malware Operators**: Running compromised control panels with XSS vulnerabilities allowing unauthorized access to criminal infrastructure
- **Black Basta Ransomware**: Leadership identified and added to Interpol Red Notice list, indicating continued law enforcement focus on this group
- **LOTUSLITE Campaign Operators**: Conducting targeted spear phishing against U.S. government and policy entities using politically themed lures