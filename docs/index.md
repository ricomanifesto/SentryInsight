# Exploitation Report

Critical exploitation activity is currently targeting multiple high-impact vulnerabilities across enterprise systems and popular software platforms. The most severe active exploits include a maximum-severity privilege escalation flaw in LiteSpeed cPanel Plugin (CVE-2026-48172), a critical SQL injection vulnerability in Ghost CMS (CVE-2026-26980) being exploited for large-scale ClickFix campaigns, and a highly critical Drupal Core SQL injection flaw that has been added to CISA's Known Exploited Vulnerabilities catalog. Additionally, threat actors are leveraging zero-day vulnerabilities in KnowledgeDeliver LMS and Trend Micro Apex One, while sophisticated supply chain attacks are compromising software packages across npm, PyPI, and other repositories to distribute credential-stealing malware.

## Active Exploitation Details

### LiteSpeed cPanel Plugin Privilege Escalation
- **Description**: A maximum-severity vulnerability in LiteSpeed User-End cPanel Plugin that allows unauthorized privilege escalation
- **Impact**: Attackers can execute scripts with root privileges, gaining complete control over affected systems
- **Status**: Actively exploited in the wild with patches available
- **CVE ID**: CVE-2026-48172

### Ghost CMS SQL Injection
- **Description**: A critical SQL injection vulnerability affecting Ghost CMS installations
- **Impact**: Allows injection of malicious JavaScript code to facilitate ClickFix attacks affecting over 700 websites
- **Status**: Actively exploited in large-scale campaigns with coordinated attacks
- **CVE ID**: CVE-2026-26980

### Drupal Core SQL Injection
- **Description**: A highly critical SQL injection vulnerability in Drupal Core
- **Impact**: Enables attackers to execute arbitrary SQL queries and potentially gain unauthorized access to website databases
- **Status**: Added to CISA KEV catalog due to active exploitation attempts

### KnowledgeDeliver LMS Zero-Day
- **Description**: A now-patched high-severity vulnerability in Digital Knowledge KnowledgeDeliver Learning Management System
- **Impact**: Exploited to deploy Godzilla web shell and Cobalt Strike for persistent access
- **Status**: Previously exploited as zero-day before patching

### Trend Micro Apex One Zero-Day
- **Description**: An unpatched vulnerability in Trend Micro Apex One security software
- **Impact**: Allows attackers to compromise Windows systems protected by the security solution
- **Status**: Currently being exploited in active attacks with patches recently released

## Affected Systems and Products

- **Ghost CMS**: All vulnerable versions susceptible to SQL injection attacks
- **LiteSpeed cPanel Plugin**: User-End plugin versions with privilege escalation vulnerability
- **Drupal Core**: Multiple versions affected by SQL injection flaw
- **KnowledgeDeliver LMS**: Digital Knowledge learning management system popular in Japan
- **Trend Micro Apex One**: Enterprise security software protecting Windows environments
- **Laravel-Lang Packages**: PHP localization packages compromised in supply chain attack
- **npm/PyPI/CratesIO Packages**: Multiple software repositories targeted by TrapDoor campaign
- **Microsoft 365**: Accounts targeted by Kali365 phishing-as-a-service platform

## Attack Vectors and Techniques

- **SQL Injection**: Exploiting database vulnerabilities to inject malicious code and gain unauthorized access
- **ClickFix Campaigns**: JavaScript injection leading to social engineering attacks that trick users into executing malicious actions
- **Supply Chain Poisoning**: Compromising legitimate software packages to distribute credential-stealing malware
- **OAuth Device Code Abuse**: Kali365 platform exploiting OAuth authentication flows to bypass security controls
- **Zero-Day Exploitation**: Targeting previously unknown vulnerabilities before patches are available
- **Privilege Escalation**: Exploiting flaws to gain elevated system access and root privileges
- **Memory-Only Malware**: RemotePE RAT deployment that operates entirely in memory to avoid detection

## Threat Actor Activities

- **ShinyHunters**: Conducted data breach against 7-Eleven, exposing personal information of over 185,000 individuals
- **Lazarus Group**: North Korea-linked actors deploying RemotePE memory-only RAT against financial and cryptocurrency firms
- **TrapDoor Campaign**: Coordinated cross-ecosystem supply chain attack targeting npm, PyPI, and CratesIO repositories
- **Ghostwriter**: Belarus-aligned group (UAC-0057/UNC1151) targeting Ukrainian government entities with Prometheus-themed phishing campaigns
- **Criminal VPN Operators**: 25 ransomware groups utilized dismantled First VPN service for attack concealment
- **ClickFix Attackers**: Large-scale exploitation of Ghost CMS vulnerability for widespread social engineering campaigns