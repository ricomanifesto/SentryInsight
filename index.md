# Exploitation Report

Current cybersecurity threats show a significant rise in sophisticated attack techniques targeting cloud platforms, supply chain vulnerabilities, and legitimate business platforms. The most critical exploitation activity involves automated OAuth abuse campaigns against Azure environments, supply chain attacks compromising popular software packages including Ruby gems and PyTorch Lightning, and the emergence of AI-assisted phishing services. Additionally, threat actors are leveraging legitimate platforms like Google AppSheet for phishing campaigns and conducting rapid SaaS extortion attacks through vishing and SSO abuse techniques.

## Active Exploitation Details

### ConsentFix v3 OAuth Abuse
- **Description**: Automated OAuth abuse technique targeting Azure environments with enhanced automation and scaling capabilities
- **Impact**: Unauthorized access to Azure resources through compromised OAuth consent flows
- **Status**: Actively circulating on hacker forums with automated tooling

### Supply Chain Package Poisoning
- **Description**: Malicious packages distributed through Ruby gems and Go modules targeting CI/CD pipelines
- **Impact**: Credential theft, GitHub Actions tampering, and unauthorized access to development environments
- **Status**: Active campaign with sleeper packages designed to push malicious payloads

### PyTorch Lightning Package Compromise
- **Description**: Popular Python package Lightning compromised to distribute two malicious versions
- **Impact**: Credential theft from developers and organizations using the compromised package
- **Status**: Malicious versions pushed to PyPI repositories

### Google AppSheet Phishing Campaign
- **Description**: Vietnamese-linked operation using Google AppSheet as a "phishing relay" to distribute phishing emails
- **Impact**: Compromise of approximately 30,000 Facebook accounts
- **Status**: Active phishing campaign leveraging legitimate Google services

### TeamPCP Mini Shai-Hulud Attack
- **Description**: Supply chain attack targeting several npm packages within SAP's cloud application development ecosystem
- **Impact**: Compromise of SAP development environments and related applications
- **Status**: Active broadening of supply chain attack capabilities

## Affected Systems and Products

- **Azure Cloud Platform**: OAuth consent flows and authentication mechanisms
- **Ruby Gems Repository**: CI/CD pipeline components and development tools
- **Go Modules**: Development packages and continuous integration systems
- **PyTorch Lightning**: Python machine learning framework and dependent applications
- **Google AppSheet**: Legitimate Google service being abused for phishing
- **SAP Cloud Development Packages**: npm packages in SAP's development ecosystem
- **Facebook Accounts**: User credentials compromised through phishing campaigns
- **Windows 11 Systems**: Third-party backup software affected by KB5083769 update
- **GitHub Actions**: CI/CD workflows targeted for tampering and credential theft

## Attack Vectors and Techniques

- **OAuth Abuse**: Automated consent flow manipulation targeting Azure environments
- **Supply Chain Poisoning**: Distribution of malicious packages through legitimate repositories
- **Phishing Relay**: Using legitimate platforms like Google AppSheet to bypass security filters
- **Sleeper Packages**: Dormant malicious packages activated to deliver payloads
- **Vishing and SSO Abuse**: Voice phishing combined with single sign-on exploitation for rapid SaaS attacks
- **AI-Assisted Phishing**: Automated generation of phishing campaign content using AI tools
- **Package Typosquatting**: Compromising legitimate package names for malicious distribution

## Threat Actor Activities

- **Vietnamese-linked Groups**: Conducting large-scale Facebook credential harvesting using Google AppSheet phishing relays
- **TeamPCP**: Expanding supply chain attacks to target SAP development ecosystems with Mini Shai-Hulud techniques
- **ConsentFix v3 Operators**: Distributing automated OAuth abuse tools through underground forums
- **Supply Chain Attackers**: Targeting popular development packages including Ruby gems, Go modules, and Python packages
- **Cybercrime Groups**: Conducting rapid SaaS extortion attacks using vishing and SSO abuse techniques with minimal trace
- **BlackCat/ALPHV Affiliates**: Former cybersecurity professionals sentenced for facilitating ransomware attacks
- **North Korean Threat Actors**: Responsible for 76% of all cryptocurrency stolen in 2026 through historic heists
- **China-linked Espionage Groups**: Targeting government and defense sectors across Asia and European NATO states