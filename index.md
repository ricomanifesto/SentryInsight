# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems worldwide. The LMDeploy toolkit experienced rapid exploitation of CVE-2026-33626 within just 13 hours of disclosure, demonstrating the speed at which attackers capitalize on newly disclosed vulnerabilities. CISA has added four actively exploited vulnerabilities to its Known Exploited Vulnerabilities catalog, including flaws in SimpleHelp, Samsung MagicINFO 9 Server, and D-Link routers. Over 10,000 Zimbra Collaboration Suite instances remain vulnerable to ongoing cross-site scripting attacks, while threat actors continue to exploit TrueConf video conferencing software vulnerabilities and deploy persistent malware like Firestarter on Cisco firewall devices.

## Active Exploitation Details

### LMDeploy Vulnerability
- **Description**: High-severity security flaw in LMDeploy open-source toolkit for compressing, deploying, and serving large language models
- **Impact**: Allows attackers to compromise systems running LMDeploy infrastructure
- **Status**: Actively exploited within 13 hours of disclosure
- **CVE ID**: CVE-2026-33626

### SimpleHelp Vulnerability
- **Description**: Security flaw in SimpleHelp remote access software
- **Impact**: Enables unauthorized access and control of affected systems
- **Status**: Added to CISA KEV catalog, actively exploited with federal deadline set for May 2026

### Samsung MagicINFO 9 Server Vulnerability
- **Description**: Security vulnerability in Samsung's digital signage management platform
- **Impact**: Allows attackers to compromise digital signage infrastructure
- **Status**: Added to CISA KEV catalog, actively exploited

### D-Link DIR-823X Router Vulnerabilities
- **Description**: Security flaws affecting D-Link DIR-823X series routers
- **Impact**: Enables network compromise and lateral movement
- **Status**: Added to CISA KEV catalog, actively exploited

### TrueConf Video Conferencing Vulnerabilities
- **Description**: Multiple security flaws in TrueConf video conferencing software
- **Impact**: Allows unauthorized access to video conferencing infrastructure and potential data theft
- **Status**: Actively exploited by PhantomCore group targeting Russian networks since September 2025

### Zimbra Cross-Site Scripting Vulnerability
- **Description**: Cross-site scripting (XSS) security flaw in Zimbra Collaboration Suite
- **Impact**: Enables script injection and potential credential theft
- **Status**: Ongoing attacks against over 10,000 exposed instances

### PackageKit Pack2TheRoot Vulnerability
- **Description**: Privilege escalation vulnerability in PackageKit daemon affecting Linux systems
- **Impact**: Allows local users to gain root permissions and install/remove system packages
- **Status**: Newly discovered vulnerability that could be exploited for privilege escalation

## Affected Systems and Products

- **LMDeploy**: Open-source toolkit for large language model deployment and serving
- **SimpleHelp**: Remote access and support software
- **Samsung MagicINFO 9 Server**: Digital signage management platform
- **D-Link DIR-823X Series**: Consumer and small business routers
- **TrueConf**: Video conferencing software primarily used in Russian networks
- **Zimbra Collaboration Suite**: Email and collaboration platform with over 10,000 vulnerable instances
- **Cisco Firepower/ASA**: Adaptive Security Appliance devices running firewall software
- **PackageKit**: Linux package management daemon
- **Microsoft Visual Studio Code**: Development environment extensions on Open VSX repository
- **Apple App Store**: iOS applications impersonating cryptocurrency wallets

## Attack Vectors and Techniques

- **Rapid Exploitation**: Attackers are exploiting disclosed vulnerabilities within hours of publication, as seen with the LMDeploy flaw
- **Supply Chain Attacks**: 73 fake VS Code extensions delivering GlassWorm v2 malware through Open VSX repository
- **Social Engineering**: Microsoft Teams used to deploy Snow malware suite including browser extensions and backdoors
- **Persistent Malware**: Firestarter malware surviving Cisco firewall updates and security patches
- **Mobile App Impersonation**: 26 fake cryptocurrency wallet apps on Apple App Store targeting seed phrases
- **Trojanized Software**: SumatraPDF reader compromised to deploy AdaptixC2 beacon malware
- **ClickFix Campaigns**: Lazarus group targeting macOS users through fake error message schemes
- **Fake CAPTCHA Schemes**: International Revenue Share Fraud (IRSF) campaigns using fake verification prompts

## Threat Actor Activities

- **PhantomCore**: Pro-Ukrainian hacktivist group actively exploiting TrueConf vulnerabilities to target Russian networks since September 2025
- **UNC6692**: Threat group using Microsoft Teams for social engineering attacks to deploy Snow malware suite
- **Tropic Trooper**: Chinese APT group using trojanized SumatraPDF and GitHub to deploy AdaptixC2 post-exploitation tools
- **Lazarus Group**: North Korean APT continuing ClickFix campaigns against macOS users and high-value organizational targets
- **BlackFile**: New financially motivated extortion group targeting retail and hospitality organizations since February 2026
- **ShinyHunters**: Extortion group threatening data leaks against companies like ADT after successful breaches
- **Chinese State Actors**: Conducting spear-phishing campaigns against NASA employees and U.S. defense software companies