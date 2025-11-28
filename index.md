# Exploitation Report

Current threat landscape shows significant exploitation activity across multiple attack vectors, with threat actors leveraging both known vulnerabilities and novel techniques. Key concerns include the ShadowV2 botnet targeting IoT devices with exploits for known vulnerabilities, signature verification bypass issues in the popular node-forge JavaScript library, critical authentication bypass vulnerabilities in ASUS AiCloud routers, and sophisticated supply chain attacks including the Qilin ransomware campaign against South Korean MSPs and the expanded Shai-Hulud campaign targeting npm and Maven repositories. Additionally, threat actors are increasingly incorporating AI and LLMs into malware to evade detection, while established groups like RomCom and Bloody Wolf continue targeted campaigns using established remote access tools.

## Active Exploitation Details

### ShadowV2 Botnet IoT Exploitation
- **Description**: New Mirai-based botnet malware targeting IoT devices from D-Link, TP-Link, and other vendors using exploits for known vulnerabilities
- **Impact**: Compromised IoT devices can be enlisted into botnets for DDoS attacks, cryptocurrency mining, or further network infiltration
- **Status**: Active exploitation observed during AWS outage as testing opportunity

### node-forge Signature Verification Bypass
- **Description**: Vulnerability in the popular JavaScript cryptography library allowing bypass of signature verifications through crafted data that appears valid
- **Impact**: Attackers can forge cryptographic signatures, potentially compromising authentication systems and data integrity
- **Status**: Fix available for the vulnerability

### ASUS AiCloud Authentication Bypass
- **Description**: Critical authentication bypass flaw in ASUS routers with AiCloud enabled, along with eight additional security vulnerabilities
- **Impact**: Complete bypass of authentication mechanisms, allowing unauthorized access to router configurations and network resources
- **Status**: New firmware released to patch vulnerabilities

## Affected Systems and Products

- **IoT Devices**: D-Link and TP-Link routers and devices targeted by ShadowV2 botnet
- **JavaScript Applications**: Systems using the node-forge cryptography library for signature verification
- **ASUS Routers**: Devices with AiCloud functionality vulnerable to authentication bypass
- **Microsoft Teams**: Guest access feature creating cross-tenant security blind spots
- **npm and Maven Ecosystems**: Over 830 compromised packages in npm registry, expansion to Maven repository
- **South Korean Financial Sector**: MSP infrastructure compromised leading to 28-victim data breach campaign

## Attack Vectors and Techniques

- **IoT Exploitation**: ShadowV2 botnet using known vulnerability exploits against network devices
- **Supply Chain Attacks**: Shai-Hulud v2 campaign compromising package repositories to steal secrets and credentials
- **Fake Browser Updates**: SocGholish JavaScript loader delivering Mythic Agent malware through fake update prompts
- **Cross-tenant Bypasses**: Microsoft Teams guest access exploited to bypass Defender for Office 365 protections
- **Cryptographic Bypass**: Crafted data exploitation to bypass signature verification in cryptographic libraries
- **AI-Enhanced Malware**: LLMs integrated into malware for runtime evasion and code augmentation
- **Script Injection**: Unauthorized script injection targeting authentication systems

## Threat Actor Activities

- **ShadowV2 Operators**: Deploying Mirai-based botnet targeting IoT infrastructure during service outages
- **Shai-Hulud Campaign**: Expanding from npm to Maven ecosystems, exposing thousands of secrets from compromised packages
- **RomCom Group**: First observed use of SocGholish fake update attacks to deliver Mythic Agent malware against U.S. civil engineering company
- **Qilin Ransomware**: Sophisticated supply chain attack against South Korean MSP resulting in 28-victim "Korean Leaks" data heist
- **Bloody Wolf**: Expanding Java-based NetSupport RAT campaigns targeting Kyrgyzstan and Uzbekistan since June 2025
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass extortion campaigns against major corporations throughout 2025