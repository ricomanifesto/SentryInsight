# Exploitation Report

The current threat landscape reveals several critical exploitation activities across multiple platforms and systems. Most notably, a critical cPanel vulnerability is being mass-exploited in "Sorry" ransomware attacks, while a Linux root access bug has been added to CISA's Known Exploited Vulnerabilities catalog. Additionally, sophisticated supply chain attacks are targeting CI/CD pipelines through poisoned Ruby gems and Go modules, and threat actors are leveraging Telegram Mini Apps for crypto scams and malware distribution. The security community is also dealing with a Microsoft Defender false positive issue affecting DigiCert certificates and various social engineering campaigns targeting SaaS environments.

## Active Exploitation Details

### Critical cPanel Vulnerability
- **Description**: A critical flaw in cPanel that allows unauthorized access to web hosting control panels
- **Impact**: Attackers can breach websites and encrypt data in ransomware attacks
- **Status**: Currently being mass-exploited in active "Sorry" ransomware campaigns
- **CVE ID**: CVE-2026-41940

### Linux Root Access Bug
- **Description**: A security vulnerability affecting various Linux distributions that enables privilege escalation to root access
- **Impact**: Attackers can gain complete administrative control over affected Linux systems
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog, indicating active exploitation in the wild
- **CVE ID**: CVE-2026-31431

### Poisoned Ruby Gems and Go Modules
- **Description**: Malicious packages distributed through Ruby gems and Go modules repositories designed to exploit CI/CD pipelines
- **Impact**: Enables credential theft, GitHub Actions tampering, and supply chain compromise
- **Status**: Active campaign targeting software development environments

### Telegram Mini Apps Abuse
- **Description**: Exploitation of Telegram's Mini App feature to run fraudulent operations and distribute malware
- **Impact**: Crypto scams, brand impersonation, and Android malware delivery
- **Status**: Large-scale fraud operation currently active

## Affected Systems and Products

- **cPanel**: Web hosting control panel software affected by critical vulnerability
- **Linux Distributions**: Various Linux distributions vulnerable to privilege escalation attack
- **Ruby Gems Repository**: Compromised packages targeting Ruby development environments
- **Go Modules Repository**: Malicious modules affecting Go development pipelines
- **Telegram Platform**: Mini Apps feature being abused for malicious activities
- **Microsoft Defender**: False positive detection affecting DigiCert root certificates
- **SAP Cloud Development**: npm packages for SAP's cloud application development ecosystem compromised
- **Facebook Accounts**: Approximately 30,000 accounts compromised through phishing campaign
- **Google AppSheet**: Platform being used as phishing relay in Facebook account compromise attacks

## Attack Vectors and Techniques

- **Mass Exploitation**: Automated scanning and exploitation of cPanel vulnerabilities for ransomware deployment
- **Supply Chain Attacks**: Distribution of malicious packages through legitimate software repositories
- **Privilege Escalation**: Exploitation of Linux vulnerabilities to gain root access
- **Social Engineering**: Vishing and SSO abuse in rapid SaaS extortion attacks
- **Phishing Campaigns**: Google AppSheet used as relay for Facebook account compromise
- **Platform Abuse**: Legitimate Telegram features weaponized for fraudulent activities
- **OAuth Manipulation**: ConsentFix v3 attacks targeting Azure with automated OAuth abuse
- **CI/CD Pipeline Exploitation**: Targeting development environments through poisoned dependencies

## Threat Actor Activities

- **ShinyHunters**: Claimed responsibility for Instructure data breach attack
- **Sorry Ransomware Group**: Conducting mass exploitation of cPanel vulnerabilities for data encryption
- **Vietnamese-Linked Operation**: Using Google AppSheet to distribute phishing emails targeting Facebook accounts
- **TeamPCP**: Broadening supply chain attacks with "Mini Shai-Hulud" attacks targeting SAP packages
- **Chinese-Aligned Espionage Groups**: Targeting government and defense sectors across South, East, and Southeast Asia, plus European government entities
- **North Korean Threat Actors**: Conducting historic cryptocurrency heists, accounting for 76% of all crypto stolen in 2026
- **BlackCat Ransomware Affiliates**: Conducting attacks with assistance from compromised cybersecurity professionals
- **ConsentFix v3 Operators**: Scaling OAuth abuse attacks against Azure environments with automation