# Exploitation Report

The current threat landscape reveals a diverse range of active exploitation activities targeting both enterprise and consumer environments. North Korean threat actors continue their aggressive supply chain attacks through malicious npm packages, deploying updated OtterCookie malware across 197 compromised packages. A new Mirai-based botnet called ShadowV2 is actively exploiting known vulnerabilities in IoT devices from major vendors like D-Link and TP-Link. Additionally, sophisticated supply chain compromises are occurring, including the Qilin ransomware group's attack on South Korean managed service providers that resulted in data theft from 28 victims. Domain takeover vulnerabilities in legacy Python packages pose significant supply chain risks, while malicious Chrome extensions are being used to steal cryptocurrency through hidden transaction injections.

## Active Exploitation Details

### ShadowV2 Botnet Malware
- **Description**: A new Mirai-based botnet malware targeting IoT devices with exploits for known vulnerabilities
- **Impact**: Attackers can compromise IoT devices and incorporate them into botnets for distributed attacks
- **Status**: Currently active, exploiting known vulnerabilities in D-Link, TP-Link, and other vendor devices

### OtterCookie Malware Campaign
- **Description**: Updated malware being distributed through 197 malicious npm packages by North Korean threat actors
- **Impact**: Supply chain compromise allowing code execution and data theft from development environments
- **Status**: Active campaign continuing since last month with new package deployments

### Domain Takeover in Python Packages
- **Description**: Vulnerable legacy Python bootstrap scripts creating domain takeover risks in PyPI packages
- **Impact**: Potential supply chain compromise through domain hijacking affecting Python package installations
- **Status**: Ongoing vulnerability affecting multiple PyPI packages

### Malicious Chrome Extension
- **Description**: Chrome Web Store extension injecting hidden Solana transfer fees into Raydium cryptocurrency swaps
- **Impact**: Financial theft through stealthy transaction manipulation during cryptocurrency exchanges
- **Status**: Active exploitation targeting cryptocurrency users

### Qilin Ransomware Supply Chain Attack
- **Description**: Sophisticated attack targeting South Korean managed service provider leading to multiple victim compromise
- **Impact**: Data theft from 28 organizations through MSP infrastructure compromise
- **Status**: Recent attack resulting in "Korean Leaks" data publication

## Affected Systems and Products

- **IoT Devices**: D-Link and TP-Link routers and networking equipment vulnerable to ShadowV2 botnet exploitation
- **npm Registry**: 197 malicious packages spreading OtterCookie malware targeting JavaScript developers
- **PyPI Packages**: Multiple legacy Python packages with domain takeover vulnerabilities
- **Chrome Browser**: Users of cryptocurrency trading extensions vulnerable to hidden fee injection
- **South Korean MSP**: 28 client organizations affected by Qilin ransomware supply chain attack
- **Microsoft Teams**: Guest access feature creating blind spots in Defender for Office 365 protection
- **GitLab Cloud**: Over 17,000 exposed secrets across 2,800 domains in public repositories

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: North Korean actors flooding npm registry with malicious packages containing OtterCookie malware
- **IoT Vulnerability Exploitation**: ShadowV2 botnet leveraging known vulnerabilities in networking equipment for botnet recruitment
- **Domain Hijacking**: Legacy Python bootstrap scripts enabling takeover attacks through expired or vulnerable domains
- **Browser Extension Abuse**: Malicious Chrome extensions manipulating cryptocurrency transactions through code injection
- **MSP Infrastructure Compromise**: Qilin ransomware group targeting managed service providers for multi-victim attacks
- **Cross-Tenant Exploitation**: Microsoft Teams guest access bypassing security controls when users join external tenants

## Threat Actor Activities

- **North Korean Groups**: Continuing Contagious Interview campaign with 197 new malicious npm packages deploying updated OtterCookie malware
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Orchestrating sophisticated supply chain attack against South Korean MSP resulting in 28-victim data breach
- **Scattered Lapsus$ Hunters**: Conducting mass extortion campaigns against major corporations with data theft and public exposure tactics
- **ShadowV2 Operators**: Deploying new Mirai-based botnet malware to compromise IoT devices and expand attack infrastructure