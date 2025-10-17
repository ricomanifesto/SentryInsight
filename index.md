# Exploitation Report

The current threat landscape shows significant active exploitation across multiple platforms and vulnerability types. Critical zero-day vulnerabilities are being exploited in enterprise file-sharing solutions, while attackers leverage recently patched flaws in networking equipment and content management systems. Notable activity includes the exploitation of a maximum-severity Adobe Experience Manager vulnerability that CISA has flagged as actively exploited, and sophisticated campaigns targeting Cisco networking devices with custom rootkits. Threat actors are also employing innovative techniques such as blockchain-based malware distribution and fraudulent certificate signing to evade detection in ransomware campaigns.

## Active Exploitation Details

### Gladinet CentreStack Local File Inclusion Zero-Day
- **Description**: A local file inclusion vulnerability in Gladinet's CentreStack business file-sharing solution that was actively exploited as a zero-day since late in the exploitation timeline
- **Impact**: Allows attackers to access sensitive files and potentially execute arbitrary code on affected systems
- **Status**: Patched by Gladinet with security updates released
- **CVE ID**: CVE-2025-11371

### Adobe Experience Manager Remote Code Execution
- **Description**: A maximum-severity vulnerability in Adobe Experience Manager that allows remote code execution on unpatched systems
- **Impact**: Attackers can execute arbitrary code and potentially gain full control of affected systems
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-20352

### Cisco SNMP Remote Code Execution Flaw
- **Description**: A recently patched remote code execution vulnerability in Cisco networking devices exploited in "Zero Disco" attacks
- **Impact**: Enables deployment of Linux rootkits and targeting of unprotected Linux systems
- **Status**: Recently patched but actively exploited to deploy custom rootkits
- **CVE ID**: CVE-2025-20352

### WatchGuard Fireware Critical Security Flaw
- **Description**: A critical security vulnerability in WatchGuard Fireware that allows unauthenticated attackers to execute arbitrary code
- **Impact**: Complete device takeover by unauthenticated attackers
- **Status**: Recently patched by WatchGuard

## Affected Systems and Products

- **Gladinet CentreStack**: Business file-sharing and cloud storage solution vulnerable to local file inclusion attacks
- **Adobe Experience Manager**: Content management system with maximum-severity remote code execution vulnerability
- **Cisco IOS Software and IOS XE Software**: Networking devices targeted with SNMP exploitation for rootkit deployment
- **WatchGuard Fireware**: VPN and firewall devices susceptible to unauthenticated code execution
- **Zendesk Platform**: Customer service platform being abused for email bombing attacks due to lax authentication
- **Microsoft Teams**: Targeted with malicious installers signed using fraudulent certificates
- **WordPress Sites**: Used as distribution points for blockchain-based malware campaigns

## Attack Vectors and Techniques

- **EtherHiding Technique**: North Korean hackers hiding malware inside blockchain smart contracts for stealthy distribution
- **Blockchain Smart Contract Abuse**: Threat actors using smart contracts to facilitate information stealer distribution (Atomic/AMOS, Lumma)
- **Fraudulent Certificate Signing**: Over 200 certificates used to sign malicious Teams installers in Rhysida ransomware campaigns
- **Linux Rootkit Deployment**: Custom rootkits deployed via Cisco SNMP vulnerabilities targeting AWS-hosted infrastructure
- **Email Bombing**: Exploitation of Zendesk authentication weaknesses to flood target inboxes with threatening messages
- **eBPF-Based Rootkit**: LinkPro rootkit using eBPF technology to hide presence and activate via magic TCP packets

## Threat Actor Activities

- **Vanilla Tempest**: Microsoft-tracked actor using fraudulent certificates in Rhysida ransomware campaigns targeting Teams users
- **UNC5142**: Financially motivated group abusing blockchain smart contracts to distribute information stealers via infected WordPress sites
- **North Korean Groups**: Leveraging EtherHiding technique for malware distribution, cryptocurrency theft, and espionage operations
- **Mysterious Elephant**: Cyber-espionage group targeting government and diplomatic entities in South Asia with sophisticated custom tools
- **Zero Disco Campaign**: Attackers exploiting Cisco SNMP flaws to deploy Linux rootkits, particularly targeting AWS infrastructure