# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited across multiple platforms this week, with Apple patching two WebKit flaws and Chinese threat groups continuing exploitation of the React2Shell vulnerability. Ransomware operators are deploying new malware families while data breaches expose millions of records across various sectors. Multiple information stealers and browser extension compromise campaigns are targeting user credentials and cryptocurrency wallets, highlighting the evolving threat landscape affecting everyday software users rely on.

## Active Exploitation Details

### Apple WebKit Zero-Day Vulnerabilities
- **Description**: Two WebKit security flaws affecting Apple's Safari browser and other Apple platforms
- **Impact**: Attackers can achieve sophisticated attacks through browser exploitation
- **Status**: Actively exploited in the wild; Apple has released security updates for iOS, iPadOS, macOS, tvOS, watchOS, visionOS, and Safari

### Sierra Wireless AirLink ALEOS Router Vulnerability
- **Description**: High-severity flaw in Sierra Wireless AirLink ALEOS routers enabling remote code execution
- **Impact**: Attackers can achieve remote code execution on affected router systems
- **Status**: Actively exploited; added to CISA's Known Exploited Vulnerabilities catalog

### React2Shell Vulnerability
- **Description**: Maximum-severity remote code execution vulnerability being exploited by multiple Chinese hacking groups
- **Impact**: Remote code execution capabilities with proof-of-concept exploits containing WAF bypasses
- **Status**: Ongoing exploitation activity with attacks flooding the internet
- **CVE ID**: CVE-2025-55182

### FreePBX Critical Vulnerabilities
- **Description**: Multiple security vulnerabilities including SQL injection, file upload, and AUTHTYPE bypass flaws
- **Impact**: Authentication bypass and remote code execution under certain circumstances
- **Status**: Patches released for the open-source private branch exchange platform

## Affected Systems and Products

- **Apple Platforms**: iOS, iPadOS, macOS, tvOS, watchOS, visionOS, and Safari browser affected by WebKit vulnerabilities
- **Sierra Wireless Routers**: AirLink ALEOS router models vulnerable to remote code execution
- **FreePBX Systems**: Open-source private branch exchange platforms with multiple critical flaws
- **Chrome and Edge Browsers**: Extensions compromised in ShadyPanda campaign affecting millions of users
- **Enterprise Systems**: Windows 11 WSL users experiencing VPN networking failures after security updates
- **Message Queuing Services**: Microsoft MSMQ functionality broken by December 2025 security updates

## Attack Vectors and Techniques

- **Browser Extension Hijacking**: ShadyPanda campaign compromising popular Chrome and Edge extensions on massive scale
- **Malicious GitHub Repositories**: Fake OSINT and GPT utility repos distributing PyStoreRAT malware payloads
- **ISO Phishing Campaigns**: Phantom Stealer malware delivered via malicious ISO files targeting Russian finance sector
- **PayPal Subscription Abuse**: Legitimate PayPal emails containing fake purchase notifications through Customer service URL field manipulation
- **Memory-Based Evasion**: SantaStealer malware operating in memory to avoid file-based detection systems
- **Chrome Extension Interception**: Featured Chrome extension with 6 million users silently gathering AI chatbot prompts

## Threat Actor Activities

- **Chinese Hacking Groups**: Five additional Chinese groups linked to React2Shell exploitation attacks by Google's threat intelligence team
- **CyberVolk/GLORIAMIST**: Pro-Russian hacktivist group launching VolkLocker ransomware-as-a-service with implementation flaws allowing free decryption
- **RansomHouse**: Confirmed theft of 740,000 customer records from Japanese e-commerce giant Askul Corporation
- **ShinyHunters**: Extortion gang targeting PornHub after stealing Premium member activity data through Mixpanel breach
- **ShadyPanda Campaign**: Large-scale browser extension compromise affecting millions of users across Chrome and Edge platforms
- **SantaStealer Operators**: Malware-as-a-service offering advertised on Telegram and hacker forums for credential theft