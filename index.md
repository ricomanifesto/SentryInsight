# Exploitation Report

Multiple critical zero-day vulnerabilities are currently under active exploitation, with Chrome V8 engine flaw CVE-2026-11645, Check Point VPN vulnerability, and LiteLLM flaw CVE-2026-42271 being the most severe. Russian-aligned groups continue exploiting the WinRAR vulnerability CVE-2025-8088 against Ukrainian targets nearly a year after patches were released. Meanwhile, supply chain attacks have intensified with the Miasma and Hades campaigns targeting Microsoft repositories and PyPI packages. Government agencies face a three-day deadline to patch Check Point systems following ransomware gang exploitation, while French government messaging systems have suffered account hijacking attacks.

## Active Exploitation Details

### Chrome V8 Zero-Day Vulnerability
- **Description**: High-severity vulnerability in Google Chrome's V8 JavaScript engine
- **Impact**: Remote code execution allowing attackers to compromise victim systems through web browsers
- **Status**: Actively exploited in the wild, patches released by Google
- **CVE ID**: CVE-2026-11645

### Check Point VPN Critical Vulnerability
- **Description**: Critical security flaw in Check Point Remote Access VPN and Mobile Access deployments
- **Impact**: Used by Qilin ransomware operators for zero-day attacks against government systems
- **Status**: Actively exploited as zero-day, CISA has ordered federal agencies to patch within 3 days

### LiteLLM Authentication Bypass
- **Description**: High-severity authentication bypass vulnerability in BerriAI LiteLLM
- **Impact**: Can be chained to achieve unauthenticated remote code execution
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation
- **CVE ID**: CVE-2026-42271

### WinRAR Archive Processing Vulnerability
- **Description**: Security flaw in WinRAR's archive processing functionality
- **Impact**: Remote code execution allowing deployment of credential stealers and data theft malware
- **Status**: Exploited by Russia-aligned groups targeting Ukrainian organizations, patches available since July 2025
- **CVE ID**: CVE-2025-8088

### Veeam Backup & Replication RCE Flaw
- **Description**: Critical remote code execution vulnerability in Veeam's Backup & Replication software
- **Impact**: Allows domain users to execute remote code on backup servers
- **Status**: Patches released by Veeam
- **CVE ID**: CVE-2026-44963

### ServiceNow Unauthenticated Access Flaw
- **Description**: Unauthenticated access vulnerability through vulnerable API endpoint
- **Impact**: Allows attackers to query and access customer instance data
- **Status**: Security incident disclosed, affecting customer data

### Microsoft Exchange Email Spoofing Vulnerability
- **Description**: "Ghost-Sender" vulnerability in Microsoft Exchange Online and hybrid configurations
- **Impact**: Enables attackers to spoof any email address using third-party mail servers or spam filters
- **Status**: Under investigation and exploitation

## Affected Systems and Products

- **Google Chrome**: V8 JavaScript engine vulnerability affecting all Chrome installations
- **Check Point VPN Systems**: Remote Access VPN and Mobile Access products vulnerable to ransomware attacks
- **BerriAI LiteLLM**: Authentication bypass leading to remote code execution
- **WinRAR**: Archive processing vulnerability in versions prior to July 2025 patches
- **Veeam Backup & Replication**: Critical RCE affecting domain-joined backup servers
- **ServiceNow**: Customer instances exposed through API vulnerability
- **Microsoft Exchange**: Online and hybrid configurations with third-party integrations
- **SAP NetWeaver**: Critical vulnerabilities requiring immediate patching
- **SAP Commerce Cloud**: Critical-severity flaws in e-commerce platform
- **French Government Tchap**: Encrypted messaging platform compromised via account hijacking

## Attack Vectors and Techniques

- **Web-Based Exploitation**: Chrome zero-day delivered through malicious websites
- **VPN Infrastructure Attacks**: Check Point systems targeted by ransomware operators for initial access
- **Supply Chain Poisoning**: Miasma and Hades campaigns targeting GitHub repositories and PyPI packages
- **Archive-Based Delivery**: WinRAR exploits distributed through malicious archive files
- **Email Spoofing**: Ghost-Sender technique using Exchange hybrid configurations
- **API Abuse**: Unauthenticated access through vulnerable ServiceNow endpoints
- **Account Hijacking**: Compromised user accounts used to breach government messaging systems
- **Malicious Package Distribution**: Fake banking app updates hosted on GitHub repositories

## Threat Actor Activities

- **Russia-Aligned Groups**: Continued targeting of Ukrainian military and government organizations using WinRAR exploits for data theft and cyberespionage operations
- **Qilin Ransomware**: Exploiting Check Point VPN zero-day for initial access to government networks
- **Miasma Campaign Operators**: Supply chain attacks compromising 73 Microsoft GitHub repositories with password-stealing malware
- **Hades Campaign**: Follow-up supply chain attack targeting PyPI with 37 malicious wheel artifacts across 19 packages
- **Silent Ransom Group**: Targeting US law firms through vishing, IT impersonation, and physical office intrusions
- **NFCShare Malware Distributors**: Spreading Android malware through fake banking application updates on GitHub