# Exploitation Report

The cybersecurity landscape this week has been dominated by sophisticated supply chain attacks and actively exploited vulnerabilities targeting critical infrastructure. Most notably, the GlassWorm malware campaign has evolved significantly, now leveraging stolen GitHub tokens to force-push malicious code into hundreds of Python repositories and abusing 72 Open VSX extensions to target developers. CISA has flagged a Wing FTP Server vulnerability as actively exploited in attacks that may lead to remote code execution. Additionally, threat actors are conducting targeted campaigns against Ukrainian entities using the DRILLAPP backdoor, while Chinese hackers continue their espionage operations against Southeast Asian military organizations. Supply chain compromises have expanded beyond traditional vectors, with the AppsFlyer Web SDK being hijacked to spread cryptocurrency-stealing JavaScript code.

## Active Exploitation Details

### Wing FTP Server Vulnerability
- **Description**: A security flaw in Wing FTP Server that is being actively exploited in the wild
- **Impact**: Attackers can potentially chain this vulnerability with other exploits to achieve remote code execution on affected systems
- **Status**: CISA has issued warnings to U.S. government agencies to secure their Wing FTP Server instances against this actively exploited vulnerability

### GlassWorm Supply Chain Attack
- **Description**: An evolved malware campaign that uses stolen GitHub tokens to inject malicious code into Python repositories and abuses Open VSX extensions
- **Impact**: Compromises software development environments, potentially affecting downstream users of infected packages and extensions
- **Status**: Active campaign with dozens of malicious extensions identified and hundreds of Python repositories compromised

### AppsFlyer Web SDK Hijack
- **Description**: Supply chain attack where the AppsFlyer Web SDK was temporarily compromised with malicious JavaScript code
- **Impact**: Cryptocurrency theft from users of websites implementing the compromised SDK
- **Status**: Temporary compromise resolved, but demonstrated supply chain vulnerability

### Companies House Security Flaw
- **Description**: Security vulnerability in the UK Companies House WebFiling service that exposed business data
- **Impact**: Unauthorized access to sensitive business information and company registry data
- **Status**: WebFiling service was taken offline and has been restored after security fixes were implemented

## Affected Systems and Products

- **Wing FTP Server**: Specific versions not detailed, but CISA warning indicates widespread deployment in government environments
- **Python Repositories**: Hundreds of repositories compromised through stolen GitHub tokens in GlassWorm campaign
- **Open VSX Extensions**: 72 malicious extensions identified targeting Visual Studio Code developers
- **AppsFlyer Web SDK**: Temporary compromise affecting websites using this analytics SDK
- **UK Companies House WebFiling**: Government registry service exposing business data
- **Samsung Galaxy Connect App**: Causing Windows 11 C: drive access issues on specific Galaxy Book 4 and desktop models
- **Windows 11 Enterprise**: RRAS (Routing and Remote Access Service) vulnerability requiring out-of-band hotpatch
- **Steam Gaming Platform**: Eight malicious games identified spreading malware to users

## Attack Vectors and Techniques

- **GitHub Token Abuse**: Attackers using stolen authentication tokens to force-push malicious code into legitimate repositories
- **Supply Chain Poisoning**: Injection of malicious code into trusted software distribution channels including package managers and extension repositories
- **Social Engineering via LiveChat**: Impersonation of PayPal and Amazon customer support to harvest credit card and personal data
- **ClickFix Campaigns**: Fake AI tool installers spreading MacSync infostealer on macOS systems
- **Microsoft Edge Debugging Abuse**: DRILLAPP backdoor leveraging browser debugging features for stealth espionage
- **Steam Game Distribution**: Malicious games uploaded to legitimate gaming platform for malware distribution
- **JavaScript SDK Injection**: Cryptocurrency-stealing code injected into widely-used web development frameworks

## Threat Actor Activities

- **GlassWorm Operators**: Conducting sophisticated supply chain attacks targeting Python developers and VS Code users through multiple attack vectors including GitHub repository compromise and malicious extension distribution
- **Russian-linked Groups**: Targeting Ukrainian entities with DRILLAPP backdoor using Microsoft Edge debugging features for covert espionage operations
- **Chinese State-sponsored Actors**: Conducting long-term espionage campaign against Southeast Asian military organizations using AppleChris and MemFun malware, with operations dating back to at least 2020
- **ClickFix Campaign Operators**: Running three distinct campaigns spreading MacSync infostealer through fake AI tool installers targeting macOS users
- **LiveChat Scammers**: Impersonating major e-commerce platforms to conduct social engineering attacks for financial data theft
- **Steam Malware Distributors**: Uploading malicious games to Steam platform for malware distribution, prompting FBI investigation