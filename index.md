# Exploitation Report

Critical exploitation activity has emerged across multiple fronts, with Google addressing two Android zero-day vulnerabilities that were actively exploited in targeted attacks as part of their December 2025 security bulletin covering 107 total flaws. North Korean threat actors continue sophisticated supply chain attacks through both the Lazarus APT's remote worker schemes and ongoing npm package poisoning campaigns, including the return of the Glassworm malware targeting developer environments. Iranian-linked hackers have deployed new backdoor capabilities against Israeli infrastructure, while the Tomiris group has evolved their tactics with public service implants for enhanced stealth in government targeting operations.

## Active Exploitation Details

### Android Framework Zero-Day Vulnerabilities
- **Description**: Two vulnerabilities in the Android framework that were being exploited in targeted attacks in the wild
- **Impact**: Attackers can exploit these flaws to compromise Android devices in targeted operations
- **Status**: Patched in Google's December 2025 Android security bulletin as part of 107 total vulnerability fixes

### SmartTube YouTube Client Compromise
- **Description**: The popular open-source SmartTube YouTube client for Android TV was compromised after attackers gained access to the developer's signing keys
- **Impact**: Malicious updates were pushed to legitimate users through the official update mechanism
- **Status**: Active compromise with malicious updates distributed to users

### University of Pennsylvania Oracle E-Business Suite Breach
- **Description**: Attackers successfully compromised Oracle E-Business Suite servers and stole documents containing personal information
- **Impact**: Data theft of personal information from university systems
- **Status**: Breach occurred in August with recent confirmation of data theft

## Affected Systems and Products

- **Android Devices**: Framework vulnerabilities affecting Android operating system across multiple versions
- **SmartTube Application**: Open-source YouTube client for Android TV platforms compromised via signing key theft
- **Oracle E-Business Suite**: Enterprise resource planning systems targeted at University of Pennsylvania
- **Visual Studio Code Extensions**: 24 malicious extensions impersonating legitimate developer tools in third wave of Glassworm campaign
- **npm Ecosystem**: Over 197 malicious packages delivered by North Korean actors since October 10
- **Browser Extensions**: ShadyPanda campaign affecting extensions with 4.3 million total installations over seven years
- **Coupang Platform**: South Korean retail platform compromised affecting 33.7 million customers

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: North Korean actors using npm packages and VS Code extensions to target developers
- **Identity Theft**: Lazarus APT recruiting legitimate developers to rent their identities for fraudulent employment
- **Signing Key Compromise**: Attackers gaining access to legitimate application signing certificates to distribute malicious updates
- **Backdoor Deployment**: Iranian groups using MuddyViper backdoor for persistent access to Israeli infrastructure
- **Phishing Campaigns**: Fake Calendly invites spoofing major brands to steal Google Workspace and Facebook business credentials
- **Browser Extension Manipulation**: Long-term campaigns turning legitimate extensions into spyware after gaining user trust
- **Public Service Implants**: Tomiris group using legitimate public services as command and control infrastructure

## Threat Actor Activities

- **Lazarus APT**: Operating sophisticated remote worker schemes to infiltrate organizations by recruiting legitimate developers and renting their identities for fraudulent employment positions
- **North Korean IT Workers**: Conducting ongoing npm package poisoning campaign with 197+ malicious packages and 31,000+ downloads targeting software developers
- **Glassworm Campaign**: Third wave of malicious VS Code extension distribution through both Microsoft Visual Studio Marketplace and Open VSX platforms
- **Iranian-Linked Groups**: Deploying MuddyViper backdoor against Israeli sectors including academia, engineering, government, manufacturing, technology, transportation, and utilities
- **Tomiris Group**: Russian-speaking threat actor targeting government and diplomatic entities in CIS member states and Central Asia using evolved tactics including public service implants for stealthier command and control
- **ShadyPanda**: Seven-year browser extension campaign affecting 4.3 million installations, turning legitimate extensions into spyware after establishing user trust
- **Inc Ransomware Gang**: Responsible for CodeRED emergency alert platform attack with claims of stealing sensitive subscriber data