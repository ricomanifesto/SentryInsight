# Exploitation Report

The cybersecurity landscape is experiencing a surge of critical exploitation activity across multiple attack vectors. Most concerning are the active zero-day exploitations of Trend Micro Apex One security software and a maximum-severity vulnerability in LiteSpeed cPanel Plugin (CVE-2026-48172) that allows root-level script execution. Additionally, a critical SQL injection flaw in Drupal Core has been added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation attempts. The threat landscape is further complicated by sophisticated supply chain attacks targeting Laravel Lang packages and Packagist repositories, delivering cross-platform credential-stealing malware. Major infrastructure disruptions have occurred with the dismantling of criminal VPN services used by 25 ransomware groups and the seizure of 800 servers enabling cyberattacks.

## Active Exploitation Details

### LiteSpeed cPanel Plugin Vulnerability
- **Description**: A maximum-severity security vulnerability impacting LiteSpeed User-End cPanel Plugin that allows attackers to execute scripts with root privileges
- **Impact**: Complete system compromise through root-level script execution
- **Status**: Currently under active exploitation in the wild
- **CVE ID**: CVE-2026-48172

### Trend Micro Apex One Zero-Day
- **Description**: Zero-day vulnerability in Trend Micro's Apex One security software targeting Windows systems
- **Impact**: Compromise of endpoint security systems, potentially allowing attackers to bypass security controls
- **Status**: Actively exploited in attacks, patches have been released

### Drupal Core SQL Injection
- **Description**: Critical SQL injection vulnerability in Drupal Core that has been recently patched
- **Impact**: Database manipulation, potential data exfiltration, and system compromise
- **Status**: Added to CISA KEV catalog due to active exploitation attempts

### Langflow Vulnerability
- **Description**: Security flaw in Langflow application that has been exploited in the wild
- **Impact**: System compromise through application-level exploitation
- **Status**: Added to CISA KEV catalog, actively exploited

## Affected Systems and Products

- **LiteSpeed cPanel Plugin**: User-End cPanel Plugin installations vulnerable to root privilege escalation
- **Trend Micro Apex One**: Windows-based endpoint security installations
- **Drupal Core**: Web applications running vulnerable Drupal installations
- **Langflow**: Applications utilizing the Langflow platform
- **Laravel Lang Packages**: PHP development environments using compromised localization packages
- **Packagist Repositories**: Eight compromised packages containing Linux malware
- **Ubiquiti UniFi OS**: Three maximum severity vulnerabilities patched (no active exploitation reported)
- **Cisco Secure Workload**: REST API vulnerability allowing unauthorized data access

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Compromise of Laravel Lang packages and Packagist repositories to deliver credential-stealing malware
- **GitHub Repository Poisoning**: Megalodon campaign targeting 5,561 repositories with malicious CI/CD workflows
- **SQL Injection**: Direct database exploitation through Drupal Core vulnerabilities
- **Zero-Day Exploitation**: Direct targeting of unpatched Trend Micro security software
- **Privilege Escalation**: Root-level access through LiteSpeed cPanel Plugin exploitation
- **Social Engineering**: Belarus-aligned Ghostwriter using Prometheus phishing lures against Ukrainian government entities

## Threat Actor Activities

- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned threat actor targeting Ukrainian government entities using Prometheus-themed phishing campaigns
- **China's Webworm APT**: Utilizing Discord and Microsoft Graph APIs to compromise European Union government systems, employing SOCKS proxies and tunneling tools
- **Kimwolf Botnet Operator**: Canadian national arrested for operating DDoS botnet affecting nearly two million devices worldwide
- **Supply Chain Attackers**: Coordinated campaign targeting multiple PHP package repositories with cross-platform credential stealers
- **Ransomware Groups**: 25 different ransomware organizations disrupted following the takedown of criminal VPN services
- **Criminal Hosting Providers**: Netherlands operation resulted in seizure of 800 servers enabling various cyberattacks and disinformation campaigns