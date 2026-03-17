# Exploitation Report

Critical exploitation activity is currently dominated by several high-impact campaigns targeting diverse systems and platforms. The most significant developments include CISA's addition of a Wing FTP Server vulnerability to the Known Exploited Vulnerabilities catalog due to active exploitation, sophisticated ransomware operations employing ClickFix social engineering tactics, and advanced persistent threat actors conducting long-term espionage campaigns. Notable threat activities include the LeakNet ransomware gang's innovative use of Deno runtime for stealthy attacks, North Korean Konni group's exploitation of KakaoTalk for malware propagation, China-nexus hackers maintaining persistent access to Southeast Asian military organizations, and the GlassWorm campaign targeting Python repositories through stolen GitHub tokens.

## Active Exploitation Details

### Wing FTP Server Path Disclosure Vulnerability
- **Description**: A medium-severity security flaw in Wing FTP Server that allows attackers to leak server paths, potentially exposing sensitive system information
- **Impact**: Path disclosure that can be chained with other vulnerabilities to achieve remote code execution
- **Status**: Actively exploited in the wild, CISA has added this vulnerability to the Known Exploited Vulnerabilities catalog

### Companies House WebFiling Security Flaw
- **Description**: A security vulnerability in the UK's Companies House WebFiling service that exposed business data
- **Impact**: Unauthorized access to sensitive business information and company registry data
- **Status**: Service was temporarily taken offline and has been restored after fixing the vulnerability

### Microsoft Edge Debugging Feature Abuse
- **Description**: DRILLAPP backdoor campaign abusing Microsoft Edge debugging capabilities for stealth operations
- **Impact**: Enables persistent access and espionage activities while evading detection through legitimate debugging processes
- **Status**: Active campaign targeting Ukrainian entities with suspected Russian threat actor involvement

## Affected Systems and Products

- **Wing FTP Server**: All versions affected by the path disclosure vulnerability requiring immediate patching
- **Companies House WebFiling Service**: British government agency's company registry system temporarily compromised
- **Python Repositories**: Hundreds of Python projects on GitHub infected through the GlassWorm campaign
- **KakaoTalk Desktop Application**: Used as propagation vector for EndRAT malware distribution
- **Microsoft Edge Browser**: Debugging features exploited by DRILLAPP backdoor for stealth operations
- **macOS Systems**: Targeted by MacSync infostealer through fake AI tool installers
- **Samsung Galaxy Book 4 and Desktop Models**: Affected by C: drive access issues on Windows 11
- **Android Devices**: Accessibility API being abused by malware, prompting security improvements in Android 17

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Deployed through compromised websites to deliver LeakNet ransomware and MacSync infostealer
- **Deno Runtime Exploitation**: In-memory loader techniques using the open-source JavaScript/TypeScript runtime for stealth
- **GitHub Token Theft**: Force-pushing malware into Python repositories using stolen authentication tokens
- **Font-Rendering Attacks**: New technique to hide malicious commands from AI tools through HTML manipulation
- **Phishing Campaigns**: Multi-vector approach using email and instant messaging platforms like KakaoTalk
- **Fake AI Tool Distribution**: Malicious installers masquerading as legitimate artificial intelligence applications
- **LiveChat Platform Abuse**: Social engineering campaigns impersonating PayPal and Amazon through customer support interactions

## Threat Actor Activities

- **LeakNet Ransomware Gang**: Actively deploying ClickFix tactics and innovative Deno-based loaders for initial access and persistence
- **Konni (North Korean APT)**: Conducting spear-phishing campaigns and leveraging KakaoTalk desktop application for malware distribution to specific contacts
- **China-Nexus Threat Actors**: Maintaining long-term persistent access to Southeast Asian military organizations using novel backdoors and familiar evasion techniques
- **GlassWorm Campaign Operators**: Sophisticated supply chain attacks targeting Python ecosystem through stolen GitHub credentials and dependency manipulation
- **Russian-Linked Groups**: Suspected involvement in DRILLAPP backdoor campaign specifically targeting Ukrainian entities for espionage purposes
- **ClickFix Campaign Actors**: Multiple distinct campaigns using the same social engineering technique to distribute various malware families across different platforms