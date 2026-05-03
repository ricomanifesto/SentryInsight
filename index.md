# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems across the cybersecurity landscape. The most severe threats include a mass-exploited cPanel vulnerability **CVE-2026-41940** being leveraged for "Sorry" ransomware attacks, and a Linux root access vulnerability **CVE-2026-31431** that has been added to CISA's Known Exploited Vulnerabilities catalog. Additionally, sophisticated attack campaigns are leveraging Telegram Mini Apps for cryptocurrency fraud and Android malware distribution, while automated OAuth abuse techniques are targeting Azure environments. Supply chain attacks are also prominent, with poisoned Ruby Gems and Go modules exploiting CI pipelines for credential theft, and TeamPCP conducting attacks against SAP packages.

## Active Exploitation Details

### Critical cPanel Vulnerability
- **Description**: A critical flaw in cPanel that enables attackers to breach websites and deploy ransomware
- **Impact**: Mass exploitation leading to data encryption in "Sorry" ransomware attacks
- **Status**: Actively being mass-exploited in the wild
- **CVE ID**: CVE-2026-41940

### Linux Root Access Bug
- **Description**: A security flaw affecting various Linux distributions that allows privilege escalation to root access
- **Impact**: Complete system compromise with administrative privileges
- **Status**: Actively exploited and added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-31431

### Poisoned Ruby Gems and Go Modules
- **Description**: Supply chain attack using sleeper packages in Ruby Gems and Go modules repositories
- **Impact**: Credential theft, GitHub Actions tampering, and CI pipeline compromise
- **Status**: Active campaign targeting software development environments

### Telegram Mini Apps Abuse
- **Description**: Large-scale fraud operation exploiting Telegram's Mini App feature
- **Impact**: Cryptocurrency scams, brand impersonation, and Android malware distribution
- **Status**: Ongoing exploitation targeting mobile users

## Affected Systems and Products

- **cPanel**: Web hosting control panel software affected by critical vulnerability
- **Linux Distributions**: Various Linux distributions vulnerable to root access exploitation
- **Ruby Gems**: Ruby package repository with compromised packages
- **Go Modules**: Go programming language module repository with malicious packages
- **Telegram Mini Apps**: Telegram's application platform being abused for fraud
- **Azure OAuth**: Microsoft Azure's OAuth implementation targeted by automated abuse
- **SAP Packages**: Several npm packages in SAP's cloud application development ecosystem
- **GitHub Actions**: CI/CD platform targeted for credential theft and tampering
- **Facebook Accounts**: Over 30,000 accounts compromised via phishing campaigns

## Attack Vectors and Techniques

- **Ransomware Deployment**: Mass exploitation of cPanel vulnerability for "Sorry" ransomware attacks
- **Privilege Escalation**: Linux vulnerability exploitation for root access
- **Supply Chain Poisoning**: Injection of malicious code into legitimate software packages
- **OAuth Abuse**: Automated ConsentFix v3 attacks targeting Azure environments
- **Phishing Campaigns**: Google AppSheet used as phishing relay for Facebook account compromise
- **Social Engineering**: Vishing and SSO abuse in rapid SaaS extortion attacks
- **Mobile Malware**: Android malware distribution through Telegram Mini Apps
- **CI Pipeline Compromise**: Targeting continuous integration systems for credential theft

## Threat Actor Activities

- **Romanian Swatting Ring**: Leader sentenced to 4 years for targeting public officials and journalists
- **BlackCat Ransomware Operators**: Two cybersecurity professionals sentenced to 4 years for facilitating attacks
- **TeamPCP**: Conducting "Mini Shai-Hulud" attacks against SAP packages in supply chain operations
- **Vietnamese-linked Groups**: Operating large-scale Facebook phishing campaigns using Google AppSheet
- **China-aligned Espionage**: Targeting Asian governments, NATO states, journalists, and activists
- **North Korean Actors**: Responsible for 76% of all cryptocurrency stolen in 2026
- **French Government Breach**: 15-year-old detained for data theft from France Titres (ANTS)
- **Cybercrime Groups**: Using vishing and SSO abuse for rapid SaaS extortion attacks