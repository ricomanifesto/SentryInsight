# Exploitation Report

Current exploitation activity reveals a concerning landscape dominated by multiple critical vulnerabilities being actively exploited across diverse platforms and attack vectors. The most significant threats include an actively exploited SQL injection vulnerability in Drupal CMS that has prompted emergency patching orders from CISA, a critical Ghost CMS SQL injection flaw (CVE-2026-26980) being weaponized in large-scale ClickFix campaigns affecting over 700 websites, and a zero-day exploitation of KnowledgeDeliver LMS systems to deploy advanced malware including Godzilla web shells and Cobalt Strike. Additionally, Microsoft has patched a critical SharePoint remote code execution vulnerability (CVE-2026-45659), while sophisticated supply chain attacks are targeting multiple package repositories including npm, PyPI, and Laravel-Lang packages to distribute credential-stealing malware.

## Active Exploitation Details

### Drupal SQL Injection Vulnerability
- **Description**: A critical SQL injection vulnerability in the Drupal content management system that allows attackers to manipulate database queries
- **Impact**: Attackers can gain unauthorized access to sensitive data, potentially compromise entire websites, and execute malicious database operations
- **Status**: Actively exploited in the wild, CISA has mandated federal agencies patch by Wednesday evening

### Ghost CMS SQL Injection Flaw
- **Description**: Critical SQL injection vulnerability in Ghost CMS platform allowing malicious JavaScript code injection
- **Impact**: Enables large-scale ClickFix attack campaigns, website hijacking, and malicious code distribution to site visitors
- **Status**: Actively exploited, affecting over 700 websites in coordinated campaign
- **CVE ID**: CVE-2026-26980

### KnowledgeDeliver LMS Zero-Day
- **Description**: High-severity security flaw in Digital Knowledge KnowledgeDeliver Learning Management System popular in Japan
- **Impact**: Zero-day exploitation enables deployment of Godzilla web shells and Cobalt Strike frameworks for persistent access
- **Status**: Previously exploited as zero-day, now patched

### Microsoft SharePoint Remote Code Execution
- **Description**: Remote code execution vulnerability affecting SharePoint across multiple server versions
- **Impact**: Allows attackers to execute arbitrary code on affected SharePoint servers without specialized conditions
- **Status**: Recently patched by Microsoft across affected versions
- **CVE ID**: CVE-2026-45659

## Affected Systems and Products

- **Drupal CMS**: Content management systems with internet exposure, particularly affecting federal government agencies
- **Ghost CMS**: Over 700 websites compromised through SQL injection exploitation
- **KnowledgeDeliver LMS**: Learning Management System deployments, particularly in Japanese organizations
- **Microsoft SharePoint**: Multiple server versions across enterprise environments
- **Laravel-Lang PHP Packages**: PHP development environments using compromised localization packages
- **npm, PyPI, and CratesIO**: Package repositories affected by TrapDoor supply chain campaign
- **Packagist Repository**: Eight packages infected with Linux malware hosted on GitHub

## Attack Vectors and Techniques

- **SQL Injection**: Primary vector for Drupal and Ghost CMS exploitations enabling database manipulation and code injection
- **Zero-Day Exploitation**: KnowledgeDeliver LMS targeted before patches were available
- **Supply Chain Attacks**: Multi-platform campaigns targeting npm, PyPI, CratesIO, and Laravel-Lang packages
- **ClickFix Campaigns**: Malicious JavaScript injection through Ghost CMS vulnerabilities
- **Phishing and SEO Poisoning**: Iranian threat actors using lures impersonating aviation organizations
- **OAuth Device Code Abuse**: Kali365 phishing service exploiting Microsoft 365 authentication flows
- **Package Hijacking**: Attackers abusing GitHub version tags to distribute malicious code

## Threat Actor Activities

- **Nimbus Manticore (Iranian APT)**: Deploying MiniFast and MiniJunk V2 malware through phishing campaigns and SEO poisoning targeting aviation sector organizations
- **Lazarus Group (North Korean APT)**: Utilizing RemotePE memory-only RAT in attacks against financial and cryptocurrency firms
- **ShinyHunters Extortion Gang**: Successfully breached 7-Eleven systems, compromising personal information of over 185,000 individuals
- **TrapDoor Campaign Operators**: Coordinating cross-ecosystem supply chain attacks across multiple package repositories
- **Russian Cybercriminals**: Operating infrastructure seized by Netherlands authorities, supporting cyberattacks and influence operations