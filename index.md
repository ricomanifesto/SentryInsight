# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise systems and infrastructure components, with threat actors leveraging both zero-day vulnerabilities and recently disclosed flaws. The most significant ongoing exploits include a critical Fortinet FortiSIEM command injection vulnerability that came under immediate attack following disclosure, a Cisco AsyncOS zero-day that has been exploited by China-linked threat actors since November 2024, and a Sitecore zero-day being used by advanced persistent threat groups to target North American critical infrastructure. Additionally, threat actors are exploiting a maximum-severity WordPress plugin vulnerability to gain administrative access to websites, while malware operators continue to evolve their tactics with sophisticated evasion techniques.

## Active Exploitation Details

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: A critical command injection vulnerability in Fortinet's FortiSIEM security information and event management platform that allows attackers to execute arbitrary commands on affected systems
- **Impact**: Complete system compromise, unauthorized access to security monitoring infrastructure, potential lateral movement within enterprise networks
- **Status**: Actively exploited by multiple threat actors from various IP addresses, with publicly available proof-of-concept exploit code accelerating attacks
- **CVE ID**: CVE-2025-64155

### Cisco AsyncOS Zero-Day Remote Code Execution
- **Description**: A maximum-severity zero-day vulnerability in Cisco AsyncOS Software affecting Secure Email Gateway and Secure Email and Web Manager appliances
- **Impact**: Remote code execution capabilities allowing complete system compromise of email security infrastructure
- **Status**: Exploited in the wild since November 2024 by China-linked APT groups, recently patched by Cisco
- **CVE ID**: Not specified in articles

### Sitecore Content Management System Zero-Day
- **Description**: A zero-day vulnerability in Sitecore content management systems being exploited for initial access into enterprise networks
- **Impact**: Initial foothold establishment in target environments, enabling further reconnaissance and lateral movement
- **Status**: Actively exploited by China-linked threat actors targeting North American critical infrastructure
- **CVE ID**: Not specified in articles

### WordPress Modular DS Plugin Critical Flaw
- **Description**: A maximum-severity security flaw in the WordPress Modular DS plugin that allows unauthorized administrative access
- **Impact**: Complete WordPress site takeover, administrative privilege escalation, potential website defacement or malicious content injection
- **Status**: Under active exploitation in the wild with attackers gaining admin access to affected WordPress installations
- **CVE ID**: CVE-2026-23550

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security information and event management platforms used for enterprise security monitoring
- **Cisco Secure Email Gateway**: Email security appliances running vulnerable AsyncOS software versions
- **Cisco Secure Email and Web Manager**: Management systems for email security infrastructure
- **Sitecore CMS**: Content management systems used by enterprise organizations
- **WordPress Sites**: Websites using the vulnerable Modular DS plugin
- **Critical Infrastructure**: North American utility, energy, and other essential service providers

## Attack Vectors and Techniques

- **Command Injection Attacks**: Exploiting input validation weaknesses in FortiSIEM to execute arbitrary system commands
- **Zero-Day Exploitation**: Leveraging previously unknown vulnerabilities in Cisco and Sitecore products for initial access
- **Spear Phishing Campaigns**: Venezuela-themed phishing emails delivering LOTUSLITE backdoor to U.S. policy entities
- **Malicious Browser Extensions**: Five Chrome extensions impersonating Workday and NetSuite platforms for credential theft
- **Archive-Based Evasion**: GootLoader malware using concatenated ZIP archives (500-1,000 parts) to bypass security detection
- **Cross-Site Scripting**: XSS vulnerabilities in StealC malware control panels allowing researcher infiltration

## Threat Actor Activities

- **UAT-8837 (China-linked APT)**: Targeting North American critical infrastructure using Sitecore zero-day exploits and focusing on utility and energy sectors
- **China-linked APT Groups**: Exploiting Cisco AsyncOS zero-day since November 2024 for persistent access to email security infrastructure
- **Black Basta Ransomware**: Leadership identified by international law enforcement with operators added to Interpol Red Notice list
- **StealC Malware Operators**: Running compromised control panels vulnerable to XSS attacks, exposing active criminal sessions to security researchers
- **GootLoader Operators**: Evolving malware delivery techniques using sophisticated archive concatenation for detection evasion
- **WordPress Attackers**: Actively exploiting Modular DS plugin vulnerability to gain administrative access across multiple websites