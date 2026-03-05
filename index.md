# Exploitation Report

Critical vulnerabilities are under active exploitation across multiple enterprise platforms, with attackers targeting cloud infrastructure, networking equipment, and mobile devices. The most significant threats include a command injection flaw in VMware Aria Operations (CVE-2026-22719) that grants broad access to cloud environments, two actively exploited vulnerabilities in Cisco SD-WAN Manager systems, maximum severity flaws in Cisco Secure Firewall Management Center, and a sophisticated iOS exploit kit called Coruna targeting Apple devices. Meanwhile, advanced persistent threat groups including APT28-linked actors and Iran-nexus threat actors are deploying new malware families and conducting targeted campaigns against government entities, while law enforcement agencies have successfully dismantled major cybercrime platforms including Tycoon 2FA and LeakBase forum.

## Active Exploitation Details

### VMware Aria Operations Command Injection Flaw
- **Description**: A command injection vulnerability affecting Broadcom VMware Aria Operations that allows remote code execution
- **Impact**: Attackers can achieve remote code execution and gain broad access to victims' cloud environments
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-22719

### Cisco SD-WAN Manager Vulnerabilities
- **Description**: Two security flaws in Cisco Catalyst SD-WAN Manager that are being actively exploited
- **Impact**: Unauthorized access to SD-WAN infrastructure and potential network compromise
- **Status**: Actively exploited in attacks, Cisco urging immediate upgrades

### Cisco Secure Firewall Management Center Vulnerabilities
- **Description**: Two maximum-severity vulnerabilities in Cisco Secure FMC software
- **Impact**: Root access to firewall management systems
- **Status**: Security updates released, maximum severity rating

### FreeScout Mail2Shell Zero-Click Attack
- **Description**: Maximum severity vulnerability in FreeScout helpdesk platform enabling zero-click remote code execution
- **Impact**: Complete system compromise without user interaction or authentication required
- **Status**: Actively exploitable, allows hijacking of mail servers

### Coruna iOS Exploit Kit
- **Description**: Sophisticated exploit kit containing 23 iOS exploits across five exploitation chains
- **Impact**: Complete device compromise for espionage and cryptocurrency theft
- **Status**: Actively used by multiple threat actors in targeted campaigns

## Affected Systems and Products

- **VMware Aria Operations**: Cloud management platform with command injection vulnerability
- **Cisco SD-WAN Manager**: Network management systems under active attack
- **Cisco Secure Firewall Management Center**: Enterprise firewall management software
- **FreeScout Helpdesk Platform**: Open-source customer support system
- **Apple iOS Devices**: iPhones running iOS versions 13.0 through 17.2.1
- **Laravel PHP Packages**: Malicious packages deployed through Packagist repository
- **HungerRush POS Systems**: Restaurant point-of-sale platform targeted in extortion campaigns

## Attack Vectors and Techniques

- **Command Injection**: Direct execution of malicious commands through vulnerable interfaces
- **Zero-Click Exploitation**: Remote code execution without requiring user interaction
- **Phishing Campaigns**: Impersonation of government agencies and legitimate services
- **Supply Chain Attacks**: Malicious packages distributed through legitimate software repositories
- **Social Engineering**: Fake support communications to steal credentials
- **Adversary-in-the-Middle Attacks**: Credential harvesting through sophisticated phishing platforms
- **Spear Phishing**: Targeted emails impersonating legitimate organizations
- **Brute Force Attacks**: Automated credential stuffing and password attacks

## Threat Actor Activities

- **Dust Specter (Iran-nexus)**: Targeting Iraqi government officials with SPLITDROP and GHOSTFORM malware using fake Ministry of Foreign Affairs communications
- **APT28-linked Campaign**: Deploying BadPaw loader and MeowMeow backdoor against Ukrainian entities
- **Silver Dragon (APT41-linked)**: Conducting cyber espionage against European and Southeast Asian governments using Cobalt Strike and Google Drive for command and control
- **Multiple iOS Exploit Actors**: Using Coruna exploit kit for both espionage campaigns and financially motivated cryptocurrency theft
- **Phobos Ransomware Operation**: Russian-administered ransomware group with hundreds of victims worldwide
- **Hacktivist Groups**: Conducting 149 DDoS attacks against 110 organizations across 16 countries following Middle East conflicts
- **Cybercrime Forums**: LeakBase and Tycoon 2FA platforms facilitating large-scale credential theft and phishing operations before law enforcement takedowns