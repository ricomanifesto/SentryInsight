# Exploitation Report

Critical exploitation activity has emerged across multiple attack vectors, with threat actors leveraging compromised browser extensions, software supply chain attacks, and sophisticated malware campaigns. The ShadyPanda operation has successfully compromised over 4.3 million browser extension installations across a seven-year campaign, while North Korean threat actors continue flooding the npm ecosystem with malicious packages. Additionally, CISA has added an actively exploited cross-site scripting vulnerability in OpenPLC ScadaBR to its Known Exploited Vulnerabilities catalog, and the Shai-hulud worm has evolved to target cloud credentials across major platforms including AWS, Google Cloud Platform, and Azure.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: A cross-site scripting (XSS) vulnerability in the OpenPLC ScadaBR industrial control system software
- **Impact**: Allows attackers to execute malicious scripts in users' browsers, potentially leading to credential theft or unauthorized access
- **Status**: Actively exploited in the wild and added to CISA's KEV catalog
- **CVE ID**: CVE-2021-26829

### SmartTube Android TV Application Compromise
- **Description**: The popular open-source SmartTube YouTube client for Android TV was compromised through stolen developer signing keys
- **Impact**: Malicious updates pushed to legitimate users, potentially compromising Android TV devices
- **Status**: Developer signing keys compromised, malicious updates distributed

### Browser Extension Supply Chain Attacks
- **Description**: ShadyPanda operation targeting legitimate browser extensions, converting them into spyware after gaining user trust
- **Impact**: Data theft and surveillance capabilities deployed to millions of users across Chrome and Edge browsers
- **Status**: Seven-year ongoing campaign with over 4.3 million installations compromised

### npm Package Poisoning Campaign
- **Description**: North Korean threat actors deploying 197 malicious npm packages containing updated OtterCookie malware
- **Impact**: Supply chain compromise targeting JavaScript developers and their downstream applications
- **Status**: Active campaign continuing from previous Contagious Interview operations

### Shai-hulud 2.0 Cloud Credential Theft
- **Description**: Self-replicating npm-package poisoning worm evolved to steal cloud credentials and secrets
- **Impact**: Credential and secret theft from AWS, Google Cloud Platform, and Azure environments
- **Status**: Active variant of previously identified worm with enhanced cloud targeting capabilities

## Affected Systems and Products

- **OpenPLC ScadaBR**: Industrial control system software vulnerable to XSS attacks
- **SmartTube**: Android TV YouTube client with compromised signing infrastructure
- **Chrome and Edge Browser Extensions**: Over 4.3 million installations across multiple legitimate extensions
- **npm Package Ecosystem**: JavaScript package repository targeted by multiple malicious campaigns
- **AWS, Google Cloud Platform, Azure**: Cloud platforms targeted for credential theft
- **Android TV Devices**: Devices running compromised SmartTube applications
- **Coupang Platform**: South Korean retailer with 33.7 million customer records exposed
- **Asahi Group Systems**: Japanese beer producer with up to 1.9 million individuals affected

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Targeting legitimate software distribution channels including browser extension stores and npm registry
- **Code Signing Key Theft**: Compromising developer signing certificates to distribute malicious updates through legitimate channels
- **Self-Replicating Malware**: Worm-like propagation through package dependencies and development environments
- **Social Engineering**: Long-term campaigns building trust before deploying malicious functionality
- **Cross-Site Scripting**: Exploiting web application vulnerabilities in industrial control systems
- **Malware-as-a-Service**: Professional malware distribution models targeting mobile platforms
- **Evil Twin WiFi Networks**: Creating rogue wireless access points to intercept traveler data

## Threat Actor Activities

- **ShadyPanda**: Seven-year browser extension campaign converting legitimate extensions into spyware, targeting over 4.3 million users with data theft and surveillance capabilities
- **North Korean APT Groups**: Continued flooding of npm registry with malicious packages as part of Contagious Interview campaign, deploying OtterCookie malware to compromise developer environments
- **Tomiris**: Government-focused threat actor shifting to public-service implants for stealthier command and control communications, targeting foreign ministries and intergovernmental organizations in Russia
- **Bloody Wolf**: Expanding Java-based NetSupport RAT attacks in Central Asian countries including Kyrgyzstan and Uzbekistan since June 2025
- **Albiriox Operators**: Malware-as-a-Service providers targeting 400+ Android applications with on-device fraud and screen manipulation capabilities