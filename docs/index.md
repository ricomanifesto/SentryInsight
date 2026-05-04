# Exploitation Report

Critical vulnerabilities are currently under active exploitation across multiple platforms, posing significant risks to organizations worldwide. The most severe threats include a Linux root access vulnerability (CVE-2026-31431) that CISA has added to its Known Exploited Vulnerabilities catalog, and a critical cPanel flaw (CVE-2026-41940) being mass-exploited in "Sorry" ransomware attacks. Additionally, threat actors are leveraging sophisticated attack vectors including Telegram Mini Apps for malware distribution, automated OAuth abuse targeting Azure environments, poisoned software packages in CI pipelines, and large-scale phishing campaigns compromising thousands of Facebook accounts.

## Active Exploitation Details

### Linux Root Access Vulnerability
- **Description**: A recently disclosed security flaw impacting various Linux distributions that enables attackers to gain root-level access to affected systems
- **Impact**: Complete system compromise with administrative privileges, potentially allowing full control over affected Linux systems
- **Status**: Actively exploited in the wild and added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-31431

### Critical cPanel Vulnerability
- **Description**: A critical security flaw in cPanel that is being exploited for data encryption attacks
- **Impact**: Website compromise leading to data encryption and ransomware deployment
- **Status**: Mass exploitation ongoing with "Sorry" ransomware attacks
- **CVE ID**: CVE-2026-41940

### Software Supply Chain Attacks
- **Description**: Poisoned Ruby Gems and Go Modules deployed as sleeper packages in software repositories
- **Impact**: Credential theft, GitHub Actions tampering, and compromise of CI/CD pipelines
- **Status**: Active campaign targeting development environments

## Affected Systems and Products

- **Linux Distributions**: Various distributions affected by root access vulnerability
- **cPanel Hosting Platforms**: Web hosting environments using vulnerable cPanel versions
- **Azure Environments**: Microsoft Azure platforms targeted by automated OAuth abuse
- **Telegram Ecosystem**: Mini Apps feature being exploited for malware distribution
- **Facebook Accounts**: Over 30,000 accounts compromised through phishing campaigns
- **SAP Development Packages**: npm packages in SAP's cloud application development ecosystem
- **Development Environments**: Ruby Gems and Go Modules repositories compromised
- **Educational Technology**: Canvas learning platform and Instructure systems

## Attack Vectors and Techniques

- **ConsentFix v3 Attacks**: Automated OAuth abuse techniques targeting Azure with scaling potential and minimal detection
- **Telegram Mini App Abuse**: Exploitation of Telegram's Mini App feature for crypto scams and Android malware delivery
- **Google AppSheet Phishing**: Vietnamese-linked operation using Google AppSheet as a phishing relay for Facebook account compromise
- **Supply Chain Poisoning**: Deployment of malicious packages in Ruby Gems and Go Modules repositories
- **Vishing and SSO Abuse**: Rapid SaaS extortion attacks combining voice phishing with single sign-on exploitation
- **AI-Enhanced Phishing**: Bluekit phishing service featuring AI assistant and 40+ templates for campaign generation

## Threat Actor Activities

- **ShinyHunters**: Data breach activities targeting educational technology company Instructure
- **Sorry Ransomware Group**: Mass exploitation of cPanel vulnerabilities for data encryption attacks
- **Vietnamese Cybercriminals**: Large-scale Facebook phishing operation compromising 30,000 accounts via Google AppSheet
- **North Korean APT Groups**: Responsible for 76% of all cryptocurrency theft in 2026, conducting historic heists with potential AI assistance
- **China-Aligned Espionage Groups**: Targeting Asian governments, NATO states, journalists, and activists across multiple regions
- **TeamPCP**: Supply chain attacks targeting SAP packages with "Mini Shai-Hulud" attack methodology
- **BlackCat Ransomware Affiliates**: Ongoing ransomware operations with insider assistance from cybersecurity professionals
- **Cybercrime Groups**: Rapid SaaS extortion attacks using vishing and SSO abuse techniques