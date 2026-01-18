# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value systems across enterprise environments. A China-linked threat actor has been exploiting a Sitecore zero-day vulnerability to gain initial access to North American critical infrastructure systems. Simultaneously, attackers are actively exploiting CVE-2025-64155, a command injection vulnerability in Fortinet FortiSIEM, and CVE-2026-23550, a maximum-severity flaw in the WordPress Modular DS plugin that allows attackers to gain administrative access. These attacks are complemented by sophisticated malware campaigns including GhostPoster browser extensions with 840,000 installations and credential-stealing Chrome extensions targeting enterprise HR platforms.

## Active Exploitation Details

### Sitecore Zero-Day Vulnerability
- **Description**: An undisclosed zero-day vulnerability in Sitecore content management systems being exploited by China-linked threat actors
- **Impact**: Provides initial access to critical infrastructure systems in North America, enabling lateral movement and persistent access
- **Status**: Currently being exploited in the wild by UAT-8837 threat group; patch status unknown

### Fortinet FortiSIEM Command Injection
- **Description**: A critical command injection vulnerability in Fortinet's FortiSIEM security information and event management platform
- **Impact**: Allows remote code execution and complete system compromise of security monitoring infrastructure
- **Status**: Actively exploited with publicly available proof-of-concept code
- **CVE ID**: CVE-2025-64155

### WordPress Modular DS Plugin Vulnerability
- **Description**: A maximum-severity security flaw in the WordPress Modular DS plugin that allows unauthorized administrative access
- **Impact**: Complete WordPress site takeover, allowing attackers to modify content, install malicious plugins, and access sensitive data
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-23550

### Cisco AsyncOS Zero-Day
- **Description**: A maximum-severity remote code execution vulnerability in Cisco AsyncOS Software affecting Secure Email Gateway and Secure Email and Web Manager
- **Impact**: Complete compromise of email security infrastructure, allowing attackers to bypass security controls and access email communications
- **Status**: Exploited by China-linked APT groups since November 2024, recently patched

## Affected Systems and Products

- **Sitecore Content Management Systems**: Undisclosed versions used in North American critical infrastructure
- **Fortinet FortiSIEM**: Security information and event management platforms
- **WordPress Sites**: Sites using the Modular DS plugin
- **Cisco Secure Email Gateway**: Email security appliances running vulnerable AsyncOS versions
- **Cisco Secure Email and Web Manager**: Management platforms for email security infrastructure
- **Google Chrome**: Browser extensions targeting enterprise users through malicious add-ons
- **Enterprise HR Platforms**: Workday, NetSuite, and similar ERP systems targeted by credential theft

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Sitecore and Cisco systems for initial access
- **Command Injection**: Exploitation of FortiSIEM vulnerability using publicly available proof-of-concept code
- **Malicious Browser Extensions**: Deployment of credential-stealing extensions masquerading as legitimate productivity tools
- **Social Engineering**: GhostPoster campaign using fake browser extensions to compromise user accounts
- **Spear Phishing**: Venezuela-themed lures targeting U.S. policy entities with LOTUSLITE backdoor
- **Malformed Archive Evasion**: GootLoader malware using 500-1,000 concatenated ZIP archives to bypass security detection
- **Cross-Site Scripting**: XSS vulnerabilities in StealC malware control panels exploited by researchers

## Threat Actor Activities

- **UAT-8837 (China-linked)**: Targeting North American critical infrastructure using Sitecore zero-day and other vulnerabilities for persistent access
- **China-linked APT Groups**: Exploiting Cisco AsyncOS zero-day in Secure Email Gateway appliances since November 2024
- **Black Basta Ransomware**: Leadership identified by Ukrainian and German law enforcement, with leader added to Europol and Interpol wanted lists
- **GhostPoster Campaign**: Operators distributing 17 malicious browser extensions across Chrome, Firefox, and Edge stores with 840,000 total installations
- **LOTUSLITE Operators**: Targeting U.S. government and policy entities with Venezuela-themed spear phishing campaigns
- **GootLoader Distributors**: Using sophisticated ZIP archive concatenation techniques to evade security detection systems
- **StealC Malware Operators**: Running info-stealing campaigns with compromised web-based control panels due to XSS vulnerabilities