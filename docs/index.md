# Exploitation Report

Critical exploitation activity is currently dominated by several high-severity vulnerabilities being actively exploited in the wild. The most severe threats include a maximum-severity LiteSpeed cPanel Plugin vulnerability (CVE-2026-48172) allowing root-level script execution, a critical Drupal Core SQL injection vulnerability that has been added to CISA's Known Exploited Vulnerabilities catalog, and a zero-day vulnerability in Trend Micro Apex One targeting Windows systems. Additionally, multiple supply chain attacks have targeted PHP package repositories including Packagist and Laravel-Lang packages, while threat actors continue to leverage infrastructure takedowns and sophisticated attack vectors to compromise enterprise systems.

## Active Exploitation Details

### LiteSpeed cPanel Plugin Vulnerability
- **Description**: A maximum-severity security vulnerability in LiteSpeed User-End cPanel Plugin allowing unauthorized script execution
- **Impact**: Attackers can execute scripts with root privileges, providing complete system compromise
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2026-48172

### Drupal Core SQL Injection Vulnerability
- **Description**: A critical SQL injection flaw in Drupal Core that enables database manipulation and unauthorized access
- **Impact**: Attackers can extract sensitive data, modify database contents, and potentially gain administrative access
- **Status**: Recently patched but actively exploited, added to CISA KEV catalog
- **CVE ID**: Not specified in the articles

### Trend Micro Apex One Zero-Day
- **Description**: A zero-day vulnerability in Trend Micro's Apex One cybersecurity software targeting Windows systems
- **Impact**: Allows attackers to compromise endpoints running the security software
- **Status**: Zero-day vulnerability being actively exploited in attacks
- **CVE ID**: Not specified in the articles

### Langflow Vulnerability
- **Description**: A security flaw in Langflow that has been exploited in the wild
- **Impact**: Specific impact details not provided in the articles
- **Status**: Added to CISA KEV catalog due to active exploitation
- **CVE ID**: Not specified in the articles

### Cisco Secure Workload REST API Vulnerability
- **Description**: A maximum-severity flaw in Cisco Secure Workload REST API allowing unauthorized data access
- **Impact**: Unauthenticated remote attackers can access sensitive data
- **Status**: Patches released by Cisco
- **CVE ID**: CVE-2026-20223

## Affected Systems and Products

- **LiteSpeed User-End cPanel Plugin**: Web hosting control panel plugin with root execution capabilities
- **Drupal Core**: Content management system installations worldwide
- **Trend Micro Apex One**: Windows-based cybersecurity endpoints
- **Langflow**: Application development platform
- **Cisco Secure Workload**: Network security and monitoring infrastructure
- **Packagist PHP Packages**: Eight compromised packages containing Linux malware
- **Laravel-Lang PHP Packages**: Multiple compromised packages delivering credential stealers
- **Ubiquiti UniFi OS**: Three maximum severity vulnerabilities patched
- **GitHub Repositories**: 5,561 repositories targeted in Megalodon CI/CD campaign

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Coordinated attacks on PHP package repositories delivering malware through legitimate software distribution channels
- **SQL Injection Exploitation**: Active targeting of Drupal installations using critical database manipulation flaws
- **Zero-Day Exploitation**: Targeted attacks against Trend Micro security software using previously unknown vulnerabilities
- **CI/CD Pipeline Compromise**: Megalodon campaign pushing 5,718 malicious commits to GitHub repositories within six hours
- **REST API Exploitation**: Unauthenticated access to Cisco Secure Workload data through API vulnerabilities
- **Phishing Campaigns**: Prometheus-themed lures targeting Ukrainian government entities
- **Social Engineering**: Increased targeting of healthcare sector with evolved social engineering tactics

## Threat Actor Activities

- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned group targeting Ukrainian government organizations using Prometheus phishing malware and online learning platform lures
- **China's Webworm APT**: Advanced persistent threat group targeting EU governments using Discord and Microsoft Graph APIs with SOCKS proxies and SoftEther VPN tunneling tools
- **Supply Chain Attackers**: Coordinated campaign actors compromising multiple PHP package ecosystems with cross-platform credential stealers and Linux malware
- **Kimwolf Botnet Operator**: Canadian individual arrested for operating DDoS botnet infecting nearly two million devices worldwide
- **Megalodon Campaign Operators**: Automated attack campaign targeting thousands of GitHub repositories with malicious CI/CD workflows
- **Ransomware Groups**: 25 different ransomware organizations using dismantled First VPN service to obscure attack origins