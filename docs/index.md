# Exploitation Report

The current threat landscape shows significant exploitation activity across multiple vectors, with threat actors leveraging supply chain attacks, malware-as-a-service platforms, and social engineering techniques. Notable activities include the deployment of Mirai-based botnet malware targeting IoT devices, sophisticated supply chain compromises affecting package repositories, and advanced ransomware operations. North Korean threat actors continue their campaign activities through malicious npm packages, while new botnet infrastructure exploits known IoT vulnerabilities for widespread device compromise.

## Active Exploitation Details

### ShadowV2 Botnet IoT Exploitation
- **Description**: A new Mirai-based botnet malware targeting IoT devices from multiple vendors including D-Link and TP-Link
- **Impact**: Device compromise, botnet recruitment, and potential use for DDoS attacks and cryptomining operations
- **Status**: Actively exploiting known vulnerabilities in IoT devices during recent AWS outage testing

### Shai-Hulud v2 Supply Chain Attack
- **Description**: Multi-platform supply chain attack compromising over 830 packages in npm registry and expanding to Maven ecosystem
- **Impact**: Exposure of thousands of secrets and potential widespread software supply chain compromise
- **Status**: Active campaign with expanding scope across multiple package repositories

### OtterCookie Malware Distribution
- **Description**: North Korean threat actors distributing updated OtterCookie malware through 197 malicious npm packages
- **Impact**: System compromise and potential data theft targeting software developers
- **Status**: Ongoing campaign as part of the Contagious Interview operation

### Chrome Extension Solana Injection
- **Description**: Malicious Chrome extension injecting hidden Solana transfer fees into Raydium swap transactions
- **Impact**: Financial theft through cryptocurrency transaction manipulation
- **Status**: Recently discovered on Chrome Web Store with active deployment

## Affected Systems and Products

- **D-Link IoT Devices**: Multiple models vulnerable to ShadowV2 botnet exploitation
- **TP-Link IoT Devices**: Various router and networking equipment models targeted
- **npm Package Registry**: Over 830 compromised packages containing malicious code
- **Maven Ecosystem**: Secondary target for Shai-Hulud v2 supply chain attacks
- **Chrome Browser**: Users with malicious extensions face cryptocurrency theft risk
- **Asahi Group Systems**: Administrative systems compromised affecting 1.9 million individuals
- **French Football Federation**: Administrative management software breached through compromised accounts
- **GitLab Cloud**: Over 17,000 exposed secrets across 2,800+ domains in public repositories
- **Microsoft Teams**: Guest access feature creating security blind spots for Defender protection
- **Gainsight Applications**: Customer management systems affected by suspicious activity
- **OpenAI API Systems**: Customer data exposed through third-party vendor Mixpanel breach

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Injection of malicious code into legitimate software packages across npm and Maven repositories
- **IoT Vulnerability Exploitation**: Targeting known security flaws in consumer and enterprise IoT devices for botnet recruitment
- **Evil Twin WiFi Networks**: Creation of rogue wireless access points to intercept user credentials and data
- **Browser Extension Manipulation**: Deployment of malicious Chrome extensions to inject unauthorized cryptocurrency transactions
- **Account Compromise**: Use of compromised credentials to access administrative systems and steal sensitive data
- **Cross-Tenant Attacks**: Exploitation of Microsoft Teams guest access features to bypass security protections
- **Vendor Supply Chain Attacks**: Compromising third-party service providers to access customer data
- **Social Engineering**: Targeting developers through fake interview processes and malicious package distribution

## Threat Actor Activities

- **North Korean APT Groups**: Continuing Contagious Interview campaign with 197 new malicious npm packages distributing OtterCookie malware
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks targeting Kyrgyzstan and Uzbekistan since June 2025
- **Qilin Ransomware Group**: Conducting sophisticated supply chain attack against South Korean MSP resulting in 28-victim "Korean Leaks" data heist
- **ShadowV2 Operators**: Deploying new Mirai-based botnet targeting IoT devices and using AWS outages as testing opportunities
- **Shai-Hulud Attackers**: Orchestrating large-scale supply chain compromise across multiple package repositories exposing thousands of secrets
- **Scattered LAPSUS$ Hunters**: Continuing mass data theft and extortion campaigns against major corporations throughout 2025