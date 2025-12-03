# Exploitation Report

The cybersecurity landscape is currently experiencing significant exploitation activity across multiple vectors, with particular concern around zero-day vulnerabilities in Android systems and sophisticated supply chain attacks. Google has confirmed two Android framework vulnerabilities are being actively exploited in targeted attacks, while threat actors continue to weaponize trusted platforms like NPM and browser extensions for large-scale campaigns. Notable activities include North Korean APT groups conducting elaborate social engineering schemes, Iranian-linked actors deploying new backdoors against Israeli targets, and massive supply chain compromises affecting hundreds of thousands of developers through malicious packages and browser extensions.

## Active Exploitation Details

### Android Framework Zero-Day Vulnerabilities
- **Description**: Two critical vulnerabilities in the Android framework are being actively exploited in targeted attacks
- **Impact**: Attackers can achieve system compromise and unauthorized access to Android devices
- **Status**: Google has released patches in the December 2025 Android security bulletin addressing 107 total vulnerabilities

### IP Camera Exploitation Campaign
- **Description**: Large-scale hacking of IP cameras across Korea resulting in theft and monetization of private footage
- **Impact**: Over 120,000 IP cameras compromised, with stolen intimate videos sold to foreign adult websites
- **Status**: Four suspects arrested by Korean National Police, investigation ongoing

### Oracle E-Business Suite Breach
- **Description**: Successful exploitation of Oracle E-Business Suite servers at University of Pennsylvania
- **Impact**: Theft of documents containing personal information from university systems
- **Status**: Breach occurred in August, university has confirmed data theft

## Affected Systems and Products

- **Android Operating System**: Framework vulnerabilities affecting Android devices globally
- **IP Camera Systems**: Over 120,000 devices compromised across Korea
- **Oracle E-Business Suite**: Enterprise business application servers
- **NPM Package Registry**: Hundreds of malicious packages with over 31,000 downloads
- **Browser Extensions**: 4.3 million installations affected across Chrome and Edge platforms
- **Microsoft Visual Studio Marketplace**: 24 malicious extensions impersonating developer tools
- **CodeRED Emergency Alert Platform**: Critical infrastructure system completely shut down

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious NPM packages designed to steal developer credentials and secrets
- **Browser Extension Hijacking**: Legitimate extensions turned into spyware affecting millions of users
- **Social Engineering**: Elaborate fake interview schemes targeting software developers
- **Phishing Campaigns**: Calendly-themed lures impersonating major brands to steal business account credentials
- **Zero-Day Exploitation**: Active exploitation of unpatched Android vulnerabilities in targeted attacks
- **AI Evasion Techniques**: Hidden prompts and scripts designed to bypass AI-powered security scanners
- **Identity Rental Schemes**: North Korean actors recruiting legitimate developers to rent their identities

## Threat Actor Activities

- **Lazarus APT Group**: Conducting sophisticated remote worker schemes captured live by researchers, targeting software developers through fake job opportunities
- **MuddyWater (Iranian APT)**: Deploying new MuddyViper backdoor against Israeli sectors including academia, engineering, government, manufacturing, technology, transportation, and utilities
- **North Korean IT Workers**: Large-scale identity rental operations targeting software developers for illicit fundraising activities
- **ShadyPanda**: Seven-year browser extension campaign affecting 4.3 million installations, converting legitimate extensions into spyware
- **GlassWorm Campaign**: Supply chain attacks infiltrating Visual Studio Marketplace with 24 malicious extensions impersonating popular developer tools
- **Shai-Hulud Operators**: Advanced NPM malware attack exposing up to 400,000 developer secrets through infected packages
- **Tomiris Group**: Russian-speaking APT targeting government and diplomatic entities in CIS member states and Central Asia
- **Inc Ransomware Gang**: Responsible for CodeRED Emergency Alert Platform attack, claiming theft of sensitive subscriber data