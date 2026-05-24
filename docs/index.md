# Exploitation Report

Critical exploitation activity continues to escalate across multiple platforms, with several maximum-severity vulnerabilities actively exploited in the wild. The most concerning developments include active exploitation of **CVE-2026-48172** in LiteSpeed cPanel Plugin with a CVSS score of 10.0, allowing attackers to execute scripts as root. Additionally, a Drupal Core SQL injection vulnerability has been added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation attempts. Supply chain attacks have intensified with sophisticated campaigns targeting Laravel Lang packages and Packagist repositories, delivering cross-platform credential-stealing malware. Zero-day exploitation has been confirmed in Trend Micro Apex One security software, while coordinated attacks have compromised thousands of GitHub repositories through malicious CI/CD workflows.

## Active Exploitation Details

### LiteSpeed cPanel Plugin Root Privilege Escalation
- **Description**: A maximum-severity vulnerability in LiteSpeed User-End cPanel Plugin that enables remote code execution
- **Impact**: Attackers can execute arbitrary scripts with root privileges, leading to complete system compromise
- **Status**: Actively exploited in the wild, patches available
- **CVE ID**: CVE-2026-48172

### Drupal Core SQL Injection Vulnerability
- **Description**: A critical SQL injection flaw in Drupal Core affecting the content management system
- **Impact**: Allows attackers to execute arbitrary SQL queries, potentially leading to data theft and system compromise
- **Status**: Recently patched but actively exploited, added to CISA KEV catalog

### Trend Micro Apex One Zero-Day
- **Description**: An undisclosed zero-day vulnerability in Trend Micro's Apex One security platform
- **Impact**: Enables attackers to compromise Windows systems protected by the security software
- **Status**: Actively exploited in attacks, patches released by Trend Micro

### Langflow Vulnerability
- **Description**: A security flaw impacting the Langflow platform
- **Impact**: Allows unauthorized access and potential system compromise
- **Status**: Added to CISA KEV catalog due to active exploitation

### Cisco Secure Workload REST API Vulnerability
- **Description**: A maximum-severity authentication bypass flaw in Cisco Secure Workload REST API
- **Impact**: Enables unauthenticated remote attackers to access sensitive data
- **Status**: Recently patched with updates available
- **CVE ID**: CVE-2026-20223

## Affected Systems and Products

- **LiteSpeed cPanel Plugin**: Web hosting control panel environments running vulnerable plugin versions
- **Drupal Core**: Content management systems across various hosting platforms and enterprises
- **Trend Micro Apex One**: Windows endpoint security deployments in enterprise environments
- **Laravel Lang Packages**: PHP development environments using compromised localization packages
- **Packagist Repositories**: PHP package management systems with infected packages
- **Cisco Secure Workload**: Network security and workload protection platforms
- **GitHub Repositories**: Development environments with compromised CI/CD workflows
- **Ubiquiti UniFi OS**: Network infrastructure management systems
- **npm Packages**: JavaScript development environments and package repositories

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Attackers compromising legitimate packages in Laravel Lang and Packagist repositories to distribute credential-stealing malware
- **GitHub Tag Abuse**: Exploitation of GitHub version tagging systems to distribute malicious payloads through legitimate-appearing releases
- **CI/CD Workflow Manipulation**: Mass compromise of GitHub repositories through automated injection of malicious CI/CD workflows
- **Malicious Binary Hosting**: Use of GitHub Releases to host and distribute Linux malware binaries
- **Authentication Bypass**: Exploitation of REST API vulnerabilities to gain unauthorized access to sensitive systems
- **Root Privilege Escalation**: Direct escalation to root-level access through vulnerable cPanel plugins
- **SQL Injection**: Database manipulation and data exfiltration through Drupal Core vulnerabilities

## Threat Actor Activities

- **Laravel Lang Attackers**: Sophisticated supply chain campaign targeting PHP developers with cross-platform credential-stealing malware delivered through compromised localization packages
- **Megalodon Campaign**: Automated attack targeting 5,561 GitHub repositories with 5,718 malicious commits deployed within a six-hour window
- **Packagist Attackers**: Coordinated campaign infecting eight packages with Linux malware hosted on GitHub infrastructure
- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned threat actor targeting Ukrainian government entities using Prometheus phishing malware and online learning platform lures
- **Webworm APT**: Chinese advanced persistent threat group leveraging Discord and Microsoft Graph APIs to compromise European government systems
- **Kimwolf Botnet Operator**: Canadian cybercriminal operating distributed denial-of-service botnet affecting nearly two million devices worldwide
- **First VPN Criminal Network**: Criminal VPN service used by 25 ransomware groups to obscure attack origins, recently dismantled by international law enforcement