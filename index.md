# Exploitation Report

Critical zero-day and actively exploited vulnerabilities are posing significant threats across enterprise environments. Most notably, attackers are exploiting CVE-2025-11371, a local file inclusion vulnerability in Gladinet CentreStack business solutions, which has been leveraged as a zero-day since late 2024. Additionally, CISA has added a maximum-severity Adobe Experience Manager vulnerability to its Known Exploited Vulnerabilities catalog, indicating active exploitation in the wild. Nation-state actors continue to demonstrate sophisticated attack capabilities, with Chinese threat groups employing AI-optimized attack chains and novel techniques like EtherHiding to hide malware in blockchain smart contracts. The threat landscape is further complicated by supply chain attacks targeting VS Code extensions and the emergence of advanced Linux rootkits using eBPF technology.

## Active Exploitation Details

### Gladinet CentreStack Zero-Day Vulnerability
- **Description**: Local file inclusion vulnerability in Gladinet's CentreStack business file-sharing solution
- **Impact**: Allows threat actors to access and potentially exfiltrate sensitive files from affected systems
- **Status**: Actively exploited as zero-day since late 2024; security updates now available
- **CVE ID**: CVE-2025-11371

### Adobe Experience Manager Critical Flaw
- **Description**: Maximum-severity vulnerability in Adobe Experience Manager with a perfect CVSS score of 10.0
- **Impact**: Enables attackers to execute arbitrary code on unpatched systems
- **Status**: Actively exploited in attacks; added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: Not specified in articles

### Oracle Zero-Day Attack
- **Description**: Zero-day vulnerability affecting Oracle systems used in enterprise environments
- **Impact**: Data exfiltration and system compromise; specifically impacted Harvard University
- **Status**: Actively exploited by Clop ransomware group in broader campaign against Oracle customers
- **CVE ID**: Not specified in articles

### Cisco IOS Software SNMP Vulnerability
- **Description**: Security flaw impacting Cisco IOS Software and IOS XE Software related to SNMP functionality
- **Impact**: Allows deployment of Linux rootkits on older systems
- **Status**: Recently disclosed and exploited in "Zero Disco" campaign attacks
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **Gladinet CentreStack**: Business file-sharing and collaboration solution
- **Adobe Experience Manager**: Enterprise content management platform
- **Oracle Systems**: Various Oracle products used by enterprise customers
- **Cisco IOS/IOS XE**: Network infrastructure devices running affected software versions
- **Microsoft Teams**: Targeted by Rhysida ransomware through malicious installers
- **WordPress Sites**: Used as infrastructure for blockchain-based malware distribution
- **Visual Studio Code Extensions**: Over 100 extensions with exposed access tokens
- **F5 BIG-IP**: Network security and application delivery systems

## Attack Vectors and Techniques

- **EtherHiding**: North Korean hackers hiding malware inside blockchain smart contracts for stealth and resilience
- **Blockchain Smart Contract Abuse**: UNC5142 threat group using smart contracts to distribute information stealers like Atomic (AMOS) and Lumma
- **AI-Optimized Attack Chains**: Chinese hackers testing enhanced attack methodologies in Taiwan
- **Certificate-Based Attacks**: Rhysida ransomware using over 200 certificates to sign malicious Teams installers
- **eBPF Rootkit Technology**: LinkPro Linux rootkit using extended Berkeley Packet Filter to hide presence and activate via magic TCP packets
- **Supply Chain Attacks**: VS Code extension publishers exposing access tokens that could allow malicious updates
- **Social Engineering**: Fake LastPass and Bitwarden breach notifications leading to PC compromises

## Threat Actor Activities

- **Chinese State-Sponsored Groups**: Testing AI-enhanced attack capabilities in Taiwan; Jewelbug group infiltrating Russian IT networks for extended periods
- **North Korean Hackers**: Employing EtherHiding technique for cryptocurrency theft and espionage operations
- **UNC5142**: Financially motivated group abusing blockchain infrastructure to distribute information-stealing malware
- **Rhysida Ransomware**: Targeting Microsoft Teams users with certificate-signed malicious installers
- **Clop Ransomware Group**: Exploiting Oracle zero-day vulnerabilities in campaign against multiple organizations including Harvard University
- **Nation-State Actors**: Compromising F5 BIG-IP environments and stealing source code and vulnerability information
- **Mysterious Elephant**: Cyber-espionage group targeting government and diplomatic entities in South Asia with custom sophisticated tools