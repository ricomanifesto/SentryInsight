# Exploitation Report

The cybersecurity landscape is experiencing a surge of critical exploitation activity across multiple platforms and systems. Attackers are actively exploiting zero-day vulnerabilities in learning management systems, content management platforms, and enterprise software to deploy web shells, steal credentials, and conduct espionage campaigns. Most notably, threat actors are leveraging previously unknown flaws in KnowledgeDeliver LMS and Ghost CMS to compromise hundreds of websites, while nation-state groups continue sophisticated supply chain attacks and infrastructure compromises. The exploitation activity spans from AI-assisted attacks requiring urgent 12-hour patching windows to large-scale malware campaigns targeting thousands of GitHub repositories.

## Active Exploitation Details

### KnowledgeDeliver LMS Zero-Day Vulnerability
- **Description**: A critical zero-day vulnerability in the KnowledgeDeliver learning management system that allows remote code execution
- **Impact**: Attackers can deploy web shells including Godzilla and Cobalt Strike, gaining persistent access to compromised systems
- **Status**: Previously exploited as zero-day, now patched by vendor

### Ghost CMS SQL Injection Vulnerability
- **Description**: Critical SQL injection vulnerability in Ghost CMS allowing malicious JavaScript code injection
- **Impact**: Large-scale compromise of over 700 websites for ClickFix attack campaigns
- **Status**: Actively exploited in ongoing campaigns
- **CVE ID**: CVE-2026-26980

### SharePoint Remote Code Execution Vulnerability
- **Description**: Remote code execution vulnerability in Microsoft SharePoint across multiple server versions
- **Impact**: Allows attackers to execute arbitrary code without specialized conditions
- **Status**: Patched via out-of-band Microsoft update
- **CVE ID**: CVE-2026-45659

### Drupal SQL Injection Vulnerability
- **Description**: SQL injection vulnerability in Drupal content management system
- **Impact**: Active exploitation targeting government and enterprise systems
- **Status**: CISA has mandated federal agencies patch within emergency timeframe

## Affected Systems and Products

- **KnowledgeDeliver LMS**: Learning management system popular in Japan, vulnerable to zero-day remote code execution
- **Ghost CMS**: Content management system with over 700 compromised websites
- **Microsoft SharePoint**: Multiple server versions affected by remote code execution vulnerability
- **Drupal CMS**: Content management system with actively exploited SQL injection flaw
- **GitHub Repositories**: Over 5,500 repositories compromised by Megalodon malware campaign
- **npm, PyPI, and CratesIO**: Package repositories targeted in TrapDoor supply chain attacks
- **Windows Server 2016**: Domain controller lookup failures after security updates

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Immediate deployment of web shells through unknown vulnerabilities in enterprise software
- **SQL Injection**: Large-scale exploitation of database vulnerabilities for website compromise
- **Supply Chain Attacks**: Coordinated campaigns across multiple package repositories (npm, PyPI, CratesIO)
- **DLL Side-Loading**: Advanced persistence techniques used in nation-state espionage campaigns
- **ClickFix Campaigns**: Social engineering attacks leveraging compromised websites
- **Web Shell Deployment**: Installation of Godzilla and Cobalt Strike for persistent access
- **Repository Poisoning**: Mass compromise of GitHub repositories for credential theft
- **OAuth Device Code Abuse**: Phishing-as-a-Service platforms bypassing multi-factor authentication

## Threat Actor Activities

- **MuddyWater**: Iranian state-sponsored group conducting DLL side-loading espionage campaigns across nine countries on four continents
- **ShinyHunters**: Extortion group responsible for data breaches at Charter Communications and 7-Eleven, affecting over 185,000 individuals
- **Lazarus Group**: North Korean threat actors deploying RemotePE memory-only RAT against financial and cryptocurrency firms
- **Nimbus Manticore**: Iranian state-sponsored actor (aka Screening Serpens, UNC1549) using aviation-themed lures for MiniFast and MiniJunk V2 malware delivery
- **TeamPCP**: Threat group behind Shai-Hulud worm causing significant open source ecosystem damage
- **TrapDoor Campaign**: Coordinated cross-ecosystem supply chain attackers targeting multiple package repositories
- **Megalodon Campaign**: Large-scale GitHub repository compromise affecting thousands of repositories in six hours