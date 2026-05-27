# Exploitation Report

Several critical zero-day and recently disclosed vulnerabilities are currently being exploited in the wild, representing significant threats to enterprise environments. The most concerning activities include a zero-day exploitation of KnowledgeDeliver learning management systems for web shell deployment, active exploitation of Drupal SQL injection vulnerabilities prompting urgent CISA directives, and widespread attacks against Ghost CMS installations affecting over 700 websites. Additionally, supply chain attacks are targeting multiple package repositories simultaneously, while state-sponsored groups continue leveraging DLL side-loading techniques for espionage operations across multiple continents.

## Active Exploitation Details

### KnowledgeDeliver LMS Zero-Day Vulnerability
- **Description**: A critical zero-day vulnerability in Digital Knowledge KnowledgeDeliver learning management system that allows remote code execution
- **Impact**: Attackers can deploy web shells including Godzilla and Cobalt Strike for persistent access and lateral movement
- **Status**: Now patched; was actively exploited as zero-day before disclosure

### Drupal SQL Injection Vulnerability
- **Description**: SQL injection vulnerability in Drupal content management system affecting internet-facing installations
- **Impact**: Allows unauthorized database access and potential system compromise
- **Status**: Actively exploited in the wild; CISA has mandated federal agencies patch by Wednesday evening

### Ghost CMS SQL Injection Flaw
- **Description**: Critical SQL injection vulnerability in Ghost CMS allowing malicious JavaScript injection
- **Impact**: Used to fuel large-scale ClickFix attacks affecting over 700 websites
- **Status**: Actively exploited in coordinated campaign
- **CVE ID**: CVE-2026-26980

### Microsoft SharePoint Remote Code Execution
- **Description**: Remote code execution vulnerability affecting SharePoint server versions
- **Impact**: Allows attackers to execute arbitrary code without specialized conditions
- **Status**: Patched via out-of-band update from Microsoft
- **CVE ID**: CVE-2026-45659

## Affected Systems and Products

- **KnowledgeDeliver LMS**: Learning management system popular in Japan; specific versions exploited via zero-day
- **Drupal CMS**: Content management systems with internet exposure; federal agencies ordered to patch immediately
- **Ghost CMS**: Over 700 websites compromised through SQL injection vulnerability
- **Microsoft SharePoint**: Multiple server versions affected by remote code execution flaw
- **GitHub Repositories**: Over 5,500 repositories infected with Megalodon malware in coordinated campaign
- **Package Repositories**: npm, PyPI, and Crates.io targeted in TrapDoor supply chain attacks
- **Windows Server 2016**: Domain controller lookup failures after KB5087537 security update

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: KnowledgeDeliver vulnerability exploited before public disclosure to deploy web shells
- **SQL Injection**: Ghost CMS and Drupal vulnerabilities leveraged for database compromise and code injection
- **Web Shell Deployment**: Godzilla web shell installed via KnowledgeDeliver exploitation for persistent access
- **Supply Chain Poisoning**: TrapDoor campaign targeting multiple package ecosystems simultaneously
- **Repository Compromise**: Megalodon malware campaign pushing malicious commits to thousands of GitHub repositories
- **DLL Side-Loading**: Advanced persistent threat groups using legitimate processes to load malicious libraries
- **OAuth Device Code Abuse**: Kali365 phishing service exploiting Microsoft 365 authentication mechanisms
- **ClickFix Attacks**: Malicious JavaScript injection through Ghost CMS compromise

## Threat Actor Activities

- **MuddyWater**: Iranian state-sponsored group conducting espionage campaigns across nine countries using DLL side-loading techniques
- **Lazarus Group**: North Korean APT deploying RemotePE memory-only RAT against financial and cryptocurrency firms
- **Nimbus Manticore**: Iranian threat actor (aka Screening Serpens, UNC1549) using aviation industry lures and SEO poisoning
- **ShinyHunters**: Extortion group behind Charter Communications and 7-Eleven data breaches affecting hundreds of thousands
- **TeamPCP**: Hackers behind Shai-Hulud worm causing significant damage to open source ecosystem
- **TrapDoor Campaign**: Coordinated supply chain attack spreading credential-stealing malware across multiple platforms
- **Megalodon Operators**: Campaign targeting GitHub repositories with thousands of malicious commits in six-hour window