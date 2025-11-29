# Exploitation Report

Current cybersecurity threats are dominated by sophisticated supply chain attacks, advanced malware campaigns, and exploitation of trust relationships. North Korean threat actors continue aggressive operations through malicious package repositories, deploying updated malware variants across npm and Maven ecosystems. Meanwhile, ransomware groups are executing complex multi-victim attacks through MSP compromises, and new botnet malware is actively exploiting IoT device vulnerabilities. Attackers are increasingly leveraging AI-powered tools and social engineering techniques, while targeting authentication bypass vulnerabilities and trust mechanisms in widely-used platforms.

## Active Exploitation Details

### ShadowV2 Botnet IoT Vulnerabilities
- **Description**: New Mirai-based botnet malware targeting IoT devices from D-Link, TP-Link, and other vendors with exploits for known vulnerabilities
- **Impact**: Device compromise, botnet recruitment, potential DDoS attacks and lateral movement
- **Status**: Active exploitation observed, vendors have patches available for known vulnerabilities

### Node-Forge Signature Verification Bypass
- **Description**: Vulnerability in the popular JavaScript cryptography library that allows bypassing signature verifications through crafted data
- **Impact**: Authentication bypass, data integrity compromise, potential code execution
- **Status**: Recently patched, active exploitation possible in unpatched implementations

### Microsoft Teams Guest Access Security Bypass
- **Description**: Cross-tenant blind spot that allows attackers to bypass Microsoft Defender for Office 365 protections via Teams guest access feature
- **Impact**: Security protection bypass, potential malware delivery, data exfiltration
- **Status**: Active exploitation vector, mitigation guidance available

### Legacy Python Bootstrap Domain Takeover
- **Description**: Vulnerable code in legacy Python packages on PyPI that could enable supply chain compromise via domain takeover
- **Impact**: Supply chain compromise, malicious code injection, widespread package poisoning
- **Status**: Multiple vulnerable packages identified, remediation in progress

## Affected Systems and Products

- **D-Link IoT Devices**: Multiple router and IoT device models targeted by ShadowV2 botnet
- **TP-Link IoT Devices**: Various router models exploited for botnet recruitment
- **Node-Forge JavaScript Library**: Popular cryptography library with signature verification bypass
- **Microsoft Teams**: Guest access feature enabling security bypass across tenants
- **PyPI Python Packages**: Legacy packages with domain takeover vulnerabilities
- **npm Registry**: Over 197 malicious packages deployed by North Korean actors
- **Maven Repository**: Supply chain attack expansion from npm ecosystem
- **GitLab Cloud**: 5.6 million public repositories scanned, 17,000+ secrets exposed
- **French Football Federation**: Administrative management software compromised
- **South Korean Financial Sector**: 28 organizations affected via MSP supply chain attack

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Mass deployment of malicious packages across npm and Maven repositories
- **IoT Device Exploitation**: Known vulnerability exploitation for botnet recruitment
- **Evil Twin WiFi Networks**: Airport-based credential harvesting operations
- **Social Engineering**: AI-enhanced phishing and credential theft campaigns
- **Cross-Tenant Attacks**: Microsoft Teams guest access exploitation for security bypass
- **Domain Takeover**: Legacy package infrastructure compromise for supply chain attacks
- **Ransomware Deployment**: MSP infrastructure compromise for multi-victim operations
- **Chrome Extension Abuse**: Hidden cryptocurrency transfer fee injection
- **Credential Harvesting**: Automated scanning for exposed secrets in public repositories

## Threat Actor Activities

- **North Korean APT Groups**: Continued Contagious Interview campaign expansion with 197 new malicious npm packages containing updated OtterCookie malware
- **Bloody Wolf**: Java-based NetSupport RAT deployment targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Sophisticated supply chain attack against South Korean MSP resulting in 28-victim "Korean Leaks" data heist
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass data theft and extortion against major corporations
- **Evil Twin Operator**: Individual sentenced for airport WiFi credential harvesting operations across Australia
- **Shai-Hulud Campaign**: Second wave supply chain attack compromising 830+ npm packages and expanding to Maven ecosystem