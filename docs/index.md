# Exploitation Report

The current threat landscape is dominated by critical exploitation activities across multiple vectors, with particular concern around infrastructure targeting and AI-enhanced attack campaigns. CISA has issued urgent warnings for federal agencies to patch three iOS security flaws being actively exploited in cyberespionage and cryptocurrency theft attacks using the Coruna exploit kit. Additionally, critical vulnerabilities in Cisco Catalyst SD-WAN Manager and Hikvision products with CVSS 9.8 severity ratings have been added to CISA's Known Exploited Vulnerabilities catalog, indicating active exploitation in the wild. The report also reveals widespread zero-day exploitation, with Google tracking 90 zero-day vulnerabilities exploited throughout 2025, nearly half targeting enterprise software and appliances.

## Active Exploitation Details

### iOS Security Flaws (Coruna Exploit Kit)
- **Description**: Three iOS security vulnerabilities being exploited through the Coruna exploit kit for targeted attacks
- **Impact**: Enables cyberespionage operations and cryptocurrency theft from mobile devices
- **Status**: CISA has ordered federal agencies to patch immediately due to active exploitation

### Cisco Catalyst SD-WAN Manager Vulnerabilities
- **Description**: Two critical vulnerabilities in Cisco's SD-WAN management platform confirmed under active exploitation
- **Impact**: Attackers can gain unauthorized access to network management infrastructure
- **Status**: Active exploitation confirmed by Cisco, patches available

### Hikvision Critical Vulnerability
- **Description**: Critical security flaw in Hikvision products with maximum CVSS 9.8 severity rating
- **Impact**: Complete system compromise and unauthorized access to surveillance systems
- **Status**: Added to CISA KEV catalog due to active exploitation

### WordPress User Registration Plugin Vulnerability
- **Description**: Critical vulnerability in User Registration & Membership plugin affecting over 60,000 WordPress sites
- **Impact**: Allows attackers to create unauthorized administrator accounts
- **Status**: Currently being exploited in the wild

### Zero-Day Vulnerabilities (2025)
- **Description**: 90 zero-day vulnerabilities tracked throughout 2025, with nearly half targeting enterprise software
- **Impact**: Various impacts depending on specific vulnerabilities, ranging from data theft to system compromise
- **Status**: Active exploitation confirmed across multiple attack campaigns

## Affected Systems and Products

- **Apple iOS**: Mobile devices targeted through Coruna exploit kit campaigns
- **Cisco Catalyst SD-WAN Manager**: Network infrastructure management systems
- **Hikvision Products**: Surveillance and security camera systems
- **WordPress Sites**: Over 60,000 sites using vulnerable User Registration & Membership plugin
- **Enterprise Software**: Nearly half of 2025 zero-days targeted enterprise applications and appliances
- **Telecommunications Infrastructure**: South American telecom providers targeted by Chinese APT groups
- **Windows and Linux Systems**: Targeted in multi-stage malware campaigns and APT operations

## Attack Vectors and Techniques

- **Mobile Exploit Kits**: Coruna exploit kit targeting iOS devices for surveillance and crypto theft
- **Social Engineering**: ClickFix and InstallFix campaigns tricking users into running malicious commands
- **AI-Enhanced Malware Development**: Nation-state actors using AI tools for mass malware production
- **Multi-Stage Malware Deployment**: VOID#GEIST campaign delivering XWorm, AsyncRAT, and Xeno RAT
- **Supply Chain Attacks**: Fake repositories promoted through search engines deploying infostealers
- **Phishing-as-a-Service**: Tycoon 2FA platform bypassing multifactor authentication
- **JavaScript Worm Propagation**: Self-propagating worms targeting wiki platforms
- **Plugin Exploitation**: WordPress plugin vulnerabilities for privilege escalation

## Threat Actor Activities

- **North Korean APTs**: Enhanced IT worker scams using AI for face swapping and communication
- **Transparent Tribe (APT36)**: Pakistan-aligned group using AI for mass malware implant production targeting India
- **MuddyWater**: Iran-linked group deploying new Dindoor backdoor against U.S. networks including banks and airlines
- **UAT-9244**: China-linked APT targeting South American telecommunications with TernDoor, PeerTime, and BruteEntry malware
- **Iranian Cyber-Kinetic Operations**: IP camera hacking for missile strike planning and physical asset targeting
- **ClickFix Campaign Operators**: Widespread social engineering campaigns using Windows Terminal for Lumma Stealer deployment
- **Cryptocurrency Theft Groups**: Multi-million dollar operations including $46M theft from U.S. Marshals Service
- **Business Email Compromise Rings**: $100+ million fraud operations targeting U.S. businesses