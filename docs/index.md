# Exploitation Report

The current threat landscape reveals significant supply chain attacks targeting package repositories, with North Korean threat actors deploying hundreds of malicious packages across npm and Maven ecosystems. Critical vulnerabilities are being actively exploited in IoT devices through new botnet operations, while sophisticated ransomware groups continue to leverage supply chain compromises for large-scale data theft operations. Additional concerns include JavaScript library vulnerabilities that bypass cryptographic signature verification and Microsoft Teams security bypasses that remove endpoint protection capabilities.

## Active Exploitation Details

### ShadowV2 Botnet IoT Exploitation
- **Description**: New Mirai-based botnet malware targeting IoT devices from multiple vendors including D-Link and TP-Link
- **Impact**: Device compromise and botnet recruitment for distributed attacks
- **Status**: Actively exploiting known vulnerabilities in IoT devices, taking advantage of AWS outages for testing

### node-forge Signature Verification Bypass
- **Description**: Vulnerability in the popular JavaScript cryptography library allowing attackers to bypass signature verifications
- **Impact**: Attackers can craft data that appears cryptographically valid, undermining security controls
- **Status**: Patch available, vulnerability affects signature verification mechanisms

### Microsoft Teams Defender Bypass
- **Description**: Cross-tenant blind spot allowing attackers to bypass Microsoft Defender for Office 365 protections via guest access feature
- **Impact**: Complete removal of endpoint protection when users join external Teams tenants
- **Status**: Active exploitation technique affecting enterprise security posture

### Legacy Python Bootstrap Script Vulnerabilities
- **Description**: Vulnerable code in legacy Python packages creating domain takeover risks
- **Impact**: Potential supply chain compromise through domain hijacking attacks
- **Status**: Multiple PyPI packages affected, creates persistent supply chain risk

## Affected Systems and Products

- **IoT Devices**: D-Link, TP-Link, and other vendor devices vulnerable to ShadowV2 botnet exploitation
- **JavaScript Applications**: Systems using node-forge cryptography library for signature verification
- **Microsoft Teams Environments**: Enterprise environments using guest access features with external tenants
- **Python Package Ecosystem**: PyPI packages containing legacy bootstrap scripts with domain takeover vulnerabilities
- **npm Registry**: 197 malicious packages deployed by North Korean actors, 830+ packages in Shai-Hulud v2 campaign
- **Maven Repository**: Expanded Shai-Hulud v2 attack targeting Java ecosystem
- **GitLab Repositories**: 5.6 million public repositories scanned, 17,000+ exposed secrets discovered
- **Chrome Web Store**: Malicious extensions injecting hidden Solana transfer fees

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Mass deployment of malicious packages across npm and Maven repositories
- **IoT Botnet Recruitment**: Exploitation of known vulnerabilities in consumer and enterprise IoT devices
- **Cross-Tenant Security Bypass**: Abuse of legitimate Microsoft Teams features to remove security protections
- **Cryptographic Bypass**: Crafting of malicious data to circumvent signature verification processes
- **Domain Takeover**: Exploitation of abandoned domains referenced in legacy package bootstrap scripts
- **Secret Harvesting**: Automated scanning and extraction of credentials from public code repositories
- **Browser Extension Injection**: Malicious Chrome extensions modifying cryptocurrency transactions

## Threat Actor Activities

- **North Korean Actors (Contagious Interview Campaign)**: Deployed 197 malicious npm packages continuing their supply chain poisoning operations with updated OtterCookie malware
- **Bloody Wolf**: Expanded Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Conducted sophisticated supply chain attack against South Korean MSP, resulting in "Korean Leaks" operation affecting 28 victims in the financial sector
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass data theft and public extortion campaigns against major corporations
- **Shai-Hulud Operators**: Executed second wave of supply chain attacks expanding from npm to Maven, exposing thousands of secrets across both ecosystems