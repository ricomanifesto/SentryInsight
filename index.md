# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms, with threat actors targeting content management systems, hosting infrastructure, and software supply chains. The most significant activity involves CVE-2026-26980 in Ghost CMS being exploited for large-scale ClickFix attacks affecting over 700 websites, CVE-2026-48172 in LiteSpeed cPanel Plugin enabling root-level script execution, and a Drupal SQL injection vulnerability that prompted CISA to add it to their Known Exploited Vulnerabilities catalog. Additional exploitation includes a zero-day vulnerability in KnowledgeDeliver LMS and coordinated supply chain attacks targeting npm, PyPI, and Packagist repositories to distribute credential-stealing malware.

## Active Exploitation Details

### Ghost CMS SQL Injection Vulnerability
- **Description**: Critical SQL injection flaw in Ghost CMS allowing attackers to inject malicious JavaScript code into websites
- **Impact**: Over 700 websites compromised to serve ClickFix attack flows targeting users with fake update prompts
- **Status**: Recently disclosed and being actively exploited in large-scale campaigns
- **CVE ID**: CVE-2026-26980

### LiteSpeed cPanel Plugin Root Execution Flaw
- **Description**: Maximum-severity vulnerability in LiteSpeed User-End cPanel Plugin allowing unauthorized script execution with root privileges
- **Impact**: Attackers can achieve complete system compromise with administrative access
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-48172

### Drupal Core SQL Injection Vulnerability
- **Description**: Critical SQL injection vulnerability in Drupal content management system core
- **Impact**: Allows attackers to execute arbitrary SQL commands and potentially compromise entire websites
- **Status**: Added to CISA Known Exploited Vulnerabilities catalog due to active exploitation, federal agencies given 48-hour patching deadline

### KnowledgeDeliver LMS Zero-Day
- **Description**: High-severity security flaw in Digital Knowledge KnowledgeDeliver Learning Management System popular in Japan
- **Impact**: Exploited to deploy Godzilla web shell and Cobalt Strike beacons for persistent access
- **Status**: Was exploited as zero-day before being patched, now fixed

## Affected Systems and Products

- **Ghost CMS**: Content management system with over 700 compromised websites
- **LiteSpeed cPanel Plugin**: Web server plugin affecting hosting environments
- **Drupal Core**: Content management system used by government and enterprise organizations
- **KnowledgeDeliver LMS**: Learning management system popular in Japanese organizations
- **npm, PyPI, CratesIO**: Software package repositories targeted in supply chain attacks
- **Laravel Lang packages**: PHP localization packages compromised via GitHub version tags
- **Packagist**: PHP package repository with 8 infected packages containing Linux malware

## Attack Vectors and Techniques

- **SQL Injection**: Primary vector for Ghost CMS and Drupal exploitation enabling database manipulation
- **ClickFix Campaigns**: Social engineering technique using fake update prompts to trick users into downloading malware
- **Supply Chain Poisoning**: Compromise of legitimate software packages to distribute credential-stealing malware
- **GitHub Tag Abuse**: Manipulation of version control tags to distribute malicious code through trusted repositories
- **Phishing and SEO Poisoning**: Used by Iranian actors to distribute MiniFast and MiniJunk V2 malware
- **OAuth Device Code Authentication Abuse**: Kali365 phishing service bypassing multi-factor authentication for Microsoft 365 accounts

## Threat Actor Activities

- **Iranian Nimbus Manticore Group**: Conducting campaigns using aviation industry lures to deploy MiniFast and MiniJunk V2 malware via phishing and SEO poisoning
- **North Korean Lazarus Group**: Deploying RemotePE memory-only RAT against financial and cryptocurrency firms with cross-platform capabilities
- **ShinyHunters Extortion Gang**: Compromised 7-Eleven systems exposing personal information of over 183,000 individuals
- **Belarus-aligned Ghostwriter**: Targeting Ukrainian government entities with Prometheus phishing malware impersonating educational platforms
- **TrapDoor Campaign Operators**: Coordinating cross-ecosystem supply chain attacks across npm, PyPI, and CratesIO to distribute credential stealers
- **Criminal VPN Operators**: First VPN service dismantled by international law enforcement after being used by 25 ransomware groups
- **Dutch Hosting Infrastructure**: 800 servers seized from hosting companies enabling Russian cyberattacks and influence operations