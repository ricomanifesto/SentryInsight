# Exploitation Report

The current threat landscape reveals significant active exploitation across multiple attack vectors, with Android zero-day vulnerabilities being exploited in targeted attacks and widespread malicious campaigns targeting developer ecosystems. Two critical Android framework vulnerabilities are confirmed to be actively exploited in the wild, while sophisticated supply chain attacks through npm packages and browser extensions continue to compromise millions of users. Threat actors are leveraging enhanced backdoor capabilities, AI jailbreaking techniques, and infrastructure-as-a-service models to conduct espionage operations and financial fraud at scale.

## Active Exploitation Details

### Android Framework Zero-Day Vulnerabilities
- **Description**: Two critical vulnerabilities in the Android framework that allow attackers to compromise device security through targeted exploitation
- **Impact**: Complete device compromise, unauthorized access to sensitive data, and potential persistent access to affected Android systems
- **Status**: Actively exploited in targeted attacks; patches released in December 2025 Android security bulletin addressing 107 total vulnerabilities

### IP Camera Security Vulnerabilities
- **Description**: Systematic exploitation of security weaknesses in over 120,000 IP cameras across South Korea, allowing unauthorized access to video streams
- **Impact**: Mass surveillance breach with stolen intimate footage sold on foreign adult websites, severe privacy violations affecting thousands of users
- **Status**: Active exploitation confirmed with arrests made; specific vulnerabilities and patch status not disclosed

### Oracle E-Business Suite Vulnerabilities
- **Description**: Security flaws in Oracle EBS systems allowing unauthorized access to sensitive institutional data
- **Impact**: Data theft including personal information from university systems, potential exposure of student and employee records
- **Status**: Actively exploited in August 2024 against University of Pennsylvania systems

## Affected Systems and Products

- **Android Devices**: All Android versions affected by framework vulnerabilities, with patches available in December 2025 security update
- **IP Cameras**: Over 120,000 IP camera systems in South Korea compromised through unspecified security weaknesses
- **Oracle E-Business Suite**: Enterprise systems vulnerable to data theft attacks targeting educational institutions
- **NPM Ecosystem**: Hundreds of malicious packages in Node Package Manager registry exposing up to 400,000 developer secrets
- **Browser Extensions**: 4.3 million installations of malicious Chrome and Edge extensions turned into spyware
- **Visual Studio Code Extensions**: 24 malicious extensions impersonating popular developer tools in Microsoft marketplace

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Shai-Hulud 2.0 worm self-replicating through npm packages to steal AWS, Google Cloud, and Azure credentials
- **Extension Hijacking**: ShadyPanda campaign converting legitimate browser extensions into spyware over seven-year period
- **AI Prompt Injection**: Poetry-based jailbreaking techniques increasing AI model attack success rates from 8% to 43%
- **Social Engineering**: Fake Calendly invitations impersonating major brands to hijack Google Workspace and Facebook business accounts
- **Identity Rental Schemes**: North Korean operatives recruiting legitimate developers to rent identities for illicit IT work
- **Phishing Campaigns**: Sophisticated lures targeting ad manager accounts through spoofed brand communications

## Threat Actor Activities

- **MuddyWater (Iran)**: Evolved operations using new MuddyViper backdoor and Fooder loader for memory-only tactics against Israeli sectors including academia, engineering, government, manufacturing, technology, transportation, and utilities
- **Lazarus Group (North Korea)**: Remote worker infiltration scheme captured live, targeting software development companies through fake employment operations
- **ShadyPanda**: Long-term browser extension campaign spanning seven years with over 4.3 million compromised installations
- **GlassWorm**: Supply chain campaign targeting developer tools through 24 malicious Visual Studio Code extensions
- **Tomiris**: Russian-speaking group deploying new Havoc framework tools against government and diplomatic entities in CIS states and Central Asia
- **Inc Ransomware Gang**: Responsible for CodeRED emergency alert platform attack, claiming theft of sensitive subscriber data
- **North Korean IT Workers**: Systematic identity theft operations recruiting legitimate engineers for sanctions evasion and revenue generation