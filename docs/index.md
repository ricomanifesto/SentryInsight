# Exploitation Report

Current cybersecurity threat landscape reveals significant exploitation activity across multiple vectors, with notable supply chain attacks targeting package repositories, advanced malware campaigns leveraging artificial intelligence capabilities, and sophisticated botnet operations exploiting IoT devices. The most critical activities include North Korean threat actors deploying 197 malicious npm packages containing updated OtterCookie malware, the emergence of ShadowV2 botnet exploiting known vulnerabilities in IoT devices, and large-scale supply chain attacks compromising over 830 npm packages in the Shai-Hulud v2 campaign. Additional concerns include malicious LLMs empowering low-skilled attackers with advanced capabilities and ongoing ransomware operations targeting managed service providers for broader impact.

## Active Exploitation Details

### ShadowV2 Botnet Exploitation
- **Description**: New Mirai-based botnet malware targeting IoT devices with exploits for known vulnerabilities
- **Impact**: Compromise of IoT devices for botnet recruitment and potential DDoS attacks
- **Status**: Actively exploiting known vulnerabilities in D-Link, TP-Link, and other vendor devices

### OtterCookie Malware Distribution
- **Description**: North Korean threat actors deploying updated malware through 197 malicious npm packages
- **Impact**: Supply chain compromise affecting developers and downstream applications
- **Status**: Active campaign continuing from previous month with expanded package deployment

### Shai-Hulud v2 Supply Chain Attack
- **Description**: Large-scale supply chain attack compromising over 830 npm packages and expanding to Maven ecosystem
- **Impact**: Exposure of thousands of secrets and potential widespread application compromise
- **Status**: Active campaign with cross-platform expansion from npm to Maven repositories

### node-forge Signature Verification Bypass
- **Description**: Vulnerability in popular JavaScript cryptography library allowing signature verification bypass
- **Impact**: Attackers can craft data that appears valid, potentially compromising cryptographic operations
- **Status**: Fix available for the vulnerability

### Python Package Domain Takeover
- **Description**: Legacy Python bootstrap scripts creating domain-takeover risks in multiple PyPI packages
- **Impact**: Potential supply chain compromise through domain takeover attacks
- **Status**: Vulnerable code identified across legacy Python packages

## Affected Systems and Products

- **IoT Devices**: D-Link, TP-Link, and other vendor devices targeted by ShadowV2 botnet
- **npm Registry**: 197 packages containing OtterCookie malware, 830+ packages in Shai-Hulud v2 campaign
- **Maven Ecosystem**: Expansion target for Shai-Hulud v2 supply chain attack
- **node-forge Library**: Popular JavaScript cryptography library with signature verification flaw
- **PyPI Packages**: Multiple legacy Python packages with domain takeover vulnerabilities
- **Microsoft Teams**: Guest access feature bypassing Defender for Office 365 protections
- **Chrome Browser**: Malicious extensions injecting hidden Solana transfer fees
- **GitLab Repositories**: Over 17,000 exposed secrets across 5.6 million public repositories
- **South Korean MSP**: 28 victims affected through Qilin ransomware supply chain attack

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Compromising package repositories (npm, Maven, PyPI) to distribute malware
- **IoT Exploitation**: Targeting known vulnerabilities in consumer and enterprise IoT devices
- **Evil Twin WiFi**: Creating rogue access points to steal credentials and data
- **Domain Takeover**: Exploiting legacy bootstrap scripts pointing to expired domains
- **Cross-tenant Attacks**: Abusing Microsoft Teams guest access to bypass security controls
- **Browser Extension Injection**: Malicious Chrome extensions modifying cryptocurrency transactions
- **Social Engineering**: Using malicious LLMs to generate convincing phishing content
- **MSP Compromise**: Targeting managed service providers for broader victim access

## Threat Actor Activities

- **North Korean Groups**: Continued Contagious Interview campaign with 197 new malicious npm packages containing OtterCookie malware
- **Bloody Wolf**: Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware**: Sophisticated supply chain attack on South Korean MSP affecting 28 victims in "Korean Leaks" operation
- **Scattered LAPSUS$ Hunters**: Mass extortion campaigns targeting major corporations with data theft and public exposure
- **Shai-Hulud Operators**: Large-scale supply chain attack compromising 830+ npm packages and expanding to Maven ecosystem
- **Cryptocurrency Fraudsters**: Chrome extension attacks injecting hidden fees into Solana transactions
- **Airport WiFi Attackers**: Seven-year prison sentence for individual conducting evil twin attacks across Australian airports