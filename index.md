# Exploitation Report

The current threat landscape is dominated by several critical exploitation activities, with CVE-2025-55182 being actively exploited in a large-scale credential harvesting campaign affecting 766 Next.js hosts. Simultaneously, sophisticated supply chain attacks are targeting high-profile packages like Axios through social engineering, while North Korean threat actors continue their aggressive campaigns with a $285 million cryptocurrency theft and coordinated attacks against European government entities. The emergence of cookie-controlled PHP web shells and advanced mobile malware variants demonstrates the evolving sophistication of exploitation techniques across multiple platforms.

## Active Exploitation Details

### React2Shell Vulnerability
- **Description**: A vulnerability in Next.js hosts being exploited for large-scale credential harvesting operations
- **Impact**: Attackers can steal database credentials, SSH private keys, and Amazon Web Services credentials from compromised systems
- **Status**: Actively exploited against 766 Next.js hosts in ongoing campaign
- **CVE ID**: CVE-2025-55182

### DarkSword iOS Vulnerability
- **Description**: A severe mobile OS-cracking tool affecting iOS systems
- **Impact**: Complete compromise of iOS devices, allowing attackers to bypass security controls
- **Status**: Recently patched by Apple for iOS 18, breaking their typical patching precedent

### Axios npm Package Supply Chain Compromise
- **Description**: Social engineering attack against the maintainer of the popular Axios npm package
- **Impact**: Potential code execution and data theft across applications using the compromised package
- **Status**: Confirmed supply chain attack orchestrated by North Korean threat actors

### Durable Nonce Exploitation in Solana
- **Description**: Advanced attack targeting Solana-based decentralized exchange Drift Protocol
- **Impact**: $285 million financial loss through exploitation of Security Council administrative powers
- **Status**: Completed attack with confirmed North Korean attribution

## Affected Systems and Products

- **Next.js Hosts**: 766 confirmed compromised systems affected by credential harvesting campaign
- **iOS Devices**: Systems vulnerable to DarkSword exploitation tool, now patched for iOS 18
- **Linux Servers**: Targeted by cookie-controlled PHP web shells for persistent access
- **npm Ecosystem**: Applications using compromised Axios package at risk of supply chain attacks
- **Solana Protocol**: Drift decentralized exchange lost $285 million in sophisticated attack
- **European Government Systems**: Multiple diplomatic and government organizations targeted by TA416
- **Mobile Platforms**: iOS and Android apps on official stores compromised with SparkCat malware
- **Zendesk Platform**: Third-party breach affecting Hims & Hers customer support data
- **Windows Systems**: 254 servers locked in internal extortion plot by malicious employee

## Attack Vectors and Techniques

- **Social Engineering**: Highly-targeted campaigns against package maintainers and cryptocurrency platform administrators
- **Supply Chain Attacks**: Compromise of trusted software packages and dependencies to reach downstream targets
- **Cookie-Controlled Web Shells**: PHP-based backdoors using HTTP cookies as control channels for stealth persistence
- **OAuth-Based Phishing**: Advanced phishing campaigns targeting European government credentials
- **Mobile App Store Infiltration**: Malicious applications bypassing security checks on official app stores
- **Administrative Privilege Abuse**: Internal threats exploiting elevated access for extortion purposes
- **Credential Harvesting**: Large-scale operations targeting sensitive authentication data and private keys

## Threat Actor Activities

- **UNC1069 (North Korean)**: Orchestrated sophisticated social engineering campaign against Axios maintainer, leading to npm supply chain compromise
- **TA416 (China-linked)**: Renewed targeting of European government and diplomatic organizations since mid-2025 using PlugX malware and OAuth-based phishing
- **TeamPCP**: Supply chain attacks expanding in scope with involvement from ShinyHunters and Lapsus$ groups, affecting European Commission and 30 EU entities
- **Qilin Ransomware Group**: Claimed responsibility for attack against German political party Die Linke, threatening sensitive data leak
- **SparkCat Operators**: Deployed new malware variants through official iOS and Android app stores targeting cryptocurrency wallet recovery phrases
- **DPRK-linked Actors**: Multiple sophisticated operations including $285 million Drift Protocol theft and various social engineering campaigns