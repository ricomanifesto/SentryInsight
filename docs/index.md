# Exploitation Report

Multiple critical vulnerabilities are currently under active exploitation, with several maximum-severity flaws demanding immediate attention. The most concerning include a zero-day vulnerability in Trend Micro Apex One security software, a critical SQL injection flaw in Drupal Core that has been added to CISA's Known Exploited Vulnerabilities catalog, and a maximum-severity authentication bypass in LiteSpeed cPanel Plugin. Additionally, sophisticated supply chain attacks are targeting Laravel-Lang PHP packages and multiple Packagist repositories, while threat actors are leveraging compromised infrastructure and malicious CI/CD workflows to distribute credential-stealing malware across development environments.

## Active Exploitation Details

### Trend Micro Apex One Zero-Day Vulnerability
- **Description**: A zero-day vulnerability affecting Trend Micro Apex One security software that allows attackers to compromise Windows systems
- **Impact**: Enables attackers to gain unauthorized access and control over Windows systems protected by the security solution
- **Status**: Zero-day vulnerability actively exploited in the wild, patches have been released by Trend Micro

### Drupal Core SQL Injection Vulnerability
- **Description**: A critical SQL injection vulnerability in Drupal Core that allows attackers to execute arbitrary database queries
- **Impact**: Attackers can potentially access, modify, or delete sensitive database information and gain unauthorized system access
- **Status**: Recently patched but actively exploited, added to CISA KEV catalog

### LiteSpeed cPanel Plugin Authentication Bypass
- **Description**: A maximum-severity security vulnerability in the LiteSpeed User-End cPanel Plugin that allows unauthorized access
- **Impact**: Enables attackers to execute scripts with root privileges, leading to complete system compromise
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-48172

### Langflow Security Vulnerability
- **Description**: A security flaw affecting Langflow that is being actively exploited
- **Impact**: Allows attackers to compromise systems running the vulnerable Langflow software
- **Status**: Active exploitation confirmed, added to CISA KEV catalog

## Affected Systems and Products

- **Trend Micro Apex One**: Windows-based security software installations vulnerable to zero-day attacks
- **Drupal Core**: Web content management systems running vulnerable Drupal installations
- **LiteSpeed cPanel Plugin**: Web hosting environments using the LiteSpeed User-End cPanel Plugin
- **Laravel-Lang Packages**: PHP development environments using compromised Laravel localization packages
- **Packagist Repositories**: Eight packages on Packagist repository containing malicious Linux binaries
- **GitHub Repositories**: Over 5,500 GitHub repositories targeted by malicious CI/CD workflows
- **Langflow Software**: Systems running vulnerable Langflow installations
- **Ubiquiti UniFi OS**: Network management systems running vulnerable UniFi OS versions
- **Cisco Secure Workload**: Enterprise security platforms with REST API vulnerabilities

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Attackers compromising legitimate software packages to distribute malware through trusted development channels
- **Malicious CI/CD Workflows**: Automated campaigns pushing thousands of malicious commits to GitHub repositories within short timeframes
- **Credential Harvesting**: Cross-platform credential-stealing malware deployed through compromised packages
- **GitHub Tag Manipulation**: Abuse of GitHub version tags to distribute malicious payloads while maintaining appearance of legitimacy
- **Zero-Day Exploitation**: Active targeting of unpatched vulnerabilities in widely-used security software
- **SQL Injection Attacks**: Database manipulation through vulnerable web applications
- **Authentication Bypass**: Direct system access through plugin vulnerabilities leading to privilege escalation

## Threat Actor Activities

- **Megalodon Campaign**: Automated attack campaign that pushed 5,718 malicious commits to 5,561 GitHub repositories within six hours, demonstrating sophisticated automation capabilities
- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned threat actor targeting Ukrainian government entities using Prometheus phishing malware and online learning platform lures
- **Supply Chain Attackers**: Coordinated campaign targeting both Laravel-Lang packages and Packagist repositories, deploying cross-platform credential stealers
- **Webworm APT**: Chinese advanced persistent threat group using Discord and Microsoft Graph APIs to target European Union government organizations
- **Ransomware Infrastructure**: At least 25 ransomware groups utilizing criminal VPN services that have been dismantled by international law enforcement
- **Kimwolf Botnet Operator**: Canadian suspect arrested for operating distributed denial-of-service botnet that infected nearly two million devices worldwide