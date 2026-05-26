# Exploitation Report

This report analyzes several critical vulnerability exploitation campaigns that pose significant threats to organizations worldwide. The most severe activities include widespread exploitation of content management systems, supply chain attacks targeting multiple software repositories, and sophisticated phishing campaigns. Notable exploitations include a Drupal SQL injection vulnerability being actively exploited in the wild, a critical Ghost CMS flaw affecting over 700 websites, and a maximum-severity LiteSpeed cPanel plugin vulnerability with a perfect CVSS score. Multiple supply chain attacks have compromised popular package repositories including npm, PyPI, Laravel-Lang, and Packagist, while threat actors continue to deploy advanced malware and phishing platforms targeting enterprise environments.

## Active Exploitation Details

### Drupal SQL Injection Vulnerability
- **Description**: A SQL injection vulnerability in the Drupal content management system that has been flagged as actively exploited
- **Impact**: Attackers can potentially compromise web servers and access sensitive database information
- **Status**: CISA has ordered federal agencies to patch by Wednesday evening; actively exploited in the wild

### Ghost CMS SQL Injection Vulnerability
- **Description**: A critical SQL injection vulnerability in Ghost CMS being exploited to inject malicious JavaScript code
- **Impact**: Threat actors can hijack websites and launch ClickFix attacks against visitors
- **Status**: Over 700 websites compromised in large-scale campaign
- **CVE ID**: CVE-2026-26980

### KnowledgeDeliver LMS Zero-Day
- **Description**: A high-severity security flaw in Digital Knowledge KnowledgeDeliver Learning Management System popular in Japan
- **Impact**: Exploitation allows deployment of Godzilla web shell and Cobalt Strike for persistent access
- **Status**: Previously exploited as zero-day, now patched

### LiteSpeed cPanel Plugin Critical Vulnerability
- **Description**: A maximum-severity security vulnerability in LiteSpeed User-End cPanel Plugin
- **Impact**: Allows attackers to execute scripts with root privileges on affected systems
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-48172

### Microsoft SharePoint Remote Code Execution
- **Description**: A remote code execution vulnerability affecting SharePoint across multiple server versions
- **Impact**: Could allow attackers to execute arbitrary code without specialized conditions
- **Status**: Recently patched by Microsoft
- **CVE ID**: CVE-2026-45659

## Affected Systems and Products

- **Drupal CMS**: Content management systems using vulnerable Drupal versions
- **Ghost CMS**: Over 700 websites compromised through SQL injection attacks
- **Digital Knowledge KnowledgeDeliver**: Learning Management Systems deployed in Japan
- **LiteSpeed cPanel Plugin**: Web hosting environments using affected plugin versions
- **Microsoft SharePoint**: Multiple server versions across various deployments
- **Laravel-Lang Packages**: PHP development environments using compromised localization packages
- **npm/PyPI/Crates.io**: Developer environments using packages from affected repositories
- **Packagist**: PHP development environments using compromised packages

## Attack Vectors and Techniques

- **SQL Injection**: Exploitation of database vulnerabilities in Drupal and Ghost CMS platforms
- **Supply Chain Attacks**: Compromise of legitimate software packages across multiple repositories
- **Phishing-as-a-Service**: Kali365 platform targeting Microsoft 365 accounts through OAuth abuse
- **ClickFix Campaigns**: Social engineering attacks delivered through compromised Ghost CMS websites
- **SEO Poisoning**: Iranian threat actors using search engine optimization manipulation
- **Memory-Only Malware**: Deployment of RemotePE RAT that operates entirely in memory
- **Cross-Platform Credential Theft**: Multi-ecosystem attacks targeting developer credentials

## Threat Actor Activities

- **Nimbus Manticore (Iranian APT)**: Deploying MiniFast and MiniJunk V2 malware through phishing and SEO poisoning campaigns targeting aviation organizations
- **Lazarus Group (North Korean APT)**: Using RemotePE memory-only RAT against financial and cryptocurrency firms
- **ShinyHunters**: Data extortion gang responsible for 7-Eleven breach affecting 185,000 individuals
- **TrapDoor Campaign**: Coordinated supply chain attack spreading credential-stealing malware across npm, PyPI, and Crates.io
- **ClickFix Operators**: Large-scale campaign exploiting Ghost CMS vulnerability to distribute malicious JavaScript
- **Laravel-Lang Attackers**: Sophisticated supply chain compromise targeting PHP localization packages
- **Kali365 Operators**: Phishing-as-a-Service platform specifically targeting Microsoft 365 environments