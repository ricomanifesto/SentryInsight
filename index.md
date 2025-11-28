# Exploitation Report

The cybersecurity landscape is experiencing significant exploitation activity across multiple vectors, with threat actors leveraging both traditional attack methods and emerging AI-powered techniques. Critical vulnerabilities are being actively exploited in ASUS routers, IoT devices, and cryptographic libraries, while sophisticated supply chain attacks target software repositories. Notable campaigns include Bloody Wolf's expansion of NetSupport RAT operations in Central Asia, ShadowV2 botnet targeting IoT infrastructure, and Qilin ransomware conducting large-scale supply chain attacks affecting South Korean financial institutions. The emergence of AI-enhanced malware and the exploitation of script injection vulnerabilities in authentication systems represent evolving threats requiring immediate attention.

## Active Exploitation Details

### ASUS AiCloud Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass flaw affecting ASUS routers with AiCloud functionality enabled
- **Impact**: Complete authentication bypass allowing unauthorized access to router configurations and network resources
- **Status**: Firmware patches released by ASUS to address nine security vulnerabilities including this critical flaw

### IoT Device Vulnerabilities (ShadowV2 Botnet Campaign)
- **Description**: Multiple known vulnerabilities in D-Link, TP-Link, and other IoT device vendors being exploited by Mirai-based botnet malware
- **Impact**: Remote code execution leading to device compromise and botnet recruitment
- **Status**: Active exploitation observed with ShadowV2 malware using AWS outage as testing opportunity

### Node-forge Signature Verification Bypass
- **Description**: Vulnerability in the popular 'node-forge' JavaScript cryptography library allowing signature verification bypass
- **Impact**: Attackers can craft data that appears valid, bypassing cryptographic security controls
- **Status**: Fix released for the vulnerability

### Memory Encryption Bypass Vulnerabilities
- **Description**: Hardware-based vulnerabilities in AMD and Intel confidential computing protections
- **Impact**: Circumvention of scalable memory encryption using inexpensive hardware modules
- **Status**: Research demonstrates practical exploitation methods

## Affected Systems and Products

- **ASUS Routers**: AiCloud-enabled routers vulnerable to authentication bypass
- **IoT Devices**: D-Link and TP-Link devices targeted by ShadowV2 botnet malware
- **Node-forge Library**: JavaScript cryptography library with signature verification weakness
- **AMD/Intel Processors**: Memory encryption features vulnerable to hardware-based bypass
- **Microsoft Entra ID**: Authentication system targeted by script injection attacks
- **Gainsight Applications**: Customer success platform experiencing suspicious activity
- **OpenAI API**: Customer data exposed through Mixpanel vendor breach
- **Chrome Extensions**: Malicious extensions injecting hidden cryptocurrency transfers
- **npm and Maven Repositories**: Software packages compromised in Shai-Hulud supply chain attack

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Shai-Hulud campaign compromising 830+ npm packages and expanding to Maven ecosystem
- **Script Injection**: Unauthorized scripts targeting Microsoft Entra ID authentication flows
- **SocGholish Fake Updates**: JavaScript loader delivering Mythic Agent malware via fake browser updates
- **NetSupport RAT Deployment**: Java-based remote access trojans distributed by Bloody Wolf threat actor
- **Botnet Exploitation**: ShadowV2 leveraging known IoT vulnerabilities for device recruitment
- **Cryptocurrency Theft**: Malicious Chrome extensions injecting hidden Solana transfer fees
- **AI-Enhanced Malware**: Integration of large language models for runtime evasion and code augmentation
- **Hardware-Based Attacks**: Physical modules bypassing memory encryption protections

## Threat Actor Activities

- **Bloody Wolf**: Expanding NetSupport RAT campaigns targeting Kyrgyzstan and Uzbekistan since June 2025
- **RomCom Group**: Using SocGholish fake update attacks to deliver Mythic Agent malware to U.S. civil engineering companies
- **Qilin Ransomware**: Conducting sophisticated supply chain attack against South Korean MSP affecting 28 victims in "Korean Leaks" operation
- **Scattered LAPSUS$ Hunters**: Continuing mass extortion campaigns against major corporations with regular data theft operations
- **ShadowV2 Operators**: Deploying Mirai-based botnet malware targeting IoT infrastructure during AWS outage testing
- **Shai-Hulud Campaign**: Second wave attackers compromising software supply chain across npm and Maven repositories
- **Iranian Threat Actors**: Deploying "cyber-enabled kinetic targeting" in coordination with missile attacks