# Exploitation Report

A critical wave of exploitation activity has emerged across multiple platforms, with attackers actively leveraging zero-day vulnerabilities, recently patched flaws, and authentication weaknesses. Notable incidents include the exploitation of CVE-2025-20352 in Cisco networking devices to deploy rootkits, CVE-2025-11371 in Gladinet CentreStack as a zero-day since late 2024, and a maximum-severity Adobe Experience Manager vulnerability being actively exploited in the wild. Threat actors are also abusing Zendesk's authentication weaknesses for email bombing campaigns and leveraging blockchain technology to hide malware distribution. North Korean hackers have been observed using sophisticated techniques like EtherHiding to conceal malware within blockchain smart contracts, while the Rhysida ransomware group has been using fraudulent certificates to sign malicious Teams installers.

## Active Exploitation Details

### Cisco SNMP Remote Code Execution Vulnerability
- **Description**: A remote code execution vulnerability in Cisco networking devices that allows attackers to deploy rootkits on switches and target unprotected Linux systems
- **Impact**: Full compromise of network infrastructure and deployment of persistent rootkits
- **Status**: Recently patched but actively exploited in "Zero Disco" attack campaigns
- **CVE ID**: CVE-2025-20352

### Gladinet CentreStack Zero-Day Vulnerability
- **Description**: A local file inclusion vulnerability in Gladinet's CentreStack business file-sharing solution
- **Impact**: Unauthorized access to local files and potential system compromise
- **Status**: Zero-day actively exploited since late 2024, security updates recently released
- **CVE ID**: CVE-2025-11371

### Adobe Experience Manager Critical Vulnerability
- **Description**: A maximum-severity vulnerability with a perfect 10.0 CVSS score affecting Adobe Experience Manager
- **Impact**: Remote code execution on unpatched systems
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

### WatchGuard Fireware Critical Vulnerability
- **Description**: A critical security flaw in WatchGuard Fireware that allows unauthenticated attackers to execute arbitrary code
- **Impact**: Complete device takeover by unauthenticated attackers
- **Status**: Recently patched after disclosure by security researchers

### Zendesk Authentication Weakness
- **Description**: Widespread lack of proper authentication controls in Zendesk customer service platform
- **Impact**: Email bombing attacks flooding targeted inboxes with menacing messages from legitimate Zendesk corporate accounts
- **Status**: Actively being exploited by cybercriminals for harassment campaigns

## Affected Systems and Products

- **Cisco IOS Software and IOS XE Software**: Networking devices vulnerable to SNMP-based attacks leading to rootkit deployment
- **Gladinet CentreStack**: Business file-sharing solution affected by zero-day local file inclusion vulnerability
- **Adobe Experience Manager**: Content management system with maximum-severity remote code execution flaw
- **WatchGuard Fireware**: Network security appliances vulnerable to unauthenticated code execution
- **Zendesk Platform**: Customer service platform with authentication weaknesses enabling abuse
- **Microsoft Teams**: Targeted by Rhysida ransomware through malicious installers signed with fraudulent certificates
- **WordPress Sites**: Used as distribution points for blockchain-based malware campaigns
- **AWS Infrastructure**: Compromised systems discovered hosting new Linux rootkits

## Attack Vectors and Techniques

- **SNMP Exploitation**: Attackers leveraging Cisco SNMP vulnerabilities to deploy rootkits and compromise network infrastructure
- **EtherHiding Technique**: North Korean hackers hiding malware within Ethereum blockchain smart contracts for stealth and persistence
- **Fraudulent Code Signing**: Rhysida ransomware operators using over 200 revoked certificates to sign malicious Teams installers
- **Blockchain Smart Contract Abuse**: UNC5142 threat actor using smart contracts to distribute information stealers like Atomic and Lumma
- **Email Bombing**: Exploitation of Zendesk authentication weaknesses to flood targets with threatening messages
- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in file-sharing platforms
- **Supply Chain Attacks**: Targeting of developer environments through compromised VS Code marketplace extensions

## Threat Actor Activities

- **Vanilla Tempest**: Microsoft-tracked threat actor using fraudulent certificates in Rhysida ransomware campaigns targeting Teams users
- **UNC5142**: Financially motivated group abusing blockchain smart contracts to distribute information-stealing malware through infected WordPress sites
- **North Korean APT Groups**: Using EtherHiding techniques to hide malware in blockchain smart contracts for cryptocurrency theft and espionage
- **Mysterious Elephant**: Cyber-espionage group targeting government and diplomatic entities in South Asia with sophisticated custom tools
- **Zero Disco Campaign**: Attackers exploiting Cisco vulnerabilities to deploy Linux rootkits including the newly discovered LinkPro rootkit
- **Prosper Breach Actors**: Hackers who compromised financial services company systems affecting 17.6 million accounts
- **Sotheby's Breach Actors**: Threat actors who infiltrated the auction house's systems and stole sensitive financial information