# Exploitation Report

The current threat landscape is dominated by sophisticated supply chain attacks targeting developer environments and critical infrastructure vulnerabilities. The GlassWorm malware campaign represents a significant escalation in supply chain threats, evolving to abuse stolen GitHub tokens for injecting malware into Python repositories and exploiting 72 Open VSX extensions to target developers. Meanwhile, CISA has flagged a Wing FTP Server vulnerability as actively exploited in the wild, and attackers have successfully hijacked the AppsFlyer Web SDK to distribute cryptocurrency-stealing JavaScript code. State-sponsored groups continue targeting critical sectors, with Russian-linked actors deploying the DRILLAPP backdoor against Ukrainian entities and Chinese hackers conducting long-term espionage campaigns against Southeast Asian military organizations using AppleChris and MemFun malware.

## Active Exploitation Details

### Wing FTP Server Vulnerability
- **Description**: A critical vulnerability in Wing FTP Server that enables remote code execution when chained with other exploits
- **Impact**: Attackers can achieve remote code execution on affected systems
- **Status**: Actively exploited in attacks, CISA has issued warnings to U.S. government agencies

### GlassWorm Supply Chain Attack
- **Description**: Sophisticated malware campaign targeting developers through multiple vectors including stolen GitHub tokens and malicious VSX extensions
- **Impact**: Malware injection into Python repositories, compromise of developer environments, and potential widespread distribution through dependency chains
- **Status**: Actively evolving with new evasion techniques and attack vectors

### AppsFlyer Web SDK Hijack
- **Description**: Supply chain attack where the AppsFlyer Web SDK was temporarily compromised with malicious JavaScript code
- **Impact**: Cryptocurrency theft from users of applications using the compromised SDK
- **Status**: Temporary hijacking that has been addressed, but demonstrates ongoing supply chain risks

## Affected Systems and Products

- **Wing FTP Server**: Vulnerable instances requiring immediate patching to prevent remote code execution
- **Python Repositories**: Hundreds of repositories targeted by GlassWorm campaign through stolen GitHub tokens
- **Open VSX Registry**: 72 malicious extensions identified as part of GlassWorm campaign targeting developers
- **AppsFlyer Web SDK**: JavaScript SDK temporarily compromised to distribute crypto-stealing code
- **Steam Gaming Platform**: Eight malicious games identified by FBI investigation spreading malware to gamers
- **Samsung Galaxy Book 4**: Windows 11 devices affected by Samsung Galaxy Connect app blocking C: drive access
- **Companies House WebFiling**: UK government service experienced security flaw exposing business data

## Attack Vectors and Techniques

- **Stolen GitHub Token Abuse**: Attackers using compromised GitHub tokens to force-push malware into legitimate repositories
- **VSX Extension Poisoning**: Malicious extensions uploaded to Open VSX registry to target Visual Studio Code developers
- **SDK Supply Chain Compromise**: Hijacking of legitimate software development kits to distribute malware
- **Gaming Platform Abuse**: Uploading malicious games to Steam platform for malware distribution
- **Microsoft Edge Debugging Abuse**: DRILLAPP backdoor leverages Edge debugging features for stealth espionage
- **ClickFix Social Engineering**: Fake AI tool installers used to deploy MacSync infostealer on macOS systems
- **LiveChat Impersonation**: Social engineering campaigns impersonating PayPal and Amazon through customer support interactions

## Threat Actor Activities

- **Russian-linked APT Groups**: Deploying DRILLAPP backdoor against Ukrainian entities using Microsoft Edge debugging for stealth operations
- **Chinese State-sponsored Actors**: Long-term espionage campaign targeting Southeast Asian military organizations with AppleChris and MemFun malware, dating back to at least 2020
- **GlassWorm Campaign Operators**: Sophisticated supply chain attackers evolving techniques to target developer environments through multiple vectors
- **Cybercriminals**: Targeting Poland's National Centre for Nuclear Research, Stryker medical technology company, and conducting phishing campaigns through various platforms