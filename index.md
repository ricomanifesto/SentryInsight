# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited by threat actors, with multiple high-severity flaws affecting enterprise infrastructure. China-linked APT groups have exploited Sitecore and Cisco AsyncOS zero-days targeting critical infrastructure and secure email gateways. A critical Fortinet FortiSIEM command injection vulnerability (CVE-2025-64155) is under active exploitation shortly after disclosure. Additionally, a maximum-severity WordPress plugin flaw (CVE-2026-23550) is being exploited to gain administrative access to websites. These incidents highlight the persistent threat from both nation-state actors and cybercriminal groups actively targeting enterprise systems and infrastructure.

## Active Exploitation Details

### Sitecore Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Sitecore content management system exploited by China-linked threat actors
- **Impact**: Allows initial access to critical infrastructure systems in North America
- **Status**: Zero-day vulnerability actively exploited since at least 2024, patch status unclear

### Cisco AsyncOS Zero-Day RCE
- **Description**: Maximum-severity remote code execution vulnerability in Cisco AsyncOS Software for Secure Email Gateway and Secure Email and Web Manager
- **Impact**: Complete compromise of Cisco email security appliances, allowing attackers full system control
- **Status**: Exploited since November 2024, patched by Cisco in January 2026

### Fortinet FortiSIEM Command Injection
- **Description**: Critical command injection vulnerability in Fortinet FortiSIEM security information and event management system
- **Impact**: Remote code execution allowing complete system compromise
- **Status**: Active exploitation reported with publicly available proof-of-concept code
- **CVE ID**: CVE-2025-64155

### WordPress Modular DS Plugin Flaw
- **Description**: Maximum-severity security flaw in WordPress Modular DS plugin
- **Impact**: Allows attackers to gain full administrative access to WordPress websites
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-23550

## Affected Systems and Products

- **Sitecore CMS**: Content management systems used by critical infrastructure organizations
- **Cisco Secure Email Gateway**: Email security appliances running AsyncOS software
- **Cisco Secure Email and Web Manager**: Management systems for Cisco security products
- **Fortinet FortiSIEM**: Security information and event management platforms
- **WordPress Modular DS Plugin**: WordPress websites using the vulnerable plugin
- **Chrome Browser**: Five malicious extensions impersonating Workday and NetSuite platforms

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple threat actors leveraging previously unknown vulnerabilities for initial access
- **Command Injection**: Exploitation of input validation flaws to execute arbitrary commands
- **Malicious Browser Extensions**: Chrome extensions masquerading as legitimate HR and ERP platforms to hijack user accounts
- **ZIP Archive Evasion**: GootLoader malware using 500-1,000 concatenated ZIP archives to bypass detection systems
- **Spear Phishing**: Venezuela-themed lures delivering LOTUSLITE backdoor to U.S. policy entities
- **Cross-Site Scripting**: XSS vulnerabilities in StealC malware control panels exploited by researchers

## Threat Actor Activities

- **UAT-8837 (China-linked APT)**: Targeting critical infrastructure systems in North America using Sitecore zero-day and other vulnerabilities for persistent access
- **China-linked APT Group**: Exploiting Cisco AsyncOS zero-day in Secure Email Gateway appliances since November 2024
- **Black Basta Ransomware Group**: Leadership identified by Ukrainian and German law enforcement, with key figures added to INTERPOL Red Notice and EU Most Wanted lists
- **Unknown Threat Actors**: Actively exploiting Fortinet FortiSIEM vulnerability using publicly available exploit code
- **GootLoader Operators**: Evolving evasion techniques using malformed ZIP archives for initial access operations
- **LOTUSLITE Campaign**: Targeting U.S. government and policy entities with Venezuela-themed spear phishing attacks