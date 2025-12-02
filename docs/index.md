# Exploitation Report

The cybersecurity landscape is witnessing an escalation in sophisticated attack campaigns with threat actors employing diverse vectors ranging from supply chain compromises to browser extension malware. The most critical activity includes the Tomiris group's advanced espionage operations against government entities, the continued spread of Glassworm malware through legitimate development platforms, and the massive ShadyPanda browser extension campaign affecting over 4.3 million users. Additionally, ransomware groups like Inc continue to target critical infrastructure, while North Korean actors persist in flooding package repositories with malicious code. A particularly concerning development is the active exploitation of an XSS vulnerability in OpenPLC ScadaBR systems, now officially tracked by CISA as a known exploited vulnerability.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: A cross-site scripting (XSS) vulnerability in OpenPLC ScadaBR that allows attackers to execute malicious scripts in users' browsers
- **Impact**: Attackers can steal credentials, session tokens, and perform unauthorized actions within the application context
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities (KEV) catalog
- **CVE ID**: CVE-2021-26829

### Tomiris Advanced Persistent Threat Campaign
- **Description**: Russian-speaking threat group conducting sophisticated cyber-espionage operations using public service implants for stealthier command and control
- **Impact**: Establishment of persistent remote access to foreign ministries, intergovernmental organizations, and government entities
- **Status**: Ongoing active campaign with evolved tactics and new tools including "Havoc" framework

### Glassworm Malware Supply Chain Attack
- **Description**: Third wave of malicious Visual Studio Code packages distributed through OpenVSX and Microsoft Visual Studio marketplaces
- **Impact**: Code execution on developer systems, potential theft of source code and development credentials
- **Status**: Active campaign with 24 new malicious packages identified in latest wave

### ShadyPanda Browser Extension Compromise
- **Description**: Seven-year-long campaign converting legitimate browser extensions into spyware through malicious updates
- **Impact**: Data theft, credential harvesting, and surveillance capabilities affecting over 4.3 million installations
- **Status**: Active long-term campaign with five extensions initially legitimate before becoming malicious

### SmartTube Android TV Application Compromise
- **Description**: Popular open-source YouTube client compromised after attackers gained access to developer's code signing keys
- **Impact**: Malicious updates pushed to users, potential for remote code execution and device compromise
- **Status**: Incident resolved, but demonstrates supply chain vulnerability in mobile applications

### Shai-hulud 2.0 npm Worm
- **Description**: Self-replicating npm package poisoning worm with enhanced capabilities for cloud credential theft
- **Impact**: Credential and secret theft from AWS, Google Cloud Platform, and Azure environments
- **Status**: Active variant threatening cloud ecosystems with improved evasion techniques

### North Korean OtterCookie Malware Distribution
- **Description**: Deployment of 197 malicious npm packages as part of the Contagious Interview campaign
- **Impact**: Supply chain compromise targeting developers with updated malware payloads
- **Status**: Ongoing campaign with continued flooding of npm registry

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control systems with XSS vulnerability requiring immediate patching
- **Visual Studio Code Extensions**: Developers using OpenVSX and Microsoft marketplace extensions
- **Chrome and Edge Browser Extensions**: Users with ShadyPanda-compromised extensions installed
- **SmartTube for Android TV**: Users of the popular YouTube client application
- **npm Package Ecosystem**: Node.js developers and applications using compromised packages
- **Government IT Infrastructure**: Foreign ministries and diplomatic entities in CIS states and Central Asia
- **Cloud Platforms**: AWS, Google Cloud Platform, and Azure environments at risk from credential theft
- **CodeRED Emergency Alert Platform**: Critical infrastructure for emergency communications
- **Coupang Retail Platform**: 33.7 million customers affected by data breach
- **Microsoft Teams**: Organizations using guest access features vulnerable to Defender bypass
- **Asahi Group Systems**: 1.9 million individuals affected by cyberattack on Japanese beer giant

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious packages injected into legitimate software repositories and development platforms
- **Browser Extension Hijacking**: Long-term campaigns converting legitimate extensions into malware through updates
- **Code Signing Key Theft**: Compromise of developer signing certificates to push malicious application updates
- **Public Service Implants**: Use of legitimate cloud services for command and control to evade detection
- **Cross-Site Scripting**: Web application vulnerabilities exploited for credential theft and unauthorized access
- **Ransomware Operations**: Data exfiltration and encryption attacks against critical infrastructure
- **Evil Twin WiFi Networks**: Man-in-the-middle attacks on travelers in airports to steal credentials
- **Social Engineering**: Impersonation of IT professionals using deepfakes and stolen identities for insider threats
- **Domain Takeover**: Exploitation of legacy bootstrap scripts in Python packages for supply chain attacks
- **Teams Guest Access Abuse**: Bypassing Microsoft Defender protections through cross-tenant vulnerabilities

## Threat Actor Activities

- **Tomiris Group**: Russian-speaking APT conducting espionage against government entities in CIS member states and Central Asia using advanced stealth techniques and the Havoc framework
- **ShadyPanda**: Long-term actor operating seven-year browser extension campaign with over 4.3 million compromised installations
- **Inc Ransomware Gang**: Responsible for CodeRED emergency platform attack with claims of sensitive subscriber data theft
- **North Korean Actors**: Continuing Contagious Interview campaign with 197 new malicious npm packages distributing OtterCookie malware
- **Glassworm Campaign Operators**: Targeting developer ecosystems through malicious VS Code extensions in sustained third-wave attack
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks in Kyrgyzstan and Uzbekistan since June 2025
- **Cryptomixer Operators**: Cryptocurrency mixing service facilitating money laundering for cybercriminals before law enforcement takedown
- **Albiriox MaaS Providers**: Offering Android malware-as-a-service targeting 400+ applications for on-device fraud