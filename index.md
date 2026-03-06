# Exploitation Report

Critical exploitation activity is currently affecting multiple sectors with several high-severity vulnerabilities under active attack. Cisco Catalyst SD-WAN Manager systems face immediate threats from two actively exploited vulnerabilities, while threat actors are leveraging new malware campaigns targeting telecommunications infrastructure and government entities. Notable activity includes Chinese state-sponsored groups deploying advanced malware toolkits against South American telecommunications providers, Iranian-linked APT groups using sophisticated backdoors against U.S. networks, and Russian campaigns targeting Ukrainian entities with previously undocumented malware families. Additionally, WordPress membership plugins and surveillance systems have been compromised, while Google reports tracking 90 zero-day vulnerabilities that were actively exploited throughout 2025.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Vulnerabilities
- **Description**: Two security flaws in Cisco Catalyst SD-WAN Manager (formerly SD-WAN vManage) are being actively exploited by threat actors
- **Impact**: Unauthorized access to SD-WAN management infrastructure, potential network compromise
- **Status**: Under active exploitation, patches available from Cisco

### WordPress User Registration & Membership Plugin Vulnerability
- **Description**: Critical vulnerability in the User Registration & Membership plugin affecting over 60,000 WordPress sites
- **Impact**: Attackers can create administrative accounts on vulnerable WordPress installations
- **Status**: Currently being exploited to create unauthorized admin accounts

### Hikvision Security Vulnerability
- **Description**: High-severity security flaw with CVSS score of 9.8 affecting Hikvision products
- **Impact**: Critical system compromise potential
- **Status**: Added to CISA Known Exploited Vulnerabilities (KEV) catalog

### Rockwell Automation Security Vulnerability
- **Description**: Critical vulnerability with CVSS score of 9.8 in Rockwell Automation products
- **Impact**: Potential industrial control system compromise
- **Status**: Added to CISA Known Exploited Vulnerabilities (KEV) catalog

### Wikipedia JavaScript Worm
- **Description**: Self-propagating JavaScript worm that targeted the Wikimedia Foundation infrastructure
- **Impact**: Page vandalization and modification of user scripts across multiple wikis
- **Status**: Security incident contained by Wikimedia Foundation

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Network management systems vulnerable to active exploitation
- **WordPress Sites**: Over 60,000 sites using User Registration & Membership plugin at risk
- **Hikvision Products**: Video surveillance and security systems with critical vulnerabilities
- **Rockwell Automation Systems**: Industrial control and automation products
- **Telecommunications Infrastructure**: South American telecom providers targeted by Chinese APT groups
- **U.S. Banking and Airlines**: Networks infiltrated by Iranian MuddyWater group
- **Ukrainian Government Entities**: Targeted by Russian APT28-linked campaigns
- **Iraqi Government Officials**: Targeted by Iran-nexus Dust Specter group
- **FBI Surveillance Systems**: Warrant management and wiretap systems breached
- **Wikipedia/Wikimedia**: Multiple wiki platforms affected by JavaScript worm

## Attack Vectors and Techniques

- **Social Engineering**: ClickFix campaigns using Windows Terminal to deploy Lumma Stealer malware
- **Supply Chain Attacks**: Fake GitHub repositories promoted through Microsoft Bing AI search results
- **Malware Deployment**: Advanced persistent threat groups using custom backdoors and loaders
- **Phishing-as-a-Service**: Tycoon 2FA platform enabling large-scale credential harvesting attacks
- **JavaScript Exploitation**: Self-propagating worm targeting wiki platform vulnerabilities
- **Business Email Compromise**: Large-scale fraud operations targeting U.S. businesses
- **Network Edge Compromise**: APT groups targeting edge devices and network infrastructure
- **Credential Harvesting**: Adversary-in-the-middle attacks bypassing multi-factor authentication

## Threat Actor Activities

- **MuddyWater (Iranian APT)**: Deploying new Dindoor backdoor against U.S. companies including banks and airlines
- **UAT-9244 (Chinese APT)**: Targeting South American telecommunications with TernDoor, PeerTime, and BruteEntry malware toolkit
- **APT28 (Russian)**: Deploying BadPaw loader and MeowMeow backdoor in campaigns against Ukrainian entities
- **Dust Specter (Iran-nexus)**: Targeting Iraqi government officials with SPLITDROP and GHOSTFORM malware while impersonating Ministry of Foreign Affairs
- **APT36 (Pakistan)**: Using AI-powered malware assembly techniques to scale malicious code production
- **ClickFix Campaign Operators**: Leveraging Windows Terminal in sophisticated social engineering attacks
- **Tycoon 2FA Operators**: Running phishing-as-a-service platform linked to 64,000 attacks before law enforcement takedown
- **LeakBase Forum Administrators**: Operating large-scale stolen credentials marketplace before FBI and Europol seizure