# Exploitation Report

The current threat landscape reveals active exploitation of critical vulnerabilities across industrial control systems, with CISA adding a cross-site scripting vulnerability in OpenPLC ScadaBR to its Known Exploited Vulnerabilities catalog. Simultaneously, threat actors are leveraging supply chain attacks through malicious packages in popular development repositories, with North Korean hackers deploying hundreds of malicious npm packages containing updated OtterCookie malware. New botnet malware variants are targeting IoT devices from major vendors, while sophisticated threat groups are conducting multi-victim ransomware campaigns through managed service provider compromises.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: A cross-site scripting (XSS) vulnerability affecting OpenPLC ScadaBR industrial control system software
- **Impact**: Attackers can execute malicious scripts in users' browsers, potentially leading to session hijacking, credential theft, or unauthorized system access in industrial environments
- **Status**: Currently being actively exploited in the wild, prompting CISA to add it to the Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2021-26829

### ShadowV2 Botnet Exploitation of IoT Vulnerabilities
- **Description**: New Mirai-based botnet malware exploiting known vulnerabilities in IoT devices from multiple vendors
- **Impact**: Compromised devices are enlisted into botnet operations for distributed attacks, cryptocurrency mining, or other malicious activities
- **Status**: Active exploitation targeting D-Link, TP-Link, and other IoT device manufacturers with existing vulnerabilities

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control system software vulnerable to XSS attacks
- **D-Link IoT Devices**: Various models targeted by ShadowV2 botnet malware
- **TP-Link IoT Devices**: Multiple device types susceptible to botnet exploitation
- **npm Registry Packages**: 197 malicious packages deployed by North Korean threat actors
- **Maven Ecosystem**: Over 830 packages compromised in Shai-Hulud v2 supply chain attack
- **South Korean MSP Infrastructure**: Financial sector organizations compromised through managed service provider breach
- **Microsoft Teams**: Guest access feature creating cross-tenant security blind spots
- **PyPI Python Packages**: Legacy packages vulnerable to domain takeover attacks

## Attack Vectors and Techniques

- **Cross-Site Scripting (XSS)**: Exploitation of web application vulnerabilities in industrial control systems
- **Supply Chain Poisoning**: Injection of malicious code into legitimate software repositories and package managers
- **Evil Twin WiFi Networks**: Creation of malicious wireless access points to intercept user credentials and data
- **Domain Takeover**: Exploitation of abandoned domains referenced in legacy Python bootstrap scripts
- **Botnet Recruitment**: Automated exploitation of known IoT vulnerabilities to expand botnet infrastructure
- **Guest Access Bypass**: Abuse of Microsoft Teams cross-tenant features to evade security protections
- **MSP Compromise**: Targeting managed service providers to gain access to multiple client organizations

## Threat Actor Activities

- **North Korean Hackers**: Deployed 197 malicious npm packages as part of the Contagious Interview campaign, distributing updated OtterCookie malware
- **Bloody Wolf**: Expanded Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Conducted sophisticated supply chain attack against South Korean MSP, resulting in 28-victim "Korean Leaks" data breach campaign
- **Shai-Hulud Operators**: Launched second wave of supply chain attacks, compromising over 830 npm packages and expanding to Maven ecosystem
- **Scattered LAPSUS$ Hunters**: Continued mass extortion campaigns against major corporations through data theft and public exposure