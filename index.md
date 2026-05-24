# Exploitation Report

The current threat landscape is dominated by several critical active exploitation campaigns targeting widely-used software platforms and infrastructure. Most notably, threat actors are actively exploiting maximum-severity vulnerabilities in LiteSpeed cPanel Plugin (CVE-2026-48172) enabling root-level script execution, a critical SQL injection flaw in Drupal Core that has been added to CISA's Known Exploited Vulnerabilities catalog, and a zero-day vulnerability in Trend Micro Apex One security software. Additionally, sophisticated supply chain attacks have compromised Laravel Lang PHP packages and multiple Packagist packages to deliver credential-stealing malware, while advanced persistent threat groups like Ghostwriter continue targeting government entities with phishing campaigns.

## Active Exploitation Details

### LiteSpeed cPanel Plugin Root Privilege Escalation
- **Description**: A maximum-severity security vulnerability in LiteSpeed User-End cPanel Plugin that allows attackers to execute scripts with root privileges
- **Impact**: Complete system compromise with root-level access on affected web hosting environments
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2026-48172 (CVSS score: 10.0)

### Drupal Core SQL Injection Vulnerability
- **Description**: A critical SQL injection flaw in Drupal Core that enables unauthorized database access and manipulation
- **Impact**: Unauthorized access to sensitive data, potential for complete site compromise and data exfiltration
- **Status**: Recently patched but actively exploited, added to CISA Known Exploited Vulnerabilities catalog
- **CVE ID**: Not specified in the source material

### Trend Micro Apex One Zero-Day
- **Description**: An undisclosed zero-day vulnerability in Trend Micro's Apex One security software targeting Windows systems
- **Impact**: Compromise of endpoint security solutions, potential for bypassing security controls
- **Status**: Actively exploited in attacks, recently patched by Trend Micro
- **CVE ID**: Not specified in the source material

### Langflow Vulnerability
- **Description**: A security flaw in Langflow that has been actively exploited by threat actors
- **Impact**: Unauthorized access and potential system compromise
- **Status**: Added to CISA Known Exploited Vulnerabilities catalog
- **CVE ID**: Not specified in the source material

### Cisco Secure Workload REST API Flaw
- **Description**: A maximum-severity vulnerability in Cisco Secure Workload REST API allowing unauthenticated remote access to sensitive data
- **Impact**: Unauthorized access to sensitive organizational data without authentication
- **Status**: Recently patched by Cisco
- **CVE ID**: CVE-2026-20223 (CVSS score: 10.0)

## Affected Systems and Products

- **LiteSpeed cPanel Plugin**: Web hosting environments using LiteSpeed technology with cPanel integration
- **Drupal Core**: Content management systems running Drupal, affecting numerous websites globally
- **Trend Micro Apex One**: Windows endpoint security deployments across enterprise environments
- **Laravel Lang Packages**: PHP development environments using Laravel framework localization packages
- **Packagist Repositories**: PHP package management systems and dependent applications
- **Cisco Secure Workload**: Enterprise network security and workload protection systems
- **Langflow**: Data flow and workflow management systems
- **Ubiquiti UniFi OS**: Network infrastructure management systems (three maximum severity vulnerabilities patched)
- **GitHub Repositories**: Development environments affected by Megalodon campaign targeting CI/CD workflows

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Attackers compromised legitimate PHP packages in Laravel Lang and Packagist repositories to distribute credential-stealing malware
- **GitHub Version Tag Abuse**: Sophisticated manipulation of GitHub version tags to distribute malicious packages while appearing legitimate
- **CI/CD Workflow Exploitation**: Megalodon campaign pushed 5,718 malicious commits to 5,561 GitHub repositories within six hours using automated techniques
- **Zero-Day Exploitation**: Direct exploitation of previously unknown vulnerabilities in security software
- **SQL Injection Attacks**: Traditional but effective database manipulation attacks against Drupal installations
- **Phishing with Platform Lures**: Ghostwriter threat actors using Ukrainian Prometheus learning platform lures for government targeting
- **Cross-Platform Malware Deployment**: Comprehensive credential stealers targeting multiple operating systems and applications

## Threat Actor Activities

- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned threat actor targeting Ukrainian government entities using Prometheus platform lures for phishing campaigns
- **Supply Chain Attackers**: Coordinated campaigns targeting PHP ecosystem through Laravel Lang and Packagist package repositories
- **Webworm APT**: Chinese advanced persistent threat group using Discord and Microsoft Graph APIs to target European Union government systems
- **Megalodon Campaign Operators**: Automated attack campaign targeting thousands of GitHub repositories with malicious CI/CD workflows
- **Kimwolf Botnet Operator**: Canadian national arrested for operating DDoS botnet that infected nearly two million devices worldwide
- **Criminal VPN Network**: First VPN service dismantled by international law enforcement, used by 25 different ransomware groups for attack obfuscation
- **CINEMAGOAL Piracy Operation**: Italian authorities disrupted ecosystem that stole streaming authentication codes from major platforms including Netflix and Disney+