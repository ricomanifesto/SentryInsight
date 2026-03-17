# Exploitation Report

CISA has flagged a critical Wing FTP Server vulnerability for active exploitation, adding it to the Known Exploited Vulnerabilities catalog due to evidence of in-the-wild attacks. This vulnerability enables path disclosure attacks and may be chained with other exploits for remote code execution. Meanwhile, sophisticated supply chain attacks are targeting developers through the GlassWorm campaign, which has evolved to abuse GitHub tokens and Visual Studio Code extensions. China-nexus threat actors continue extensive espionage operations against Southeast Asian military organizations using novel backdoors, while various social engineering campaigns leverage legitimate services like LiveChat to steal credentials and personal data.

## Active Exploitation Details

### Wing FTP Server Path Disclosure Vulnerability
- **Description**: A medium-severity security flaw in Wing FTP Server that allows attackers to leak server paths and potentially chain with other vulnerabilities
- **Impact**: Path disclosure that can be leveraged in remote code execution attack chains
- **Status**: Actively exploited in the wild, CISA has mandated federal agencies secure their instances

### GlassWorm Supply Chain Campaign
- **Description**: Multi-vector supply chain attack targeting Python developers through compromised GitHub repositories and Visual Studio Code extensions
- **Impact**: Code injection into hundreds of Python repositories, credential theft, and development environment compromise
- **Status**: Ongoing campaign with evolving techniques including stolen GitHub token abuse and Open VSX registry manipulation

### AppsFlyer Web SDK Supply Chain Attack
- **Description**: Temporary compromise of the AppsFlyer Web SDK with malicious JavaScript code
- **Impact**: Cryptocurrency theft from applications using the compromised SDK
- **Status**: Incident contained but demonstrates supply chain vulnerability risks

## Affected Systems and Products

- **Wing FTP Server**: All versions vulnerable to path disclosure attacks, government agencies specifically at risk
- **Python Repositories**: Hundreds of GitHub repositories compromised through stolen tokens and force-push attacks
- **Visual Studio Code Extensions**: 72 malicious extensions distributed through Open VSX registry targeting developers
- **AppsFlyer Web SDK**: Temporarily compromised with crypto-stealing JavaScript code
- **Windows 11 Samsung PCs**: Galaxy Book 4 and desktop models experiencing C: drive access issues after security updates
- **Southeast Asian Military Systems**: Targeted by Chinese hackers using AppleChris and MemFun malware
- **Steam Gaming Platform**: Eight malicious games identified containing malware, FBI investigation ongoing
- **UK Companies House**: WebFiling service affected by security flaw exposing business data

## Attack Vectors and Techniques

- **GitHub Token Theft**: Stolen authentication tokens used to force-push malware into legitimate repositories
- **Extension Poisoning**: Malicious Visual Studio Code extensions distributed through official registries
- **Social Engineering via LiveChat**: Impersonation of PayPal and Amazon through customer support interactions
- **ClickFix Campaigns**: Fake AI tool installers delivering MacSync infostealer to macOS users  
- **Microsoft Edge Debugging Abuse**: DRILLAPP backdoor leveraging Edge debugging features for stealth operations
- **Supply Chain Compromise**: Direct injection of malicious code into widely-used development tools and SDKs
- **Gaming Platform Abuse**: Distribution of malware through legitimate Steam game titles

## Threat Actor Activities

- **China-Nexus Groups**: Long-term espionage campaign against Southeast Asian military organizations using AppleChris and MemFun backdoors, maintaining persistent access since at least 2020
- **Russian-Linked Actors**: Targeting Ukrainian entities with DRILLAPP backdoor, abusing Microsoft Edge debugging capabilities for stealth operations
- **GlassWorm Operators**: Sophisticated supply chain attackers evolving tactics to hide in dependencies and abuse legitimate development platforms
- **Steam Malware Distributors**: Cybercriminals using gaming platform to distribute malware, prompting FBI investigation and victim identification efforts
- **Financial Fraud Groups**: Leveraging legitimate customer support platforms like LiveChat to conduct credential harvesting and payment fraud campaigns