# Exploitation Report

CISA has added an actively exploited cross-site scripting vulnerability in OpenPLC ScadaBR to its Known Exploited Vulnerabilities catalog, highlighting ongoing threats to industrial control systems. Concurrently, North Korean threat actors are conducting sophisticated supply chain attacks through malicious npm packages, while the Qilin ransomware group has executed a major supply chain attack targeting South Korean MSPs that compromised 28 victims. Additional threats include a new Mirai-based botnet targeting IoT devices, malicious LLM tools enabling less skilled attackers, and various data breaches affecting major organizations.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: A cross-site scripting (XSS) vulnerability affecting OpenPLC ScadaBR, an industrial control system platform
- **Impact**: Attackers can execute malicious scripts in users' browsers, potentially leading to credential theft, session hijacking, or unauthorized system access in industrial environments
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2021-26829

### ShadowV2 Botnet IoT Exploits
- **Description**: A new Mirai-based botnet malware targeting IoT devices from D-Link, TP-Link, and other vendors
- **Impact**: Device compromise, botnet recruitment, and potential use in DDoS attacks or other malicious activities
- **Status**: Active exploitation of known vulnerabilities in IoT devices

### North Korean npm Package Supply Chain Attack
- **Description**: Deployment of 197 malicious npm packages containing updated OtterCookie malware
- **Impact**: Code execution, data theft, and potential compromise of development environments
- **Status**: Active campaign by North Korean threat actors continuing the Contagious Interview operation

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control system platform vulnerable to XSS attacks
- **IoT Devices**: D-Link, TP-Link, and other vendor devices targeted by ShadowV2 botnet
- **npm Ecosystem**: JavaScript package repository compromised with 197 malicious packages
- **Maven Ecosystem**: Affected by Shai-Hulud v2 supply chain attack expanding from npm
- **Microsoft Teams**: Guest access feature creating bypass opportunities for Defender protection
- **Asahi Group Holdings**: Beer production company affected by September cyberattack impacting 1.9 million individuals
- **French Football Federation**: Administrative management software compromised through account takeover
- **OpenAI API**: Customer data exposed through Mixpanel vendor breach
- **Gainsight**: Customer relationship platform with expanded impact from Salesforce security incident
- **GitLab Cloud**: Over 17,000 secrets exposed across 2,800 domains in public repositories

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Malicious packages in npm and Maven repositories targeting developers
- **Cross-Site Scripting (XSS)**: Web application vulnerabilities enabling script injection
- **Botnet Recruitment**: IoT device exploitation for malware distribution and DDoS capabilities
- **Evil Twin WiFi Networks**: Rogue access points deployed in airports to steal traveler data
- **Account Takeover**: Compromised credentials used to access administrative systems
- **Domain Takeover**: Legacy Python bootstrap scripts creating takeover risks in PyPI packages
- **Prompt Injection**: AI model manipulation techniques targeting LLM-based systems
- **Third-Party Vendor Compromise**: Indirect attacks through analytics and service providers

## Threat Actor Activities

- **North Korean Groups**: Conducting Contagious Interview campaign with 197 malicious npm packages and updated OtterCookie malware
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Executed sophisticated supply chain attack on South Korean MSP, compromising 28 victims in "Korean Leaks" operation
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting data theft and mass extortion campaigns against major corporations
- **ShadowV2 Operators**: Deploying new Mirai-based botnet targeting IoT devices, using AWS outages as testing opportunities
- **Shai-Hulud Campaign**: Second wave attackers compromising over 830 npm packages and expanding to Maven ecosystem