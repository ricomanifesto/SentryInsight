# Exploitation Report

Recent cybersecurity incidents reveal a concerning pattern of active exploitation across multiple attack vectors, with threat actors leveraging malicious packages, browser extensions, and compromised applications to target organizations and individuals. The most critical activity includes the Tomiris APT group's sophisticated espionage campaigns against government entities, the ShadyPanda operation affecting over 4.3 million users through malicious browser extensions, and the ongoing Glassworm malware campaign targeting Visual Studio Code packages. Additionally, supply chain attacks continue to proliferate with North Korean actors flooding npm repositories with malicious packages, while ransomware groups like Inc maintain pressure on critical infrastructure through targeted attacks on emergency services platforms.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: Cross-site scripting vulnerability in OpenPLC ScadaBR industrial control system software
- **Impact**: Allows attackers to execute malicious scripts in users' browsers, potentially leading to credential theft and session hijacking
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2021-26829

### ShadyPanda Browser Extension Campaign
- **Description**: Long-running malware operation using seemingly legitimate Chrome and Edge browser extensions that evolved into spyware
- **Impact**: Data theft, credential harvesting, and surveillance of over 4.3 million users across a seven-year campaign
- **Status**: Active exploitation with five extensions starting as legitimate tools before being weaponized

### Glassworm Malware Campaign
- **Description**: Third wave of malicious Visual Studio Code packages on OpenVSX and Microsoft Visual Studio marketplaces
- **Impact**: Code injection and potential system compromise for developers using infected extensions
- **Status**: Active with 24 new malicious packages deployed in latest wave

### SmartTube Application Compromise
- **Description**: Popular open-source YouTube client for Android TV compromised through stolen developer signing keys
- **Impact**: Malicious updates pushed to users, potentially compromising Android TV devices
- **Status**: Supply chain attack successfully executed, malicious update distributed

### Shai-hulud 2.0 npm Worm
- **Description**: Self-replicating npm package poisoning worm targeting cloud environments
- **Impact**: Credential and secret theft from AWS, Google Cloud Platform, and Azure environments
- **Status**: Active variant threatening cloud ecosystem security

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control system software vulnerable to XSS attacks
- **Chrome and Edge Browser Extensions**: Over 4.3 million installations affected by ShadyPanda campaign
- **Visual Studio Code Marketplace**: 24 malicious packages in latest Glassworm wave
- **SmartTube for Android TV**: Popular YouTube client compromised via stolen signing keys
- **npm Package Registry**: 197 malicious packages deployed by North Korean actors
- **CodeRED Emergency Alert Platform**: Critical infrastructure targeted by Inc ransomware
- **Coupang Retail Platform**: 33.7 million customer records compromised
- **Asahi Group Holdings**: 1.9 million individuals affected in September cyberattack

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages injected into npm registry and Visual Studio Code marketplaces
- **Browser Extension Abuse**: Legitimate extensions weaponized for data theft and surveillance
- **Code Signing Compromise**: Developer signing keys stolen to distribute malicious updates
- **Cross-Site Scripting**: Industrial control systems targeted for credential harvesting
- **Self-Replicating Worms**: Automated propagation through package dependencies
- **Evil Twin WiFi Networks**: In-flight network attacks targeting travelers at airports
- **Ransomware Deployment**: Critical infrastructure platforms shut down through encryption attacks

## Threat Actor Activities

- **Tomiris APT Group**: Russian-speaking actors targeting government and diplomatic entities in CIS states and Central Asia using new "Havoc" tools and public service implants for stealthier command and control
- **ShadyPanda**: Seven-year browser extension campaign amassing millions of installations for data theft operations
- **North Korean Actors**: Contagious Interview campaign deploying 197 npm packages with updated OtterCookie malware
- **Inc Ransomware Gang**: Responsible for CodeRED emergency platform attack, claiming theft of sensitive subscriber data
- **Bloody Wolf**: Java-based NetSupport RAT attacks expanded to target Kyrgyzstan and Uzbekistan
- **Glassworm Campaign Operators**: Third wave of Visual Studio Code marketplace poisoning with 24 new malicious packages