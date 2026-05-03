# Exploitation Report

A critical wave of exploitation activity is currently impacting organizations worldwide, with the most significant threat being the mass exploitation of a newly disclosed cPanel vulnerability tracked as CVE-2026-41940 for "Sorry" ransomware deployments. Concurrently, sophisticated attack campaigns are leveraging automated OAuth abuse techniques targeting Azure environments, while supply chain attacks are compromising popular Python packages and development ecosystems. North Korean threat actors continue their aggressive cryptocurrency theft operations, representing 76% of all crypto stolen in 2026, while Chinese-aligned groups are conducting extensive espionage campaigns across Asian governments and NATO states.

## Active Exploitation Details

### Critical cPanel Vulnerability
- **Description**: A newly disclosed critical flaw in cPanel infrastructure that allows attackers to breach websites and deploy ransomware
- **Impact**: Complete website compromise leading to data encryption and ransomware deployment
- **Status**: Currently being mass-exploited in active "Sorry" ransomware attacks
- **CVE ID**: CVE-2026-41940

### ConsentFix v3 OAuth Abuse
- **Description**: Automated OAuth abuse technique targeting Azure environments with enhanced scaling capabilities
- **Impact**: Unauthorized access to Azure resources and potential privilege escalation
- **Status**: Actively circulating on hacker forums with automation tools available

### Supply Chain Package Poisoning
- **Description**: Malicious versions of popular development packages including PyTorch Lightning, Ruby Gems, and Go modules
- **Impact**: Credential theft, GitHub Actions tampering, and CI/CD pipeline compromise
- **Status**: Active compromise of multiple package repositories

### SAP Package Compromise - Mini Shai-Hulud Attack
- **Description**: TeamPCP threat group targeting npm packages within SAP's cloud application development ecosystem
- **Impact**: Supply chain compromise affecting SAP development environments
- **Status**: Ongoing attacks by TeamPCP expanding their supply chain targeting

## Affected Systems and Products

- **cPanel Infrastructure**: Web hosting control panels vulnerable to CVE-2026-41940 exploitation
- **Microsoft Azure**: OAuth systems targeted by automated ConsentFix v3 attacks
- **Python Package Index (PyPI)**: PyTorch Lightning and Intercom-client packages compromised
- **Ruby Gems Repository**: Multiple poisoned gems targeting CI/CD pipelines
- **Go Modules**: Malicious packages exploiting development workflows
- **SAP Cloud Development**: npm packages within SAP ecosystem compromised
- **Facebook Accounts**: 30,000 accounts compromised via Google AppSheet phishing
- **Trellix Systems**: Source code repositories breached with unauthorized access
- **Canvas Learning Platform**: Instructure systems affected by cybersecurity incident
- **Windows 11 Systems**: Backup software failures caused by KB5083769 update

## Attack Vectors and Techniques

- **Ransomware Deployment**: Mass exploitation of cPanel vulnerability for "Sorry" ransomware distribution
- **OAuth Abuse**: Automated techniques for compromising Azure Single Sign-On systems
- **Supply Chain Poisoning**: Sleeper packages in development repositories delivering malicious payloads
- **Phishing Relay**: Google AppSheet used as phishing infrastructure for Facebook account compromise
- **Vishing and SSO Abuse**: Cybercrime groups conducting rapid SaaS environment attacks
- **AI-Assisted Development**: Malicious use of AI tools for phishing campaign generation
- **Repository Compromise**: Direct targeting of source code repositories

## Threat Actor Activities

- **Sorry Ransomware Group**: Mass exploitation campaign targeting cPanel infrastructure for data encryption
- **TeamPCP**: Expanding supply chain attacks to SAP development packages with Mini Shai-Hulud techniques
- **North Korean APT Groups**: Historic cryptocurrency theft operations accounting for 76% of 2026 crypto theft
- **Chinese-Aligned APT**: Espionage campaign targeting Asian governments, NATO states, journalists, and activists
- **Vietnamese Phishing Operation**: Large-scale Facebook account compromise using Google AppSheet infrastructure
- **BlackCat Ransomware Affiliates**: Continuing operations despite law enforcement actions and insider arrests
- **Romanian Swatting Ring**: Coordinated attacks against public officials and journalists
- **French Data Breach Actor**: 15-year-old detained for selling stolen government agency data