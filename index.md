# Exploitation Report

The current threat landscape reveals several critical active exploitation campaigns, with CISA flagging a Wing FTP Server vulnerability for active exploitation and multiple sophisticated attack vectors being deployed by threat actors. LeakNet ransomware operations are leveraging ClickFix social engineering techniques combined with Deno runtime for stealthy deployments, while North Korean threat actors are conducting targeted phishing campaigns using EndRAT malware. Supply chain attacks continue to escalate with GlassWorm malware evolving to abuse GitHub tokens and Visual Studio Code extensions, and a significant compromise of the AppsFlyer Web SDK affecting cryptocurrency security across multiple websites. State-sponsored groups are maintaining persistent access to Southeast Asian military organizations through novel backdoors, while Ukrainian entities face targeted espionage campaigns using Microsoft Edge debugging features for stealth operations.

## Active Exploitation Details

### Wing FTP Server Path Disclosure Vulnerability
- **Description**: A medium-severity security flaw in Wing FTP Server that allows attackers to leak server paths and potentially chain with other vulnerabilities for remote code execution
- **Impact**: Attackers can obtain sensitive server path information and potentially achieve remote code execution when chained with other exploits
- **Status**: Actively exploited in the wild and added to CISA's Known Exploited Vulnerabilities catalog

### ClickFix Social Engineering Campaign
- **Description**: Multiple campaigns using fake error messages and malicious installers to deploy various malware payloads including LeakNet ransomware and MacSync infostealer
- **Impact**: Complete system compromise, ransomware deployment, and data theft through social engineering rather than technical exploits
- **Status**: Ongoing campaigns targeting multiple platforms including Windows and macOS

### AppsFlyer Web SDK Supply Chain Attack
- **Description**: Temporary compromise of the AppsFlyer Web SDK with malicious JavaScript code designed to steal cryptocurrency
- **Impact**: Cryptocurrency theft from users visiting websites that implemented the compromised SDK
- **Status**: Attack was detected and remediated, but affected multiple websites during the compromise period

### GlassWorm Campaign GitHub Token Abuse
- **Description**: Malware campaign leveraging stolen GitHub tokens to inject malicious code into Python repositories and Visual Studio Code extensions
- **Impact**: Code repository compromise, malware distribution through legitimate development channels, and supply chain poisoning
- **Status**: Ongoing campaign with 72 malicious Open VSX extensions identified and hundreds of Python repositories affected

## Affected Systems and Products

- **Wing FTP Server**: All versions vulnerable to path disclosure attacks
- **Windows 11 Enterprise**: Devices receiving hotpatch updates affected by RRAS remote code execution vulnerability
- **Samsung Galaxy Book 4**: Systems experiencing C: drive access issues due to Samsung Galaxy Connect app
- **GitHub Repositories**: Hundreds of Python projects compromised through stolen token abuse
- **Visual Studio Code**: 72 malicious extensions identified in Open VSX registry
- **AppsFlyer SDK**: Websites using the Web SDK temporarily affected by cryptocurrency stealer
- **Microsoft Edge**: Browsers on Ukrainian systems targeted for debugging API abuse
- **KakaoTalk Desktop**: Application compromised to spread EndRAT malware
- **Companies House WebFiling**: UK government service affected by data exposure flaw

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Fake error messages prompting users to run malicious PowerShell commands or download infected installers
- **Supply Chain Poisoning**: Compromising legitimate software distribution channels including GitHub repositories and VS Code extensions
- **Token Theft and Abuse**: Stealing GitHub authentication tokens to force-push malicious code into repositories
- **SDK Hijacking**: Temporarily compromising third-party software development kits to inject malicious code
- **Phishing and Spear Phishing**: Targeted email campaigns to deliver initial access malware
- **Living-off-the-Land**: Abusing legitimate tools like Microsoft Edge debugging APIs and Deno runtime for stealth
- **Application Hijacking**: Compromising messaging applications like KakaoTalk for lateral malware distribution

## Threat Actor Activities

- **LeakNet Ransomware Gang**: Deploying ransomware through ClickFix techniques and Deno runtime-based loaders for enhanced stealth
- **North Korean Threat Actors (Konni)**: Conducting spear-phishing campaigns to deploy EndRAT and compromise KakaoTalk for malware propagation
- **China-Nexus Groups**: Maintaining multi-year persistent access to Southeast Asian military organizations using novel backdoors and evasion techniques
- **Russian-Linked Actors**: Targeting Ukrainian entities with DRILLAPP backdoor campaign leveraging Microsoft Edge debugging for espionage
- **GlassWorm Operators**: Escalating supply chain attacks through GitHub token theft and malicious VS Code extension distribution
- **Cryptocurrency Thieves**: Hijacking popular Web SDKs to inject crypto-stealing JavaScript across multiple websites
- **Social Engineering Groups**: Abusing legitimate platforms like LiveChat to conduct phishing campaigns targeting PayPal and Amazon customers