# Exploitation Report

Current threat activity reveals several critical exploitation campaigns targeting enterprise infrastructure and mobile platforms. CISA has added three actively exploited vulnerabilities affecting Citrix Session Recording and Git to its Known Exploited Vulnerabilities catalog, indicating ongoing attacks against these systems. Meanwhile, the HOOK Android banking trojan has evolved to include ransomware capabilities with 107 remote commands, demonstrating the increasing sophistication of mobile malware. Additionally, coordinated scanning campaigns are targeting Microsoft RDP authentication servers, while threat actors are leveraging AI systems for novel attack vectors and exploiting Salesforce platforms to breach major organizations.

## Active Exploitation Details

### Citrix Session Recording Vulnerabilities
- **Description**: Security flaws in Citrix Session Recording systems that are being actively exploited in the wild
- **Impact**: Attackers can potentially gain unauthorized access to session recording infrastructure and sensitive recorded data
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog, indicating active exploitation

### Git Vulnerabilities
- **Description**: Security vulnerabilities affecting Git version control systems
- **Impact**: Could allow attackers to compromise source code repositories and development infrastructure
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog, confirming active exploitation

### Apple Security Flaw
- **Description**: A dangerous security vulnerability affecting iPhone, iPad, and Mac devices
- **Impact**: Apple warns the flaw might have already been exploited in "extremely sophisticated attacks" targeting specific individuals
- **Status**: Patches available, but exploitation may have already occurred in targeted attacks

### Salesforce Platform Exploitation
- **Description**: Widespread attacks targeting Salesforce platforms affecting multiple organizations
- **Impact**: Data breaches affecting over 1.1 million customers at Farmers Insurance alone
- **Status**: Active exploitation resulting in confirmed data breaches

## Affected Systems and Products

- **Citrix Session Recording**: Session recording infrastructure and related components
- **Git Systems**: Version control systems and repositories
- **Apple Devices**: iPhone, iPad, and Mac systems requiring immediate updates
- **Microsoft RDP**: Remote Desktop Web Access and RDP Web Authentication servers
- **Salesforce Platforms**: Customer relationship management and data storage systems
- **Android Devices**: Mobile devices targeted by HOOK banking trojan variants
- **AI Systems**: Large language models vulnerable to prompt injection attacks

## Attack Vectors and Techniques

- **Coordinated Network Scanning**: Nearly 1,971 IP addresses conducting coordinated scans against Microsoft RDP authentication servers
- **Banking Trojan Evolution**: HOOK Android trojan now features ransomware-style overlay screens and expanded to 107 remote commands
- **AI Prompt Injection**: Novel attacks hiding malicious prompts in downscaled images processed by AI systems before delivery to language models
- **Captive Portal Hijacking**: UNC6384 threat group using captive portal compromises with valid certificates for initial access
- **ClickFix Social Engineering**: Attacks tricking AI-generated content summaries into pushing malware to unsuspecting users

## Threat Actor Activities

- **UNC6384 (China-nexus)**: Targeting diplomats in Southeast Asia and global entities using PlugX malware via captive portal hijacks and valid certificates to advance Beijing's strategic interests
- **HOOK Operators**: Android banking trojan developers adding ransomware capabilities and expanding command functionality to 107 remote commands
- **Lab-Dookhtegen**: Claims responsibility for major attacks on over 60 Iranian cargo ships and oil tankers, disrupting maritime communications
- **RDP Scanning Campaign**: Coordinated effort involving nearly 2,000 IP addresses systematically probing Microsoft Remote Desktop infrastructure
- **Salesforce Attackers**: Threat actors conducting widespread attacks against Salesforce platforms, resulting in multiple organizational breaches