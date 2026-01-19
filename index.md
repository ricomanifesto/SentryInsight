# Exploitation Report

The current threat landscape reveals critical active exploitation across multiple fronts, with China-linked advanced persistent threat actors demonstrating particularly aggressive tactics. Key exploitation activities include zero-day vulnerabilities in Sitecore content management systems and Cisco Secure Email Gateways, active attacks against Fortinet's FortiSIEM platform, and a critical WordPress plugin vulnerability under widespread exploitation. Additionally, sophisticated malware campaigns are leveraging browser extensions and complex evasion techniques to compromise enterprise systems and steal credentials.

## Active Exploitation Details

### Sitecore Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Sitecore content management systems that allows initial access to targeted networks
- **Impact**: Enables threat actors to gain unauthorized access to critical infrastructure systems and establish persistent presence
- **Status**: Currently under active exploitation by China-linked APT group UAT-8837 targeting North American critical infrastructure

### Cisco AsyncOS Remote Code Execution Vulnerability
- **Description**: A maximum-severity security flaw in Cisco AsyncOS Software affecting Cisco Secure Email Gateway and Cisco Secure Email and Web Manager
- **Impact**: Allows remote code execution enabling complete system compromise
- **Status**: Patches released by Cisco after exploitation by China-linked APT groups
- **CVE ID**: CVE-2025-20002

### FortiSIEM Command Injection Vulnerability
- **Description**: A critical command injection vulnerability in Fortinet's FortiSIEM security information and event management platform
- **Impact**: Enables attackers to execute arbitrary commands and potentially gain full system control
- **Status**: Actively exploited from multiple IP addresses shortly after disclosure
- **CVE ID**: CVE-2025-64155

### WordPress Modular DS Plugin Authentication Bypass
- **Description**: A maximum-severity authentication bypass vulnerability in the WordPress Modular DS plugin
- **Impact**: Allows attackers to gain administrative access to WordPress sites without authentication
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-23550

## Affected Systems and Products

- **Sitecore Content Management Systems**: Multiple versions affected by zero-day exploitation
- **Cisco Secure Email Gateway**: AsyncOS Software vulnerable to remote code execution
- **Cisco Secure Email and Web Manager**: AsyncOS Software vulnerable to remote code execution
- **Fortinet FortiSIEM**: Security information and event management platform affected by command injection
- **WordPress Sites**: Sites using the Modular DS plugin vulnerable to authentication bypass
- **Google Chrome**: Multiple malicious extensions targeting enterprise HR and ERP platforms
- **Mozilla Firefox**: Affected by GhostPoster malicious extension campaign
- **Microsoft Edge**: Affected by GhostPoster malicious extension campaign

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: China-linked APTs leveraging unknown vulnerabilities in Sitecore and Cisco systems for initial access
- **Malicious Browser Extensions**: Credential-stealing extensions masquerading as productivity tools for enterprise platforms like Workday and NetSuite
- **GhostPoster Campaign**: Sophisticated extension-based attacks with over 840,000 installations across multiple browsers
- **Archive Concatenation**: GootLoader malware using 500-1,000 concatenated ZIP archives to evade security detection
- **Venezuela-Themed Spear Phishing**: LOTUSLITE backdoor delivery targeting U.S. policy entities using politically relevant lures
- **Cross-Site Scripting**: XSS vulnerabilities in StealC malware control panels exploited by researchers for intelligence gathering

## Threat Actor Activities

- **UAT-8837 (China-linked APT)**: Targeting North American critical infrastructure using Sitecore zero-day vulnerabilities for initial access
- **China-linked APT Groups**: Exploiting Cisco Secure Email Gateway zero-day vulnerabilities for persistent access to email infrastructure
- **Black Basta Ransomware**: Leader identified and added to Europol and Interpol wanted lists, with two Ukrainian nationals suspected of group involvement
- **GhostPoster Operators**: Running large-scale malicious extension campaigns across Chrome, Firefox, and Edge with significant user impact
- **LOTUSLITE Campaign**: Targeting U.S. government and policy entities with Venezuela-themed spear phishing attacks
- **StealC Operators**: Information-stealing malware operations compromised by researchers exploiting control panel vulnerabilities