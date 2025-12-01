# Exploitation Report

The current threat landscape shows significant active exploitation activity across multiple attack vectors. CISA has added an actively exploited cross-site scripting vulnerability in OpenPLC ScadaBR industrial control systems to their Known Exploited Vulnerabilities catalog, highlighting critical infrastructure targeting. Simultaneously, multiple sophisticated threat actors including Tomiris, Bloody Wolf, and North Korean groups are deploying advanced persistent threats through supply chain attacks, malicious packages, and steganographic techniques. The ShadowV2 botnet is actively exploiting IoT devices from major vendors, while large-scale supply chain compromises like Shai-Hulud v2 have exposed thousands of secrets across npm and Maven repositories.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: A cross-site scripting vulnerability in OpenPLC ScadaBR industrial control software that allows attackers to inject malicious scripts
- **Impact**: Attackers can execute arbitrary JavaScript code in the context of the vulnerable application, potentially leading to session hijacking, credential theft, or further system compromise
- **Status**: Actively exploited in the wild and added to CISA's KEV catalog
- **CVE ID**: CVE-2021-26829

### IoT Device Exploitation by ShadowV2 Botnet
- **Description**: A new Mirai-based botnet malware targeting IoT devices with known vulnerabilities in their firmware and management interfaces
- **Impact**: Compromised devices can be recruited into botnets for DDoS attacks, cryptocurrency mining, or as proxies for further malicious activities
- **Status**: Active exploitation campaign targeting D-Link, TP-Link, and other vendor devices with unpatched vulnerabilities

### Supply Chain Package Compromise
- **Description**: Multiple supply chain attacks targeting npm and Maven repositories with malicious packages designed to steal credentials and sensitive data
- **Impact**: Developers downloading compromised packages can have their development environments compromised, leading to broader organizational breaches
- **Status**: Over 830 npm packages compromised in Shai-Hulud v2 campaign, with attack expanding to Maven ecosystem

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control system software used in SCADA environments
- **D-Link IoT Devices**: Various IoT devices from D-Link with unpatched firmware vulnerabilities
- **TP-Link IoT Devices**: IoT devices from TP-Link vulnerable to known exploits
- **npm Registry Packages**: Over 830 compromised packages in the npm ecosystem
- **Maven Repository Packages**: Multiple malicious packages targeting Java developers
- **Microsoft Teams**: Guest access feature creating bypass opportunities for Defender protections
- **Salesforce/Gainsight**: Customer relationship management platforms affected by suspicious activity
- **PyPI Python Packages**: Legacy Python packages with domain takeover vulnerabilities

## Attack Vectors and Techniques

- **Cross-Site Scripting (XSS)**: Injection of malicious scripts into vulnerable web applications to steal credentials or hijack sessions
- **IoT Botnet Recruitment**: Exploitation of known vulnerabilities in IoT devices to build botnet infrastructure
- **Supply Chain Poisoning**: Injection of malicious code into legitimate software packages to compromise downstream users
- **Evil Twin WiFi Attacks**: Creation of rogue WiFi networks to intercept and steal user credentials and sensitive data
- **Package Typosquatting**: Creation of malicious packages with names similar to legitimate ones to trick developers
- **Domain Takeover**: Exploitation of abandoned domains referenced in legacy code to inject malicious content
- **Steganographic C2 Communication**: Use of public services and image-based steganography to hide command and control traffic

## Threat Actor Activities

- **Tomiris**: Targeting foreign ministries and government entities in Russia using public service implants for stealthier command and control communications
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks into Kyrgyzstan and Uzbekistan with sophisticated delivery mechanisms
- **North Korean Actors**: Deploying 197 malicious npm packages as part of the Contagious Interview campaign to spread updated OtterCookie malware
- **Qilin Ransomware Group**: Conducting sophisticated supply chain attack against South Korean MSP resulting in 28-victim "Korean Leaks" data heist
- **Scattered LAPSUS$ Hunters**: Conducting mass extortion campaigns against major corporations through data theft and public exposure
- **Shai-Hulud Operators**: Expanding supply chain attack from npm to Maven ecosystem, exposing thousands of secrets across multiple domains