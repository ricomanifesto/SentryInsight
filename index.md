# Exploitation Report

Critical exploitation activity continues to surge across multiple attack vectors, with several zero-day vulnerabilities being actively exploited in the wild. Most notably, a maximum-severity vulnerability in LiteSpeed cPanel Plugin (CVE-2026-48172) is under active exploitation, allowing attackers to execute scripts with root privileges. Additionally, threat actors are exploiting a critical SQL injection flaw in Ghost CMS (CVE-2026-26980) to conduct large-scale ClickFix campaigns affecting over 700 websites. The cybersecurity landscape is also witnessing sophisticated supply chain attacks targeting multiple package repositories including npm, PyPI, and CratesIO, while state-sponsored groups like Lazarus continue deploying advanced memory-only malware against financial institutions. A Trend Micro Apex One zero-day vulnerability is being exploited in attacks targeting Windows systems, and a recently patched Drupal Core SQL injection bug has been added to CISA's Known Exploited Vulnerabilities catalog.

## Active Exploitation Details

### LiteSpeed cPanel Plugin Vulnerability
- **Description**: A maximum-severity security vulnerability impacting LiteSpeed User-End cPanel Plugin that allows unauthorized script execution
- **Impact**: Attackers can run scripts as root, achieving complete system compromise
- **Status**: Currently under active exploitation in the wild
- **CVE ID**: CVE-2026-48172

### Ghost CMS SQL Injection Flaw
- **Description**: A critical SQL injection vulnerability in Ghost CMS being exploited to inject malicious JavaScript code
- **Impact**: Enables large-scale ClickFix attack campaigns, compromising over 700 websites
- **Status**: Actively exploited in coordinated campaigns
- **CVE ID**: CVE-2026-26980

### Trend Micro Apex One Zero-Day
- **Description**: A zero-day vulnerability in Trend Micro's Apex One security software
- **Impact**: Allows attackers to compromise Windows systems protected by the security solution
- **Status**: Currently being exploited in active attacks, patches have been released

### Drupal Core SQL Injection Vulnerability
- **Description**: A recently patched critical security flaw impacting Drupal Core
- **Impact**: SQL injection attacks allowing unauthorized database access and manipulation
- **Status**: Added to CISA KEV catalog due to active exploitation

## Affected Systems and Products

- **Ghost CMS**: Content management system affected by SQL injection vulnerability (CVE-2026-26980)
- **LiteSpeed cPanel Plugin**: Web server plugin vulnerable to root privilege escalation (CVE-2026-48172)
- **Trend Micro Apex One**: Security software with zero-day vulnerability affecting Windows systems
- **Drupal Core**: Popular content management framework with critical SQL injection flaw
- **Microsoft 365**: Targeted by Kali365 phishing-as-a-service platform via OAuth device code authentication
- **npm, PyPI, CratesIO**: Package repositories targeted in TrapDoor supply chain attacks
- **Laravel Lang Packages**: PHP localization packages compromised to deliver credential-stealing malware
- **Packagist**: PHP package repository affected by supply chain attacks targeting 8 packages
- **Ubiquiti UniFi OS**: Three maximum severity vulnerabilities patched, exploitable by remote attackers

## Attack Vectors and Techniques

- **ClickFix Attacks**: Malicious JavaScript injection through Ghost CMS exploitation to trigger social engineering campaigns
- **OAuth Device Code Abuse**: Kali365 phishing service exploits OAuth authentication to steal Microsoft 365 session tokens
- **Supply Chain Poisoning**: TrapDoor campaign distributes credential-stealing malware across multiple package ecosystems
- **Memory-Only Malware**: Lazarus Group deploys RemotePE cross-platform RAT that operates entirely in memory
- **Phishing-as-a-Service**: FBI warns of Kali365 platform providing turnkey phishing capabilities for Microsoft 365 targeting
- **GitHub CI/CD Exploitation**: Megalodon campaign targets 5,561 repositories with malicious CI/CD workflows
- **Root Privilege Escalation**: LiteSpeed plugin vulnerability allows direct root access on compromised systems

## Threat Actor Activities

- **Lazarus Group**: North Korea-linked APT deploying RemotePE memory-only RAT against financial and cryptocurrency firms
- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned threat actor targeting Ukrainian government entities with Prometheus-themed phishing campaigns
- **TrapDoor Operators**: Coordinated campaign operators spreading credential-stealing malware across npm, PyPI, and CratesIO repositories
- **ClickFix Campaign Actors**: Large-scale exploitation of Ghost CMS vulnerability affecting 700+ websites for social engineering attacks
- **Kali365 Operators**: Phishing-as-a-service providers facilitating Microsoft 365 account hijacking through OAuth abuse
- **Megalodon Campaign**: Automated attack targeting over 5,500 GitHub repositories with malicious CI/CD workflows in coordinated six-hour window