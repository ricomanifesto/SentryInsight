# Exploitation Report

Critical exploitation activity is currently affecting multiple platforms and systems, with significant threats spanning Linux distributions, web hosting infrastructure, and cloud environments. Active exploitation includes a Linux root access vulnerability affecting various distributions that has been added to CISA's Known Exploited Vulnerabilities catalog, mass exploitation of a critical cPanel flaw being leveraged in ransomware campaigns, and sophisticated attacks targeting Azure environments through OAuth abuse. Additionally, supply chain attacks are targeting development environments through compromised packages in popular repositories, while threat actors are conducting rapid SaaS extortion attacks using voice phishing and SSO abuse techniques.

## Active Exploitation Details

### Linux Root Access Vulnerability
- **Description**: A recently disclosed security flaw impacting various Linux distributions that allows attackers to gain root access
- **Impact**: Complete system compromise with administrative privileges
- **Status**: Actively exploited in the wild and added to CISA KEV catalog
- **CVE ID**: CVE-2026-31431

### cPanel Critical Vulnerability
- **Description**: A critical security flaw in cPanel hosting control panel software
- **Impact**: Mass exploitation leading to website breaches and data encryption in ransomware attacks
- **Status**: Being mass-exploited by "Sorry" ransomware operators
- **CVE ID**: CVE-2026-41940

### Lightning Python Package Compromise
- **Description**: The popular PyTorch Lightning Python package was compromised with malicious versions pushed to PyPI repository
- **Impact**: Credential theft from development environments and CI/CD pipelines
- **Status**: Active supply chain attack affecting Python developers

### Ruby Gems and Go Modules Supply Chain Attack
- **Description**: Sleeper packages in Ruby Gems and Go Modules repositories used to deliver malicious payloads
- **Impact**: Credential theft, GitHub Actions tampering, and development environment compromise
- **Status**: Ongoing campaign targeting CI/CD pipelines

### SAP Package Compromise
- **Description**: Several npm packages for SAP's cloud application development ecosystem compromised in "Mini Shai-Hulud" attack
- **Impact**: Supply chain compromise affecting SAP development environments
- **Status**: Active compromise by TeamPCP threat group

## Affected Systems and Products

- **Linux Distributions**: Various distributions affected by root access vulnerability
- **cPanel Hosting**: Web hosting platforms using cPanel control panel software
- **PyTorch Lightning**: Python machine learning development package
- **Azure Active Directory**: Cloud identity platform targeted by ConsentFix v3 OAuth abuse
- **Ruby Gems Repository**: Ruby package management system
- **Go Modules Repository**: Go programming language package system
- **SAP Cloud Development**: npm packages for SAP's cloud application ecosystem
- **Facebook Accounts**: 30,000 accounts compromised via Google AppSheet phishing
- **France Titres (ANTS)**: French government administrative document agency

## Attack Vectors and Techniques

- **ConsentFix v3**: Automated OAuth abuse targeting Azure environments with enhanced scaling capabilities
- **Supply Chain Attacks**: Malicious packages in software repositories targeting development environments
- **Phishing-as-a-Service**: Bluekit service offering 40+ templates and AI-assisted campaign generation
- **Google AppSheet Abuse**: Vietnamese-linked operation using Google AppSheet as phishing relay
- **Vishing and SSO Abuse**: Voice phishing combined with single sign-on exploitation for rapid SaaS attacks
- **Ransomware Deployment**: "Sorry" ransomware leveraging cPanel vulnerabilities for mass attacks

## Threat Actor Activities

- **Vietnamese Phishing Group**: Compromised 30,000 Facebook accounts using Google AppSheet phishing relay infrastructure
- **TeamPCP**: Conducting "Mini Shai-Hulud" supply chain attacks against SAP development packages
- **Sorry Ransomware Operators**: Mass-exploiting cPanel vulnerability for widespread ransomware deployment
- **China-Aligned APT**: Espionage campaign targeting Asian governments, NATO states, journalists, and activists
- **North Korean Groups**: Responsible for 76% of all cryptocurrency theft in 2026, leveraging AI assistance
- **Cybercrime Groups**: Conducting rapid SaaS extortion attacks using vishing and SSO abuse techniques
- **French Data Breach Suspect**: 15-year-old detained for selling stolen French government agency data
- **BlackCat Ransomware Affiliates**: Two cybersecurity professionals sentenced to 4 years for facilitating attacks