# Exploitation Report

Critical exploitation activity is currently dominated by sophisticated supply chain attacks and infrastructure targeting. The GlassWorm malware campaign represents a significant escalation in developer-focused attacks, leveraging stolen GitHub tokens to inject malicious code into Python repositories while simultaneously abusing 72 Open VSX extensions to target development environments. CISA has flagged a Wing FTP Server vulnerability as actively exploited in the wild, warning federal agencies to secure their instances against potential remote code execution attacks. State-sponsored activities continue with China-nexus threat actors maintaining persistent access to Southeast Asian military organizations through novel backdoors, while Russian-linked groups deploy the DRILLAPP backdoor against Ukrainian entities using Microsoft Edge debugging features for stealth operations.

## Active Exploitation Details

### Wing FTP Server Vulnerability
- **Description**: A security flaw in Wing FTP Server that is being actively exploited by threat actors
- **Impact**: The vulnerability may be chained in remote code execution attacks, allowing attackers to gain unauthorized system access
- **Status**: Currently being exploited in the wild; CISA has issued warnings to federal agencies to secure their instances

### GlassWorm Supply Chain Attack
- **Description**: A sophisticated malware campaign targeting developers through multiple attack vectors including stolen GitHub tokens and malicious Visual Studio Code extensions
- **Impact**: Malware injection into Python repositories, compromise of development environments, and potential downstream supply chain contamination
- **Status**: Active campaign with significant escalation in attack methods

### Companies House Security Flaw
- **Description**: A security vulnerability in the UK's Companies House WebFiling service that exposed business data
- **Impact**: Exposure of sensitive business registration and filing information
- **Status**: Service was temporarily taken offline for remediation; now restored

## Affected Systems and Products

- **Wing FTP Server**: File transfer server instances requiring immediate patching and security review
- **Python Repositories**: Hundreds of repositories on GitHub targeted for malware injection
- **Open VSX Registry**: 72 malicious extensions targeting Visual Studio Code development environments
- **AppsFlyer Web SDK**: JavaScript SDK temporarily hijacked for cryptocurrency theft
- **Steam Gaming Platform**: Eight malicious games identified as malware delivery vectors
- **Companies House WebFiling**: UK government business registry service
- **Windows 11**: Samsung PC users experiencing C: drive access issues after February 2026 security updates
- **Microsoft Edge**: Browser debugging features abused by DRILLAPP backdoor

## Attack Vectors and Techniques

- **Stolen Token Abuse**: Attackers using compromised GitHub tokens to force-push malicious code into legitimate repositories
- **Supply Chain Poisoning**: Injection of malware into development tools and dependencies to reach downstream targets
- **Browser Debugging Exploitation**: DRILLAPP backdoor leverages Microsoft Edge debugging capabilities for stealth operations
- **Social Engineering**: ClickFix campaigns distributing MacSync infostealer through fake AI tool installers
- **Extension Marketplace Abuse**: Malicious extensions distributed through Open VSX registry targeting developers
- **Phishing via LiveChat**: Attackers impersonating PayPal and Amazon through customer support interactions
- **SDK Hijacking**: Temporary compromise of AppsFlyer Web SDK to inject cryptocurrency-stealing code

## Threat Actor Activities

- **China-nexus Groups**: Long-term cyberespionage campaign against Southeast Asian military organizations using AppleChris and MemFun malware, maintaining persistent access since at least 2020
- **Russian-linked Actors**: Deployment of DRILLAPP backdoor against Ukrainian entities, utilizing Microsoft Edge debugging for stealth espionage operations
- **GlassWorm Campaign Operators**: Sophisticated supply chain attackers targeting developer ecosystems through multiple simultaneous attack vectors
- **Steam Game Malware Distributors**: Threat actors uploading malicious games to Steam platform for malware distribution, prompting FBI investigation
- **Cryptocurrency Thieves**: Groups exploiting compromised SDKs and fake AI tools to steal digital assets
- **State-sponsored Espionage**: Continued targeting of military and government organizations across Southeast Asia and Eastern Europe