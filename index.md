# Exploitation Report

This report identifies critical vulnerability exploitation activity across industrial control systems, supply chain environments, and enterprise infrastructure. The most significant exploitation involves a cross-site scripting vulnerability in OpenPLC ScadaBR (CVE-2021-26829) that CISA has added to its Known Exploited Vulnerabilities catalog, indicating active targeting of industrial systems. Additionally, multiple supply chain attacks are ongoing, including North Korean threat actors deploying 197 malicious npm packages containing OtterCookie malware, the ShadowV2 botnet exploiting known IoT vulnerabilities, and the Shai-Hulud v2 campaign compromising over 830 npm packages while expanding to Maven repositories. These activities demonstrate sophisticated attackers targeting critical infrastructure and software supply chains with immediate operational impact.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: A cross-site scripting (XSS) vulnerability in OpenPLC ScadaBR that allows attackers to execute malicious scripts in users' browsers
- **Impact**: Attackers can steal credentials, perform unauthorized actions, or compromise industrial control systems
- **Status**: Actively exploited and added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2021-26829

### ShadowV2 Botnet IoT Exploitation
- **Description**: A new Mirai-based botnet malware targeting IoT devices with known vulnerabilities
- **Impact**: Compromised devices become part of a botnet for DDoS attacks and other malicious activities
- **Status**: Actively exploiting known vulnerabilities in D-Link, TP-Link, and other IoT vendors

### Shai-Hulud v2 Supply Chain Attack
- **Description**: Second wave of supply chain attack compromising npm and Maven package repositories
- **Impact**: Exposure of thousands of secrets and potential code execution in downstream applications
- **Status**: Over 830 npm packages compromised, expanding to Maven ecosystem

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control system software used in SCADA environments
- **IoT Devices**: D-Link and TP-Link devices with known security vulnerabilities
- **npm Registry**: Over 830 packages compromised in Shai-Hulud v2 campaign
- **Maven Repository**: Targeted as expansion of Shai-Hulud supply chain attack
- **PyPI Packages**: Legacy Python packages vulnerable to domain takeover attacks
- **Microsoft Teams**: Guest access feature can bypass Defender for Office 365 protections
- **GitLab Cloud**: 5.6 million public repositories scanned, revealing 17,000 exposed secrets

## Attack Vectors and Techniques

- **Cross-Site Scripting**: Exploitation of XSS vulnerabilities in industrial control systems
- **Supply Chain Poisoning**: Injection of malicious code into legitimate package repositories
- **IoT Botnet Recruitment**: Targeting known vulnerabilities in consumer and enterprise IoT devices
- **Domain Takeover**: Legacy Python bootstrap scripts creating takeover opportunities
- **Evil Twin WiFi**: Creation of malicious WiFi hotspots to intercept user credentials
- **Guest Access Bypass**: Leveraging Microsoft Teams guest features to evade security controls

## Threat Actor Activities

- **North Korean Contagious Interview Campaign**: Deployed 197 malicious npm packages containing updated OtterCookie malware targeting software developers
- **Bloody Wolf**: Expanded Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Conducted sophisticated supply chain attack on South Korean MSP, affecting 28 victims in "Korean Leaks" operation
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass extortion campaigns against major corporations through data theft
- **ShadowV2 Operators**: Utilized AWS outage as testing opportunity for new botnet malware deployment