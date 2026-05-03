# Exploitation Report

Current threat landscapes reveal several critical exploitation campaigns targeting diverse systems and platforms. CISA has added a Linux root access vulnerability CVE-2026-31431 to its Known Exploited Vulnerabilities catalog, indicating active exploitation in the wild. A critical cPanel flaw CVE-2026-41940 is being mass-exploited in "Sorry" ransomware attacks, compromising websites globally. Additionally, sophisticated supply chain attacks are targeting software packages including PyTorch Lightning and Ruby Gems, while advanced OAuth abuse techniques called ConsentFix v3 are targeting Azure environments. North Korean threat actors continue their cryptocurrency theft operations, accounting for 76% of all crypto stolen in 2026, while Vietnamese-linked campaigns have compromised over 30,000 Facebook accounts through Google AppSheet phishing relays.

## Active Exploitation Details

### Linux Root Access Vulnerability
- **Description**: A recently disclosed security flaw affecting various Linux distributions that allows attackers to gain root access privileges
- **Impact**: Complete system compromise with administrative privileges on affected Linux systems
- **Status**: Added to CISA's KEV catalog, indicating active exploitation in the wild
- **CVE ID**: CVE-2026-31431

### cPanel Critical Vulnerability
- **Description**: A critical flaw in cPanel infrastructure being mass-exploited for ransomware deployment
- **Impact**: Website compromise and data encryption through "Sorry" ransomware attacks
- **Status**: Actively exploited in widespread ransomware campaigns
- **CVE ID**: CVE-2026-41940

### PyTorch Lightning Supply Chain Attack
- **Description**: Compromise of the popular Python package Lightning with malicious versions deployed to PyPI
- **Impact**: Credential theft from developer environments and CI/CD pipelines
- **Status**: Active malicious packages detected and being distributed

### Ruby Gems and Go Modules Supply Chain Attack
- **Description**: Sleeper packages containing malicious payloads targeting CI pipelines
- **Impact**: Credential theft, GitHub Actions tampering, and supply chain compromise
- **Status**: Active campaign using poisoned packages

## Affected Systems and Products

- **Linux Distributions**: Multiple distributions affected by root access vulnerability CVE-2026-31431
- **cPanel Infrastructure**: Web hosting platforms using cPanel affected by CVE-2026-41940
- **PyTorch Lightning**: Python machine learning package compromised in supply chain attack
- **Ruby Gems**: Ruby package ecosystem targeted with poisoned gems
- **Go Modules**: Go programming language packages compromised
- **Azure Environment**: Microsoft Azure targeted by ConsentFix v3 OAuth abuse
- **Facebook Accounts**: Over 30,000 accounts compromised via phishing campaigns
- **SAP Packages**: npm packages for SAP's cloud development ecosystem compromised

## Attack Vectors and Techniques

- **ConsentFix v3**: Automated OAuth abuse technique targeting Azure environments with scaling potential
- **Supply Chain Attacks**: Malicious packages inserted into legitimate software repositories (PyPI, Ruby Gems, Go Modules)
- **Phishing Relay**: Google AppSheet used as phishing infrastructure to distribute malicious emails
- **Vishing and SSO Abuse**: Voice phishing combined with single sign-on exploitation for SaaS environment attacks
- **Ransomware Deployment**: Mass exploitation of cPanel vulnerability for "Sorry" ransomware distribution
- **Privilege Escalation**: Linux vulnerability exploitation for root access

## Threat Actor Activities

- **North Korean Groups**: Conducting historic cryptocurrency heists with 76% of all crypto stolen in 2026, potentially AI-assisted operations
- **Vietnamese-Linked Operation**: Targeting Facebook accounts through Google AppSheet phishing campaigns, compromising 30,000+ accounts
- **China-Aligned Espionage**: Targeting government and defense sectors across South, East, and Southeast Asia, plus European government entities
- **TeamPCP**: Broadening supply chain attacks with "Mini Shai-Hulud" attacks against SAP packages
- **BlackCat Ransomware Affiliates**: Two cybersecurity professionals sentenced to 4 years for facilitating attacks
- **Romanian Swatting Ring**: Leader sentenced for coordinating attacks against 75+ public officials and journalists
- **Cybercrime Groups**: Conducting rapid SaaS extortion attacks using vishing and SSO abuse techniques