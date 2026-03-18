# Exploitation Report

Current threat landscape shows significant active exploitation across multiple attack vectors, with several critical vulnerabilities being leveraged in the wild. Apple has deployed its first Background Security Improvements update to address a WebKit vulnerability (CVE-2026-20643) affecting iOS, macOS, and iPadOS devices. CISA has flagged a Wing FTP Server vulnerability as actively exploited, posing risks for remote code execution attacks. Multiple sophisticated malware campaigns are ongoing, including the evolved GlassWorm supply-chain attacks targeting GitHub repositories and the LeakNet ransomware group's adoption of ClickFix social engineering techniques. Additionally, North Korean threat actors are actively deploying EndRAT malware through phishing campaigns while leveraging KakaoTalk for lateral propagation.

## Active Exploitation Details

### WebKit Vulnerability in Apple Devices
- **Description**: Critical WebKit vulnerability affecting iOS, iPadOS, and macOS systems that required Apple's first Background Security Improvements update
- **Impact**: Potential code execution and system compromise through web-based attacks
- **Status**: Patched via Background Security Improvements update without requiring full OS upgrade
- **CVE ID**: CVE-2026-20643

### Wing FTP Server Path Disclosure Vulnerability
- **Description**: Medium-severity security flaw in Wing FTP Server that allows path disclosure and server information leakage
- **Impact**: Can be chained with other vulnerabilities to achieve remote code execution
- **Status**: Actively exploited in attacks, flagged by CISA for immediate patching

### GlassWorm Supply-Chain Malware
- **Description**: Sophisticated malware campaign targeting software development environments through compromised GitHub tokens
- **Impact**: Code injection into Python repositories, malicious package distribution, and development environment compromise
- **Status**: Actively ongoing with evolved evasion techniques and dependency hiding capabilities

### Companies House Security Flaw
- **Description**: Security vulnerability in UK's Companies House WebFiling service that exposed business registration data
- **Impact**: Unauthorized access to sensitive business information and company records
- **Status**: Service temporarily taken offline for remediation, now restored

## Affected Systems and Products

- **Apple Devices**: iOS, iPadOS, and macOS systems vulnerable to WebKit attacks
- **Wing FTP Server**: All versions susceptible to path disclosure vulnerability
- **GitHub Repositories**: Hundreds of Python repositories compromised through stolen tokens
- **VSCode Extensions**: Malicious extensions distributed through OpenVSX marketplace
- **npm Packages**: Supply-chain attacks targeting JavaScript package ecosystem
- **Companies House WebFiling**: UK business registration platform experiencing data exposure

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: LeakNet ransomware using fake error prompts on compromised websites to trick users into executing malware
- **Deno Runtime Loader**: In-memory malware deployment using legitimate JavaScript/TypeScript runtime for evasion
- **Font-Rendering Attacks**: New technique to hide malicious commands from AI tools using HTML font manipulation
- **KakaoTalk Propagation**: North Korean actors using legitimate messaging platform for malware distribution
- **GitHub Token Abuse**: Force-pushing malware into repositories using stolen authentication tokens
- **BYOVD Techniques**: Warlock ransomware group employing Bring Your Own Vulnerable Driver methods for privilege escalation

## Threat Actor Activities

- **LeakNet Ransomware Group**: Deploying stealthy attacks through compromised websites using ClickFix techniques and Deno runtime loaders for payload delivery
- **North Korean Konni Group**: Conducting spear-phishing campaigns to deploy EndRAT malware and abuse KakaoTalk desktop applications for lateral movement
- **GlassWorm Operators**: Executing coordinated supply-chain attacks across GitHub, npm, and VSCode ecosystems with improved dependency hiding techniques
- **Warlock Ransomware Group**: Enhancing post-exploitation capabilities with stealthier cross-network activities and advanced BYOVD techniques
- **China-Nexus APT Groups**: Maintaining persistent access in Southeast Asian military organizations through novel backdoors and familiar evasion methods
- **Credential Theft Campaigns**: Industrialized infostealer malware operations with AI-enabled social engineering targeting authentication systems