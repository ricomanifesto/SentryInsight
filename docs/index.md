# Exploitation Report

Current cybersecurity activity reveals a concerning landscape of sophisticated attack campaigns targeting various platforms and organizations. Notable incidents include ConsentFix v3 attacks leveraging automated OAuth abuse against Azure environments, Vietnamese-operated phishing campaigns compromising 30,000 Facebook accounts through Google AppSheet, and multiple supply chain attacks targeting Ruby Gems, Go modules, and Python packages. Additionally, North Korean threat actors continue their aggressive cryptocurrency theft operations, while cybercrime groups are conducting rapid SaaS extortion attacks using vishing and SSO abuse techniques. These incidents demonstrate an escalation in automation, social engineering sophistication, and supply chain targeting across the threat landscape.

## Active Exploitation Details

### ConsentFix v3 OAuth Abuse Attack
- **Description**: An evolved attack technique targeting Azure environments through automated OAuth consent manipulation, building on previous ConsentFix methods with enhanced automation and scaling capabilities
- **Impact**: Unauthorized access to Azure resources and services through manipulated OAuth consent flows
- **Status**: Currently circulating on hacker forums with active exploitation targeting Azure customers

### Google AppSheet Phishing Campaign
- **Description**: Vietnamese-linked operation using Google AppSheet as a "phishing relay" to distribute phishing emails targeting Facebook account credentials
- **Impact**: Compromise of approximately 30,000 Facebook accounts through credential theft
- **Status**: Active campaign with ongoing credential harvesting activities

### Supply Chain Attacks on Software Packages
- **Description**: Multiple coordinated attacks targeting Ruby Gems, Go modules, and Python packages (including PyTorch Lightning and Intercom-client) using sleeper packages and poisoned repositories
- **Impact**: Credential theft, GitHub Actions tampering, and CI pipeline exploitation affecting development environments
- **Status**: Active campaign with malicious packages deployed to compromise CI/CD pipelines

### SAP Package Compromise - Mini Shai-Hulud Attack
- **Description**: TeamPCP threat group compromising several npm packages for SAP's cloud application development ecosystem
- **Impact**: Supply chain contamination affecting SAP cloud development environments
- **Status**: Active compromise with broadening supply chain attack scope

### AI-Discovered Linux Vulnerability
- **Description**: Nine-year-old Linux bug discovered through AI-assisted vulnerability scanning with available proof-of-concept exploit code
- **Impact**: Potential system compromise through exploitation of long-standing kernel vulnerability
- **Status**: Patch available, but exploitation risk remains for unpatched systems

## Affected Systems and Products

- **Microsoft Azure**: OAuth consent flows and Azure Active Directory environments
- **Facebook/Meta Platforms**: User accounts and authentication systems  
- **Google AppSheet**: Platform being abused as phishing relay infrastructure
- **Development Ecosystems**: Ruby Gems, Go modules, Python packages (PyTorch Lightning, Intercom-client)
- **SAP Cloud Platform**: npm packages for cloud application development
- **Linux Systems**: Kernel vulnerability affecting systems running unpatched versions
- **Windows 11**: Backup software failures caused by KB5083769 security update
- **Trellix**: Source code repositories compromised with unauthorized access
- **Instructure Canvas**: Educational technology platform experiencing cybersecurity incident
- **France Titres (ANTS)**: French government administrative document agency

## Attack Vectors and Techniques

- **OAuth Abuse**: Automated manipulation of Azure OAuth consent flows for persistent access
- **Phishing Relay**: Using legitimate Google AppSheet platform to bypass email security filters
- **Supply Chain Poisoning**: Injection of malicious code into trusted software package repositories
- **Sleeper Packages**: Deployment of initially benign packages that are later updated with malicious payloads
- **Vishing and SSO Abuse**: Voice phishing combined with single sign-on exploitation for SaaS environments
- **AI-Enhanced Discovery**: Automated vulnerability scanning using artificial intelligence tools
- **Social Engineering**: Sophisticated targeting of specific user groups and organizations
- **CI/CD Pipeline Exploitation**: Targeting continuous integration environments for credential theft

## Threat Actor Activities

- **Vietnamese Threat Groups**: Conducting large-scale phishing operations targeting Facebook users through Google AppSheet platform abuse
- **TeamPCP**: Broadening supply chain attacks from previous focus to include SAP ecosystem targeting
- **North Korean State Actors**: Maintaining aggressive cryptocurrency theft operations with 76% of 2026 stolen crypto attributed to DPRK groups
- **China-Linked APT Groups**: Targeting Asian governments, NATO states, journalists, and activists through espionage campaigns
- **BlackCat/ALPHV Ransomware Operators**: Continuing operations despite law enforcement actions, with cybersecurity professionals sentenced for facilitating attacks
- **Romanian Cybercriminals**: Operating swatting rings targeting public officials, journalists, and religious institutions
- **Brazilian DDoS Operators**: Anti-DDoS firms paradoxically enabling botnet attacks against Brazilian ISPs
- **Cybercrime Syndicates**: Conducting rapid SaaS extortion attacks using minimal detection techniques and operating within cloud environments