# Exploitation Report

Critical Android vulnerabilities are under active exploitation, with Google confirming two framework bugs being exploited in the wild as part of their December security update addressing 107 total flaws. Simultaneously, multiple sophisticated threat campaigns are leveraging supply chain attacks through malicious packages and browser extensions, while ransomware groups continue targeting critical infrastructure and emergency services.

## Active Exploitation Details

### Android Framework Vulnerabilities
- **Description**: Two Android framework vulnerabilities have been actively exploited in targeted attacks
- **Impact**: Attackers can achieve system-level compromise and persistent access to affected Android devices
- **Status**: Patched in Google's December 2024 Android security update
- **CVE ID**: CVE-2021-26829

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: Cross-site scripting vulnerability in OpenPLC ScadaBR industrial control system software
- **Impact**: Remote code execution and unauthorized access to industrial control systems
- **Status**: Actively exploited and added to CISA's Known Exploited Vulnerabilities catalog

## Affected Systems and Products

- **Android Operating System**: Framework vulnerabilities affecting multiple Android versions
- **OpenPLC ScadaBR**: Industrial control system software vulnerable to XSS attacks
- **Visual Studio Code Extensions**: Marketplace compromised with 4.3 million malicious installations via ShadyPanda campaign
- **npm Package Registry**: 197 malicious packages deployed by North Korean threat actors
- **SmartTube Android TV App**: Compromised through stolen developer signing keys
- **Chrome and Edge Browsers**: Browser extensions turned into spyware affecting millions of users

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious npm packages and browser extensions used to deliver malware
- **Code Signing Key Theft**: Attackers compromising developer signing keys to push malicious updates
- **Browser Extension Hijacking**: Legitimate extensions converted to spyware through malicious updates
- **Domain Takeover**: Legacy Python packages vulnerable to supply chain attacks via domain takeover
- **Cross-Tenant Bypass**: Microsoft Teams guest access feature used to bypass Defender protections
- **Evil Twin WiFi Networks**: Rogue wireless networks deployed in airports to steal traveler data

## Threat Actor Activities

- **ShadyPanda**: Seven-year campaign distributing malicious browser extensions with 4.3 million total installations
- **North Korean Hackers**: Contagious Interview campaign deploying 197 malicious npm packages with updated OtterCookie malware
- **Tomiris Group**: Russian-speaking APT targeting government and diplomatic entities in CIS states using public service implants for stealth
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks in Kyrgyzstan and Uzbekistan
- **Inc Ransomware Gang**: Responsible for CodeRED emergency alert platform compromise, claiming theft of sensitive subscriber data
- **Glassworm Campaign**: Third wave of malicious Visual Studio Code packages targeting developers