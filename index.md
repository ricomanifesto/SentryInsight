# Exploitation Report

The cybersecurity landscape is experiencing intense exploitation activity across multiple critical vulnerabilities and attack vectors. Cisco's Catalyst SD-WAN Manager systems face active exploitation of two high-severity vulnerabilities, while CISA has added critical flaws in Hikvision and Rockwell Automation products to its Known Exploited Vulnerabilities catalog. WordPress sites are under active attack through a critical User Registration & Membership plugin vulnerability allowing unauthorized admin account creation. Additionally, Google's Threat Intelligence Group reports that 90 zero-day vulnerabilities were exploited throughout 2025, with nearly half targeting enterprise software and appliances, indicating a sustained focus on high-value corporate targets.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Vulnerabilities
- **Description**: Two high-severity security flaws affecting Catalyst SD-WAN Manager (formerly SD-WAN vManage) systems
- **Impact**: Active exploitation allowing attackers to compromise SD-WAN infrastructure and potentially gain unauthorized network access
- **Status**: Currently under active exploitation in the wild; Cisco urging immediate upgrades

### Hikvision Security Vulnerability
- **Description**: Critical security flaw in Hikvision products with CVSS 9.8 severity rating
- **Impact**: High-severity exploitation allowing potential unauthorized access to surveillance systems
- **Status**: Added to CISA KEV catalog, indicating active exploitation

### Rockwell Automation Security Vulnerability
- **Description**: Critical security flaw in Rockwell Automation industrial control systems with CVSS 9.8 severity rating
- **Impact**: High-severity exploitation potentially affecting industrial control systems and operational technology
- **Status**: Added to CISA KEV catalog, indicating active exploitation

### WordPress User Registration & Membership Plugin Vulnerability
- **Description**: Critical vulnerability in the User Registration & Membership plugin installed on over 60,000 WordPress sites
- **Impact**: Allows attackers to create unauthorized administrator accounts, leading to complete site compromise
- **Status**: Under active exploitation with hackers targeting vulnerable installations

### Zero-Day Exploitation Surge
- **Description**: Widespread exploitation of previously unknown vulnerabilities across enterprise software and appliances
- **Impact**: Complete system compromise, data theft, and unauthorized access to enterprise networks
- **Status**: 90 zero-day vulnerabilities actively exploited in 2025, with 45 targeting enterprise environments

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Network infrastructure management systems requiring immediate security updates
- **Hikvision Surveillance Systems**: Video surveillance and security camera systems with critical vulnerabilities
- **Rockwell Automation Industrial Controls**: Industrial control systems and operational technology infrastructure
- **WordPress Sites**: Over 60,000 websites using the User Registration & Membership plugin
- **Enterprise Software**: Wide range of enterprise applications and appliances targeted by zero-day exploits
- **Telecommunications Infrastructure**: South American telecom providers targeted by Chinese state-sponsored groups
- **Windows Terminal Applications**: Systems vulnerable to ClickFix social engineering campaigns deploying Lumma Stealer

## Attack Vectors and Techniques

- **SD-WAN Infrastructure Targeting**: Direct exploitation of network management vulnerabilities to compromise enterprise connectivity
- **Social Engineering via ClickFix Campaigns**: Using Windows Terminal applications to deploy sophisticated malware chains
- **Phishing-as-a-Service Operations**: Large-scale credential harvesting through platforms like Tycoon 2FA affecting 64,000+ attacks
- **WordPress Plugin Exploitation**: Automated attacks targeting vulnerable membership plugins to create admin accounts
- **Zero-Day Exploitation**: Systematic targeting of previously unknown vulnerabilities in enterprise software
- **Self-Propagating Worms**: JavaScript-based attacks spreading across wiki platforms and modifying user scripts
- **Industrial Control System Targeting**: Focused attacks on operational technology and industrial automation systems

## Threat Actor Activities

- **MuddyWater (Iran-linked)**: Targeting U.S. networks including banks and airlines with new Dindoor backdoor malware
- **UAT-9244 (China-linked)**: Targeting South American telecommunications infrastructure with TernDoor, PeerTime, and BruteEntry malware toolkit
- **APT28 (Russia-linked)**: Deploying BadPaw loader and MeowMeow backdoor in targeted campaigns against Ukrainian entities
- **APT36 (Pakistan)**: Embracing AI-powered malware development to create large-scale, automated attack tools
- **Dust Specter (Iran-suspected)**: Targeting Iraqi government officials with SPLITDROP and GHOSTFORM malware while impersonating Ministry of Foreign Affairs
- **Cybercriminal Syndicates**: Operating large-scale phishing-as-a-service platforms and stolen credential marketplaces before law enforcement disruption