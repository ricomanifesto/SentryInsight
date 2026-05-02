# Exploitation Report

The current cybersecurity landscape reveals a diverse array of active exploitation activities targeting multiple vectors. Notable threats include sophisticated OAuth abuse campaigns targeting Azure environments through ConsentFix v3 attacks, large-scale phishing operations compromising thousands of Facebook accounts via Google AppSheet, and supply chain attacks targeting software development environments through poisoned Ruby Gems and Go modules. Additionally, cybercrime groups are conducting rapid SaaS extortion attacks using vishing and SSO abuse techniques, while nation-state actors continue extensive espionage campaigns against government and defense sectors across Asia and Europe.

## Active Exploitation Details

### ConsentFix v3 OAuth Abuse
- **Description**: An automated OAuth abuse technique targeting Azure environments with enhanced scaling capabilities
- **Impact**: Unauthorized access to Azure resources through manipulated OAuth consent flows
- **Status**: Actively being deployed by threat actors with automated tooling available on hacker forums

### Google AppSheet Phishing Campaign
- **Description**: Vietnamese-linked phishing operation using Google AppSheet as a relay to distribute malicious emails
- **Impact**: Compromise of approximately 30,000 Facebook accounts through credential harvesting
- **Status**: Active campaign with ongoing credential theft operations

### Software Supply Chain Attacks (Ruby Gems and Go Modules)
- **Description**: Malicious packages distributed through software repositories to exploit CI/CD pipelines
- **Impact**: Credential theft, GitHub Actions tampering, and unauthorized access to development environments
- **Status**: Active campaign using sleeper packages to deploy subsequent malicious payloads

### PyTorch Lightning Package Compromise
- **Description**: Compromise of the popular Python package Lightning with malicious versions pushed to PyPI
- **Impact**: Credential theft from developer environments using the compromised package
- **Status**: Malicious versions identified and targeted for remediation

### BlackCat Ransomware Operations
- **Description**: Ransomware-as-a-Service operation targeting various organizations with insider assistance
- **Impact**: Data encryption, extortion, and significant financial losses to victim organizations
- **Status**: Ongoing operations despite law enforcement actions against facilitators

## Affected Systems and Products

- **Microsoft Azure**: OAuth consent mechanisms and SSO integrations vulnerable to abuse
- **Facebook/Meta Platforms**: User accounts compromised through phishing campaigns
- **Google AppSheet**: Legitimate service abused as phishing relay infrastructure
- **Python Package Index (PyPI)**: Distribution platform for malicious Lightning package versions
- **Ruby Gems Repository**: Platform used for distributing poisoned packages
- **Go Modules**: Package management system targeted for supply chain attacks
- **SAP Development Packages**: npm packages for SAP cloud application development compromised
- **Windows 11**: Backup software functionality disrupted by security updates
- **CI/CD Pipelines**: Development environments targeted for credential harvesting

## Attack Vectors and Techniques

- **OAuth Consent Abuse**: Automated manipulation of Azure OAuth flows to gain unauthorized access
- **Phishing Relay**: Using legitimate Google AppSheet service to distribute phishing emails
- **Supply Chain Poisoning**: Injection of malicious code into popular software packages
- **Vishing and SSO Abuse**: Voice phishing combined with single sign-on exploitation for SaaS environments
- **Insider Assistance**: Use of compromised cybersecurity professionals to facilitate ransomware attacks
- **Package Typosquatting**: Distribution of malicious packages with similar names to legitimate software
- **CI Pipeline Exploitation**: Targeting continuous integration systems for credential theft

## Threat Actor Activities

- **Vietnamese Cybercrime Groups**: Conducting large-scale Facebook account compromise operations using Google services
- **ConsentFix Operators**: Developing and distributing automated OAuth abuse tools on underground forums
- **Supply Chain Attackers**: Systematic compromise of software repositories targeting developer environments
- **BlackCat Affiliates**: Ransomware operations with insider assistance from compromised security professionals
- **China-aligned APT Groups**: Espionage campaigns targeting Asian governments, NATO states, journalists, and activists
- **North Korean Threat Actors**: Cryptocurrency theft operations accounting for 76% of all stolen crypto in 2026
- **TeamPCP**: Supply chain attacks expanding to target SAP development ecosystems
- **Romanian Cybercriminals**: Operating swatting rings and cargo theft operations