# Exploitation Report

The cybersecurity landscape is currently experiencing significant exploitation activity across multiple vectors, with CISA adding a cross-site scripting vulnerability in OpenPLC ScadaBR to its Known Exploited Vulnerabilities catalog, indicating active exploitation in the wild. Concurrently, threat actors are leveraging sophisticated supply chain attacks, malicious package repositories, and advanced AI-powered tools to conduct large-scale campaigns. Notable activities include North Korean hackers flooding npm with malicious packages, the emergence of new botnets targeting IoT devices, and ransomware operations exploiting managed service providers to compromise multiple downstream victims.

## Active Exploitation Details

### Cross-Site Scripting in OpenPLC ScadaBR
- **Description**: A cross-site scripting vulnerability affecting OpenPLC ScadaBR industrial control systems
- **Impact**: Allows attackers to execute malicious scripts in users' browsers, potentially leading to credential theft, session hijacking, and unauthorized system access
- **Status**: Actively exploited in the wild according to CISA, added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2021-26829

### ShadowV2 Botnet IoT Exploits
- **Description**: A new Mirai-based botnet malware targeting IoT devices from D-Link, TP-Link, and other vendors
- **Impact**: Compromises IoT devices to build botnet infrastructure for DDoS attacks and other malicious activities
- **Status**: Active exploitation of known vulnerabilities in IoT devices, leveraged AWS outage as testing opportunity

### Supply Chain Attacks on Package Repositories
- **Description**: Multiple campaigns targeting npm and Maven package repositories with malicious packages
- **Impact**: Code execution in developer environments, credential theft, and potential downstream compromise of applications
- **Status**: Over 830 compromised packages in npm registry (Shai-Hulud v2), 197 malicious npm packages (North Korean OtterCookie campaign)

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control systems vulnerable to cross-site scripting attacks
- **IoT Devices**: D-Link and TP-Link devices targeted by ShadowV2 botnet malware
- **npm Registry**: Over 1,000 malicious packages across multiple supply chain campaigns
- **Maven Repository**: Targeted by Shai-Hulud v2 campaign expansion
- **Microsoft Teams**: Guest access feature creates blind spot in Defender for Office 365 protections
- **GitLab Public Repositories**: Over 17,000 exposed secrets across 2,800 domains
- **Asahi Group Holdings**: Beer manufacturer affected by September cyberattack impacting 1.9 million individuals
- **French Football Federation**: Administrative management software compromised via account takeover

## Attack Vectors and Techniques

- **Cross-Site Scripting (XSS)**: Exploitation of web application vulnerabilities to execute malicious scripts
- **Supply Chain Compromise**: Injection of malicious code into legitimate software packages and repositories
- **Evil Twin WiFi Networks**: Creation of rogue access points to intercept user credentials and data
- **IoT Botnet Recruitment**: Exploitation of known vulnerabilities in Internet of Things devices
- **Package Repository Poisoning**: Upload of malicious packages to npm and Maven registries
- **Account Compromise**: Unauthorized access to administrative accounts for lateral movement
- **Cross-Tenant Security Bypass**: Exploitation of Microsoft Teams guest access to evade security protections

## Threat Actor Activities

- **North Korean Hackers**: Conducting Contagious Interview campaign with 197 malicious npm packages distributing updated OtterCookie malware
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Orchestrated sophisticated supply chain attack against South Korean MSP, compromising 28 downstream victims in "Korean Leaks" operation
- **Scattered LAPSUS$ Hunters**: Prolific cybercriminal group conducting mass extortion campaigns against major corporations throughout 2025
- **Shai-Hulud Campaign Operators**: Expanding supply chain attacks from npm to Maven repositories, compromising over 830 packages
- **ShadowV2 Operators**: Deploying new Mirai-based botnet malware targeting IoT infrastructure