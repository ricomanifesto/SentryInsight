# Exploitation Report

The current threat landscape shows intense exploitation activity across multiple critical vulnerabilities, with attackers targeting enterprise infrastructure, file-sharing solutions, and web applications. Most concerning is the active exploitation of zero-day vulnerabilities in Gladinet CentreStack file-sharing software and Oracle systems, alongside maximum-severity flaws in Adobe Experience Manager and Cisco networking equipment. Nation-state actors and ransomware groups are leveraging these vulnerabilities for espionage, data theft, and persistent access, while also employing novel techniques like blockchain-based malware distribution and eBPF rootkits for stealth operations.

## Active Exploitation Details

### Gladinet CentreStack Zero-Day Vulnerability
- **Description**: Local file inclusion vulnerability in Gladinet's CentreStack business solution that has been actively exploited as a zero-day since late in the reporting period
- **Impact**: Attackers can access sensitive files and potentially execute arbitrary code on affected systems
- **Status**: Security updates have been released to address the vulnerability
- **CVE ID**: CVE-2025-11371

### Adobe Experience Manager Critical Vulnerability
- **Description**: Maximum-severity vulnerability in Adobe Experience Manager that allows remote code execution on unpatched systems
- **Impact**: Attackers can execute arbitrary code and gain full control of affected systems
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: Not specified in the articles

### Cisco SNMP Vulnerability
- **Description**: Remote code execution vulnerability in older Cisco IOS Software and IOS XE Software networking devices
- **Impact**: Attackers can deploy Linux rootkits and gain persistent access to network infrastructure
- **Status**: Recently patched but actively exploited against unpatched systems in "Zero Disco" attacks
- **CVE ID**: CVE-2025-20352

### Oracle Zero-Day Vulnerability
- **Description**: Zero-day vulnerability affecting Oracle systems that was exploited in attacks against Harvard University and other customers
- **Impact**: Data theft and system compromise, claimed by Clop ransomware group
- **Status**: Active exploitation as part of broader campaign against Oracle customers
- **CVE ID**: Not specified in the articles

### F5 BIG-IP Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in F5's BIG-IP environment exploited by nation-state actors
- **Impact**: Source code theft, customer information exposure, and potential backdoor access
- **Status**: Disclosed by F5 following nation-state intrusion
- **CVE ID**: Not specified in the articles

## Affected Systems and Products

- **Gladinet CentreStack**: Business file-sharing and collaboration solution
- **Adobe Experience Manager**: Enterprise content management and digital experience platform
- **Cisco IOS/IOS XE Software**: Network operating systems on older, unprotected networking devices
- **Oracle Systems**: Multiple Oracle products targeted in widespread campaign
- **F5 BIG-IP**: Application delivery controllers and load balancers
- **Microsoft Teams**: Targeted through malicious installer certificates in ransomware attacks
- **WordPress Sites**: Used as distribution points for blockchain-based malware campaigns
- **Visual Studio Code Marketplace**: Supply chain risks from exposed secrets and credentials

## Attack Vectors and Techniques

- **EtherHiding Technique**: North Korean hackers hiding malware inside blockchain smart contracts for stealth and resilience
- **Blockchain Smart Contract Abuse**: UNC5142 threat actor using smart contracts to distribute information stealers like Atomic (AMOS) and Lumma
- **eBPF Rootkit Deployment**: LinkPro Linux rootkit using extended Berkeley Packet Filter to hide from detection and activate via magic TCP packets
- **Certificate-Based Attacks**: Malicious Teams installers signed with valid certificates for ransomware distribution
- **Supply Chain Targeting**: Exploitation of exposed secrets in development marketplaces and repositories
- **Phishing Campaigns**: Targeting password manager users with campaigns leveraging trust in credential vaults

## Threat Actor Activities

- **North Korean Groups**: Employing EtherHiding technique for malware distribution, cryptocurrency theft, and espionage operations
- **UNC5142**: Financially motivated actor abusing blockchain smart contracts to distribute information stealing malware through compromised WordPress sites
- **Rhysida Ransomware**: Targeting Microsoft Teams users through malicious installers before Microsoft disrupted operations by revoking certificates
- **Clop Ransomware**: Claiming responsibility for Harvard University breach and broader Oracle customer targeting campaign
- **Nation-State Actors**: Breaching F5 systems with zero-day vulnerabilities to steal BIG-IP source code and customer information
- **Jewelbug (Chinese APT)**: Five-month infiltration of Russian IT service provider, expanding operations beyond Southeast Asia
- **Mysterious Elephant**: Cyber-espionage group targeting government and diplomatic entities in South Asia with custom sophisticated tools