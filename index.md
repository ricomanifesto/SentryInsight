# Exploitation Report

Critical exploitation activity is currently centered around several high-severity vulnerabilities being actively exploited in the wild. The most severe incidents include a zero-day vulnerability in Trend Micro Apex One being exploited in targeted attacks, a maximum-severity LiteSpeed cPanel Plugin flaw allowing root-level script execution, and widespread exploitation of Ghost CMS and Drupal Core SQL injection vulnerabilities. Additionally, sophisticated supply chain attacks are targeting multiple package managers including npm, PyPI, and Laravel-Lang packages, while the Lazarus Group continues deploying advanced memory-only malware against financial institutions.

## Active Exploitation Details

### Trend Micro Apex One Zero-Day Vulnerability
- **Description**: An actively exploited zero-day vulnerability in Trend Micro's Apex One cybersecurity software targeting Windows systems
- **Impact**: Allows attackers to compromise Windows systems protected by Apex One security software
- **Status**: Zero-day vulnerability with active exploitation confirmed; patches have been released

### LiteSpeed cPanel Plugin Critical Vulnerability
- **Description**: A maximum-severity security vulnerability in LiteSpeed User-End cPanel Plugin
- **Impact**: Enables attackers to execute scripts with root privileges on affected systems
- **Status**: Currently under active exploitation in the wild
- **CVE ID**: CVE-2026-48172

### Ghost CMS SQL Injection Vulnerability
- **Description**: Critical SQL injection vulnerability in Ghost CMS being exploited to inject malicious JavaScript code
- **Impact**: Allows attackers to hijack websites and launch ClickFix attack campaigns targeting over 700 sites
- **Status**: Under active exploitation in large-scale campaigns
- **CVE ID**: CVE-2026-26980

### Drupal Core SQL Injection Vulnerability
- **Description**: Critical SQL injection vulnerability in Drupal Core that was recently patched
- **Impact**: Allows unauthorized database access and potential site compromise
- **Status**: Added to CISA KEV catalog due to confirmed active exploitation

## Affected Systems and Products

- **Ghost CMS**: Content management system vulnerable to SQL injection attacks affecting 700+ sites
- **Trend Micro Apex One**: Cybersecurity software for Windows environments experiencing zero-day exploitation
- **LiteSpeed cPanel Plugin**: Web hosting control panel plugin with root privilege escalation
- **Drupal Core**: Open-source content management framework with SQL injection vulnerability
- **npm, PyPI, CratesIO Packages**: Software package repositories targeted in TrapDoor supply chain attacks
- **Laravel-Lang PHP Packages**: Localization packages compromised to deliver credential-stealing malware
- **Packagist Packages**: Eight PHP packages infected with Linux malware hosted on GitHub
- **Ubiquiti UniFi OS**: Network management platform with three maximum severity vulnerabilities

## Attack Vectors and Techniques

- **SQL Injection Attacks**: Exploitation of database vulnerabilities in Ghost CMS and Drupal Core to inject malicious code
- **ClickFix Campaigns**: JavaScript injection techniques used to trigger malicious download flows on compromised websites
- **Supply Chain Poisoning**: Coordinated attacks across multiple package managers (npm, PyPI, CratesIO) to distribute malware
- **Memory-Only Malware**: RemotePE RAT deployment by Lazarus Group using fileless persistence techniques
- **OAuth Device Code Abuse**: Kali365 phishing service exploiting Microsoft 365 authentication mechanisms
- **Package Version Manipulation**: Abuse of GitHub version tags to distribute malicious updates through legitimate packages
- **Zero-Day Exploitation**: Direct targeting of unpatched vulnerabilities in security software

## Threat Actor Activities

- **Lazarus Group**: North Korea-linked APT deploying RemotePE memory-only RAT against financial and cryptocurrency firms using cross-platform malware capabilities
- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned threat actor targeting Ukrainian government entities with Prometheus phishing malware campaigns
- **TrapDoor Campaign Operators**: Coordinated attackers conducting cross-ecosystem supply chain attacks spanning npm, PyPI, and Crates.io to distribute credential-stealing malware
- **Kali365 Service Operators**: Phishing-as-a-Service platform operators targeting Microsoft 365 accounts through OAuth exploitation
- **ClickFix Campaign Actors**: Large-scale operators exploiting Ghost CMS vulnerabilities to inject malicious JavaScript across hundreds of compromised websites