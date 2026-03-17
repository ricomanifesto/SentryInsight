# Exploitation Report

Current security threats demonstrate a sophisticated landscape of active exploitation targeting critical infrastructure, development environments, and enterprise systems. The most concerning activities include the GlassWorm supply chain campaign targeting developers through malicious extensions and stolen GitHub tokens, CISA's warning about active exploitation of Wing FTP Server vulnerabilities, and targeted espionage campaigns using advanced malware like DRILLAPP backdoor against Ukrainian entities and AppleChris/MemFun malware against Southeast Asian militaries. Additionally, supply chain attacks have emerged through hijacked SDKs and malicious Steam games, while ransomless attacks like the Stryker incident demonstrate new destructive capabilities that can wipe thousands of devices without traditional malware deployment.

## Active Exploitation Details

### Wing FTP Server Vulnerability
- **Description**: A vulnerability in Wing FTP Server that is being actively exploited in the wild and may be chained with other vulnerabilities to achieve remote code execution
- **Impact**: Remote code execution capabilities when chained with other attack vectors
- **Status**: CISA has issued warnings for U.S. government agencies to secure their Wing FTP Server instances

### GlassWorm Supply Chain Attack
- **Description**: Multi-vector supply chain attack targeting Python repositories and Visual Studio Code extensions through stolen GitHub tokens and malicious Open VSX extensions
- **Impact**: Malware injection into hundreds of Python repositories and deployment of 72 malicious Open VSX extensions targeting developers
- **Status**: Ongoing campaign with evolved evasion techniques

### Chrome Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities affecting Google Chrome browser
- **Impact**: Active exploitation in the wild with potential for code execution and system compromise
- **Status**: Part of weekly security recap indicating active exploitation

### Companies House Security Flaw
- **Description**: Security vulnerability in the UK's Companies House WebFiling service that exposed business data
- **Impact**: Exposure of sensitive business registration and filing information
- **Status**: Service was temporarily shut down on Friday for remediation and has since been restored

## Affected Systems and Products

- **Wing FTP Server**: File transfer protocol server software used in enterprise environments
- **Python Repositories**: Hundreds of Python software repositories on GitHub platforms
- **Visual Studio Code Extensions**: 72 malicious extensions in the Open VSX registry targeting developers
- **Google Chrome**: Multiple versions affected by zero-day vulnerabilities
- **AppsFlyer Web SDK**: Marketing attribution platform temporarily hijacked for cryptocurrency theft
- **Steam Gaming Platform**: Eight malicious games identified by FBI investigation
- **Samsung Galaxy Books**: Specific models experiencing C: drive access issues on Windows 11
- **Stryker Medical Devices**: Tens of thousands of employee devices wiped in ransomless attack
- **Companies House WebFiling Service**: UK government business registry platform

## Attack Vectors and Techniques

- **Supply Chain Injection**: GlassWorm campaign using stolen GitHub tokens to force-push malware into legitimate repositories
- **Extension Poisoning**: Deployment of malicious Visual Studio Code extensions through Open VSX registry
- **SDK Hijacking**: Temporary compromise of AppsFlyer Web SDK to inject cryptocurrency-stealing JavaScript
- **Social Engineering**: ClickFix campaigns using fake AI tool installers to distribute MacSync infostealer on macOS
- **Stealth Backdoors**: DRILLAPP backdoor abusing Microsoft Edge debugging features for persistent access
- **Gaming Platform Abuse**: Distribution of malware through legitimate Steam gaming platform
- **Ransomless Attacks**: Stryker attack demonstrating device wiping without traditional ransomware deployment
- **Phishing via LiveChat**: Attackers impersonating PayPal and Amazon through customer support interactions

## Threat Actor Activities

- **Russian-Linked Groups**: Targeting Ukrainian entities with DRILLAPP backdoor malware using Microsoft Edge debugging for stealth espionage operations
- **Chinese State-Sponsored Actors**: Long-term espionage campaign against Southeast Asian military organizations using AppleChris and MemFun malware, dating back to at least 2020
- **GlassWorm Operators**: Sophisticated supply chain attackers targeting the software development ecosystem through multiple vectors including GitHub token theft and extension poisoning
- **Cryptocurrency Thieves**: Opportunistic actors hijacking popular SDKs and development tools for financial gain
- **Gaming Platform Attackers**: Groups distributing malware through Steam games, prompting FBI investigation and victim identification efforts