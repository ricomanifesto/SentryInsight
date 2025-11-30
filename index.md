# Exploitation Report

Current threat activity reveals significant supply chain attacks targeting software repositories, with North Korean threat actors deploying massive malware campaigns through npm packages. Critical exploitation includes botnet malware targeting IoT devices with known vulnerabilities, malicious browser extensions stealing cryptocurrency funds, and sophisticated supply chain compromises affecting major organizations. Multiple data breaches have occurred through various attack vectors including compromised accounts, vendor breaches, and social engineering campaigns. The threat landscape shows increased use of AI-powered malware tools and advanced persistent threat activities across multiple sectors.

## Active Exploitation Details

### ShadowV2 Botnet Malware
- **Description**: New Mirai-based botnet malware targeting IoT devices from multiple vendors
- **Impact**: Device compromise and botnet enrollment for distributed attacks
- **Status**: Actively exploiting known vulnerabilities in D-Link, TP-Link, and other IoT devices

### OtterCookie Malware Campaign
- **Description**: Updated malware distributed through 197 malicious npm packages by North Korean threat actors
- **Impact**: Supply chain compromise and system infiltration through package repositories
- **Status**: Active distribution through npm registry as part of Contagious Interview campaign

### Shai-Hulud v2 Supply Chain Attack
- **Description**: Second wave attack compromising over 830 npm packages and expanding to Maven ecosystem
- **Impact**: Exposure of thousands of secrets and potential widespread supply chain compromise
- **Status**: Active across multiple package repositories with ongoing expansion

### Chrome Extension Cryptocurrency Theft
- **Description**: Malicious Chrome Web Store extension injecting hidden Solana transfer fees
- **Impact**: Theft of cryptocurrency funds during legitimate swap transactions on Raydium
- **Status**: Active exploitation targeting cryptocurrency users

### Microsoft Teams Guest Access Bypass
- **Description**: Cross-tenant vulnerability allowing attackers to bypass Microsoft Defender for Office 365 protections
- **Impact**: Removal of security protections when users join external Teams tenants
- **Status**: Active vulnerability with demonstrated bypass techniques

## Affected Systems and Products

- **IoT Devices**: D-Link, TP-Link, and other vendor devices vulnerable to ShadowV2 botnet
- **Software Repositories**: npm registry (830+ packages), Maven ecosystem, PyPI packages with domain takeover risks
- **Microsoft Teams**: Guest access functionality bypassing Defender protections
- **Chrome Browser**: Extensions from Chrome Web Store targeting cryptocurrency transactions
- **Enterprise Systems**: Asahi Group Holdings, French Football Federation, Gainsight, OpenAI/Mixpanel
- **Financial Sector**: South Korean organizations targeted through MSP supply chain attack

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages in npm, Maven, and PyPI repositories
- **Domain Takeover**: Legacy Python bootstrap scripts creating takeover opportunities
- **Social Engineering**: Evil Twin WiFi networks targeting airport travelers
- **Account Compromise**: Compromised administrative accounts for system access
- **Vendor Breaches**: Third-party analytics provider compromises affecting downstream customers
- **Cross-Tenant Attacks**: Exploiting Microsoft Teams guest access features
- **Malicious Extensions**: Browser extensions with hidden cryptocurrency theft functionality
- **Ransomware Deployment**: Qilin ransomware through MSP compromise affecting multiple victims

## Threat Actor Activities

- **North Korean Groups**: Contagious Interview campaign deploying OtterCookie malware through 197 npm packages
- **Bloody Wolf**: Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Scattered LAPSUS$ Hunters**: Data theft and mass extortion campaigns affecting dozens of major corporations
- **Qilin Ransomware**: Korean Leaks operation affecting 28 victims through South Korean MSP breach
- **ShadowV2 Operators**: IoT botnet campaign leveraging AWS outage as testing opportunity
- **Cryptocurrency Thieves**: Chrome extension developers targeting Solana transactions
- **Airport WiFi Attackers**: Seven-year prison sentence for Australian evil twin network operator