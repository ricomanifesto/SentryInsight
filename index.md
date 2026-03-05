# Exploitation Report

Critical exploitation activity is currently dominated by widespread zero-day abuse and targeted attacks on enterprise infrastructure. Google Threat Intelligence Group tracked 90 zero-day vulnerabilities actively exploited throughout 2025, with nearly half targeting enterprise software and appliances. Cisco has confirmed active exploitation of multiple vulnerabilities in their Catalyst SD-WAN Manager platform, while a sophisticated iOS exploit kit named Coruna has been deployed in both espionage and financially motivated attacks. Additionally, threat actors continue to leverage advanced malware campaigns, with APT28 deploying new backdoors against Ukrainian entities and Iran-linked groups targeting Iraqi officials with custom malware families.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Vulnerabilities
- **Description**: Two security flaws in Cisco Catalyst SD-WAN Manager (formerly SD-WAN vManage) are being actively exploited in the wild
- **Impact**: Attackers can potentially gain unauthorized access to network management systems and compromise SD-WAN infrastructure
- **Status**: Cisco has confirmed active exploitation and is urging administrators to upgrade vulnerable devices immediately

### VMware Aria Operations Command Injection Flaw
- **Description**: Command injection vulnerability in VMware Aria Operations allowing remote code execution
- **Impact**: Exploitation grants attackers broad access to victims' cloud environments and resources
- **Status**: Actively exploited in the wild, putting cloud infrastructure at significant risk

### FreeScout Mail2Shell Zero-Click Attack
- **Description**: Maximum severity vulnerability in the FreeScout helpdesk platform enabling zero-click remote code execution
- **Impact**: Hackers can achieve complete system compromise without any user interaction or authentication requirements
- **Status**: Critical zero-click attack vector allowing full server hijacking

### Cisco Secure Firewall Management Center Vulnerabilities
- **Description**: Two maximum-severity vulnerabilities in Cisco Secure FMC software
- **Impact**: Successful exploitation provides attackers with root-level access to firewall management systems
- **Status**: Security updates released to address critical access control bypass

### Coruna iOS Exploit Kit
- **Description**: Sophisticated exploit kit containing 23 iOS exploits across five attack chains targeting iOS versions 13.0 through 17.2.1
- **Impact**: Enables complete device compromise for espionage and cryptocurrency theft operations
- **Status**: Actively deployed by multiple threat actors in targeted campaigns

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Network management platform vulnerable to active exploitation
- **VMware Aria Operations**: Cloud management platform affected by command injection vulnerabilities
- **FreeScout Helpdesk Platform**: Open-source customer support system with zero-click RCE vulnerability
- **Cisco Secure Firewall Management Center**: Enterprise firewall management software with root access vulnerabilities
- **Apple iOS Devices**: iPhones running iOS versions 13.0 through 17.2.1 targeted by Coruna exploit kit
- **Enterprise Software and Appliances**: Nearly half of the 90 tracked zero-days target enterprise infrastructure

## Attack Vectors and Techniques

- **Zero-Click Exploitation**: Mail2Shell attack requires no user interaction to compromise FreeScout servers
- **Command Injection**: VMware Aria Operations vulnerability allows arbitrary command execution
- **Multi-Stage iOS Exploitation**: Coruna kit uses five distinct exploit chains for comprehensive device compromise
- **Network Infrastructure Targeting**: Active exploitation of SD-WAN and firewall management platforms
- **Phishing-as-a-Service**: Tycoon2FA platform facilitated large-scale credential harvesting operations
- **Adversary-in-the-Middle Attacks**: Sophisticated credential harvesting bypassing multi-factor authentication

## Threat Actor Activities

- **APT28 (Russian Military Intelligence)**: Deploying BadPaw loader and MeowMeow backdoor in Ukraine targeting campaign
- **Dust Specter (Iran-linked)**: Targeting Iraqi government officials with SPLITDROP and GHOSTFORM malware while impersonating Ministry of Foreign Affairs
- **Multiple iOS Threat Actors**: Using Coruna exploit kit for both espionage campaigns and cryptocurrency theft operations
- **Cybercriminal Networks**: Operating through seized platforms including LeakBase forum (142,000 members) and Tycoon2FA phishing service (64,000 attacks)
- **Hacktivist Groups**: Conducting 149 DDoS attacks against 110 organizations across 16 countries following Middle East conflict escalation
- **Cryptocurrency Thieves**: Exploiting various platforms including $46 million theft from U.S. Marshals Service and targeting iOS users through Coruna kit