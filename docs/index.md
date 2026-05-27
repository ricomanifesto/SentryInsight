# Exploitation Report

Several critical vulnerabilities are currently being actively exploited in the wild, posing significant threats to organizations worldwide. The most concerning activities include zero-day exploitation of KnowledgeDeliver LMS systems leading to web shell deployment, large-scale exploitation of Ghost CMS vulnerabilities affecting over 700 websites for ClickFix attacks, and active targeting of Drupal systems through SQL injection vulnerabilities. Additionally, threat actors are leveraging supply chain attacks across multiple package repositories and conducting sophisticated espionage campaigns using advanced malware frameworks.

## Active Exploitation Details

### KnowledgeDeliver LMS Zero-Day Vulnerability
- **Description**: A critical zero-day vulnerability in Digital Knowledge KnowledgeDeliver Learning Management System that allows unauthorized code execution and web shell deployment
- **Impact**: Attackers can deploy Godzilla web shells and Cobalt Strike beacons, gaining persistent access to compromised systems
- **Status**: Previously exploited as zero-day, now patched

### Ghost CMS SQL Injection Vulnerability
- **Description**: Critical SQL injection vulnerability in Ghost CMS allowing malicious JavaScript code injection
- **Impact**: Enables large-scale ClickFix attack campaigns targeting website visitors with fake error messages to deliver malware
- **Status**: Actively exploited across 700+ compromised websites
- **CVE ID**: CVE-2026-26980

### SharePoint Remote Code Execution Vulnerability
- **Description**: Remote code execution vulnerability in Microsoft SharePoint affecting multiple server versions
- **Impact**: Attackers can execute arbitrary code without specialized conditions, potentially gaining full system access
- **Status**: Patched via out-of-band update from Microsoft
- **CVE ID**: CVE-2026-45659

### Drupal SQL Injection Vulnerability
- **Description**: SQL injection vulnerability in Drupal content management system actively targeted by threat actors
- **Impact**: Allows unauthorized database access and potential system compromise
- **Status**: CISA has ordered federal agencies to patch within emergency timeframes due to active exploitation

## Affected Systems and Products

- **KnowledgeDeliver LMS**: Learning management system popular in Japan, vulnerable to zero-day exploitation
- **Ghost CMS**: Content management system with over 700 confirmed compromised websites
- **Microsoft SharePoint**: Multiple server versions affected by remote code execution vulnerability
- **Drupal CMS**: Content management systems targeted via SQL injection attacks
- **Package Repositories**: npm, PyPI, and CratesIO affected by TrapDoor supply chain attacks
- **GitHub Repositories**: Over 5,500 repositories compromised by Megalodon malware campaign
- **Microsoft 365**: Accounts targeted by Kali365 phishing-as-a-service platform

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in KnowledgeDeliver systems
- **SQL Injection**: Database manipulation attacks against Ghost CMS and Drupal installations
- **Web Shell Deployment**: Installation of Godzilla web shells for persistent access
- **Supply Chain Attacks**: TrapDoor campaign spreading credential-stealing malware across multiple package ecosystems
- **ClickFix Campaigns**: Fake browser error messages used to deliver malware via compromised Ghost CMS sites
- **DLL Side-Loading**: Advanced technique used by MuddyWater for evasion and persistence
- **OAuth Device Code Abuse**: Kali365 platform exploiting Microsoft 365 authentication mechanisms
- **Memory-Only Execution**: RemotePE malware operating entirely in memory to avoid detection
- **Phishing and SEO Poisoning**: Iranian actors using fake aviation organization lures

## Threat Actor Activities

- **MuddyWater (Iranian APT)**: Conducting espionage campaigns across nine countries using DLL side-loading techniques and targeting government and critical infrastructure
- **Lazarus Group (North Korean APT)**: Deploying RemotePE memory-only RAT against financial institutions and cryptocurrency firms
- **Nimbus Manticore/UNC1549 (Iranian)**: Using aviation industry lures in phishing campaigns deploying MiniFast and MiniJunk V2 malware
- **ShinyHunters**: Extortion group responsible for data breaches at Charter Communications and 7-Eleven, affecting hundreds of thousands of individuals
- **TeamPCP**: Operators behind Shai-Hulud worm causing significant damage to open source ecosystems
- **TrapDoor Campaign Operators**: Coordinating cross-platform supply chain attacks targeting developer communities
- **Megalodon Campaign**: Rapidly compromising thousands of GitHub repositories in coordinated six-hour attack window