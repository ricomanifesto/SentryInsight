# Exploitation Report

Critical vulnerability exploitation is currently targeting enterprise infrastructure with multiple zero-day attacks and active exploitation campaigns. Most concerning are the active exploitation of CVE-2025-11371 in Gladinet file-sharing software, CVE-2025-20352 affecting Cisco networking devices, and maximum-severity Adobe Experience Manager vulnerabilities. Nation-state actors are deploying sophisticated rootkits and leveraging blockchain-based malware distribution techniques, while ransomware groups continue targeting major organizations through compromised Microsoft Teams installations and Oracle zero-day exploits.

## Active Exploitation Details

### Gladinet CentreStack Zero-Day Vulnerability
- **Description**: Local file inclusion vulnerability in Gladinet's CentreStack business file-sharing solution
- **Impact**: Allows threat actors to gain unauthorized access to file systems and potentially execute arbitrary code
- **Status**: Actively exploited as zero-day since late 2024, security updates now available
- **CVE ID**: CVE-2025-11371

### Cisco SNMP Remote Code Execution Flaw
- **Description**: Remote code execution vulnerability in Cisco IOS Software and IOS XE Software SNMP implementation
- **Impact**: Enables deployment of Linux rootkits and persistent access to network infrastructure
- **Status**: Recently patched but actively exploited in "Zero Disco" attacks against older unprotected devices
- **CVE ID**: CVE-2025-20352

### Adobe Experience Manager Critical Vulnerability
- **Description**: Maximum-severity vulnerability in Adobe Experience Manager with a perfect 10.0 CVSS score
- **Impact**: Allows attackers to execute arbitrary code on unpatched systems
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

### Oracle Zero-Day Vulnerability
- **Description**: Zero-day vulnerability in Oracle systems exploited by Clop ransomware group
- **Impact**: Data theft and system compromise of major organizations including Harvard University
- **Status**: Active exploitation in ongoing campaign targeting Oracle customers

### F5 BIG-IP Zero-Day Exploits
- **Description**: Multiple zero-day vulnerabilities in F5 BIG-IP environment
- **Impact**: Source code theft, exposure of undisclosed vulnerabilities, and customer information compromise
- **Status**: Exploited by nation-state actors in sophisticated breach

## Affected Systems and Products

- **Gladinet CentreStack**: Business file-sharing solution vulnerable to local file inclusion attacks
- **Cisco IOS/IOS XE**: Networking devices with SNMP vulnerabilities, particularly older unprotected systems
- **Adobe Experience Manager**: Web content management systems with critical RCE vulnerability
- **Oracle Systems**: Various Oracle products targeted in zero-day campaign
- **F5 BIG-IP**: Application delivery controllers and load balancers
- **Microsoft Teams**: Targeted through malicious installer certificates
- **WordPress Sites**: Compromised sites used for blockchain-based malware distribution
- **Windows 11**: Localhost HTTP/2 connectivity issues affecting local applications

## Attack Vectors and Techniques

- **EtherHiding Technique**: North Korean hackers embedding malware in blockchain smart contracts for stealth distribution
- **Blockchain Smart Contract Abuse**: UNC5142 threat group using smart contracts to distribute information stealers like Atomic (AMOS) and Lumma
- **Linux Rootkit Deployment**: LinkPro rootkit using eBPF technology with magic TCP packet activation
- **Certificate-Based Attacks**: Rhysida ransomware using signed malicious Teams installers
- **Phishing Campaigns**: Targeting password manager users, particularly LastPass customers
- **Supply Chain Compromise**: Over 550 unique secrets exposed in Visual Studio Code marketplaces
- **Magic TCP Packets**: LinkPro rootkit activation mechanism for stealth operations

## Threat Actor Activities

- **North Korean Groups**: Leveraging EtherHiding for cryptocurrency theft and espionage operations
- **UNC5142**: Financially motivated group abusing blockchain infrastructure for malware distribution
- **Rhysida Ransomware**: Targeting Microsoft Teams users with signed malicious installers
- **Clop Ransomware Group**: Exploiting Oracle zero-days in campaign against major organizations
- **Chinese APT Jewelbug**: Five-month infiltration of Russian IT service provider infrastructure
- **Mysterious Elephant**: Cyber-espionage group using custom tools against South Asian government entities
- **Nation-State Actors**: Sophisticated multi-month breach of F5 systems with source code theft
- **Zero Disco Campaign**: Exploiting Cisco vulnerabilities for rootkit deployment on network infrastructure