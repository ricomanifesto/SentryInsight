# Exploitation Report

The current threat landscape reveals significant exploitation activity across multiple attack vectors, with particular focus on telecom infrastructure, e-commerce platforms, and mobile devices. China-linked threat actors continue leveraging sophisticated espionage campaigns using advanced implants like BPFDoor to target government networks through telecom providers. Critical vulnerabilities are being actively exploited in Magento/Adobe Commerce installations through PolyShell attacks affecting over half of vulnerable stores, while iOS devices face ongoing threats from evolved exploit frameworks based on previous zero-day campaigns. Additionally, threat actors are increasingly abusing legitimate platforms and AI-powered tools to conduct credential theft and payment fraud operations.

## Active Exploitation Details

### PolyShell Vulnerability in Magento/Adobe Commerce
- **Description**: Critical vulnerability affecting version 2 of Magento Open Source and Adobe Commerce installations
- **Impact**: Allows attackers to compromise e-commerce stores and potentially access sensitive customer and payment data
- **Status**: Currently being actively exploited against 56% of all vulnerable Magento stores worldwide

### iOS Kernel Vulnerabilities (Coruna Exploit Kit)
- **Description**: Evolved exploit framework reusing code from the 2023 Operation Triangulation campaign targeting iOS devices
- **Impact**: Enables zero-click exploitation of iPhones via iMessage, allowing complete device compromise and espionage
- **Status**: Active exploitation detected in mass attacks using updated versions of previous zero-day exploits

### Claude Chrome Extension XSS Vulnerability
- **Description**: Cross-site scripting vulnerability in Anthropic's Claude Google Chrome Extension enabling zero-click prompt injection
- **Impact**: Attackers can trigger malicious prompts and potentially compromise user interactions with the AI assistant by simply visiting a malicious webpage
- **Status**: Vulnerability disclosed and patched

### NetScaler ADC and Gateway Vulnerabilities
- **Description**: Two newly patched vulnerabilities in Citrix NetScaler products, with one being similar to previously exploited CitrixBleed flaws
- **Impact**: Could potentially allow unauthorized access and compromise of network infrastructure
- **Status**: Patches available; Citrix urging immediate patching due to similarity to previous zero-day exploits

## Affected Systems and Products

- **Magento Open Source v2**: E-commerce platforms vulnerable to PolyShell attacks
- **Adobe Commerce v2**: Enterprise e-commerce solutions affected by the same vulnerability
- **iOS Devices**: iPhones targeted by Coruna exploit kit via iMessage zero-click exploits
- **Claude Chrome Extension**: AI assistant browser extension vulnerable to XSS attacks
- **Citrix NetScaler ADC**: Application delivery controllers with newly discovered vulnerabilities
- **Citrix NetScaler Gateway**: VPN and remote access solutions requiring immediate patching
- **Telecom Network Infrastructure**: Compromised by China-linked actors for espionage operations
- **TikTok for Business Accounts**: Targeted in sophisticated phishing campaigns
- **Microsoft Account Systems**: Credential theft via abuse of Bubble AI app builder platform

## Attack Vectors and Techniques

- **BPFDoor Implants**: Stealthy backdoor malware embedded in telecom networks for persistent access
- **Zero-Click iMessage Exploits**: iOS device compromise without user interaction via messaging platform
- **WebRTC Data Channels**: Payment skimmers bypassing Content Security Policy (CSP) controls on e-commerce sites
- **Phishing via No-Code Platforms**: Abuse of legitimate Bubble AI platform to host credential theft applications
- **Bot-Driven Account Takeovers**: Multi-stage fraud attacks chaining bots, proxies, and stolen credentials
- **Solana Blockchain Dead Drops**: GlassWorm malware using cryptocurrency blockchain for command and control
- **AI Platform Abuse**: Threat actors leveraging AI-powered tools for enhanced social engineering and evasion

## Threat Actor Activities

- **Red Menshen (China-linked)**: Long-term espionage campaign targeting government networks via telecom infrastructure using BPFDoor implants
- **PolyShell Attackers**: Mass exploitation campaign targeting vulnerable Magento/Adobe Commerce installations across 56% of susceptible stores
- **Coruna Kit Operators**: Advanced persistent threat group deploying evolved iOS exploit framework based on Operation Triangulation code
- **GlassWorm Campaign**: Sophisticated malware operation using Solana blockchain for C2 communications and comprehensive data theft
- **TikTok Business Phishers**: Organized campaign specifically targeting business accounts with bot-detection evasion techniques
- **RedLine Infostealer Network**: Prolific malware operation with alleged administrator extradited to US for prosecution
- **Torg Grabber Operators**: New infostealer campaign targeting 850 browser extensions including 700+ cryptocurrency wallets
- **LeakBase Forum Administration**: Major cybercrime marketplace for stolen data and hacking tools disrupted by Russian law enforcement