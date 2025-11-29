# Exploitation Report

The current threat landscape reveals a diverse array of active exploitation campaigns targeting critical infrastructure, supply chain components, and enterprise systems. Notable activities include sophisticated supply chain attacks against PyPI and npm repositories exposing thousands of secrets, North Korean threat actors deploying malware through package registries, and enterprise-focused campaigns leveraging known IoT vulnerabilities. The emergence of AI-enhanced malware development tools is enabling less sophisticated attackers to create more advanced threats, while traditional attack vectors like Evil Twin WiFi networks and ransomware operations continue to impact organizations globally.

## Active Exploitation Details

### Domain Takeover Vulnerabilities in PyPI Packages
- **Description**: Legacy Python bootstrap scripts in multiple PyPI packages contain vulnerable code that could enable supply chain compromise through domain takeover attacks
- **Impact**: Attackers could potentially compromise the Python Package Index supply chain, affecting downstream users of vulnerable packages
- **Status**: Actively identified and disclosed, remediation status varies by package

### IoT Device Vulnerabilities
- **Description**: Known vulnerabilities in D-Link, TP-Link, and other vendor devices are being exploited by the ShadowV2 botnet malware
- **Impact**: Remote code execution and device compromise leading to botnet recruitment
- **Status**: Actively exploited by Mirai-based botnet malware

### Node-forge Signature Verification Bypass
- **Description**: Vulnerability in the popular JavaScript cryptography library allowing bypass of signature verifications through crafted data
- **Impact**: Authentication bypass and potential compromise of cryptographic operations
- **Status**: Fixed in recent library update

### Microsoft Teams Cross-Tenant Security Bypass
- **Description**: Guest access feature in Microsoft Teams can bypass Defender for Office 365 protections when users join external tenants
- **Impact**: Security control evasion and potential exposure to malicious content
- **Status**: Identified security gap requiring configuration adjustments

### GitLab Repository Secret Exposure
- **Description**: Widespread exposure of sensitive credentials and secrets across public GitLab repositories
- **Impact**: Over 17,000 secrets exposed across 2,800+ domains, enabling potential unauthorized access
- **Status**: Ongoing exposure risk across multiple repositories

## Affected Systems and Products

- **PyPI Package Registry**: Multiple legacy Python packages with domain takeover vulnerabilities
- **npm Package Registry**: 197+ malicious packages spreading OtterCookie malware, 830+ packages in Shai-Hulud v2 campaign
- **Maven Repository**: Recently targeted by Shai-Hulud v2 supply chain attack expansion
- **D-Link and TP-Link IoT Devices**: Various models targeted by ShadowV2 botnet exploitation
- **Microsoft Teams**: Guest access feature creating cross-tenant security gaps
- **Microsoft Entra ID**: Authentication systems targeted for script injection attacks
- **Windows 11**: Lock screen password option visibility issues affecting user authentication
- **GitLab Cloud**: 5.6 million public repositories scanned, exposing secrets across platforms
- **Chrome Web Store**: Malicious extensions targeting cryptocurrency transactions
- **Gainsight Platform**: Customer applications affected by suspicious activity
- **French Football Federation Systems**: Administrative management software compromised
- **OpenAI API**: Customer data exposed through Mixpanel vendor breach

## Attack Vectors and Techniques

- **Evil Twin WiFi Networks**: Deployment of rogue access points at airports to intercept user credentials and data
- **Supply Chain Poisoning**: Injection of malicious code into package repositories including npm, PyPI, and Maven
- **SocGholish Fake Updates**: JavaScript loader delivering Mythic Agent malware through fake browser update prompts
- **Cross-Tenant Exploitation**: Leveraging Microsoft Teams guest access to bypass security controls
- **Botnet Recruitment**: Exploitation of known IoT vulnerabilities for device compromise and network inclusion
- **Credential Harvesting**: Automated scanning and extraction of secrets from public code repositories
- **AI-Enhanced Malware Development**: Use of unrestricted LLMs like WormGPT 4 and KawaiiGPT for malicious code generation
- **Cryptojacking Extensions**: Chrome extensions injecting hidden cryptocurrency transfers into legitimate transactions
- **Script Injection**: Unauthorized script execution in authentication systems

## Threat Actor Activities

- **North Korean Actors**: Continued Contagious Interview campaign deploying 197 npm packages containing updated OtterCookie malware targeting developers
- **RomCom Group**: First observed use of SocGholish loader to deliver Mythic Agent malware against U.S. civil engineering companies
- **Bloody Wolf**: Expansion of Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Operators**: Sophisticated supply chain attack against South Korean MSP resulting in "Korean Leaks" data heist affecting 28 victims
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass extortion campaigns against major corporations
- **Shai-Hulud Campaign Actors**: Second wave attacks expanding from npm to Maven ecosystems, compromising over 830 packages
- **ShadowV2 Botnet Operators**: Mirai-based botnet leveraging AWS outages as testing opportunities while targeting IoT devices
- **Cryptocurrency Attackers**: Chrome extension developers creating malicious tools for Solana transaction manipulation