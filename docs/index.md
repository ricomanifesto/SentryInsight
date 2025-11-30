# Exploitation Report

The current threat landscape reveals significant exploitation activity across multiple attack vectors, with threat actors leveraging supply chain vulnerabilities, malicious packages, and social engineering techniques. North Korean threat actors continue their aggressive campaigns through malicious npm packages, while new botnets like ShadowV2 exploit IoT device vulnerabilities. Supply chain attacks have escalated with the Shai-Hulud v2 campaign expanding from npm to Maven ecosystems, and ransomware groups like Qilin are conducting sophisticated multi-victim operations through MSP breaches.

## Active Exploitation Details

### ShadowV2 Mirai-based Botnet
- **Description**: A new Mirai-based botnet malware targeting IoT devices from multiple vendors including D-Link and TP-Link
- **Impact**: Compromises IoT devices to expand botnet infrastructure for potential DDoS attacks and further exploitation
- **Status**: Actively exploiting known vulnerabilities in IoT devices

### Shai-Hulud v2 Supply Chain Attack
- **Description**: Second wave of supply chain attack spreading from npm to Maven ecosystem, compromising over 830 packages in npm registry
- **Impact**: Exposes thousands of secrets and credentials from compromised packages, enabling further attacks
- **Status**: Active campaign with expanding reach across multiple package repositories

### OtterCookie Malware Distribution
- **Description**: Updated malware being distributed through 197 malicious npm packages by North Korean threat actors
- **Impact**: Enables persistent access and data theft from developer environments
- **Status**: Ongoing campaign with continuous package uploads to npm registry

### Legacy Python Bootstrap Domain Takeover
- **Description**: Vulnerable code in legacy Python packages creating potential for supply chain compromise via domain takeover
- **Impact**: Could allow attackers to compromise PyPI packages and distribute malicious updates
- **Status**: Vulnerability identified in multiple PyPI packages requiring remediation

## Affected Systems and Products

- **IoT Devices**: D-Link and TP-Link devices vulnerable to ShadowV2 botnet exploitation
- **npm Registry**: Over 830 compromised packages in the Shai-Hulud v2 campaign
- **Maven Ecosystem**: Newly targeted by Shai-Hulud v2 supply chain attack
- **PyPI Packages**: Legacy Python packages with domain takeover vulnerabilities
- **Microsoft Teams**: Guest access feature creates blind spot bypassing Defender for Office 365 protections
- **GitLab Cloud**: Over 17,000 exposed secrets across 2,800 unique domains in public repositories
- **Chrome Web Store**: Malicious extension injecting hidden Solana transfer fees
- **South Korean Financial Sector**: 28 organizations affected by Qilin ransomware through MSP breach

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages uploaded to npm and Maven repositories to compromise downstream users
- **Domain Takeover**: Exploiting abandoned domains referenced in legacy Python bootstrap scripts
- **Evil Twin WiFi**: Creating malicious WiFi networks to intercept user credentials and data
- **Guest Access Exploitation**: Using Microsoft Teams guest features to bypass security protections
- **Browser Extension Manipulation**: Injecting malicious code through Chrome extensions to steal cryptocurrency
- **MSP Supply Chain Attack**: Compromising managed service providers to access multiple client organizations
- **Social Engineering**: Using malicious LLMs to generate convincing phishing content and attack tools

## Threat Actor Activities

- **North Korean Contagious Interview Campaign**: Continued flooding of npm registry with malicious packages carrying OtterCookie malware
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Conducting sophisticated supply chain attack against South Korean MSP, resulting in 28-victim "Korean Leaks" operation
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass extortion campaigns against major corporations throughout 2025
- **Shai-Hulud Operators**: Orchestrating large-scale supply chain attacks across multiple package ecosystems
- **Cryptocurrency Scammers**: Deploying malicious Chrome extensions to steal funds through hidden transaction manipulation