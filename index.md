# Exploitation Report

Critical exploitation activity is currently targeting multiple infrastructure components across enterprise and consumer environments. The most significant threats include the FIRESTARTER malware persisting on Cisco Firepower devices despite security patches, active exploitation of LMDeploy vulnerabilities within hours of disclosure, ongoing attacks against over 10,000 vulnerable Zimbra servers, and the compromise of the Bitwarden CLI npm package. State-sponsored groups, particularly Chinese APTs, are demonstrating sophisticated persistence techniques while cybercriminal groups are leveraging AI-enhanced phishing campaigns and exploiting WordPress plugin vulnerabilities for initial access.

## Active Exploitation Details

### FIRESTARTER Malware on Cisco Firepower Devices
- **Description**: Custom malware targeting Cisco Firepower and Secure Firewall devices running Adaptive Security Appliance (ASA) software with persistence capabilities
- **Impact**: Maintains access to federal agency network infrastructure despite security patches and updates, allowing long-term espionage and potential lateral movement
- **Status**: Actively deployed on federal civilian agency devices, survives standard patching processes

### LMDeploy Remote Code Execution Vulnerability
- **Description**: High-severity security flaw in LMDeploy, an open-source toolkit for compressing, deploying, and serving large language models
- **Impact**: Remote code execution capabilities allowing complete system compromise
- **Status**: Exploited in the wild within 13 hours of public disclosure
- **CVE ID**: CVE-2026-33626

### Zimbra Cross-Site Scripting Attacks
- **Description**: Cross-site scripting (XSS) security flaw affecting Zimbra Collaboration Suite instances
- **Impact**: Enables session hijacking, credential theft, and potential access to email systems
- **Status**: Over 10,000 ZCS instances exposed online are vulnerable to ongoing attacks

### Breeze Cache WordPress Plugin File Upload Vulnerability
- **Description**: Critical vulnerability allowing arbitrary file uploads without authentication in the Breeze Cache plugin for WordPress
- **Impact**: Remote code execution and full website compromise through malicious file uploads
- **Status**: Actively exploited by threat actors targeting WordPress installations

### PackageKit Privilege Escalation (Pack2TheRoot)
- **Description**: Vulnerability in the PackageKit daemon allowing local privilege escalation
- **Impact**: Local Linux users can install or remove system packages and gain root permissions
- **Status**: Recently disclosed vulnerability affecting Linux distributions

### Bitwarden CLI npm Package Compromise
- **Description**: Malicious version of the @bitwarden/cli package uploaded to npm containing credential-stealing payload
- **Impact**: Developer credential theft and potential supply chain compromise affecting projects using the malicious package
- **Status**: Package was compromised and later removed, but may have affected developers who downloaded during the compromise window

## Affected Systems and Products

- **Cisco Firepower and Secure Firewall**: Devices running Adaptive Security Appliance (ASA) software
- **LMDeploy**: Open-source toolkit for large language model deployment
- **Zimbra Collaboration Suite**: Over 10,000 instances exposed online
- **WordPress Sites**: Using Breeze Cache plugin
- **Linux Distributions**: Systems running PackageKit daemon
- **npm Ecosystem**: Developers using Bitwarden CLI package
- **Apple iOS Devices**: 26 fake cryptocurrency wallet apps discovered on App Store

## Attack Vectors and Techniques

- **Persistence Mechanisms**: FIRESTARTER malware survives security patches and updates on Cisco devices
- **Supply Chain Attacks**: Compromise of legitimate npm packages and trojanized software distribution
- **Social Engineering**: Microsoft Teams deployment of Snow malware suite and AI-enhanced phishing campaigns
- **Cross-Site Scripting**: Web-based attacks targeting email infrastructure
- **File Upload Exploitation**: Bypassing authentication to upload malicious files
- **ClickFix Campaigns**: Lazarus group targeting macOS users with fake error messages
- **Trojanized Software**: Distribution of malicious SumatraPDF versions containing AdaptixC2 Beacon

## Threat Actor Activities

- **UNC6692**: Using Microsoft Teams for social engineering to deploy custom Snow malware suite including browser extensions, tunnelers, and backdoors
- **Chinese APT Groups**: Operating industrialized botnets and targeting cloud infrastructure using Microsoft Outlook, Slack, Discord, and file.io for command and control
- **Tropic Trooper**: Chinese state-sponsored group targeting home routers and Japanese organizations using trojanized SumatraPDF and GitHub infrastructure
- **Lazarus Group**: North Korean APT leveraging ClickFix techniques for initial access against macOS users and high-value targets
- **ShinyHunters**: Extortion group threatening data leaks after compromising ADT home security systems
- **BlackFile Group**: New financially motivated threat actor targeting retail and hospitality organizations with data theft and extortion since February 2026
- **Myanmar-based Criminal Ring**: 29 individuals charged for financial fraud targeting US citizens through fake investment sites