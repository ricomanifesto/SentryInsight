# Exploitation Report

The cybersecurity landscape is experiencing significant exploitation activity across multiple attack vectors. A critical cPanel vulnerability CVE-2026-41940 is being mass-exploited in ransomware campaigns, while sophisticated supply chain attacks are targeting development environments through poisoned Ruby Gems and Go modules. Azure environments face automated OAuth abuse through ConsentFix v3 attacks, and a large-scale phishing campaign has compromised 30,000 Facebook accounts using Google AppSheet as a relay. Additionally, North Korean threat actors continue their aggressive cryptocurrency theft operations, now controlling 76% of all crypto stolen in 2026.

## Active Exploitation Details

### Critical cPanel Vulnerability
- **Description**: A newly disclosed critical flaw in cPanel that allows attackers to breach websites and deploy ransomware
- **Impact**: Attackers can gain unauthorized access to websites and encrypt data in "Sorry" ransomware attacks
- **Status**: Currently being mass-exploited in active ransomware campaigns
- **CVE ID**: CVE-2026-41940

### ConsentFix v3 OAuth Abuse
- **Description**: An evolved attack technique targeting Azure environments through automated OAuth consent abuse
- **Impact**: Enables attackers to gain persistent access to Azure environments with minimal detection
- **Status**: Actively circulating on hacker forums with automation capabilities

### Supply Chain Attacks on Development Packages
- **Description**: Sophisticated campaign using poisoned Ruby Gems and Go modules to exploit CI/CD pipelines
- **Impact**: Credential theft, GitHub Actions tampering, and compromise of development environments
- **Status**: Active exploitation targeting software development supply chains

### Facebook Account Compromise Campaign
- **Description**: Vietnamese-linked operation using Google AppSheet as a phishing relay to compromise Facebook accounts
- **Impact**: Successful compromise of approximately 30,000 Facebook accounts
- **Status**: Active phishing campaign with significant scale

## Affected Systems and Products

- **cPanel**: Web hosting control panel software experiencing critical vulnerability exploitation
- **Azure Environments**: Microsoft cloud services targeted through OAuth consent abuse
- **Ruby Gems**: Package repository for Ruby programming language affected by malicious packages
- **Go Modules**: Go programming language package system compromised with malicious modules
- **Facebook Accounts**: Social media platform accounts targeted through phishing campaigns
- **Google AppSheet**: Google's no-code platform being abused as phishing infrastructure
- **PyTorch Lightning**: Popular Python machine learning package compromised in supply chain attack
- **Intercom-client**: Customer messaging platform package targeted for credential theft
- **SAP npm Packages**: Cloud application development packages hit by "Mini Shai-Hulud" attack
- **CI/CD Pipelines**: Continuous integration systems targeted for credential theft

## Attack Vectors and Techniques

- **Mass Exploitation**: Automated scanning and exploitation of cPanel vulnerabilities for ransomware deployment
- **OAuth Consent Abuse**: Automated techniques for gaining persistent Azure access through consent manipulation
- **Supply Chain Poisoning**: Injection of malicious code into legitimate software packages and dependencies
- **Phishing Relay**: Using legitimate Google AppSheet platform to distribute phishing emails and evade detection
- **Package Typosquatting**: Creating malicious packages with names similar to legitimate ones
- **CI Pipeline Exploitation**: Targeting continuous integration systems to steal credentials and tamper with workflows
- **Vishing and SSO Abuse**: Voice phishing combined with single sign-on exploitation for rapid SaaS environment compromise

## Threat Actor Activities

- **North Korean Groups**: Conducting historic cryptocurrency heists with AI assistance, controlling 76% of stolen crypto in 2026
- **Vietnamese Operators**: Running large-scale Facebook phishing campaigns using Google AppSheet infrastructure
- **TeamPCP**: Broadening supply chain attacks to target SAP development ecosystems
- **China-Linked Groups**: Targeting Asian governments, NATO states, journalists, and activists in espionage campaigns
- **Cybercrime Groups**: Conducting rapid SaaS extortion attacks using vishing and SSO abuse techniques
- **Supply Chain Attackers**: Using sleeper packages as conduits for subsequent malicious payload deployment
- **Sorry Ransomware Operators**: Mass-exploiting cPanel vulnerabilities for website encryption attacks