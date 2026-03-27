# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms, with particular focus on AI frameworks, e-commerce platforms, and iOS devices. The most significant active exploitation involves CVE-2026-33017 in the Langflow AI platform, where threat actors began exploiting the code injection vulnerability within hours of disclosure. Additionally, widespread attacks against Magento stores using the PolyShell vulnerability are targeting over half of all vulnerable installations, while sophisticated iOS exploit frameworks continue to evolve from previous zero-click campaigns.

## Active Exploitation Details

### Langflow AI Platform Code Injection Vulnerability
- **Description**: Critical code injection vulnerability affecting the Langflow AI workflow framework
- **Impact**: Allows hackers to hijack AI workflows and execute arbitrary code
- **Status**: Actively exploited by threat actors within hours of disclosure
- **CVE ID**: CVE-2026-33017

### PolyShell Magento Vulnerability
- **Description**: Vulnerability affecting Magento Open Source version 2 and Adobe Commerce installations
- **Impact**: Enables attackers to compromise e-commerce stores and potentially access customer data
- **Status**: Active exploitation targeting 56% of all vulnerable Magento stores

### Operation Triangulation iOS Exploits
- **Description**: Zero-click iMessage exploits targeting iPhones, now evolved into the Coruna exploit framework
- **Impact**: Allows remote device compromise and espionage without user interaction
- **Status**: Framework continues to be developed and used in mass attacks

### Claude Chrome Extension XSS Vulnerability
- **Description**: Zero-click cross-site scripting vulnerability enabling prompt injection
- **Impact**: Allows malicious prompts to be triggered by simply visiting a webpage
- **Status**: Recently disclosed vulnerability in Anthropic's Claude extension

### Citrix NetScaler Vulnerabilities
- **Description**: Two vulnerabilities in NetScaler ADC and Gateway, similar to previously exploited CitrixBleed flaws
- **Impact**: Potential for unauthorized access and data exfiltration
- **Status**: Recently patched with urgent advisory from Citrix

## Affected Systems and Products

- **Langflow AI Framework**: AI workflow management platform used for building AI applications
- **Magento Open Source v2**: E-commerce platform installations running vulnerable versions
- **Adobe Commerce**: Enterprise e-commerce platform affected by PolyShell attacks
- **Apple iOS Devices**: iPhones targeted by Coruna exploit framework
- **Claude Chrome Extension**: Anthropic's AI assistant browser extension
- **Citrix NetScaler ADC/Gateway**: Network delivery and security appliances
- **Ajax Football Club IT Systems**: Fan data and ticketing systems
- **TikTok for Business Accounts**: Business accounts targeted in phishing campaigns
- **Microsoft Accounts**: Targeted through Bubble platform abuse
- **Cryptocurrency Wallets**: 728 different wallet extensions targeted by Torg Grabber

## Attack Vectors and Techniques

- **Code Injection**: Direct exploitation of Langflow framework vulnerabilities for workflow hijacking
- **Zero-Click Exploits**: iMessage-based attacks requiring no user interaction for iOS compromise
- **Web Skimming**: WebRTC-based payment skimmers bypassing Content Security Policy controls
- **Prompt Injection**: XSS-based attacks against AI assistants through malicious web content
- **Phishing Campaigns**: Multi-stage attacks using legitimate platforms to evade detection
- **No-Code Platform Abuse**: Leveraging Bubble app builder to create malicious applications
- **Browser Extension Targeting**: Mass targeting of cryptocurrency wallet browser extensions

## Threat Actor Activities

- **Red Menshen (China-linked)**: Long-term espionage campaign embedding in telecom networks using BPFDoor implants for government network surveillance
- **PolyShell Attackers**: Coordinated campaign targeting vulnerable Magento installations across multiple regions
- **Coruna Framework Operators**: Continued development and deployment of iOS exploit frameworks based on Operation Triangulation code
- **TikTok Business Phishers**: Sophisticated phishing campaign specifically targeting business accounts with bot-resistant techniques
- **Cryptocurrency Wallet Thieves**: Operators of Torg Grabber infostealer targeting extensive range of crypto wallet extensions
- **E-commerce Skimmers**: Advanced threat actors using WebRTC channels to bypass security controls and steal payment data
- **AI Platform Exploiters**: Rapid exploitation of newly disclosed AI framework vulnerabilities within hours of public disclosure