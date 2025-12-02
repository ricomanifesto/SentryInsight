# Exploitation Report

Current cybersecurity threats are dominated by sophisticated supply chain attacks, malware distribution through legitimate software channels, and targeted espionage campaigns. The most critical activity includes the Glassworm malware campaign's third wave targeting Visual Studio Code extensions, the ShadyPanda operation that has compromised browser extensions with over 4.3 million installations, and the evolution of the Shai-hulud npm-package poisoning worm. Additionally, the Tomiris threat group has escalated attacks against government entities using advanced stealth techniques, while North Korean actors continue flooding npm repositories with malicious packages. CISA has added CVE-2021-26829 to its Known Exploited Vulnerabilities catalog, indicating active exploitation of an XSS vulnerability in OpenPLC ScadaBR systems.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: Cross-site scripting vulnerability in OpenPLC ScadaBR systems allowing attackers to inject malicious scripts
- **Impact**: Potential for session hijacking, data theft, and unauthorized access to industrial control systems
- **Status**: Actively exploited in the wild, added to CISA KEV catalog
- **CVE ID**: CVE-2021-26829

### Glassworm Malware Campaign
- **Description**: Third wave of malicious Visual Studio Code extension packages distributed through OpenVSX and Microsoft Visual Studio marketplaces
- **Impact**: Code execution on developer systems, potential access to development environments and source code
- **Status**: Currently active with 24 new packages identified in latest wave

### Shai-hulud 2.0 NPM Worm
- **Description**: Self-replicating npm-package poisoning worm that has evolved to target cloud credentials
- **Impact**: Theft of AWS, Google Cloud Platform, and Azure credentials and secrets from compromised systems
- **Status**: Actively spreading through npm package ecosystem

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control system software vulnerable to XSS attacks
- **Visual Studio Code Extensions**: Developer tools compromised through malicious packages on official marketplaces
- **NPM Package Registry**: JavaScript package repository targeted by self-replicating worms
- **Chrome and Edge Browser Extensions**: Over 4.3 million installations affected by ShadyPanda campaign
- **SmartTube Android TV App**: Open-source YouTube client compromised through signing key theft
- **CodeRED Emergency Alert Platform**: Emergency notification system breached by Inc ransomware gang
- **Coupang Retail Platform**: 33.7 million customer records exposed in data breach
- **Asahi Group Holdings**: 1.9 million individuals affected by September cyberattack

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious packages distributed through legitimate software repositories including npm, Visual Studio Code marketplaces
- **Browser Extension Hijacking**: Legitimate extensions converted to malware after gaining significant user bases
- **Signing Key Theft**: Compromise of developer signing certificates to push malicious updates
- **Cross-Site Scripting**: Exploitation of XSS vulnerabilities in industrial control systems
- **Evil Twin WiFi Networks**: Rogue wireless networks deployed in airports to steal traveler data
- **Ransomware Operations**: Data encryption and exfiltration attacks against critical infrastructure
- **Social Engineering**: Impersonation of IT professionals using deepfakes and stolen identities

## Threat Actor Activities

- **Tomiris Group**: Russian-speaking APT targeting government and diplomatic entities in CIS member states and Central Asia using public-service implants for stealthier command and control
- **ShadyPanda**: Seven-year browser extension campaign operator with over 4.3 million installations across compromised extensions
- **North Korean Actors**: Contagious Interview campaign operators deploying 197 malicious npm packages containing updated OtterCookie malware
- **Inc Ransomware Gang**: Responsible for CodeRED emergency platform attack and data theft
- **Bloody Wolf**: Java-based NetSupport RAT distribution targeting Kyrgyzstan and Uzbekistan since June 2025
- **Australian Airport Attacker**: Individual sentenced to seven years for operating evil twin WiFi networks across multiple airports