# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure through multiple attack vectors, with particular emphasis on zero-day vulnerabilities and malicious browser extensions. Notable active exploits include a command injection vulnerability in Fortinet's FortiSIEM platform that came under immediate attack following disclosure, and a maximum-severity AsyncOS zero-day that has been exploited by China-linked threat actors since November 2025. Additionally, widespread campaigns involving malicious Chrome extensions are targeting enterprise HR and ERP platforms, while advanced persistent threat groups continue to exploit zero-day vulnerabilities in content management systems for initial access to critical infrastructure.

## Active Exploitation Details

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: A critical command injection vulnerability in Fortinet FortiSIEM that allows attackers to execute arbitrary commands on the system
- **Impact**: Attackers can gain unauthorized access and control over FortiSIEM installations, potentially compromising security monitoring capabilities
- **Status**: Actively being exploited by attackers from various IP addresses following public disclosure
- **CVE ID**: CVE-2025-64155

### Cisco AsyncOS Zero-Day Remote Code Execution
- **Description**: A maximum-severity security flaw in Cisco AsyncOS Software affecting Cisco Secure Email Gateway and Cisco Secure Email and Web Manager
- **Impact**: Remote code execution capabilities allowing complete system compromise
- **Status**: Exploited by China-linked APT groups since November 2025, recently patched by Cisco
- **CVE ID**: Not specified in articles

### Sitecore Zero-Day Vulnerability
- **Description**: An unpatched zero-day vulnerability in Sitecore content management system used for initial access
- **Impact**: Provides threat actors with initial access to critical infrastructure systems
- **Status**: Actively exploited by China-linked threat actor UAT-8837 targeting North American critical infrastructure
- **CVE ID**: Not specified in articles

### WordPress Modular DS Plugin Critical Flaw
- **Description**: A maximum-severity authentication bypass vulnerability in the WordPress Modular DS plugin
- **Impact**: Allows attackers to gain administrative access to WordPress sites without authentication
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-23550

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security information and event management systems vulnerable to command injection attacks
- **Cisco Secure Email Gateway**: Email security appliances running vulnerable AsyncOS software versions
- **Cisco Secure Email and Web Manager**: Management platforms affected by AsyncOS vulnerability
- **Sitecore CMS**: Content management systems used by critical infrastructure organizations
- **WordPress Sites**: Websites using the vulnerable Modular DS plugin
- **Google Chrome**: Browser users targeted by malicious extensions impersonating enterprise platforms
- **Enterprise HR/ERP Platforms**: Organizations using Workday, NetSuite, and similar enterprise software

## Attack Vectors and Techniques

- **Malicious Browser Extensions**: Attackers deploying fake Chrome extensions masquerading as productivity and security tools for HR/ERP platforms to steal authentication credentials
- **GhostPoster Campaign**: Large-scale malicious extension distribution with over 840,000 installations across Chrome, Firefox, and Edge browsers
- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise software for initial access
- **Spear Phishing**: Venezuela-themed lures used to deliver LOTUSLITE backdoor targeting U.S. policy entities
- **Supply Chain Targeting**: Attempts to compromise AWS CodeBuild configurations to gain access to GitHub repositories including AWS JavaScript SDK
- **Concatenated ZIP Archives**: GootLoader malware using 500-1,000 concatenated ZIP archives to evade detection systems

## Threat Actor Activities

- **UAT-8837 (China-linked)**: Advanced persistent threat group focusing on North American critical infrastructure, exploiting both known vulnerabilities and zero-days including Sitecore CMS
- **China-linked APT Groups**: Multiple groups exploiting Cisco AsyncOS zero-day since November 2025, targeting secure email gateway infrastructure
- **Black Basta Ransomware**: Russia-linked ransomware-as-a-service group with leadership now on INTERPOL Red Notice and EU Most Wanted lists
- **GhostPoster Campaign Operators**: Cybercriminals distributing malicious browser extensions at scale across multiple browser platforms
- **StealC Malware Operators**: Information-stealing malware groups whose control panels were compromised by researchers exploiting XSS vulnerabilities
- **LOTUSLITE Operators**: Threat actors targeting U.S. government and policy entities using politically-themed spear phishing campaigns