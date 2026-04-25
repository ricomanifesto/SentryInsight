# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems worldwide. CISA has added four new vulnerabilities to the Known Exploited Vulnerabilities (KEV) catalog affecting SimpleHelp, Samsung MagicINFO 9 Server, and D-Link routers, indicating active exploitation in the wild. Meanwhile, attackers have rapidly exploited CVE-2026-33626 in LMDeploy within just 13 hours of public disclosure, demonstrating the increasing speed of exploit weaponization. A persistent FIRESTARTER malware campaign has compromised Cisco Firepower devices at federal agencies, surviving security patches and updates. Additionally, over 10,000 Zimbra servers remain vulnerable to ongoing cross-site scripting attacks, while hackers are actively exploiting a critical file upload vulnerability in the Breeze Cache WordPress plugin.

## Active Exploitation Details

### CISA KEV Vulnerabilities
- **Description**: Four vulnerabilities across SimpleHelp, Samsung MagicINFO 9 Server, and D-Link DIR-823X series routers
- **Impact**: Various security impacts across remote support software, digital signage systems, and network routers
- **Status**: Added to CISA KEV catalog with May 2026 federal deadline for patching

### LMDeploy Toolkit Vulnerability
- **Description**: High-severity security flaw in LMDeploy open-source toolkit for compressing, deploying, and serving large language models
- **Impact**: Complete system compromise and unauthorized access to AI model infrastructure
- **Status**: Actively exploited within 13 hours of public disclosure
- **CVE ID**: CVE-2026-33626

### FIRESTARTER Backdoor
- **Description**: Custom malware persisting on Cisco Firepower and Secure Firewall devices running Adaptive Security Appliance (ASA) software
- **Impact**: Persistent backdoor access that survives firmware updates and security patches
- **Status**: Active exploitation targeting federal civilian agencies

### Zimbra Cross-Site Scripting Vulnerability
- **Description**: Cross-site scripting (XSS) security flaw in Zimbra Collaboration Suite
- **Impact**: Web-based attacks against email and collaboration systems
- **Status**: Ongoing exploitation affecting over 10,000 exposed servers

### Breeze Cache WordPress Plugin Vulnerability
- **Description**: Critical file upload vulnerability allowing arbitrary file uploads without authentication
- **Impact**: Complete website compromise and server control
- **Status**: Active exploitation in the wild

### PackageKit Daemon Vulnerability (Pack2TheRoot)
- **Description**: Vulnerability in PackageKit daemon allowing local privilege escalation
- **Impact**: Local Linux users can install/remove system packages and gain root permissions
- **Status**: Newly disclosed vulnerability

## Affected Systems and Products

- **Cisco Firepower and Secure Firewall**: Devices running Adaptive Security Appliance (ASA) software
- **SimpleHelp**: Remote support software platform
- **Samsung MagicINFO 9 Server**: Digital signage management system
- **D-Link DIR-823X Series**: Router hardware and firmware
- **LMDeploy**: Open-source toolkit for large language model deployment
- **Zimbra Collaboration Suite**: Email and collaboration platform with over 10,000 exposed instances
- **Breeze Cache WordPress Plugin**: WordPress caching plugin
- **PackageKit Daemon**: Linux package management system
- **Bitwarden CLI npm Package**: Command-line interface for password manager
- **Checkmarx KICS**: Code analysis tool Docker images and extensions

## Attack Vectors and Techniques

- **Social Engineering via Microsoft Teams**: UNC6692 threat group impersonating IT help desk to deploy SNOW malware
- **Trojanized Software Distribution**: Tropic Trooper using compromised SumatraPDF and GitHub for AdaptixC2 deployment
- **Supply Chain Compromise**: Bitwarden CLI npm package and Checkmarx KICS tool compromised to steal developer credentials
- **ClickFix Technique**: North Korea's Lazarus group targeting macOS users
- **Spear-Phishing**: Chinese nationals posing as U.S. researchers to target NASA employees
- **AI-Powered Phishing**: Significant increase in personalized AI-generated phishing attacks
- **Vishing Attacks**: BlackFile extortion group using voice phishing against retail and hospitality
- **Persistent Backdoor**: FIRESTARTER malware surviving security updates on network infrastructure

## Threat Actor Activities

- **UNC6692**: Previously undocumented group using Microsoft Teams social engineering to deploy custom SNOW malware suite
- **Tropic Trooper**: Chinese APT group targeting home routers and Japanese organizations with trojanized applications
- **Lazarus Group**: North Korean APT leveraging ClickFix techniques against macOS users and high-value targets
- **Chinese State-Sponsored Groups**: Multiple campaigns including espionage against Mongolia using cloud tools and spear-phishing against NASA
- **BlackFile Extortion Group**: New financially motivated group targeting retail and hospitality since February 2026
- **ShinyHunters**: Threatening ADT with data leak unless ransom is paid
- **Trigona Ransomware Operators**: Using custom exfiltration tools for faster data theft
- **Chinese-Backed Botnet Operations**: Industrializing compromised device networks for low-risk attacks