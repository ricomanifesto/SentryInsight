# Exploitation Report

Multiple critical vulnerabilities are currently under active exploitation across enterprise infrastructure, with particular focus on zero-day vulnerabilities in Sitecore, Cisco AsyncOS, and Fortinet FortiSIEM platforms. China-linked threat actors have been exploiting a Sitecore zero-day to target North American critical infrastructure since at least last year, while attackers are actively exploiting recently disclosed Fortinet and Cisco vulnerabilities with publicly available exploit code. Additionally, malicious Chrome extensions are being used to steal credentials from enterprise HR platforms, and the WordPress ecosystem faces continued exploitation of plugin vulnerabilities.

## Active Exploitation Details

### Sitecore Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Sitecore content management system that allows threat actors to gain initial access to systems
- **Impact**: Complete system compromise and access to critical infrastructure networks
- **Status**: Currently being exploited by China-linked APT group UAT-8837, no patch information provided in articles

### Cisco AsyncOS Zero-Day Remote Code Execution
- **Description**: Maximum-severity remote code execution vulnerability in Cisco AsyncOS Software affecting Secure Email Gateway and Secure Email and Web Manager
- **Impact**: Complete system takeover and remote code execution on affected appliances
- **Status**: Actively exploited by China-linked APT since November 2025, recently patched by Cisco

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: Critical command injection vulnerability in FortiSIEM platform
- **Impact**: Remote command execution and complete system compromise
- **Status**: Under active exploitation with publicly available proof-of-concept code
- **CVE ID**: CVE-2025-64155

### WordPress Modular DS Plugin Authentication Bypass
- **Description**: Maximum-severity authentication bypass vulnerability in WordPress Modular DS plugin
- **Impact**: Allows attackers to gain administrative access to WordPress sites
- **Status**: Currently under active exploitation in the wild
- **CVE ID**: CVE-2026-23550

## Affected Systems and Products

- **Sitecore Content Management System**: Zero-day vulnerability affecting unspecified versions
- **Cisco Secure Email Gateway**: AsyncOS software vulnerability with maximum severity rating
- **Cisco Secure Email and Web Manager**: AsyncOS software vulnerability affecting email security appliances
- **Fortinet FortiSIEM**: Command injection vulnerability in security information and event management platform
- **WordPress Sites**: Modular DS plugin vulnerability affecting websites using this specific plugin
- **Google Chrome Browser**: Multiple malicious extensions targeting enterprise HR and ERP platforms including Workday and NetSuite

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: China-linked actors leveraging unknown vulnerabilities in Sitecore for initial access
- **Remote Code Execution**: Exploitation of Cisco AsyncOS vulnerabilities to execute arbitrary commands on email security appliances
- **Command Injection**: Direct exploitation of FortiSIEM flaws using publicly available exploit code
- **Malicious Browser Extensions**: Chrome extensions masquerading as productivity tools to steal authentication credentials
- **Social Engineering**: Venezuela-themed spear phishing campaigns delivering LOTUSLITE backdoor to U.S. policy entities
- **Malformed Archive Evasion**: GootLoader malware using concatenated ZIP archives (500-1,000 files) to evade detection systems
- **Cross-Site Scripting**: Researchers exploiting XSS vulnerabilities in StealC malware control panels for intelligence gathering

## Threat Actor Activities

- **UAT-8837 (China-linked APT)**: Targeting North American critical infrastructure using Sitecore zero-day vulnerabilities for initial access and persistence
- **China-linked APT Group**: Exploiting Cisco AsyncOS zero-day vulnerabilities in Secure Email Gateway appliances since November 2025
- **Black Basta Ransomware Group**: Russian-linked ransomware-as-a-service operation with identified Ukrainian operatives now on Europol and Interpol wanted lists
- **GhostPoster Campaign Operators**: Distributing 17 malicious browser extensions across Chrome, Firefox, and Edge stores with 840,000 total installations
- **StealC Malware Operators**: Running credential-stealing operations through compromised web-based control panels vulnerable to XSS attacks
- **Unknown Threat Actors**: Actively exploiting Fortinet FortiSIEM vulnerability using publicly available proof-of-concept exploit code