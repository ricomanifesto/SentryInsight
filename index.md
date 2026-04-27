# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms with particular focus on infrastructure devices and enterprise software. The most severe threats include the FIRESTARTER malware persisting on Cisco Firepower and ASA devices despite security patches, ongoing exploitation of a cross-site scripting vulnerability affecting over 10,000 Zimbra servers, and rapid exploitation of a newly disclosed LMDeploy vulnerability (CVE-2026-33626) within 13 hours of public disclosure. Additional concerns include active exploitation of WordPress plugin vulnerabilities, supply chain attacks targeting npm packages, and sophisticated social engineering campaigns by state-sponsored groups deploying custom malware suites.

## Active Exploitation Details

### FIRESTARTER Malware on Cisco Devices
- **Description**: Custom malware persisting on Cisco Firepower and Secure Firewall devices running Adaptive Security Appliance (ASA) software
- **Impact**: Backdoor access that survives firewall updates and security patches, affecting federal civilian agency devices
- **Status**: Active in the wild, persists despite patching efforts

### Zimbra Cross-Site Scripting Vulnerability
- **Description**: Cross-site scripting (XSS) security flaw in Zimbra Collaboration Suite (ZCS)
- **Impact**: Ongoing attacks targeting over 10,000 exposed Zimbra instances worldwide
- **Status**: Currently under active exploitation

### LMDeploy Security Flaw
- **Description**: High-severity vulnerability in LMDeploy, an open-source toolkit for compressing, deploying, and serving LLMs
- **Impact**: Enables malicious exploitation of large language model deployment infrastructure
- **Status**: Exploited within 13 hours of public disclosure
- **CVE ID**: CVE-2026-33626

### WordPress Breeze Cache Plugin Vulnerability
- **Description**: Critical file upload vulnerability in the Breeze Cache WordPress plugin
- **Impact**: Allows uploading arbitrary files on the server without authentication
- **Status**: Under active exploitation by hackers

### Pack2TheRoot Linux Vulnerability
- **Description**: Vulnerability in the PackageKit daemon affecting Linux systems
- **Impact**: Allows local users to install or remove system packages and gain root permissions
- **Status**: Newly disclosed vulnerability with root escalation potential

### SimpleHelp, Samsung MagicINFO, and D-Link Router Vulnerabilities
- **Description**: Four vulnerabilities added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: Active exploitation affecting SimpleHelp, Samsung MagicINFO 9 Server, and D-Link DIR-823X series routers
- **Status**: Under active exploitation, federal agencies must patch by May 2026

## Affected Systems and Products

- **Cisco Firepower and Secure Firewall devices**: Running Adaptive Security Appliance (ASA) software, including federal civilian agency infrastructure
- **Zimbra Collaboration Suite**: Over 10,000 instances exposed online vulnerable to XSS attacks
- **LMDeploy toolkit**: Open-source LLM deployment and serving infrastructure
- **WordPress sites**: Running vulnerable Breeze Cache plugin versions
- **Linux systems**: Using PackageKit daemon for package management
- **SimpleHelp remote access software**: Affected versions under active exploitation
- **Samsung MagicINFO 9 Server**: Digital signage management platform
- **D-Link DIR-823X series routers**: Consumer networking devices
- **Home routers**: Targeted by Tropic Trooper APT for infrastructure compromise
- **Bitwarden CLI npm package**: Briefly compromised affecting developer environments

## Attack Vectors and Techniques

- **Persistent backdoor deployment**: FIRESTARTER malware surviving security updates and patches
- **Cross-site scripting exploitation**: Large-scale attacks against Zimbra servers
- **Rapid zero-day exploitation**: CVE-2026-33626 exploited within 13 hours of disclosure
- **Unauthenticated file upload**: Arbitrary file upload attacks against WordPress plugins
- **Social engineering via Microsoft Teams**: Deployment of custom Snow malware suite
- **Supply chain compromise**: Malicious npm package injection targeting Bitwarden CLI
- **Trojanized legitimate software**: SumatraPDF reader weaponized for AdaptixC2 deployment
- **ClickFix technique**: North Korean Lazarus group targeting macOS users
- **Vishing attacks**: Voice-based social engineering for data theft and extortion
- **Custom exfiltration tools**: Command-line data stealing in ransomware operations

## Threat Actor Activities

- **UNC6692**: Deploying Snow malware suite through Microsoft Teams social engineering campaigns targeting enterprise environments
- **FIRESTARTER operators**: Maintaining persistence on federal Cisco infrastructure despite patching efforts
- **Tropic Trooper APT**: Chinese state-sponsored group targeting home routers and Japanese organizations using trojanized software and GitHub repositories
- **Lazarus Group**: North Korean APT leveraging ClickFix techniques against macOS users and high-value organizational leaders
- **BlackFile extortion group**: New financially motivated group targeting retail and hospitality organizations since February 2026 using vishing attacks
- **ShinyHunters**: Extortion group threatening ADT with data leak unless ransom demands are met
- **Chinese APT groups**: Multiple campaigns including NASA employee targeting through spear-phishing and MongoDB espionage operations using cloud tools
- **Trigona ransomware operators**: Deploying custom command-line exfiltration tools for faster data theft
- **FakeWallet developers**: Distributing 26 malicious cryptocurrency wallet apps through Apple App Store targeting seed phrases and private keys