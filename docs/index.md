# Exploitation Report

Current cybersecurity landscape shows significant exploitation activity with CISA adding Wing FTP Server vulnerabilities to its Known Exploited Vulnerabilities catalog due to active attacks. Multiple supply chain attacks are targeting developers through compromised extensions and repositories, including the GlassWorm campaign affecting Python packages and VSCode extensions. Advanced persistent threat groups continue sophisticated campaigns, with North Korean Konni group leveraging phishing and social platforms for malware distribution, while China-nexus actors maintain long-term access to Southeast Asian military organizations. Notable ransomware evolution includes LeakNet's adoption of ClickFix techniques and novel deployment methods using Deno runtime for enhanced stealth operations.

## Active Exploitation Details

### Wing FTP Server Information Disclosure Vulnerability
- **Description**: A medium-severity security flaw in Wing FTP Server that enables information disclosure, specifically leaking server path information
- **Impact**: Attackers can obtain sensitive server path information that may be chained with other vulnerabilities for remote code execution
- **Status**: Actively exploited in the wild, CISA has added to KEV catalog requiring federal agencies to patch by specific deadline

### Windows 11 RRAS Remote Code Execution Vulnerability
- **Description**: A security vulnerability affecting Windows 11 Enterprise devices in the Routing and Remote Access Service (RRAS) component
- **Impact**: Potential remote code execution on affected Windows systems
- **Status**: Microsoft released out-of-band hotpatch update to address the vulnerability

### AppsFlyer Web SDK Supply Chain Attack
- **Description**: Temporary hijacking of the AppsFlyer Web SDK with malicious JavaScript code injection
- **Impact**: Cryptocurrency theft through compromised SDK affecting websites using the service
- **Status**: Supply chain attack that was active but has been addressed

## Affected Systems and Products

- **Wing FTP Server**: All versions containing the information disclosure vulnerability
- **Windows 11 Enterprise**: Devices receiving hotpatch updates affected by RRAS vulnerability
- **Samsung Galaxy Book 4**: Models experiencing C: drive access issues with Windows 11 versions 25H2 and 24H2
- **Python Repositories**: Hundreds of Python packages targeted by GlassWorm malware injection
- **VSCode Extensions**: 72 malicious Open VSX extensions used in GlassWorm campaign
- **AppsFlyer Web SDK**: Websites using the SDK temporarily affected by crypto-stealing code
- **Microsoft Outlook Classic**: Users with Teams Meeting Add-in enabled experiencing application failures
- **Companies House WebFiling**: UK government service exposed business data through security flaw

## Attack Vectors and Techniques

- **ClickFix Technique**: Social engineering method used by LeakNet ransomware and MacSync infostealer campaigns to trick users into executing malicious code
- **Supply Chain Poisoning**: GlassWorm campaign using stolen GitHub tokens to force-push malware into legitimate repositories
- **VSCode Extension Abuse**: Malicious extensions in Open VSX registry targeting developer environments
- **Phishing with Social Platform Abuse**: Konni group using spear phishing to compromise KakaoTalk desktop applications for malware propagation
- **Microsoft Edge Debugging Abuse**: DRILLAPP backdoor leveraging browser debugging features for stealth operations
- **Deno Runtime Exploitation**: LeakNet ransomware using open-source Deno runtime for JavaScript-based malware deployment
- **LiveChat Impersonation**: Social engineering campaigns mimicking PayPal and Amazon customer support to steal credentials

## Threat Actor Activities

- **LeakNet Ransomware Group**: Evolved tactics incorporating ClickFix social engineering and Deno runtime for initial access and payload deployment in corporate environments
- **Konni Group (North Korean)**: Active phishing campaigns targeting victims to gain access to KakaoTalk desktop applications for malware distribution to contacts
- **China-Nexus Actors**: Long-term cyberespionage operations maintaining persistent access to Southeast Asian military organizations using novel backdoors and evasion techniques
- **GlassWorm Campaign Operators**: Sophisticated supply chain attacks targeting developer ecosystems through GitHub token theft and malicious extension deployment
- **Russia-Linked Actors**: DRILLAPP backdoor deployment against Ukrainian entities using Microsoft Edge debugging features for stealth espionage operations