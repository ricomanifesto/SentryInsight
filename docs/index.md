# Exploitation Report

Current threat landscape analysis reveals significant exploitation activities across multiple attack vectors, with particular emphasis on supply chain attacks, botnet operations, and targeted campaigns against enterprise environments. North Korean threat actors are actively deploying malicious packages across npm and Maven repositories, while new botnet malware targets IoT devices with known vulnerability exploits. Notable incidents include sophisticated ransomware operations in South Korea's financial sector, cross-tenant security bypasses in Microsoft Teams, and domain takeover risks affecting Python package repositories.

## Active Exploitation Details

### ShadowV2 Botnet IoT Exploitation
- **Description**: New Mirai-based botnet malware targeting IoT devices from multiple vendors including D-Link and TP-Link
- **Impact**: Compromised IoT devices integrated into botnet infrastructure for malicious activities
- **Status**: Active exploitation of known vulnerabilities in IoT devices

### Qilin Ransomware Supply Chain Attack
- **Description**: Sophisticated supply chain attack targeting South Korea's financial sector through MSP breach
- **Impact**: 28 victims compromised in "Korean Leaks" data heist operation
- **Status**: Active ransomware deployment following initial MSP compromise

### Shai-Hulud v2 Supply Chain Attack
- **Description**: Second wave of supply chain attack spreading from npm to Maven ecosystem
- **Impact**: Over 830 compromised packages in npm registry, exposing thousands of secrets
- **Status**: Active campaign expanding across multiple package repositories

### Python Package Domain Takeover Vulnerability
- **Description**: Legacy Python bootstrap scripts in PyPI packages create domain takeover opportunities
- **Impact**: Potential supply chain compromise through domain hijacking
- **Status**: Vulnerable code identified in legacy packages across PyPI

### Microsoft Teams Cross-Tenant Bypass
- **Description**: Guest access feature allows bypassing Microsoft Defender for Office 365 protections
- **Impact**: Attackers can evade security controls when users join external tenants
- **Status**: Active security bypass technique identified

## Affected Systems and Products

- **IoT Devices**: D-Link and TP-Link devices vulnerable to ShadowV2 botnet exploitation
- **South Korean Financial Sector**: 28 organizations affected through MSP supply chain attack
- **npm Registry**: Over 830 packages compromised in Shai-Hulud v2 campaign
- **Maven Repository**: Extended target of Shai-Hulud supply chain attack
- **PyPI Packages**: Legacy Python packages with domain takeover vulnerabilities
- **Microsoft Teams**: Cross-tenant environments vulnerable to Defender bypass
- **Chrome Web Store**: Malicious extensions injecting hidden Solana transfers
- **GitLab Cloud**: 5.6 million public repositories scanned, 17,000+ exposed secrets identified
- **Windows 11**: Updates since August causing password login option visibility issues
- **Gainsight Applications**: Expanded customer impact following Salesforce security alert

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Malicious package injection across npm, Maven, and PyPI repositories
- **Botnet Exploitation**: IoT device compromise using known vulnerability exploits
- **Ransomware Operations**: MSP breach leading to downstream customer compromises
- **Domain Takeover**: Exploitation of legacy bootstrap scripts in Python packages
- **Cross-Tenant Attacks**: Abuse of Microsoft Teams guest access for security bypass
- **Browser Extension Malware**: Hidden cryptocurrency transfer injection in Chrome extensions
- **Evil Twin WiFi**: Airport-based man-in-the-middle attacks using rogue access points
- **Account Compromise**: Unauthorized access to administrative management software
- **Vendor Compromise**: Third-party analytics provider breach affecting downstream customers

## Threat Actor Activities

- **North Korean Groups**: Deploying 197 malicious npm packages for OtterCookie malware distribution through Contagious Interview campaign
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Orchestrating sophisticated supply chain attacks against South Korean financial institutions
- **Scattered LAPSUS$ Hunters**: Continuing mass extortion campaigns against major corporations with data theft operations
- **ShadowV2 Operators**: Testing botnet capabilities during AWS outages while targeting IoT infrastructure
- **Shai-Hulud Attackers**: Expanding supply chain attacks from npm to Maven ecosystem for credential harvesting