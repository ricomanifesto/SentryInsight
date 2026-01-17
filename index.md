# Exploitation Report

Critical zero-day vulnerabilities are under active exploitation by sophisticated threat actors, with China-linked groups demonstrating particular persistence in targeting critical infrastructure. A Fortinet FortiSIEM command injection vulnerability (CVE-2025-64155) and a Cisco AsyncOS remote code execution flaw are being exploited in the wild, while a WordPress plugin vulnerability (CVE-2026-23550) is actively targeted for admin access. Advanced persistent threat groups, including the China-linked UAT-8837, have successfully leveraged Sitecore zero-day vulnerabilities to gain initial access into North American critical infrastructure systems.

## Active Exploitation Details

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: Critical command injection vulnerability in FortiSIEM that allows remote attackers to execute arbitrary commands
- **Impact**: Attackers can gain unauthorized system access and execute malicious commands on affected FortiSIEM installations
- **Status**: Actively exploited with publicly available proof-of-concept exploit code; attacks observed from multiple IP addresses
- **CVE ID**: CVE-2025-64155

### Cisco AsyncOS Remote Code Execution Zero-Day
- **Description**: Maximum-severity zero-day vulnerability in Cisco AsyncOS Software for Secure Email Gateway and Secure Email and Web Manager
- **Impact**: Remote code execution allowing complete system compromise
- **Status**: Exploited by China-linked APT groups since November 2025; recently patched by Cisco
- **CVE ID**: Not specified in articles

### WordPress Modular DS Plugin Authentication Bypass
- **Description**: Maximum-severity authentication bypass vulnerability in WordPress Modular DS plugin
- **Impact**: Allows attackers to gain administrative access to WordPress sites
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-23550

### Sitecore Zero-Day Vulnerability
- **Description**: Zero-day vulnerability in Sitecore content management system
- **Impact**: Provides initial access vector for advanced persistent threat groups
- **Status**: Exploited by China-linked threat actors targeting critical infrastructure
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security information and event management platform vulnerable to command injection attacks
- **Cisco Secure Email Gateway**: Email security appliances affected by AsyncOS zero-day vulnerability
- **Cisco Secure Email and Web Manager**: Management platforms running vulnerable AsyncOS software
- **WordPress Sites**: Websites using the Modular DS plugin are vulnerable to admin takeover
- **Sitecore CMS**: Content management systems targeted through zero-day exploitation
- **Google Chrome Extensions**: Five malicious extensions impersonating Workday and NetSuite platforms
- **StealC Malware Control Panels**: Web-based control panels vulnerable to cross-site scripting attacks

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of input validation flaws in FortiSIEM to execute arbitrary system commands
- **Remote Code Execution**: Zero-day exploitation of Cisco AsyncOS vulnerabilities for complete system compromise
- **Authentication Bypass**: Direct admin access through WordPress plugin vulnerabilities without credential requirements
- **Spear Phishing**: Venezuela-themed email campaigns delivering LOTUSLITE backdoor to U.S. policy entities
- **Malicious Browser Extensions**: Chrome extensions masquerading as legitimate enterprise software to hijack user accounts
- **Malformed Archive Evasion**: GootLoader malware using concatenated ZIP archives (500-1,000 parts) to bypass security detection
- **Cross-Site Scripting**: XSS vulnerabilities in malware control panels allowing unauthorized access to criminal infrastructure

## Threat Actor Activities

- **UAT-8837 (China-linked)**: Advanced persistent threat group targeting North American critical infrastructure using both known vulnerabilities and zero-day exploits including Sitecore CMS flaws
- **China-linked APT Groups**: Exploitation of Cisco AsyncOS zero-day vulnerabilities in Secure Email Gateway appliances since November 2025
- **Black Basta Ransomware**: Gang leader identified and added to Interpol's Red Notice list following law enforcement investigations in Ukraine and Germany
- **LOTUSLITE Campaign**: Targeting of U.S. government and policy entities through Venezuela-themed spear phishing attacks delivering custom backdoor malware
- **GootLoader Operators**: Enhanced evasion techniques using malformed ZIP archives containing 500-1,000 concatenated parts to avoid security detection
- **StealC Info-Stealer**: Criminal operations disrupted by researchers who exploited XSS vulnerabilities in the malware's web control panels to gather intelligence on active sessions