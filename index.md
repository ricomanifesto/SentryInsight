# Exploitation Report

Multiple critical vulnerabilities are currently under active exploitation, with threat actors leveraging SQL injection flaws, zero-day vulnerabilities, and sophisticated supply chain attacks to compromise enterprise systems. The most severe activity involves CVE-2026-26980 in Ghost CMS being exploited at scale to inject malicious JavaScript for ClickFix campaigns, while CVE-2026-48172 in LiteSpeed cPanel Plugin allows attackers to achieve root-level code execution. Additionally, a Trend Micro Apex One zero-day is being exploited in the wild, and Drupal Core SQL injection vulnerabilities have been added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation attempts.

## Active Exploitation Details

### Ghost CMS SQL Injection Vulnerability
- **Description**: Critical SQL injection flaw in Ghost CMS allowing attackers to inject malicious JavaScript code into websites
- **Impact**: Over 700 sites have been compromised and are being used for ClickFix attacks that trick users into executing malicious commands
- **Status**: Under active large-scale exploitation
- **CVE ID**: CVE-2026-26980

### LiteSpeed cPanel Plugin Vulnerability
- **Description**: Maximum-severity security flaw in LiteSpeed User-End cPanel Plugin allowing unauthorized code execution
- **Impact**: Attackers can run scripts with root privileges on affected systems
- **Status**: Currently being exploited in the wild
- **CVE ID**: CVE-2026-48172

### Trend Micro Apex One Zero-Day
- **Description**: Zero-day vulnerability in Trend Micro Apex One security software targeting Windows systems
- **Impact**: Allows attackers to compromise Windows-based security infrastructure
- **Status**: Actively exploited in attacks, patches have been released

### Drupal Core SQL Injection
- **Description**: Critical SQL injection vulnerability in Drupal Core that has been recently patched
- **Impact**: Enables database manipulation and potential full system compromise
- **Status**: Added to CISA KEV catalog due to active exploitation attempts

## Affected Systems and Products

- **Ghost CMS**: Content management system with over 700 compromised sites identified
- **LiteSpeed cPanel Plugin**: Web hosting control panel plugin with maximum severity vulnerability
- **Trend Micro Apex One**: Enterprise security software on Windows systems
- **Drupal Core**: Content management framework with widespread deployment
- **Microsoft 365**: Targeted by Kali365 phishing-as-a-service platform using OAuth abuse
- **npm, PyPI, CratesIO**: Package repositories affected by TrapDoor supply chain attacks
- **Laravel-Lang Packages**: PHP localization packages compromised with credential-stealing malware
- **Packagist Repository**: Eight packages infected with Linux malware via GitHub-hosted binaries
- **Ubiquiti UniFi OS**: Network management platform with three maximum severity vulnerabilities patched

## Attack Vectors and Techniques

- **SQL Injection Exploitation**: Direct database attacks through web application vulnerabilities
- **ClickFix Campaigns**: Social engineering attacks that trick users into executing malicious commands
- **OAuth Device Code Abuse**: Bypassing multi-factor authentication in Microsoft 365 environments
- **Supply Chain Attacks**: Compromising software packages across multiple ecosystems (npm, PyPI, Crates.io)
- **Memory-Only RAT Deployment**: RemotePE malware designed to operate entirely in system memory
- **CI/CD Pipeline Manipulation**: Megalodon campaign targeting 5,561 GitHub repositories with malicious workflows
- **Phishing-as-a-Service**: Kali365 platform providing turnkey phishing infrastructure

## Threat Actor Activities

- **Lazarus Group**: North Korean APT deploying RemotePE memory-only RAT against financial and cryptocurrency firms
- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned threat actor using Prometheus-themed lures to target Ukrainian government entities
- **TrapDoor Campaign Operators**: Coordinated group conducting cross-ecosystem supply chain attacks across npm, PyPI, and CratesIO
- **Ghost CMS Attackers**: Large-scale threat operation compromising 700+ websites for ClickFix campaigns
- **Megalodon Campaign**: Automated attack targeting thousands of GitHub repositories with malicious CI/CD workflows
- **Supply Chain Attackers**: Multiple groups targeting Laravel-Lang packages and Packagist repositories with credential-stealing malware