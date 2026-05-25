# Exploitation Report

The current threat landscape is dominated by critical vulnerabilities being actively exploited across multiple platforms and systems. Most concerning is the widespread exploitation of CVE-2026-26980 in Ghost CMS, which has compromised over 700 websites through SQL injection attacks leading to ClickFix campaigns. Additionally, CVE-2026-48172 in LiteSpeed cPanel Plugin is being exploited to achieve root-level access, while a Drupal Core SQL injection vulnerability and a Trend Micro Apex One zero-day are under active attack. The exploitation activity is compounded by sophisticated supply chain attacks targeting npm, PyPI, and other package repositories, alongside persistent threats from advanced persistent threat groups like Lazarus and Ghostwriter conducting targeted campaigns against financial institutions and government entities.

## Active Exploitation Details

### Ghost CMS SQL Injection Vulnerability
- **Description**: Critical SQL injection flaw in Ghost CMS being exploited to inject malicious JavaScript code
- **Impact**: Attackers can compromise websites and redirect users to ClickFix attack flows, potentially leading to credential theft and malware installation
- **Status**: Actively exploited in large-scale campaign affecting 700+ sites
- **CVE ID**: CVE-2026-26980

### LiteSpeed cPanel Plugin Root Privilege Escalation
- **Description**: Maximum-severity security vulnerability in LiteSpeed User-End cPanel Plugin allowing script execution with root privileges
- **Impact**: Complete system compromise through root-level access, enabling attackers to take full control of affected systems
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-48172

### Drupal Core SQL Injection Vulnerability
- **Description**: Critical SQL injection flaw in Drupal Core that has been added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: Unauthorized database access, data exfiltration, and potential complete system compromise
- **Status**: Actively exploited and recognized by CISA as a significant threat

### Trend Micro Apex One Zero-Day
- **Description**: Zero-day vulnerability in Trend Micro Apex One security software targeting Windows systems
- **Impact**: Compromise of enterprise security infrastructure, potentially allowing attackers to disable protection mechanisms
- **Status**: Actively exploited in targeted attacks

## Affected Systems and Products

- **Ghost CMS**: Content management system vulnerable to SQL injection attacks affecting 700+ websites
- **LiteSpeed cPanel Plugin**: Web hosting control panel plugin with maximum severity vulnerability
- **Drupal Core**: Popular content management framework with critical SQL injection flaw
- **Trend Micro Apex One**: Enterprise security software affected by zero-day vulnerability
- **UniFi OS**: Three maximum severity vulnerabilities patched by Ubiquiti
- **npm, PyPI, CratesIO**: Package repositories targeted in TrapDoor supply chain attack campaign
- **Laravel-Lang PHP Packages**: Compromised to deliver cross-platform credential stealing malware
- **Packagist**: Eight packages infected with GitHub-hosted Linux malware

## Attack Vectors and Techniques

- **SQL Injection**: Primary attack vector for Ghost CMS and Drupal Core vulnerabilities, enabling database manipulation and code injection
- **ClickFix Campaigns**: Malicious JavaScript injection leading to fake error pages that trick users into downloading malware
- **Supply Chain Attacks**: Coordinated campaigns targeting multiple package repositories (npm, PyPI, CratesIO) to distribute credential-stealing malware
- **Memory-Only RAT Deployment**: Lazarus Group using RemotePE malware that operates entirely in memory to evade detection
- **OAuth Device Code Abuse**: Kali365 phishing service exploiting Microsoft 365 authentication mechanisms
- **Phishing-as-a-Service**: Organized platforms providing turnkey phishing solutions targeting enterprise accounts
- **Package Hijacking**: Attackers compromising legitimate packages to distribute malicious code through trusted repositories

## Threat Actor Activities

- **Lazarus Group**: North Korea-linked APT deploying RemotePE memory-only RAT against financial and cryptocurrency firms using cross-platform capabilities
- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned threat actor targeting Ukrainian government entities using Prometheus phishing lures
- **TrapDoor Campaign Operators**: Coordinated group conducting cross-ecosystem supply chain attacks across npm, PyPI, and CratesIO
- **Kali365 Operators**: Cybercriminals running phishing-as-a-service platform specifically targeting Microsoft 365 accounts
- **ClickFix Campaign Actors**: Threat actors leveraging Ghost CMS vulnerabilities to conduct large-scale social engineering attacks
- **Criminal VPN Infrastructure**: Dismantled network that supported 25 ransomware groups in obscuring attack origins
- **CINEMAGOAL Operators**: Italian-based piracy ecosystem stealing streaming service authentication codes