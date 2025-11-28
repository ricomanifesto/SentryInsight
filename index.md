# Exploitation Report

Critical supply chain attacks and vulnerability exploitation activities are dominating the current threat landscape, with multiple sophisticated campaigns targeting development ecosystems and enterprise infrastructure. North Korean threat actors are actively deploying malware through npm package repositories, while the Qilin ransomware group has orchestrated a major supply chain attack against South Korean infrastructure. Concurrently, IoT devices face widespread exploitation through new botnet campaigns, and enterprise systems are experiencing targeted breaches leveraging compromised accounts and vendor vulnerabilities.

## Active Exploitation Details

### ShadowV2 Botnet IoT Vulnerabilities
- **Description**: A new Mirai-based botnet malware targeting IoT devices from D-Link, TP-Link, and other vendors through exploitation of known vulnerabilities
- **Impact**: Complete device compromise, botnet recruitment, potential DDoS participation, and lateral network movement
- **Status**: Active exploitation observed, with attackers using the AWS outage as a testing opportunity for their capabilities

### Node-forge Signature Verification Bypass
- **Description**: Vulnerability in the popular JavaScript cryptography library allowing attackers to bypass signature verifications by crafting data that appears valid
- **Impact**: Complete circumvention of cryptographic signature validation, enabling data tampering and authentication bypass
- **Status**: Vulnerability patched in recent library update

### Legacy Python Bootstrap Script Domain Takeover
- **Description**: Vulnerable code in legacy Python packages creating potential supply chain compromise vectors through domain takeover attacks on PyPI
- **Impact**: Supply chain compromise affecting multiple Python packages and their downstream users
- **Status**: Active risk identified across multiple PyPI packages

### Microsoft Teams Defender Bypass
- **Description**: Cross-tenant blind spot allowing attackers to bypass Microsoft Defender for Office 365 protections via Teams guest access features
- **Impact**: Complete bypass of enterprise security protections when users join external tenant environments
- **Status**: Vulnerability disclosed, mitigation guidance provided

## Affected Systems and Products

- **IoT Devices**: D-Link and TP-Link routers and network devices vulnerable to ShadowV2 botnet exploitation
- **npm Registry**: 197 malicious packages deployed by North Korean actors spreading OtterCookie malware
- **PyPI Ecosystem**: Multiple legacy Python packages containing domain takeover vulnerabilities
- **node-forge Library**: JavaScript cryptography library used across numerous web applications
- **Microsoft Teams**: Enterprise communication platform with cross-tenant security gaps
- **GitLab Cloud**: 5.6 million public repositories scanned, over 17,000 secrets exposed across 2,800 domains
- **South Korean MSP Infrastructure**: Financial sector systems compromised in sophisticated supply chain attack
- **Chrome Web Store**: Malicious extensions targeting Solana cryptocurrency transactions

## Attack Vectors and Techniques

- **Supply Chain Compromise**: North Korean actors using npm packages to distribute malware, Shai-Hulud campaign expanding from npm to Maven repositories
- **Botnet Recruitment**: ShadowV2 malware exploiting known IoT vulnerabilities for device compromise and network expansion
- **Domain Takeover**: Legacy Python bootstrap scripts creating opportunities for package repository compromise
- **Cross-tenant Exploitation**: Microsoft Teams guest access features bypassing enterprise security boundaries
- **Repository Mining**: Automated scanning of public code repositories to extract exposed credentials and secrets
- **Browser Extension Injection**: Malicious Chrome extensions injecting hidden cryptocurrency transfer fees into legitimate transactions
- **Ransomware as a Service**: Qilin ransomware operators targeting MSP infrastructure to reach multiple downstream victims

## Threat Actor Activities

- **North Korean Groups**: Continued deployment of 197 malicious npm packages as part of the Contagious Interview campaign, spreading updated OtterCookie malware targeting developer communities
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks across Kyrgyzstan and Uzbekistan since June 2025, targeting regional infrastructure
- **Qilin Ransomware Operators**: Sophisticated supply chain attack against South Korean MSP resulting in 28-victim "Korean Leaks" data heist targeting the financial sector
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass extortion campaigns against major corporations with public data exposure tactics
- **Shai-Hulud Campaign Operators**: Supply chain attackers expanding from npm to Maven ecosystems, compromising over 830 packages and exposing thousands of secrets