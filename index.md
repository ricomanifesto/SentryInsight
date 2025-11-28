# Exploitation Report

The current threat landscape reveals significant exploitation activity across multiple attack vectors, with threat actors leveraging both sophisticated new techniques and established vulnerabilities. Critical activities include the Bloody Wolf group's NetSupport RAT campaigns targeting Central Asian nations, ShadowV2 botnet exploiting IoT device vulnerabilities, and the ongoing Shai-Hulud v2 supply chain attacks affecting thousands of packages. Notable security bypasses include Microsoft Teams guest access features that can disable Defender protections and ASUS router authentication flaws. Supply chain compromises continue to pose major risks, with threat actors successfully infiltrating MSP environments to launch multi-victim ransomware campaigns.

## Active Exploitation Details

### ASUS AiCloud Authentication Bypass
- **Description**: Critical authentication bypass vulnerability affecting ASUS routers with AiCloud functionality enabled
- **Impact**: Allows attackers to bypass authentication mechanisms and potentially gain unauthorized access to router management interfaces
- **Status**: Firmware updates released by ASUS to address nine security vulnerabilities including this critical flaw

### ShadowV2 Botnet IoT Exploitation
- **Description**: New Mirai-based botnet malware actively targeting IoT devices from D-Link, TP-Link, and other vendors using known vulnerability exploits
- **Impact**: Device compromise leading to botnet enrollment and potential DDoS participation
- **Status**: Active exploitation campaign observed, leveraging AWS outage as testing opportunity

### Node-Forge Signature Verification Bypass
- **Description**: Vulnerability in the popular JavaScript cryptography library 'node-forge' that allows bypassing signature verification through crafted data
- **Impact**: Authentication bypass and potential compromise of systems relying on signature validation
- **Status**: Fix has been released for the vulnerability

### Solana Transfer Fee Injection
- **Description**: Malicious Chrome extension injecting hidden Solana transfer fees into Raydium swap transactions
- **Impact**: Financial theft through unauthorized cryptocurrency transfers
- **Status**: Active malicious extension discovered on Chrome Web Store

## Affected Systems and Products

- **Microsoft Teams**: Guest access feature creating cross-tenant security blind spots in Defender for Office 365
- **ASUS Routers**: Multiple router models with AiCloud functionality affected by critical authentication bypass
- **IoT Devices**: D-Link and TP-Link devices targeted by ShadowV2 botnet malware
- **Node-Forge Library**: Popular JavaScript cryptography package with signature verification bypass
- **Chrome Browser**: Malicious extensions targeting Solana cryptocurrency transactions
- **npm/Maven Ecosystems**: Over 830 packages compromised in Shai-Hulud v2 supply chain attack
- **South Korean MSPs**: Financial sector targeted through sophisticated supply chain attacks
- **OpenAI API**: Customer data exposure through third-party Mixpanel analytics provider breach

## Attack Vectors and Techniques

- **Cross-Tenant Exploitation**: Attackers leveraging Microsoft Teams guest access to bypass security controls across organizational boundaries
- **Supply Chain Attacks**: Multi-stage campaigns targeting package repositories and managed service providers
- **SocGholish Fake Updates**: JavaScript loaders delivering Mythic Agent malware through fake browser update prompts
- **IoT Botnet Recruitment**: Automated exploitation of known vulnerabilities in consumer networking devices
- **Browser Extension Abuse**: Malicious extensions injecting unauthorized cryptocurrency transactions
- **Script Injection Attacks**: Targeting authentication systems through unauthorized script execution

## Threat Actor Activities

- **Bloody Wolf**: Expanding NetSupport RAT campaigns from Kyrgyzstan into Uzbekistan using Java-based delivery mechanisms since June 2025
- **RomCom Group**: First observed use of SocGholish fake update attacks to deliver Mythic Agent malware against U.S. civil engineering companies
- **Qilin Ransomware**: Sophisticated supply chain attack against South Korean MSP resulting in "Korean Leaks" campaign affecting 28 victims
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass extortion campaigns against major corporations with data theft operations
- **Iranian Cyber Operations**: Deploying "cyber-enabled kinetic targeting" to support physical missile attacks against maritime and land-based targets