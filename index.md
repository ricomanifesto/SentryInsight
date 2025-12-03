# Exploitation Report

Critical exploitation activity is currently dominated by two zero-day Android vulnerabilities being actively exploited in targeted attacks, alongside a sophisticated supply chain campaign targeting developers through malicious packages. The Android framework vulnerabilities pose significant risks to mobile device security, while threat actors continue to leverage supply chain attacks through malicious npm packages, PyTorch models, and Visual Studio extensions. Notable activities include North Korean state-sponsored groups conducting identity theft schemes for IT workers, Iranian threat actors deploying new backdoors against Israeli entities, and ransomware attacks disrupting critical emergency alert systems.

## Active Exploitation Details

### Android Framework Zero-Day Vulnerabilities
- **Description**: Two critical vulnerabilities in the Android framework that allow attackers to compromise targeted devices
- **Impact**: Successful exploitation enables attackers to gain unauthorized access to Android devices in targeted attacks
- **Status**: Actively exploited in the wild; patches released in December 2025 Android security bulletin

### Picklescan Security Flaws
- **Description**: Three critical security vulnerabilities in the open-source Picklescan utility used for scanning PyTorch models
- **Impact**: Malicious actors can execute arbitrary code by loading untrusted PyTorch models, effectively bypassing security scans
- **Status**: Vulnerabilities disclosed; allows malicious PyTorch models to evade detection and execute malicious code

## Affected Systems and Products

- **Android Devices**: All Android systems affected by framework vulnerabilities; patches available in December 2025 security bulletin covering 107 total vulnerabilities
- **PyTorch Models**: Machine learning models using Picklescan utility for security scanning
- **IP Cameras**: Over 120,000 IP cameras in Korea compromised for unauthorized surveillance footage theft
- **NPM Package Registry**: Multiple malicious packages including Shai-Hulud 2.0 attack exposing 400,000+ developer secrets
- **Visual Studio Marketplace**: 24 malicious extensions impersonating popular developer tools in GlassWorm campaign
- **Oracle E-Business Suite**: University of Pennsylvania systems compromised with personal data theft
- **CodeRED Emergency Platform**: Critical emergency alert system shut down following ransomware attack

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages in npm registry, PyTorch models, and Visual Studio extensions targeting developers
- **Social Engineering**: Fake Calendly invites impersonating major brands to steal Google Workspace and Facebook credentials
- **Identity Theft Schemes**: North Korean actors recruiting legitimate developers to rent their identities for illicit operations
- **Phishing Campaigns**: Multi-brand impersonation attacks targeting advertising account managers
- **AI Evasion Techniques**: Hidden prompts and scripts designed to fool AI-powered security scanning tools
- **Camera Network Exploitation**: Mass compromise of IP camera systems for unauthorized surveillance and content theft

## Threat Actor Activities

- **North Korean State Actors**: Conducting sophisticated "fake IT worker" schemes, recruiting legitimate engineers to rent identities for fundraising operations; deploying 197+ malicious npm packages with 31,000+ downloads since October
- **Iranian MuddyWater Group**: Evolved tactics with new MuddyViper backdoor and Fooder loader, targeting Israeli academia, engineering, government, manufacturing, technology, transportation, and utilities sectors
- **GlassWorm Campaign**: Return of supply chain threat with 24 malicious Visual Studio extensions impersonating legitimate developer tools
- **Russian Tomiris Group**: Targeting government and diplomatic entities in CIS member states and Central Asia using new "Havoc" tools and tactics
- **Inc Ransomware Gang**: Successfully attacked CodeRED emergency alert platform, claiming theft of sensitive subscriber data and forcing system shutdown