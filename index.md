# Exploitation Report

The current threat landscape reveals several critical exploitation activities targeting diverse sectors from government entities to industrial control systems. Most notably, CISA has added an actively exploited cross-site scripting vulnerability in OpenPLC ScadaBR to their Known Exploited Vulnerabilities catalog, while advanced persistent threat groups like Tomiris continue to target government organizations with sophisticated command and control infrastructure. Additionally, supply chain attacks have expanded across multiple package repositories, with threat actors leveraging compromised packages in npm and Maven ecosystems to harvest credentials and establish persistent access.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: A cross-site scripting (XSS) vulnerability in OpenPLC ScadaBR, an open-source SCADA (Supervisory Control and Data Acquisition) system
- **Impact**: Allows attackers to execute malicious scripts in users' browsers, potentially leading to session hijacking, credential theft, or unauthorized system access
- **Status**: Actively exploited in the wild according to CISA, added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2021-26829

### ShadowV2 Botnet IoT Exploits
- **Description**: New Mirai-based botnet malware targeting IoT devices from multiple vendors including D-Link and TP-Link
- **Impact**: Compromises IoT devices to expand botnet infrastructure for distributed attacks
- **Status**: Active exploitation of known vulnerabilities in IoT devices

### Legacy Python Package Domain Takeover Vulnerabilities
- **Description**: Vulnerable code in legacy Python packages that creates potential for supply chain compromise through domain takeover attacks
- **Impact**: Could lead to malicious code injection in Python Package Index (PyPI) packages, affecting downstream users
- **Status**: Vulnerable packages identified and disclosed

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control systems and SCADA environments running the open-source platform
- **D-Link IoT Devices**: Various IoT device models vulnerable to ShadowV2 botnet exploitation
- **TP-Link IoT Devices**: Network devices and IoT products targeted by botnet malware
- **Python Package Index (PyPI)**: Legacy packages containing domain takeover vulnerabilities
- **npm Registry**: Over 830 packages compromised in Shai-Hulud v2 supply chain attack
- **Maven Ecosystem**: Java package repository now targeted by expanded Shai-Hulud campaign
- **Microsoft Teams**: Guest access feature creates potential bypass of Defender protections
- **South Korean MSP Infrastructure**: Managed service provider systems compromised in Qilin ransomware attack

## Attack Vectors and Techniques

- **Cross-Site Scripting (XSS)**: Exploitation of web application vulnerabilities to execute malicious scripts
- **IoT Device Exploitation**: Targeting known vulnerabilities in Internet of Things devices to build botnets
- **Supply Chain Attacks**: Compromising package repositories to distribute malicious code to downstream users
- **Domain Takeover**: Exploiting abandoned or misconfigured domains referenced in legacy code
- **Evil Twin WiFi Networks**: Creating malicious wireless access points to intercept user credentials
- **Guest Access Bypass**: Leveraging Microsoft Teams guest features to circumvent security protections
- **MSP Supply Chain Compromise**: Targeting managed service providers to access multiple client organizations

## Threat Actor Activities

- **Tomiris**: Targeting foreign ministries, intergovernmental organizations, and government entities in Russia using public-service implants for stealthier command and control communications
- **North Korean Actors (Contagious Interview Campaign)**: Deploying 197 malicious npm packages containing updated OtterCookie malware
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Scattered LAPSUS$ Hunters**: Conducting mass data theft and extortion campaigns against major corporations throughout 2025
- **Qilin Ransomware Group**: Orchestrating sophisticated supply chain attack against South Korean MSP, resulting in 28-victim "Korean Leaks" data heist
- **Shai-Hulud Campaign Operators**: Expanding supply chain attacks from npm to Maven repositories, exposing thousands of credentials and secrets