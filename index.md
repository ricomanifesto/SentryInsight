# Exploitation Report

Critical exploitation activity continues to surge across multiple platforms, with Google patching two actively exploited Android Framework vulnerabilities affecting the operating system's core functionality. Simultaneously, sophisticated threat actors including Tomiris, ShadyPanda, and North Korean groups are deploying advanced malware campaigns targeting government entities, browser users, and software supply chains. The emergence of new Android malware-as-a-service platforms and continued abuse of legitimate development tools demonstrates the evolving threat landscape facing organizations worldwide.

## Active Exploitation Details

### Android Framework Vulnerabilities
- **Description**: Two critical vulnerabilities in the Android Framework that have been actively exploited in the wild
- **Impact**: Attackers can compromise Android devices through framework-level exploitation, potentially gaining elevated system access
- **Status**: Patched by Google in monthly security updates addressing 107 total Android vulnerabilities

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: Cross-site scripting (XSS) vulnerability in OpenPLC ScadaBR industrial control system
- **Impact**: Allows attackers to inject malicious scripts into the web interface, potentially compromising industrial control systems
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation
- **CVE ID**: CVE-2021-26829

## Affected Systems and Products

- **Android Operating System**: Framework components affected by two actively exploited vulnerabilities
- **OpenPLC ScadaBR**: Industrial control system vulnerable to XSS attacks
- **SmartTube YouTube App**: Android TV application compromised through signing key theft
- **Visual Studio Code Extensions**: Marketplace packages infected with Glassworm malware
- **Chrome and Edge Browsers**: Extensions compromised in ShadyPanda campaign affecting 4.3 million installations
- **npm Package Registry**: 197 malicious packages deployed by North Korean actors, plus Shai-hulud 2.0 worm variant
- **Cloud Platforms**: AWS, Google Cloud Platform, and Azure targeted by credential theft malware

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Threat actors compromising legitimate software distribution channels including browser extension marketplaces and npm registry
- **Code Signing Key Theft**: Attackers gaining access to developer signing keys to push malicious updates through legitimate channels
- **Malware-as-a-Service**: New Android malware platform Albiriox offering comprehensive fraud capabilities to cybercriminals
- **Browser Extension Hijacking**: ShadyPanda converting legitimate extensions into spyware over multi-year campaigns
- **Framework Exploitation**: Direct attacks against Android's core framework components for system-level compromise
- **Public Service Implants**: Tomiris group using legitimate public services for covert command and control communications

## Threat Actor Activities

- **Tomiris Group**: Russian-speaking threat actor targeting government and diplomatic entities in CIS member states and Central Asia using new "Havoc" tools and public service implants for stealth
- **ShadyPanda**: Long-running operation spanning seven years, compromising browser extensions with over 4.3 million total installations across Chrome and Edge marketplaces
- **North Korean Actors**: Contagious Interview campaign operators flooding npm registry with 197 malicious packages containing updated OtterCookie malware
- **Bloody Wolf**: Threat group expanding Java-based NetSupport RAT attacks in Kyrgyzstan and Uzbekistan since June 2025
- **Inc Ransomware Gang**: Claimed responsibility for attacking CodeRED emergency alert platform, stealing sensitive subscriber data