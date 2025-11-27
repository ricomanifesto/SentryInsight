# Exploitation Report

Critical exploitation activity is currently dominated by supply chain attacks and IoT device targeting, with several major campaigns impacting thousands of organizations. The ShadowV2 botnet is actively exploiting known vulnerabilities in IoT devices from major vendors like D-Link and TP-Link, while the Shai-Hulud v2 campaign has expanded from npm to Maven ecosystems, compromising over 830 packages. Meanwhile, threat actors are leveraging authentication bypass flaws in ASUS routers and signature verification vulnerabilities in popular JavaScript libraries. Financial institutions face escalating account takeover attacks, with cybercriminals stealing over $262 million through social engineering schemes targeting bank customers.

## Active Exploitation Details

### ShadowV2 Botnet IoT Exploitation
- **Description**: Mirai-based botnet malware targeting IoT devices with exploits for known vulnerabilities
- **Impact**: Compromised IoT devices from D-Link, TP-Link, and other vendors being recruited into botnet infrastructure
- **Status**: Actively exploiting devices, leveraged AWS outage as testing opportunity

### ASUS AiCloud Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in ASUS routers with AiCloud enabled
- **Impact**: Attackers can bypass authentication mechanisms to gain unauthorized access to router management
- **Status**: Patches released by ASUS in new firmware updates

### Node-Forge Signature Verification Bypass
- **Description**: Vulnerability in the popular JavaScript cryptography library allowing bypass of signature verifications
- **Impact**: Attackers can craft malicious data that appears as valid, compromising cryptographic integrity
- **Status**: Fixed in updated versions of the node-forge package

### Qilin Ransomware Supply Chain Attack
- **Description**: Sophisticated supply chain attack targeting South Korean MSP leading to ransomware deployment
- **Impact**: 28 organizations compromised through MSP breach, data exfiltration and encryption
- **Status**: Active campaign targeting financial sector organizations

## Affected Systems and Products

- **D-Link IoT Devices**: Routers and networking equipment vulnerable to ShadowV2 botnet exploitation
- **TP-Link IoT Devices**: Consumer networking products being targeted by botnet campaigns
- **ASUS AiCloud Routers**: Critical authentication bypass affecting routers with AiCloud functionality enabled
- **Node-Forge Library**: Popular JavaScript cryptography package used across web applications
- **npm and Maven Ecosystems**: Package repositories compromised by Shai-Hulud v2 supply chain attack
- **South Korean MSP Infrastructure**: Managed service provider systems compromised leading to downstream client impacts
- **OnSolve CodeRED Platform**: Emergency notification systems disrupted by cyberattack
- **Financial Institution Systems**: Banks and credit unions targeted through account takeover schemes

## Attack Vectors and Techniques

- **IoT Vulnerability Exploitation**: ShadowV2 botnet targeting known vulnerabilities in consumer networking devices
- **Supply Chain Compromise**: Shai-Hulud v2 campaign spreading malicious packages through software repositories
- **Authentication Bypass**: Exploiting router vulnerabilities to gain unauthorized administrative access
- **Social Engineering**: Cybercriminals impersonating bank support teams to steal credentials
- **SocGholish Fake Updates**: JavaScript loader delivering Mythic Agent malware through fake browser update prompts
- **Chrome Extension Malware**: Malicious extensions injecting hidden Solana transfer fees into cryptocurrency transactions
- **AI-Enhanced Phishing**: Threat actors using large language models to create more sophisticated phishing campaigns

## Threat Actor Activities

- **RomCom Group**: Targeting U.S. civil engineering company using SocGholish fake update attacks to deliver Mythic Agent malware
- **Qilin Ransomware**: Executing sophisticated supply chain attack against South Korean MSP, resulting in "Korean Leaks" data heist affecting 28 organizations
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass extortion campaigns against major corporations
- **DPRK FlexibleFerret**: Continuing "Contagious Interview" campaign with refined tactics targeting macOS users
- **Financial Institution Impersonators**: Coordinated campaign stealing $262 million through account takeover fraud since January 2025
- **Iranian Cyber Operations**: Deploying cyber-enabled kinetic targeting in coordination with missile attacks
- **Chrome Web Store Attackers**: Distributing malicious extensions targeting cryptocurrency users with hidden fee injection