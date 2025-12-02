# Exploitation Report

The current threat landscape is dominated by sophisticated state-sponsored campaigns and targeted exploitation activities. Google has addressed two critical Android zero-day vulnerabilities that were actively exploited in targeted attacks as part of their December 2025 security bulletin covering 107 total vulnerabilities. North Korean threat actors continue their aggressive campaign through the "Contagious Interview" operation, deploying 197 malicious npm packages to spread updated OtterCookie malware targeting developers. Iranian-linked attackers have launched targeted attacks against Israeli sectors using a new MuddyViper backdoor, while the Russian-speaking Tomiris group has enhanced their capabilities with new tools and tactics targeting government entities in CIS states. Additionally, CISA has added an actively exploited cross-site scripting vulnerability in OpenPLC ScadaBR to their Known Exploited Vulnerabilities catalog, indicating ongoing exploitation in the wild.

## Active Exploitation Details

### Android Framework Zero-Day Vulnerabilities
- **Description**: Two critical vulnerabilities in the Android Framework that allow attackers to compromise targeted devices
- **Impact**: Complete device compromise and unauthorized access to sensitive data in targeted attacks
- **Status**: Patched in December 2025 Android security bulletin, previously exploited in the wild

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: Cross-site scripting vulnerability in OpenPLC ScadaBR industrial control system software
- **Impact**: Allows attackers to execute malicious scripts and potentially gain unauthorized access to SCADA systems
- **Status**: Actively exploited in the wild, added to CISA KEV catalog
- **CVE ID**: CVE-2021-26829

### SmartTube Application Compromise
- **Description**: Popular open-source YouTube client for Android TV was compromised through stolen signing keys
- **Impact**: Malicious updates pushed to users, potential device compromise and data theft
- **Status**: Developer signing keys compromised, malicious update distributed

## Affected Systems and Products

- **Android Devices**: All Android versions affected by the two zero-day vulnerabilities, patches available in December 2025 security bulletin
- **OpenPLC ScadaBR**: Industrial control system software vulnerable to XSS attacks
- **SmartTube Android TV App**: Open-source YouTube client compromised through signing key theft
- **npm Registry**: 197 malicious packages targeting Node.js developers
- **Oracle E-Business Suite**: University of Pennsylvania breach involving document theft
- **Chrome and Edge Browser Extensions**: 4.3 million installations of malicious ShadyPanda extensions
- **Visual Studio Code Extensions**: 24 new malicious packages in third wave of Glassworm campaign

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Targeted attacks using unpatched Android vulnerabilities for device compromise
- **Supply Chain Attacks**: Malicious npm packages and browser extensions to compromise developer environments
- **Social Engineering**: Fake Calendly invites spoofing major brands to steal Google Workspace and Facebook credentials
- **Identity Theft Schemes**: North Korean recruiters targeting engineers to rent identities for IT worker fraud
- **Signing Key Compromise**: Theft of developer certificates to distribute malicious software updates
- **Backdoor Deployment**: MuddyViper backdoor targeting Israeli critical infrastructure sectors
- **Malware-as-a-Service**: Albiriox Android malware offering on-device fraud capabilities

## Threat Actor Activities

- **North Korean Groups**: Continued "Contagious Interview" campaign with 197 new malicious npm packages spreading OtterCookie malware, plus identity rental schemes targeting IT professionals
- **Iranian-Linked Attackers**: Deployment of MuddyViper backdoor against Israeli academia, engineering, government, manufacturing, technology, transportation, and utilities sectors
- **Tomiris Group**: Russian-speaking threat actor targeting government and diplomatic entities in CIS member states and Central Asia with enhanced tools including Havoc framework
- **ShadyPanda Campaign**: Seven-year browser extension operation amassing 4.3 million installations across Chrome and Edge platforms
- **Inc Ransomware Gang**: Responsible for CodeRED emergency alert platform attack with claimed data theft