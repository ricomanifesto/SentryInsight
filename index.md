# Exploitation Report

Critical vulnerability exploitation activity is currently targeting multiple high-value systems across enterprise and government networks. The most significant threats include active zero-day exploitation against Adobe Experience Manager systems, ongoing attacks against Cisco networking infrastructure, and sophisticated blockchain-based malware distribution campaigns by North Korean threat actors. Organizations are also facing targeted ransomware attacks leveraging Microsoft Teams as an attack vector, while supply chain vulnerabilities in development platforms pose additional risks to enterprise environments.

## Active Exploitation Details

### Adobe Experience Manager Remote Code Execution Vulnerability
- **Description**: A maximum-severity vulnerability in Adobe Experience Manager allowing remote code execution on unpatched systems
- **Impact**: Attackers can execute arbitrary code and gain complete system control
- **Status**: Actively exploited in the wild and added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-20352

### Cisco SNMP Remote Code Execution Vulnerability
- **Description**: A remote code execution vulnerability in older Cisco IOS Software and IOS XE Software SNMP implementations
- **Impact**: Threat actors can deploy Linux rootkits and gain persistent access to networking infrastructure
- **Status**: Recently patched but actively exploited against unprotected legacy devices
- **CVE ID**: CVE-2025-20352

### Gladinet CentreStack Zero-Day Vulnerability
- **Description**: A local file inclusion vulnerability in Gladinet's CentreStack business file-sharing solution
- **Impact**: Allows unauthorized access to sensitive files and system information
- **Status**: Zero-day exploitation confirmed since late 2024, security updates now available
- **CVE ID**: CVE-2025-11371

### Oracle Zero-Day Vulnerability
- **Description**: An undisclosed zero-day vulnerability affecting Oracle systems
- **Impact**: System compromise and data exfiltration capabilities
- **Status**: Actively exploited by Clop ransomware group in targeted attacks

## Affected Systems and Products

- **Adobe Experience Manager**: All unpatched versions vulnerable to remote code execution
- **Cisco IOS Software and IOS XE Software**: Older versions with SNMP enabled at risk of rootkit deployment
- **Gladinet CentreStack**: Business file-sharing solutions vulnerable to local file inclusion attacks
- **Microsoft Teams**: Targeted by malicious installers signed with revoked certificates
- **Oracle Systems**: Various Oracle products affected by zero-day exploitation
- **WordPress Sites**: Compromised sites used as distribution points for blockchain-based malware
- **F5 BIG-IP**: Source code and customer information exposed in nation-state breach

## Attack Vectors and Techniques

- **EtherHiding Technique**: North Korean actors hiding malware payloads within Ethereum blockchain smart contracts
- **Blockchain Smart Contracts**: UNC5142 threat group abusing smart contracts to distribute information stealers like Atomic (AMOS) and Lumma
- **Supply Chain Attacks**: Malicious Teams installers distributed with legitimate-looking certificates
- **Rootkit Deployment**: Linux rootkits including LinkPro using eBPF technology for stealth and persistence
- **Magic TCP Packets**: Rootkit activation mechanisms triggered by specially crafted network traffic
- **Phishing Campaigns**: Targeted attacks against password manager users to harvest credentials

## Threat Actor Activities

- **North Korean APT Groups**: Employing EtherHiding techniques for cryptocurrency theft and espionage operations
- **UNC5142**: Financially motivated group leveraging blockchain technology to distribute information-stealing malware
- **Rhysida Ransomware Group**: Conducting targeted attacks using malicious Microsoft Teams installers
- **Clop Ransomware Group**: Exploiting Oracle zero-day vulnerabilities in attacks against educational institutions including Harvard University
- **Chinese APT Groups**: Jewelbug group conducting long-term infiltration of Russian IT service providers
- **Nation-State Actors**: Sophisticated intrusion into F5 systems exposing BIG-IP source code and customer data
- **Mysterious Elephant**: Cyber-espionage group targeting government and diplomatic entities in South Asia with custom toolsets