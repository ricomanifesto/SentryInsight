# Exploitation Report

Critical security vulnerabilities across content management systems, enterprise security platforms, and software supply chains are facing active exploitation by threat actors. The most severe incidents involve a Ghost CMS SQL injection vulnerability being exploited at scale for ClickFix attacks, multiple zero-day vulnerabilities in security products including Trend Micro Apex One and LiteSpeed cPanel Plugin, and a Drupal Core SQL injection flaw that has been added to CISA's Known Exploited Vulnerabilities catalog. Simultaneously, sophisticated supply chain attacks are compromising developer ecosystems through malicious packages on npm, PyPI, and other repositories, while North Korean threat actors deploy advanced memory-only malware against financial institutions.

## Active Exploitation Details

### Ghost CMS SQL Injection Vulnerability
- **Description**: A critical SQL injection vulnerability in Ghost CMS enabling attackers to inject malicious JavaScript code
- **Impact**: Over 700 websites compromised and used to launch ClickFix attacks against users
- **Status**: Under active large-scale exploitation
- **CVE ID**: CVE-2026-26980

### LiteSpeed cPanel Plugin Root Privilege Escalation
- **Description**: A maximum-severity security vulnerability in LiteSpeed User-End cPanel Plugin allowing script execution
- **Impact**: Attackers can execute scripts with root privileges, achieving complete system compromise
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-48172

### Drupal Core SQL Injection Vulnerability
- **Description**: A critical SQL injection flaw in Drupal Core that allows unauthorized database access
- **Impact**: Potential data theft, website compromise, and unauthorized administrative access
- **Status**: Added to CISA KEV catalog due to confirmed active exploitation
- **CVE ID**: Not specified in source articles

### Trend Micro Apex One Zero-Day
- **Description**: A zero-day vulnerability in Trend Micro's Apex One security platform targeting Windows systems
- **Impact**: Compromise of enterprise security infrastructure and potential lateral movement
- **Status**: Zero-day vulnerability under active exploitation
- **CVE ID**: Not specified in source articles

## Affected Systems and Products

- **Ghost CMS**: Content management system with over 700 compromised websites
- **LiteSpeed cPanel Plugin**: Web hosting control panel plugin with root access capabilities
- **Drupal Core**: Content management framework with widespread deployment
- **Trend Micro Apex One**: Enterprise endpoint security platform on Windows systems
- **Ubiquiti UniFi OS**: Network management platform with three maximum severity vulnerabilities
- **npm, PyPI, CratesIO**: Software package repositories targeted by supply chain attacks
- **Laravel-Lang PHP Packages**: Localization packages compromised for credential theft
- **Packagist**: PHP package repository with eight infected packages

## Attack Vectors and Techniques

- **SQL Injection**: Primary attack vector for Ghost CMS and Drupal Core compromises enabling database manipulation
- **ClickFix Attacks**: Malicious JavaScript injection through compromised CMS platforms to deceive users
- **Supply Chain Poisoning**: Malicious package injection across multiple developer ecosystems
- **Zero-Day Exploitation**: Direct targeting of unpatched vulnerabilities in security products
- **Memory-Only Malware**: RemotePE RAT deployment without disk persistence for stealth operations
- **OAuth Device Code Abuse**: Kali365 phishing service exploiting Microsoft 365 authentication flows
- **Privilege Escalation**: Root-level access through cPanel plugin vulnerabilities

## Threat Actor Activities

- **Lazarus Group**: North Korean APT deploying RemotePE memory-only RAT against financial and cryptocurrency firms
- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned group targeting Ukrainian government entities with Prometheus phishing campaigns
- **TrapDoor Campaign**: Cross-platform supply chain attackers targeting npm, PyPI, and CratesIO with credential-stealing malware
- **Kali365 Operators**: Phishing-as-a-Service platform operators targeting Microsoft 365 accounts through OAuth abuse
- **ClickFix Attackers**: Large-scale campaign operators exploiting Ghost CMS vulnerabilities for malicious JavaScript injection
- **Criminal VPN Networks**: Infrastructure providers supporting 25 ransomware groups before law enforcement takedown