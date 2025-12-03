# Exploitation Report

The cybersecurity landscape is currently experiencing significant exploitation activity across multiple vectors, with Android zero-day vulnerabilities being actively exploited in targeted attacks and sophisticated supply chain campaigns targeting developer ecosystems. Google has confirmed two Android framework vulnerabilities are being exploited in the wild, while North Korean threat actors continue their elaborate schemes targeting IT workers and developers. Notable supply chain attacks include the Shai-Hulud 2.0 campaign exposing up to 400,000 developer secrets and the ongoing GlassWorm campaign infiltrating Visual Studio Code marketplaces. Additionally, browser extension campaigns like ShadyPanda have compromised over 4.3 million installations, and Iranian-linked actors are deploying new backdoors in targeted operations against Israeli infrastructure.

## Active Exploitation Details

### Android Framework Vulnerabilities
- **Description**: Two vulnerabilities in the Android Framework have been actively exploited in targeted attacks
- **Impact**: Attackers can exploit these framework flaws to compromise Android devices in targeted campaigns
- **Status**: Patched in Google's December 2025 Android security bulletin addressing 107 total vulnerabilities

### Shai-Hulud 2.0 NPM Supply Chain Attack
- **Description**: Self-replicating npm-package poisoning worm targeting the Node Package Manager registry
- **Impact**: Exposed approximately 400,000 raw developer secrets and credentials from AWS, Google Cloud Platform, and Azure environments
- **Status**: Active campaign that infected hundreds of packages and published stolen data in 30,000 GitHub repositories

### SmartTube Android TV Application Compromise
- **Description**: Popular open-source YouTube client for Android TV was compromised through developer signing key theft
- **Impact**: Malicious updates were pushed to users through legitimate application channels
- **Status**: Developer signing keys were compromised, allowing attackers to distribute malicious updates

## Affected Systems and Products

- **Android Devices**: Framework vulnerabilities affecting multiple Android versions
- **NPM Package Manager**: Hundreds of infected packages in the registry ecosystem
- **Visual Studio Code Marketplaces**: 24 malicious extensions on Microsoft Visual Studio Marketplace and Open VSX
- **Browser Extensions**: Over 4.3 million installations across Chrome and other browsers affected by ShadyPanda campaign
- **SmartTube Application**: Android TV users receiving compromised updates
- **Oracle E-Business Suite**: University of Pennsylvania servers compromised in August
- **CodeRED Emergency Platform**: Emergency alert system shut down following ransomware attack

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages injected into NPM registry and Visual Studio marketplaces
- **Social Engineering**: North Korean actors using fake recruitment schemes to target developers
- **Credential Harvesting**: Phishing campaigns using Calendly-themed lures to steal Google Workspace and Facebook credentials
- **Browser Extension Hijacking**: Long-term campaigns converting legitimate extensions into spyware
- **AI Security Tool Evasion**: Malicious npm packages using hidden prompts to influence AI-driven security scanners
- **Identity Rental Schemes**: North Korean IT workers targeting engineers to rent their identities for illicit activities
- **Signing Key Compromise**: Attackers gaining access to developer signing keys to push malicious updates

## Threat Actor Activities

- **North Korean IT Workers**: Operating sophisticated identity rental schemes targeting engineers and developers for fundraising activities
- **Lazarus APT Group**: Conducting remote-worker schemes captured live during security research operations
- **ShadyPanda**: Seven-year-long browser extension campaign affecting over 4.3 million installations
- **GlassWorm Campaign**: Third wave of malicious Visual Studio Code packages impersonating popular developer tools
- **Iranian-Linked Actors**: Deploying new MuddyViper backdoor targeting Israeli sectors including academia, engineering, government, manufacturing, technology, transportation, and utilities
- **Tomiris Group**: Russian-speaking group targeting government and diplomatic entities in CIS member states and Central Asia using new tools and tactics
- **Inc Ransomware Gang**: Responsible for CodeRED emergency platform attack, claiming theft of sensitive subscriber data