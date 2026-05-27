# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms, with CISA issuing emergency directives for federal agencies to patch critical flaws within days. The most concerning activity involves zero-day exploitation of KnowledgeDeliver LMS systems leading to web shell deployment, active exploitation of cPanel and Drupal vulnerabilities with federal government targeting, and a massive Ghost CMS compromise affecting over 700 websites for ClickFix attacks. Microsoft has also released emergency patches for SharePoint remote code execution vulnerabilities, while threat actors are leveraging AI chatbots to distribute cryptojacking malware and conducting sophisticated supply chain attacks through GitHub repository compromises.

## Active Exploitation Details

### LiteSpeed cPanel Plugin Vulnerability
- **Description**: Critical vulnerability in LiteSpeed cPanel user-end plugin allowing unauthorized access to servers
- **Impact**: Complete server compromise and potential lateral movement across federal infrastructure
- **Status**: Under active exploitation; CISA mandated federal agencies patch within 4 days

### KnowledgeDeliver Learning Management System Zero-Day
- **Description**: Critical zero-day vulnerability in Digital Knowledge KnowledgeDeliver LMS popular in Japan
- **Impact**: Remote code execution enabling deployment of Godzilla web shells and Cobalt Strike beacons
- **Status**: Exploited as zero-day before patch availability; now patched but exploitation continues

### Drupal SQL Injection Vulnerability
- **Description**: SQL injection vulnerability in Drupal content management system affecting government servers
- **Impact**: Database compromise, data extraction, and potential administrative access
- **Status**: Under active exploitation; CISA ordered federal agencies to patch by Wednesday evening

### SharePoint Remote Code Execution Flaw
- **Description**: Remote code execution vulnerability affecting multiple SharePoint Server versions
- **Impact**: Full system compromise without specialized conditions required
- **Status**: Microsoft issued out-of-band emergency patch
- **CVE ID**: CVE-2026-45659

### Ghost CMS Critical Vulnerability
- **Description**: Critical security flaw in Ghost content management system enabling JavaScript injection
- **Impact**: Website hijacking for ClickFix attack campaigns targeting user credentials
- **Status**: Over 700 websites compromised; ongoing exploitation for malicious JavaScript injection
- **CVE ID**: CVE-2026-26980

## Affected Systems and Products

- **LiteSpeed cPanel Plugin**: Federal government servers running affected plugin versions
- **KnowledgeDeliver LMS**: Japanese organizations using Digital Knowledge learning management systems
- **Drupal CMS**: Government and enterprise content management installations
- **SharePoint Server**: Multiple versions across enterprise environments
- **Ghost CMS**: Over 700 websites compromised for ClickFix campaigns
- **GitHub Repositories**: Over 5,500 repositories infected with Megalodon malware
- **Microsoft 365**: Accounts targeted through Kali365 phishing-as-a-service platform

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities before disclosure
- **Web Shell Deployment**: Godzilla web shells installed through KnowledgeDeliver compromise
- **SQL Injection**: Database manipulation through Drupal vulnerability exploitation
- **JavaScript Injection**: Malicious code injection through Ghost CMS compromise
- **AI-Assisted Cryptojacking**: Manipulation of AI chatbot recommendations to redirect users to malicious sites
- **Supply Chain Poisoning**: Mass GitHub repository compromise through Megalodon malware campaign
- **OAuth Device Code Abuse**: Kali365 platform exploiting Microsoft 365 authentication mechanisms
- **DLL Side-Loading**: Advanced persistence techniques used by state-sponsored actors
- **Phishing-as-a-Service**: Commercialized credential theft operations targeting enterprise accounts

## Threat Actor Activities

- **MuddyWater (Iranian APT)**: Conducting espionage campaigns across 9 countries using DLL side-loading techniques targeting government and critical infrastructure
- **Nimbus Manticore (Iranian State-Sponsored)**: Deploying MiniFast and MiniJunk V2 malware through aviation industry phishing and SEO poisoning campaigns
- **ShinyHunters Extortion Group**: Conducting data breaches against Charter Communications and 7-Eleven, affecting over 185,000 individuals with extortion demands
- **TeamPCP**: Orchestrating Shai-Hulud worm attacks causing significant damage to open source ecosystem
- **Megalodon Campaign Operators**: Executing massive GitHub supply chain attack affecting 5,500+ repositories in 6-hour timeframe
- **ClickFix Campaign Actors**: Leveraging Ghost CMS vulnerabilities to hijack 700+ websites for credential theft operations
- **Kali365 Operators**: Running phishing-as-a-service platform specifically targeting Microsoft 365 enterprise accounts