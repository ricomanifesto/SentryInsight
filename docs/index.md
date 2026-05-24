# Exploitation Report

Current threat landscape reveals multiple active exploitation campaigns targeting critical vulnerabilities across enterprise systems and software supply chains. Notable active exploitation includes a maximum severity LiteSpeed cPanel Plugin vulnerability enabling root-level access, a zero-day in Trend Micro Apex One being exploited in the wild, and a critical Drupal Core SQL injection flaw now under attack. Simultaneously, sophisticated supply chain attacks have compromised Laravel Lang packages and multiple Packagist repositories, while coordinated campaigns target GitHub repositories through malicious CI/CD workflows.

## Active Exploitation Details

### LiteSpeed User-End cPanel Plugin Vulnerability
- **Description**: Maximum-severity security vulnerability in LiteSpeed User-End cPanel Plugin that allows attackers to execute scripts with root privileges
- **Impact**: Complete system compromise through root-level code execution
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2026-48172

### Trend Micro Apex One Zero-Day
- **Description**: Zero-day vulnerability in Trend Micro Apex One cybersecurity software targeting Windows systems
- **Impact**: Compromise of endpoint security solutions and potential system takeover
- **Status**: Actively exploited in attacks against Windows systems

### Drupal Core SQL Injection
- **Description**: Critical SQL injection vulnerability in Drupal Core content management system
- **Impact**: Database compromise, data exfiltration, and potential system takeover
- **Status**: Recently patched but now actively exploited, added to CISA KEV catalog

### Langflow Vulnerability
- **Description**: Security flaw in Langflow platform that has been exploited in the wild
- **Impact**: System compromise through the affected platform
- **Status**: Added to CISA Known Exploited Vulnerabilities catalog

## Affected Systems and Products

- **LiteSpeed User-End cPanel Plugin**: Web hosting control panel plugin with maximum severity vulnerability
- **Trend Micro Apex One**: Enterprise endpoint security software on Windows systems
- **Drupal Core**: Content management system installations vulnerable to SQL injection
- **Langflow Platform**: Development platform with exploited security flaws
- **Laravel Lang Packages**: PHP localization packages compromised in supply chain attack
- **Packagist Repositories**: Eight PHP packages infected with Linux malware
- **GitHub Repositories**: Over 5,500 repositories targeted with malicious CI/CD workflows
- **Ubiquiti UniFi OS**: Network management system with three maximum severity vulnerabilities
- **Cisco Secure Workload**: REST API vulnerability enabling unauthorized data access

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Compromise of legitimate software packages and repositories to distribute malware
- **Zero-Day Exploitation**: Active exploitation of previously unknown vulnerabilities in security products
- **SQL Injection**: Database compromise through malicious query injection in web applications
- **Malicious CI/CD Workflows**: Automated attacks targeting GitHub repositories through compromised continuous integration pipelines
- **Credential Theft**: Cross-platform malware designed to steal authentication credentials and sensitive data
- **Root Privilege Escalation**: Exploitation enabling attackers to gain administrative system access
- **GitHub Tag Abuse**: Manipulation of version control systems to distribute malicious code

## Threat Actor Activities

- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned threat actor targeting Ukrainian government entities using Prometheus phishing malware
- **Webworm**: China-linked advanced persistent threat group using Discord and Microsoft Graph APIs to target European Union government systems
- **Supply Chain Attackers**: Coordinated campaign operators targeting multiple package repositories with sophisticated malware distribution mechanisms
- **Megalodon Campaign**: Automated attack operation pushing over 5,700 malicious commits to GitHub repositories within six hours
- **Kimwolf Botnet Operator**: Canadian national arrested for operating DDoS botnet infecting nearly two million devices worldwide
- **First VPN Criminal Network**: Dismantled service used by 25 ransomware groups to obscure attack origins