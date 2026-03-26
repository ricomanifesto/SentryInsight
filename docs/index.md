# Exploitation Report

Current security reports reveal several critical exploitation activities targeting both enterprise systems and mobile platforms. The most significant threats include zero-click iOS exploits being actively used through the evolved Coruna framework, payment skimmers bypassing security controls on e-commerce sites using WebRTC channels, and mass attacks targeting vulnerable Magento installations through the PolyShell vulnerability. Additional concerns include sophisticated phishing campaigns leveraging legitimate platforms like Bubble AI and TikTok for Business, along with the emergence of advanced malware families like GlassWorm using blockchain-based command and control infrastructure.

## Active Exploitation Details

### Coruna iOS Exploit Framework
- **Description**: An evolved version of the framework used in Operation Triangulation espionage campaigns, targeting iPhones through zero-click iMessage exploits
- **Impact**: Allows attackers to compromise iOS devices without user interaction, enabling espionage and data theft
- **Status**: Currently active in mass attacks, reusing kernel exploit code from 2023 Triangulation attacks

### PolyShell Magento Vulnerability
- **Description**: Critical vulnerability affecting Magento Open Source version 2 and Adobe Commerce installations
- **Impact**: Enables remote code execution and complete compromise of e-commerce platforms
- **Status**: Actively exploited against 56% of all vulnerable Magento stores

### Claude Chrome Extension XSS Flaw
- **Description**: Zero-click cross-site scripting vulnerability in Anthropic's Claude Google Chrome Extension
- **Impact**: Allows malicious prompt injection simply by visiting a compromised web page
- **Status**: Vulnerability disclosed and patched

### WebRTC Payment Skimmer
- **Description**: Novel payment card skimmer that uses WebRTC data channels to receive payloads and exfiltrate stolen payment data
- **Impact**: Bypasses Content Security Policy (CSP) controls to steal payment information from e-commerce sites
- **Status**: Currently active against e-commerce platforms

### NetScaler ADC and Gateway Vulnerabilities
- **Description**: Two critical vulnerabilities in Citrix NetScaler products, with one similar to previously exploited CitrixBleed flaws
- **Impact**: Potential for unauthorized access and data theft through network appliances
- **Status**: Patches available, administrators urged to update immediately

## Affected Systems and Products

- **iOS Devices**: iPhones targeted through zero-click iMessage exploits via Coruna framework
- **Magento E-commerce Platforms**: Version 2 of Magento Open Source and Adobe Commerce installations
- **Chrome Extensions**: Claude AI extension for Google Chrome browsers
- **E-commerce Websites**: Payment processing systems vulnerable to WebRTC-based skimmers
- **Citrix Infrastructure**: NetScaler ADC and NetScaler Gateway appliances
- **Cryptocurrency Wallets**: 728 different crypto wallet extensions targeted by Torg Grabber malware
- **Microsoft Accounts**: Targeted through Bubble AI platform abuse for credential theft
- **TikTok for Business**: Accounts targeted in sophisticated phishing campaigns

## Attack Vectors and Techniques

- **Zero-Click Mobile Exploits**: Deployment of iOS exploits through iMessage without user interaction
- **WebRTC Channel Abuse**: Using WebRTC data channels to bypass security controls and exfiltrate payment data
- **Platform Abuse**: Leveraging legitimate services like Bubble AI and TikTok for malicious campaigns
- **Blockchain Command and Control**: GlassWorm malware using Solana blockchain for dead drop communications
- **Multi-Stage Fraud Operations**: Coordinated bot signups, proxy networks, and credential theft for account takeovers
- **Phishing Kit Evolution**: Advanced kits targeting specific platforms with sophisticated evasion techniques
- **Supply Chain Targeting**: Attacks against development dependencies and AI-powered recommendation systems

## Threat Actor Activities

- **Operation Triangulation Operators**: Continued evolution of iOS exploitation framework into mass attack toolkit
- **E-commerce Threat Groups**: Systematic targeting of Magento stores using automated PolyShell exploitation
- **Payment Card Skimmers**: Development of advanced WebRTC-based skimming techniques to evade detection
- **Cryptocurrency Focused Actors**: Deployment of Torg Grabber targeting extensive range of crypto wallet extensions
- **RedLine Operation**: Ongoing infostealer campaign with administrator facing extradition to United States
- **LeakBase Forum Operators**: Major cybercrime marketplace disrupted with administrator arrest in Russia
- **GlassWorm Campaign**: Multi-stage malware operation using blockchain infrastructure for persistence
- **Corporate Impersonation Groups**: Sustained campaigns impersonating major companies like Palo Alto Networks for recruitment fraud