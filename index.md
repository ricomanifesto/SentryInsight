# Exploitation Report

Critical exploitation activity has surged across multiple fronts, with threat actors actively leveraging both zero-day vulnerabilities and recently patched flaws. The most severe incidents include active exploitation of a maximum-severity Adobe Experience Manager vulnerability (CVE-2024-45138) added to CISA's Known Exploited Vulnerabilities catalog, and a zero-day local file inclusion vulnerability in Gladinet's CentreStack business solution (CVE-2025-11371) that has been exploited since late 2024. Additionally, cybercriminals are exploiting a recently patched Cisco SNMP vulnerability (CVE-2025-20352) to deploy Linux rootkits on networking infrastructure, while North Korean threat actors have been observed using innovative blockchain-based attack techniques to distribute malware and steal cryptocurrency.

## Active Exploitation Details

### Adobe Experience Manager Remote Code Execution
- **Description**: A maximum-severity vulnerability in Adobe Experience Manager that allows remote code execution on unpatched systems
- **Impact**: Attackers can execute arbitrary code on vulnerable Adobe Experience Manager installations, potentially leading to complete system compromise
- **Status**: Currently being actively exploited in attacks; CISA has added it to the Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2024-45138

### Gladinet CentreStack Local File Inclusion Zero-Day
- **Description**: A local file inclusion vulnerability in Gladinet's CentreStack business file-sharing solution that was being exploited as a zero-day
- **Impact**: Threat actors can access sensitive files and potentially achieve code execution through file inclusion attacks
- **Status**: Actively exploited since late 2024; security updates have now been released by Gladinet
- **CVE ID**: CVE-2025-11371

### Cisco SNMP Remote Code Execution
- **Description**: A recently patched remote code execution vulnerability in older Cisco IOS Software and IOS XE Software devices
- **Impact**: Attackers can deploy Linux rootkits and gain persistent access to network infrastructure
- **Status**: Recently patched but being actively exploited against unprotected older devices in "Zero Disco" attacks
- **CVE ID**: CVE-2025-20352

## Affected Systems and Products

- **Adobe Experience Manager**: Web content management platform vulnerable to remote code execution attacks
- **Gladinet CentreStack**: Business file-sharing and collaboration solution affected by local file inclusion vulnerability
- **Cisco IOS Software and IOS XE Software**: Older networking devices vulnerable to SNMP-based remote code execution
- **Microsoft Teams**: Targeted by Rhysida ransomware through fraudulent certificate abuse
- **WordPress Sites**: Being used as distribution points for blockchain-based malware campaigns
- **F5 BIG-IP**: Network infrastructure compromised by nation-state actors with source code theft

## Attack Vectors and Techniques

- **EtherHiding Technique**: North Korean hackers hiding malware inside blockchain smart contracts for stealth distribution
- **Fraudulent Code Signing**: Vanilla Tempest using over 200 revoked certificates to sign malicious Teams installers
- **Linux Rootkit Deployment**: LinkPro rootkit using eBPF technology and magic TCP packet activation on AWS infrastructure
- **Smart Contract Abuse**: UNC5142 leveraging blockchain smart contracts to distribute information stealers like Atomic and Lumma
- **Supply Chain Targeting**: Attacks on password managers through phishing campaigns exploiting user trust
- **Certificate Authority Compromise**: Large-scale certificate abuse for signing malicious ransomware payloads

## Threat Actor Activities

- **Vanilla Tempest**: Microsoft-tracked ransomware group behind Rhysida campaigns using fraudulent certificates to sign malicious Microsoft Teams installers
- **UNC5142**: Financially motivated threat actor abusing blockchain smart contracts to distribute information stealers through compromised WordPress sites
- **North Korean Groups**: Multiple DPRK-linked actors using EtherHiding techniques for malware distribution and cryptocurrency theft operations
- **Jewelbug**: Chinese threat group conducting five-month infiltration of Russian IT service providers, expanding operations beyond Southeast Asia
- **Nation-State Actors**: Sophisticated attackers compromising F5's BIG-IP environment and stealing source code along with customer information
- **Mysterious Elephant**: Cyber-espionage group targeting government and diplomatic entities in South Asia with custom sophisticated tools