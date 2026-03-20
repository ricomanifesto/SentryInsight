# Exploitation Report

Critical exploitation activity continues to target enterprise infrastructure through multiple vectors, with threat actors leveraging both zero-day vulnerabilities and recently patched flaws. Russian APT28 operatives are actively exploiting Zimbra Collaboration Suite vulnerabilities in attacks against Ukrainian government entities, while the Interlock ransomware gang has been conducting zero-day attacks against Cisco Secure Firewall Management Center systems since January. The DarkSword iOS exploit kit represents a sophisticated threat utilizing multiple zero-day vulnerabilities for complete device compromise, while widespread exploitation of Microsoft SharePoint vulnerabilities has prompted urgent CISA warnings to federal agencies.

## Active Exploitation Details

### Cisco Secure Firewall Management Center Zero-Day
- **Description**: Maximum severity remote code execution vulnerability in Cisco's Secure Firewall Management Center (FMC) software allowing root access
- **Impact**: Complete system compromise, enabling ransomware deployment and lateral movement
- **Status**: Actively exploited by Interlock ransomware gang since January 2026
- **CVE ID**: CVE-2026-20131

### DarkSword iOS Zero-Day Exploit Kit
- **Description**: Sophisticated exploit kit targeting Apple iOS devices using a chain of six vulnerabilities, including three zero-days
- **Impact**: Full device takeover, sensitive data theft, and complete system compromise
- **Status**: Actively exploited by multiple threat actors since November 2025

### Microsoft SharePoint Critical Vulnerability
- **Description**: Critical vulnerability in Microsoft SharePoint that was patched in January but is now seeing active exploitation
- **Impact**: Unauthorized access to SharePoint environments and potential data exposure
- **Status**: Currently exploited in the wild, CISA has added to Known Exploited Vulnerabilities catalog

### Zimbra Collaboration Suite Cross-Site Scripting
- **Description**: Cross-site scripting (XSS) vulnerability in Synacor Zimbra Collaboration Suite (ZCS)
- **Impact**: Unauthorized access to email systems and credential theft
- **Status**: Actively exploited by Russian APT28 in attacks against Ukrainian government

### PolyShell Magento Vulnerability
- **Description**: Newly disclosed vulnerability affecting all Magento Open Source and Adobe Commerce stable version 2 installations
- **Impact**: Unauthenticated remote code execution and account takeover
- **Status**: Recently disclosed, exploitation status being monitored

### Ubiquiti UniFi Account Takeover
- **Description**: Maximum severity vulnerability in UniFi Network Application
- **Impact**: Complete account takeover and network infrastructure compromise
- **Status**: Recently patched, no active exploitation reported

### ConnectWise ScreenConnect Signature Verification Flaw
- **Description**: Cryptographic signature verification vulnerability in ConnectWise ScreenConnect
- **Impact**: Unauthorized access and privilege escalation in remote access systems
- **Status**: Recently patched, potential for exploitation remains

## Affected Systems and Products

- **Cisco Secure Firewall Management Center**: FMC software installations vulnerable to CVE-2026-20131
- **Apple iOS Devices**: iPhone users in Saudi Arabia, Turkey, Malaysia, and Ukraine targeted by DarkSword
- **Microsoft SharePoint**: SharePoint environments across federal agencies and enterprises
- **Zimbra Collaboration Suite**: Email servers used by Ukrainian government entities
- **Magento E-commerce Platforms**: All Magento Open Source and Adobe Commerce version 2 installations
- **Ubiquiti UniFi Systems**: Network management applications and infrastructure
- **ConnectWise ScreenConnect**: Remote access and support systems
- **Android Devices**: Perseus malware targeting banking applications and note-taking apps
- **IoT Devices**: Over 3 million compromised devices in disrupted botnets
- **Microsoft Intune**: Enterprise endpoint management systems

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple threat actors leveraging previously unknown vulnerabilities for initial access
- **Ransomware Deployment**: Interlock gang using Cisco FMC vulnerability for ransomware operations
- **Bring Your Own Vulnerable Driver (BYOVD)**: 54 EDR killers exploiting 34 signed vulnerable drivers
- **Mobile Malware Distribution**: Perseus Android malware targeting banking credentials and sensitive notes
- **IoT Botnet Operations**: Large-scale DDoS attacks using compromised Internet-connected devices
- **Supply Chain Compromise**: Speagle malware hijacking legitimate Cobra DocGuard infrastructure
- **Prompt Injection**: Claude AI vulnerabilities exploited through malicious prompts
- **Microsoft Intune Abuse**: Exploitation of endpoint management tools for destructive attacks

## Threat Actor Activities

- **APT28 (Russian Military Intelligence)**: Exploiting Zimbra vulnerabilities in targeted attacks against Ukrainian government entities
- **Interlock Ransomware Gang**: Conducting zero-day attacks against Cisco FMC systems since January 2026
- **Lazarus Group (North Korean)**: Bluenoroff subgroup responsible for Bitrefill cryptocurrency exchange attack
- **Handala Hacktivist Group**: Conducted destructive cyberattack against Stryker medical technology company, wiping 80,000 devices
- **DPRK IT Workers**: Sanctioned network using fake remote jobs to fund weapons of mass destruction programs
- **Multiple iOS Exploit Actors**: Various threat groups utilizing DarkSword exploit kit for espionage and data theft
- **EDR Evasion Specialists**: 54 different EDR killer tools actively bypassing endpoint security solutions