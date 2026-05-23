# Exploitation Report

Critical zero-day and recently patched vulnerabilities are currently under active exploitation, highlighting significant risks to enterprise infrastructure. The most severe threats include a maximum-severity LiteSpeed cPanel Plugin vulnerability (CVE-2026-48172) enabling root-level script execution, a critical Drupal Core SQL injection flaw that has been added to CISA's Known Exploited Vulnerabilities catalog, and a Trend Micro Apex One zero-day affecting Windows systems. Supply chain attacks have also intensified with the compromise of Laravel-Lang PHP packages delivering credential-stealing malware and the massive Megalodon campaign targeting over 5,500 GitHub repositories. Additionally, sophisticated threat actors including the Belarus-aligned Ghostwriter group and China's Webworm APT are conducting targeted campaigns against government entities using advanced techniques.

## Active Exploitation Details

### LiteSpeed cPanel Plugin Vulnerability
- **Description**: A maximum-severity security vulnerability affecting LiteSpeed User-End cPanel Plugin that allows attackers to execute scripts with root privileges
- **Impact**: Complete system compromise with root-level access, enabling full control over affected web servers
- **Status**: Actively exploited in the wild, patches likely available
- **CVE ID**: CVE-2026-48172

### Drupal Core SQL Injection Vulnerability
- **Description**: Critical SQL injection flaw in Drupal Core that enables unauthorized database access and manipulation
- **Impact**: Database compromise, data exfiltration, potential website defacement, and unauthorized administrative access
- **Status**: Recently patched but actively exploited, added to CISA KEV catalog

### Trend Micro Apex One Zero-Day
- **Description**: Zero-day vulnerability in Trend Micro's Apex One security software affecting Windows systems
- **Impact**: Potential bypass of security controls and system compromise on Windows environments
- **Status**: Actively exploited, patches released by Trend Micro

### Langflow Vulnerability
- **Description**: Security flaw in Langflow platform that has been exploited in attacks
- **Impact**: Unauthorized access to affected systems and potential data compromise
- **Status**: Added to CISA KEV catalog, indicating active exploitation

## Affected Systems and Products

- **LiteSpeed cPanel Plugin**: Web hosting environments using LiteSpeed with cPanel integration
- **Drupal Core**: Content management systems running vulnerable Drupal versions
- **Trend Micro Apex One**: Windows systems protected by Trend Micro endpoint security
- **Langflow Platform**: Organizations using Langflow for workflow automation
- **Laravel-Lang PHP Packages**: PHP applications utilizing compromised Laravel language packages
- **GitHub Repositories**: Over 5,500 repositories targeted in Megalodon campaign
- **Ubiquiti UniFi OS**: Network infrastructure devices running vulnerable UniFi OS versions
- **Cisco Secure Workload**: Data center and cloud security platforms

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious code injection into trusted software packages and repositories
- **SQL Injection**: Database manipulation through vulnerable web application inputs
- **Zero-Day Exploitation**: Attacks leveraging previously unknown vulnerabilities
- **Phishing Campaigns**: Social engineering attacks using legitimate platform lures like Prometheus
- **CI/CD Pipeline Abuse**: Automated injection of malicious workflows into development environments
- **API Exploitation**: Unauthorized access through vulnerable REST API endpoints
- **Privilege Escalation**: Root-level access through plugin vulnerabilities

## Threat Actor Activities

- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned group targeting Ukrainian government entities using Prometheus platform lures for phishing attacks
- **Webworm APT**: Chinese advanced persistent threat group exploiting Discord and Microsoft Graph APIs to target European Union government organizations
- **Supply Chain Attackers**: Unnamed actors compromising Laravel-Lang packages and conducting the Megalodon GitHub campaign
- **KimWolf Botnet Operator**: Canadian individual arrested for operating DDoS-for-hire service affecting nearly two million devices globally
- **Criminal VPN Operators**: Dismantled network used by 25 ransomware groups for attack obfuscation