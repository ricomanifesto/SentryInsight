# Exploitation Report

The cybersecurity landscape faces unprecedented exploitation activity with multiple critical vulnerabilities being actively targeted across diverse platforms and industries. Most concerning is the active exploitation of iOS security flaws in cyberespionage and crypto-theft attacks using the Coruna exploit kit, prompting CISA to order federal agencies to immediately patch these vulnerabilities. Google's threat intelligence reveals that 90 zero-day vulnerabilities were exploited in attacks throughout 2025, with nearly half targeting enterprise software and appliances. Additionally, Cisco has confirmed active exploitation of two critical Catalyst SD-WAN Manager vulnerabilities, while WordPress sites are under attack through a critical User Registration & Membership plugin vulnerability. The threat landscape is further complicated by sophisticated social engineering campaigns, including ClickFix attacks deploying malware through fake installation guides and the emergence of AI-enhanced malware development by nation-state actors.

## Active Exploitation Details

### iOS Security Flaws (Coruna Exploit Kit)
- **Description**: Three iOS security vulnerabilities being exploited through the sophisticated Coruna exploit kit
- **Impact**: Enables cyberespionage operations and cryptocurrency theft attacks against iOS devices
- **Status**: Actively exploited; CISA has ordered federal agencies to patch immediately

### Cisco Catalyst SD-WAN Manager Vulnerabilities
- **Description**: Two critical vulnerabilities in Cisco's Catalyst SD-WAN Manager (formerly SD-WAN vManage) platform
- **Impact**: Allows attackers to compromise network management infrastructure and potentially gain control over SD-WAN deployments
- **Status**: Actively exploited in the wild; patches available

### WordPress User Registration & Membership Plugin Vulnerability
- **Description**: Critical vulnerability in the User Registration & Membership plugin affecting over 60,000 WordPress sites
- **Impact**: Enables attackers to create unauthorized administrator accounts and take complete control of affected websites
- **Status**: Actively exploited; critical patch required

### Hikvision and Rockwell Automation Critical Flaws
- **Description**: Two high-severity security flaws with CVSS 9.8 scores affecting industrial and surveillance systems
- **Impact**: Critical infrastructure compromise and unauthorized system access
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog; immediate patching required

## Affected Systems and Products

- **iOS Devices**: All iOS versions vulnerable to Coruna exploit kit attacks targeting mobile cryptocurrency applications
- **Cisco Catalyst SD-WAN Manager**: Network management platforms in enterprise environments
- **WordPress Sites**: Over 60,000 websites using the User Registration & Membership plugin
- **Hikvision Surveillance Systems**: IP cameras and video surveillance infrastructure
- **Rockwell Automation Systems**: Industrial control systems and automation platforms
- **Telecommunication Infrastructure**: South American telecom providers targeted by Chinese APT groups
- **Healthcare Systems**: TriZetto Provider Solutions affecting 3.4 million patient records
- **U.S. Government Networks**: Federal agencies and contractors targeted by Iranian MuddyWater group

## Attack Vectors and Techniques

- **Social Engineering (ClickFix/InstallFix)**: Fake installation guides for legitimate software like Claude Code that trick users into executing malicious commands
- **AI-Enhanced Malware Development**: Nation-state actors using artificial intelligence tools for rapid malware creation and deployment
- **Phishing-as-a-Service**: Tycoon 2FA platform enabling bypass of multi-factor authentication before law enforcement takedown
- **JavaScript Worm Propagation**: Self-propagating worms targeting platforms like Wikipedia for vandalization and script modification
- **Supply Chain Attacks**: Fake GitHub repositories promoted through AI-enhanced search results distributing information stealers
- **Multi-Stage RAT Deployment**: VOID#GEIST malware campaign delivering XWorm, AsyncRAT, and Xeno RAT through batch scripts
- **Network Infrastructure Targeting**: Custom malware toolkits (TernDoor, PeerTime, BruteEntry) for compromising edge devices

## Threat Actor Activities

- **North Korean APT Groups**: Leveraging AI tools including face-swapping technology to enhance IT worker infiltration scams and gain unauthorized employment
- **Transparent Tribe (APT36)**: Pakistan-aligned group using AI-powered coding tools to mass-produce malware implants targeting Indian organizations
- **Iranian MuddyWater Group**: Deploying new Dindoor backdoor against U.S. networks including banks and airlines through sophisticated persistence mechanisms
- **Chinese APT UAT-9244**: Targeting South American telecommunications infrastructure since 2024 with custom malware toolkit affecting Windows, Linux, and network edge devices
- **Business Email Compromise Rings**: Ghanaian-led fraud operations stealing over $100 million through coordinated BEC attacks and romance scams
- **Cryptocurrency Theft Operations**: Sophisticated attacks against U.S. Marshals Service resulting in $46 million theft and targeting of government surveillance systems