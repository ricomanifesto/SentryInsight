# Exploitation Report

Critical exploitation activity is currently targeting multiple systems across various platforms, with particular focus on content management systems, learning management platforms, and software supply chains. The most concerning developments include active zero-day exploitation of KnowledgeDeliver LMS systems to deploy web shells and post-exploitation tools, large-scale exploitation of Ghost CMS vulnerabilities affecting hundreds of websites, and coordinated supply chain attacks spreading credential-stealing malware across multiple package repositories. Additionally, Microsoft has issued emergency patches for SharePoint remote code execution vulnerabilities, while threat actors continue to leverage phishing-as-a-service platforms and sophisticated malware campaigns targeting financial institutions and government entities.

## Active Exploitation Details

### KnowledgeDeliver LMS Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in Digital Knowledge KnowledgeDeliver Learning Management System that allows remote code execution
- **Impact**: Attackers can deploy web shells, specifically the Godzilla web shell, and establish persistent access for further exploitation including Cobalt Strike deployment
- **Status**: Previously exploited as zero-day, now patched by vendor
- **CVE ID**: Not specified in the articles

### Ghost CMS SQL Injection Vulnerability
- **Description**: Critical SQL injection vulnerability in Ghost CMS enabling arbitrary code injection
- **Impact**: Large-scale exploitation affecting over 700 websites to inject malicious JavaScript code for ClickFix attacks
- **Status**: Actively exploited in ongoing campaign
- **CVE ID**: CVE-2026-26980

### SharePoint Remote Code Execution Vulnerability
- **Description**: Remote code execution vulnerability in Microsoft SharePoint that can be exploited without specialized conditions
- **Impact**: Complete system compromise with potential access to critical enterprise data and systems
- **Status**: Patched via Microsoft out-of-band security update
- **CVE ID**: CVE-2026-45659

### Drupal SQL Injection Vulnerability
- **Description**: SQL injection vulnerability in Drupal content management system
- **Impact**: Remote code execution and potential system compromise
- **Status**: Actively exploited and added to CISA's Known Exploited Vulnerabilities catalog with mandatory patching deadline for federal agencies
- **CVE ID**: Not specified in the articles

## Affected Systems and Products

- **KnowledgeDeliver LMS**: Learning Management System popular in Japan, vulnerable to zero-day exploitation
- **Ghost CMS**: Content management system with over 700 compromised websites
- **Microsoft SharePoint**: Enterprise collaboration platform across multiple server versions
- **Drupal CMS**: Content management system used by government and enterprise organizations
- **npm, PyPI, and CratesIO**: Software package repositories targeted in TrapDoor supply chain attacks
- **GitHub Repositories**: Over 5,500 repositories infected with Megalodon malware
- **Microsoft 365**: Accounts targeted by Kali365 phishing-as-a-service platform

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise systems
- **SQL Injection**: Database manipulation leading to code execution and site compromise
- **Web Shell Deployment**: Installation of persistent backdoors using tools like Godzilla web shell
- **Supply Chain Poisoning**: Injection of malicious packages into software repositories
- **ClickFix Attacks**: Social engineering technique using fake update prompts to deliver malware
- **Phishing-as-a-Service**: OAuth device code authentication abuse to bypass multi-factor authentication
- **DLL Side-Loading**: Legitimate application abuse to load malicious code
- **Memory-Only RAT Deployment**: Fileless malware execution to evade detection
- **SEO Poisoning**: Search engine result manipulation to distribute malware

## Threat Actor Activities

- **MuddyWater (Iranian APT)**: Conducting espionage campaigns across nine countries using DLL side-loading techniques
- **Nimbus Manticore/Screening Serpens/UNC1549 (Iranian APT)**: Deploying MiniFast and MiniJunk V2 malware via phishing and SEO poisoning
- **Lazarus Group (North Korean APT)**: Targeting financial and cryptocurrency firms with RemotePE memory-only RAT
- **ShinyHunters**: Extortion group responsible for data breaches at Charter Communications and 7-Eleven
- **TeamPCP**: Operators behind Shai-Hulud worm causing significant damage to open source ecosystem
- **TrapDoor Campaign**: Coordinated cross-ecosystem supply chain attackers targeting multiple package repositories
- **Megalodon Malware Operators**: Compromising thousands of GitHub repositories in six-hour timeframe
- **Russian-backed Infrastructure**: Operators of seized hosting infrastructure used for cyberattacks and influence operations