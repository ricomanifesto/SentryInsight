# Exploitation Report

Critical exploitation activity continues across multiple threat vectors, with CISA confirming active exploitation of a cross-site scripting vulnerability in OpenPLC ScadaBR systems. The threat landscape shows significant malware evolution with new Android malware-as-a-service platforms targeting hundreds of applications, while supply chain attacks have expanded from npm to Maven repositories. Nation-state actors including Tomiris and North Korean groups maintain persistent campaigns against government and corporate targets, employing sophisticated techniques to evade detection and establish long-term access.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: A cross-site scripting (XSS) security flaw in OpenPLC ScadaBR industrial control systems
- **Impact**: Allows attackers to execute arbitrary JavaScript code in victim browsers, potentially leading to credential theft and system compromise
- **Status**: Actively exploited in the wild; added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2021-26829

### ShadowV2 IoT Botnet Exploits
- **Description**: New Mirai-based botnet malware targeting IoT devices from multiple vendors including D-Link and TP-Link
- **Impact**: Device compromise and incorporation into botnet infrastructure for distributed attacks
- **Status**: Actively targeting known vulnerabilities in IoT devices; used AWS outage as testing opportunity

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control systems vulnerable to XSS attacks
- **IoT Devices**: D-Link and TP-Link devices targeted by ShadowV2 botnet malware
- **Android Devices**: Over 400 applications targeted by Albiriox malware-as-a-service platform
- **npm Registry**: Over 830 packages compromised in Shai-Hulud v2 supply chain attack
- **Maven Repository**: Now targeted by expanded Shai-Hulud campaign
- **Microsoft Teams**: Guest access feature creating cross-tenant security blind spots
- **GitLab Repositories**: 5.6 million public repositories scanned, revealing over 17,000 exposed secrets

## Attack Vectors and Techniques

- **Malware-as-a-Service**: Albiriox platform offering on-device fraud capabilities and screen control
- **Supply Chain Attacks**: Shai-Hulud v2 campaign expanding from npm to Maven repositories with thousands of exposed secrets
- **Cross-Site Scripting**: Active exploitation of XSS vulnerabilities in industrial control systems
- **Evil Twin WiFi Networks**: Airport-based attacks targeting traveler credentials and data
- **Public Service Implants**: Tomiris group using legitimate services for command and control communications
- **Social Engineering**: North Korean Contagious Interview campaign deploying 197 malicious npm packages

## Threat Actor Activities

- **Tomiris Group**: Conducting sophisticated attacks against government entities and foreign ministries using public service implants for stealthier command and control operations
- **North Korean Hackers**: Expanding Contagious Interview campaign with 197 new malicious npm packages delivering updated OtterCookie malware
- **Bloody Wolf**: Targeting organizations in Kyrgyzstan and Uzbekistan with Java-based NetSupport RAT attacks since June 2025
- **Scattered LAPSUS$ Hunters**: Continuing data theft and mass extortion campaigns against major corporations throughout 2025
- **Cybercriminals**: Leveraging unrestricted large language models like WormGPT 4 and KawaiiGPT to generate advanced malicious code and ransomware encryptors