# Exploitation Report

Current cybersecurity threats are dominated by sophisticated supply chain attacks, AI-enhanced malware development, and large-scale data breaches affecting millions of users. North Korean threat actors continue their aggressive campaigns with updated malware variants targeting software repositories, while ransomware groups execute complex multi-victim operations through managed service provider compromises. The emergence of malicious AI tools is lowering the barrier for inexperienced attackers to create functional malware, while traditional attack vectors like Evil Twin WiFi networks and domain takeover vulnerabilities continue to pose significant risks to organizations worldwide.

## Active Exploitation Details

### ShadowV2 Botnet IoT Vulnerabilities
- **Description**: A new Mirai-based botnet malware targeting IoT devices from D-Link, TP-Link, and other vendors with exploits for known vulnerabilities
- **Impact**: Complete device compromise, botnet recruitment, and potential use in DDoS attacks
- **Status**: Actively exploiting known vulnerabilities in IoT devices; patches available but many devices remain unpatched

### Python Package Bootstrap Script Domain Takeover
- **Description**: Vulnerable legacy Python packages on PyPI contain bootstrap scripts that reference expired domains, creating supply chain compromise opportunities
- **Impact**: Attackers can register expired domains and serve malicious code to unsuspecting package users
- **Status**: Multiple packages affected; domain takeover risk remains active for unpatched legacy packages

### Microsoft Teams Guest Access Bypass
- **Description**: Cross-tenant blind spot allows attackers to bypass Microsoft Defender for Office 365 protections via Teams guest access feature
- **Impact**: Complete bypass of enterprise security protections when users join external tenants
- **Status**: Active vulnerability; Microsoft security controls can be circumvented through legitimate guest access functionality

### Solana Transfer Fee Injection
- **Description**: Malicious Chrome extension injects hidden Solana transfer fees into Raydium swap transactions
- **Impact**: Financial theft through cryptocurrency transaction manipulation
- **Status**: Active malware distributed through Chrome Web Store

## Affected Systems and Products

- **Asahi Group Holdings**: Beer production systems affected in September cyberattack impacting 1.9 million individuals
- **D-Link and TP-Link IoT Devices**: Multiple router and IoT device models vulnerable to ShadowV2 botnet exploitation
- **French Football Federation**: Administrative management software used by football clubs compromised
- **GitLab Cloud**: 5.6 million public repositories with over 17,000 exposed secrets across 2,800+ domains
- **Microsoft Windows 11**: Lock screen password option visibility issues in updates since August
- **Microsoft Teams**: Enterprise tenants using guest access features
- **npm Registry**: 197 malicious packages deployed by North Korean actors, 830+ packages in Shai-Hulud v2 campaign
- **OpenAI ChatGPT API**: Customer data exposed through Mixpanel vendor breach
- **Python Package Index (PyPI)**: Legacy packages vulnerable to domain takeover attacks
- **Salesforce/Gainsight**: Customer management applications affected by suspicious activity
- **South Korean MSP**: Financial sector clients affected by Qilin ransomware supply chain attack

## Attack Vectors and Techniques

- **Evil Twin WiFi Networks**: Rogue access points deployed in airports to steal traveler credentials and data
- **Supply Chain Attacks**: Malicious packages injected into npm, Maven, and PyPI repositories for software compromise
- **Domain Takeover**: Registration of expired domains referenced in legacy Python bootstrap scripts
- **Cross-Tenant Exploitation**: Abuse of Microsoft Teams guest access to bypass security controls
- **Browser Extension Malware**: Chrome extensions modified to inject hidden cryptocurrency transfer fees
- **Ransomware via MSP**: Sophisticated supply chain attacks through managed service providers affecting multiple downstream clients
- **AI-Enhanced Code Generation**: Malicious LLMs like WormGPT 4 and KawaiiGPT generating functional ransomware and attack scripts

## Threat Actor Activities

- **North Korean Actors (Contagious Interview Campaign)**: Deployed 197 malicious npm packages spreading updated OtterCookie malware targeting software developers
- **Bloody Wolf**: Expanded Java-based NetSupport RAT attacks in Kyrgyzstan and Uzbekistan using sophisticated delivery mechanisms
- **Qilin Ransomware Group**: Executed "Korean Leaks" operation affecting 28 victims through South Korean MSP compromise
- **Scattered LAPSUS$ Hunters**: Continued mass extortion campaigns targeting major corporations with data theft and public exposure tactics
- **Shai-Hulud Campaign Operators**: Expanded from npm to Maven ecosystem, compromising 830+ packages and exposing thousands of secrets
- **ShadowV2 Botnet Operators**: Leveraged AWS outage as testing opportunity for new Mirai-based IoT botnet infrastructure