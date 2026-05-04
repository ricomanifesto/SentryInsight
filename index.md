# Exploitation Report

Critical vulnerabilities are currently under active exploitation, with CISA adding CVE-2026-31431, a Linux root access bug, to its Known Exploited Vulnerabilities catalog due to confirmed in-the-wild abuse. Additionally, CVE-2026-41940, a critical cPanel flaw, is being mass-exploited in "Sorry" ransomware campaigns targeting websites. The threat landscape also includes sophisticated supply chain attacks through poisoned Ruby Gems and Go modules, automated OAuth abuse targeting Azure environments, and large-scale phishing operations compromising thousands of Facebook accounts through Google AppSheet.

## Active Exploitation Details

### Linux Root Access Vulnerability
- **Description**: A recently disclosed security flaw affecting various Linux distributions that enables privilege escalation to root access
- **Impact**: Attackers can gain complete administrative control over compromised Linux systems
- **Status**: Actively exploited in the wild, prompting CISA to add it to the KEV catalog
- **CVE ID**: CVE-2026-31431

### Critical cPanel Vulnerability
- **Description**: A newly disclosed critical flaw in cPanel web hosting control panel software
- **Impact**: Enables attackers to breach websites and deploy "Sorry" ransomware for data encryption
- **Status**: Under mass exploitation for ransomware attacks
- **CVE ID**: CVE-2026-41940

### Supply Chain Package Poisoning
- **Description**: Malicious packages distributed through Ruby Gems and Go modules repositories targeting CI/CD pipelines
- **Impact**: Credential theft, GitHub Actions tampering, and supply chain compromise
- **Status**: Active campaign using sleeper packages as initial infection vectors

## Affected Systems and Products

- **Linux Distributions**: Various distributions affected by the root access vulnerability
- **cPanel Hosting Platforms**: Web hosting environments using vulnerable cPanel versions
- **Azure/Microsoft 365**: Organizations using OAuth and SSO integrations targeted by ConsentFix v3 attacks
- **Facebook Accounts**: Over 30,000 accounts compromised through Google AppSheet phishing campaigns
- **Telegram Mini Apps**: Platform being abused for crypto scams and Android malware distribution
- **Ruby and Go Development Environments**: CI/CD pipelines using compromised packages
- **SAP Cloud Development**: npm packages in SAP's ecosystem compromised by TeamPCP group

## Attack Vectors and Techniques

- **Privilege Escalation**: Linux kernel exploits enabling root access on compromised systems
- **Ransomware Deployment**: Mass exploitation of cPanel vulnerabilities for "Sorry" ransomware attacks
- **Automated OAuth Abuse**: ConsentFix v3 technique with enhanced automation and scaling capabilities
- **Phishing as a Service**: Google AppSheet used as phishing relay for Facebook account compromise
- **Supply Chain Attacks**: Poisoned packages in software repositories targeting development pipelines
- **Vishing and SSO Abuse**: Rapid SaaS extortion attacks with minimal forensic traces
- **Social Engineering**: Telegram Mini Apps used for brand impersonation and cryptocurrency scams

## Threat Actor Activities

- **Vietnamese Phishing Operation**: Large-scale Facebook account compromise using Google AppSheet as phishing infrastructure
- **TeamPCP Group**: Supply chain attacks targeting SAP packages with "Mini Shai-Hulud" techniques
- **Sorry Ransomware Operators**: Mass exploitation of cPanel vulnerabilities for website encryption
- **China-Linked Espionage Groups**: Targeting Asian governments, NATO states, journalists, and activists
- **BlackCat Ransomware Affiliates**: Operations facilitated by sentenced cybersecurity professionals
- **ConsentFix Operators**: Automated OAuth abuse campaigns circulating on hacker forums
- **Cryptocurrency Scammers**: Telegram Mini Apps abuse for crypto fraud and malware distribution
- **Romanian Swatting Ring**: Coordinated harassment campaigns against public officials and journalists