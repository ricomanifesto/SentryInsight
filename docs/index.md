# Exploitation Report

Current threat landscape shows significant active exploitation across multiple attack vectors, with threat actors leveraging compromised development environments, malicious browser extensions, and supply chain attacks to target organizations worldwide. The Tomiris APT group has evolved its tactics to use public service implants for stealthier command and control operations against government targets, while the ShadyPanda campaign has successfully compromised 4.3 million browser extension installations over seven years. Notable active exploitation includes CVE-2021-26829, a cross-site scripting vulnerability in OpenPLC ScadaBR that has been added to CISA's Known Exploited Vulnerabilities catalog. Additionally, multiple supply chain attacks are ongoing, including the third wave of Glassworm malware targeting VS Code packages, the return of the Shai-hulud 2.0 worm threatening cloud ecosystems, and North Korean threat actors deploying 197 malicious npm packages containing updated OtterCookie malware.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: A cross-site scripting (XSS) vulnerability affecting OpenPLC ScadaBR systems that allows attackers to execute malicious scripts in the context of legitimate users
- **Impact**: Attackers can steal credentials, session tokens, and perform unauthorized actions on behalf of legitimate users in industrial control systems
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities (KEV) catalog
- **CVE ID**: CVE-2021-26829

### Glassworm Malware Campaign
- **Description**: Third wave of malicious Visual Studio Code packages distributed through OpenVSX and Microsoft Visual Studio marketplaces, with 24 new packages added in the latest campaign
- **Impact**: Code execution, data theft, and potential supply chain compromise affecting developers and development environments
- **Status**: Active ongoing campaign since October, currently in third wave of attacks

### Shai-hulud 2.0 Worm
- **Description**: Self-replicating npm-package poisoning worm that has evolved to target cloud environments with enhanced credential stealing capabilities
- **Impact**: Can steal credentials and secrets from AWS, Google Cloud Platform, and Azure cloud environments while spreading across npm ecosystems
- **Status**: Active variant threatening cloud infrastructure with improved evasion techniques

### SmartTube Signing Key Compromise
- **Description**: Popular open-source YouTube client for Android TV was compromised after attackers gained access to the developer's signing keys
- **Impact**: Malicious updates pushed to legitimate users, potential for widespread device compromise and data theft
- **Status**: Compromise confirmed, malicious updates distributed to user base

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control systems and SCADA environments vulnerable to XSS attacks
- **Visual Studio Code Extensions**: OpenVSX and Microsoft Visual Studio marketplaces affected by Glassworm malware packages
- **npm Package Registry**: Cloud environments using npm packages at risk from Shai-hulud 2.0 worm propagation
- **Browser Extensions**: Chrome and Edge extensions with over 4.3 million combined installations compromised by ShadyPanda
- **SmartTube Android TV App**: Open-source YouTube client users affected by malicious update distribution
- **CodeRED Emergency Platform**: Emergency alert system shut down following ransomware attack by Inc gang
- **Coupang Retail Platform**: 33.7 million customer records exposed in data breach
- **Asahi Group Holdings**: Up to 1.9 million individuals impacted by September cyberattack

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages injected into npm registry and VS Code marketplaces to compromise developer environments
- **Browser Extension Hijacking**: Legitimate extensions converted to spyware after gaining user trust over extended periods
- **Signing Key Compromise**: Attackers gaining access to code signing certificates to distribute malicious updates through legitimate channels
- **Public Service Implants**: Advanced persistent threat groups using public services as command and control infrastructure for stealth
- **Cross-Site Scripting (XSS)**: Web application vulnerabilities exploited to execute malicious scripts in industrial control systems
- **Evil Twin WiFi Networks**: Rogue wireless access points deployed in airports to steal traveler credentials and data
- **Ransomware Operations**: Targeted attacks against critical infrastructure and emergency services platforms

## Threat Actor Activities

- **Tomiris APT Group**: Russian-speaking group targeting government and diplomatic entities in CIS member states and Central Asia using advanced public service implants for command and control
- **ShadyPanda Campaign**: Seven-year browser extension operation affecting 4.3 million installations, evolving legitimate extensions into comprehensive spyware platforms
- **North Korean Threat Actors**: Contagious Interview campaign operators deploying 197 malicious npm packages containing updated OtterCookie malware targeting developers
- **Inc Ransomware Gang**: Claimed responsibility for CodeRED emergency platform attack and theft of sensitive subscriber data
- **Bloody Wolf**: Cyber attack campaign targeting Kyrgyzstan and Uzbekistan since June 2025 using Java-based NetSupport RAT delivery
- **Glassworm Operators**: Multi-wave campaign targeting VS Code development environments with 24 new malicious packages in latest iteration