# Exploitation Report

Critical exploitation activity is currently targeting web platforms and supply chain components with multiple high-severity vulnerabilities under active attack. Threat actors are leveraging SQL injection flaws in popular content management systems, exploiting zero-day vulnerabilities in enterprise security products, and conducting sophisticated supply chain attacks across multiple package repositories. The most concerning activities include the exploitation of Ghost CMS and Drupal Core SQL injection vulnerabilities affecting hundreds of websites, a zero-day attack against Trend Micro Apex One security software, and coordinated supply chain compromises targeting npm, PyPI, and other developer repositories with credential-stealing malware.

## Active Exploitation Details

### Ghost CMS SQL Injection Vulnerability
- **Description**: Critical SQL injection vulnerability in Ghost CMS being exploited to inject malicious JavaScript code
- **Impact**: Attackers can hijack websites and launch ClickFix attacks against visitors, with over 700 sites reportedly compromised
- **Status**: Actively exploited in large-scale campaigns
- **CVE ID**: CVE-2026-26980

### Drupal Core SQL Injection Flaw
- **Description**: Highly critical SQL injection vulnerability in Drupal Core that allows remote code execution
- **Impact**: Attackers can gain unauthorized access to databases and execute arbitrary commands on affected systems
- **Status**: Added to CISA KEV catalog due to active exploitation
- **CVE ID**: Not specified in articles

### LiteSpeed cPanel Plugin Root Privilege Escalation
- **Description**: Maximum severity vulnerability in LiteSpeed User-End cPanel Plugin allowing arbitrary script execution
- **Impact**: Attackers can execute scripts with root privileges on affected web servers
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-48172

### Trend Micro Apex One Zero-Day
- **Description**: Zero-day vulnerability in Trend Micro Apex One security software
- **Impact**: Allows attackers to compromise Windows systems protected by the security solution
- **Status**: Actively exploited, patches have been released
- **CVE ID**: Not specified in articles

### Ubiquiti UniFi OS Critical Vulnerabilities
- **Description**: Three maximum severity vulnerabilities in UniFi OS affecting network management systems
- **Impact**: Remote attackers can exploit these flaws without authentication to compromise network infrastructure
- **Status**: Patches released by Ubiquiti
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **Ghost CMS**: Content management system with over 700 compromised sites
- **Drupal Core**: Popular web development framework used across enterprise and government sectors
- **LiteSpeed cPanel Plugin**: Web server control panel plugin for hosting environments
- **Trend Micro Apex One**: Enterprise endpoint security solution protecting Windows systems
- **Ubiquiti UniFi OS**: Network management platform for enterprise networking equipment
- **Laravel-Lang PHP Packages**: Localization packages for Laravel web framework
- **npm, PyPI, CratesIO**: Major software package repositories for JavaScript, Python, and Rust
- **Packagist**: PHP package repository with 8 compromised packages

## Attack Vectors and Techniques

- **SQL Injection Attacks**: Exploiting database vulnerabilities in web applications to inject malicious code and gain unauthorized access
- **ClickFix Social Engineering**: Using compromised websites to display fake error messages that trick users into executing malicious commands
- **Supply Chain Poisoning**: Compromising legitimate software packages with credential-stealing malware across multiple ecosystems
- **Zero-Day Exploitation**: Targeting previously unknown vulnerabilities in security products before patches are available
- **OAuth Device Code Abuse**: Exploiting Microsoft 365 authentication flows through phishing-as-a-service platforms
- **Memory-Only RAT Deployment**: Using fileless malware techniques to avoid detection while maintaining persistent access

## Threat Actor Activities

- **Lazarus Group**: North Korean APT deploying RemotePE memory-only RAT against financial and cryptocurrency organizations
- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned group targeting Ukrainian government entities with Prometheus-themed phishing campaigns
- **Kali365 Operators**: Cybercriminals running phishing-as-a-service platform specifically targeting Microsoft 365 accounts
- **TrapDoor Campaign**: Coordinated supply chain attackers distributing credential-stealing malware across npm, PyPI, and CratesIO repositories
- **First VPN Criminal Network**: Dismantled VPN service that facilitated operations for 25 different ransomware groups
- **Dutch Hosting Infrastructure**: Criminal hosting providers enabling cyberattacks and disinformation campaigns for Russian threat actors