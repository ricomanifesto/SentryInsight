# Exploitation Report

Critical exploitation activity is currently targeting a diverse range of systems with several high-impact vulnerabilities being actively exploited. The most concerning developments include rapid exploitation of a newly disclosed LMDeploy vulnerability within 13 hours of public disclosure, ongoing attacks against over 10,000 vulnerable Zimbra servers, and persistent malware surviving security patches on Cisco firewall devices. Additionally, CISA has added four exploited vulnerabilities to its Known Exploited Vulnerabilities catalog, indicating active in-the-wild exploitation targeting SimpleHelp, Samsung MagicINFO 9 Server, and D-Link router systems.

## Active Exploitation Details

### LMDeploy Security Flaw
- **Description**: High-severity security vulnerability in LMDeploy, an open-source toolkit for compressing, deploying, and serving large language models (LLMs)
- **Impact**: Allows attackers to compromise systems running vulnerable LMDeploy instances
- **Status**: Actively exploited within 13 hours of public disclosure
- **CVE ID**: CVE-2026-33626

### Zimbra Collaboration Suite XSS Vulnerability
- **Description**: Cross-site scripting (XSS) security flaw affecting Zimbra Collaboration Suite (ZCS) instances
- **Impact**: Enables attackers to execute malicious scripts in users' browsers and potentially compromise email systems
- **Status**: Over 10,000 Zimbra servers currently vulnerable to ongoing attacks

### TrueConf Video Conferencing Vulnerabilities
- **Description**: Security vulnerabilities in TrueConf video conferencing software affecting Russian networks
- **Impact**: Allows unauthorized access and compromise of video conferencing infrastructure
- **Status**: Actively exploited by PhantomCore hacktivist group since September 2025

### Pack2TheRoot Vulnerability
- **Description**: Vulnerability in the PackageKit daemon affecting Linux systems
- **Impact**: Allows local Linux users to install or remove system packages and gain root permissions
- **Status**: Newly disclosed vulnerability with root privilege escalation capabilities

### CISA KEV Catalog Additions
- **Description**: Four vulnerabilities added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: Various impacts depending on specific vulnerability, affecting remote access and system compromise
- **Status**: Active exploitation confirmed, federal deadline set for May 2026
- **Affected Products**: SimpleHelp, Samsung MagicINFO 9 Server, D-Link DIR-823X series routers

## Affected Systems and Products

- **Zimbra Collaboration Suite (ZCS)**: Over 10,000 instances exposed online vulnerable to XSS attacks
- **LMDeploy Toolkit**: Open-source large language model deployment systems
- **TrueConf Video Conferencing**: Servers in Russian networks
- **Linux Systems**: PackageKit daemon installations vulnerable to Pack2TheRoot
- **Cisco Firepower and Secure Firewall**: Devices running Adaptive Security Appliance (ASA) software
- **SimpleHelp**: Remote access software systems
- **Samsung MagicINFO 9 Server**: Digital signage server platforms
- **D-Link DIR-823X Series**: Router hardware models
- **Microsoft Visual Studio Code**: Extensions on Open VSX repository
- **Apple App Store**: 26 malicious cryptocurrency wallet applications
- **Microsoft Teams**: Used as attack vector for malware deployment

## Attack Vectors and Techniques

- **Social Engineering via Microsoft Teams**: UNC6692 threat group deploys custom "Snow" malware suite through Teams platform
- **Fake VS Code Extensions**: 73 malicious extensions on Open VSX repository delivering GlassWorm v2 information-stealing malware
- **Fake CAPTCHA Schemes**: International Revenue Share Fraud (IRSF) campaigns using fake verification to trick users into premium SMS charges
- **Trojanized Software**: SumatraPDF reader compromised to deploy AdaptixC2 Beacon post-exploitation agent
- **ClickFix Technique**: Lazarus group targeting macOS users with deceptive fix prompts
- **Persistent Malware**: Firestarter malware surviving Cisco firewall updates and security patches
- **Spear-Phishing Campaigns**: Chinese nationals targeting NASA employees and U.S. defense software
- **Fake Cryptocurrency Wallets**: Malicious apps targeting crypto seed phrases and private keys

## Threat Actor Activities

- **PhantomCore**: Pro-Ukrainian hacktivist group actively targeting TrueConf servers in Russia since September 2025
- **UNC6692**: Threat group using Microsoft Teams for social engineering to deploy Snow malware suite including browser extensions, tunnelers, and backdoors
- **Lazarus Group**: North Korean APT continuing ClickFix campaigns against macOS users in Mac-centric organizations
- **Tropic Trooper**: Chinese-speaking threat actors using trojanized SumatraPDF to target Chinese-speaking individuals with AdaptixC2 deployment
- **BlackFile Extortion Group**: New financially motivated group targeting retail and hospitality organizations since February 2026 with data theft and extortion attacks
- **ShinyHunters**: Extortion group threatening to leak stolen ADT data unless ransom demands are met
- **Chinese Nation-State Actors**: Conducting spear-phishing campaigns against NASA employees targeting U.S. defense software access
- **GlassWorm Campaign Operators**: Persistent information-stealing campaign distributing malware through fake VS Code extensions
- **FakeWallet Operators**: Cybercriminals distributing 26 malicious cryptocurrency wallet apps on Apple App Store