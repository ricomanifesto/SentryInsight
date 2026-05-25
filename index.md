# Exploitation Report

The cybersecurity landscape is currently experiencing a surge in critical exploitation activities across multiple fronts. Active exploitation campaigns are targeting fundamental web infrastructure including Ghost CMS SQL injection vulnerabilities, Drupal Core flaws, and LiteSpeed cPanel plugins. Supply chain attacks have intensified with sophisticated campaigns like TrapDoor targeting npm, PyPI, and CratesIO repositories, while Laravel-Lang packages and Packagist repositories have been compromised to distribute credential-stealing malware. Zero-day vulnerabilities are being actively exploited in Trend Micro Apex One security software, and maximum-severity flaws have been discovered in Cisco Secure Workload and Ubiquiti UniFi OS systems.

## Active Exploitation Details

### Ghost CMS SQL Injection Vulnerability
- **Description**: Critical SQL injection flaw in Ghost CMS being exploited to inject malicious JavaScript code
- **Impact**: Enables large-scale ClickFix attack campaigns that can compromise website visitors
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-26980

### Drupal Core SQL Injection Vulnerability
- **Description**: Critical SQL injection bug in Drupal Core that has been recently patched
- **Impact**: Allows attackers to execute arbitrary SQL commands and potentially gain full system access
- **Status**: Actively exploited and added to CISA KEV catalog
- **CVE ID**: Not specified in the articles

### LiteSpeed cPanel Plugin Vulnerability
- **Description**: Maximum-severity security flaw in LiteSpeed User-End cPanel Plugin
- **Impact**: Enables attackers to run scripts with root privileges
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-48172

### Trend Micro Apex One Zero-Day
- **Description**: Zero-day vulnerability in Trend Micro Apex One security software
- **Impact**: Allows attackers to compromise Windows systems protected by the security solution
- **Status**: Actively exploited, patch released
- **CVE ID**: Not specified in the articles

### Langflow Vulnerability
- **Description**: Security flaw in Langflow platform
- **Impact**: Exploitation details not specified in available content
- **Status**: Added to CISA KEV catalog due to active exploitation
- **CVE ID**: Not specified in the articles

## Affected Systems and Products

- **Ghost CMS**: Content management system vulnerable to SQL injection attacks
- **Drupal Core**: Critical web platform experiencing targeted SQL injection exploitation
- **LiteSpeed cPanel Plugin**: Web hosting control panel plugin with root privilege escalation
- **Trend Micro Apex One**: Enterprise security software with zero-day vulnerability
- **Laravel-Lang Packages**: PHP localization packages compromised in supply chain attack
- **npm, PyPI, CratesIO**: Package repositories targeted by TrapDoor campaign
- **Packagist**: PHP package repository with 8 infected packages
- **Cisco Secure Workload**: Network security platform with maximum-severity REST API flaw
- **Ubiquiti UniFi OS**: Network management system with three maximum-severity vulnerabilities
- **Langflow**: Platform added to CISA KEV due to active exploitation

## Attack Vectors and Techniques

- **SQL Injection**: Large-scale exploitation of Ghost CMS and Drupal Core vulnerabilities
- **Supply Chain Attacks**: Multi-ecosystem campaigns targeting software repositories
- **Credential Stealing**: Malware deployment through compromised packages
- **ClickFix Campaigns**: JavaScript injection leading to social engineering attacks
- **Zero-Day Exploitation**: Active targeting of unpatched Trend Micro security software
- **CI/CD Pipeline Abuse**: Megalodon campaign targeting GitHub repositories with malicious workflows
- **Social Engineering**: Phishing campaigns using legitimate platform lures
- **DDoS Operations**: KimWolf botnet infecting nearly two million devices

## Threat Actor Activities

- **TrapDoor Campaign**: Coordinated cross-ecosystem supply chain attack targeting npm, PyPI, and CratesIO repositories
- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned threat actor targeting Ukrainian government entities with Prometheus-themed phishing
- **Megalodon Campaign**: Automated attack targeting 5,561 GitHub repositories with malicious CI/CD workflows
- **Webworm APT**: China-linked group using Discord and Microsoft Graph APIs to target European Union governments
- **KimWolf Operators**: DDoS-for-hire service administrators arrested for operating botnet affecting two million devices
- **ClickFix Attackers**: Large-scale campaign exploiting Ghost CMS vulnerabilities for social engineering
- **Laravel-Lang Attackers**: Sophisticated supply chain compromise targeting PHP development ecosystem
- **Packagist Attackers**: Coordinated campaign infecting 8 packages with Linux malware hosted on GitHub