# Exploitation Report

Critical cybersecurity incidents have emerged involving mass exploitation of cPanel infrastructure through CVE-2026-41940, leading to widespread "Sorry" ransomware deployments. Concurrently, sophisticated attack campaigns are targeting cloud environments through automated OAuth abuse, supply chain compromises affecting popular software packages, and coordinated phishing operations that have successfully compromised thousands of accounts. North Korean threat actors continue to dominate cryptocurrency theft operations, while Chinese-linked espionage groups expand their targeting of government entities across multiple continents.

## Active Exploitation Details

### Critical cPanel Vulnerability
- **Description**: A newly disclosed critical vulnerability in cPanel hosting management software
- **Impact**: Attackers can breach websites and deploy ransomware to encrypt data
- **Status**: Being mass-exploited in active "Sorry" ransomware attacks
- **CVE ID**: CVE-2026-41940

### ConsentFix v3 OAuth Abuse
- **Description**: Automated OAuth consent abuse attack targeting Microsoft Azure environments
- **Impact**: Unauthorized access to cloud resources through manipulated consent flows
- **Status**: Actively circulated on hacker forums with automation capabilities

### PyTorch Lightning Supply Chain Attack
- **Description**: Compromise of popular Python package Lightning with malicious versions
- **Impact**: Credential theft from developers and organizations using the compromised package
- **Status**: Active supply chain attack with malicious versions distributed

### Ruby Gems and Go Modules Supply Chain Attack
- **Description**: Sleeper packages used as conduits for malicious payloads in CI/CD pipelines
- **Impact**: Credential theft, GitHub Actions tampering, and unauthorized access to development environments
- **Status**: Active campaign targeting software development workflows

### TeamPCP SAP Package Compromise
- **Description**: Mini Shai-Hulud attack targeting npm packages in SAP's cloud application development ecosystem
- **Impact**: Supply chain compromise affecting SAP development environments
- **Status**: Active attacks broadening TeamPCP's supply chain targeting scope

## Affected Systems and Products

- **cPanel**: Hosting management software vulnerable to mass exploitation
- **Microsoft Azure**: OAuth consent flows targeted by automated abuse campaigns
- **PyTorch Lightning**: Python machine learning framework compromised in package repositories
- **Ruby Gems**: Ruby package ecosystem targeted with malicious gems
- **Go Modules**: Go programming language packages compromised in CI pipelines
- **SAP npm packages**: Cloud application development packages targeted by TeamPCP
- **Intercom-client**: Python package compromised for credential theft
- **Facebook**: 30,000 accounts compromised through Google AppSheet phishing relay
- **Windows 11**: Third-party backup software failures following security updates

## Attack Vectors and Techniques

- **Mass Ransomware Deployment**: Exploitation of cPanel vulnerability for "Sorry" ransomware distribution
- **Automated OAuth Abuse**: ConsentFix v3 technique with scaling potential and automation features
- **Supply Chain Poisoning**: Multiple campaigns targeting package repositories with malicious code
- **Phishing Relay**: Google AppSheet used as intermediary platform for Facebook account compromise
- **Vishing Combined with SSO Abuse**: Voice phishing integrated with single sign-on exploitation for SaaS extortion
- **AI-Assisted Phishing**: Bluekit service offering 40+ templates with AI-generated campaign drafts
- **Sleeper Package Strategy**: Dormant malicious packages activated after gaining trust in repositories

## Threat Actor Activities

- **North Korean Groups**: Dominating cryptocurrency theft operations with 76% of all crypto stolen in 2026
- **Chinese-Linked Espionage Groups**: Targeting Asian governments, NATO states, journalists, and activists across South, East, and Southeast Asia plus European governments
- **Vietnamese-Linked Operation**: Using Google AppSheet phishing relay to compromise 30,000 Facebook accounts
- **TeamPCP**: Expanding supply chain attacks to include SAP package ecosystem with Mini Shai-Hulud techniques
- **BlackCat/ALPHV Affiliates**: Former cybersecurity professionals sentenced for facilitating ransomware operations
- **Romanian Swatting Ring**: Leader sentenced for targeting 75+ public officials, journalists, and religious institutions
- **Cargo Theft Cybercriminals**: FBI reports sharp surge in cyber-enabled cargo theft with significant losses across US and Canada