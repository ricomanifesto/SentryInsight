# Exploitation Report

Critical exploitation activity is currently underway involving multiple zero-day vulnerabilities and actively exploited flaws across enterprise infrastructure. China-linked threat actors are exploiting zero-day vulnerabilities in Sitecore content management systems and Cisco AsyncOS software to target critical infrastructure and secure email gateways in North America. Additionally, attackers are actively exploiting a maximum-severity authentication bypass flaw in the WordPress Modular DS plugin and a critical Fortinet FortiSIEM vulnerability. These attacks demonstrate sophisticated targeting of enterprise systems with publicly available exploit code enabling widespread exploitation campaigns.

## Active Exploitation Details

### Sitecore Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Sitecore content management system being exploited for initial access into critical infrastructure systems
- **Impact**: Allows threat actors to gain initial foothold in critical infrastructure networks in North America
- **Status**: Currently being exploited by China-linked APT group UAT-8837; patch status not specified in source

### Cisco AsyncOS Zero-Day RCE
- **Description**: Maximum-severity remote code execution vulnerability in Cisco AsyncOS Software for Secure Email Gateway and Secure Email and Web Manager appliances
- **Impact**: Complete system compromise of email security infrastructure
- **Status**: Actively exploited since November 2025, recently patched by Cisco in January 2026

### WordPress Modular DS Plugin Authentication Bypass
- **Description**: Maximum-severity authentication bypass vulnerability allowing remote attackers to gain administrative access
- **Impact**: Complete takeover of WordPress sites with admin-level privileges
- **Status**: Currently under active exploitation in the wild
- **CVE ID**: CVE-2026-23550

### Fortinet FortiSIEM Critical Vulnerability
- **Description**: Critical vulnerability in Fortinet FortiSIEM security information and event management platform
- **Impact**: System compromise of security monitoring infrastructure
- **Status**: Currently being exploited with publicly available proof-of-concept exploit code

## Affected Systems and Products

- **Sitecore Content Management System**: Critical infrastructure organizations in North America
- **Cisco AsyncOS Software**: Secure Email Gateway (SEG) appliances and Secure Email and Web Manager systems
- **WordPress Modular DS Plugin**: WordPress websites using the vulnerable plugin
- **Fortinet FortiSIEM**: Security information and event management deployments
- **Google Chrome Extensions**: Malicious extensions impersonating Workday and NetSuite platforms

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise systems
- **Spear Phishing**: Venezuela-themed lures targeting U.S. government and policy entities
- **Browser Extension Hijacking**: Malicious Chrome extensions masquerading as legitimate HR and ERP platforms
- **Supply Chain Targeting**: Misconfiguration attacks targeting AWS CodeBuild and GitHub repositories
- **Authentication Bypass**: Remote exploitation of plugin vulnerabilities to gain administrative access

## Threat Actor Activities

- **UAT-8837 (China-linked APT)**: Targeting critical infrastructure systems in North America using Sitecore zero-day vulnerabilities and focusing on long-term persistent access
- **China-linked APT Groups**: Exploiting Cisco AsyncOS zero-day in email gateway infrastructure since November 2025, demonstrating sophisticated email security targeting
- **LOTUSLITE Campaign Operators**: Targeting U.S. government and policy entities using politically themed spear phishing with Venezuela-related lures to deliver backdoor malware
- **Gootloader Operators**: Enhanced evasion techniques using malformed ZIP archives split into up to 1,000 parts for initial access delivery