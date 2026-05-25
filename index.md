# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms, with several high-severity flaws receiving immediate attention from security agencies. A Ghost CMS SQL injection vulnerability (CVE-2026-26980) is being exploited in large-scale ClickFix campaigns, while a maximum-severity LiteSpeed cPanel Plugin vulnerability (CVE-2026-48172) allows attackers to execute scripts with root privileges. CISA has added multiple vulnerabilities to its Known Exploited Vulnerabilities catalog, including a Drupal Core SQL injection bug and flaws in Trend Micro Apex One and Langflow. Supply chain attacks are proliferating across development ecosystems, targeting Laravel Lang packages, Packagist repositories, and GitHub repositories through automated campaigns.

## Active Exploitation Details

### Ghost CMS SQL Injection Vulnerability
- **Description**: Critical SQL injection vulnerability in Ghost CMS being exploited to inject malicious JavaScript code
- **Impact**: Enables ClickFix attack flows through malicious code injection
- **Status**: Currently being exploited in large-scale campaigns
- **CVE ID**: CVE-2026-26980

### LiteSpeed cPanel Plugin Vulnerability
- **Description**: Maximum-severity security vulnerability in LiteSpeed User-End cPanel Plugin
- **Impact**: Allows attackers to execute scripts with root privileges
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-48172

### Drupal Core SQL Injection
- **Description**: Critical SQL injection vulnerability in Drupal Core
- **Status**: Added to CISA KEV catalog due to active exploitation, recently patched

### Trend Micro Apex One Zero-Day
- **Description**: Zero-day vulnerability in Trend Micro Apex One security software
- **Impact**: Targets Windows systems
- **Status**: Actively exploited, now patched by Trend Micro

### Cisco Secure Workload REST API Flaw
- **Description**: Maximum-severity vulnerability in Cisco Secure Workload REST API
- **Impact**: Enables unauthenticated remote access to sensitive data
- **Status**: Recently patched
- **CVE ID**: CVE-2026-20223

## Affected Systems and Products

- **Ghost CMS**: Content management system affected by SQL injection vulnerability
- **LiteSpeed cPanel Plugin**: Web server plugin with root privilege escalation flaw
- **Drupal Core**: Popular content management framework with SQL injection vulnerability
- **Trend Micro Apex One**: Enterprise security software with zero-day exploitation
- **Cisco Secure Workload**: Network security platform with REST API vulnerability
- **Laravel Lang Packages**: PHP localization packages compromised in supply chain attack
- **Packagist Repositories**: Eight packages infected with Linux malware
- **Ubiquiti UniFi OS**: Three maximum severity vulnerabilities patched
- **Langflow Platform**: Added to CISA KEV catalog for active exploitation

## Attack Vectors and Techniques

- **SQL Injection**: Ghost CMS and Drupal Core vulnerabilities enable database manipulation and code injection
- **Supply Chain Poisoning**: Laravel Lang packages and Packagist repositories compromised to distribute credential-stealing malware
- **GitHub Repository Compromise**: Megalodon campaign targeting 5,561 repositories with malicious CI/CD workflows
- **Zero-Day Exploitation**: Trend Micro Apex One vulnerability exploited before patches were available
- **API Authentication Bypass**: Cisco Secure Workload flaw allows unauthenticated data access
- **ClickFix Social Engineering**: Ghost CMS exploits combined with social engineering techniques
- **Cross-Platform Malware**: Laravel-Lang attack delivers comprehensive credential-stealing framework

## Threat Actor Activities

- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned group targeting Ukrainian government entities using Prometheus phishing malware
- **China's Webworm**: APT group using Discord and Microsoft Graph APIs to compromise EU government systems, employing SOCKS proxies and SoftEther VPN for tunneling
- **Supply Chain Attackers**: Coordinated campaigns targeting multiple package repositories including Laravel Lang and Packagist ecosystems
- **Megalodon Campaign**: Automated GitHub attack pushing 5,718 malicious commits across thousands of repositories within six hours
- **Kimwolf Botnet Operator**: Canadian national arrested for operating DDoS-for-hire service infecting nearly two million devices worldwide
- **CINEMAGOAL Operators**: Italian authorities disrupted piracy ecosystem stealing streaming authentication codes from Netflix, Disney+, and Spotify