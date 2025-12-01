# Exploitation Report

Current cybersecurity threats reveal significant exploitation activity across multiple vectors, with particular emphasis on XSS vulnerabilities in industrial systems, mobile malware operations, and advanced persistent threat campaigns. The most critical concern is the active exploitation of CVE-2021-26829, a cross-site scripting vulnerability in OpenPLC ScadaBR that has been added to CISA's Known Exploited Vulnerabilities catalog. Additionally, sophisticated malware-as-a-service operations like Albiriox are targeting hundreds of mobile applications for fraud activities, while advanced threat actors such as Tomiris are deploying novel stealth techniques against government entities. The threat landscape is further complicated by large-scale supply chain attacks targeting software repositories and the emergence of AI-enhanced malware capabilities.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: A cross-site scripting (XSS) vulnerability affecting OpenPLC ScadaBR industrial control systems
- **Impact**: Attackers can execute malicious scripts in the context of legitimate users, potentially compromising industrial control systems
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2021-26829

### Albiriox Android Malware
- **Description**: A sophisticated malware-as-a-service (MaaS) targeting over 400 mobile applications for on-device fraud
- **Impact**: Enables screen control manipulation, credential theft, and financial fraud across multiple mobile platforms
- **Status**: Actively distributed through MaaS model with comprehensive fraud capabilities

### ShadowV2 Botnet
- **Description**: Mirai-based botnet malware targeting IoT devices with known vulnerability exploits
- **Impact**: Device compromise leading to botnet recruitment and potential DDoS attacks
- **Status**: Active exploitation of IoT devices from multiple vendors including D-Link and TP-Link

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control system software vulnerable to XSS attacks
- **Android Devices**: Over 400 mobile applications targeted by Albiriox malware
- **IoT Devices**: D-Link, TP-Link, and other vendor devices targeted by ShadowV2 botnet
- **Microsoft Teams**: Guest access feature bypassing Defender for Office 365 protections
- **npm Registry**: 197 malicious packages deployed by North Korean actors
- **PyPI Packages**: Legacy Python packages with domain-takeover vulnerabilities
- **GitLab Repositories**: 5.6 million public repositories exposing over 17,000 secrets
- **Maven Ecosystem**: Compromised packages in Shai-Hulud v2 supply chain attack

## Attack Vectors and Techniques

- **Cross-Site Scripting (XSS)**: Exploitation of web application vulnerabilities in industrial systems
- **Malware-as-a-Service**: Commercial distribution of sophisticated mobile malware
- **Supply Chain Attacks**: Compromise of software repositories including npm and Maven ecosystems
- **Guest Access Bypass**: Exploitation of Microsoft Teams cross-tenant functionality
- **IoT Exploitation**: Targeting known vulnerabilities in internet-connected devices
- **AI-Enhanced Malware**: Integration of large language models for evasion and code augmentation
- **Evil Twin WiFi**: Deployment of rogue wireless networks in airports and public spaces
- **Domain Takeover**: Exploitation of legacy bootstrap scripts in Python packages

## Threat Actor Activities

- **Tomiris Group**: Targeting government entities and foreign ministries using public-service implants for stealthier command-and-control operations
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks across Kyrgyzstan and Uzbekistan
- **North Korean Actors**: Deploying 197 malicious npm packages spreading updated OtterCookie malware in Contagious Interview campaign
- **Scattered LAPSUS$ Hunters**: Conducting mass data theft and extortion campaigns against major corporations
- **Supply Chain Attackers**: Executing Shai-Hulud v2 campaign affecting both npm and Maven ecosystems with over 830 compromised packages