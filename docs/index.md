# Exploitation Report

Critical exploitation activity is currently centered around several key vulnerabilities and attack campaigns. CISA has flagged a Wing FTP Server vulnerability as actively exploited, highlighting its addition to the Known Exploited Vulnerabilities catalog due to evidence of ongoing attacks. Sophisticated supply chain attacks are targeting developers through the GlassWorm campaign, which has evolved to compromise Python repositories via stolen GitHub tokens and abuse Open VSX extensions. Chinese state-sponsored threat actors continue persistent espionage operations against Southeast Asian military organizations using custom malware, while the AppsFlyer Web SDK was temporarily hijacked to distribute cryptocurrency-stealing code. Additionally, new social engineering campaigns are leveraging trusted platforms like LiveChat to conduct phishing operations targeting sensitive financial data.

## Active Exploitation Details

### Wing FTP Server Path Disclosure Vulnerability
- **Description**: A medium-severity security flaw in Wing FTP Server that allows attackers to leak server paths
- **Impact**: Unauthorized disclosure of server directory structures and file paths, potentially enabling reconnaissance for further attacks
- **Status**: Actively exploited in the wild according to CISA, added to Known Exploited Vulnerabilities catalog

### AppsFlyer Web SDK Supply Chain Attack
- **Description**: Temporary hijacking of the AppsFlyer Web SDK with malicious JavaScript code injection
- **Impact**: Cryptocurrency theft from users of websites implementing the compromised SDK
- **Status**: Supply chain attack successfully executed, SDK has been remediated

### Windows 11 RRAS Remote Code Execution Flaw
- **Description**: Security vulnerability affecting Windows 11 Enterprise's Routing and Remote Access Service
- **Impact**: Remote code execution capabilities for attackers
- **Status**: Microsoft released out-of-band hotpatch to address the vulnerability

## Affected Systems and Products

- **Wing FTP Server**: File transfer protocol server software with path disclosure vulnerability
- **Python Repositories**: Hundreds of Python projects targeted through stolen GitHub tokens in GlassWorm campaign
- **Open VSX Extensions**: 72 malicious extensions uploaded to target developers
- **AppsFlyer Web SDK**: Temporarily compromised with crypto-stealing JavaScript
- **Windows 11 Enterprise**: RRAS component affected by remote code execution flaw
- **Samsung Galaxy Book 4**: Specific models experiencing C: drive access issues after February 2026 updates
- **Steam Gaming Platform**: Eight malicious games distributed containing malware
- **Companies House WebFiling**: British government service affected by data exposure flaw

## Attack Vectors and Techniques

- **Supply Chain Compromise**: GlassWorm campaign targeting Python repositories and VSX extensions to reach developers
- **Token Theft and Force-Push**: Stolen GitHub tokens used to inject malware directly into legitimate repositories
- **Social Engineering via LiveChat**: Attackers impersonating PayPal and Amazon support to harvest credit card data
- **ClickFix Campaigns**: Fake AI tool installers distributing MacSync infostealer on macOS systems
- **Microsoft Edge Debugging Abuse**: DRILLAPP backdoor leveraging browser debugging features for stealth operations
- **Steam Game Distribution**: Malicious games uploaded to gaming platform for malware distribution
- **Device Wiping**: Stryker attack remotely wiped tens of thousands of employee devices without traditional malware

## Threat Actor Activities

- **China-Linked APT Groups**: Long-term espionage campaign against Southeast Asian military organizations using AppleChris and MemFun malware, maintaining persistent access since at least 2020
- **Russian-Linked Actors**: Suspected involvement in DRILLAPP backdoor campaign targeting Ukrainian entities
- **GlassWorm Operators**: Sophisticated supply chain attackers targeting developer ecosystems through multiple vectors including GitHub repositories and VSX extensions
- **Financial Cybercriminals**: Groups conducting cryptocurrency theft through compromised web SDKs and phishing operations
- **Steam Malware Distributors**: Criminal actors uploading eight malicious games to Steam platform, now subject to FBI investigation