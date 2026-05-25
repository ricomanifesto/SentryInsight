# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and software systems through various attack vectors. Threat actors are actively exploiting vulnerabilities in content management systems, web hosting infrastructure, and supply chain components. Most concerning are the ongoing exploits of Ghost CMS SQL injection vulnerabilities affecting over 700 websites, zero-day attacks against Trend Micro Apex One security software, and a maximum-severity LiteSpeed cPanel plugin flaw enabling root-level access. Additionally, sophisticated supply chain attacks have compromised multiple package repositories including npm, PyPI, and Packagist, while state-sponsored groups continue targeted campaigns against financial institutions and government entities.

## Active Exploitation Details

### Ghost CMS SQL Injection Vulnerability
- **Description**: Critical SQL injection vulnerability in Ghost CMS being exploited to inject malicious JavaScript code
- **Impact**: Attackers can hijack websites and launch ClickFix attack campaigns affecting over 700 sites
- **Status**: Actively exploited in large-scale campaigns
- **CVE ID**: CVE-2026-26980

### Trend Micro Apex One Zero-Day
- **Description**: Zero-day vulnerability in Trend Micro Apex One security software
- **Impact**: Attackers can compromise Windows systems protected by the security solution
- **Status**: Actively exploited in the wild, patches have been released

### LiteSpeed cPanel Plugin Root Execution Flaw
- **Description**: Maximum-severity vulnerability allowing unauthorized script execution with root privileges
- **Impact**: Complete system compromise and administrative access
- **Status**: Under active exploitation
- **CVE ID**: CVE-2026-48172

### Drupal Core SQL Injection Bug
- **Description**: Critical SQL injection vulnerability in Drupal Core that allows database manipulation
- **Impact**: Remote code execution and complete site compromise
- **Status**: Added to CISA KEV catalog due to active exploitation

### Ubiquiti UniFi OS Vulnerabilities
- **Description**: Three maximum severity vulnerabilities in UniFi OS
- **Impact**: Remote attackers can gain unauthorized access without authentication
- **Status**: Patches released, exploitation potential remains high

## Affected Systems and Products

- **Ghost CMS**: Content management system with over 700 confirmed compromised sites
- **Trend Micro Apex One**: Enterprise endpoint security solution on Windows systems
- **LiteSpeed Technologies**: cPanel plugin used in web hosting environments
- **Drupal Core**: Content management framework powering numerous websites
- **Laravel-Lang Packages**: PHP localization packages in the Laravel ecosystem
- **npm, PyPI, Crates.io**: Major package repositories for JavaScript, Python, and Rust
- **Packagist**: PHP package repository with 8 confirmed malicious packages
- **Ubiquiti UniFi OS**: Network management platform for enterprise environments

## Attack Vectors and Techniques

- **SQL Injection**: Primary attack method for Ghost CMS and Drupal exploits enabling database manipulation
- **ClickFix Campaigns**: Social engineering technique combining malicious JavaScript injection with user deception
- **Supply Chain Poisoning**: Coordinated attacks across multiple package repositories (TrapDoor campaign)
- **OAuth Device Code Abuse**: Kali365 phishing service exploiting Microsoft 365 authentication flows
- **Memory-Only RAT Deployment**: RemotePE malware operating entirely in memory to evade detection
- **CI/CD Pipeline Compromise**: Megalodon campaign targeting 5,561 GitHub repositories through malicious workflows
- **Version Tag Manipulation**: Laravel-Lang attack using GitHub release mechanisms for malware distribution

## Threat Actor Activities

- **Lazarus Group**: North Korean APT deploying RemotePE cross-platform malware against financial and cryptocurrency firms
- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned group targeting Ukrainian government entities with Prometheus-themed phishing campaigns
- **TrapDoor Campaign Operators**: Coordinated supply chain attackers targeting npm, PyPI, and Crates.io with credential-stealing malware
- **Russian Cyber Operations**: Utilizing compromised Dutch hosting infrastructure (800 seized servers) for cyberattacks and influence operations
- **Ransomware Groups**: 25 different ransomware organizations using dismantled First VPN service for attack obfuscation
- **Kali365 Operators**: Phishing-as-a-Service platform specifically targeting Microsoft 365 environments through OAuth exploitation