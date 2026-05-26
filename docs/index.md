# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and content management systems, with threat actors actively exploiting vulnerabilities in Ghost CMS, Drupal, SharePoint, and KnowledgeDeliver LMS. The most concerning developments include large-scale campaigns leveraging Ghost CMS vulnerabilities for ClickFix attacks affecting over 700 sites, CISA's urgent directive for federal agencies to patch actively exploited Drupal vulnerabilities, and sophisticated supply chain attacks targeting multiple package repositories. Iranian state-sponsored actors and the North Korean Lazarus Group are conducting targeted campaigns against aviation, financial, and cryptocurrency sectors, while coordinated supply chain attacks are compromising developer environments across npm, PyPI, and other repositories.

## Active Exploitation Details

### Ghost CMS SQL Injection Vulnerability
- **Description**: A critical SQL injection vulnerability in Ghost CMS that allows attackers to inject malicious JavaScript code into websites
- **Impact**: Over 700 websites have been compromised to fuel ClickFix attacks, enabling credential theft and further malware distribution
- **Status**: Being actively exploited in large-scale campaigns
- **CVE ID**: CVE-2026-26980

### Drupal Vulnerability
- **Description**: An SQL injection vulnerability in the Drupal content management system that poses immediate risk to government systems
- **Impact**: Allows attackers to compromise servers and potentially gain unauthorized access to sensitive government data
- **Status**: Actively exploited in the wild, with CISA mandating federal agencies patch by Wednesday evening
- **CVE ID**: Not specified in articles

### SharePoint Remote Code Execution
- **Description**: A remote code execution vulnerability affecting SharePoint that can be exploited without requiring specialized conditions
- **Impact**: Allows attackers to execute arbitrary code on affected SharePoint servers
- **Status**: Recently patched by Microsoft across multiple server versions
- **CVE ID**: CVE-2026-45659

### KnowledgeDeliver LMS Vulnerability
- **Description**: A high-severity security flaw affecting Digital Knowledge KnowledgeDeliver Learning Management System popular in Japan
- **Impact**: Exploited as a zero-day to deploy Godzilla web shell and Cobalt Strike for persistent access
- **Status**: Now patched, but was actively exploited before disclosure

## Affected Systems and Products

- **Ghost CMS**: Content management system with over 700 compromised sites used for ClickFix campaigns
- **Drupal CMS**: Content management systems in federal government environments requiring immediate patching
- **Microsoft SharePoint**: Server versions across multiple releases affected by remote code execution vulnerability
- **Digital Knowledge KnowledgeDeliver**: Learning Management System popular in Japanese organizations
- **Windows Server 2016**: Domain controller lookup failures after May 2026 security updates
- **Laravel-Lang PHP Packages**: Localization packages compromised in supply chain attack
- **npm, PyPI, CratesIO**: Package repositories targeted in coordinated TrapDoor supply chain campaign
- **Packagist**: Eight packages infected with GitHub-hosted Linux malware

## Attack Vectors and Techniques

- **SQL Injection**: Exploitation of Ghost CMS and Drupal vulnerabilities to inject malicious code and gain unauthorized access
- **ClickFix Attacks**: Malicious JavaScript injection through compromised Ghost CMS sites to trick users into downloading malware
- **Supply Chain Poisoning**: Compromise of legitimate software packages across multiple repositories (npm, PyPI, CratesIO, Packagist)
- **Phishing and SEO Poisoning**: Iranian actors using aviation industry lures and search engine optimization manipulation
- **OAuth Device Code Abuse**: Kali365 phishing service exploiting Microsoft 365 authentication mechanisms
- **Memory-Only Execution**: RemotePE RAT operating entirely in memory to evade detection
- **MFA Prompt Bombing**: Overwhelming users with authentication prompts to bypass multi-factor authentication

## Threat Actor Activities

- **Nimbus Manticore (Screening Serpens/UNC1549)**: Iranian state-sponsored group deploying MiniFast and MiniJunk V2 malware through phishing campaigns targeting aviation sector organizations
- **Lazarus Group**: North Korean threat actor using RemotePE memory-only RAT to target financial institutions and cryptocurrency firms
- **ShinyHunters**: Extortion gang responsible for 7-Eleven data breach exposing personal information of 185,000 individuals
- **TrapDoor Campaign Actors**: Coordinated threat actors targeting npm, PyPI, and CratesIO with credential-stealing malware across multiple ecosystems
- **Laravel-Lang Attackers**: Sophisticated actors compromising PHP packages to deliver cross-platform credential stealers through GitHub version tag manipulation
- **Kali365 Operators**: Phishing-as-a-service platform operators targeting Microsoft 365 accounts through OAuth exploitation