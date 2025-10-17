# Exploitation Report

The current threat landscape reveals a concerning surge in active exploitation across multiple critical vulnerabilities, with several zero-day attacks and recently patched flaws being leveraged by sophisticated threat actors. Most notably, threat actors are exploiting a zero-day vulnerability in Gladinet's CentreStack file-sharing software (CVE-2025-11371), a maximum-severity Adobe Experience Manager flaw, and a Cisco SNMP vulnerability (CVE-2025-20352) to deploy Linux rootkits. Nation-state actors, including Chinese and North Korean groups, are conducting advanced campaigns using innovative techniques such as blockchain-based malware distribution and AI-optimized attack chains. The exploitation activity spans from enterprise software vulnerabilities to supply chain compromises, highlighting the broad attack surface that organizations must defend against.

## Active Exploitation Details

### Gladinet CentreStack Zero-Day Vulnerability
- **Description**: Local file inclusion vulnerability in Gladinet's CentreStack business file-sharing solution that has been actively exploited as a zero-day since late 2024
- **Impact**: Allows threat actors to gain unauthorized access to sensitive files and potentially execute arbitrary code on affected systems
- **Status**: Security updates have been released to address the vulnerability
- **CVE ID**: CVE-2025-11371

### Adobe Experience Manager Critical Flaw
- **Description**: Maximum-severity vulnerability in Adobe Experience Manager with a perfect CVSS score of 10.0
- **Impact**: Enables attackers to execute arbitrary code on unpatched systems, providing complete system compromise
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation in the wild
- **Affected Systems**: Adobe Experience Manager installations

### Cisco SNMP Remote Code Execution Vulnerability
- **Description**: Remote code execution vulnerability in older Cisco IOS Software and IOS XE Software networking devices
- **Impact**: Allows threat actors to deploy Linux rootkits and gain persistent access to network infrastructure
- **Status**: Recently patched but actively exploited against unprotected systems
- **CVE ID**: CVE-2025-20352

### Oracle Zero-Day Attack
- **Description**: Zero-day vulnerability in Oracle systems exploited in coordinated attacks against multiple organizations
- **Impact**: Data theft and system compromise, with the Clop ransomware group claiming responsibility for breaches
- **Status**: Part of broader campaign targeting Oracle customers, including Harvard University

### F5 BIG-IP Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in F5 BIG-IP systems exploited by nation-state actors
- **Impact**: Source code theft, exposure of customer information, and potential backdoor access to critical network infrastructure
- **Status**: Ongoing investigation with F5 working to address the vulnerabilities

## Affected Systems and Products

- **Gladinet CentreStack**: Business file-sharing and collaboration platform vulnerable to local file inclusion attacks
- **Adobe Experience Manager**: Enterprise content management system with critical remote code execution vulnerability
- **Cisco IOS Software and IOS XE Software**: Older networking devices vulnerable to SNMP-based attacks
- **Oracle Systems**: Multiple Oracle products targeted in zero-day campaign affecting enterprise customers
- **F5 BIG-IP**: Load balancing and application delivery systems compromised by nation-state actors
- **Microsoft Visual Studio Code Marketplace**: Over 550 unique secrets exposed, creating supply chain risks
- **WordPress Sites**: Compromised sites used as infrastructure for blockchain-based malware distribution
- **Microsoft Teams**: Targeted by Rhysida ransomware through malicious installer certificates
- **Windows 11**: HTTP/2 localhost connectivity issues affecting application functionality

## Attack Vectors and Techniques

- **EtherHiding Technique**: North Korean hackers embedding malware within blockchain smart contracts for stealth and resilience
- **Blockchain Smart Contract Abuse**: UNC5142 threat group using smart contracts to distribute Atomic (AMOS) and Lumma Stealer malware
- **Linux Rootkit Deployment**: Advanced rootkits including LinkPro using eBPF technology to hide from detection and activate via magic TCP packets
- **Supply Chain Compromise**: Exploitation of VS Code marketplace secrets and malicious Teams installer certificates
- **AI-Optimized Attack Chains**: Chinese hackers testing artificial intelligence to enhance attack methodologies in Taiwan
- **Certificate-Based Attacks**: Rhysida ransomware using over 200 fraudulent certificates to sign malicious Teams installers
- **SNMP Protocol Exploitation**: Remote code execution through vulnerable SNMP implementations in network devices

## Threat Actor Activities

- **North Korean APT Groups**: Conducting sophisticated campaigns using EtherHiding techniques for cryptocurrency theft and espionage operations
- **UNC5142**: Financially motivated threat group leveraging blockchain technology and compromised WordPress sites for information stealer distribution
- **Rhysida Ransomware**: Targeting Microsoft Teams users through certificate-based social engineering attacks
- **Chinese Nation-State Actors**: Testing AI-enhanced attack methodologies and infiltrating Russian IT networks through the Jewelbug campaign
- **Clop Ransomware Group**: Exploiting Oracle zero-day vulnerabilities in coordinated attacks against educational institutions and enterprises
- **Mysterious Elephant**: Cyber-espionage group targeting South Asian government and diplomatic entities with custom sophisticated tools
- **Nation-State Actors**: Conducting advanced persistent threat campaigns against F5 infrastructure and exposing critical source code