# Exploitation Report

Current cybersecurity threat landscape shows significant exploitation activity across multiple vectors, with critical vulnerabilities being actively exploited in enterprise environments. Key concerns include a critical FortiSIEM command injection vulnerability under active exploitation, a Sitecore zero-day being leveraged by China-linked APT groups for critical infrastructure attacks, and a maximum-severity Cisco AsyncOS zero-day exploited in secure email gateways. Additionally, widespread malicious browser extension campaigns are targeting enterprise platforms, while advanced malware loaders are employing sophisticated evasion techniques to bypass security controls.

## Active Exploitation Details

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: Critical command injection vulnerability in FortiSIEM security information and event management platform
- **Impact**: Allows attackers to execute arbitrary commands on affected systems
- **Status**: Currently under active exploitation from various IP addresses following disclosure
- **CVE ID**: CVE-2025-64155

### Sitecore Zero-Day Vulnerability
- **Description**: Zero-day vulnerability in Sitecore content management platform exploited by China-linked threat actors
- **Impact**: Enables unauthorized access to critical infrastructure systems and data exfiltration
- **Status**: Actively exploited in targeted attacks against North American critical infrastructure

### Cisco AsyncOS Remote Code Execution
- **Description**: Maximum-severity security flaw in Cisco AsyncOS Software for Cisco Secure Email Gateway and Cisco Secure Email and Web Manager
- **Impact**: Allows remote code execution on secure email infrastructure
- **Status**: Patched by Cisco after nearly a month of exploitation by China-linked APT groups

### AMD StackWarp Hardware Vulnerability
- **Description**: Hardware flaw affecting AMD processors that breaks SEV-SNP (Secure Encrypted Virtualization - Secure Nested Paging) protections
- **Impact**: Compromises confidential computing protections on virtualized environments
- **Status**: Disclosed by academic researchers, affects Zen 1-5 CPUs

### StealC Malware Panel Cross-Site Scripting
- **Description**: XSS vulnerability in the web-based control panel used by StealC information stealer operators
- **Impact**: Allows researchers to monitor threat actor operations and gather intelligence
- **Status**: Vulnerability exploited by security researchers for threat intelligence gathering

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security information and event management platforms under active exploitation
- **Sitecore CMS**: Content management systems in critical infrastructure environments
- **Cisco Secure Email Gateway**: Email security appliances running vulnerable AsyncOS software
- **Cisco Secure Email and Web Manager**: Management platforms for email security solutions
- **AMD Processors**: Zen 1-5 architecture CPUs with SEV-SNP vulnerabilities
- **Google Chrome Extensions**: Malicious extensions targeting enterprise HR and ERP platforms including Workday and NetSuite
- **Enterprise Browsers**: Chrome, Firefox, and Edge browsers with malicious GhostPoster extensions (840,000+ installations)

## Attack Vectors and Techniques

- **Spear Phishing**: Venezuela-themed lures targeting U.S. policy entities for LOTUSLITE backdoor delivery
- **Malicious Browser Extensions**: Chrome extensions masquerading as productivity tools to steal authentication credentials
- **ClickFix-Style Social Engineering**: CrashFix extension deliberately crashes browsers to deliver ModeloRAT malware
- **Concatenated ZIP Archives**: GootLoader malware using 500-1,000 concatenated ZIP files to evade detection
- **Hardware-Level Exploitation**: StackWarp attacks targeting AMD processor security features
- **Command Injection**: Direct exploitation of FortiSIEM vulnerabilities for system compromise
- **Zero-Day Exploitation**: Coordinated attacks against Sitecore and Cisco platforms before patches were available

## Threat Actor Activities

- **China-Linked APT Groups**: Systematic targeting of North American critical infrastructure using Sitecore zero-day vulnerabilities and Cisco email gateway exploits
- **KongTuke Campaign**: Ongoing operation using malicious Chrome extensions and ModeloRAT for credential theft and system compromise
- **Black Basta Ransomware**: Russia-linked RaaS group with identified Ukrainian operatives added to EU Most Wanted and INTERPOL Red Notice
- **GhostPoster Campaign**: Coordinated malicious extension deployment across multiple browser stores affecting 840,000+ users
- **Access Brokers**: Jordanian operator pleading guilty to selling network access to 50+ corporate environments
- **StealC Operators**: Information stealer campaigns with compromised control panels exposing operational security