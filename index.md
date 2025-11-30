# Exploitation Report

Current security intelligence reveals a significant surge in sophisticated supply chain attacks and enterprise-targeted campaigns. North Korean threat actors continue their aggressive npm package poisoning operations with 197 new malicious packages delivering updated OtterCookie malware, while the Shai-Hulud v2 campaign has expanded from npm to Maven ecosystems, compromising over 830 packages. Critical infrastructure remains under threat as the ShadowV2 botnet exploits known vulnerabilities in IoT devices from major vendors, and the Qilin ransomware group executed a sophisticated supply chain attack against South Korea's financial sector through MSP compromise. Enterprise environments face increasing risks from malicious AI-powered tools, cross-tenant security bypasses in Microsoft Teams, and domain takeover vulnerabilities in legacy Python packages.

## Active Exploitation Details

### ShadowV2 Mirai-based Botnet
- **Description**: New botnet malware targeting IoT devices using known vulnerability exploits against D-Link, TP-Link, and other vendor devices
- **Impact**: Device compromise for botnet recruitment, potential DDoS participation, and lateral network movement
- **Status**: Active exploitation of known vulnerabilities in IoT devices, leveraged AWS outage as testing opportunity

### OtterCookie Malware via npm Packages
- **Description**: North Korean threat actors deploying 197 malicious npm packages in continuation of Contagious Interview campaign
- **Impact**: Supply chain compromise targeting developers, credential theft, and system infiltration
- **Status**: Ongoing active campaign with continuous package uploads to npm registry

### Shai-Hulud v2 Supply Chain Attack
- **Description**: Multi-ecosystem supply chain attack compromising over 830 npm packages and expanding to Maven repositories
- **Impact**: Mass compromise of development environments and exposure of thousands of secrets
- **Status**: Active campaign spreading across multiple package management ecosystems

### Microsoft Teams Cross-Tenant Security Bypass
- **Description**: Guest access feature allows attackers to bypass Microsoft Defender for Office 365 protections when users join external tenants
- **Impact**: Security control evasion, potential data exfiltration, and compromise of enterprise protection mechanisms
- **Status**: Active vulnerability affecting Microsoft Teams guest access functionality

### Chrome Extension Solana Injection Attack
- **Description**: Malicious Chrome Web Store extension injecting hidden Solana transfer fees into Raydium swap transactions
- **Impact**: Cryptocurrency theft through transaction manipulation and fee injection
- **Status**: Active malicious extension deployed on Chrome Web Store

### Legacy Python Package Domain Takeover
- **Description**: Vulnerable bootstrap scripts in legacy Python packages creating domain takeover risks in PyPI ecosystem
- **Impact**: Supply chain compromise potential through domain hijacking and malicious package injection
- **Status**: Vulnerable code identified in multiple legacy packages

## Affected Systems and Products

- **IoT Devices**: D-Link and TP-Link devices vulnerable to ShadowV2 botnet exploitation
- **npm Registry**: 197 malicious packages targeting JavaScript developers
- **Maven Repository**: Expanded Shai-Hulud campaign affecting Java development ecosystem
- **PyPI Packages**: Legacy Python packages with domain takeover vulnerabilities
- **Microsoft Teams**: Enterprise tenants using guest access functionality
- **Chrome Browser**: Users of malicious extensions from Chrome Web Store
- **Salesforce/Gainsight**: Customer management platforms affected by security incidents
- **GitLab Cloud**: 5.6 million public repositories exposing over 17,000 secrets
- **South Korean Financial Sector**: MSP supply chain attack affecting 28 organizations

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Mass deployment of malicious packages across npm and Maven ecosystems
- **IoT Exploitation**: Leveraging known vulnerabilities in consumer and enterprise IoT devices
- **Cross-Tenant Abuse**: Exploiting Microsoft Teams guest access to bypass security controls
- **Browser Extension Malware**: Cryptocurrency transaction manipulation through malicious Chrome extensions
- **Social Engineering**: North Korean Contagious Interview campaign targeting developers
- **Domain Takeover**: Legacy package vulnerabilities enabling supply chain compromise
- **MSP Compromise**: Targeting managed service providers for downstream victim access
- **Evil Twin WiFi**: Airport-based WiFi attacks for credential harvesting
- **AI-Powered Malware**: LLM-generated malicious code for evasion and automation

## Threat Actor Activities

- **North Korean APT Groups**: Continued Contagious Interview campaign with 197 new npm packages deploying OtterCookie malware
- **Bloody Wolf**: Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Sophisticated supply chain attack against South Korean financial sector through MSP breach affecting 28 victims
- **Scattered LAPSUS$ Hunters**: Mass extortion campaigns targeting major corporations with data theft operations
- **ShadowV2 Operators**: IoT botnet development and deployment targeting consumer devices
- **Shai-Hulud Campaign**: Multi-ecosystem supply chain attacks compromising development environments
- **Cryptocurrency Scammers**: Chrome extension deployment for Solana transaction manipulation