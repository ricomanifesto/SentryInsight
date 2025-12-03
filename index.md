# Exploitation Report

Multiple critical security incidents have emerged across various platforms, with Android zero-day vulnerabilities being actively exploited in targeted attacks, sophisticated supply chain campaigns targeting developers through malicious NPM packages, and advanced persistent threat groups deploying new backdoors in espionage operations. Notable activities include North Korean state-sponsored actors infiltrating software development environments, Iranian threat groups targeting Israeli infrastructure with advanced stealth techniques, and widespread exploitation of IP cameras leading to privacy violations. The security landscape demonstrates a concerning shift toward more sophisticated attack vectors including AI-powered evasion techniques and the commoditization of cybercrime tools through subscription-based models.

## Active Exploitation Details

### Android Framework Zero-Day Vulnerabilities
- **Description**: Two critical vulnerabilities in the Android framework are being actively exploited in targeted attacks
- **Impact**: Attackers can compromise Android devices through these framework-level flaws, potentially gaining system-level access
- **Status**: Patched in Google's December 2025 Android security bulletin alongside 105 other vulnerabilities

### IP Camera Security Vulnerabilities
- **Description**: Widespread exploitation of IP camera security flaws allowing unauthorized access to surveillance feeds
- **Impact**: Unauthorized access to private video feeds, enabling theft and sale of intimate content
- **Status**: Over 120,000 IP cameras compromised across South Korea, with suspects arrested for selling stolen footage

### Oracle E-Business Suite Vulnerabilities
- **Description**: Security flaws in Oracle E-Business Suite servers enabling unauthorized data access
- **Impact**: Theft of documents containing personal information from enterprise systems
- **Status**: Exploited against University of Pennsylvania in August, resulting in confirmed data breach

## Affected Systems and Products

- **Android Devices**: Framework-level vulnerabilities affecting multiple Android versions
- **IP Cameras**: Over 120,000 surveillance cameras compromised across South Korea
- **NPM Ecosystem**: 197+ malicious packages with 31,000+ downloads targeting JavaScript developers
- **Browser Extensions**: 24 malicious Visual Studio Code extensions in Microsoft Marketplace and Open VSX
- **Oracle E-Business Suite**: Enterprise resource planning systems vulnerable to data theft
- **Popular Browser Extensions**: 4.3 million installations compromised by ShadyPanda campaign over seven years

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious NPM packages disguised as legitimate developer tools targeting software engineers
- **Extension Marketplace Abuse**: Malicious browser extensions impersonating popular development tools to harvest credentials
- **Social Engineering**: Fake IT recruitment schemes targeting developers for identity theft and remote work fraud
- **Memory-Only Malware**: Advanced backdoors like MuddyViper operating entirely in memory to evade detection
- **AI Evasion Techniques**: Hidden prompts and scripts designed to influence AI-driven security scanners
- **Phishing Campaigns**: Calendly-themed attacks impersonating major brands to steal Google Workspace and Facebook credentials

## Threat Actor Activities

- **MuddyWater (Iran-linked)**: Deploying new MuddyViper backdoor with Fooder loader against Israeli sectors including academia, engineering, government, manufacturing, and utilities
- **Lazarus APT (North Korea)**: Operating sophisticated remote worker identity rental schemes to infiltrate organizations while evading sanctions
- **ShadyPanda**: Conducting seven-year browser extension campaign compromising 4.3 million installations for data harvesting
- **GlassWorm**: Returning with 24 malicious Visual Studio Code extensions targeting developers through supply chain attacks
- **Tomiris (Russian-speaking)**: Targeting government and diplomatic entities in CIS states and Central Asia using new Havoc framework tools
- **Shai-Hulud Operators**: Executing second major NPM supply chain attack exposing 400,000 developer secrets through infected packages
- **Inc Ransomware Gang**: Attacking CodeRED emergency alert platform and claiming theft of sensitive subscriber data