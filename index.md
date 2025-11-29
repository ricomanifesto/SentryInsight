# Exploitation Report

The cybersecurity landscape continues to face significant threats from multiple fronts, with supply chain attacks emerging as a dominant threat vector. North Korean threat actors have intensified their malicious package distribution campaigns, flooding npm repositories with hundreds of malicious packages while expanding their operations to target PyPI and Maven ecosystems. Meanwhile, sophisticated botnet operations are exploiting known IoT vulnerabilities, and social engineering attacks are leveraging AI-powered tools to enhance their effectiveness. Critical infrastructure targets including financial services and managed service providers are experiencing targeted ransomware campaigns, demonstrating the evolving sophistication of threat actors in 2024.

## Active Exploitation Details

### ShadowV2 Botnet IoT Device Exploitation
- **Description**: A new Mirai-based botnet malware targeting IoT devices from multiple vendors including D-Link and TP-Link
- **Impact**: Compromised IoT devices can be incorporated into botnets for DDoS attacks and other malicious activities
- **Status**: Active exploitation of known vulnerabilities in IoT devices

### Domain Takeover Vulnerabilities in PyPI Packages
- **Description**: Legacy Python bootstrap scripts contain vulnerable code that could enable supply chain compromise through domain takeover
- **Impact**: Attackers could potentially compromise multiple PyPI packages and their dependent systems
- **Status**: Vulnerabilities discovered in legacy packages, posing ongoing supply chain risk

### Forge Library Signature Verification Bypass
- **Description**: Vulnerability in the node-forge JavaScript cryptography library allowing bypass of signature verifications
- **Impact**: Attackers can craft data that appears valid, compromising cryptographic integrity
- **Status**: Fixed in updated versions of the library

### Microsoft Teams Cross-Tenant Security Bypass
- **Description**: Guest access feature in Teams can bypass Microsoft Defender for Office 365 protections when users join external tenants
- **Impact**: Attackers can evade security protections through cross-tenant vulnerabilities
- **Status**: Security researcher disclosure, mitigation strategies being developed

## Affected Systems and Products

- **IoT Devices**: D-Link and TP-Link devices vulnerable to ShadowV2 botnet exploitation
- **Python Package Index (PyPI)**: Legacy packages with domain takeover vulnerabilities
- **npm Registry**: 197+ malicious packages distributed by North Korean actors
- **Maven Ecosystem**: Expansion of Shai-Hulud v2 supply chain attack from npm
- **Node-forge Library**: JavaScript cryptography library with signature verification flaws
- **Microsoft Teams**: Cross-tenant security bypass affecting Office 365 environments
- **GitLab Cloud**: 5.6 million public repositories scanned, 17,000+ exposed secrets discovered
- **Chrome Web Store**: Malicious extensions injecting hidden Solana transaction fees

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: North Korean actors flooding package repositories with malicious code
- **Evil Twin WiFi Networks**: Physical proximity attacks targeting airport and travel environments
- **Social Engineering**: AI-powered malicious LLMs generating sophisticated attack scripts
- **Credential Theft**: Targeting exposed secrets in public code repositories
- **Cross-Tenant Exploitation**: Leveraging Microsoft Teams guest access to bypass security controls
- **Domain Takeover**: Exploiting legacy bootstrap scripts in Python packages
- **Botnet Recruitment**: IoT device compromise for distributed attack infrastructure

## Threat Actor Activities

- **North Korean Contagious Interview Campaign**: Deployed 197+ npm packages spreading OtterCookie malware, expanding operations to target software developers
- **Bloody Wolf**: Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2024
- **Qilin Ransomware Group**: Sophisticated supply chain attack on South Korean MSP leading to 28-victim "Korean Leaks" data heist
- **Scattered LAPSUS$ Hunters**: Mass data exfiltration and extortion campaigns targeting major corporations throughout 2024
- **Shai-Hulud v2 Operators**: Expanded supply chain attack from npm to Maven ecosystem, compromising 830+ packages
- **Airport WiFi Attackers**: Seven-year prison sentence handed down for operating evil twin networks targeting travelers
- **Cryptocurrency Fraudsters**: Chrome extension operators injecting hidden Solana transfer fees into legitimate transactions