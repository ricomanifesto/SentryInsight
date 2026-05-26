# Exploitation Report

This week has seen a surge in critical vulnerability exploitation across multiple platforms, with threat actors actively targeting content management systems, enterprise security tools, and software supply chains. The most alarming activities include active exploitation of a Ghost CMS SQL injection vulnerability affecting over 700 websites, zero-day attacks against Trend Micro's Apex One security platform, and sophisticated supply chain compromises across multiple package repositories. Critical infrastructure components including Drupal Core, LiteSpeed cPanel plugins, and Ubiquiti UniFi OS have also come under active attack, demonstrating the broad scope of current threat activity.

## Active Exploitation Details

### Ghost CMS SQL Injection Vulnerability
- **Description**: Critical SQL injection flaw in Ghost CMS allowing remote code execution through malicious JavaScript injection
- **Impact**: Attackers can hijack websites to deploy ClickFix attack campaigns, leading to credential theft and malware distribution
- **Status**: Actively exploited in large-scale campaigns affecting 700+ websites
- **CVE ID**: CVE-2026-26980

### Trend Micro Apex One Zero-Day
- **Description**: Zero-day vulnerability in Trend Micro's Apex One endpoint security platform targeting Windows systems
- **Impact**: Enables attackers to compromise enterprise security infrastructure and bypass protection mechanisms
- **Status**: Actively exploited in the wild, patches recently released

### LiteSpeed cPanel Plugin Critical Flaw
- **Description**: Maximum severity security vulnerability allowing unauthorized script execution with root privileges
- **Impact**: Complete system compromise with administrative access to web hosting environments
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-48172

### Drupal Core SQL Injection
- **Description**: Highly critical SQL injection vulnerability in Drupal Core affecting content management functionality
- **Impact**: Remote code execution and complete site compromise
- **Status**: Added to CISA KEV catalog due to active exploitation attempts

## Affected Systems and Products

- **Ghost CMS**: All versions prior to security update, affecting content management platforms
- **Trend Micro Apex One**: Windows-based endpoint security deployments
- **LiteSpeed User-End cPanel Plugin**: Web hosting control panels with LiteSpeed integration
- **Drupal Core**: Content management systems running vulnerable Drupal versions
- **Ubiquiti UniFi OS**: Network infrastructure management platforms
- **Laravel-Lang PHP Packages**: Development frameworks using compromised localization packages
- **npm, PyPI, and CratesIO**: Software repositories affected by TrapDoor supply chain attacks
- **Packagist**: PHP package repository with eight compromised packages

## Attack Vectors and Techniques

- **SQL Injection Exploitation**: Direct database manipulation through web application vulnerabilities
- **ClickFix Social Engineering**: JavaScript-based attacks tricking users into executing malicious code
- **Supply Chain Poisoning**: Compromising legitimate software packages with credential-stealing malware
- **Zero-Day Exploitation**: Targeting unpatched vulnerabilities in security products
- **OAuth Device Code Abuse**: Bypassing multi-factor authentication through Kali365 phishing service
- **Memory-Only Malware Deployment**: RemotePE RAT operating exclusively in system memory
- **Package Repository Hijacking**: Abusing GitHub version tags to distribute malicious code

## Threat Actor Activities

- **Lazarus Group**: Deploying RemotePE memory-only RAT against financial and cryptocurrency firms using cross-platform malware
- **TrapDoor Campaign**: Coordinated cross-ecosystem supply chain attack targeting npm, PyPI, and CratesIO with credential-stealing malware
- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned group targeting Ukrainian government entities using Prometheus phishing lures
- **Ghost CMS Attackers**: Large-scale exploitation campaign affecting 700+ websites for ClickFix attack distribution
- **Laravel-Lang Compromisers**: Sophisticated supply chain attack targeting PHP development frameworks
- **Kali365 Operators**: Phishing-as-a-Service platform specifically targeting Microsoft 365 accounts through OAuth abuse