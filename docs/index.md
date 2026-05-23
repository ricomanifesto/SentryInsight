# Exploitation Report

Critical vulnerabilities across multiple enterprise platforms are under active exploitation, posing significant risks to organizations worldwide. The most severe threats include a maximum-severity LiteSpeed cPanel plugin vulnerability (CVE-2026-48172) being exploited to achieve root-level access, a critical Drupal Core SQL injection flaw that has been added to CISA's Known Exploited Vulnerabilities catalog, and a zero-day vulnerability in Trend Micro Apex One security software. Additional high-severity vulnerabilities in Ubiquiti UniFi OS and Cisco Secure Workload have been patched, while threat actors continue to exploit infrastructure vulnerabilities through sophisticated campaigns targeting government entities and telecommunications providers.

## Active Exploitation Details

### LiteSpeed cPanel Plugin Vulnerability
- **Description**: A maximum-severity security vulnerability in the LiteSpeed User-End cPanel Plugin that allows unauthorized script execution with root privileges
- **Impact**: Attackers can gain complete administrative control over affected systems, execute arbitrary commands, and potentially compromise entire hosting infrastructure
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-48172

### Drupal Core SQL Injection Vulnerability
- **Description**: A critical SQL injection vulnerability in Drupal Core that allows attackers to manipulate database queries
- **Impact**: Unauthorized database access, data exfiltration, potential complete system compromise
- **Status**: Actively exploited and added to CISA KEV catalog, patch available
- **CVE ID**: Not specified in articles

### Trend Micro Apex One Zero-Day
- **Description**: A zero-day vulnerability affecting Trend Micro's Apex One security software on Windows systems
- **Impact**: Compromise of endpoint security solutions, potential bypass of security controls
- **Status**: Actively exploited in attacks, security update released
- **CVE ID**: Not specified in articles

### Langflow Vulnerability
- **Description**: Security vulnerability in Langflow platform that has been added to CISA's KEV catalog
- **Impact**: Unauthorized access and potential system compromise
- **Status**: Under active exploitation
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **LiteSpeed User-End cPanel Plugin**: Web hosting management software with maximum severity vulnerability
- **Drupal Core**: Content management system with critical SQL injection flaw
- **Trend Micro Apex One**: Enterprise endpoint security solution on Windows systems
- **Langflow Platform**: Development platform with exploited vulnerability
- **Ubiquiti UniFi OS**: Network management platform with three maximum severity vulnerabilities
- **Cisco Secure Workload**: REST API vulnerability with CVSS 10.0 rating
- **Chromium Browser**: Unfixed vulnerability allowing background JavaScript execution

## Attack Vectors and Techniques

- **SQL Injection**: Critical vulnerability in Drupal Core allowing database manipulation
- **Root Privilege Escalation**: LiteSpeed plugin exploitation enabling administrative access
- **Zero-Day Exploitation**: Active targeting of unpatched Trend Micro security software
- **CI/CD Pipeline Attacks**: Megalodon campaign targeting 5,561 GitHub repositories with malicious workflows
- **Phishing Campaigns**: Ghostwriter threat group using Prometheus platform lures against Ukrainian government
- **API Exploitation**: Maximum severity Cisco Secure Workload REST API vulnerability
- **Background Process Exploitation**: Chromium vulnerability maintaining JavaScript execution after browser closure

## Threat Actor Activities

- **Ghostwriter (UAC-0057, UNC1151)**: Belarus-aligned group targeting Ukrainian government entities with Prometheus-themed phishing campaigns using malicious lures
- **Webworm**: Chinese APT group leveraging Discord and Microsoft Graph APIs to target European Union government systems, utilizing SOCKS proxies and SoftEther VPN for tunneling
- **Chinese Cyber-Espionage Groups**: Deploying Showboat Linux malware and JFMBackdoor Windows malware against Middle East telecommunications providers
- **Megalodon Campaign**: Automated attack pushing 5,718 malicious commits to GitHub repositories within six hours
- **Kimwolf Botnet Operators**: Canadian national arrested for operating DDoS botnet infecting nearly two million devices worldwide
- **Criminal VPN Networks**: International takedown of VPN service used by 25 ransomware groups for attack obfuscation