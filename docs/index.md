# Exploitation Report

Critical exploitation activity continues to escalate with multiple actively exploited vulnerabilities impacting enterprise systems. A severe Linux privilege escalation vulnerability CVE-2026-31431 has been added to CISA's Known Exploited Vulnerabilities catalog, while a critical cPanel flaw CVE-2026-41940 is being mass-exploited in widespread "Sorry" ransomware campaigns. Additionally, threat actors are leveraging sophisticated attack vectors including Telegram Mini Apps for crypto scams and malware distribution, OAuth abuse in Azure environments, and supply chain attacks targeting CI/CD pipelines through poisoned Ruby Gems and Go modules.

## Active Exploitation Details

### Linux Root Access Vulnerability
- **Description**: A privilege escalation vulnerability affecting various Linux distributions that allows attackers to gain root access
- **Impact**: Complete system compromise and administrative control over affected Linux systems
- **Status**: Currently being actively exploited in the wild, added to CISA KEV catalog
- **CVE ID**: CVE-2026-31431

### cPanel Critical Vulnerability
- **Description**: A critical security flaw in cPanel control panel software being exploited for ransomware deployment
- **Impact**: Complete website compromise and data encryption in "Sorry" ransomware attacks
- **Status**: Mass exploitation ongoing for ransomware operations
- **CVE ID**: CVE-2026-41940

### Supply Chain Attacks via Package Repositories
- **Description**: Malicious packages deployed in Ruby Gems and Go module repositories targeting CI/CD pipelines
- **Impact**: Credential theft, GitHub Actions tampering, and unauthorized access to development environments
- **Status**: Active campaign using sleeper packages to deliver malicious payloads

## Affected Systems and Products

- **Linux Distributions**: Multiple distributions affected by privilege escalation vulnerability
- **cPanel Systems**: Web hosting control panels vulnerable to mass ransomware exploitation
- **Telegram Platform**: Mini Apps feature abused for crypto scams and Android malware delivery
- **Azure/Microsoft 365**: OAuth systems targeted by automated ConsentFix v3 attacks
- **Ruby Gems Repository**: Poisoned packages targeting Ruby development environments
- **Go Modules**: Compromised packages affecting Go-based CI/CD pipelines
- **SAP Development Packages**: npm packages in SAP's cloud application development ecosystem compromised
- **Facebook Accounts**: Over 30,000 accounts compromised via Google AppSheet phishing campaigns

## Attack Vectors and Techniques

- **Privilege Escalation**: Exploitation of Linux kernel vulnerabilities for root access
- **Ransomware Deployment**: Mass exploitation of cPanel flaws for "Sorry" ransomware attacks
- **OAuth Abuse**: Automated ConsentFix v3 attacks targeting Azure environments with scaled consent abuse
- **Social Engineering**: Vishing combined with SSO abuse in rapid SaaS extortion attacks
- **Supply Chain Poisoning**: Deployment of malicious packages in legitimate software repositories
- **Phishing Relay**: Google AppSheet used as intermediate platform for Facebook credential harvesting
- **Mobile Malware**: Android malware distribution through Telegram Mini Apps
- **Package Typosquatting**: "Mini Shai-Hulud" attacks targeting SAP development packages

## Threat Actor Activities

- **North Korean Groups**: Responsible for 76% of all cryptocurrency stolen in 2026, conducting historic heists
- **Vietnamese-Linked Operations**: Large-scale Facebook account compromise using Google AppSheet phishing
- **TeamPCP**: Supply chain attacks targeting SAP packages with sophisticated package poisoning
- **China-Aligned Espionage**: Targeting Asian governments, NATO states, journalists, and activists
- **BlackCat Ransomware Affiliates**: Coordinated attacks facilitated by cybersecurity professionals (now sentenced)
- **Sorry Ransomware Group**: Mass exploitation of cPanel vulnerabilities for widespread encryption attacks
- **Cybercrime Groups**: Rapid SaaS extortion using vishing and SSO abuse with minimal forensic traces