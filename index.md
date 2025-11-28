# Exploitation Report

Multiple critical security incidents highlight active exploitation campaigns targeting enterprise infrastructure and IoT devices. The Qilin ransomware group orchestrated a sophisticated supply chain attack against South Korean financial institutions through MSP compromise, while the ShadowV2 botnet exploited IoT device vulnerabilities during AWS outages for testing purposes. Additional threats include the Bloody Wolf threat actor expanding NetSupport RAT deployments across Central Asia, RomCom leveraging SocGholish fake update campaigns, and widespread supply chain attacks targeting npm and Maven package repositories. These incidents demonstrate escalating sophistication in exploitation techniques, particularly through compromised third-party vendors and automated botnet operations.

## Active Exploitation Details

### Qilin Ransomware Supply Chain Attack
- **Description**: Sophisticated supply chain attack targeting South Korean MSP infrastructure leading to compromise of 28 victim organizations
- **Impact**: Full network compromise, data exfiltration, and ransomware deployment across multiple financial sector entities
- **Status**: Active campaign identified as "Korean Leaks" data heist operation

### ShadowV2 Mirai-based Botnet
- **Description**: New Mirai variant targeting IoT devices from D-Link, TP-Link, and other vendors with known vulnerability exploits
- **Impact**: Device compromise, botnet recruitment, and potential DDoS capabilities
- **Status**: Actively exploiting known vulnerabilities in IoT infrastructure

### ASUS AiCloud Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in ASUS routers with AiCloud enabled
- **Impact**: Complete router compromise and potential network lateral movement
- **Status**: Firmware patches released to address nine security vulnerabilities including critical auth bypass

### Node-forge Signature Verification Bypass
- **Description**: Vulnerability in popular JavaScript cryptography library allowing signature verification bypass
- **Impact**: Authentication bypass and potential cryptographic security circumvention
- **Status**: Fix available for signature verification flaw

### Shai-Hulud v2 Supply Chain Attack
- **Description**: Second wave supply chain attack expanding from npm to Maven ecosystem
- **Impact**: Compromise of over 830 packages, exposure of thousands of secrets and credentials
- **Status**: Active campaign spreading across multiple package repositories

## Affected Systems and Products

- **ASUS Routers**: AiCloud-enabled routers affected by critical authentication bypass vulnerability
- **IoT Devices**: D-Link and TP-Link devices targeted by ShadowV2 botnet malware
- **South Korean Financial Sector**: Multiple institutions compromised through MSP supply chain attack
- **npm and Maven Repositories**: Over 830 packages compromised in Shai-Hulud v2 campaign
- **Node-forge Library**: Popular JavaScript cryptography package with signature bypass flaw
- **Chrome Extensions**: Malicious extensions injecting hidden Solana transfer fees
- **London Government Systems**: Royal Borough of Kensington and Chelsea and Westminster City Council experiencing disruptions

## Attack Vectors and Techniques

- **Supply Chain Compromise**: MSP infrastructure targeting for downstream victim access
- **Fake Software Updates**: SocGholish JavaScript loader delivering Mythic Agent malware
- **IoT Vulnerability Exploitation**: Automated exploitation of known device vulnerabilities
- **Package Repository Poisoning**: Malicious package injection into npm and Maven ecosystems
- **Social Engineering**: NetSupport RAT delivery through Java-based attack campaigns
- **Browser Extension Manipulation**: Cryptocurrency transaction hijacking through malicious Chrome extensions
- **Vendor Compromise**: Third-party analytics provider breaches affecting downstream customers

## Threat Actor Activities

- **Qilin Ransomware Group**: Orchestrating sophisticated supply chain attacks against Korean financial sector through MSP compromise
- **Bloody Wolf**: Expanding Java-based NetSupport RAT campaigns targeting Kyrgyzstan and Uzbekistan since June 2025
- **RomCom**: First documented use of SocGholish fake update attacks to deliver Mythic Agent malware
- **ShadowV2 Operators**: Leveraging AWS outages as testing opportunities for new botnet malware
- **Shai-Hulud Attackers**: Scaling supply chain attacks across multiple package repositories with credential harvesting focus
- **Scattered LAPSUS$ Hunters**: Continuing mass extortion campaigns against major corporations with public data exposure tactics