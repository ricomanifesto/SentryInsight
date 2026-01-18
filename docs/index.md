# Exploitation Report

Critical vulnerability exploitation activity is currently targeting enterprise infrastructure and web applications across multiple sectors. Active attacks are exploiting zero-day vulnerabilities in Sitecore content management systems by China-linked threat actors targeting North American critical infrastructure, while a maximum-severity command injection flaw in Fortinet FortiSIEM is being actively exploited with publicly available proof-of-concept code. Additionally, a critical WordPress plugin vulnerability is under active exploitation to gain administrative access, and Cisco has patched a zero-day remote code execution vulnerability in AsyncOS that was exploited by China-linked APTs for nearly three months. These exploitation campaigns demonstrate sophisticated threat actors leveraging both zero-day vulnerabilities and recently disclosed flaws to achieve persistent access to enterprise systems.

## Active Exploitation Details

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: A critical command injection vulnerability in Fortinet FortiSIEM security information and event management platform
- **Impact**: Attackers can execute arbitrary commands and gain unauthorized access to security monitoring infrastructure
- **Status**: Actively exploited with publicly available proof-of-concept exploit code
- **CVE ID**: CVE-2025-64155

### WordPress Modular DS Plugin Authentication Bypass
- **Description**: A maximum-severity security flaw in the WordPress Modular DS plugin that allows authentication bypass
- **Impact**: Attackers can gain administrative access to WordPress sites without authentication
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2026-23550

### Cisco AsyncOS Zero-Day Remote Code Execution
- **Description**: A maximum-severity remote code execution vulnerability in Cisco AsyncOS Software for Secure Email Gateway and Secure Email and Web Manager
- **Impact**: Complete system compromise and unauthorized access to email security infrastructure
- **Status**: Exploited since November 2025 by China-linked APT, recently patched

### Sitecore Zero-Day Vulnerability
- **Description**: An unspecified zero-day vulnerability in Sitecore content management system
- **Impact**: Initial access vector for advanced persistent threat operations targeting critical infrastructure
- **Status**: Actively exploited by China-linked threat actor UAT-8837 for critical infrastructure attacks

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security information and event management platform experiencing active command injection exploitation
- **WordPress Modular DS Plugin**: WordPress plugin vulnerable to authentication bypass attacks
- **Cisco Secure Email Gateway**: Email security appliances affected by AsyncOS zero-day exploitation
- **Cisco Secure Email and Web Manager**: Email and web security management systems compromised through AsyncOS vulnerability
- **Sitecore Content Management System**: Enterprise CMS platforms targeted through zero-day exploitation
- **Google Chrome Browser**: Five malicious extensions impersonating Workday and NetSuite discovered in Chrome Web Store
- **StealC Malware Control Panels**: Info-stealing malware infrastructure compromised through cross-site scripting vulnerabilities

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of FortiSIEM vulnerability to execute arbitrary system commands
- **Authentication Bypass**: WordPress plugin exploitation to gain unauthorized administrative privileges
- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities leveraged for initial access and persistence
- **Malicious Browser Extensions**: Chrome extensions masquerading as legitimate enterprise applications to hijack user accounts
- **Spear Phishing**: Venezuela-themed political lures used to deliver LOTUSLITE backdoor to U.S. government entities
- **Malformed ZIP Archives**: GootLoader malware using concatenated ZIP archives (500-1,000 parts) to evade security detection
- **Cross-Site Scripting**: XSS vulnerabilities in malware control panels exploited by security researchers

## Threat Actor Activities

- **UAT-8837 (China-linked)**: Advanced persistent threat group targeting North American critical infrastructure using Sitecore zero-day vulnerabilities for initial access
- **China-linked APT**: Exploitation of Cisco AsyncOS zero-day since November 2025 targeting Secure Email Gateway appliances
- **Black Basta Ransomware**: Two Ukrainian individuals identified as operators of Russia-linked ransomware-as-a-service group, with leader added to Europol and INTERPOL wanted lists
- **LOTUSLITE Campaign**: Targeting U.S. government and policy entities using Venezuela-themed spear phishing to deliver backdoor malware
- **GootLoader Operators**: Malware distribution group implementing advanced evasion techniques using malformed multi-part ZIP archives
- **StealC Malware Operators**: Info-stealing malware campaign disrupted by researchers exploiting XSS vulnerabilities in their control panels