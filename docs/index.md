# Exploitation Report

Current threat activity reveals a concerning trend of sophisticated supply chain attacks, malware distribution campaigns, and exploitation of trust mechanisms across multiple platforms. Notable activities include North Korean threat actors flooding npm repositories with malicious packages in their ongoing Contagious Interview campaign, the emergence of ShadowV2 botnet targeting IoT devices, and RomCom's adoption of SocGholish fake update attacks. The Shai-Hulud supply chain attack has expanded from npm to Maven ecosystems, while Qilin ransomware executed a sophisticated supply chain attack against South Korean financial institutions. Additionally, threat actors are increasingly leveraging malicious LLMs and AI-generated content to enhance their attack capabilities and evade detection.

## Active Exploitation Details

### ShadowV2 Botnet IoT Exploitation
- **Description**: New Mirai-based botnet malware targeting IoT devices from multiple vendors including D-Link and TP-Link
- **Impact**: Attackers can establish persistent botnet infrastructure and control compromised IoT devices for malicious activities
- **Status**: Actively exploiting known vulnerabilities in IoT devices during recent AWS outage testing

### North Korean npm Package Poisoning
- **Description**: Deployment of 197 malicious npm packages containing updated OtterCookie malware as part of the Contagious Interview campaign
- **Impact**: Supply chain compromise targeting developers and organizations through infected dependency packages
- **Status**: Ongoing campaign with continuous package uploads to npm registry

### SocGholish JavaScript Loader Attacks
- **Description**: Fake browser update mechanism used by RomCom threat actors to deliver Mythic Agent malware
- **Impact**: Initial access leading to full system compromise and potential data theft
- **Status**: Active exploitation targeting U.S.-based civil engineering companies

### Shai-Hulud Supply Chain Attack
- **Description**: Second wave of supply chain attack spreading from npm to Maven ecosystem, compromising over 830 packages
- **Impact**: Exposure of thousands of secrets and potential compromise of downstream applications
- **Status**: Actively expanding across multiple package repositories

### Chrome Extension Cryptocurrency Theft
- **Description**: Malicious browser extension injecting hidden Solana transfer fees into Raydium swap transactions
- **Impact**: Financial theft through manipulation of cryptocurrency transactions
- **Status**: Recently discovered on Chrome Web Store

### Microsoft Teams Guest Access Bypass
- **Description**: Cross-tenant vulnerability allowing attackers to bypass Microsoft Defender for Office 365 protections
- **Impact**: Security control evasion in enterprise environments using Teams guest access
- **Status**: Active vulnerability requiring configuration changes

## Affected Systems and Products

- **IoT Devices**: D-Link and TP-Link devices vulnerable to ShadowV2 botnet exploitation
- **npm Registry**: 197 malicious packages targeting Node.js developers and applications
- **Maven Repository**: Expanding Shai-Hulud campaign affecting Java development ecosystem
- **Chrome Web Store**: Malicious extensions targeting cryptocurrency users
- **Microsoft Teams**: Guest access feature creating security blind spots in tenant environments
- **Forge JavaScript Library**: Cryptographic library with signature verification bypass vulnerability
- **PyPI Package Repository**: Legacy Python packages with domain takeover vulnerabilities
- **South Korean Financial Sector**: 28 organizations affected by Qilin ransomware supply chain attack
- **OpenAI API Customers**: Data exposure through third-party analytics provider Mixpanel breach
- **French Football Federation**: Administrative management software compromised through account takeover

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Injection of malicious code into legitimate package repositories (npm, Maven, PyPI)
- **Fake Browser Updates**: SocGholish JavaScript loader masquerading as browser security updates
- **Evil Twin WiFi Networks**: Man-in-the-middle attacks targeting airport travelers
- **Malicious Browser Extensions**: Cryptocurrency transaction manipulation through browser plugins
- **Cross-Tenant Access Abuse**: Exploitation of Microsoft Teams guest features to bypass security controls
- **MSP Infrastructure Compromise**: Leveraging managed service provider access for multi-victim attacks
- **AI-Enhanced Malware**: Use of malicious LLMs for code generation and detection evasion
- **Domain Takeover**: Exploitation of legacy bootstrap scripts in Python packages

## Threat Actor Activities

- **North Korean APT Groups**: Continued Contagious Interview campaign with OtterCookie malware distribution through npm packages
- **RomCom**: First observed use of SocGholish fake update infrastructure to deliver Mythic Agent malware
- **Qilin Ransomware**: Sophisticated supply chain attack against South Korean MSP affecting 28 financial sector victims in "Korean Leaks" operation
- **Bloody Wolf**: Expansion of Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass data extortion campaigns against major corporations
- **Cryptocurrency Thieves**: Development of specialized Chrome extensions for Solana transaction manipulation
- **Botnet Operators**: ShadowV2 malware distribution targeting IoT device vulnerabilities during infrastructure testing