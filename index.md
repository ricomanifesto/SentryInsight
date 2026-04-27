# Exploitation Report

Current threat activity reveals a concerning landscape of active exploitation targeting critical infrastructure and enterprise systems. Notable incidents include the rapid exploitation of LMDeploy within 13 hours of disclosure (CVE-2026-33626), active attacks against over 10,000 vulnerable Zimbra servers through XSS vulnerabilities, and the deployment of persistent malware like Firestarter on Cisco Firepower devices that survives security updates. CISA has added four new vulnerabilities to their Known Exploited Vulnerabilities catalog, affecting SimpleHelp, Samsung MagicINFO 9 Server, and D-Link routers. Additional exploitation activity includes attacks on WordPress sites through the Breeze Cache plugin and the emergence of sophisticated social engineering campaigns using fake CAPTCHA schemes and Microsoft Teams for malware delivery.

## Active Exploitation Details

### LMDeploy Remote Code Execution Vulnerability
- **Description**: High-severity security flaw in the open-source LMDeploy toolkit for compressing, deploying, and serving large language models
- **Impact**: Allows attackers to execute arbitrary code on affected systems
- **Status**: Actively exploited in the wild within 13 hours of public disclosure
- **CVE ID**: CVE-2026-33626

### Zimbra Cross-Site Scripting (XSS) Vulnerability
- **Description**: Cross-site scripting security flaw affecting Zimbra Collaboration Suite instances
- **Impact**: Enables attackers to execute malicious scripts in users' browsers and potentially steal credentials
- **Status**: Currently under active exploitation with over 10,000 vulnerable servers exposed online

### Breeze Cache WordPress Plugin File Upload Vulnerability
- **Description**: Critical vulnerability allowing arbitrary file uploads without authentication
- **Impact**: Enables attackers to upload malicious files and potentially gain full control of WordPress sites
- **Status**: Actively exploited by hackers targeting WordPress installations

### Pack2TheRoot Linux Privilege Escalation
- **Description**: Vulnerability in the PackageKit daemon affecting Linux systems
- **Impact**: Allows local users to install/remove system packages and gain root permissions
- **Status**: Newly disclosed vulnerability with potential for widespread exploitation

### CISA KEV Additions
- **Description**: Four vulnerabilities affecting SimpleHelp, Samsung MagicINFO 9 Server, and D-Link DIR-823X series routers
- **Impact**: Various impacts including remote code execution and unauthorized access
- **Status**: Added to Known Exploited Vulnerabilities catalog with May 2026 federal remediation deadline

## Affected Systems and Products

- **LMDeploy**: Open-source toolkit for large language model deployment and serving
- **Zimbra Collaboration Suite**: Over 10,000 instances exposed online and vulnerable to XSS attacks
- **Breeze Cache WordPress Plugin**: WordPress sites using this caching plugin for performance optimization
- **PackageKit Daemon**: Linux distributions utilizing PackageKit for package management
- **Cisco Firepower/ASA Devices**: Firewalls running Adaptive Security Appliance software targeted by Firestarter malware
- **SimpleHelp**: Remote support and access software
- **Samsung MagicINFO 9 Server**: Digital signage content management system
- **D-Link DIR-823X Series**: Consumer and small business routers
- **Microsoft Teams**: Enterprise communication platform exploited for malware delivery
- **Apple App Store**: 26 malicious cryptocurrency wallet applications targeting seed phrases

## Attack Vectors and Techniques

- **Rapid Exploitation**: LMDeploy vulnerability exploited within 13 hours of disclosure, demonstrating threat actors' speed
- **Social Engineering via Microsoft Teams**: UNC6692 threat group using Teams to deploy custom "Snow" malware suite
- **Fake CAPTCHA Schemes**: International Revenue Share Fraud (IRSF) campaigns tricking users into sending premium SMS messages
- **Trojanized Software**: Tropic Trooper using compromised SumatraPDF reader to deploy AdaptixC2 beacon
- **Persistent Malware**: Firestarter backdoor surviving security patches and updates on Cisco devices
- **ClickFix Campaigns**: North Korea's Lazarus group targeting macOS users with fake error messages
- **File Upload Exploitation**: Unauthorized file uploads through vulnerable WordPress plugins
- **Cloud Service Abuse**: Chinese APTs leveraging Microsoft Outlook, Slack, Discord, and file.io for command and control

## Threat Actor Activities

- **UNC6692**: Deploying custom "Snow" malware suite through Microsoft Teams social engineering, including browser extensions, tunnelers, and backdoors
- **Lazarus Group**: North Korean state-sponsored group targeting macOS users through ClickFix campaigns and fake error dialogs
- **Tropic Trooper**: Chinese-speaking APT group using trojanized SumatraPDF and targeting Japanese organizations and home routers
- **Chinese State-Sponsored Groups**: Industrializing botnet operations and using compromised cloud tools to spy on Mongolia
- **BlackFile Extortion Group**: New financially motivated group targeting retail and hospitality organizations with data theft and extortion since February 2026
- **ShinyHunters**: Extortion group threatening to leak ADT customer data unless ransom demands are met
- **Chinese National**: Individual posed as U.S. researcher in spear-phishing campaign targeting NASA employees and defense software
- **Myanmar Criminal Ring**: 29 individuals charged for financial fraud targeting U.S. citizens through fake investment sites