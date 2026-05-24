# Exploitation Report

The current threat landscape is dominated by several critical zero-day and recently patched vulnerabilities being actively exploited in the wild. Most concerning is the active exploitation of CVE-2026-48172, a maximum-severity vulnerability in LiteSpeed cPanel Plugin that allows attackers to run scripts with root privileges. Additionally, multiple supply chain attacks are targeting popular development frameworks, including compromised Laravel Lang packages and coordinated attacks on Packagist repositories. The Drupal Core SQL injection vulnerability recently added to CISA's KEV catalog demonstrates continued exploitation of web application frameworks, while a Trend Micro Apex One zero-day highlights ongoing threats to enterprise security solutions.

## Active Exploitation Details

### LiteSpeed cPanel Plugin Root Privilege Escalation
- **Description**: A maximum-severity security vulnerability in LiteSpeed User-End cPanel Plugin that enables unauthorized script execution
- **Impact**: Attackers can execute arbitrary scripts with root privileges on affected systems
- **Status**: Currently being actively exploited in the wild
- **CVE ID**: CVE-2026-48172 (CVSS score: 10.0)

### Drupal Core SQL Injection Vulnerability
- **Description**: A critical SQL injection flaw in Drupal Core that has been recently patched
- **Impact**: Allows attackers to execute arbitrary SQL queries and potentially gain unauthorized access to database content
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation attempts

### Trend Micro Apex One Zero-Day
- **Description**: An unpatched vulnerability in Trend Micro's Apex One cybersecurity software affecting Windows systems
- **Impact**: Enables attackers to compromise enterprise security solutions and potentially gain system access
- **Status**: Currently being exploited in attacks targeting Windows environments

### Langflow Vulnerability
- **Description**: A security flaw in the Langflow application development platform
- **Impact**: Allows unauthorized access and potential system compromise
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to confirmed exploitation

### Cisco Secure Workload REST API Vulnerability
- **Description**: A maximum-severity flaw in Cisco Secure Workload's REST API interface
- **Impact**: Enables unauthenticated remote attackers to access sensitive data
- **Status**: Recently patched by Cisco
- **CVE ID**: CVE-2026-20223 (CVSS score: 10.0)

## Affected Systems and Products

- **LiteSpeed User-End cPanel Plugin**: Web hosting control panel plugin with root privilege escalation vulnerability
- **Drupal Core**: Popular content management system with SQL injection vulnerability
- **Trend Micro Apex One**: Enterprise cybersecurity solution with zero-day vulnerability on Windows systems
- **Laravel Lang Packages**: PHP localization packages compromised in supply chain attack
- **Packagist Repositories**: Eight packages infected with malicious code targeting Linux systems
- **Langflow**: Application development platform added to CISA KEV catalog
- **Cisco Secure Workload**: Network security solution with REST API vulnerability
- **Ubiquiti UniFi OS**: Network management platform with three maximum severity vulnerabilities
- **npm Package Registry**: Software repository targeted by supply chain security improvements

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Compromised PHP packages delivering cross-platform credential-stealing malware through GitHub version tags
- **Malicious Code Injection**: Linux malware hosted on GitHub Releases URLs embedded in legitimate packages
- **SQL Injection**: Critical database manipulation attacks against Drupal Core installations
- **Root Privilege Escalation**: Exploitation of cPanel plugin vulnerabilities to gain system-level access
- **Zero-Day Exploitation**: Active targeting of unpatched Trend Micro security software
- **CI/CD Workflow Compromise**: Megalodon campaign pushing malicious commits to thousands of GitHub repositories
- **Phishing Campaigns**: Targeted attacks using Ukrainian learning platform lures
- **API Manipulation**: Exploitation of REST API vulnerabilities for unauthorized data access

## Threat Actor Activities

- **Ghostwriter (UAC-0057, UNC1151)**: Belarus-aligned threat actor targeting Ukrainian government entities using Prometheus phishing malware and online learning platform lures
- **Webworm**: China-linked advanced persistent threat group using Discord and Microsoft Graph APIs to target European Union government systems, employing SOCKS proxies and tunneling tools
- **Supply Chain Attackers**: Coordinated campaign targeting Laravel Lang packages and Packagist repositories with sophisticated credential-stealing malware
- **Megalodon Campaign**: Automated attack pushing over 5,700 malicious commits to more than 5,500 GitHub repositories within six hours
- **Kimwolf Botnet Operators**: Canadian national arrested for operating distributed denial-of-service botnet affecting nearly two million devices worldwide
- **CINEMAGOAL Piracy Network**: Italian authorities dismantled streaming piracy ecosystem that stole authentication codes from major platforms including Netflix and Disney+