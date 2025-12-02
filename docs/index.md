# Exploitation Report

Recent security activity reveals several critical exploitation trends, with Google addressing two actively exploited Android framework vulnerabilities among 107 total security flaws. Threat actors continue to leverage malicious browser extensions, NPM package poisoning campaigns, and supply chain attacks to compromise systems. The CISA has added CVE-2021-26829, an actively exploited cross-site scripting vulnerability in OpenPLC ScadaBR, to their Known Exploited Vulnerabilities catalog. Additionally, sophisticated campaigns like ShadyPanda have successfully compromised over 4.3 million browser extension installations, while North Korean actors persist with NPM-based malware distribution through the OtterCookie campaign.

## Active Exploitation Details

### Android Framework Vulnerabilities
- **Description**: Two critical vulnerabilities in the Android framework that were being actively exploited in the wild
- **Impact**: Attackers could potentially gain unauthorized access to Android devices and compromise system security
- **Status**: Patched by Google in their December 2024 monthly security update alongside 105 other vulnerabilities

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: Cross-site scripting (XSS) vulnerability in OpenPLC ScadaBR industrial control system software
- **Impact**: Allows attackers to execute malicious scripts in users' browsers, potentially leading to session hijacking, data theft, or system manipulation
- **Status**: Actively exploited in the wild and added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2021-26829

### SmartTube Application Compromise
- **Description**: Supply chain attack targeting the popular open-source SmartTube YouTube client for Android TV
- **Impact**: Malicious update pushed to users after attackers gained access to developer signing keys, potentially compromising user devices
- **Status**: Developer signing keys compromised, malicious updates distributed

## Affected Systems and Products

- **Android Devices**: All Android systems vulnerable to the two framework bugs until December 2024 security update applied
- **OpenPLC ScadaBR**: Industrial control system software affected by XSS vulnerability
- **SmartTube for Android TV**: Popular YouTube client compromised through signing key theft
- **Chrome and Edge Browser Extensions**: Over 4.3 million installations affected by ShadyPanda campaign
- **NPM Registry**: 197 malicious packages deployed by North Korean actors in OtterCookie campaign
- **Visual Studio Code Extensions**: OpenVSX and Microsoft Visual Studio marketplaces targeted by Glassworm malware
- **Microsoft Teams**: Guest access feature creates bypass opportunities for Defender for Office 365
- **PyPI Python Packages**: Legacy bootstrap scripts create domain takeover risks

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Attackers gaining access to developer signing keys and certificate infrastructure to distribute malicious updates
- **Browser Extension Poisoning**: Long-term campaigns converting legitimate extensions into spyware through updates
- **NPM Package Flooding**: Mass deployment of malicious packages to overwhelm detection systems
- **Cross-Tenant Access Bypass**: Exploitation of Microsoft Teams guest access to bypass security controls
- **Domain Takeover**: Leveraging abandoned domains in legacy Python packages for supply chain attacks
- **Malware-as-a-Service**: Albiriox Android malware offering comprehensive fraud capabilities
- **Evil Twin WiFi Networks**: Creating rogue access points to steal traveler data at airports

## Threat Actor Activities

- **ShadyPanda**: Seven-year browser extension campaign amassing 4.3 million installations, converting legitimate extensions into spyware
- **North Korean Actors**: Continued OtterCookie campaign with 197 new malicious NPM packages targeting developers
- **Tomiris Group**: Russian-speaking APT targeting government and diplomatic entities in CIS states using public service implants for stealth
- **Bloody Wolf**: Java-based NetSupport RAT attacks expanding into Kyrgyzstan and Uzbekistan since June 2025
- **Glassworm Operators**: Third wave of malicious VS Code packages on OpenVSX and Microsoft marketplaces
- **Inc Ransomware Gang**: Responsible for CodeRED emergency alert platform attack and data theft claims