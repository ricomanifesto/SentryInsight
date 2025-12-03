# Exploitation Report

Current cybersecurity landscape reveals significant exploitation activity across multiple platforms, with particular concern around Android zero-day vulnerabilities, massive botnet-driven DDoS attacks, and sophisticated supply chain compromises. Two Android framework vulnerabilities are being actively exploited in targeted attacks, while the Aisuru botnet has achieved record-breaking distributed denial-of-service attacks reaching 29.7 Tbps. Supply chain attacks continue to proliferate through malicious packages in npm, Rust crates, and developer tool ecosystems, with North Korean threat actors leading sophisticated campaigns targeting developers and financial institutions.

## Active Exploitation Details

### Android Framework Zero-Day Vulnerabilities
- **Description**: Two critical vulnerabilities in the Android framework are being actively exploited in targeted attacks
- **Impact**: Attackers can achieve system-level compromise on Android devices through these framework flaws
- **Status**: Patched in December 2025 Android security bulletin as part of 107 total vulnerabilities addressed

### Oracle E-Business Suite Vulnerabilities
- **Description**: Clop ransomware group targeting vulnerable Oracle E-Business Suite instances in coordinated data theft campaign
- **Impact**: Successful exploitation leads to data breaches affecting educational institutions and enterprises
- **Status**: Actively exploited by Clop group with multiple universities compromised including University of Phoenix

### Picklescan Security Flaws
- **Description**: Three critical security flaws in the open-source Picklescan utility used for scanning PyTorch models
- **Impact**: Malicious actors can execute arbitrary code by loading untrusted PyTorch models that evade security scans
- **Status**: Vulnerabilities allow complete evasion of security scanning mechanisms

## Affected Systems and Products

- **Android Devices**: Framework vulnerabilities affecting Android operating system across multiple versions
- **Oracle E-Business Suite**: Enterprise software installations targeted in Clop ransomware campaign
- **PyTorch Models**: Machine learning models processed through vulnerable Picklescan utility
- **IP Cameras**: Over 120,000 IP cameras in Korea compromised for illegal surveillance operations
- **NPM Ecosystem**: JavaScript package registry targeted with malicious packages and supply chain attacks
- **Visual Studio Marketplace**: Microsoft development environment compromised with 24 malicious extensions
- **Rust Crate Registry**: Rust package ecosystem targeted with OS-specific malware delivery

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages deployed across npm, Rust crates, and Visual Studio extensions to target developers
- **DDoS Amplification**: Aisuru botnet leveraging massive scale to achieve record-breaking 29.7 Tbps attack volumes
- **Social Engineering**: Fake Calendly invites impersonating major brands to steal Google Workspace and Facebook credentials
- **Identity Rental Schemes**: North Korean actors recruiting legitimate developers to rent their identities for illicit operations
- **Memory-Only Tactics**: Advanced persistence techniques avoiding disk-based detection mechanisms
- **AI Evasion Techniques**: Hidden prompts and scripts designed to influence AI-driven security scanners

## Threat Actor Activities

- **Clop Ransomware Group**: Conducting systematic data theft campaign targeting Oracle E-Business Suite vulnerabilities across educational sector
- **Aisuru Botnet Operators**: Launched over 1,300 DDoS attacks in three months, achieving record-breaking attack volumes
- **MuddyWater (Iranian APT)**: Deploying new MuddyViper backdoor with enhanced stealth capabilities targeting Israeli infrastructure sectors
- **North Korean IT Workers**: Operating sophisticated identity rental schemes and fake remote worker operations for financial gain
- **Lazarus APT**: Advanced persistent threat group conducting live remote worker infiltration schemes captured by security researchers
- **GlassWorm Campaign**: Supply chain attackers infiltrating developer tool marketplaces with impersonated legitimate extensions