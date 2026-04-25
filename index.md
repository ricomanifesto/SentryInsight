# Exploitation Report

Critical vulnerability exploitation continues to escalate across multiple platforms, with attackers rapidly weaponizing newly disclosed flaws and deploying sophisticated attack campaigns. The most concerning activity includes the exploitation of CVE-2026-33626 in LMDeploy within just 13 hours of public disclosure, active attacks against over 10,000 vulnerable Zimbra servers, and persistent malware targeting Cisco Firepower devices that survives security patches. Supply chain compromises are also accelerating, affecting critical developer tools like Bitwarden CLI and Checkmarx KICS, while threat actors leverage social engineering through legitimate platforms like Microsoft Teams to deploy advanced malware suites.

## Active Exploitation Details

### LMDeploy Remote Code Execution Vulnerability
- **Description**: High-severity security flaw in LMDeploy, an open-source toolkit for compressing, deploying, and serving Large Language Models
- **Impact**: Attackers can achieve remote code execution on affected systems
- **Status**: Actively exploited in the wild within 13 hours of public disclosure
- **CVE ID**: CVE-2026-33626

### Zimbra Cross-Site Scripting Vulnerability
- **Description**: Cross-site scripting (XSS) security flaw affecting Zimbra Collaboration Suite (ZCS) instances
- **Impact**: Enables malicious script execution in user browsers and potential data theft
- **Status**: Currently under active exploitation with over 10,000 exposed servers vulnerable

### Breeze Cache WordPress Plugin File Upload Vulnerability
- **Description**: Critical vulnerability in the Breeze Cache plugin for WordPress allowing arbitrary file uploads
- **Impact**: Attackers can upload malicious files to servers without authentication, leading to complete system compromise
- **Status**: Actively exploited by threat actors

### Pack2TheRoot Linux Privilege Escalation
- **Description**: Vulnerability in the PackageKit daemon affecting Linux systems
- **Impact**: Allows local users to install or remove system packages and gain root permissions
- **Status**: Recently disclosed vulnerability with potential for widespread exploitation

### FIRESTARTER Backdoor on Cisco Devices
- **Description**: Custom malware persisting on Cisco Firepower and Secure Firewall devices running Adaptive Security Appliance (ASA)
- **Impact**: Provides persistent access to network infrastructure that survives firmware updates and security patches
- **Status**: Confirmed deployment on federal civilian agency device, remains persistent despite patching efforts

## Affected Systems and Products

- **LMDeploy**: Open-source toolkit for Large Language Model deployment and serving
- **Zimbra Collaboration Suite**: Email and collaboration platform with over 10,000 exposed instances
- **Breeze Cache WordPress Plugin**: WordPress caching plugin allowing unauthenticated file uploads
- **Linux PackageKit Daemon**: Package management system across various Linux distributions
- **Cisco Firepower and Secure Firewall**: Network security appliances running ASA software
- **SimpleHelp, Samsung MagicINFO 9 Server, D-Link DIR-823X**: Products recently added to CISA's Known Exploited Vulnerabilities catalog
- **Bitwarden CLI npm Package**: Command-line interface package for Bitwarden password manager
- **Checkmarx KICS**: Infrastructure-as-Code security analysis tool with compromised Docker images and VSCode extensions

## Attack Vectors and Techniques

- **Rapid Exploitation**: Attackers weaponizing vulnerabilities within hours of public disclosure, as seen with the LMDeploy flaw
- **Social Engineering via Microsoft Teams**: UNC6692 threat group impersonating IT help desk personnel to deploy SNOW malware suite
- **Supply Chain Compromise**: Malicious packages injected into software distribution channels including npm repositories and Docker images
- **Persistent Malware**: FIRESTARTER backdoor designed to survive system updates and security patches
- **Trojanized Software**: Legitimate applications like SumatraPDF modified to deploy malicious payloads
- **Cross-Site Scripting**: Exploitation of XSS vulnerabilities in web applications for credential theft and session hijacking
- **Vishing and Social Engineering**: BlackFile extortion group targeting retail and hospitality organizations through voice phishing
- **ClickFix Campaigns**: Lazarus group leveraging fake browser error messages targeting macOS users

## Threat Actor Activities

- **UNC6692**: Social engineering campaigns via Microsoft Teams to deploy custom SNOW malware suite including browser extensions, tunnelers, and backdoors
- **BlackFile Extortion Group**: New financially motivated group conducting data theft and extortion attacks against retail and hospitality organizations since February 2026
- **Tropic Trooper APT**: Chinese state-sponsored group using trojanized SumatraPDF and GitHub repositories to deploy AdaptixC2 Beacon, expanding targeting to home routers and Japanese organizations
- **Lazarus Group**: North Korean APT continuing ClickFix campaigns targeting macOS users and high-value organizational leaders
- **Chinese APT Groups**: Multiple state-backed groups conducting espionage operations against Mongolia using cloud services like Microsoft Outlook, Slack, Discord, and file.io for command and control
- **ShinyHunters**: Extortion group threatening ADT with data leak unless ransom demands are met
- **Chinese Social Engineering Campaign**: Targeting NASA employees and U.S. defense software through sophisticated phishing operations
- **Trigona Ransomware Operators**: Deploying custom data exfiltration tools for faster and more efficient data theft during attacks