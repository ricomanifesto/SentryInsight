# Exploitation Report

The current threat landscape is characterized by several critical zero-day vulnerabilities under active exploitation and sophisticated supply chain attacks targeting developer ecosystems. Most concerning is the maximum-severity vulnerability in LiteSpeed cPanel Plugin (CVE-2026-48172) being actively exploited to achieve root access, alongside a Trend Micro Apex One zero-day vulnerability targeting Windows systems. Additionally, multiple coordinated supply chain attacks have compromised Laravel-Lang PHP packages and Packagist repositories, delivering cross-platform credential-stealing malware. The Drupal Core SQL injection vulnerability has also been added to CISA's Known Exploited Vulnerabilities catalog following active exploitation attempts.

## Active Exploitation Details

### LiteSpeed cPanel Plugin Vulnerability
- **Description**: A maximum-severity security flaw in the LiteSpeed User-End cPanel Plugin allowing unauthorized script execution
- **Impact**: Attackers can execute scripts with root privileges on affected systems
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-48172 (CVSS score: 10.0)

### Trend Micro Apex One Zero-Day
- **Description**: A zero-day vulnerability in Trend Micro's Apex One security software
- **Impact**: Enables attacks targeting Windows systems through the security software itself
- **Status**: Actively exploited, patches have been released
- **CISA KEV Status**: Added to Known Exploited Vulnerabilities catalog

### Drupal Core SQL Injection
- **Description**: A critical SQL injection vulnerability in Drupal Core
- **Impact**: Allows attackers to execute arbitrary SQL queries and potentially gain unauthorized access to database content
- **Status**: Recently patched but under active exploitation attempts
- **CISA KEV Status**: Added to Known Exploited Vulnerabilities catalog

### Langflow Vulnerability
- **Description**: A security flaw in Langflow that has been exploited in the wild
- **Impact**: Specific attack vectors not detailed but significant enough for CISA KEV inclusion
- **Status**: Under active exploitation
- **CISA KEV Status**: Added to Known Exploited Vulnerabilities catalog

### Cisco Secure Workload REST API Flaw
- **Description**: A maximum-severity vulnerability in Cisco Secure Workload REST API
- **Impact**: Allows unauthenticated remote attackers to access sensitive data
- **Status**: Patches released
- **CVE ID**: CVE-2026-20223 (CVSS score: 10.0)

## Affected Systems and Products

- **LiteSpeed cPanel Plugin**: User-End cPanel Plugin installations vulnerable to root privilege escalation
- **Trend Micro Apex One**: Windows systems running the security software
- **Drupal Core**: Web applications built on affected Drupal versions
- **Laravel-Lang Packages**: PHP developers using compromised localization packages
- **Packagist Repositories**: Eight packages containing malicious Linux binaries
- **Cisco Secure Workload**: Systems using the REST API functionality
- **Ubiquiti UniFi OS**: Three maximum severity vulnerabilities patched
- **Langflow**: AI workflow management systems

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Attackers compromised Laravel-Lang PHP packages and Packagist repositories to deliver credential-stealing malware
- **GitHub Tag Abuse**: Malicious actors used GitHub version tags to distribute compromised packages
- **Cross-Platform Malware**: Comprehensive credential-stealing frameworks targeting multiple operating systems
- **SQL Injection**: Direct database manipulation through Drupal Core vulnerability
- **REST API Exploitation**: Unauthenticated access to sensitive data through Cisco Secure Workload
- **Zero-Day Exploitation**: Active targeting of unpatched Trend Micro security software
- **Privilege Escalation**: Root access achievement through LiteSpeed cPanel Plugin vulnerability
- **GitHub Repository Compromise**: Megalodon campaign pushed 5,718 malicious commits to 5,561 repositories using CI/CD workflow manipulation

## Threat Actor Activities

- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned threat actor targeting Ukrainian government entities using Prometheus phishing malware lures
- **Webworm**: China-linked APT group using Discord and Microsoft Graph APIs to target European Union government systems, employing SOCKS proxies and tunneling tools
- **Supply Chain Attackers**: Coordinated campaign targeting both Laravel and Packagist ecosystems with sophisticated credential-stealing infrastructure
- **Megalodon Campaign**: Automated attack campaign compromising thousands of GitHub repositories through malicious CI/CD workflows
- **Kimwolf Botnet Operator**: Canadian national arrested for operating DDoS botnet affecting nearly two million devices worldwide
- **CINEMAGOAL Operators**: Italian authorities dismantled piracy ecosystem that stole streaming authentication codes from major platforms
- **First VPN Criminal Network**: Dismantled VPN service used by 25 ransomware groups to obscure attack origins