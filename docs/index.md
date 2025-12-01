# Exploitation Report

Critical exploitation activity is dominated by actively exploited vulnerabilities in industrial control systems and sophisticated supply chain attacks targeting multiple ecosystems. CISA has added CVE-2021-26829, a cross-site scripting vulnerability in OpenPLC ScadaBR, to its Known Exploited Vulnerabilities catalog due to confirmed active exploitation. Meanwhile, threat actors are leveraging advanced malware distribution through package repositories, with North Korean hackers deploying 197 malicious npm packages containing updated OtterCookie malware, and the Shai-Hulud v2 campaign expanding from npm to Maven ecosystems. Additional concerns include new botnet malware targeting IoT devices and sophisticated ransomware operations affecting managed service providers.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: A cross-site scripting (XSS) vulnerability affecting OpenPLC ScadaBR industrial control systems
- **Impact**: Attackers can execute malicious scripts in users' browsers, potentially leading to session hijacking, credential theft, or unauthorized actions within the SCADA environment
- **Status**: Actively exploited in the wild, added to CISA's KEV catalog
- **CVE ID**: CVE-2021-26829

### ShadowV2 Botnet IoT Exploitation
- **Description**: A new Mirai-based botnet malware targeting Internet of Things devices with known vulnerability exploits
- **Impact**: Compromised devices can be used for DDoS attacks, cryptocurrency mining, or as entry points for lateral movement
- **Status**: Active exploitation of known vulnerabilities in D-Link and TP-Link devices

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control systems and SCADA environments vulnerable to XSS attacks
- **D-Link IoT Devices**: Network equipment targeted by ShadowV2 botnet malware
- **TP-Link IoT Devices**: Consumer and enterprise networking hardware compromised by botnet operations
- **npm Registry**: JavaScript package repository compromised with 197 malicious packages and 830+ Shai-Hulud v2 packages
- **Maven Repository**: Java package ecosystem now targeted by Shai-Hulud v2 supply chain attacks
- **PyPI Packages**: Python package repository containing legacy bootstrap scripts vulnerable to domain takeover
- **Microsoft Teams**: Guest access feature creating security blind spots in Defender for Office 365
- **South Korean MSPs**: Managed service providers targeted in sophisticated supply chain attacks

## Attack Vectors and Techniques

- **Cross-Site Scripting (XSS)**: Exploitation of web application vulnerabilities in industrial control systems
- **Supply Chain Poisoning**: Malicious package distribution through npm, Maven, and PyPI repositories
- **IoT Botnet Deployment**: Exploitation of known vulnerabilities in network devices for botnet recruitment
- **Evil Twin WiFi Networks**: Rogue wireless access points deployed in airports to steal traveler data
- **Domain Takeover**: Exploitation of legacy Python bootstrap scripts for package repository compromise
- **Guest Access Abuse**: Microsoft Teams cross-tenant vulnerabilities bypassing security protections
- **Ransomware as a Service**: Qilin ransomware deployment through compromised managed service providers

## Threat Actor Activities

- **North Korean Hackers (Contagious Interview Campaign)**: Continued flooding of npm registry with 197 malicious packages containing updated OtterCookie malware targeting software developers
- **Bloody Wolf**: Java-based NetSupport RAT distribution campaign targeting Kyrgyzstan and Uzbekistan since June 2025
- **Shai-Hulud v2 Operators**: Sophisticated supply chain attack expanding from npm to Maven ecosystem, exposing thousands of secrets across compromised packages
- **Qilin Ransomware Group**: Orchestrated sophisticated supply chain attack against South Korean financial sector through MSP breach, affecting 28 victims in "Korean Leaks" operation
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass data extortion campaigns against major corporations throughout 2025