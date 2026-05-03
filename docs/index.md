# Exploitation Report

Critical exploitation activity is currently dominated by several high-impact vulnerabilities and attack campaigns. CISA has added a Linux root access vulnerability CVE-2026-31431 to its Known Exploited Vulnerabilities catalog due to active exploitation in the wild. Simultaneously, a critical cPanel flaw CVE-2026-41940 is being mass-exploited in "Sorry" ransomware attacks, targeting web hosting infrastructure. Supply chain attacks have intensified with poisoned Ruby Gems and Go modules targeting CI pipelines for credential theft, while North Korean threat actors continue their aggressive cryptocurrency theft operations, now controlling 76% of all crypto stolen in 2026.

## Active Exploitation Details

### Linux Root Access Vulnerability
- **Description**: A security flaw impacting various Linux distributions that allows unauthorized root access
- **Impact**: Complete system compromise with administrative privileges
- **Status**: Recently disclosed and actively exploited, added to CISA KEV catalog
- **CVE ID**: CVE-2026-31431

### Critical cPanel Vulnerability
- **Description**: A critical flaw in cPanel web hosting control panel software
- **Impact**: Website breaches and data encryption in ransomware attacks
- **Status**: Mass-exploited in "Sorry" ransomware campaign
- **CVE ID**: CVE-2026-41940

### Poisoned Software Packages
- **Description**: Malicious Ruby Gems and Go modules deployed as sleeper packages in software repositories
- **Impact**: Credential theft, GitHub Actions tampering, and CI pipeline compromise
- **Status**: Active supply chain attack campaign targeting development environments

### PyTorch Lightning Package Compromise
- **Description**: Popular Python package Lightning compromised with two malicious versions
- **Impact**: Credential theft through compromised package installations
- **Status**: Active supply chain attack affecting Python development environments

## Affected Systems and Products

- **Linux Distributions**: Various distributions affected by root access vulnerability
- **cPanel Systems**: Web hosting platforms using cPanel control panel software
- **CI/CD Pipelines**: Development environments using Ruby Gems and Go modules
- **Python Development**: Systems using PyTorch Lightning and Intercom-client packages
- **SAP Development**: npm packages for SAP's cloud application development ecosystem
- **Azure Environments**: OAuth-enabled systems targeted by ConsentFix v3 attacks
- **Facebook Accounts**: 30,000 accounts compromised through Google AppSheet phishing

## Attack Vectors and Techniques

- **ConsentFix v3**: Automated OAuth abuse targeting Azure environments with enhanced scaling capabilities
- **Phishing Relay**: Google AppSheet used as intermediate platform to distribute phishing emails
- **Supply Chain Poisoning**: Malicious packages uploaded to legitimate software repositories
- **Vishing and SSO Abuse**: Voice phishing combined with single sign-on exploitation for rapid SaaS extortion
- **AI-Assisted Phishing**: Bluekit phishing service includes AI assistant for campaign generation
- **Mini Shai-Hulud Attack**: TeamPCP targeting SAP packages in supply chain attacks

## Threat Actor Activities

- **North Korean Groups**: Conducting historic cryptocurrency heists, controlling 76% of all crypto stolen in 2026, potentially using AI assistance
- **Vietnamese-Linked Operation**: Using Google AppSheet as phishing relay to compromise 30,000 Facebook accounts
- **China-Aligned Espionage**: Targeting government and defense sectors across South, East, and Southeast Asia, plus one European government
- **Sorry Ransomware Group**: Mass-exploiting cPanel vulnerability for website encryption attacks
- **TeamPCP**: Expanding supply chain attacks to target SAP development packages
- **BlackCat Ransomware Affiliates**: Two cybersecurity professionals sentenced for facilitating attacks
- **Romanian Swatting Ring**: Leader sentenced for targeting 75+ public officials and journalists