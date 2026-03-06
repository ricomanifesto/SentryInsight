# Exploitation Report

Critical vulnerability exploitation activity has intensified across multiple sectors, with significant threats targeting enterprise infrastructure and government systems. The most severe incidents include active exploitation of Cisco Catalyst SD-WAN Manager vulnerabilities with CVSS 9.8 scores, alongside critical flaws in Hikvision and Rockwell Automation products that have been added to CISA's Known Exploited Vulnerabilities catalog. State-sponsored actors are leveraging sophisticated malware toolkits, with Iranian-linked MuddyWater deploying new Dindoor backdoors against U.S. networks and Chinese APT groups targeting South American telecommunications infrastructure with advanced malware suites. Social engineering campaigns have evolved with new InstallFix and ClickFix techniques deploying infostealers through fake software installation guides, while a WordPress membership plugin vulnerability is being actively exploited to create unauthorized administrator accounts across thousands of sites.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Vulnerabilities
- **Description**: Two critical vulnerabilities affecting Cisco Catalyst SD-WAN Manager (formerly SD-WAN vManage) systems are under active exploitation
- **Impact**: Attackers can potentially gain unauthorized access to network management infrastructure
- **Status**: Confirmed active exploitation in the wild; patches available from Cisco

### Hikvision and Rockwell Automation Critical Flaws
- **Description**: Security vulnerabilities with CVSS 9.8 severity scores affecting Hikvision and Rockwell Automation products
- **Impact**: Critical system compromise potential across industrial and surveillance infrastructure
- **Status**: Added to CISA Known Exploited Vulnerabilities (KEV) catalog, indicating confirmed exploitation

### WordPress User Registration & Membership Plugin Vulnerability
- **Description**: Critical vulnerability in the User Registration & Membership plugin affecting over 60,000 WordPress sites
- **Impact**: Attackers can create unauthorized administrator accounts, gaining full control of affected websites
- **Status**: Active exploitation confirmed; plugin installed on more than 60,000 sites

### Wikipedia JavaScript Worm
- **Description**: Self-propagating JavaScript worm targeting the Wikimedia Foundation infrastructure
- **Impact**: Page vandalization and modification of user scripts across multiple wikis
- **Status**: Security incident confirmed; worm actively spreading across Wikipedia platforms

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Network management systems vulnerable to critical exploitation
- **Hikvision Products**: Surveillance and security camera systems with CVSS 9.8 vulnerabilities
- **Rockwell Automation Products**: Industrial control and automation systems facing critical flaws
- **WordPress Sites**: Over 60,000 sites using vulnerable User Registration & Membership plugin
- **Wikimedia Foundation**: Multiple wiki platforms affected by JavaScript worm propagation
- **Telecommunications Infrastructure**: South American telecom providers targeted by Chinese APT groups
- **U.S. Corporate Networks**: Banks, airlines, and other enterprises compromised by Iranian actors

## Attack Vectors and Techniques

- **InstallFix Social Engineering**: New variation of ClickFix technique convincing users to run malicious commands under the pretext of installing legitimate software like Claude AI
- **ClickFix Campaign via Windows Terminal**: Sophisticated attack chain leveraging Windows Terminal app to deploy Lumma Stealer malware
- **Fake GitHub Repositories**: Malicious OpenClaw installers promoted through Microsoft Bing's AI-enhanced search results
- **AI-Assisted Malware Development**: Pakistan's APT36 using AI for rapid malware generation and assembly line production
- **Self-Propagating JavaScript Worms**: Automated spreading mechanisms targeting wiki platforms and content management systems
- **Phishing-as-a-Service Platforms**: Tycoon 2FA platform enabling bypass of multifactor authentication defenses

## Threat Actor Activities

- **Iranian MuddyWater (APT)**: Deploying new Dindoor backdoor against U.S. networks, targeting banks, airlines, and other critical infrastructure with persistent access techniques
- **Chinese UAT-9244 (APT)**: Targeting South American telecommunications providers since 2024 using TernDoor, PeerTime, and BruteEntry malware toolkit against Windows, Linux, and edge devices
- **Pakistani APT36**: Implementing AI-driven malware assembly line using "vibe-coding" techniques to produce malware at scale
- **Dust Specter (Iran-nexus)**: Targeting Iraqi government officials with new SPLITDROP and GHOSTFORM malware, impersonating Ministry of Foreign Affairs communications
- **Fraud Networks**: $100 million fraud ring using business email compromise attacks and romance scams, with Ghanaian national pleading guilty to participation