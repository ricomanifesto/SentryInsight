# Exploitation Report

Critical active exploitation is currently targeting multiple enterprise and infrastructure systems across various sectors. The most significant threats include zero-day vulnerabilities in Cisco's AsyncOS software being exploited by China-linked APT groups since November, a critical Fortinet FortiSIEM command injection flaw under active attack, and a Sitecore zero-day being leveraged for initial access into North American critical infrastructure. Additionally, WordPress environments face immediate risk from active exploitation of the Modular DS plugin, while threat actors continue to evolve their attack methods through sophisticated malware delivery techniques and browser extension abuse.

## Active Exploitation Details

### Cisco AsyncOS Zero-Day Vulnerability
- **Description**: A maximum-severity remote code execution vulnerability in Cisco AsyncOS Software affecting Cisco Secure Email Gateway and Cisco Secure Email and Web Manager
- **Impact**: Complete system compromise and remote code execution capabilities for attackers
- **Status**: Patched by Cisco in January 2026 after being exploited since November 2025
- **CVE ID**: Not specified in available reporting

### Fortinet FortiSIEM Command Injection Flaw
- **Description**: Critical command injection vulnerability allowing unauthorized system access
- **Impact**: Attackers can execute arbitrary commands and gain control of affected FortiSIEM systems
- **Status**: Under active exploitation with publicly available proof-of-concept exploit code
- **CVE ID**: CVE-2025-64155

### Sitecore Zero-Day Vulnerability
- **Description**: Previously unknown vulnerability in Sitecore content management systems
- **Impact**: Provides initial access vectors for threat actors targeting critical infrastructure
- **Status**: Actively exploited by China-linked threat actors for initial network access

### WordPress Modular DS Plugin Vulnerability
- **Description**: Maximum-severity security flaw in the Modular DS WordPress plugin
- **Impact**: Allows attackers to gain administrative access to WordPress websites
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-23550

## Affected Systems and Products

- **Cisco AsyncOS Software**: Cisco Secure Email Gateway and Cisco Secure Email and Web Manager appliances
- **Fortinet FortiSIEM**: Security Information and Event Management platforms
- **Sitecore CMS**: Content management systems used by organizations in critical infrastructure sectors
- **WordPress Modular DS Plugin**: WordPress websites using the vulnerable plugin
- **Google Chrome Extensions**: Malicious extensions impersonating Workday and NetSuite platforms
- **StealC Malware Infrastructure**: Web-based control panels used by malware operators

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of previously unknown vulnerabilities in enterprise software
- **Command Injection**: Leveraging input validation flaws to execute arbitrary system commands
- **Spear Phishing**: Venezuela-themed targeted email campaigns delivering LOTUSLITE backdoor
- **Malicious Browser Extensions**: Chrome extensions masquerading as legitimate HR and ERP platforms
- **Archive-Based Evasion**: GootLoader malware using concatenated ZIP archives (500-1,000 files) to bypass detection
- **Cross-Site Scripting**: XSS vulnerabilities in malware control panels being exploited by researchers

## Threat Actor Activities

- **UAT-8837 (China-linked APT)**: Targeting North American critical infrastructure using both known and zero-day vulnerabilities, including Sitecore exploitation for initial access
- **China-linked APT Groups**: Exploiting Cisco AsyncOS zero-day in Secure Email Gateway environments since November 2025
- **LOTUSLITE Campaign Operators**: Conducting spear phishing attacks against U.S. government and policy entities using Venezuela-themed lures
- **Black Basta Ransomware**: Leadership identified and added to Interpol's Red Notice list following law enforcement action
- **StealC Operators**: Running compromised malware infrastructure with exposed control panels due to XSS vulnerabilities
- **GootLoader Distributors**: Evolving malware delivery techniques using sophisticated archive concatenation methods