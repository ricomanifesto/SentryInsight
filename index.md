# Exploitation Report

Current exploitation activity reveals a concerning landscape of actively exploited vulnerabilities and sophisticated attack campaigns. CISA has added CVE-2021-26829, a cross-site scripting vulnerability in OpenPLC ScadaBR, to its Known Exploited Vulnerabilities catalog, indicating active exploitation in the wild. Meanwhile, threat actors are leveraging supply chain attacks through malicious packages in npm and Maven repositories, with the Shai-Hulud v2 campaign compromising over 830 npm packages and expanding to Maven ecosystems. North Korean threat actors continue their malicious activities through the Contagious Interview campaign, deploying 197 malicious npm packages containing updated OtterCookie malware. Additionally, the ShadowV2 botnet is targeting IoT devices from major vendors using known vulnerabilities, while the Qilin ransomware group has executed a sophisticated supply chain attack affecting South Korea's financial sector.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: Cross-site scripting (XSS) vulnerability in OpenPLC ScadaBR industrial control software
- **Impact**: Allows attackers to execute arbitrary scripts in users' browsers, potentially leading to session hijacking, credential theft, and unauthorized access to industrial control systems
- **Status**: Actively exploited in the wild according to CISA's KEV catalog
- **CVE ID**: CVE-2021-26829

### IoT Device Vulnerabilities Targeted by ShadowV2 Botnet
- **Description**: Multiple known vulnerabilities in IoT devices from D-Link, TP-Link, and other vendors
- **Impact**: Device compromise leading to botnet recruitment, DDoS attacks, and potential lateral movement within networks
- **Status**: Actively exploited by new Mirai-based ShadowV2 botnet malware

### Microsoft Defender for Office 365 Bypass
- **Description**: Cross-tenant blind spot in Microsoft Teams guest access feature
- **Impact**: Attackers can bypass Microsoft Defender for Office 365 protections when users join external tenants
- **Status**: Active vulnerability allowing security control bypass

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control system software vulnerable to XSS attacks
- **D-Link IoT Devices**: Various models targeted by ShadowV2 botnet exploitation
- **TP-Link IoT Devices**: Multiple product lines susceptible to known vulnerability exploitation
- **Microsoft Teams**: Guest access feature creating security blind spots in cross-tenant scenarios
- **npm Registry**: Over 830 packages compromised in Shai-Hulud v2 supply chain attack
- **Maven Repository**: Newly targeted ecosystem in expanded Shai-Hulud v2 campaign
- **South Korean MSP Infrastructure**: Financial sector systems compromised in Qilin ransomware supply chain attack

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages deployed across npm (830+ packages) and Maven repositories in Shai-Hulud v2 campaign
- **Cross-Site Scripting (XSS)**: Exploitation of web application vulnerabilities in industrial control systems
- **Botnet Recruitment**: ShadowV2 malware leveraging known IoT vulnerabilities for device compromise
- **Evil Twin WiFi Networks**: Airport-based attacks to steal traveler credentials and data
- **Cross-Tenant Exploitation**: Abuse of Microsoft Teams guest access to bypass security protections
- **Domain Takeover**: Legacy Python bootstrap scripts creating domain takeover risks in PyPI packages
- **Social Engineering**: North Korean Contagious Interview campaign targeting developers

## Threat Actor Activities

- **North Korean Threat Actors**: Deploying 197 malicious npm packages with updated OtterCookie malware as part of ongoing Contagious Interview campaign targeting software developers
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks in Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Executed sophisticated supply chain attack against South Korean MSP, affecting 28 victims in financial sector through "Korean Leaks" operation
- **Scattered LAPSUS$ Hunters**: Cybercriminal group conducting mass extortion campaigns against major corporations with data theft operations
- **Shai-Hulud Attackers**: Orchestrating large-scale supply chain attack across multiple package repositories, exposing thousands of secrets