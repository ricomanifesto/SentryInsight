# Exploitation Report

Current cybersecurity threats reveal a concerning landscape of active exploitation across multiple attack vectors. Critical vulnerabilities are being exploited in IoT devices through botnet campaigns, supply chain attacks are targeting software package repositories with malicious code injection, and sophisticated threat actors are employing advanced techniques including AI-enhanced malware generation. Notable activities include the ShadowV2 botnet targeting IoT devices from major vendors, large-scale supply chain compromises affecting npm and Maven repositories, and North Korean threat groups continuing their malicious package distribution campaigns. Organizations face particular risks from script injection attacks, signature verification bypasses, and cross-tenant security gaps in enterprise platforms.

## Active Exploitation Details

### IoT Device Vulnerabilities via ShadowV2 Botnet
- **Description**: A new Mirai-based botnet malware targeting IoT devices from D-Link, TP-Link, and other vendors using exploits for known vulnerabilities
- **Impact**: Device compromise leading to botnet recruitment and potential distributed attacks
- **Status**: Currently active with ongoing exploitation campaigns

### Legacy Python Bootstrap Script Vulnerabilities
- **Description**: Vulnerable code in legacy Python packages creating domain-takeover risks through compromised bootstrap scripts
- **Impact**: Supply chain compromise potential through domain hijacking affecting PyPI packages
- **Status**: Active risk requiring package maintainer attention

### Node-forge Signature Verification Bypass
- **Description**: Vulnerability in the popular JavaScript cryptography library allowing bypass of signature verification through crafted data
- **Impact**: Attackers can bypass cryptographic signature validations by creating data that appears legitimate
- **Status**: Fix available, requiring library updates

### Microsoft Teams Cross-Tenant Security Bypass
- **Description**: Guest access feature in Teams allows attackers to bypass Microsoft Defender for Office 365 protections when users join external tenants
- **Impact**: Complete removal of Defender protections for users joining malicious external tenants
- **Status**: Active vulnerability with no immediate fix announced

## Affected Systems and Products

- **D-Link IoT Devices**: Various models targeted by ShadowV2 botnet exploiting known vulnerabilities
- **TP-Link IoT Devices**: Multiple device types compromised through automated exploitation campaigns
- **PyPI Python Packages**: Legacy packages with vulnerable bootstrap scripts affecting supply chain security
- **Node-forge Library**: Popular JavaScript cryptography library with signature verification flaws
- **npm Registry**: Over 830 packages compromised in Shai-Hulud v2 supply chain attack
- **Maven Ecosystem**: Now targeted by Shai-Hulud campaign expansion from npm
- **Microsoft Teams**: Guest access functionality creating cross-tenant security gaps
- **GitLab Cloud**: Over 5.6 million public repositories scanned revealing 17,000+ exposed secrets
- **Windows 11**: Updates since August causing password login option visibility issues

## Attack Vectors and Techniques

- **Botnet Recruitment**: ShadowV2 malware automatically scanning and exploiting IoT devices using known vulnerability exploits
- **Supply Chain Poisoning**: Malicious packages injected into npm and Maven repositories to compromise downstream applications
- **Domain Takeover**: Legacy Python bootstrap scripts creating opportunities for supply chain compromise through expired domain acquisition
- **Script Injection**: Unauthorized script injection attacks targeting authentication systems
- **Evil Twin WiFi**: Airport-based WiFi attacks using fake networks to steal traveler credentials and data
- **SocGholish Fake Updates**: JavaScript loader delivering advanced malware through fake browser update prompts
- **Cross-Platform Malware**: AI-enhanced malware generation improving capabilities across multiple attack vectors

## Threat Actor Activities

- **North Korean Hackers**: Continued deployment of 197 malicious npm packages spreading updated OtterCookie malware through Contagious Interview campaign
- **RomCom Group**: Using SocGholish fake update attacks to deliver Mythic Agent malware, representing first observed use of this specific delivery mechanism
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware**: Sophisticated supply chain attack against South Korean MSP resulting in 28-victim "Korean Leaks" data heist
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass data theft and extortion campaigns against major corporations
- **Shai-Hulud Campaign**: Advanced supply chain attackers expanding operations from npm to Maven ecosystem with over 830 compromised packages