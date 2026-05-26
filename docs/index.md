# Exploitation Report

Critical exploitation activity continues to surge across multiple platforms and systems, with threat actors leveraging both newly discovered vulnerabilities and sophisticated supply chain attacks. The most significant developments include active exploitation of a Drupal SQL injection vulnerability flagged by CISA, a zero-day attack against KnowledgeDeliver LMS that deployed advanced malware, and the widespread abuse of Ghost CMS affecting over 700 websites. Iranian state-sponsored groups, including MuddyWater and Nimbus Manticore, are conducting extensive espionage campaigns using DLL side-loading and phishing techniques, while the North Korean Lazarus Group has deployed new memory-only malware against financial institutions. Multiple coordinated supply chain attacks have compromised popular package repositories including npm, PyPI, and Packagist, exposing developers to credential-stealing malware.

## Active Exploitation Details

### Drupal SQL Injection Vulnerability
- **Description**: A critical SQL injection vulnerability in the Drupal content management system that allows remote code execution
- **Impact**: Attackers can execute arbitrary SQL commands and potentially gain full system access
- **Status**: Actively exploited in the wild; CISA has ordered federal agencies to patch by Wednesday evening

### KnowledgeDeliver LMS Zero-Day
- **Description**: A high-severity security flaw in Digital Knowledge KnowledgeDeliver, a Learning Management System popular in Japan
- **Impact**: Enables deployment of Godzilla web shell and Cobalt Strike for persistent access and lateral movement
- **Status**: Previously zero-day vulnerability, now patched; was actively exploited before disclosure

### Ghost CMS SQL Injection
- **Description**: A critical SQL injection vulnerability in Ghost CMS enabling malicious JavaScript injection
- **Impact**: Allows injection of malicious code to conduct ClickFix attacks and compromise website visitors
- **Status**: Actively exploited in large-scale campaign affecting 700+ websites
- **CVE ID**: CVE-2026-26980

### SharePoint Remote Code Execution
- **Description**: A remote code execution vulnerability affecting multiple SharePoint Server versions
- **Impact**: Attackers can execute arbitrary code without specialized conditions or requirements
- **Status**: Recently patched by Microsoft across affected server versions
- **CVE ID**: CVE-2026-45659

## Affected Systems and Products

- **Drupal CMS**: Content management systems with internet-facing exposure
- **KnowledgeDeliver LMS**: Learning management systems, particularly popular in Japanese organizations
- **Ghost CMS**: Content management platforms running vulnerable versions
- **SharePoint Server**: Multiple versions across enterprise environments
- **Windows Server 2016**: Domain controller functionality affected by recent security updates
- **npm, PyPI, Crates.io**: Package repositories and dependent development environments
- **Packagist**: PHP package repository and Composer-based applications
- **Laravel Lang packages**: Localization packages in Laravel development frameworks

## Attack Vectors and Techniques

- **DLL Side-Loading**: Iranian MuddyWater group using legitimate applications to load malicious DLLs for stealth
- **SQL Injection**: Direct database manipulation through vulnerable input validation in web applications
- **Supply Chain Attacks**: Coordinated campaigns targeting multiple package repositories with malicious code
- **Phishing and SEO Poisoning**: Iranian Nimbus Manticore using aviation industry lures and search engine manipulation
- **Memory-Only Malware**: RemotePE RAT executing entirely in memory to evade detection
- **OAuth Device Code Abuse**: Kali365 phishing service exploiting Microsoft 365 authentication mechanisms
- **ClickFix Campaigns**: JavaScript injection leading to fake error pages prompting malicious downloads
- **Package Hijacking**: Abuse of GitHub version tags and repository takeover for malware distribution

## Threat Actor Activities

- **MuddyWater (Iranian APT)**: Conducting espionage campaigns across nine countries using DLL side-loading techniques targeting government and critical infrastructure
- **Nimbus Manticore (Iranian APT)**: Deploying MiniFast and MiniJunk V2 malware through aviation industry phishing lures and SEO poisoning
- **Lazarus Group (North Korean APT)**: Targeting financial and cryptocurrency firms with cross-platform RemotePE memory-only RAT for persistent access
- **ShinyHunters**: Extortion gang responsible for 7-Eleven data breach affecting 185,000 individuals
- **TrapDoor Campaign**: Coordinated supply chain attackers distributing credential-stealing malware across npm, PyPI, and Crates.io ecosystems
- **CINEMAGOAL Operators**: Piracy network dismantled by Italian authorities that was stealing streaming service authentication codes